# Sources — AI Tech Radar, 21 July 2026 ("The Passport")

Every claim in this edition traces to a public source below. Figures are attributed to the organization that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Technical details are drawn from vendor documentation where available and from industry and security coverage otherwise.

## The story — agent identity moves below the application tier

### Google — Gemini Enterprise Agent Platform (cryptographically attested agent identity)

- Tech Times, "Gemini Enterprise Agent Platform Leads Enterprise AI Governance as OpenAI Starts Billing for Agents" — https://www.techtimes.com/articles/320956/20260719/gemini-enterprise-agent-platform-leads-enterprise-ai-governance-openai-starts-billing-agents.htm
- Google Cloud Documentation, "Agent Identity overview | Gemini Enterprise Agent Platform" — https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview
- Google Cloud Documentation, "Agent Gateway overview | Gemini Enterprise Agent Platform" — https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview
- Google Cloud Blog, "Introducing Gemini Enterprise Agent Platform" — https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
- Infosecurity Magazine, "Google Introduces Unique AI Agent Identities in New Gemini Enterprise" — https://www.infosecurity-magazine.com/news/google-ai-agent-identities-gemini/
- Google Codelabs, "Governing agentic workloads with Agent Gateway on Gemini Enterprise Agent Platform" — https://codelabs.developers.google.com/cloudnet-agent-gateway

Claims sourced here (as reported): Google's Gemini Enterprise Agent Platform assigns every deployed agent a unique, cryptographically attested identity using the SPIFFE (Secure Production Identity Framework for Everyone) standard; every API call, data access request and file operation an agent performs is signed, logged and traceable to that identity; identities are secured with mutual-TLS / Context-Aware Access, and a unified Agent Gateway acts as a policy enforcement point. Gemini Enterprise places Agent Identity and the Agent Gateway below the application tier as infrastructure primitives, so governance is enforced regardless of how an agent was built or by whom — reported as an architectural difference from competitors such as Anthropic and OpenAI, which have positioned agent-governance controls at the application tier. Coverage also notes OpenAI moving to credit-based billing for agents.

### Agent identity as a first-class non-human identity (industry best practice)

- Okta, "AI Agents at Work 2026: Securing the agentic enterprise" — https://www.okta.com/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/
- Cloud Security Alliance (Lab Space), "The Non-Human Identity Governance Vacuum" (whitepaper) — https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/
- Reco, "Non-Human Identities for AI Agents: How to Govern Access at Enterprise Scale" — https://www.reco.ai/blog/non-human-identities-for-ai-agents
- nhimg.org, "AI agent identity security in 2026: are your controls keeping up?" — https://nhimg.org/community/agentic-ai-and-nhis/ai-agent-identity-security-in-2026-are-your-controls-keeping-up/

Claims sourced here (as reported): Industry best practice frames an AI agent as a first-class non-human identity — its own principal, cryptographically attested, short-lived at runtime, with the human preserved as the delegating subject via token exchange — and notes Microsoft, AWS and Google shipped versions of this pattern over the last two quarters.

## The population inversion — non-human identities outnumber humans

- Palo Alto Networks, 2026 Identity Security Landscape (relayed via coverage) — https://securew2.com/signal/the-non-human-identity-crisis-when-machines-outnumber-people-45-to-1
- SecureW2, "The Non-Human Identity Crisis: When Machines Outnumber People 45 to 1" — https://securew2.com/signal/the-non-human-identity-crisis-when-machines-outnumber-people-45-to-1
- The Hacker News, "The Non-Human Identity Crisis: Why Your Machine Identities Are Your Biggest Governance Gap" — https://thehackernews.com/expert-insights/2026/05/the-non-human-identity-crisis-why-your.html
- Cyber Strategy Institute, "2026 NHI Reality Report: 5 Critical Identity Risks" — https://cyberstrategyinstitute.com/2026-nhi-reality-report/
- nhimg.org, "Identity governance is shifting as non-human identities outnumber humans" — https://nhimg.org/articles/identity-governance-is-shifting-as-non-human-identities-outnumber-humans/

