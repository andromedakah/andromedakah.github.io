# Sources — AI Tech Radar, 18 August 2026 ("The Deputy")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or outlet that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Note: several primary publisher pages (OpenAI, and various trade outlets) were unreachable from the compile environment behind the network egress proxy; those items were verified by cross-referencing multiple reputable outlets and are flagged accordingly.

## The story — enterprise AI shifts from assistance to execution

### The signal — the majority of enterprise AI output is now the agent's

- OpenAI, "From assistance to execution: How enterprises put AI to work" — https://openai.com/index/how-enterprises-put-ai-to-work/
- OpenAI, "Enterprise Signals" (enterprise data) — https://openai.com/signals/enterprise-data/
- Digital Today (EN), "OpenAI says 64 percent of enterprise output tokens come from Codex; frontier firms use 8.3 times more" — https://www.digitaltoday.co.kr/en/view/92763/openai-says-64-percent-of-enterprise-output-tokens-come-from-codex-frontier-firms-use-8-3-times-more
- VKTR, "OpenAI Data Shows Top Enterprise AI Users Now Consume 8x More Than Typical Firms" — https://www.vktr.com/ai-news/openai-data-shows-top-enterprise-ai-users-now-consume-8x-more-than-typical-firms/
- BankInfoSecurity, "Enterprise AI Token Spend Shifts From Chat to Agents" — https://www.bankinfosecurity.com/enterprise-ai-token-spend-shifts-from-chat-to-agents-a-32539
- ResultSense, "OpenAI says heaviest enterprise users are pulling away" — https://www.resultsense.com/news/2026-08-13-openai-enterprise-frontier-gap/
- daily.dev, "From assistance to execution: How enterprises put AI to work" — https://daily.dev/posts/from-assistance-to-execution-how-enterprises-put-ai-to-work-t3rvfezpk

Claims sourced here (as reported): On or about 13 August 2026, OpenAI published "From assistance to execution: How enterprises put AI to work" (an Enterprise Signal report). It reported that, as of June 2026, Codex generated ~64% of the combined Codex-and-ChatGPT output tokens among enterprise customers; that "frontier firms" (the top ~10% of firms by AI usage) generated ~8.3× as many output tokens per active user as typical firms, up from a ~2.6× gap in January; and that Codex weekly-active users grew ~108× in legal, ~41× in sales and recruiting and ~26× in marketing since February versus ~5× in engineering. The report's thesis is that enterprise AI is shifting from assistance (suggesting) to execution (acting). Figures are relayed via multiple secondary outlets as reported and should be re-verified at OpenAI's primary page before republishing.

### The control — identity becomes the control plane for acting agents

- Google Cloud Blog, "Introducing Gemini Enterprise Agent Platform" — https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
- Google Cloud Documentation, "Agent Identity overview" — https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview
- Google Cloud Documentation, "Use Agent Identity with Agent Runtime" — https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity
- Google (blog.google), "Gemini Enterprise Agent Platform lets you build, govern and optimize your agents" — https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-enterprise-agent-platform/
- Google Cloud Blog, "What's new in Gemini Enterprise Agent Platform" — https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform

Claims sourced here (as reported): Google's Gemini Enterprise Agent Platform gives each agent a fully managed, unique identity. Access tokens issued for Google Cloud are cryptographically bound to the agent's X.509 certificates, making bound tokens unreplayable to resist token theft and account takeover; agent identities are not shared by default, cannot be impersonated, and do not allow long-lived service-account keys. The platform provides per-action authorization (via an auth manager and Agent Gateway) and full auditing. The platform's general availability was announced earlier in 2026; Agent Identity is carried here as the standing enterprise mechanism for governing agents that act.

### The scale — non-human identity is the defining gap

- Cloud Security Alliance (Lab), "The Non-Human Identity Governance Vacuum" (whitepaper: non-human identity & agentic AI governance) — https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/
- Okta, "AI Agent Identity for Enterprise Security at Scale" — https://www.okta.com/identity-101/what-is-ai-agent-identity/
- Reco, "Non-Human Identities for AI Agents: How to Govern Access at Enterprise Scale" — https://www.reco.ai/blog/non-human-identities-for-ai-agents
- Saviynt, "Identity Security for, and by, AI Agents" — https://saviynt.com/blog/identity-security-for-and-by-ai-agents

