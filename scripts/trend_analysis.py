#!/usr/bin/env python3
"""
AI Tech Radar — plain-language trends (zero-LLM, deterministic).

Reads ai-radar/tags.json (a hand-kept list of each edition's topics) and every
edition's ai-radar.md, then writes a friendly, non-technical trends page at
ai-radar/trends/index.html:

  1. The big picture   — a plain one-line summary + a few headline counts.
  2. Most-covered topics — a simple ranked bar (how many editions mention each).
  3. Heating up / cooling down — which topics rose or faded lately, in plain words.
  4. Topics that come up together — the topic pairs that appear side by side most.
  5. How solid are the numbers — figures checked against a named source, plus the
     figures repeated across the most editions.

Everything is counted directly from files already in this repo. No AI writes any
of it, and there are no live data feeds — it is arithmetic over a hand-kept list.
"""

import datetime as dt
import html
import json
import os
import re
import sys
from collections import defaultdict, Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RADAR_DIR = os.path.join(REPO_ROOT, "ai-radar")
TAGS_PATH = os.path.join(RADAR_DIR, "tags.json")
FACTS_PATH = os.path.join(RADAR_DIR, "verified_facts.json")
OUT_DIR = os.path.join(RADAR_DIR, "trends")

BAR = "#7f77dd"           # single hue for magnitude (most-covered topics)
RECENT_WINDOW = 12        # "lately" = the most recent N editions


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def esc(s):
    return html.escape(str(s), quote=True)


# --------------------------------------------------------------------------- #
# Counting                                                                     #
# --------------------------------------------------------------------------- #

def topic_totals(editions):
    c = Counter()
    for e in editions:
        for t in set(e["tags"]):
            c[t] += 1
    return c


def heating(editions):
    """Compare each topic's rate in the most recent editions vs. the earlier ones."""
    ordered = sorted(editions, key=lambda e: e["date"])
    if len(ordered) < RECENT_WINDOW + 4:
        return None
    recent = ordered[-RECENT_WINDOW:]
    earlier = ordered[:-RECENT_WINDOW]
    rc, ec = Counter(), Counter()
    for e in recent:
        for t in set(e["tags"]):
            rc[t] += 1
    for e in earlier:
        for t in set(e["tags"]):
            ec[t] += 1
    rows = []
    for t in set(list(rc) + list(ec)):
        r_rate = rc[t] / len(recent)
        e_rate = ec[t] / len(earlier)
        rows.append({
            "tag": t, "recent": rc[t], "recent_n": len(recent),
            "earlier": ec[t], "earlier_n": len(earlier),
            "delta": r_rate - e_rate,
        })
    rows.sort(key=lambda x: x["delta"], reverse=True)
    return rows


def top_pairs(editions, k=6):
    pair = Counter()
    for e in editions:
        tags = sorted(set(e["tags"]))
        for i, a in enumerate(tags):
            for b in tags[i + 1:]:
                pair[(a, b)] += 1
    return [(a, b, n) for (a, b), n in pair.most_common(k) if n >= 2]


# --------------------------------------------------------------------------- #
# The numbers we quote: check each verified figure against the editions        #
# --------------------------------------------------------------------------- #

def load_edition_text(date):
    path = os.path.join(RADAR_DIR, date, "ai-radar.md")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def verified_with_counts(editions, facts):
    """For each hand-verified figure, count how many editions repeat it.

    Plain-language corroboration: a figure matched to a named source AND repeated
    across many editions is more trustworthy than one mentioned once. Matching is
    a simple case-insensitive substring test against the fact's match_patterns.
    """
    texts = [load_edition_text(e["date"]).lower() for e in editions]
    out = []
    for f in facts:
        pats = [p.lower() for p in f.get("match_patterns", [])]
        n = sum(1 for t in texts if any(p in t for p in pats)) if pats else 0
        out.append({"claim": f["claim"], "url": f["source_url"],
                    "source": f["source_title"], "n": n})
    out.sort(key=lambda x: -x["n"])
    return out


# --------------------------------------------------------------------------- #
# Render                                                                       #
# --------------------------------------------------------------------------- #

