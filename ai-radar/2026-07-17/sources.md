# Sources — AI Tech Radar, 17 July 2026 ("The Standard Coupling")

Every claim in this edition traces to a public source below. Figures are attributed to the organization that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." The MCP specification is a live, versioned standard; the 28 July 2026 revision described here was a release candidate at press time, with the final specification scheduled to publish on that date.

## The story — MCP's 2026-07-28 specification (stateless core, Extensions, Tasks, MCP Apps, deprecation policy)

- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Model Context Protocol blog (index) — https://blog.modelcontextprotocol.io/
- The New Stack, "MCP's biggest growing pains for production use will soon be solved" (roadmap 2026) — https://thenewstack.io/model-context-protocol-roadmap-2026/
- MCP.Directory, "MCP 2026-07-28: The Stateless Release Candidate, Explained" — https://mcp.directory/blog/mcp-2026-07-28-release-candidate
- Stacktree, "MCP 2026-07-28 spec: what changed, what breaks" — https://stacktr.ee/blog/mcp-2026-spec-changes
- Médéric Hurier (Fmind), "MCP 2026-07-28: Stateless core, enterprise authorization, and SDK betas" — https://fmind.medium.com/mcp-2026-07-28-stateless-core-enterprise-authorization-and-sdk-betas-2646a980d594
- Model Context Protocol — Wikipedia (MCP introduced by Anthropic, November 2024) — https://en.wikipedia.org/wiki/Model_Context_Protocol

Claims sourced here: The next MCP specification — its largest revision since MCP's November-2024 debut — goes final on 28 July 2026 (a release candidate at press time). Its stateless core removes the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header; client context now travels in `_meta` on every request, so any request can land on any server instance behind a plain round-robin load balancer, with no sticky sessions or shared session store. The Extensions framework becomes first-class (reverse-DNS identifiers, capability negotiation); the Tasks feature graduates from core to an extension; MCP Apps (SEP-1865) let servers ship interactive HTML rendered by hosts in a sandboxed iframe, with UI-initiated actions traveling the same JSON-RPC audit/consent path as a direct tool call; authorization is hardened (OAuth 2.0 / OpenID Connect alignment, including RFC 9207 `iss` validation); and a formal deprecation policy (Active → Deprecated → Removed, ≥12-month windows) deprecates Roots, Sampling and Logging. The "11 days" figure is a simple count from this edition's date (17 July 2026) to 28 July 2026 and is the radar's own.

## Enterprise-Managed Authorization (EMA) going stable; beta SDKs

- InfoQ, "AI Model Context Protocol Adds Centralised Auth for Enterprise" — https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/
- TechTimes, "MCP Enterprise Authorization Goes Stable: Zero-Touch SSO for Okta, Anthropic, VS Code" — https://www.techtimes.com/articles/318708/20260619/mcp-enterprise-authorization-goes-stable-zero-touch-sso-okta-anthropic-vs-code.htm
- Web Developer, "MCP Enterprise-Managed Authorization Goes Stable, Bringing Zero-Touch SSO to Agent Tooling" — https://webdeveloper.com/news/mcp-enterprise-managed-authorization-stable/
- MCP.Directory, "MCP Enterprise-Managed Authorization (2026)" — https://mcp.directory/blog/mcp-enterprise-managed-authorization-2026
- Ehsan Hosseini, "Enterprise-Managed Authorization for MCP: what it actually does, and what it leaves to you" — https://ehosseini.info/articles/mcp-enterprise-managed-authorization-ema/

Claims sourced here (as reported): MCP's Enterprise-Managed Authorization (EMA) extension went stable on 18 June 2026. It makes the organization's identity provider the authority for MCP server access: a client obtains an Identity Assertion JWT Authorization Grant (ID-JAG) during SSO and exchanges it for an access token from the MCP server's authorization server, so the user is never redirected through a per-server consent screen and engineers no longer paste personal API keys into local agent configs. EMA had support from an initial set of MCP servers and clients (including Okta, Anthropic's shared MCP layer, and VS Code). Beta SDKs for Python, TypeScript, Go and C# shipped on 29 June 2026 so teams could test the new revision.

## The security surface of the new spec

