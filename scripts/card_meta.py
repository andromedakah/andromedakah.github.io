#!/usr/bin/env python3
"""Apply the dual-title / eyebrow architecture to the landing feed cards.

Reads ai-radar/cards_meta.json and, for each edition card in ai-radar/index.html
(matched by its YYYY-MM-DD href), sets the accent eyebrow label to the edition's
operational category and inserts a concrete subtitle directly under the creative
title. Idempotent — safe to re-run whenever cards_meta.json changes.

    python3 scripts/card_meta.py
"""
import json, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = os.path.join(ROOT, "ai-radar", "cards_meta.json")
PAGE = os.path.join(ROOT, "ai-radar", "index.html")

EYEBROW_RE = re.compile(
    r'(<div class="mb-1 text-\[11px\] font-bold uppercase tracking-wider text-accent">).*?(</div>)',
    re.S)
SUB_RE = re.compile(r'\s*<div class="card-sub[^"]*">.*?</div>', re.S)


def esc(s):
    return html.escape(s, quote=True)


def transform(card, eyebrow, subtitle):
    card = EYEBROW_RE.sub(lambda m: m.group(1) + esc(eyebrow) + m.group(2), card, count=1)
    card = SUB_RE.sub("", card, count=1)  # drop any prior subtitle
    sub = ('\\1\n      <div class="card-sub mt-1 text-[13px] font-semibold '
           'leading-snug text-subink">' + esc(subtitle) + '</div>')
    card = re.sub(r'(</h3>)', sub, card, count=1)
    return card


def main():
    meta = json.load(open(META))["cards"]
    page = open(PAGE).read()
    done = 0
    for date, m in meta.items():
        pat = re.compile(
            r'(<a href="' + re.escape(date) + r'/index\.html" class="item[^"]*">)(.*?)(</a>)', re.S)
        mo = pat.search(page)
        if not mo:
            continue
        new_inner = transform(mo.group(2), m["eyebrow"], m["subtitle"])
        page = page[:mo.start()] + mo.group(1) + new_inner + mo.group(3) + page[mo.end():]
        done += 1
    open(PAGE, "w").write(page)
    print(f"dual-title cards applied: {done}/{len(meta)} -> {PAGE}")


if __name__ == "__main__":
    main()
