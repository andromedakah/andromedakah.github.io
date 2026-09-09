# Sources — AI Tech Radar, 9 September 2026 ("The Tide Table")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or outlet that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure is reported via secondary coverage, a vendor or lab publication, a standards-body page, or a survey summary, it is marked "as reported." **Verification note:** essentially all source domains (including cnbc.com, mckinsey.com and the lab primary blogs) were unreachable to direct fetch from the compile environment behind the network egress proxy; the figures below rest on search-engine extraction of the named sources and should be re-verified against the primary publications before republishing.

## The story — a grander ship every week ("model fatigue"): build one quay any ship can dock at, keep a disciplined watch, and put your strength in the larder, not the pier

### The cadence — four frontier labs shipped major models in a single week (the datable hook)

- CNBC, "'Model fatigue' sets in as AI labs race to roll out new versions at a frenetic pace" (6 Sep 2026) — https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html (egress-blocked to direct fetch; relayed via search summary — **[Consolidating source for the cadence and the "model fatigue" effect; corroborated across Startup Fortune, AI Weekly and llm-stats]**)
- CNBC on X — https://x.com/CNBC/status/2096572100219715912 (via search summary)
- Startup Fortune, "Anthropic, OpenAI, Meta and Google All Shipped New AI Models in One Week" — https://startupfortune.com/anthropic-openai-meta-and-google-all-shipped-new-ai-models-in-one-week/ (via search summary)
- Startup Fortune, "Four AI Labs Released Major Models in One Week and Buyers Can't Keep Up" — https://startupfortune.com/four-ai-labs-released-major-models-in-one-week-and-buyers-cant-keep-up/ (via search summary)
- AI Weekly, "CNBC: 'Model Fatigue' Grips Enterprise Buyers After Anthropic, OpenAI, Meta and Google All Ship in One Week" — https://aiweekly.co/alerts/cnbc-model-fatigue-grips-enterprise-buyers-after-anthropic-openai-meta-and (via search summary)
- llm-stats, "AI Updates Today (September 2026) — Latest AI Model Releases" — https://llm-stats.com/llm-updates (via search summary)
- Digital Today, "Companies face 'AI model fatigue' as advanced models pour out" — https://www.digitaltoday.co.kr/en/view/100543/companies-face-ai-model-fatigue-as-advanced-models-pour-out (via search summary)

Claims sourced here (as reported): four frontier labs shipped major models inside a single week in early September 2026 — Anthropic's Claude Fable 5.1 and its gated sibling Claude Mythos 5.1 (~1 September), Meta's Muse Spark 1.3 (2 September), Google's Gemini 3.8 Flash (2 September, its third Flash release in six weeks) and OpenAI's GPT-6 Astra (3 September). CNBC (6 September) reports the effect on enterprise buyers as "model fatigue": CEOs, IT managers, CFOs and founders spend an outsized share of their time comparing costs and capabilities, only to watch the comparison go stale before they finish it; some startups have stopped trying to evaluate every release and cap their shortlist at around five models instead of ten. CNBC frames the pace as a "share-of-wallet" arms race by labs racing toward public markets — each already valued near $1 trillion by private investors — and notes that over 1,100 lab employees have separately petitioned Washington to help pace frontier AI development. Carried here as "the tide table": the sea (the cadence) will not stop, so build a harbor that receives every ship rather than re-cutting the pier for each hull.

### The economics inside the churn — Anthropic Fable 5.1 pricing (each release is substantive)

- Price Per Token, "New Models Today — AI & LLM Releases Last 24 Hours" — https://pricepertoken.com/news/model-releases (via search summary)
- Startup Fortune (as above), on Fable 5.1 pricing (via search summary)

Claims sourced here (as reported): Anthropic's Claude Fable 5.1 kept the same headline API rates as Fable 5 but cut cached-input reads from $1.00 to $0.25 per million tokens, making typical workloads about 25% cheaper and highly agentic workloads as much as ~45% cheaper. Carried here as the point that each release is substantive enough that ignoring it costs money and re-integrating each costs attention — the contradiction the tide table resolves.

### The structural answer — the model gateway / model-agnostic abstraction layer (the standing quay)