- SecurityWeek, "New Enterprise-Ready MCP Specification Brings New Security Challenges" — https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/
- Akamai, "The New MCP Specification: What Security Teams Must Prepare For" — https://www.akamai.com/blog/security-research/new-mcp-specification-security-teams-must-prepare
- TrueFoundry, "MCP Security Risks & Best Practices: Enterprise Guide" — https://www.truefoundry.com/blog/mcp-security-risks-best-practices

Claims sourced here (as reported): Akamai's security researchers flag new, implementation-dependent risks in the stateless model, MCP Apps and the Tasks extension. The introduction of application-managed state, rich interactive AI interfaces, and long-running asynchronous tasks creates new avenues for abuse — including unauthorized access to customer data, user-targeted phishing through trusted AI experiences, the bypass of enterprise security controls, and service disruption through abuse of background-processing workflows.

## Stewardship and scale of the MCP ecosystem

- Agentic AI Foundation (AAIF), "MCP Is Growing Up" — https://aaif.io/blog/mcp-is-growing-up/
- WorkOS, "Everything your team needs to know about MCP in 2026" — https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026
- Anthropic, "Introducing the Model Context Protocol" — https://www.anthropic.com/news/model-context-protocol

Claims sourced here (as reported): Over 10,000 MCP servers had been published as of early 2026. In December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation, with OpenAI, Google, Microsoft, AWS and Block among the founding members.

## EU AI Act — GPAI enforcement (the mandatory counterweight)

- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Artificial Intelligence Act, "Implementation Timeline" — https://artificialintelligenceact.eu/implementation-timeline/
- beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines
- Gibson Dunn, "EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines and Other Key Changes" — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/

Claims sourced here: On 2 August 2026 the enforcement and penalty powers of the EU AI Act over general-purpose AI (GPAI) providers become fully applicable, including fines of up to €15M or 3% of global annual turnover (Article 101); the AI Office can request documentation, run technical evaluations, demand risk-mitigation measures, and restrict or withdraw a model from the EU market; obligations flow down to deployers. The May 2026 Digital Omnibus reshuffled high-risk deadlines but left the 2 August GPAI date standing. The "16 days" figure is a simple count from this edition's date (17 July 2026) to 2 August 2026 and is the radar's own.

## AI governance gap & agent adoption (context)

- Corporate Compliance Insights, "Only 26% of Companies Say Governance Frameworks Are Fully Aligned With AI Adoption" (news roundup, 8 July 2026) — https://www.corporatecomplianceinsights.com/news-roundup-july-8-2026/
- AI Governance Statistics 2026, Evolvance Market Research — https://evolvancemarketresearch.com/statistics/ai-governance-statistics/
- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up From Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

Claims sourced here: Industry surveys report a persistent AI-governance deficit — on the order of ~8% of organizations with a comprehensive AI-governance framework against ~88% actively using AI, and only ~26% saying their governance frameworks are fully aligned with the pace of adoption (as reported). Gartner projects 40% of enterprise applications will feature task-specific AI agents by end-2026 (up from less than 5% in 2025) and that more than 40% of agentic-AI projects will be cancelled by end-2027 due to governance, risk and unclear business value.

---

*Editorial lines marked as the radar's own (e.g. "A standard coupling standardizes the fitting, not the fire. Adopt the universal thread — but own where the water goes, the pressure, and who holds the key.") are the AI Tech Radar's framing and are not third-party quotes. The 1904 Great Baltimore Fire / fire-hose-coupling standardization illustration is a well-worn historical analogy used allegorically, not as a sourced claim about AI. The MCP 2026-07-28 specification mechanics are relayed from the Model Context Protocol blog and secondary coverage; the 28 July 2026 final-spec date is the MCP project's. EMA going stable (18 June 2026) and the 29 June beta SDKs are relayed from InfoQ, TechTimes and secondary coverage and marked "as reported." The security-risk characterization is relayed from Akamai and SecurityWeek and marked "as reported." The 10,000+ MCP servers figure, the Agentic AI Foundation stewardship, and the governance-gap figures rest on secondary coverage and industry surveys and are marked "as reported." The EU AI Act mechanics are relayed from the European Commission and secondary coverage. The Gartner figures are Gartner's.*
