# Sources — AI Tech Radar, 24 September 2026 ("The Whetstone")

The anchor (Anthropic's Claude Opus 5.5 model page) was fetched directly. Other figures are
relayed from vendor announcements and reputable secondary coverage surfaced via web search, and
are marked **"as reported"** in the brief. Several secondary source pages could not be fetched
directly (the compile environment's network egress proxy blocked them — TechCrunch, VentureBeat,
The Register), so specific secondary figures — the SWE-bench Pro number and the release-cadence
day counts — should be reconciled against the primary publications before republishing.

## The anchor — Claude Opus 5.5 (Anthropic, 22 Sep 2026)
- Introducing Claude Opus 5.5 — Anthropic (read directly): https://www.anthropic.com/claude-opus-5-5
  - "at the level of Claude Fable 5.1 on most work"; ~40% lower cost on typical workloads
  - Pricing $4 / $20 per M input/output tokens (−20% vs Opus 5's $5/$25); cache reads $0.20 (−60%); cache writes $5
  - Output >30% faster than Opus 5
  - Terminal-Bench 4.0 66.4% (vs 52.3%); FrontierCode v1.1 54.4% (vs 48.0%); CursorBench 4.0 57.8% (vs 46.6%); GDPval-AA v2.1 1846 Elo (vs 1708); OSWorld 2.0 81.8% partial (vs 74.0%)
  - Containment eval: attempted to circumvent boundaries ~85% less often than Opus 5, "every attempt low severity and self-reported"

## Secondary coverage — Opus 5.5 launch, pricing, cadence, "legacy"
- Anthropic releases Claude Opus 5.5, beating Fable 5.1 on key agentic benchmarks at 60% cheaper API price — VentureBeat: https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price
- Anthropic releases Opus 5.5 with lower prices and Fable-level performance — TechCrunch: https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/
- Anthropic launches Claude Opus 5.5 at lower cost, higher performance — QZ: https://qz.com/anthropic-claude-opus-55-cost-performance-092226
- Anthropic upgrades Claude with new Opus 5.5 model, details here — 9to5Mac: https://9to5mac.com/2026/09/22/anthropic-upgrades-claude-with-new-opus-5-5-model-details-here/
- Claude Opus 5.5: Complete Guide to Specs, Pricing and Benchmarks (SWE-bench Pro ~89.9%) — Codersera: https://codersera.com/blog/claude-opus-5-5-complete-guide-2026/
- Claude Opus 5.5 Benchmarks, Pricing & Context Window — LLM-Stats: https://llm-stats.com/models/claude-opus-5-5
- Claude Opus 5.5: Pricing, Benchmarks and Breaking Changes (Opus 5 → legacy; Sonnet 5.5 / Haiku 5.5 next) — Digital Applied: https://www.digitalapplied.com/blog/claude-opus-5-5-launch-pricing-benchmarks-2026

## The clock — release cadence, the racing frontier
- AI Model Releases: September 2026 Tracker and Dated Ledger (cadence quarterly→monthly; 21 days after Fable 5.1/Mythos 5.1; 39 days after Opus 5) — Digital Applied: https://www.digitalapplied.com/blog/ai-model-releases-september-2026-tracker
- AI Frontier Model Tracker (updated 23 Sep 2026) — DemandSphere: https://www.demandsphere.com/research/demandsphere-radar/ai-frontier-model-tracker/
- Frontier AI keeps racing despite calls to slow down — The Register (egress-blocked; headline as reported): https://www.theregister.com/ai-and-ml/2026/09/23/frontier-ai-keeps-racing-despite-calls-to-slow-down/5298448
- 2026 in artificial intelligence (GPT-6 Astra 3 Sep; Sol and Luna 19 days later; multi-lab September) — Wikipedia: https://en.wikipedia.org/wiki/2026_in_artificial_intelligence

## Prior rails (background)
- The Foundation (22 Sep 2026 edition — own the floor, keep the larder, light a second fire): https://andromedakah.github.io/ai-radar/2026-09-22/index.html
- EU AI Act — up-to-date developments and analyses: https://artificialintelligenceact.eu/
- The enforcement framework of the AI Act — European Commission: https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act
- The 2026-07-28 MCP Specification — Model Context Protocol blog: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Gartner: 40% of enterprise apps will feature task-specific AI agents by 2026: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

## Owner-verified recurring facts (see ai-radar/verified_facts.json)
- Gartner — over 40% of agentic AI projects canceled by end of 2027: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- EU AI Act penalties up to €35M or 7% of global turnover: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

---

*Editorial framing — the "whetstone" allegory (the model as a reaping-blade re-ground sharper and
cheaper every three weeks, the smaller blade now beating the bigger one and last month's flagship
already "old iron"; keep your own grindstone, fit one standard hilt, grind your grip to no single
blade) — is expressly the radar's own reading, not a sourced claim about any specific company beyond
the reported Anthropic, OpenAI and cadence figures.*
