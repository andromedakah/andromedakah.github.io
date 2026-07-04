#!/usr/bin/env python3
"""
AI Tech Radar — deterministic trend analysis (zero-LLM).

Reads ai-radar/tags.json (hand-maintained tag index, one entry per published
edition) and regenerates a static trends page at ai-radar/trends/index.html:

  1. Tag frequency per edition + a stacked bar chart (SVG, hand-computed).
  2. Week-over-week velocity per tag: (count_this_week - count_last_week) / count_last_week.
  3. A tag co-occurrence matrix (which topics get covered together).
  4. A fact spot-check: regex-extracts numeric claims from each edition's
     ai-radar.md and checks them against ai-radar/verified_facts.json, a
     small hand-curated allowlist of facts with a real source URL. Anything
     not in the allowlist is reported as UNCONFIRMED (not false) -- this is
     a spot-check against a finite local list, not exhaustive fact-checking,
     and it makes zero network or LLM calls.

No LLM calls, no network calls, no generative summaries. Everything here is
computed directly from tags.json / verified_facts.json / the edition
markdown files already committed to this repo.
"""

import datetime as dt
import html
import json
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RADAR_DIR = os.path.join(REPO_ROOT, "ai-radar")
TAGS_PATH = os.path.join(RADAR_DIR, "tags.json")
FACTS_PATH = os.path.join(RADAR_DIR, "verified_facts.json")
OUT_DIR = os.path.join(RADAR_DIR, "trends")

TAG_COLORS = [
    "#7f77dd", "#1d9e75", "#d85a30", "#ef9f27", "#378add",
    "#c3577a", "#5aa7a0", "#a08b5c", "#8f7fe0", "#4fa3d1",
]

NUMERIC_CLAIM_RE = re.compile(
    r"[^.\n]{0,60}(?:\$?\d[\d,.]*\s?(?:%|percent|x|×|B|M|K|billion|million))[^.\n]{0,60}",
    re.IGNORECASE,
)


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def iso_week(date_str):
    d = dt.date.fromisoformat(date_str)
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


# --------------------------------------------------------------------------- #
# 1-2. Tag frequency + velocity                                               #
# --------------------------------------------------------------------------- #

def compute_tag_stats(editions):
    all_tags = []
    seen = set()
    for e in editions:
        for tag in e["tags"]:
            if tag not in seen:
                seen.add(tag)
                all_tags.append(tag)

    per_edition_counts = [
        {"date": e["date"], "headline": e.get("headline", ""), "tags": e["tags"]}
        for e in editions
    ]

    week_counts = defaultdict(lambda: defaultdict(int))
    for e in editions:
        wk = iso_week(e["date"])
        for tag in e["tags"]:
            week_counts[tag][wk] += 1

    velocity = {}
    for tag, weeks in week_counts.items():
        ordered_weeks = sorted(weeks.keys())
        if len(ordered_weeks) < 2:
            velocity[tag] = None
            continue
        prev, last = weeks[ordered_weeks[-2]], weeks[ordered_weeks[-1]]
        velocity[tag] = None if prev == 0 else round((last - prev) / prev * 100, 1)

    return all_tags, per_edition_counts, week_counts, velocity


def compute_cooccurrence(editions, all_tags):
    matrix = {a: {b: 0 for b in all_tags} for a in all_tags}
    for e in editions:
        tags = e["tags"]
        for i, a in enumerate(tags):
            for b in tags[i + 1:]:
                matrix[a][b] += 1
                matrix[b][a] += 1
    return matrix


# --------------------------------------------------------------------------- #
# 3. Fact spot-check                                                          #
# --------------------------------------------------------------------------- #

def load_edition_text(date):
    path = os.path.join(RADAR_DIR, date, "ai-radar.md")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def spot_check_facts(editions, facts):
    results = []
    for e in editions:
        text = load_edition_text(e["date"])
        if not text:
            continue
        claims = {m.group(0).strip() for m in NUMERIC_CLAIM_RE.finditer(text)}
        for claim_snippet in claims:
            snippet_lower = claim_snippet.lower()
            matched = None
            for fact in facts:
                if any(p.lower() in snippet_lower for p in fact["match_patterns"]):
                    matched = fact
                    break
            results.append({
                "date": e["date"],
                "snippet": claim_snippet,
                "status": "confirmed" if matched else "unconfirmed",
                "fact": matched,
            })
    return results


# --------------------------------------------------------------------------- #
# 4. Render                                                                    #
# --------------------------------------------------------------------------- #

