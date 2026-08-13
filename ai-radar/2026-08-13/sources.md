# Sources — AI Tech Radar, 13 August 2026 ("The Blossom Price")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or outlet that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Note: several primary publisher pages sit behind paywalls or were unreachable at compile time; those items were verified by cross-referencing multiple reputable outlets and are flagged accordingly.

## The story — the market prices agents by the blossom, not the fruit

### The signal — Cognition (Devin) reported in talks at ≥$40B

- TechCrunch, "AI coding startup Cognition reportedly already in talks to raise at $40B valuation" — https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/
- Bloomberg, "AI startup Cognition in new funding talks at $40 billion value" (12 Aug 2026) — https://www.bloomberg.com/news/articles/2026-08-12/ai-startup-cognition-in-new-funding-talks-at-40-billion-value
- TechCrunch (prior round, context), "AI coding startup Cognition raises $1B at $25B pre-money valuation" (May 2026) — https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/

Claims sourced here (as reported): On 12 August 2026, Cognition — the AI-coding company behind the Devin agent — was reported to be in talks to raise more than $1 billion at a valuation of at least $40 billion, up from a ~$26 billion valuation ($1B raised at a $25B pre-money) three months earlier, on a revenue run-rate now approaching $1 billion (roughly double the ~$492M cited at the May round). The implied ~40× forward-revenue multiple is an arithmetic implication of the reported valuation and run-rate, not a figure disclosed by the company. The Scott Wu quotation (Devin usage "growing roughly 50% month over month") is relayed from TechCrunch coverage as reported. The orchard / blossom-price allegory is the radar's framing.

### The headwind — the AI ROI gap

- Netguru, "AI adoption statistics 2026" (relaying PwC's 2026 Global CEO Survey) — https://www.netguru.com/blog/ai-adoption-statistics

Claims sourced here (as reported, approximate): PwC's 2026 Global CEO Survey reports that 56% of CEOs saw no measurable AI ROI in the past 12 months, while 91% of businesses use AI and roughly 65% of enterprises raised AI budgets (median +22% year over year). Figures are relayed from secondary coverage of the PwC survey and are approximate.

## The harvest, for real — agents that are shipping value

- Salesforce Investor Relations, "Salesforce Delivers Record First Quarter Fiscal 2027 Results" — https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-First-Quarter-Fiscal-2027-Results/default.aspx
- CNBC, "Salesforce Q1 fiscal 2027 earnings" — https://www.cnbc.com/2026/05/27/salesforce-crm-q1-earnings-report-2027.html
- Motley Fool, "Microsoft (MSFT) Q4 2026 earnings call transcript" — https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/
- Microsoft Learn, "Microsoft 365 Copilot release notes (August 2026)" — https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

Claims sourced here (as reported): Salesforce reported Agentforce ARR of ~$1.2B (+205% YoY), combined Agentforce + Data 360 ARR of ~$3.4B (+200% YoY), 3.8B agentic work units delivered to date, and 28.6T tokens processed, in its Q1 FY2027 results (reported 27 May 2026 — the latest available; Q2 FY2027 was not yet published at compile time). Microsoft's AI business run-rate is cited at ~$37B, and Satya Nadella's remarks that roughly one in three GitHub pull requests now involve an agent, and on the shift from end-user-driven to agent-driven workloads, are relayed from Q4 FY2026 earnings-call coverage as reported (primary transcript egress-blocked at compile time; verify verbatim at source before republishing).

## The trust gate — poured this week

- AIwire / HPCwire, "AI Trust and Security Consortium launches to set peer-defined standards for enterprise AI" (12 Aug 2026) — https://www.hpcwire.com/aiwire/2026/08/12/ai-trust-and-security-consortium-launches-to-set-peer-defined-standards-for-enterprise-ai/
- European Commission, "Commission starts enforcing AI Act rules and new transparency requirements from 2 August" — https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714
- Cooley, "EU AI Act transparency obligations take effect 2 August 2026" — https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
- CNBC, "White House dictates access to newest frontier AI models" — https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html

Claims sourced here (as reported): The AI Trust and Security Consortium (AITSC) launched on 12 August 2026, opening applications for a founding cohort of roughly 50 enterprise security and technology leaders to set peer-defined standards for enterprise AI deployment and governance. The EU AI Act's GPAI oversight and transparency duties have been enforceable since 2 August 2026 — including obligations to disclose that a user is interacting with AI and to machine-readable-label AI-generated or manipulated content — with penalties up to the higher of €15 million or 3% of worldwide annual turnover. The US is reported to be gating access to the newest frontier models (e.g., a requested gate on GPT-5.6; vetted partner tiers such as OpenAI's "Daybreak").

