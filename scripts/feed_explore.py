#!/usr/bin/env python3
"""Build the landing-feed "Explore" block: search + interactive topic mind map.

Deterministic, zero-LLM. Reads ai-radar/tags.json (+ each edition's ai-radar.md)
and injects, between the EXPLORE:START / EXPLORE:END markers in
ai-radar/index.html:
  - a search input + status line + clear button
  - a row of "popular" quick-filter chips (verticals + companies actually
    covered by the editions)
  - an inline-SVG topic mind map (hub -> one clickable branch per topic)
  - two <script type="application/json"> blobs:
      #radar-topics : {date: [full topic list]}   (drives the mind-map filter)
      #radar-index  : {date: "extra searchable keywords"}  (companies, verticals,
                       entities, and topic words mined from the edition, so
                       search finds them even when they're not on the card)

The search/filter behaviour lives in the page's main <script> (static).
Run whenever tags.json or an edition changes:  python3 scripts/feed_explore.py
Pass --debug to print per-keyword edition counts instead of writing the page.
"""
import json, html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RADAR = os.path.join(ROOT, "ai-radar")
TAGS = os.path.join(RADAR, "tags.json")
PAGE = os.path.join(RADAR, "index.html")

COLORS = {
    "EU AI Act": "#2b6fb0", "Agentic AI": "#6c63d6", "AI governance": "#0f8f7e",
    "Security & containment": "#c8452f", "MCP & agent standards": "#0d7a54",
    "Model pricing & commoditization": "#8659c4", "Open-weight models": "#c2551f",
    "ROI & adoption": "#b3760a", "Market & vendors": "#bd4f86",
    "Cost & compute": "#9a7d10", "Data & memory": "#2f7fb8",
}
LABELS = {
    "EU AI Act": "⚖️ EU AI Act", "Agentic AI": "🤖 Agentic AI",
    "AI governance": "📋 AI governance", "Security & containment": "🛡️ Security & containment",
    "MCP & agent standards": "🔌 MCP & agent standards",
    "Model pricing & commoditization": "🧩 Pricing & commoditization",
    "Open-weight models": "⚙️ Open-weight models", "ROI & adoption": "📈 ROI & adoption",
    "Market & vendors": "🏢 Market & vendors", "Cost & compute": "💰 Cost & compute",
    "Data & memory": "🧠 Data & memory",
}

# Verticals are detected OUTSIDE the boilerplate "C-Level Engagement — Questions
# by Sector" block (every edition lists all sectors there), so a vertical only
# tags an edition where it is discussed substantively.
VERTICALS = {
    "Financial services": ["financial service", "financial-service", "finance", "banking", "bank", "fintech", "insurance", "insurer"],
    "Healthcare": ["healthcare", "health care", "clinical", "life science", "patient", "pharma", "biotech"],
    "Manufacturing": ["manufacturing", "manufacturer", "industrial", "factory", "supply chain"],
    "Retail": ["retail", "consumer", "e-commerce", "ecommerce"],
    "Public sector": ["public sector", "government", "citizen", "defense", "defence"],
    "Legal / IP": ["trade secret", "intellectual property", "copyright", "patent"],
    "Energy": ["energy", "power grid", "datacenter", "data center", "electricity"],
}
# Companies / vendors / analysts / regulators — scanned across the whole edition.
COMPANIES = {
    "OpenAI": ["openai", "chatgpt", "gpt-5", "gpt5", "altman"],
    "Anthropic": ["anthropic", "claude", "opus", "cowork"],
    "Google": ["google", "gemini", "deepmind", "hassabis"],
    "Microsoft": ["microsoft", "azure", "copilot"],
    "NVIDIA": ["nvidia", "jensen huang", "huang"],
    "Amazon / AWS": ["amazon", "aws"],
    "Meta": ["meta"],
    "SAP": ["sap", "tabpfn"],
    "IBM": ["ibm"],
    "Oracle": ["oracle"],
    "Salesforce": ["salesforce"],
    "Kimi": ["kimi", "moonshot"],
    "DeepSeek": ["deepseek"],
    "MinIO": ["minio"],
    "Cognizant": ["cognizant"],
    "Apple": ["apple"],
    "Hugging Face": ["hugging face", "huggingface"],
    "Palantir": ["palantir"],
    "Elastic": ["elastic"],
    "DoorDash": ["doordash"],
    "HubSpot": ["hubspot"],
    "DevRev": ["devrev"],
    "CyberArk": ["cyberark"],
    "Rubrik": ["rubrik"],
    "Palo Alto": ["palo alto"],
    "Gartner": ["gartner"],
    "McKinsey": ["mckinsey"],
    "Forrester": ["forrester"],
    "IDC": ["idc"],
    "MIT": ["mit", "nanda"],
    "Stanford": ["stanford"],
    "Citi": ["citi"],
    "China": ["china", "chinese"],
    "Illinois": ["illinois"],
    "EU / Brussels": ["european commission", "brussels", "eu ai office", "ai office"],
}