CSS = """
  :root{--bg:#0d1117;--panel:#161b22;--panel2:#1c2330;--line:#2a3240;--ink:#e8edf3;
    --muted:#9aa7b6;--soft:#c3ccd8;--accent:#7f77dd;--teal:#1d9e75;--max:860px;--radius:14px;}
  *{box-sizing:border-box}
  body{margin:0;background:linear-gradient(180deg,#0b0f15,#0d1117);color:var(--ink);
    font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .wrap{max-width:var(--max);margin:0 auto;padding:0 20px}
  header.top{padding:38px 0 22px;border-bottom:1px solid var(--line);margin-bottom:30px}
  .kicker{letter-spacing:.18em;text-transform:uppercase;font-size:12px;color:var(--accent);font-weight:600}
  h1{font-size:32px;line-height:1.15;margin:.35em 0 .15em}
  .sub{color:var(--soft);max-width:70ch}
  section{margin:42px 0}
  h2{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
    border-bottom:1px solid var(--line);padding-bottom:8px;margin:0 0 18px}
  .card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:22px 24px;margin:16px 0}
  a{color:#9d96f0;text-decoration:none} a:hover{text-decoration:underline}
  table{width:100%;border-collapse:collapse;margin:14px 0;font-size:14px}
  th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}
  th{color:var(--muted);font-weight:600;text-transform:uppercase;font-size:11px;letter-spacing:.08em}
  .up{color:var(--teal);font-weight:700} .down{color:#d85a30;font-weight:700} .flat{color:var(--muted)}
  .legend{display:flex;gap:14px;flex-wrap:wrap;margin-top:10px;font-size:13px;color:var(--muted)}
  .legend span{display:inline-flex;align-items:center;gap:6px}
  .dot{width:11px;height:11px;border-radius:3px;display:inline-block}
  .matrix td, .matrix th{text-align:center;padding:6px}
  .matrix .rowlabel{text-align:left;color:var(--soft)}
  .cell0{background:transparent}
  .status-confirmed{color:var(--teal);font-weight:600}
  .status-unconfirmed{color:#ef9f27;font-weight:600}
  .note{color:var(--muted);font-size:13px}
  footer{border-top:1px solid var(--line);margin-top:50px;padding:26px 0 50px;color:var(--muted);font-size:13px}
"""


def render_bar_chart(per_edition_counts, all_tags):
    color_of = {tag: TAG_COLORS[i % len(TAG_COLORS)] for i, tag in enumerate(all_tags)}
    n = len(per_edition_counts)
    bar_w, gap, chart_h, top_pad = 70, 30, 220, 10
    width = max(n * (bar_w + gap) + gap, 300)

    bars = []
    for i, e in enumerate(per_edition_counts):
        x = gap + i * (bar_w + gap)
        tags = e["tags"]
        unit_h = (chart_h - top_pad) / max(len(tags), 1)
        y = chart_h
        for tag in tags:
            y -= unit_h
            bars.append(
                f'<rect x="{x}" y="{y:.1f}" width="{bar_w}" height="{unit_h:.1f}" '
                f'fill="{color_of[tag]}" stroke="#0d1117" stroke-width="1">'
                f'<title>{html.escape(tag)} — {html.escape(e["date"])}</title></rect>'
            )
        bars.append(
            f'<text x="{x + bar_w / 2}" y="{chart_h + 18}" text-anchor="middle" '
            f'font-size="11" fill="#9aa7b6" font-family="sans-serif">{html.escape(e["date"][5:])}</text>'
        )

    legend = "".join(
        f'<span><i class="dot" style="background:{color_of[tag]}"></i>{html.escape(tag)}</span>'
        for tag in all_tags
    )
    return f"""<div class="card">
<svg viewBox="0 0 {width} {chart_h + 30}" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="Tag frequency per edition" style="max-width:100%;height:auto">
{''.join(bars)}
</svg>
<div class="legend">{legend}</div>
</div>"""


def render_velocity_table(velocity):
    rows = []
    for tag in sorted(velocity, key=lambda t: (velocity[t] is None, -(velocity[t] or 0))):
        v = velocity[tag]
        if v is None:
            cell = '<span class="flat">— (only one week of data so far)</span>'
        elif v > 0:
            cell = f'<span class="up">▲ +{v}%</span>'
        elif v < 0:
            cell = f'<span class="down">▼ {v}%</span>'
        else:
            cell = '<span class="flat">flat</span>'
        rows.append(f"<tr><td>{html.escape(tag)}</td><td>{cell}</td></tr>")
    return f"""<table><tr><th>Tag</th><th>Week-over-week velocity</th></tr>{''.join(rows)}</table>"""


