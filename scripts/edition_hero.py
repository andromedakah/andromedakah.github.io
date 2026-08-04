#!/usr/bin/env python3
"""Apply the dual-title / eyebrow architecture to the edition pages (EN + FR).

For every edition in ai-radar/cards_meta.json, set the hero kicker to
"<brand> · <category eyebrow>" and insert a concrete subtitle under the <h1>,
in both the English page (index.html) and the French page (index.fr.html).
Idempotent — safe to re-run whenever cards_meta.json changes.

    python3 scripts/edition_hero.py
"""
import json, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RADAR = os.path.join(ROOT, "ai-radar")
META = os.path.join(RADAR, "cards_meta.json")

LANGS = [
    {"file": "index.html",    "brand": "🛰️ AI Tech Radar", "eb": "eyebrow",    "sub": "subtitle"},
    {"file": "index.fr.html", "brand": "🛰️ Radar IA",      "eb": "eyebrow_fr", "sub": "subtitle_fr"},
]

KICKER_RE = re.compile(r'<div class="kicker">.*?</div>')
SUBHEAD_RE = re.compile(r'\s*<div class="subhead">.*?</div>')
KICKER_CSS_RE = re.compile(r'(\.kicker\{[^}]*\})')
SUBHEAD_CSS = ('.subhead{font-size:17px;line-height:1.4;color:var(--soft);'
               'font-weight:600;margin:.15em 0 .45em}')


def esc(s):
    return html.escape(s, quote=False)  # keep literal apostrophes (valid in text)


def apply_page(path, brand, eyebrow, subtitle):
    s = open(path, encoding="utf-8").read()
    orig = s
    # 1. kicker -> brand · category
    s = KICKER_RE.sub('<div class="kicker">' + esc(brand + " · " + eyebrow) + '</div>', s, count=1)
    # 2. subtitle under the h1 (drop any prior one first)
    s = SUBHEAD_RE.sub("", s, count=1)
    s = re.sub(r'(</h1>)', r'\1\n  <div class="subhead">' + esc(subtitle) + '</div>', s, count=1)
    # 3. ensure .subhead CSS exists
    if ".subhead{" not in s:
        s = KICKER_CSS_RE.sub(lambda m: m.group(1) + "\n  " + SUBHEAD_CSS, s, count=1)
    if s != orig:
        open(path, "w", encoding="utf-8").write(s)
        return True
    return False


def main():
    meta = json.load(open(META))["cards"]
    changed = 0
    for date, m in meta.items():
        for L in LANGS:
            path = os.path.join(RADAR, date, L["file"])
            if not os.path.exists(path):
                continue
            if apply_page(path, L["brand"], m[L["eb"]], m[L["sub"]]):
                changed += 1
    print(f"edition heroes updated: {changed} pages across {len(meta)} editions")


if __name__ == "__main__":
    main()
