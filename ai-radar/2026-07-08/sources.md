# Sources — AI Tech Radar, 8 July 2026 ("Behind the Wall")

Every claim in this edition traces to a public source below. Figures are attributed to the organization that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure is reported via secondary coverage or rests on a single industry source, it is marked "as reported."

## MCP Enterprise-Managed Authorization (EMA) reaches "stable"

- Model Context Protocol Blog, "Enterprise-Managed Authorization: Zero-touch OAuth for MCP" — https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/
- Model Context Protocol, "Enterprise-Managed Authorization" (extension spec) — https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization
- modelcontextprotocol/ext-auth (GitHub), stable EMA specification — https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/stable/enterprise-managed-authorization.mdx
- Claude by Anthropic, "Centrally manage authorization for MCP connectors" — https://claude.com/blog/enterprise-managed-auth
- The New Stack, "MCP gets its missing enterprise authorization layer" — https://thenewstack.io/mcp-gets-its-missing-enterprise-authorization-layer/
- InfoQ, "AI Model Context Protocol Adds Centralised Auth for Enterprise" — https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/
- Ehsan Hosseini, "Enterprise-Managed Authorization for MCP: what it actually does, and what it leaves to you" — https://ehosseini.info/articles/mcp-enterprise-managed-authorization-ema/

Claims sourced here: EMA reached "stable" (18 June 2026); it lets an enterprise provision MCP server access centrally through its identity provider, so a user's connectors are wired up on first login with no per-app OAuth click-through; access decisions and a single auditable trail live in the IdP admin console; Okta is the first supported IdP (via Cross App Access), Anthropic implemented it in Claude's shared MCP layer, VS Code on the client, and Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase (and Slack adding) on the server side. Quote — "Logging in once and automatically having all your MCP connectors automatically setup is pretty magical." — Tom Moor, Head of Engineering, Linear (Model Context Protocol blog).

## MCP 2026-07-28 stateless specification and its new security surface

- Model Context Protocol Blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- SecurityWeek, "New Enterprise-Ready MCP Specification Brings New Security Challenges" — https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/
- Akamai, "The New MCP Specification: What Security Teams Must Prepare For" — https://www.akamai.com/blog/security-research/new-mcp-specification-security-teams-must-prepare
- SecurityWeek, "Claude Code OAuth Tokens Can Be Stolen Through Stealthy MCP Hijacking" — https://www.securityweek.com/claude-code-oauth-tokens-can-be-stolen-through-stealthy-mcp-hijacking/
- arXiv, "Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies" — https://arxiv.org/pdf/2504.08623

Claims sourced here: the 2026-07-28 specification is the largest MCP revision since launch, with a release candidate published 21 May 2026 and a ~ten-week validation window; it removes the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header, making the protocol stateless so any server instance can run behind a plain round-robin load balancer, with metadata in `_meta` and new `Mcp-Method` / `Mcp-Name` routing headers; auth hardening aligns with OAuth 2.0 / OIDC (mandatory `iss` validation per RFC 9207); extensions framework adds MCP Apps and a Tasks extension; the stateless model makes "the state visible to the model rather than hidden away." Security framing (as reported): the enterprise-ready spec "shifts critical security responsibilities from the protocol itself to developers and platform operators"; client-held tracking identifiers, if predictable, risk workflow hijacking, cross-tenant actions and data-access violations; the new headers risk protocol-confusion attacks and leakage of keys, tokens or PII; benefits include an end to session hijacking, no unsolicited server prompts, and stronger auth; organizations have a 12-month window (changes take effect 28 July 2026).

## MCP as the cross-vendor standard — adoption and governance

- andrew.ooo, "MCP Enterprise Adoption: The July 2026 State of Play" — https://andrew.ooo/answers/mcp-model-context-protocol-enterprise-adoption-july-2026/
- WorkOS, "Everything your team needs to know about MCP in 2026" — https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026
- Agentic AI Foundation (AAIF), "MCP Is Growing Up" — https://aaif.io/blog/mcp-is-growing-up/
- Wikipedia, "Model Context Protocol" — https://en.wikipedia.org/wiki/Model_Context_Protocol

Claims sourced here (as reported): ~78% of enterprise AI teams have MCP-backed agents in production; ~28% of Fortune 500 run MCP servers; ~97M monthly SDK downloads; MCP was introduced by Anthropic (Nov 2024) and donated to the Linux Foundation's Agentic AI Foundation (Dec 2025), and is supported across Anthropic, OpenAI, Google, Microsoft, Salesforce and Snowflake.

## Enterprise-AI deployment context and agent adoption

- PYMNTS, "AI Giants Pour Billions Into Enterprise Deployment" — https://www.pymnts.com/news/artificial-intelligence/2026/ai-giants-spend-8-billion-dollars-fix-enterprise-adoption/
- Microsoft Blog, "Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence" — https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/
- TechCrunch, "Microsoft launches its own AI deployment company with $2.5 billion commitment" — https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/
- OpenAI, "Introducing OpenAI Frontier" — https://openai.com/index/introducing-openai-frontier/

Claims sourced here (as reported): Microsoft, OpenAI and Anthropic committed roughly $8B combined into enterprise-AI deployment ventures in 2026; Gartner forecasts 40% of enterprise apps will embed task-specific AI agents by end of 2026 and >40% of agentic AI projects will be cancelled by 2027, while ~70% of developers report problems integrating AI agents with existing systems.

## EU AI Act — GPAI enforcement

- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/
- EU Artificial Intelligence Act, "Implementation Timeline" — https://artificialintelligenceact.eu/implementation-timeline/
- Latham & Watkins, "AI Act Update: EU Resolves to Change Rules and Extend Deadlines" — https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines

Claims sourced here: the Commission's supervision and enforcement powers over GPAI providers, and Article 50 transparency obligations, take effect 2 August 2026; the maximum GPAI penalty is €15M or 3% of global annual turnover, whichever is higher; the Digital Omnibus (political agreement reached 7 May 2026) extends high-risk (Annex III) deadlines while 2 August 2026 remains live for GPAI enforcement and Article 50.

---

*Editorial lines marked "the radar's framing" (e.g. "The socket is the easy part — own the panel"; "A standard becomes infrastructure the day it becomes load-bearing — and infrastructure fails to whoever owns the wiring") are the AI Tech Radar's own and are not third-party quotes. The SecurityWeek line is quoted from its analysis of the 2026-07-28 specification; the Linear quote is from the Model Context Protocol blog's Enterprise-Managed Authorization announcement. Where dates or single-source figures differ across outlets, the edition presents them conservatively and marks them "as reported."*
