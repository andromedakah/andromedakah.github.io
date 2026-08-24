# Sources — AI Tech Radar, 24 August 2026 ("The Gatehouse")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or outlet that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Note: this was a quiet late-August weekend for hard, same-day news; the edition is built from the strongest verifiable recent development — the emergence of the agent/MCP gateway as the enterprise control plane, set against the ungoverned status quo of shadow agents and shadow MCP — rather than from a single 24-hour headline, and says so honestly. Several primary and secondary pages were unreachable from the compile environment behind the network egress proxy; those items were verified by cross-referencing multiple reputable outlets and search summaries and are flagged accordingly.

## The story — the agent/MCP gateway crystallizes as the enterprise control plane

### The gate — the gateway becomes a category

- Snowflake, "Enterprise AI Security: Agentic Controls and MCP Governance" (Cortex AI Gateway, Black Hat 2026) — https://www.snowflake.com/en/blog/enterprise-ai-security-agentic-mcp-governance/
- SiliconANGLE, "Snowflake debuts Cortex AI Gateway to govern and monitor enterprise AI agents" — https://siliconangle.com/2026/07/28/snowflake-debuts-cortex-ai-gateway-govern-monitor-enterprise-ai-agents/
- VentureBeat, "Snowflake launches Cortex AI Gateway to control AI agents and prevent runaway enterprise costs" — https://venturebeat.com/security/snowflake-launches-cortex-ai-gateway-to-control-ai-agents-and-prevent-runaway-enterprise-costs
- Forkast, "Snowflake's Cortex AI Gateway Signals MCP Gateways Are Crystallizing as Infrastructure" — https://forkast.news/snowflakes-cortex-ai-gateway-signals-mcp-gateways-are-crystallizing-as-infrastructure/
- Forbes (Janakiram MSV), "Agent Gateways Are Becoming The Control Plane For Enterprise AI" — https://www.forbes.com/sites/janakirammsv/2026/07/05/agent-gateways-are-becoming-the-control-plane-for-enterprise-ai/
- Enterprise DNA, "Snowflake Launches Cortex AI Gateway for Enterprise Agent Governance" — https://enterprisedna.co/resources/news/snowflake-cortex-ai-gateway-enterprise-agent-governance-july-2026/
- GetAIGovernance, "Snowflake Launches Cortex AI Gateway for Secure Agent Interoperability and Cost Control" — https://getaigovernance.net/blog/snowflake-cortex-ai-gateway-agentic-security
- Preloop, "The AI Agent Control Plane in 2026 — MCP Gateways, Model Gateways, and Human Approvals" — https://preloop.ai/resources/ai-agent-control-plane-2026

Claims sourced here (as reported): At Black Hat 2026, Snowflake launched its Cortex AI Gateway — enforcing identity, policy and audit at the tool-call level, centralizing authentication, permissions and audit logging in one place across more than 100 MCP servers, and applying zero-copy boundaries, dynamic data masking and real-time exfiltration safeguards before an agent touches a row of data. The gateway is built on Natoma (a centralized MCP gateway that enforces identity, policy and audit at the tool-call level), which Snowflake acquired in May 2026, and launched with seven identity partners: 1Password, Aembit, Cyera, Linx Security, Okta, SailPoint and Saviynt. Forbes characterized agent gateways as "the control plane for enterprise AI"; analysts (Forkast and others) described MCP gateways as "crystallizing as infrastructure"; VentureBeat framed the gateway as a way to control agents and prevent runaway costs. These are the "gate" facts. (Note: the Snowflake launch itself dates to late July / Black Hat 2026; the "control plane" / "crystallizing as infrastructure" framing is the recent synthesis carried here as the week's dominant thread.)

### The gaps — the ungoverned status quo (shadow agents)

- Gravitee, "State of AI Agent Security 2026" (survey of 750 CIOs, CTOs and engineering leaders, US + UK) — referenced via secondary coverage
- Airia, "Shadow AI Statistics: Key Data Points Every CISO Needs in 2026" — https://airia.com/blog/shadow-ai-statistics-key-data-points-every-ciso-needs-in-2026/
- Cloud Security Alliance, "The Invisible Enterprise: Shadow AI and the Ungoverned Frontier" — https://labs.cloudsecurityalliance.org/research/csa-whitepaper-shadow-ai-asset-blindness-systemic-risk-20260/
- Questa AI, "Shadow AI in 2026: Statistics, Risks & Enterprise Guide" — https://www.questa-ai.com/privacy-cafe/shadow-ai-the-biggest-data-risk-in-2026

Claims sourced here (as reported): Gravitee's survey of 750 CIOs, CTOs and engineering leaders across US and UK enterprises found that 47% of the roughly 3 million AI agents those firms have deployed are not actively monitored or secured — an estimated 1.5 million agents "at risk of going rogue" — and that 88% of organizations surveyed have already experienced or suspected an AI-agent-related security or data-privacy incident in the last twelve months. (The 88% agent-incident figure was also carried in this radar's 17 and 20 August editions.) These are the "gaps" figures: the ungoverned status quo the gate is built to close.

