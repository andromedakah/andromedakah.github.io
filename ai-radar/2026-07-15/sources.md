# Sources — AI Tech Radar, 15 July 2026 ("The Gauge War")

Every claim in this edition traces to a public source below. Figures are attributed to the organization that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure is reported via secondary coverage or rests on a single source, it is marked "as reported." The agent-standards landscape (ARD, MCP, A2A) is a fast-moving snapshot; specifications are early-stage drafts and are described as such.

## The standards war — framing (The Information)

- The Information, "Google and Microsoft Team Up to Beat Back Anthropic and OpenAI" — https://www.theinformation.com/newsletters/applied-ai/google-microsoft-team-beat-back-anthropic-openai
- CryptoBriefing, "Google, Microsoft, and Salesforce back new AI software standard to counter OpenAI and Anthropic" — https://cryptobriefing.com/ard-ai-standard-google-microsoft-salesforce/
- Swisher Post, "AI agent standard ARD backed by Google and Microsoft" — https://www.swisherpost.com/technology/ai-agent-standard-ard-google-microsoft/

Claims sourced here (as reported): The enterprise-software incumbents are using standards battles to encircle Anthropic and OpenAI on the agent-tooling layer; the vehicle is the ARD (Agentic Resource Discovery) specification, backed by a coalition of incumbents that does not include Anthropic or OpenAI. The "Google and Microsoft Team Up to Beat Back Anthropic and OpenAI" headline framing is The Information's.

## ARD (Agentic Resource Discovery) — the discovery layer

- Google Developers Blog, "Announcing the Agentic Resource Discovery specification" — https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/
- AgenticResourceDiscovery.org — specification site — https://agenticresourcediscovery.org/ and https://agenticresourcediscovery.org/spec/
- Microsoft (Command Line), "Introducing the Agentic Resource Discovery specification (ARD)" — https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/
- Hugging Face, "Agentic Resource Discovery: Let agents search" — https://huggingface.co/blog/agentic-resource-discovery-launch
- Search Engine Journal, "Google, Microsoft Back Draft AI Agent Discovery Spec" — https://www.searchenginejournal.com/google-microsoft-back-draft-ai-agent-discovery-spec/579894/
- Developer-Tech, "GitHub and Google back ARD standard for AI agent discovery" — https://www.developer-tech.com/news/github-google-ard-ai-agent-discovery/
- Synscribe, "Google Just Standardized Agentic Discovery. Here's What It Means (and What It Misses)" — https://www.synscribe.com/blog/google-agentic-resource-discovery-ard-specification

Claims sourced here (as reported): ARD is a v0.9 draft open specification (Apache-2.0), announced 17 June 2026, defining how AI resources are cataloged, discovered and searched across federated networks. Publishers host a machine-readable `ai-catalog.json` at `/.well-known/ai-catalog.json` describing agentic resources (MCP servers, A2A agents, skills, APIs); registries crawl and index catalogs and expose a search/REST API that agents query at runtime (`POST /search`). Backers include Google, Microsoft, GitHub, GoDaddy, Hugging Face, Nvidia, Salesforce, ServiceNow, Databricks, Snowflake and Cisco (11 organizations). Neither Anthropic nor OpenAI appeared on the initial backer list. ARD is the discovery ("phone book") layer that precedes an MCP connection.

## GitHub agent finder (built on ARD)

- GitHub Changelog, "Agent finder for GitHub Copilot now available" (2026-06-17) — https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/
- Developers Digest, "GitHub Copilot Agent Finder: What ARD Means for Third-Party AI Tools in 2026" — https://www.developersdigest.tech/blog/github-copilot-agent-finder-ard-specification-2026

Claims sourced here (as reported): GitHub agent finder implements the open ARD specification and is available on all GitHub Copilot plans. Instead of hand-wiring which MCP servers, skills, tools and agents each agent should use, Copilot can discover the right capability for a task at runtime from any catalog you point it at; enterprises configure policies (which registries to trust, what to allow) and, per GitHub, "agent finder only ever surfaces what your enterprise permits."

## MCP adoption / position

