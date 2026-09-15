# AI Tech Radar — MONTHLY WRAP-UP cloud routine prompt

This is the **self-contained prompt** for the monthly wrap-up, meant to run as its **own
scheduled cloud routine** (claude.ai/code Schedule / routines), separate from the daily
`ROUTINE_PROMPT.md`. It builds the previous month's wrap-up once a month.

> Suggested schedule: **monthly, 1st of the month, ~08:41 Europe/Paris** (`41 8 1 * *`).
> Off-minute on purpose so it doesn't collide with everyone's top-of-hour jobs. Running on
> the 1st means the previous month is fully over and all its editions exist.

## Why this is a separate routine

The wrap-up used to be a conditional step inside the daily routine ("on the last edition of
the month"). That is fragile: if the month's final daily run is skipped, delayed, or the
condition is missed, the month is **silently never wrapped up** (this is exactly how
August 2026 was missed). Splitting it into its own monthly schedule makes the trigger
reliable. The daily routine also keeps a **catch-up safeguard** (see
`ROUTINE_PROMPT.md` → "Monthly wrap-up") that fills in any previous month still missing a
wrap-up, so the two mechanisms back each other up.

## How to install it as a cloud routine (one-time, ~2 min)

The cloud-routine backend is **not reachable from the local Claude Code CLI**, so a literal
in-session cron cannot schedule a monthly job (a session-only job expires in days and would
never survive to fire). Set this up from the web app, the same way as the daily routine:

1. Open **claude.ai/code** and select the **cloud environment** that has this repo —
   `andromedakah/andromedakah.github.io` — connected with **push (write) access**.
2. Open the **Routines / Schedule** panel (clock icon) → **New routine**.
3. **Schedule:** `41 8 1 * *`, timezone **Europe/Paris** (monthly, 1st, ~08:41).
4. **Prompt:** paste everything below the `---` line of this file.
5. Save. Optionally trigger a manual run once to confirm it builds EN + FR, surfaces the
   links, and pushes live.

---

Build (or refresh) the **monthly wrap-up** of the AI Tech Radar for the **previous calendar
month** and publish it to this GitHub Pages site. Run fully autonomously; no user is
present. This prompt is self-contained.

## Repository
- Repo: `andromedakah/andromedakah.github.io`. The radar lives ONLY under `/ai-radar/`.
  NEVER overwrite the site root `README.md`.
- Branch `main`. Before pushing: `git fetch origin main && git rebase origin/main`; if push
  is rejected, fetch + rebase and retry.

## Which month
- Determine today's date with `date -u`. The target is the **previous calendar month**
  (`YYYY-MM`). Only ever build a wrap-up for a month that is fully over — never the current
  month.
- If `/ai-radar/wrap-ups/<YYYY-MM>/index.html` already exists, refresh it in place rather
  than duplicating. If earlier months are also missing a wrap-up, build those too.

## Source material (no external research required)
Distill the target month's daily editions that already live in `/ai-radar/<YYYY-MM>-*/`
(their `ai-radar.md`, titles and subheads). The wrap-up is a distillation of the editions
and their sources — keep every figure traceable to an edition or its source. The
owner-verified fact core is `ai-radar/verified_facts.json` **only**; everything else is
"as reported" and must be marked as such.

## Output — create `/ai-radar/wrap-ups/<YYYY-MM>/`
Two structurally identical pages, `index.html` (EN) and `index.fr.html` (FR — careful
human-quality translation of EVERYTHING, including SVG `aria-label`, `<title>` tooltips and
labels; `lang="fr"`, `u.lang='fr-FR'` and a French voice in the TTS). **Copy the structure,
CSS and scripts from the most recent existing wrap-up** (`/ai-radar/wrap-ups/2026-08/` is
the current reference; 2026-07 preceded it) — swap only content and the two SVGs. Keep: dark
theme + light-mode toggle, sticky TOC with EN/FR switch, and the read-aloud TTS player in
both pages.

REQUIRED SECTIONS, in this order (see 2026-08 for the exact shape):
1. Header + lede (the month's single thesis) and a "Listen to this wrap-up" TTS button.
2. `#overview` — "The month at a glance": 4 KPI tiles + a framing paragraph.
3. `#allegory` — **Allegory of the Month** (a fresh C-level metaphor for the month's thesis;
   do NOT reuse a prior month's) ending in "The question it forces".
4. `#arc` — the week-by-week arc (an editorial reading of the month's headlines).
5. `#mindmap` — **required, every month**: a `<section id="mindmap">` (linked from the nav)
   with a self-contained inline-SVG radial mind map — a centre node holding the month's
   single thesis and **6 branches** (one per part of the story), each a rounded-rect node
   (emoji + short title + one line of that month's best-sourced facts), joined to the centre
   by curved `<path>` strokes, each a distinct palette colour
   (`--accent`/`--teal`/`--coral`/`--amber`/`--blue` + one extra). Wrap it in a `.chart` div
   (keeps its dark background in light mode); give the `<svg>` a full `role="img"` +
   `aria-label` and a `<title>` tooltip on every branch stating its source basis. Recentre
   the thesis and rebuild the branches for the new month — do NOT reuse a prior month's.
6. `#map` — **Signal vs Noise**: an inline-SVG scatter (Evidence × Persistence) placing the
   month's storylines, a legend, a "how points are placed" method note, and the same data as
   a table. Signal = multi-source/verified/in-force; Hype-watch = single-vendor/contested/
   unconfirmed.
7. `#clevel` — C-level questions by sector (cross-sector, financial services, healthcare/
   life sciences, manufacturing/industrials, retail/consumer, public sector/regulated).
8. `#facts` — the fact-checked core from `ai-radar/verified_facts.json` (owner-verified, with
   source links), then a short "strong as-reported numbers" list (named source, not owner-
   verified). Keep verified separate from "as reported".
9. `#look` — What to look for next month.
10. Footer with methodology + links (feed, previous month's wrap-up, archive, trends, RSS).

## Surface it (required)
A wrap-up nobody links to is invisible. After building it:
- `ai-radar/index.html` — the hero "📊 Start here: <Month> wrap-up" button → the new month.
- `ai-radar/archive/index.html` — flip the new month's header from the
  `<span class="wrapna">Monthly wrap-up — at month end</span>` placeholder to
  `<a class="wrapbtn" href="../wrap-ups/YYYY-MM/index.html">📊 Monthly wrap-up →</a>`, and
  point the nav + footer "wrap-up" links at the new month (leave older months' own
  archive-row buttons intact). If the month's edition count in the archive is stale, correct
  it.
- `ai-radar/trends/index.html` — nav + footer wrap-up links → the new month.
- The new wrap-up's own nav + footer link back to the previous month's wrap-up (EN→EN,
  FR→FR).

## Finish
Commit (message e.g. `Add AI-Tech-Radar monthly wrap-up — <Month YYYY>`, ending with
`Co-Authored-By: Claude <noreply@anthropic.com>`) and `git push origin main`. Report the
live URLs: `https://andromedakah.github.io/ai-radar/wrap-ups/<YYYY-MM>/index.html` (EN + FR)
and the landing page.