Claims sourced here (as reported): Non-human identities now outnumber human identities by roughly 45 to 1 (Rubrik Zero Labs); by 109 to 1 in the average enterprise, up from 82 to 1 a year earlier (Palo Alto Networks, 2026 Identity Security Landscape); and by up to 144 to 1 in cloud-native / DevOps environments (Entro Labs). About 78% of organizations lack documented, formally adopted policies for creating or removing non-human identities, and roughly two-thirds of enterprises have suffered a breach via a compromised NHI.

## The governance gap — enterprise agent adoption vs. control

- OutSystems, "96% of Organizations Use AI Agents: 2026 OutSystems Research" — https://www.outsystems.com/news/enterprise-ai-agent-report-2026/
- OutSystems, "State of AI Development 2026: The Move to Agentic AI" — https://www.outsystems.com/1/state-ai-development
- Business Wire, "Agentic AI Goes Mainstream in the Enterprise, but 94% Raise Concern About Sprawl, OutSystems Research Finds" — https://www.businesswire.com/news/home/20260407749542/en/Agentic-AI-Goes-Mainstream-in-the-Enterprise-but-94-Raise-Concern-About-Sprawl-OutSystems-Research-Finds
- TechHQ, "Agentic AI Governance Is the CIO's Most Urgent Blind Spot" — https://techhq.com/news/agentic-ai-governance-enterprise-gap/

Claims sourced here: OutSystems' State of AI Development 2026 (survey of 1,879 IT leaders, published April 2026) found 96% of enterprises run AI agents but only 12% have a centralized platform to manage them; 36% have a centralized approach to agentic governance; 97% are exploring agentic AI strategies; and 94% are concerned that AI sprawl is compounding complexity, technical debt and security risk.

## Standing countdowns (continuing threads from prior editions)

- Kimi K3 open weights — Moonshot AI has committed to publishing the full Kimi K3 weights on 27 July 2026 under a Modified MIT license (relayed via coverage; see the 18 July "Aluminum Age" edition's sources for the full Kimi K3 source list).
  - Cryptobriefing, "Kimi K3 launches with 2.8 trillion parameters, open weights dropping July 27" — https://cryptobriefing.com/kimi-k3-open-weights-july-27/
- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- WorkOS, "The biggest MCP spec update ships July 28: What changes for AI agent authentication" — https://workos.com/blog/mcp-2026-spec-agent-authentication

Claims sourced here: Kimi K3's full open weights publish on 27 July 2026 (Moonshot's date). The MCP 2026-07-28 specification goes final on 28 July 2026, aligning MCP authorization with OAuth 2.1 and OpenID Connect (MCP servers become formal OAuth 2.1 resource servers). The "6 days," "7 days" and "12 days" figures are simple counts from this edition's date (21 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own.

## The mandatory counterweight — EU AI Act GPAI enforcement (applicable 2 August 2026)

- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European Commission, "Guidelines for providers of general-purpose AI models" — https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/
- beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines

Claims sourced here: From 2 August 2026 the European Commission's enforcement powers over general-purpose AI (GPAI) providers become fully applicable — including the power to request documentation and information (Article 91), conduct evaluations (Article 92), request measures including risk mitigation and market restriction (Article 93), and impose fines of up to €15 million or 3% of global annual turnover, whichever is higher (Article 101). Obligations reach deployers, not only model providers.

## Adoption context

- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up From Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- Gartner, "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027" — https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

Claims sourced here: Gartner projects 40% of enterprise applications will feature task-specific AI agents by end-2026 (up from less than 5% in 2025) and that more than 40% of agentic-AI projects will be cancelled by end-2027 due to escalating costs, unclear business value or inadequate risk controls.

---

*Editorial lines marked as the radar's own (e.g. "A seal is worthless if anyone can wear the ring… we check at the border, not the front desk.") are the AI Tech Radar's framing and are not third-party quotes. The passport allegory — the historical safe-conduct and passport (issued by a sovereign, naming and vouching for the bearer, sealed and later stamped and photographed to be verifiable, limited in time and route, and checked at the border by a guard while an innkeeper merely recorded arrivals) — is a well-worn historical illustration used allegorically, told approximately, and is not a sourced claim about AI. The Gemini Enterprise, non-human-identity and OutSystems details are relayed from the coverage and documentation listed above; where a figure rests on secondary reporting it is marked "as reported." Model, product and vendor names (Gemini Enterprise, SPIFFE, Kimi K3, MCP, OAuth 2.1) reflect the products as described in the cited 2026 sources.*