- Medium (Adithya Giridharan), "MCP at 97 Million: Anthropic's Protocol Bet Has Already Won" — https://medium.com/@AdithyaGiridharan/mcp-at-97-million-anthropics-protocol-bet-has-already-won-the-standard-for-agentic-ai-8601151b3f46
- andrew.ooo, "MCP Enterprise Adoption: The July 2026 State of Play" — https://andrew.ooo/answers/mcp-model-context-protocol-enterprise-adoption-july-2026/
- InfoQ, "AI Model Context Protocol Adds Centralised Auth for Enterprise" — https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/
- Wikipedia, "Model Context Protocol" — https://en.wikipedia.org/wiki/Model_Context_Protocol

Claims sourced here (as reported): Anthropic open-sourced MCP in November 2024; in roughly 18 months it became the de facto standard for connecting agents to enterprise tools. Secondary coverage cites ~97M monthly SDK downloads, MCP-backed agents in production at 78% of enterprise AI teams, and ~28% of Fortune 500 companies running MCP servers (July 2026). These density figures rest on secondary coverage and are marked "as reported."

## A2A / Agentic AI Foundation (AAIF)

- The Next Web, "Google Cloud Next 2026: AI agents, A2A protocol, Workspace Studio, and the full-stack bet against OpenAI and Anthropic" — https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era
- 36Kr, "Rare Joint Appearance of OpenAI, Anthropic, and Google: Agentic AI Foundation Launched" — https://eu.36kr.com/en/p/3589328631202050
- AAIF / Agentic AI Foundation — https://aaif.io/blog/mcp-is-growing-up/

Claims sourced here (as reported): Google's Agent2Agent (A2A) protocol has reached ~150 organizations in production and is now governed by the Linux Foundation's Agentic AI Foundation (AAIF), which also houses Anthropic's MCP, Block's *goose* project and OpenAI's *AGENTS.md* specification.

## Agent adoption, ROI & governance

- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up From Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- Salesforce, "Salesforce Delivers Record Fourth Quarter Fiscal 2026 Results" — https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/
- TechHQ, "Salesforce's Agentforce enterprise bet is paying off and the numbers prove it" — https://techhq.com/news/salesforce-agentforce-enterprise-agentic-ai/

Claims sourced here: Gartner projects 40% of enterprise applications will feature task-specific AI agents by end-2026 (up from less than 5% in 2025) and that more than 40% of agentic-AI projects will be cancelled by end-2027 due to governance and ROI failures. Salesforce reported Agentforce ARR of $800M in Q4 FY2026, up 169% year-over-year (Agentforce + Data 360 ARR exceeding $2.9B, up over 200% YoY).

## PwC 29th Global CEO Survey (2026)

- PwC, "PwC 2026 Global CEO Survey" — https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-global-ceo-survey.html
- PwC, "Leading through uncertainty in the age of AI — PwC's 29th Global CEO Survey" (PDF) — https://www.pwc.com/gx/en/ceo-survey/2026/pwc-ceo-survey-2026.pdf

Claims sourced here: 56% of CEOs report they have seen no significant financial benefit from AI to date; only one in eight (12%) say AI has delivered both cost and revenue benefits. Based on responses from 4,454 CEOs across 95 countries and territories.

## EU AI Act — GPAI enforcement (secondary thread)

- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Artificial Intelligence Act, "Implementation Timeline" — https://artificialintelligenceact.eu/implementation-timeline/
- beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines

Claims sourced here (as reported): On 2 August 2026 the enforcement and penalty powers of the EU AI Act over general-purpose AI (GPAI) providers become fully applicable, including fines of up to €15M or 3% of global annual turnover (Article 101). The "18 days" figure is a simple count from this edition's date (15 July 2026) to 2 August 2026 and is the radar's own.

---

*Editorial lines marked "the radar's framing" (e.g. "In a gauge war the prize isn't the best gauge — it's the junction everyone must pass through. Don't bet the estate on the winner; own the interchange.") are the AI Tech Radar's own and are not third-party quotes. The 19th-century railway-gauge-war allegory is a well-worn historical illustration used allegorically, not as a sourced claim. The ARD/MCP/A2A landscape is a fast-moving snapshot: ARD is an early-stage v0.9 draft and field naming is still converging; adoption density figures for MCP and A2A rest on secondary coverage and are marked "as reported." The Salesforce, Gartner and PwC figures are from the named primary publications. The EU AI Act mechanics are relayed from the European Commission and secondary coverage.*