def render_matrix(matrix, all_tags):
    if len(all_tags) < 2:
        return '<p class="note">Not enough distinct tags yet to compute co-occurrence.</p>'
    max_v = max((matrix[a][b] for a in all_tags for b in all_tags if a != b), default=0)
    header = "".join(f'<th>{html.escape(t)}</th>' for t in all_tags)
    rows = []
    for a in all_tags:
        cells = []
        for b in all_tags:
            if a == b:
                cells.append('<td class="cell0">·</td>')
                continue
            v = matrix[a][b]
            if v == 0 or max_v == 0:
                cells.append('<td class="cell0">0</td>')
            else:
                alpha = 0.15 + 0.65 * (v / max_v)
                cells.append(f'<td style="background:rgba(127,119,221,{alpha:.2f})">{v}</td>')
        rows.append(f'<tr><td class="rowlabel">{html.escape(a)}</td>{"".join(cells)}</tr>')
    return f"""<div style="overflow-x:auto"><table class="matrix"><tr><th></th>{header}</tr>{''.join(rows)}</table></div>"""


def render_facts(facts_checked):
    if not facts_checked:
        return '<p class="note">No edition markdown found to spot-check yet.</p>'
    rows = []
    for r in facts_checked:
        if r["status"] == "confirmed":
            f = r["fact"]
            detail = f'<a href="{html.escape(f["source_url"])}">{html.escape(f["source_title"])}</a>'
            status = '<span class="status-confirmed">CONFIRMED</span>'
        else:
            detail = '<span class="note">not in local allowlist</span>'
            status = '<span class="status-unconfirmed">UNCONFIRMED</span>'
        rows.append(
            f'<tr><td>{html.escape(r["date"])}</td><td>{html.escape(r["snippet"])}</td>'
            f'<td>{status}</td><td>{detail}</td></tr>'
        )
    return f"""<table><tr><th>Edition</th><th>Claim (extracted)</th><th>Status</th><th>Source</th></tr>{''.join(rows)}</table>"""


def render_page(all_tags, per_edition_counts, velocity, matrix, facts_checked, generated_at):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Tech Radar — Trends</title>
<meta name="description" content="Deterministic trend analysis of the AI Tech Radar: tag frequency, week-over-week velocity, topic co-occurrence, and a fact spot-check. No LLM, no generative summaries.">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <div class="kicker">📈 AI Tech Radar · Trends</div>
  <h1>Trend Analysis</h1>
  <p class="sub">Computed directly from <code>ai-radar/tags.json</code> and each edition's <code>ai-radar.md</code> —
  no LLM calls, no generative summaries. Regenerated by <code>scripts/trend_analysis.py</code>
  as part of the daily build.</p>
</header>

<section id="frequency">
<h2>Tag frequency per edition</h2>
{render_bar_chart(per_edition_counts, all_tags)}
</section>

<section id="velocity">
<h2>Week-over-week velocity</h2>
<p class="note">Velocity = (count this ISO week − count previous week the tag appeared) / previous week's count.</p>
<div class="card">{render_velocity_table(velocity)}</div>
</section>

<section id="cooccurrence">
<h2>Topic co-occurrence</h2>
<p class="note">How many editions mentioned both tags together. Darker = more frequent pairing.</p>
<div class="card">{render_matrix(matrix, all_tags)}</div>
</section>

<section id="factcheck">
<h2>Fact spot-check</h2>
<p class="note">Numeric claims extracted from each edition via regex, checked against a small
hand-curated allowlist in <code>ai-radar/verified_facts.json</code>. This is a spot-check against
a finite local list, not exhaustive fact-checking — UNCONFIRMED means "not in the allowlist yet",
not "false".</p>
<div class="card">{render_facts(facts_checked)}</div>
</section>

<footer>
<p>Generated {html.escape(generated_at)} · <a href="../index.html">← all editions</a> · <a href="../feed.xml">RSS</a></p>
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

    all_tags, per_edition_counts, week_counts, velocity = compute_tag_stats(editions)
    matrix = compute_cooccurrence(editions, all_tags)
    facts_checked = spot_check_facts(editions, facts)

    os.makedirs(OUT_DIR, exist_ok=True)
    generated_at = dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    page = render_page(all_tags, per_edition_counts, velocity, matrix, facts_checked, generated_at)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)

    print(f"Wrote {os.path.join(OUT_DIR, 'index.html')} "
          f"({len(editions)} editions, {len(all_tags)} tags, {len(facts_checked)} claims checked).")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