## The rails — the plumbing standardizes

- Official Model Context Protocol blog, "MCP specification 2026-07-28" — https://blog.modelcontextprotocol.io/posts/2026-07-28/

Claims sourced here: The MCP 2026-07-28 specification introduced a stateless protocol core (removing the `initialize`/`initialized` handshake and `Mcp-Session-Id`), header-based routing, cacheable list results, Multi Round-Trip Requests, hardened authorization (RFC 9207 issuer validation; a move from Dynamic Client Registration to Client ID Metadata Documents), and a stabilized Enterprise-Managed Authorization extension. Adoption is cited at roughly 500 million SDK downloads a month, with the TypeScript and Python SDKs each past one billion total downloads.

## The roots — commodity models

- LLM-Stats, "AI news / Open LLM leaderboard" — https://llm-stats.com/ai-news
- DeepLearning.AI, The Batch, "Kimi K2.6 matches open Qwen 3.6 Max and DeepSeek V4 falls just behind top closed models" — https://www.deeplearning.ai/the-batch/kimi-k2-6-matches-open-qwen3-6-max-anddeepseek-v4-falls-just-behind-top-closed-models
- CNBC, "OpenAI expanding GPT-5.6 model release" — https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html
- Anthropic newsroom (Opus 5, egress-blocked at compile time — verify) — https://www.anthropic.com/news

Claims sourced here (as reported, standing context): Claude Opus 5, GPT-5.6, Google Gemini 3.6 Flash, Moonshot Kimi K3 (reported at the top of open-weight leaderboards) and DeepSeek V4 Flash (pricing cited at ~$0.14 per million input / ~$0.28 per million output tokens, cache-miss) are relayed from model-tracker and vendor coverage as the rented, swappable "roots" of the stack.

## Prior-week context (covered in the 12 August edition)

- CNBC, "Nvidia taps Wall Street asset managers in $500 billion AI push" — https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html
- Fortune, "Nvidia's private-capital deal and the 'circular financing' question" — https://fortune.com/2026/08/12/nvidia-private-capital-deal-circular-financing-ai-boom/

Claims sourced here (context only): Nvidia's ~$500B AI-infrastructure financing alliance (with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR) and the Anthropic × Macquarie × GIC data-center venture are referenced as the prior week's development — the financing of the compute "road" — and were the subject of the 12 August 2026 edition ("The Toll Road").

---

*Editorial lines marked as the radar's own (e.g. "Blossom is a promise; fruit is a fact — and a long season stands between them. Price the agent by the harvest in your barn, not the bloom on the branch…") are the AI Tech Radar's framing and are not third-party quotes. The orchard / blossom-price allegory — an orchard town that begins pricing its trees by their spring bloom rather than their autumn harvest — is a common illustration used allegorically, told approximately, and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported"; the flagged verbatim quotes (Nadella, Karp) rest on secondary coverage of egress-blocked primary pages and should be re-verified at source before republishing. The implied ~40× forward-revenue multiple for Cognition is the radar's arithmetic on the reported valuation and run-rate, not a company disclosure. Product, firm and institution names (Cognition, Devin, Salesforce, Microsoft, GitHub, Palantir, OpenAI, Anthropic, Google, Moonshot, DeepSeek, Nvidia, Macquarie, GIC, the European Commission, AITSC) reflect the sources as described in the cited 2026 material. This edition's central datable development in the window is Cognition's reported ≥$40B funding talks (12 August), set against the PwC ROI backdrop, a governance/trust layer going live (AITSC, EU AI Act), standardizing agent rails (MCP), and continued model commoditization.*