Claims sourced here (as reported, approximate): Non-human identities now outnumber human users by an average of roughly 45 to 1, and in cloud-native environments the ratio can reach ~144 to 1. Unlike fixed service accounts, AI agents plan actions, select tools, interact with multiple systems and adapt as a task evolves, and a single agent can simultaneously hold credentials across CRM, email, cloud infrastructure and payment systems — making purpose-built non-human-identity governance (unique identity, just-in-time credentials, per-action authorization scoping, and audit trails) the defining security requirement of the agentic era.

## The engine — commodity models, now built for action

- VentureBeat, "Google's Gemini 3.7 Flash targets coding and agents with a 50% introductory price cut" — https://venturebeat.com/technology/googles-gemini-3-7-flash-targets-coding-and-agents-with-a-50-introductory-price-cut
- NokiaPowerUser, "Google just quiet-dropped Gemini 3.7 Flash in Antigravity — and it's built for agents, not chatbots" — https://nokiapoweruser.com/gemini-3-7-flash-google-antigravity-benchmarks-pricing/
- Google DeepMind, "Gemini 3.7 Flash — Model Card" — https://deepmind.google/models/model-cards/gemini-3-7-flash/
- OfficeChai, "Google Releases Gemini 3.7 Flash, Competes With GPT 5.6 Terra & Muse Spark 1.2 On Benchmarks" — https://officechai.com/ai/gemini-3-7-flash-benchmarks/
- AI Weekly, "AI News Today, August 17" (GPT-5.6 Sol Ultrafast on Cerebras, ~750 tok/s) — https://aiweekly.co/ai-news-today
- AI Release Tracker, "Latest AI Model Releases — August 2026" — https://aireleasetracker.com/latest
- llm-stats.com, "AI Updates Today (August 2026)" — https://llm-stats.com/llm-updates

Claims sourced here (as reported, standing context): Gemini 3.7 Flash shipped on or about 13 August 2026 built "for agents, not chatbots," lifting AutomationBench to ~30.4% (from ~17%) and DeepSWE v1.1 to ~65.3% (from ~49%), with an introductory price of $0.75/$3.75 per 1M tokens (a 50% cut) through 31 December 2026. On or about 17 August, OpenAI opened a limited preview of GPT-5.6 Sol "Ultrafast" mode, powered by Cerebras, delivering ~750 output tokens/sec and up to ~14× standard throughput. Open-weight Z.ai GLM-5.3 and Alibaba Qwen3.8 shipped 14 August; xAI's Grok 4.6 (12 August) tied GPT-5.6 Sol Max at the top of the Artificial Analysis Intelligence Index at $2/$6 per million tokens; Grok 3 was retired 15 August. These join the standing engine field — Claude Opus 5, GPT-5.6 Sol, Moonshot Kimi K3, DeepSeek V4-Pro — relayed from model-tracker and vendor coverage as the rented, swappable, per-token-priced model layer.

## The field — production is the frame

- Six Five Media / GlobeNewswire, "Six Five Media Unveils 'AI Unleashed' Lineup for Six Five Summit 2026, Headlined by Salesforce CEO Marc Benioff" (17 Aug 2026) — https://www.globenewswire.com/news-release/2026/08/17/3346280/0/en/six-five-media-unveils-ai-unleashed-lineup-for-six-five-summit-2026-headlined-by-salesforce-ceo-marc-benioff.html
- Yahoo Finance (syndication) — https://finance.yahoo.com/technology/ai/articles/six-five-media-unveils-ai-152800194.html
- Microsoft Learn, "August 2026 announcements — Partner Center" (Copilot work/personal account separation, 18 Aug) — https://learn.microsoft.com/en-us/partner-center/announcements/2026-august