- vaasblock, "Enterprise AI Vendor Lock-In: The Switching Cost Problem No One Is Measuring" — https://www.vaasblock.com/research/enterprise-ai-vendor-lock-in-switching-costs-copilot-agentforce-2026/ (via search summary — **[Search-extracted]**)
- orchestrator.dev, "AI Cost Control: Breaking Free from Vendor Lock-In" — https://orchestrator.dev/blog/2026-03-27-ai-cost-control-vendor-strategy/ (via search summary)
- Swfte AI, "AI Vendor Lock-in: How Enterprises Are Breaking Free in 2026" — https://www.swfte.com/blog/avoid-ai-vendor-lock-in-enterprise-guide (via search summary)
- Chat GPT AI Hub, "AI Vendor Lock-In vs Flexibility: How to Build a Multi-Model AI Strategy in 2026" — https://chatgptaihub.com/ai-vendor-lock-in-multi-model-strategy-2026-enterprise-guide/ (via search summary)
- Augment Code, "Model-Agnostic AI: Why Provider Lock-In Is So Expensive" — https://www.augmentcode.com/guides/model-agnostic-ai-why-provider-lock-in-is-so-expensive (via search summary)
- Lyzr, "LLM Agnostic Solutions: 2026 Enterprise AI Guide" — https://www.lyzr.ai/blog/llm-agnostic-solutions-enterprise-guide/ (via search summary)
- Kai Waehner, "Enterprise Agentic AI Landscape Q2 2026: Trust, Flexibility, and Vendor Lock-in" — https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/ (via search summary)

Claims sourced here (as reported): the most effective structural investment against vendor lock-in is an AI model gateway — an abstraction layer between applications and model providers that routes all LLM requests through a unified, vendor-agnostic API, so switching or adding a provider requires no application-code change. Mature enterprise architectures route each workload to the optimal model for the task on cost, latency, quality and data-sensitivity. AI vendor lock-in is estimated to cost ~19–34% in switching; ~37% of organisations now run five or more models in production, up from ~29% the prior year; and the behavioural lock-in lives in prompts, workflows and accumulated instructions tuned to a specific provider, not in the API itself. Carried here as "the standing quay": the gateway is the quay any ship can dock at, and the evaluation harness is the tide table.

### The value gate — value lives in your data and process, not the model (the larder)

- McKinsey & Company, "The State of AI: Global Survey 2026" — https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai (primary; egress-blocked; via secondary coverage — **[Corroborated across multiple outlets]**)
- OpenAI, "The next phase of enterprise AI" — https://openai.com/index/next-phase-of-enterprise-ai/ (via search summary)
- OpenAI, "Enterprise signals: What frontier firms are doing differently" — https://openai.com/signals/enterprise-data/ (via search summary)

Claims sourced here (context, as reported): McKinsey's State of AI 2026 finds the enterprise differentiator is proprietary data and redesigned process, not the model, and that ~80% of firms report productivity gains while only ~37% report any EBIT impact. The same body of coverage reports that 32% of organisations have skipped buying at least one software product or feature because they could build it internally with agentic coding tools, and that large enterprises scaling agents in one or more functions rose from ~27% to ~40%. Related enterprise signals (as reported via OpenAI): agentic AI (Codex tokens) reached ~64% of combined Codex + ChatGPT output tokens among enterprise customers by June 2026; Codex passed ~3M weekly active users; and enterprise makes up more than 40% of OpenAI's revenue. Carried here as "the larder": the lasting value is on your side of the API — the data, process and evaluations no new model can make stale.

### Deployment, not model choice, is the scarce work — Microsoft's Frontier Company (standing)

- The Decoder, "Microsoft launches $2.5 billion 'Frontier Company' to embed 6,000 AI engineers inside enterprise clients" — https://the-decoder.com/microsoft-launches-2-5-billion-frontier-company-to-embed-6000-ai-engineers-inside-enterprise-clients/ (via search summary)
- CNBC, "Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit" (2 Jul 2026) — https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html (via search summary)
- TechCrunch, "Microsoft launches its own AI deployment company with $2.5 billion commitment" — https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/ (via search summary)

Claims sourced here (context, as reported): Microsoft's Frontier Company (launched 2 July 2026) commits $2.5 billion and ~6,000 engineers to "forward-deployed engineering" — placing technical teams directly alongside enterprise clients to design, deploy and run AI systems with measurable ROI rather than more pilots. Carried here as context: the scarce enterprise work is deployment, process redesign and data — not choosing this week's model.

## Standing context (background)