### The gaps — inventory blindness and shadow MCP

- Zuplo, "Shadow MCP: The Ungoverned AI Agent Tools Putting Your APIs at Risk" — https://zuplo.com/learning-center/shadow-mcp-ungoverned-ai-agent-security
- Qualys, "MCP Servers: The New Shadow IT for AI in 2026 — Qualys TotalAI" — https://blog.qualys.com/product-tech/2026/03/19/mcp-servers-shadow-it-ai-qualys-totalai-2026
- WorkOS, "The tools that caught shadow IT can't see MCP sprawl" — https://workos.com/blog/mcp-sprawl-invisible-to-shadow-it-tools
- Accuro AI, "Shadow MCP: Find the AI Servers You Can't See" — https://accuroai.co/blog/shadow-mcp-finding-ai-servers-security-cant-see

Claims sourced here (as reported): IBM's Think 2026 research found that only 18% of organizations maintain a complete inventory of their AI agents (and MCP servers are a layer below the agents). MCP adoption grew more than 400% in 2025, with the majority of deployments occurring outside any formal security review; MCP-related vulnerabilities increased about 270% from Q2 to Q3 2025, and 315 MCP-related vulnerabilities were published in 2025, accounting for 14.4% of all AI-related vulnerabilities. Gartner projects that shadow AI will be a contributing factor in 40% of enterprise AI failures by 2027. These are the "shadow MCP" figures — the least-governed layer beneath the agent.

### The toll — runaway cost as the driver

- Joget, "AI Agent Adoption 2026: What the Data Shows | Gartner, IDC" — https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
- Portal26, "AI Agent Cost Control: Stop Agents Burning Budget" — https://portal26.ai/ai-agent-cost-control-stop-agents-burning-budget/
- Kosmoy, "6 AI Gateway Trends of 2026: What Held Up by August" — https://www.kosmoy.com/resources/blog/6-ai-gateway-trends-that-will-shape-2026/

Claims sourced here (as reported): Gartner expects more than 40% of agentic-AI projects to be cancelled before production by the end of 2027 over escalating costs, unclear value or weak risk controls. Trade coverage cites concrete runaway-cost examples, including an enterprise reportedly spending on the order of $500 million in a single month after deploying AI access with no usage caps, and reports of a company burning through its annual AI budget within months. Carried here as the cost driver behind the gateway's cost-metering function; treated as "as reported" and, for the dramatic single-figure examples, as illustrative trade reporting to be re-verified before republishing.

### The ledger — compliance in statute

- European Commission, "Commission starts enforcing AI Act rules and new transparency requirements on 2 August" — https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- Salt Security, "EU AI Act Compliance 2026: What High-risk AI Systems Must Do Now" (Article 12 logging) — https://salt.security/eu-ai-act-compliance
- Snowflake blog (MCP governance and Article 12 gateway logs, above) — https://www.snowflake.com/en/blog/enterprise-ai-security-agentic-mcp-governance/
- Gibson Dunn, "EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines and Other Key Changes" — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/

Claims sourced here (as reported): As of 2 August 2026, the European Commission's AI Office, with national authorities, began enforcing the AI Act, and Article 50 transparency rules began to apply. Article 12 requires automatic event logging built for full reconstructability of what a system did, when, and on what basis — which makes audit-grade gateway logs a hard requirement for any agent (or MCP gateway) touching credit, employment, healthcare or critical-infrastructure data. Active enforcement of general-purpose AI (GPAI) rules enables model inspections and market restrictions, with fines up to the higher of €15 million or 3% of worldwide annual turnover. High-risk obligations were deferred to December 2027 and August 2028 under the Digital Omnibus on AI. Cited as the "ledger" in statute — the legal basis for the gate's audit function.

### Market validation — the identity M&A

- Coverage of the end-of-July 2026 agent-identity consolidation (as reported): Snowflake's gateway launch with seven identity partners; Cyera's ~$1 billion acquisition of Oasis; Okta's ~$200 million acquisition of Permiso — relayed via Preloop and secondary deal coverage.

