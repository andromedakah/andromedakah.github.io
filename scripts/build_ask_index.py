#!/usr/bin/env python3
"""Build the retrieval index for the "Ask the Radar" page.

Reads every edition's ai-radar/<YYYY-MM-DD>/ai-radar.md, splits it into
passages (paragraphs, list items and flattened table rows) tagged with the
edition date, headline and section, strips Markdown, and writes a single
JSON the static Ask page loads and searches client-side (BM25). Also folds
in the owner-verified facts from verified_facts.json.

No server, no API key, no LLM at query time — the answer is composed in the
browser from the indexed brief text, with citations back to each edition.

Deterministic and idempotent — re-run it whenever a new edition ships:

    python3 scripts/build_ask_index.py
"""
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RADAR = os.path.join(ROOT, "ai-radar")
OUT = os.path.join(RADAR, "ask", "index.json")
FACTS = os.path.join(RADAR, "verified_facts.json")
TAGS = os.path.join(RADAR, "tags.json")


def load_headlines():
    """Authoritative per-edition titles from tags.json (falls back to parsed)."""
    out = {}
    try:
        for e in json.load(open(TAGS, encoding="utf-8")).get("editions", []):
            if e.get("date") and e.get("headline"):
                out[e["date"]] = e["headline"]
    except Exception:
        pass
    return out

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")        # [text](url) -> text
EMPH_RE = re.compile(r"[*_`>#]+")                      # markdown emphasis / heading marks
WS_RE = re.compile(r"\s+")

# Section weights: how much a passage's home section is worth for factual Q&A.
SECTION_WEIGHT = {
    "header": 1.20,
    "executive summary": 1.30,
    "numbers to quote in a meeting": 1.30,
    "technical deep-dive": 1.15,
    "quotes that catch the eye": 1.10,
    "c-level engagement": 1.05,
    "so what": 1.10,
    "allegory of the day": 0.70,
}


def section_key(title):
    t = title.lower()
    for k in SECTION_WEIGHT:
        if k in t:
            return k
    # strip a leading "n · " numbering to match on the words
    t2 = re.sub(r"^\s*\d+\s*[·.\-]\s*", "", t)
    for k in SECTION_WEIGHT:
        if k in t2:
            return k
    return "body"


def clean(text):
    text = LINK_RE.sub(r"\1", text)
    text = text.replace("|", " ").replace("`", "")
    text = EMPH_RE.sub("", text)
    text = WS_RE.sub(" ", text).strip()
    return text


def is_refrain(text):
    """The long allegory 'litany' paragraphs repeat near-verbatim across
    editions (the model is a rented stove; the knowledge is the larder; …).
    They add bulk and near-duplicate noise, so drop the worst offenders."""
    low = text.lower()
    return low.count(" is why ") >= 4 or ("rented stove" in low and "the larder" in low and len(text) > 700)


def parse_md(path, date):
    lines = open(path, encoding="utf-8").read().splitlines()
    headline = date
    section = "header"
    in_fence = False
    buf = []
    passages = []

    def emit(txt):
        txt = clean(txt)
        if len(txt) < 45 or is_refrain(txt):
            return
        if len(txt) > 1000:
            txt = txt[:997].rsplit(" ", 1)[0] + "…"
        passages.append({"s": section, "t": txt})

    def flush():
        if not buf:
            return
        raw = " ".join(buf).strip()
        buf.clear()
        emit(raw)

    def table_row(s):
        """One Markdown table row -> a clean passage, or None to skip."""
        cells = [c.strip() for c in s.strip().strip("|").split("|")]
        joined = " ".join(cells)
        if set(joined.replace("-", "").replace(":", "").strip()) <= set(" "):
            return None  # separator row |---|---|
        if [c.lower() for c in cells] in (["metric", "value", "source"], ["", "", ""]):
            return None  # header row
        return " — ".join(c for c in cells if c)

    for ln in lines:
        s = ln.rstrip()
        if s.strip().startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if s.startswith("# "):
            flush()
            title = clean(s[2:])
            # "🗓️ AI Tech Radar — The Foundation" -> "The Foundation"
            m = re.search(r"—\s*(.+)$", title)
            headline = (m.group(1).strip() if m else title) or date
            section = "header"
            continue
        if s.startswith("## ") or s.startswith("### "):
            flush()
            section = clean(s.lstrip("#").strip())
            continue
        if s.strip().startswith("|"):
            flush()
            row = table_row(s)
            if row:
                emit(row)
            continue
        if not s.strip():
            flush()
            continue
        buf.append(s.strip())
    flush()

    # attach display section label + weight
    out = []
    seen = set()
    for p in passages:
        key = p["t"][:90].lower()
        if key in seen:
            continue
        seen.add(key)
        w = SECTION_WEIGHT.get(section_key(p["s"]), 1.0)
        out.append({"s": p["s"], "t": p["t"], "w": round(w, 2)})
    return headline, out


def main():
    dates = sorted(
        d for d in os.listdir(RADAR)
        if DATE_RE.match(d) and os.path.isfile(os.path.join(RADAR, d, "ai-radar.md"))
    )
    headlines = load_headlines()
    editions = []
    passages = []
    for date in dates:
        md = os.path.join(RADAR, date, "ai-radar.md")
        parsed_headline, ps = parse_md(md, date)
        headline = headlines.get(date) or parsed_headline
        url = f"../{date}/index.html"
        editions.append({"d": date, "h": headline, "u": url})
        for i, p in enumerate(ps):
            passages.append({
                "d": date, "h": headline, "u": url,
                "s": p["s"], "w": p["w"], "t": p["t"],
            })

    facts = []
    if os.path.exists(FACTS):
        try:
            for f in json.load(open(FACTS, encoding="utf-8")).get("facts", []):
                facts.append({
                    "claim": f.get("claim", ""),
                    "source_title": f.get("source_title", ""),
                    "source_url": f.get("source_url", ""),
                })
        except Exception:
            pass

    built = dates[-1] if dates else ""
    data = {
        "built": built,
        "editions": editions,
        "passages": passages,
        "facts": facts,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(OUT)
    print(f"ask index: {len(editions)} editions, {len(passages)} passages, "
          f"{len(facts)} verified facts -> {OUT} ({size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
