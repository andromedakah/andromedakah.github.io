# Sources — AI Tech Radar, 7 August 2026 ("The Keyring")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or official that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Details drawn directly from the Model Context Protocol's product documentation/blog are marked "as documented."

## The story — own the keyring: Okta Cross App Access on MCP's Enterprise-Managed Authorization

### The standard — MCP Enterprise-Managed Authorization (stable) + the 7-28 spec

- Model Context Protocol Blog, "Enterprise-Managed Authorization: Zero-touch OAuth for MCP" — https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/
- Model Context Protocol Blog, "The 2026-07-28 MCP Specification Release Candidate" (final 7-28 spec: stateless core, Extensions framework, Tasks, MCP Apps, authorization hardening, deprecation policy) — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Model Context Protocol, "What is the Model Context Protocol (MCP)?" — https://modelcontextprotocol.io/docs/getting-started/intro
- InfoQ, "AI Model Context Protocol Adds Centralised Auth for Enterprise" — https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/
- Web Developer, "MCP Enterprise-Managed Authorization Goes Stable, Bringing Zero-Touch SSO to Agent Tooling" — https://webdeveloper.com/news/mcp-enterprise-managed-authorization-stable/
- TechTimes, "MCP Enterprise Authorization Goes Stable: Zero-Touch SSO for Okta, Anthropic, VS Code" — https://www.techtimes.com/articles/318708/20260619/mcp-enterprise-authorization-goes-stable-zero-touch-sso-okta-anthropic-vs-code.htm

Claims sourced here: The Model Context Protocol's Enterprise-Managed Authorization (EMA) extension reached stable status on 18 June 2026, and the 2026-07-28 MCP specification is final (as documented). Per the MCP Blog (as documented): organizations centrally provision MCP server access through their identity provider, so users get connected servers on first login without per-app OAuth; the client obtains an Identity Assertion JWT Authorization Grant (ID-JAG) from the IdP and exchanges it for an access token scoped to the user's groups and roles; there are no per-server consent screens. Okta is the first supported identity provider (via Cross App Access); supported clients include Anthropic's Claude, Claude Code and Cowork, and Visual Studio Code; supported servers include Asana, Atlassian, Canva, Figma, Granola, Linear and Supabase, with Slack actively adding support. The quote from Tom Moor (Head of Engineering, Linear) — "Logging in once and automatically having all your MCP connectors automatically set up is pretty magical" — is relayed as reported.

### Okta Cross App Access (XAA) — general availability and the Anthropic partnership

- Okta (Newsroom), "Okta advances the industry standard for secure AI agent connections with expanding Cross App Access ecosystem" — https://www.okta.com/newsroom/press-releases/okta-announces-cross-app-access-partners/
- Okta (Newsroom), "Okta becomes a featured identity provider powering secure AI agent connections for Anthropic's Claude Enterprise" — https://www.okta.com/newsroom/press-releases/okta-becomes-a-featured-identity-provider-powering-secure-ai-agent-connections-for-claude-enterprise/
- Okta, "Cross App Access — Controlling AI Agent and App Connections" — https://www.okta.com/solutions/cross-app-access/
- Okta, "Cross App Access: Securing AI agent and app-to-app connections" — https://www.okta.com/identity-101/cross-app-access-securing-ai-agent-and-app-to-app-connections/
- SiliconANGLE, "Okta expands Cross App Access ecosystem to secure AI agent connections" — https://siliconangle.com/2026/06/23/okta-expands-cross-app-access-ecosystem-secure-ai-agent-connections/
- Okta (Newsroom), "Okta introduces Cross App Access to help secure AI agents in the enterprise" — https://www.okta.com/newsroom/press-releases/okta-introduces-cross-app-access-to-help-secure-ai-agents-in-the/
- explainx.ai, "Claude Enterprise-Managed Auth: Zero-Touch MCP via Okta 2026" — https://explainx.ai/blog/anthropic-claude-enterprise-managed-auth-mcp-okta-2026
- Cyber Magazine, "How Okta & Anthropic Are Partnering on XAA, MCP & Glasswing" — https://cybermagazine.com/news/how-okta-anthropic-are-partnering-on-xaa-mcp-glasswing

Claims sourced here (as reported): Okta's Cross App Access (XAA) — an extension of OAuth that secures agent-driven and app-to-app interactions — reaches general availability for Okta Workforce customers through the Okta Integration Network starting August 2026. XAA replaces per-application, "allow"-style consent prompts with policy-based access decisions managed by the identity provider, giving admins visibility and control over which agents reach which apps while eliminating consent fatigue. Anthropic has named Okta a featured identity provider for Claude, Claude Code and Cowork, building on a beta with joint customers including HubSpot, Ramp and Webflow. Named ecosystem partners/adopters include Asana, Atlassian, Cloudflare, Datadog, Salesforce's Slack, Zoom and Anthropic's Claude. The quote from Mayank Malhotra (Anthropic) — "Enterprise-managed auth gives MCP the foundation it needs to scale across an enterprise, with Okta as our first identity provider partner. When an admin authorises a connector once for the whole organisation, every employee gets instant access to more of their tools through Claude, governed by the IDP they already trust." — is relayed from trade coverage as reported.