CSS = """
  :root{--bg:#0d1117;--panel:#161b22;--panel2:#1c2330;--line:#2a3240;--ink:#e8edf3;
    --muted:#9aa7b6;--soft:#c3ccd8;--accent:#7f77dd;--teal:#1d9e75;--coral:#d85a30;--max:820px;--radius:14px}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:linear-gradient(180deg,#0b0f15,#0d1117);color:var(--ink);
    font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  a{color:#9d96f0;text-decoration:none} a:hover{text-decoration:underline}
  .wrap{max-width:var(--max);margin:0 auto;padding:0 20px}
  nav.toc{position:sticky;top:0;background:rgba(13,17,23,.82);backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line);z-index:5;font-size:13px}
  nav.toc .wrap{display:flex;gap:18px;flex-wrap:wrap;padding:12px 20px}
  nav.toc a{color:var(--muted)} nav.toc a:hover{color:#fff;text-decoration:none}
  nav.toc .here{color:#fff;font-weight:600}
  header.top{padding:40px 0 22px;border-bottom:1px solid var(--line);margin-bottom:24px}
  .kicker{letter-spacing:.18em;text-transform:uppercase;font-size:12px;color:var(--accent);font-weight:600}
  h1{font-size:34px;line-height:1.12;margin:.3em 0 .12em}
  .sub{color:var(--soft);max-width:66ch;font-size:17px}
  section{margin:40px 0}
  h2{font-size:19px;margin:0 0 6px}
  .lead{color:var(--soft);font-size:15px;margin:0 0 14px;max-width:70ch}
  .card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;margin:14px 0}
  /* stat tiles */
  .stat{display:flex;gap:14px;flex-wrap:wrap;margin:18px 0 6px}
  .kpi{flex:1 1 150px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
  .kpi .n{font-size:26px;font-weight:800;color:#fff;line-height:1.1}
  .kpi .l{font-size:12.5px;color:var(--muted);margin-top:4px}
  /* ranked bars */
  .bars{margin:6px 0}
  .bar{display:grid;grid-template-columns:190px 1fr auto;align-items:center;gap:12px;padding:7px 0}
  .bar .lab{color:var(--soft);font-size:14px;text-align:right;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .bar .track{background:var(--panel2);border-radius:7px;height:20px;overflow:hidden}
  .bar .fill{height:100%;background:var(--accent);border-radius:7px}
  .bar .val{color:#fff;font-weight:700;font-size:14px;font-variant-numeric:tabular-nums;min-width:2.4em;text-align:right}
  @media(max-width:560px){.bar{grid-template-columns:130px 1fr auto}.bar .lab{font-size:12.5px}}
  /* heating up */
  .move{display:flex;gap:12px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--line)}
  .move:last-child{border-bottom:0}
  .move .ar{font-weight:800;font-size:15px;width:1.4em;flex:none}
  .move .up{color:var(--teal)} .move .dn{color:var(--coral)}
  .move .t{color:#fff;font-weight:600;min-width:170px}
  .move .d{color:var(--muted);font-size:14px}
  /* pairs */
  .pairs{display:flex;flex-direction:column;gap:0}
  .pairrow{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px solid var(--line)}
  .pairrow:last-child{border-bottom:0}
  .pairrow .p{color:#fff}
  .pairrow .p b{color:var(--soft);font-weight:600}
  .pairrow .c{color:var(--muted);font-size:14px;white-space:nowrap}
  /* numbers */
  table{width:100%;border-collapse:collapse;margin:8px 0;font-size:14px}
  th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
  th{color:var(--muted);font-weight:600;text-transform:uppercase;font-size:11px;letter-spacing:.06em}
  .chk{color:var(--teal);font-weight:700;white-space:nowrap}
  .seen{color:var(--soft);white-space:nowrap;font-variant-numeric:tabular-nums}
  .note{color:var(--muted);font-size:13px}
  footer{border-top:1px solid var(--line);margin-top:44px;padding:24px 0 50px;color:var(--muted);font-size:13px}
  @media(max-width:600px){
    header.top{padding:28px 0 18px}
    h1{font-size:26px} h2{font-size:18px} .sub{font-size:15.5px} .lead{font-size:14.5px}
    .kpi .n{font-size:22px}
    .bar{grid-template-columns:1fr auto;gap:4px 10px;padding:9px 0}
    .bar .lab{grid-column:1 / -1;text-align:left;white-space:normal}
    .move{flex-wrap:wrap;gap:2px 10px}
    .move .t{min-width:0}
    .pairrow{flex-direction:column;gap:2px}
    table{font-size:13px} th,td{padding:8px 8px}
  }
"""