Claims sourced here (as reported): In a 72-hour window at the end of July 2026, the industry saw three major moves in the agent-identity space — the launch of Snowflake's gateway with seven identity partners, Cyera's ~$1 billion acquisition of Oasis, and Okta's ~$200 million acquisition of Permiso. Carried here as market validation that the gateway/agent-identity control plane is consolidating fast.

## The rails — the protocol standardizes (standing context)

- Official Model Context Protocol blog, "The 2026-07-28 Specification" — https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Toloka, "The future of MCP: 2026 roadmap, enterprise adoption, and what comes next" — https://toloka.ai/blog/the-future-of-mcp-enterprise-adoption/

Claims sourced here (as reported): The MCP 2026-07-28 specification introduced a stateless protocol core, an Extensions framework, and the AWS-contributed Tasks extension for reliable long-running agents. In December 2025, Anthropic donated MCP to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, cementing MCP as a vendor-neutral open standard governed by a community process. Cited as the rail the gate governs.

## The engine — commodity models, priced per token (standing context)

- Local AI Zone, "Latest AI Developments: August 2026 Update" — https://local-ai-zone.github.io/blog/ai-updates-august-2026.html
- LLM-Stats, "LLM News Today (August 2026) – AI Model Releases" — https://llm-stats.com/ai-news
- Axis Intelligence, "AI Model Release Tracker 2026" — https://axis-intelligence.com/ai-model-release-tracker/

Claims sourced here (as reported, standing context): August 2026 was described as the fastest month in AI history, with 11+ model releases in roughly 20 days from five or more providers (including Gemini 3.7 Flash, Qwen3.8, DeepSeek V4-Pro GA, NVIDIA Nemotron variants and Claude Opus 5 updates), the pace outrunning the industry's ability to fully test each release. The standing engine field carried as context — Claude Opus 5 (Artificial Analysis Intelligence Index ~63, Agentic Index ~55, at $5/$25 per million tokens), xAI Grok 4.6 (Intelligence Index ~61 at $2/$6), OpenAI GPT-5.6 and GPT-5.6-Luna ($0.20/$1.20), Google Gemini 3.7 Flash, and open-weight Z.ai GLM-5.3 and Alibaba Qwen3.8 — is relayed from model-tracker and vendor coverage as the rented, swappable, per-token-priced model layer whose cost per unit of intelligence keeps falling.

## Prior-day context (background only)

Claims sourced here (context only): This week's earlier editions — "The Reservoir" (23 Aug, the spend-value gap and the trust-gate), "The Locksmith" (22 Aug, agentic AI as a two-edged security actor), "The Guardrail" (21 Aug, agentic adoption outrunning governance), "The Watchman" (20 Aug, oversight without custody) and "The Deputy" (18 Aug, identity/mandate/audit as the control plane) — are referenced only as prior-day background to the gatehouse thesis. In particular, the gateway is the natural culmination of the week's arc: after the deputy that acts, the watchman that sees, the guardrail that bounds and the reservoir's finding that value lives in the plumbing, the market's converging answer is a single governed door.

---

*Editorial lines marked as the radar's own (e.g. "The point was never to keep the agents out. It is to make them all pass one door you control — named, permissioned, inspected, metered and logged. A wall with a hundred gaps is not a wall.") are the AI Tech Radar's framing and are not third-party quotes. The gatehouse allegory — a walled city that let its wall fall into a hundred gaps for the speed of trade, then found it could neither see, permit, price nor prove who passed until it built a single gatehouse every cart had to enter — is a common illustration used allegorically and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported." Product, firm and institution names (Snowflake, Natoma, Gravitee, IBM, Gartner, Forbes, Cyera, Oasis, Okta, Permiso, 1Password, Aembit, Linx Security, SailPoint, Saviynt, Qualys, Zuplo, the European Commission, the Linux Foundation / Agentic AI Foundation, and the model vendors) reflect the sources as described in the cited 2026 material. Several primary and secondary pages were unreachable behind the network egress proxy and the figures were cross-referenced across multiple reputable outlets; they should be re-verified at source before republishing. This edition's central development in the window is the crystallization of the agent/MCP gateway as the enterprise control plane — the single governed point through which every agent's access to models, data and tools is routed, named, permissioned, metered and logged — set against the ungoverned status quo (47% of agents unmonitored, 18% inventoried, MCP adoption up 400% with 315 logged vulnerabilities) and made a legal requirement by the EU AI Act's Article 12 logging duties.*
