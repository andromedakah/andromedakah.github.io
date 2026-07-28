# Sources — AI Tech Radar, 28 July 2026 ("The Mailroom")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or official that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported."

## The story — the universal connector goes stateless, and the security boundary moves onto you

### MCP 2026-07-28 specification goes final (28 July 2026)

- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Model Context Protocol blog, "Beta SDKs for the 2026-07-28 MCP Spec Release Candidate Are Here" — https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/
- The Register, "Model Context Protocol prepares to break with its stateful past" — https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/
- WorkOS, "The biggest MCP spec update ships July 28: What changes for AI agent authentication" — https://workos.com/blog/mcp-2026-spec-agent-authentication
- TechTimes, "AI Tool Protocol Drops Sessions Tomorrow: MCP's Largest Spec Change Since Launch" — https://www.techtimes.com/articles/321671/20260727/ai-tool-protocol-drops-sessions-tomorrow-mcps-largest-spec-change-since-launch.htm
- Stacktree, "MCP 2026-07-28 spec: what changed, what breaks" — https://stacktr.ee/blog/mcp-2026-spec-changes
- DigitalApplied, "MCP Goes Stateless July 28: What Breaks, What Gets Cheaper" — https://www.digitalapplied.com/blog/mcp-2026-07-28-spec-stateless-migration-guide

Claims sourced here (as reported): The MCP 2026-07-28 specification went final on 28 July 2026 — the largest revision since the protocol's 2024 debut. Six coordinated Specification Enhancement Proposals make the core stateless: SEP-2575 removes the `initialize`/`initialized` handshake; SEP-2567 removes the `Mcp-Session-Id` header and protocol-level sessions; SEP-2243 adds routing headers (`Mcp-Method`, `Mcp-Name`); so "any MCP request can land on any server instance" and remote servers that once needed sticky sessions and shared session stores now run behind a plain round-robin load balancer. Three legacy features — Roots, Sampling, Logging — are deprecated under SEP-2577 with at least a 12-month window before removal. Authorization is rewritten to align with OAuth 2.1 and OpenID Connect (validate the `iss` per RFC 9207; declare OIDC `application_type`). Two extensions ride the same audit-and-consent path as a tool call: MCP Apps (sandboxed HTML UIs, SEP-1865) and Tasks (long-running work, SEP-2663). The release candidate was published earlier in 2026 with a validation window before the 28 July final date.

### MCP adoption and governance

- news.bitcoin.com, "MCP in 2026: 97 Million Downloads and Growing Crypto Infrastructure" — https://news.bitcoin.com/mcp-in-2026-97-million-downloads-and-growing-crypto-infrastructure-from-bitgo-to-coingecko/
- Tech Insider Ireland, "MCP Hits 10,000+ Servers as Biggest Update Ships [2026]" — https://tech-insider.org/ie/model-context-protocol-mcp-update-2026/
- Effloow, "MCP Ecosystem in 2026: From Experiment to 97 Million Installs" — https://effloow.com/articles/mcp-ecosystem-growth-100-million-installs-2026
- DigitalApplied, "MCP Adoption Statistics 2026: Model Context Protocol" — https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol

Claims sourced here (as reported): MCP's Python and TypeScript SDKs reached roughly 97 million monthly downloads (up from ~100,000 at late-2024 launch), with more than 10,000 active MCP servers across public and enterprise deployments as of early 2026. In December 2025 Anthropic donated MCP to the newly formed Agentic AI Foundation (AAIF) under the Linux Foundation, with OpenAI and Block among the co-founders and platinum members including AWS, Google, Microsoft, Cloudflare, GitHub and Bloomberg.

### The security shift — a stateless protocol relocates the boundary to the implementer

- SecurityWeek, "New Enterprise-Ready MCP Specification Brings New Security Challenges" — https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/
- Akamai, "The New MCP Specification: What Security Teams Must Prepare For" — https://www.akamai.com/blog/security-research/new-mcp-specification-security-teams-must-prepare
- Security Boulevard, "Akamai Report Details MCP Security Weaknesses" — https://securityboulevard.com/2026/06/akamai-report-details-mcp-security-weaknesses/
- news4hackers, "Enterprise-Grade MCP Specification Introduces Critical Security Challenges" — https://www.news4hackers.com/enterprise-grade-mcp-specification-introduces-critical-security-challenges
- RockCyber, "MCP Authorization Scope Is the Hole the New Spec Handed You" — https://www.rockcybermusings.com/p/mcp-authorization-scope-spec-gap

