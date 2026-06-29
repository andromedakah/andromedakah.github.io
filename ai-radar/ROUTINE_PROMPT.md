# AI Tech Radar — cloud routine prompt

This is the **self-contained prompt** for running the daily AI Tech Radar as a
cloud routine (claude.ai/code Schedule / routines) — no local machine required.
Paste it into a new scheduled routine that has this repo connected with push access.

> Suggested schedule: daily, ~07:47 Europe/Paris (`47 7 * * *`).

---

Generate today's edition of the **AI Tech Radar** — a daily enterprise-AI
situational-awareness brief — and publish it to this GitHub Pages site. Run fully
autonomously; no user is present. This prompt is self-contained: do NOT rely on any
local files, paths, or memory.

## Repository
- Repo: `andromedakah/andromedakah.github.io` (personal user-pages Jekyll site). The
  radar lives ONLY under `/ai-radar/`. NEVER overwrite the site root `README.md`
  (the owner edits it directly on GitHub).
- Branch `main`. Git identity: Kahina Ferroukhi <kahina.ferroukhi@gmail.com>.
- Before pushing: `git fetch origin main && git rebase origin/main`. If push is
  rejected, fetch + rebase and retry.

## Audience & goal
Serve BOTH engineers and C-level executives. The owner is moving from Software
Engineer toward C-level engagement, and uses this to talk to engineers and the
boardroom and spark AI use-case creativity. All data must be REAL and ACCURATE —
every figure carries a source link.

## Research
Web-search the last ~3 days of AI news from trusted sources: vendor newsrooms
(OpenAI, Anthropic, Google, Microsoft, NVIDIA, SAP, IBM, AWS), analysts (Gartner,
McKinsey, Forrester, Morgan Stanley, IDC, S&P Global), regulators (EU Commission),
and reputable press (VentureBeat, CNBC, The New Stack, Reuters). Pick ONE coherent
theme for the day. Check existing `/ai-radar/<date>/` editions and do NOT repeat a
recent theme or allegory.

## Output — create under `/ai-radar/YYYY-MM-DD/`
- `ai-radar.md` — full brief
- `sources.md` — every claim's source as a real link, grouped by topic
- `index.html` — English web edition
- `index.fr.html` — French edition (careful human-quality translation of EVERYTHING,
  including SVG diagram labels + UI strings)
- `email.html` — email-ready edition (table layout, inline styles)

REQUIRED SECTIONS in every brief, in this order:
1. Executive summary (90-second read)
2. Allegory of the day — one specific topic, framed at C-level strategy
3. C-level engagement — sharp questions broken out cross-sector: cross-sector,
   financial services, healthcare/life sciences, manufacturing/industrials,
   retail/consumer, public sector/regulated
4. Technical deep-dive — explain one principle with an INLINE SVG diagram, and how it
   lands on LEGACY technology
5. Quotes that catch attention (real quotes → real people; mark editorial lines as the
   radar's own framing)
6. Numbers to quote in a meeting (sourced table)
7. So what — 3 moves for the next 30 days

## Template & feed mechanics
- Copy structure/CSS/JS from the MOST RECENT `/ai-radar/<date>/index.html` and
  `index.fr.html`; swap only content + the SVG diagram. Keep: dark theme, sticky TOC,
  EN/FR toggle ("🌐 EN · FR"), and the read-aloud TTS player in BOTH pages (browser
  `speechSynthesis`: "🔊 Listen to this brief" button + sticky bottom player; FR uses
  `u.lang='fr-FR'` + a French voice). Keep EN and FR structurally identical.
- Behave as a real daily feed: PREPEND a new `<item>` to `/ai-radar/feed.xml` (newest
  first; never remove existing items), update `<lastBuildDate>`, and add a new entry at
  the TOP of the `/ai-radar/index.html` landing feed list. Use guid `ai-radar-YYYY-MM-DD`
  and link `https://andromedakah.github.io/ai-radar/YYYY-MM-DD/index.html`.

## Finish
Commit (end the message with `Co-Authored-By: Claude <noreply@anthropic.com>`) and
`git push origin main`. Report live URLs: the edition page,
`https://andromedakah.github.io/ai-radar/`, and `feed.xml`.