Claims sourced here (as reported): On 17 August 2026, in the announcement of The Six Five Summit: AI Unleashed 2026 (25–27 August, Marc Benioff Day 1 keynote), Patrick Moorhead (CEO and Chief Analyst, Moor Insights & Strategy) is quoted saying "AI has moved out of the demo phase and into production, and the enterprise leaders defining that shift are the ones building the platforms, the silicon, the cloud, and the agents that customers actually run." Cited as evidence that the industry's framing has moved from capability to deployment. Separately, Microsoft introduced updates (from 18 August) to help users distinguish work and personal accounts in Copilot — noted only as a parallel identity-boundary signal.

## The gate — the trust layer is live

- European Commission, "Commission starts enforcing AI Act rules and new transparency requirements on 2 August" — https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- European Commission (press corner), IP/26/1714 — https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714
- Cooley, "EU AI Act: Transparency Obligations Take Effect 2 August 2026" — https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
- AIwire / HPCwire, "AI Trust and Security Consortium launches to set peer-defined standards for enterprise AI" (12 Aug 2026) — https://www.hpcwire.com/aiwire/2026/08/12/ai-trust-and-security-consortium-launches-to-set-peer-defined-standards-for-enterprise-ai/

Claims sourced here (as reported): The EU AI Act's transparency duties have been enforceable since 2 August 2026 — including obligations to disclose that a user is interacting with AI and to machine-readable-label AI-generated or manipulated content — with penalties up to the higher of €15 million or 3% of worldwide annual turnover, and up to €35 million or 7% for prohibited practices. These duties are directly relevant to disclosing and logging the actions of agents that act in an enterprise's name. The AI Trust and Security Consortium (AITSC) launched on 12 August 2026 with a founding cohort of roughly 50 enterprise security and technology leaders.

## The rails — the plumbing standardizes

- Official Model Context Protocol blog, "MCP specification 2026-07-28" — https://blog.modelcontextprotocol.io/posts/2026-07-28/

Claims sourced here: The MCP 2026-07-28 specification introduced a stateless protocol core (removing the initialize/initialized handshake and Mcp-Session-Id), cacheable list results, hardened authorization, and a stabilized Enterprise-Managed Authorization extension. The TypeScript and Python SDKs are each past one billion total downloads. Cited here as the rail an agent uses to reach tools and systems — and, once it carries authority, a grant that needs identity and scope attached.

## Prior-day context (background only)

Claims sourced here (context only): This week's earlier editions — "The Far Bank" (17 Aug, MIT NANDA's finding that 95% of gen-AI pilots deliver no measurable P&L impact and the crossing from pilot to value), "The Free Table" (16 Aug, the vendor business model), "The Last Mile" (15 Aug, distribution) and "The Harbor Pilot" (14 Aug, the pilotage/context layer) — are referenced only as prior-day background to the assistance-to-execution thesis.

---

*Editorial lines marked as the radar's own (e.g. "When your cleverest servant stops advising and starts acting, you have not merely gained speed — you have handed out your seal… an act taken in your name cannot be un-taken. Name every deputy, bound every mandate, keep the ledger") are the AI Tech Radar's framing and are not third-party quotes. The deputy / badge / ledger allegory — a house that replaces advising counselors with badged deputies who act in its name, forty deputies per family member, a magistrate who requires each deputy to declare himself, and the discipline of non-forgeable identity, bounded mandate and a complete ledger — is a common illustration used allegorically and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported"; the OpenAI "From assistance to execution" figures, the Google Agent Identity characterization, the non-human-identity ratios, and the Gemini 3.7 Flash / GPT-5.6 Sol Ultrafast details rest partly on secondary coverage of egress-blocked primary pages and should be re-verified at source before republishing. Product, firm and institution names (OpenAI, Google, Cerebras, Z.ai, Alibaba/Qwen, xAI, Moonshot, DeepSeek, Moor Insights & Strategy, Six Five Media, Cloud Security Alliance, the European Commission, AITSC) reflect the sources as described in the cited 2026 material. This edition's central datable development in the window is OpenAI's 13 August "From assistance to execution" report — that the majority of enterprise AI output now comes from an agent (Codex) rather than a chatbot — set against Google's per-agent identity layer, the non-human-identity governance gap, continued engine commoditization built for action (Gemini 3.7 Flash, GPT-5.6 Sol Ultrafast, GLM-5.3, Qwen3.8), and a live governance/trust layer (EU AI Act, AITSC, MCP).*