Claims sourced here (as reported): Maxim Zavodchik, Senior Director of Threat Research at Akamai, said that "since the protocol is transitioning to a stateless model and introducing rich UI apps and asynchronous tasks, critical security boundaries are now entirely dependent on how developers implement them," and that "while the update improves the foundation by eliminating older protocol-level risks, implementation choices will now dictate the overall security posture." Coverage enumerates the implementation-dependent failure modes: workflow hijacking and cross-tenant access; privilege escalation and secrets leakage; header/body inconsistencies that bypass security controls; hit-and-run DoS attacks against long-running tasks; and malicious script execution and phishing through insecure UI panels. The move to statelessness addresses session hijacking but shifts responsibility for security to developers and platform operators.

## The market prices the layer — Gartner (20 July 2026)

- Gartner, "Gartner Forecasts Worldwide AI Platforms and Models Market to Grow 63% in 2026" — https://www.gartner.com/en/newsroom/press-releases/2026-07-20-gartner-forecasts-worldwide-ai-platforms-and-models-market-to-grow-63-percent-in-2026
- HPCwire / AIwire, "Gartner Forecasts Worldwide AI Platforms and Models Market to Grow 63% in 2026" — https://www.hpcwire.com/aiwire/2026/07/20/gartner-forecasts-worldwide-ai-platforms-and-models-market-to-grow-63-in-2026/
- eletimes.ai, "Gartner Forecasts … Biggest Winners Will Be Vendors That Help Enterprises Manage Where and How AI is Used" — https://www.eletimes.ai/gartner-forecasts-worldwide-ai-platforms-and-models-market-to-grow-63-in-2026-biggest-winners-will-be-vendors-that-help-enterprises-manage-where-and-how-ai-is-used

Claims sourced here (as reported): Gartner forecasts worldwide end-user spending on AI models and platforms to total $64 billion in 2026, up 63.4% from $39 billion in 2025; spending on GenAI models is forecast to grow 117%, AI platform spending 36.9%, and domain-specific language models / specialized models 210% in 2026. Arunasree Cheparthi, Senior Principal Research Analyst at Gartner, is quoted that "over the long-term, the biggest winners will be vendors that help enterprises manage where and how AI is used across the business."

## The readiness gap — Arctera State of AI Governance 2026 (21 July 2026)

- GlobeNewswire / Arctera, "Arctera State of AI Governance 2026 Finds More Than Three-Quarters (78%) of Organizations Using AI Expect Communications Risk to Rise, But Fewer Than One in Five Can Prove AI Governance Readiness" — https://www.globenewswire.com/news-release/2026/07/21/3330375/0/en/arctera-state-of-ai-governance-2026-finds-more-than-three-quarters-78-of-organizations-using-ai-expect-communications-risk-to-rise-but-fewer-than-one-in-five-can-prove-ai-governanc.html
- IT Brief UK, "AI governance gap leaves firms unable to prove decisions" — https://itbrief.co.uk/story/ai-governance-gap-leaves-firms-unable-to-prove-decisions
- vmblog, "Arctera State of AI Governance 2026" — https://vmblog.com/news/arctera-state-of-ai-governance-2026-finds-more-than-three-quarters-78-of-organizations-using-ai-expect-communications-risk-to-rise-but-fewer-than-one-in-five-can-prove-ai-governance-readiness/

Claims sourced here (as reported): In Arctera's "State of AI Governance 2026" (a Hanover Research–commissioned survey of ~500 full-time professionals in finance, healthcare and energy/utilities across the Americas and EMEA, all decision-makers or influencers on compliance), 78% expect AI-assisted communications risk to increase over the next 12–24 months; 55% have core AI policies, training and review steps in place; but fewer than one in five (19%) have the logging, retention, detection and scoring controls needed to prove what their AI produced, who reviewed it, where it went and whether the record was kept.

