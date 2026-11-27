# Sources — AI Tech Radar, 27 November 2026 ("The Tool-Chest")

All figures are relayed from vendor announcements, security research and reputable secondary
coverage surfaced via web search, and are marked **"as reported"** in the brief. Several
source pages could not be fetched directly (the compile environment's network egress proxy
blocked them), so specific figures — the `agent-framework` version numbers and targeted token
types, the ~31-minute quarantine window, the Entra Agent ID coverage, the non-human-identity
ratios, and the 1 February 2027 Google Workspace MCP requirement — should be reconciled
against the primary publications before republishing.

## The good news — agent identity became first-class (Microsoft Ignite 2026)
- What's new in Microsoft Agent 365 — Ignite 2026 — Microsoft Tech Community: https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753
- Microsoft Ignite 2026: your guide to Agent 365 — Microsoft Tech Community: https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/4571750
- Microsoft Ignite opens Agent 365, Azure Catalyst and Entra Agent Identity GA for enterprise AI — AI Weekly: https://aiweekly.co/alerts/microsoft-ignite-opens-agent-365-azure-catalyst-and-entra-agent-identity-ga-for
- Governing Agent identities and access — Microsoft Entra ID Governance: https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
- Microsoft Agent 365 integration with Foundry — Microsoft Foundry docs: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-365-integration
- Microsoft unveils Agent 365 to help IT manage AI agent sprawl — Computerworld: https://www.computerworld.com/article/4092436/microsoft-unveils-agent-365-to-help-it-manage-ai-agent-sprawl.html

## The hard news — Microsoft `agent-framework` PyPI package poisoned (17 Nov 2026)
- Microsoft's agent-framework PyPI package compromised to steal credentials — BleepingComputer: https://bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials
- Attackers hijack Microsoft's agent-framework package to steal Azure and CI credentials — CSO Online: https://www.csoonline.com/article/4250156/attackers-hijack-microsofts-agent-framework-package-to-steal-azure-and-ci-credentials.html
- Attackers hijack Microsoft's agent-framework package to steal Azure and CI credentials — InfoWorld: https://www.infoworld.com/article/4250167/attackers-hijack-microsofts-agent-framework-package-to-steal-azure-and-ci-credentials-2.html
- Credential stealer slipped into Microsoft's official Python agent framework — Help Net Security: https://www.helpnetsecurity.com/?p=391769
- Microsoft Agent Framework releases poisoned with credential stealer — SecurityWeek: https://securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer
- Microsoft Agent Framework hit by PyPI malware attack — Computing: https://www.computing.co.uk/news/2026/security/microsoft-agent-framework-hit-by-pypi-malware-attack
- Microsoft Agent Framework PyPI Releases Found Stealing Credentials — eSecurity Planet: https://www.esecurityplanet.com/threats/news-microsoft-agent-framework-pypi-credential-theft/
- GitHub Advisory GHSA-764m-3ppc-5m73 and issue #10411 (authoritative specifics; referenced via the above coverage)

## The scale underneath — non-human identity sprawl
- 2026 Identity Security Landscape (109:1 NHI-to-human, up from 82:1) — Palo Alto Networks (cited via secondary coverage): https://www.paloaltonetworks.com/
- GitGuardian report identifies non-human identity sprawl as primary security risk for enterprise infrastructure 2026 — NHI Mgmt Group: https://nhimg.org/nhi-news/non-human-identity-sprawl-enterprise-security-2026
- AI agents now outnumber employees 45 to 1: why non-human identity is enterprise security's next crisis — Promact: https://promactinfo.com/blogs/ai-agents-now-outnumber-employees-45-to-1-why-non-human-identity-is-enterprise-securitys-next-crisis/
- Why non-human identities are the fastest-growing security risk in AI-driven enterprises — Token Security: https://www.token.security/blog/why-non-human-identities-are-the-fastest-growing-security-risk-in-ai-driven-enterprises
- Non-human identity statistics 2026: the machine identity crisis by the numbers — Axis Intelligence: https://axis-intelligence.com/non-human-identity-statistics/

## The rails tightening — MCP and Google Workspace agents
- Security and AI news from the week beginning 18 November 2026 (Google Workspace agents must connect via MCP servers or CLI from 1 Feb 2027) — Enterprise Times: https://www.enterprisetimes.co.uk/2026/11/25/security-and-ai-news-from-the-week-beginning-18-november-2026/
- Configure the Google Workspace MCP servers — Google for Developers: https://developers.google.com/workspace/guides/configure-mcp-servers
- Agent tools and security updates for Workspace developers — Google Workspace Updates: https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html
- The 2026-07-28 MCP Specification — Model Context Protocol blog: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP graduates to enterprise infrastructure: stateless architecture, formal governance and security — Agentic AI Foundation: https://aaif.io/blog/mcp-graduates-to-enterprise-infrastructure-stateless-architecture-formal-governance-and-security

## Governance maturing alongside
- Daily / weekly AI agent news, week of 26 November 2026 (Claude Enterprise Compliance API; BlackLine AIUC-1 for Verity AI agents) — AI Agents Store: https://aiagentstore.ai/ai-agent-news/this-week
- Yesterday's Marketing Technology & AI News: November 26, 2026 — The Agile Brand Guide: https://agilebrandguide.com/yesterdays-marketing-technology-ai-news-november-26-2026/

## Prior rails (background)
- EU AI Act — up-to-date developments and analyses: https://artificialintelligenceact.eu/
- EU regulatory framework for AI (high-risk regime, Article 50 transparency) — European Commission: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Gartner: 40% of enterprise apps will feature task-specific AI agents by 2026: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

## Owner-verified recurring facts (see ai-radar/verified_facts.json)
- Gartner — over 40% of agentic AI projects canceled by end of 2027: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- EU AI Act penalties up to €35M or 7% of global turnover: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

---

*Editorial framing — the "tool-chest" allegory (agent identity as real working papers fixed to
the hand, versus the poisoned tool the papered hand reaches for; seal the hand, inspect the
chest and not just the famous mark, shrink the blast radius) — is expressly the radar's own
reading, not a sourced claim about any specific company beyond the reported Microsoft, Entra
Agent ID, `agent-framework`, Palo Alto, GitGuardian, Google, MCP, Anthropic and BlackLine figures.*