### The standards floor — MCP 2026-07-28 (verified at primary source in prior editions)

- Model Context Protocol, "MCP specification 2026-07-28" — https://blog.modelcontextprotocol.io/posts/2026-07-28/ (**[Verified — read directly at primary source in prior editions]**)

Claims sourced here (verified at the MCP primary source in prior editions): the 2026-07-28 MCP specification promoted Enterprise-Managed Authorization (EMA) to stable and adopted Client ID Metadata Documents (CIMD) in place of Dynamic Client Registration. Referenced here as the vendor-neutral plumbing beneath the model-agnostic gateway — how to admit, name and govern models and agents without wedding the estate to one supplier.

### Enforcement is live — the EU AI Act GPAI / systemic-risk regime (standing)

- European Commission, "Enforcement of the AI Act" — https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act (via search summary — **[Corroborated for 2 Aug 2026 enforcement]**)
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/ (via search summary)

Claims sourced here (as reported): EU AI Act enforcement powers over general-purpose AI models became operative on 2 August 2026; models above the systemic-risk threshold owe model evaluation, adversarial red-teaming, serious-incident reporting and cybersecurity duties, and the regime expects documented evaluation regardless of which model is deployed. Penalties are tiered: up to €35M or 7% of global turnover for prohibited practices; up to €15M or 3% for GPAI non-compliance. Carried here as context: governance evidence should attach to your governed interface and evaluations, not to one vendor's model card — so it survives a model swap.

## Prior-day context (background only)

Claims sourced here (context only): this week's earlier editions — "The Locksmith" (8 Sep, three labs gate a frontier cyber "twin" to defenders), "The Keyring" (7 Sep, every agent you admit is handed a key: keep the ring), "The Herald's Proclamation" (6 Sep, which first noted OpenAI's GPT-6 Astra launch and the "AGI" framing), "The Apprentice's Apprentice" (5 Sep, the tools improve the tools), "The Miller's Toll" (4 Sep, the cheapest tier is paid in your data), "The Two Mills" (3 Sep, motion vs value / ROI) and "The Break-In" (2 Sep, the cost of the ungoverned agent) — are referenced only as prior-day background. The tide table is the natural next figure: yesterday the board held the locksmith; today the harder question is the sea itself — a grander ship every week — and whether you have a harbor that receives every ship, or a pier you must tear down again.

---

*Editorial lines marked as the radar's own (e.g. "A harbor wed to one hull is a harbor held hostage by the next; the only harbor that thrives on a rising tide is the one built to receive them all.") are the AI Tech Radar's framing and are not third-party quotes. The tide-table allegory — a harbor town that stops re-cutting its pier for every hull, builds one quay any ship can dock at, keeps a tide table, and moves its strength into the larder — is a common civic illustration used allegorically and is not a sourced claim about any specific company, product or incident. Where a quotation or figure is attributed via secondary coverage, a vendor or lab publication, a standards-body page or a survey summary rather than a primary release, it is marked "as reported." The central figures come from the early-September 2026 release cadence and its reported effect on buyers (CNBC's "model fatigue" reporting of 6 September, corroborated across Startup Fortune, AI Weekly and llm-stats), the enterprise-architecture consensus on model gateways and vendor lock-in (multiple 2026 analyses), and the McKinsey State of AI 2026 value gate, with Microsoft's Frontier Company as deployment-gap context. Standing context — the MCP 2026-07-28 standards floor (the only figure read at its primary source) and the live EU AI Act GPAI/systemic-risk enforcement regime — is relayed as noted. Product, firm and model names (Anthropic / Claude / Fable / Mythos, Meta / Muse Spark, Google / Gemini, OpenAI / GPT-6 Astra / Codex, Microsoft / Frontier Company, CNBC, McKinsey / QuantumBlack, the Model Context Protocol, the European Commission / EU AI Office) reflect the sources as described in the cited 2026 material. Essentially all source domains were unreachable to direct fetch from the compile environment behind the network egress proxy, so the figures rest on search-engine extraction of the named sources and, in several cases, are unconfirmed against a primary source. This edition's central development in the window is one of cadence rather than a single capability: four frontier-class models shipped inside a single week, and the enterprise question shifted from "which model is best" to "can we absorb a weekly stream of them without being remade by any one" — hold one quay any ship can dock at, keep the tide table, and fill the larder, not the pier.*
