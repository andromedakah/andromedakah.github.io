#!/usr/bin/env python3
"""Build the archive topic mind map.

Deterministic, zero-LLM. Reads ai-radar/tags.json, assigns every edition to its
PRIMARY topic (the first tag — the owner orders tags lead-first), and emits a
self-contained inline-SVG mind map: a central hub -> one branch per topic ->
one clickable leaf per daily edition. Injects the result into
ai-radar/archive/index.html between the MINDMAP:START / MINDMAP:END markers
(inserting the section after </header> if the markers are absent).

Run whenever tags.json changes (e.g. after a new edition ships):
    python3 scripts/archive_mindmap.py
"""
import json, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAGS = os.path.join(ROOT, "ai-radar", "tags.json")
ARCHIVE = os.path.join(ROOT, "ai-radar", "archive", "index.html")

# One distinct, dark-background-legible colour per vocabulary topic.
COLORS = {
    "EU AI Act": "#378add",
    "Agentic AI": "#7f77dd",
    "AI governance": "#4db6a4",
    "Security & containment": "#e0645f",
    "MCP & agent standards": "#1d9e75",
    "Model pricing & commoditization": "#a98be0",
    "Open-weight models": "#d85a30",
    "ROI & adoption": "#ef9f27",
    "Market & vendors": "#d06fa5",
    "Cost & compute": "#e0b341",
    "Data & memory": "#6fb3e8",
}
# Short label + emoji per topic (keeps nodes compact).
LABELS = {
    "EU AI Act": "⚖️ EU AI Act",
    "Agentic AI": "🤖 Agentic AI",
    "AI governance": "📋 AI governance",
    "Security & containment": "🛡️ Security & containment",
    "MCP & agent standards": "🔌 MCP & agent standards",
    "Model pricing & commoditization": "🧩 Pricing & commoditization",
    "Open-weight models": "⚙️ Open-weight models",
    "ROI & adoption": "📈 ROI & adoption",
    "Market & vendors": "🏢 Market & vendors",
    "Cost & compute": "💰 Cost & compute",
    "Data & memory": "🧠 Data & memory",
}

# layout constants
ROOT_X, ROOT_W = 10, 184
TOPIC_X, TOPIC_W = 300, 256
LEAF_X, LEAF_W, LEAF_H = 600, 376, 21
TOP = 40
PITCH = 25          # vertical distance between consecutive leaves
GROUP_GAP = 12      # extra gap between topic groups


def esc(s):
    return html.escape(s, quote=True)