# Chip order (only those actually covered by >=2 editions are shown, capped).
VERT_ORDER = ["Financial services", "Healthcare", "Manufacturing", "Retail",
              "Public sector", "Energy", "Legal / IP"]
VENDOR_ORDER = ["OpenAI", "Anthropic", "Google", "NVIDIA", "Kimi", "DeepSeek",
                "Microsoft", "Amazon / AWS", "Hugging Face", "Palantir", "Oracle",
                "IBM", "Cognizant", "Salesforce", "SAP", "Apple", "Meta", "MinIO"]
CHIP_CAP = 16

HX, HUB_W, HUB_H = 12, 150, 64
PX, PW, PH = 300, 320, 26
TOP, PITCH = 14, 33


def esc(s):
    return html.escape(s, quote=True)


def matched(text, aliases):
    hits = []
    for a in aliases:
        if " " in a or "-" in a:
            if a in text:
                hits.append(a)
        elif re.search(r"\b" + re.escape(a) + r"\b", text):
            hits.append(a)
    return hits


def strip_clevel(md):
    # drop the "C-Level Engagement — Questions by Sector" section (to next ## heading)
    return re.sub(r"(?ims)^##\s+[^\n]*c-?level engagement.*?(?=^##\s)", "", md)


def core_text(md):
    """The substantive framing only: executive summary + allegory + deep-dive.
    Drops the C-Level sector boilerplate and the Quotes/Numbers/So-what sections
    (which cite many orgs in passing), so a company/vertical tags an edition only
    when the edition is actually about it."""
    core = re.split(r"(?im)^##\s+5\b", md)[0]
    return strip_clevel(core)


def mine(date, headline, topics):
    """Return (index_tokens:set, vert_hits:set, comp_hits:set) for one edition."""
    path = os.path.join(RADAR, date, "ai-radar.md")
    body = ""
    if os.path.exists(path):
        body = open(path, encoding="utf-8").read()
    core = (headline + "\n" + core_text(body)).lower()
    tokens = set(t.lower() for t in topics)
    tokens.update(re.findall(r"[a-z0-9]+", headline.lower()))
    verts, comps = set(), set()
    for name, al in VERTICALS.items():
        if matched(core, al):
            verts.add(name)
            tokens.add(name.lower()); tokens.update(al)
    for name, al in COMPANIES.items():
        if matched(core, al):
            comps.add(name)
            tokens.add(name.lower()); tokens.update(al)
    return tokens, verts, comps