## The scale — why the keyring shipped now (non-human identity sprawl)

- Palo Alto Networks, "2026 Identity Security Landscape" — https://www.paloaltonetworks.com/resources/research/identity-security-landscape
- Axis Intelligence, "Machine Identity Statistics 2026: Non-Human Identity Ratios, Secrets Sprawl, and Certificate Lifecycle Data" — https://axis-intelligence.com/machine-identity-statistics/
- GitGuardian, "State of Secrets Sprawl 2026" — https://www.gitguardian.com/state-of-secrets-sprawl-report-2026
- Cloud Security Alliance, "The Non-Human Identity Governance Vacuum (Agentic AI)" — https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/

Claims sourced here (as reported): Palo Alto Networks' 2026 Identity Security Landscape found that machine identities, including AI agents, now outnumber human identities roughly 109 to 1, of which about 79 are AI agents (roughly 72.5% of machine identities), up from about 82 to 1 a year earlier (an increase of about a third in a single year). Other 2026 reports (GitGuardian, KPMG) cite ratios of roughly 80-to-1; the exact ratio varies by methodology.

## The demand signal — agents at enterprise scale

- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up from Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- DigitalApplied, "AI Agent Adoption 2026: 120+ Enterprise Data Points" (S&P Global / McKinsey production figures) — https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
- IDC (via analyst coverage), on AI proof-of-concept-to-production rates — https://www.idc.com/
- Forrester, on enterprise vendors shipping MCP servers in 2026 — https://www.forrester.com/

Claims sourced here (as reported): Gartner projects that 40% of enterprise applications will feature task-specific AI agents by 2026, up from less than 5% in 2025. Roughly 31% of enterprises have at least one AI agent in production (S&P Global Market Intelligence / McKinsey), with banking and insurance leading (~47%) and healthcare and government trailing (~18%). IDC found that 88% of AI proofs-of-concept never reach widescale deployment. Forrester projects that a growing share of enterprise application vendors will ship MCP servers in 2026.

## The regulatory backdrop — EU AI Act enforcement, still live

- European Commission (Press corner), "Commission starts enforcing AI Act rules and new transparency requirements on 2 August" — https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714
- Wilson Sonsini, "EU AI Act Enforcement Phase Begins" — https://www.wsgr.com/en/insights/eu-ai-act-enforcement-phase-begins.html
- Help Net Security, "EU begins enforcing AI Act, putting AI models under the microscope" (4 August 2026) — https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/
- EU Artificial Intelligence Act, "Article 11: Technical Documentation" — https://artificialintelligenceact.eu/article/11/
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/

Claims sourced here (as reported): EU AI Act enforcement has been live since 2 August 2026, with the AI Office empowered to request documentation from GPAI providers, evaluate models, demand risk-mitigation measures, and fine up to the higher of €15 million or 3% of worldwide annual turnover (Article 99), with €7.5 million or 1.5% for incorrect information. More than 180 organizations signed the GPAI Code of Practice; France designated CNIL as its national competent authority. On 4 August 2026 CNIL issued formal information requests to 14 financial institutions running credit-scoring algorithms, demanding the Article 11 technical documentation; the CNIL specifics rest on secondary coverage.

## The engine — commodity models (context)

- LLM-Stats, "AI Updates Today (August 2026) – Latest AI Model Releases" — https://llm-stats.com/llm-updates
- Evertune, "AI Model Release Tracker" — https://www.evertune.ai/resources/ai-model-tracker
- FelloAI, "Best AI Models in August 2026: ChatGPT, Claude, Gemini & Grok" — https://felloai.com/best-ai-models/

Claims sourced here (as reported): Claude Opus 5 (ranked first, Intelligence Index 61 / Agentic Index 55.3 at $5/$25 per million tokens), Google Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3 open weights, and DeepSeek V4-Flash-0731 (MIT-licensed open weights) are relayed from model-tracker and vendor coverage as reported.

---

*Editorial lines marked as the radar's own (e.g. "The model is the worker's brain — rented and swappable. The keyring is yours, or it is a thousand loose keys on a hundred untracked belts.") are the AI Tech Radar's framing and are not third-party quotes. The keyring allegory — a great house whose steward holds one ring and cuts each key to a single room — is a common illustration used allegorically, told approximately, and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported"; details drawn from the Model Context Protocol's blog/documentation are marked "as documented." Product, firm and institution names (Okta, Cross App Access, Model Context Protocol, Anthropic, Claude, Claude Code, Cowork, Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase, Slack, Cloudflare, Datadog, Zoom, HubSpot, Ramp, Webflow, Gartner, S&P Global, McKinsey, IDC, Forrester, Palo Alto Networks, the European Commission, the EU AI Office, CNIL, OpenAI, Google, DeepSeek, Moonshot) reflect the sources as described in the cited 2026 material.*