def render_bars(totals, n_editions):
    if not totals:
        return '<p class="note">No topics tracked yet.</p>'
    top = totals.most_common()
    mx = top[0][1]
    rows = []
    for tag, cnt in top:
        pct = round(cnt / mx * 100)
        share = round(cnt / n_editions * 100)
        rows.append(
            f'<div class="bar"><div class="lab" title="{esc(tag)}">{esc(tag)}</div>'
            f'<div class="track"><div class="fill" style="width:{pct}%"></div></div>'
            f'<div class="val" title="in {cnt} of {n_editions} editions ({share}%)">{cnt}</div></div>'
        )
    return f'<div class="bars">{"".join(rows)}</div>'


def render_heating(rows):
    if not rows:
        return '<p class="note">Not enough editions yet to compare recent vs. earlier coverage.</p>'
    risers = [r for r in rows if r["delta"] > 0.001][:3]
    coolers = [r for r in rows if r["delta"] < -0.001][-3:][::-1]
    out = []
    for r in risers:
        out.append(
            f'<div class="move"><span class="ar up">▲</span>'
            f'<span class="t">{esc(r["tag"])}</span>'
            f'<span class="d">in {r["recent"]} of the last {r["recent_n"]} editions '
            f'(was {r["earlier"]} of the earlier {r["earlier_n"]})</span></div>'
        )
    for r in coolers:
        out.append(
            f'<div class="move"><span class="ar dn">▼</span>'
            f'<span class="t">{esc(r["tag"])}</span>'
            f'<span class="d">in {r["recent"]} of the last {r["recent_n"]} editions '
            f'(was {r["earlier"]} of the earlier {r["earlier_n"]})</span></div>'
        )
    return "".join(out)


def render_pairs(pairs):
    if not pairs:
        return '<p class="note">No repeated topic pairings yet.</p>'
    rows = []
    for a, b, n in pairs:
        rows.append(
            f'<div class="pairrow"><span class="p"><b>{esc(a)}</b> + <b>{esc(b)}</b></span>'
            f'<span class="c">together in {n} editions</span></div>'
        )
    return f'<div class="pairs">{"".join(rows)}</div>'


def render_numbers(rows):
    if not rows:
        return '<p class="note">No verified figures yet.</p>'
    def label(nn):
        return f'{nn} edition' + ("s" if nn != 1 else "")
    trs = []
    for r in rows:
        seen = (f'<span class="chk">{label(r["n"])}</span>' if r["n"] >= 3
                else (f'<span class="seen">{label(r["n"])}</span>' if r["n"] > 0
                      else '<span class="note">—</span>'))
        trs.append(
            f'<tr><td>{esc(r["claim"])}</td>'
            f'<td><a href="{esc(r["url"])}">{esc(r["source"])}</a></td>'
            f'<td>{seen}</td></tr>'
        )
    return (
        '<table><tr><th>Figure we\'ve checked</th><th>Source</th><th>Repeated in</th></tr>'
        + "".join(trs) + "</table>"
    )