## Supporting context

### Claude Opus 5 (24 July 2026)

- Coursiv, "Claude Opus 5: Benchmarks, Pricing, and Full Guide (July 2026)" — https://coursiv.io/blog/claude-opus-5
- Fello AI, "Claude Opus 5: Pricing, Benchmarks & Effort Setting" — https://felloai.com/claude-opus-5/

Claims sourced here (as reported): Anthropic released Claude Opus 5 on 24 July 2026 at $5 per million input tokens / $25 per million output tokens, and independent testing (Artificial Analysis) ranked it #1 on both its Intelligence and Agentic indices at launch.

### Kimi K3 open weights (27 July 2026)

- VentureBeat, "China's Moonshot AI releases Kimi K3, the largest open-source model ever" — https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems
- TECHi, "Kimi K3's open weights arrive July 27. The catch is 1.4TB" — https://www.techi.com/kimi-k3-open-weights-inference-economics/

Claims sourced here (as reported): Moonshot AI published the full open weights of Kimi K3 (a 2.8-trillion-parameter mixture-of-experts model under a Modified MIT license) at 00:00 UTC on 27 July 2026.

### Fireworks AI Series D and other enterprise items

- Solutions Review, "AI News for the Week of July 24; Updates from Booz Allen, Gartner, Microsoft & More" — https://solutionsreview.com/ai-news-for-the-week-of-july-24-updates-from-booz-allen-gartner-microsoft-more/

Claims sourced here (as reported): Fireworks AI raised $1.5 billion in a Series D round; Block introduced "Buzz," an agentic workspace for human–AI collaboration in operational workflows (referenced as context for the market's shift toward orchestration and cost control).

### EU AI Act — Article 50 transparency and GPAI enforcement (2 August 2026)

- European Commission, "Transparency obligations under Article 50 of the AI Act" (FAQ) — https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- EU Artificial Intelligence Act, "The EU AI Act's Transparency Rules: A Practical Guide to Article 50" — https://artificialintelligenceact.eu/transparency-rules-article-50/
- ComplianceHub, "What Actually Comes Due on August 2, 2026: EU AI Act Article 50 Transparency and the Digital Omnibus Reset" — https://compliancehub.wiki/eu-ai-act-article-50-transparency-digital-omnibus-2026/

Claims sourced here: On 2 August 2026, Article 50 transparency obligations (chatbot/agent disclosure, machine-readable marking of AI-generated content, deepfake labeling) become enforceable across all 27 member states, and the Commission's GPAI enforcement powers apply — both carrying the higher of €15 million or 3% of global turnover under Article 99. A narrow grace to 2 December 2026 applies only to the marking/detection obligation for AI-generated content already on the market before 2 August 2026.

### Supporting governance figure (continuing thread)

- OutSystems survey of ~1,900 IT leaders (only 12% of enterprises say they can centrally govern their AI agents) — relayed via coverage (as reported).

---

*Editorial lines marked as the radar's own (e.g. "A universal standard standardizes the envelope, not the safety of what's inside. Adopt the protocol — and own the mailroom.") are the AI Tech Radar's framing and are not third-party quotes. The mailroom allegory — the historical shift from a local post whose postmaster provided security by acquaintance to a universal, standardized postal system that guarantees the envelope moves but not the safety of its contents, and the resulting need to run one's own mailroom (sender verification, inbound scanning, locked per-recipient boxes, and a delivery logbook) — is a well-worn illustration used allegorically, told approximately, and is not a sourced claim about any specific postal system or about MCP. The "5 days" figure is a simple count from this edition's date (28 July 2026) to 2 August 2026 and is the radar's own. Product, firm, protocol, analyst and institute names (Model Context Protocol, Agentic AI Foundation, Linux Foundation, Akamai, SecurityWeek, Gartner, Arctera, Hanover Research, Anthropic, Claude Opus 5, Artificial Analysis, Moonshot AI, Kimi K3, Fireworks AI, Block, OutSystems, the European Commission) reflect the sources as described in the cited 2026 material. SEP identifiers and technical specifics are relayed from the Model Context Protocol blog as reported.*