def build_svg(vocab, editions):
    # group editions by primary topic (first tag)
    groups = {}
    for e in editions:
        primary = e["tags"][0]
        groups.setdefault(primary, []).append(e)
    for g in groups.values():
        g.sort(key=lambda e: e["date"])

    vindex = {name: i for i, name in enumerate(vocab)}
    order = sorted(groups.keys(), key=lambda t: (-len(groups[t]), vindex.get(t, 99)))

    # assign leaf y positions, group by group
    y = TOP + LEAF_H / 2
    topic_rows = []  # (topic, [(edition, leaf_cy), ...], topic_cy)
    for t in order:
        leaves = []
        for e in groups[t]:
            leaves.append((e, y))
            y += PITCH
        topic_cy = sum(cy for _, cy in leaves) / len(leaves)
        topic_rows.append((t, leaves, topic_cy))
        y += GROUP_GAP
    bottom = y - GROUP_GAP + LEAF_H / 2
    total = sum(len(v) for v in groups.values())
    all_cys = [cy for _, leaves, _ in topic_rows for _, cy in leaves]
    root_cy = (min(all_cys) + max(all_cys)) / 2
    vb_h = round(bottom + 22)
    vb_w = LEAF_X + LEAF_W + 16

    parts = []
    parts.append(
        f'<svg viewBox="0 0 {vb_w} {vb_h}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" style="width:100%;min-width:900px;height:auto" '
        f'aria-label="Mind map of all {total} AI Tech Radar editions grouped by primary topic. '
        f'A central hub branches into {len(order)} topics; each topic branches into its daily editions.">'
    )
    # --- connectors first (under the nodes) ---
    for t, leaves, tcy in topic_rows:
        c = COLORS.get(t, "#9aa7b6")
        # root -> topic
        parts.append(
            f'<path d="M{ROOT_X+ROOT_W} {root_cy:.1f} C{ROOT_X+ROOT_W+50} {root_cy:.1f} '
            f'{TOPIC_X-50} {tcy:.1f} {TOPIC_X} {tcy:.1f}" fill="none" stroke="{c}" '
            f'stroke-width="2" opacity="0.55"/>'
        )
        # topic -> leaves
        for _, lcy in leaves:
            parts.append(
                f'<path d="M{TOPIC_X+TOPIC_W} {tcy:.1f} C{TOPIC_X+TOPIC_W+38} {tcy:.1f} '
                f'{LEAF_X-38} {lcy:.1f} {LEAF_X} {lcy:.1f}" fill="none" stroke="{c}" '
                f'stroke-width="1.3" opacity="0.4"/>'
            )
    # --- topic nodes ---
    for t, leaves, tcy in topic_rows:
        c = COLORS.get(t, "#9aa7b6")
        label = esc(LABELS.get(t, t))
        n = len(leaves)
        ty = tcy - 19
        parts.append(
            f'<g><title>{esc(t)} — {n} edition{"s" if n != 1 else ""} led with this topic.</title>'
            f'<rect x="{TOPIC_X}" y="{ty:.1f}" width="{TOPIC_W}" height="38" rx="10" '
            f'fill="#1c2330" stroke="{c}" stroke-width="2"/>'
            f'<text x="{TOPIC_X+16}" y="{tcy+4:.1f}" font-size="12.5" font-weight="700" '
            f'fill="#e8edf3" font-family="sans-serif">{label}'
            f'<tspan fill="{c}" font-weight="800"> ({n})</tspan></text></g>'
        )
    # --- leaf nodes (clickable) ---
    for t, leaves, tcy in topic_rows:
        c = COLORS.get(t, "#9aa7b6")
        for e, lcy in leaves:
            mmdd = esc(e["date"][5:])
            head = esc(e["headline"])
            href = f'../{e["date"]}/index.html'
            ly = lcy - LEAF_H / 2
            parts.append(
                f'<a href="{href}"><g><title>{mmdd} · {head} — primary topic: {esc(t)}</title>'
                f'<rect x="{LEAF_X}" y="{ly:.1f}" width="{LEAF_W}" height="{LEAF_H}" rx="6" '
                f'fill="#161b22" stroke="{c}" stroke-width="1.3"/>'
                f'<text x="{LEAF_X+12}" y="{lcy+3.6:.1f}" font-size="10.5" '
                f'font-family="sans-serif">'
                f'<tspan fill="{c}" font-weight="700">{mmdd}</tspan>'
                f'<tspan fill="#c3ccd8">  ·  {head}</tspan></text></g></a>'
            )
    # --- hub node last (on top) ---
    ry = root_cy - 42
    parts.append(
        f'<rect x="{ROOT_X}" y="{ry:.1f}" width="{ROOT_W}" height="84" rx="14" '
        f'fill="#221f3d" stroke="#7f77dd" stroke-width="2.4"/>'
        f'<text x="{ROOT_X+ROOT_W/2:.0f}" y="{root_cy-16:.1f}" text-anchor="middle" '
        f'font-size="11" font-weight="700" letter-spacing="0.12em" fill="#9d96f0" '
        f'font-family="sans-serif">🛰️ AI TECH RADAR</text>'
        f'<text x="{ROOT_X+ROOT_W/2:.0f}" y="{root_cy+7:.1f}" text-anchor="middle" '
        f'font-size="18" font-weight="800" fill="#ffffff" font-family="sans-serif">{total} editions</text>'
        f'<text x="{ROOT_X+ROOT_W/2:.0f}" y="{root_cy+27:.1f}" text-anchor="middle" '
        f'font-size="10.5" fill="#9aa7b6" font-family="sans-serif">Jun–Aug 2026 · by topic</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts), total, len(order)


SECTION_TMPL = """<!-- MINDMAP:START (generated by scripts/archive_mindmap.py — do not hand-edit) -->
  <section class="month" id="topicmap">
    <div class="mhead"><h2>Topic map <span class="ct">every edition, mapped to its lead topic</span></h2></div>
    <p class="sub" style="margin:10px 0 4px">A mind map of the whole archive: each daily edition is placed under the one topic it led with, so you can see at a glance where the {total} editions cluster — and jump straight to any of them. Every leaf links to its brief; hover a branch for the count.</p>
    <div class="chart">
{svg}
    </div>
    <p class="wrapna" style="margin:8px 2px 0">Primary-topic assignment uses each edition's lead tag from <code>tags.json</code> ({ntopics} topics in the controlled vocabulary); many editions touch several topics — see the <a href="../trends/index.html">trend analysis</a> for the full multi-tag view.</p>
  </section>
<!-- MINDMAP:END -->"""


def main():
    data = json.load(open(TAGS))
    vocab = data["vocabulary"]
    editions = data["editions"]
    svg, total, ntopics = build_svg(vocab, editions)
    section = SECTION_TMPL.format(svg=svg, total=total, ntopics=ntopics)

    page = open(ARCHIVE).read()
    if "<!-- MINDMAP:START" in page:
        page = re.sub(
            r"<!-- MINDMAP:START.*?<!-- MINDMAP:END -->",
            lambda m: section,
            page,
            flags=re.S,
        )
    else:
        page = page.replace("</header>\n", "</header>\n" + section + "\n", 1)
    open(ARCHIVE, "w").write(page)
    print(f"archive mind map: {total} editions across {ntopics} topics -> {ARCHIVE}")


if __name__ == "__main__":
    main()