def build(vocab, editions, debug=False):
    by_date = {e["date"]: e["tags"] for e in editions}
    index, vcount, ccount = {}, {}, {}
    for e in editions:
        toks, verts, comps = mine(e["date"], e["headline"], e["tags"])
        index[e["date"]] = " ".join(sorted(toks))
        for v in verts:
            vcount[v] = vcount.get(v, 0) + 1
        for c in comps:
            ccount[c] = ccount.get(c, 0) + 1

    if debug:
        print("VERTICALS:", json.dumps(vcount, indent=1))
        print("COMPANIES:", json.dumps(dict(sorted(ccount.items(), key=lambda x: -x[1])), indent=1))
        return None, 0, 0

    # topic counts across all tags (topic filter matches any tag)
    counts = {}
    for e in editions:
        for t in e["tags"]:
            counts[t] = counts.get(t, 0) + 1
    vindex = {n: i for i, n in enumerate(vocab)}
    order = sorted(counts.keys(), key=lambda t: (-counts[t], vindex.get(t, 99)))

    # chips: verticals then vendors, in a stable preference order, each covered
    # by >=2 editions, capped — analysts/regulators are left to search/topic map.
    chips = []
    for v in VERT_ORDER:
        if vcount.get(v, 0) >= 2:
            chips.append((v, VERTICALS[v][0], vcount[v], "v"))
    for c in VENDOR_ORDER:
        if ccount.get(c, 0) >= 2:
            chips.append((c, COMPANIES[c][0], ccount[c], "c"))
    chips = chips[:CHIP_CAP]

    # ---- topic mind map ----
    n = len(order)
    cys = [TOP + i * PITCH + PH / 2 for i in range(n)]
    hy = (cys[0] + cys[-1]) / 2
    vb_w, vb_h = PX + PW + 16, round(cys[-1] + PH / 2 + 14)
    svg = [f'<svg viewBox="0 0 {vb_w} {vb_h}" xmlns="http://www.w3.org/2000/svg" '
           f'style="width:100%;min-width:560px;height:auto" role="group" '
           f'aria-label="Topic mind map — tap a branch to filter the feed to that topic.">']
    for cy, t in zip(cys, order):
        c = COLORS.get(t, "#8a8f98")
        svg.append(f'<path d="M{HX+HUB_W} {hy:.1f} C{HX+HUB_W+46} {hy:.1f} {PX-42} {cy:.1f} '
                   f'{PX} {cy:.1f}" fill="none" stroke="{c}" stroke-width="1.6" opacity="0.45"/>')
    svg.append(
        f'<rect x="{HX}" y="{hy-HUB_H/2:.1f}" width="{HUB_W}" height="{HUB_H}" rx="14" fill="#1a1a1e"/>'
        f'<text x="{HX+HUB_W/2:.0f}" y="{hy-9:.1f}" text-anchor="middle" font-size="10" font-weight="700" '
        f'letter-spacing="0.14em" fill="#9aa0a6" font-family="Inter,sans-serif">🧭 EXPLORE</text>'
        f'<text x="{HX+HUB_W/2:.0f}" y="{hy+8:.1f}" text-anchor="middle" font-size="15" font-weight="800" '
        f'fill="#f7f7f5" font-family="Inter,sans-serif">Topics</text>'
        f'<text x="{HX+HUB_W/2:.0f}" y="{hy+24:.1f}" text-anchor="middle" font-size="9.5" '
        f'fill="#9aa0a6" font-family="Inter,sans-serif">tap to filter</text>')
    for cy, t in zip(cys, order):
        c = COLORS.get(t, "#8a8f98")
        svg.append(
            f'<g class="mm-node" data-topic="{esc(t)}" tabindex="0" role="button" '
            f'aria-label="Filter the feed to the {counts[t]} editions tagged {esc(t)}">'
            f'<rect x="{PX}" y="{cy-PH/2:.1f}" width="{PW}" height="{PH}" rx="13" fill="#ffffff" stroke="{c}" stroke-width="1.5"/>'
            f'<circle cx="{PX+15}" cy="{cy:.1f}" r="4" fill="{c}"/>'
            f'<text x="{PX+28}" y="{cy+4:.1f}" font-size="12.5" font-weight="600" fill="#1a1a1e" font-family="Inter,sans-serif">{esc(LABELS.get(t,t))}</text>'
            f'<text class="mm-ct" x="{PX+PW-14}" y="{cy+4:.1f}" text-anchor="end" font-size="12" font-weight="800" fill="{c}" font-family="Inter,sans-serif">{counts[t]}</text>'
            f'</g>')
    svg.append("</svg>")
    svg = "\n".join(svg)

    # ---- chip row ----
    chip_html = "".join(
        f'<button type="button" class="chip" data-q="{esc(q)}" '
        f'title="{esc(("Vertical" if kind=="v" else "Company"))} · {n} editions">{esc(name)}</button>'
        for (name, q, n, kind) in chips)

    topics_blob = json.dumps(by_date, ensure_ascii=False, separators=(",", ":"))
    index_blob = json.dumps(index, ensure_ascii=False, separators=(",", ":"))
    total = len(editions)

    section = f"""<!-- EXPLORE:START (generated by scripts/feed_explore.py — do not hand-edit) -->
    <div class="explore" role="search">
      <div class="ex-field">
        <svg class="ex-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><line x1="20.5" y1="20.5" x2="16.5" y2="16.5"></line></svg>
        <label for="feed-search" class="sr-only">Search editions</label>
        <input id="feed-search" type="search" autocomplete="off" enterkeyhint="search" placeholder="Search {total} briefs — topic, company, vertical…">
        <kbd class="ex-kbd" aria-hidden="true">/</kbd>
        <button id="feed-clear-in" class="ex-xin" type="button" hidden aria-label="Clear search text">✕</button>
      </div>
      <div class="ex-quick">
        <span class="ex-lbl">Quick filters</span>
        <div class="chips">{chip_html}</div>
      </div>
      <div id="feed-status" class="ex-status" role="status" aria-live="polite" hidden>
        <span id="feed-count" class="ex-count"></span>
        <span id="feed-active" class="ex-active" hidden></span>
        <button id="feed-clear" class="ex-clearall" type="button">Clear all</button>
      </div>
      <details class="ex-map" open>
        <summary><span class="ex-map-t">🧭 Explore by topic</span><span class="ex-map-h">tap a branch to filter</span></summary>
        <div class="ex-map-body">
{svg}
        </div>
      </details>
    </div>
    <script type="application/json" id="radar-topics">{topics_blob}</script>
    <script type="application/json" id="radar-index">{index_blob}</script>
<!-- EXPLORE:END -->"""
    return section, total, n


def main():
    debug = "--debug" in sys.argv
    data = json.load(open(TAGS))
    section, total, ntopics = build(data["vocabulary"], data["editions"], debug=debug)
    if debug:
        return
    page = open(PAGE).read()
    if "<!-- EXPLORE:START" in page:
        page = re.sub(r"<!-- EXPLORE:START.*?<!-- EXPLORE:END -->", lambda m: section, page, flags=re.S)
    else:
        anchor = "    <!-- DAILY BRIEF UPDATE"
        page = page.replace(anchor, section + "\n" + anchor, 1)
    open(PAGE, "w").write(page)
    print(f"explore block: {total} editions, {ntopics} topics -> {PAGE}")


if __name__ == "__main__":
    main()