def render_page(editions, totals, heat, pairs, numbers, generated_at):
    n = len(editions)
    dates = sorted(e["date"] for e in editions)
    span = f"{dates[0]} to {dates[-1]}"
    top_tag, top_cnt = totals.most_common(1)[0]
    top_share = round(top_cnt / n * 100)
    top_number = numbers[0]["claim"] if numbers and numbers[0]["n"] > 0 else None
    summary = (
        f"Across <strong>{n} editions</strong> ({esc(span)}), the topic that came up most was "
        f"<strong>{esc(top_tag)}</strong> — in {top_cnt} of them ({top_share}%)."
    )
    if top_number:
        summary += f" The figure repeated across the most editions: <strong>{esc(top_number)}</strong>."

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Tech Radar — Trends</title>
<meta name="description" content="What the AI Tech Radar is tracking, in plain language: the topics that come up most, what's heating up or cooling down, which topics show up together, and how well-checked the numbers we quote are. Counted by hand from every edition — no AI, no live data feeds.">
<style>{CSS}</style>
</head>
<body>
<nav class="toc"><div class="wrap">
  <a href="../index.html">← Feed</a>
  <a href="../archive/index.html">Archive</a>
  <a href="../wrap-ups/2026-07/index.html">July wrap-up</a>
  <a class="here">Trends</a>
  <a href="../feed.xml">RSS</a>
</div></nav>

<div class="wrap">
<header class="top">
  <div class="kicker">📈 AI Tech Radar · Trends</div>
  <h1>What the radar keeps talking about</h1>
  <p class="sub">The themes that show up most across every edition, what's rising or fading, and how well-checked the numbers we quote are. It's all simple counting from a hand-kept list — no AI writes this page, and nothing here is a live data feed.</p>
</header>

<section id="bigpicture">
<h2>The big picture</h2>
<p class="lead">{summary}</p>
<div class="stat">
  <div class="kpi"><div class="n">{n}</div><div class="l">editions tracked</div></div>
  <div class="kpi"><div class="n">{len(totals)}</div><div class="l">topics followed</div></div>
  <div class="kpi"><div class="n">{esc(top_tag)}</div><div class="l">most-covered topic ({top_cnt}×)</div></div>
</div>
</section>

<section id="topics">
<h2>Most-covered topics</h2>
<p class="lead">How many editions mention each topic. Longer bar = the radar returns to it more often.</p>
<div class="card">{render_bars(totals, n)}</div>
</section>

<section id="heating">
<h2>Heating up &amp; cooling down</h2>
<p class="lead">Comparing the last {RECENT_WINDOW} editions with the ones before them — where the conversation is moving.</p>
<div class="card">{render_heating(heat)}</div>
</section>

<section id="together">
<h2>Topics that come up together</h2>
<p class="lead">The pairs of themes that most often show up in the same edition — usually because they're really one story.</p>
<div class="card">{render_pairs(pairs)}</div>
</section>

<section id="numbers">
<h2>How solid are the numbers?</h2>
<p class="lead">Every figure below was matched by hand to a real, published source. The last column shows how many editions repeat it — a number quoted across many days of independent research is more trustworthy than one mentioned once.</p>
<div class="card">
{render_numbers(numbers)}
</div>
</section>

<footer>
<p>Counted by hand from <a href="../tags.json">a simple list of each edition's topics</a> and each edition's brief — no AI writing this page, no live data feeds. Last updated {esc(generated_at)}.</p>
<p><a href="../index.html">← Full feed</a> · <a href="../archive/index.html">Archive</a> · <a href="../wrap-ups/2026-07/index.html">July wrap-up</a> · <a href="../feed.xml">RSS</a></p>
</footer>
</div>
</body>
</html>
"""


def main():
    editions = load_json(TAGS_PATH, {"editions": []})["editions"]
    editions = sorted(editions, key=lambda e: e["date"])
    facts = load_json(FACTS_PATH, {"facts": []})["facts"]
    if not editions:
        print("No editions in tags.json yet; nothing to analyze.")
        return

    totals = topic_totals(editions)
    heat = heating(editions)
    pairs = top_pairs(editions)
    numbers = verified_with_counts(editions, facts)

    os.makedirs(OUT_DIR, exist_ok=True)
    generated_at = dt.datetime.utcnow().strftime("%Y-%m-%d")
    page = render_page(editions, totals, heat, pairs, numbers, generated_at)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)

    repeated = sum(1 for x in numbers if x["n"] > 0)
    print(f"Wrote {os.path.join(OUT_DIR, 'index.html')} "
          f"({len(editions)} editions, {len(totals)} topics, "
          f"{len(pairs)} pairs, {len(numbers)} verified figures, {repeated} repeated).")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
