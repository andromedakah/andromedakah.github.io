# Sources — AI Tech Radar, 20 October 2026 ("The Insider")

All figures and quotes are relayed from the publications below, surfaced via web search, and are marked "as reported" in the edition. Where a direct page fetch was blocked by the compile environment's network egress proxy, specific wordings — Nadella's and Cox's quotes, the product names, and the "60 agent types / +35" figures — should be reconciled against the primary source before republishing. The "insider" framing (an agent as a trusted insider whose access is the attack surface; the model is not a trust boundary; separate the counsel from the keys, give each agent a face, set a quick watchman, keep the decisions human) is expressly the radar's own editorial reading.

## Primary anchor — Microsoft (19 October 2026)

- **Microsoft Security blog — "Agents are your newest insiders. Security must move at their speed"** (Nadim Abdo, CVP, Identity and Network Access), 19 Oct 2026. Treat AI agents as insider threats; "frontier models can't be trusted" by default. Satya Nadella: "separate the supply of intelligence from the authority over it"; "the most trustworthy agentic system will not be the one with the model we trust most. It will be the one designed that enables us to trust the model least." Terrell Cox (CVP & Deputy CISO, Customer Security): "Agents will only be adopted at scale if they can be trusted at scale." Products: Entra Agent ID (an identity per agent, separate from its human sponsor); Guardian Agents (agents that monitor other agents at machine speed, while people set the rules and keep the decisions that matter); Project Perception; Microsoft Agent 365; Microsoft Execution Container (MXC); dynamic permissions / dynamic agent risk / dynamic conditional access; Playbooks. Local agent discovery expanded by 35 types to 60 supported, incl. Claude Code, OpenAI Codex, GitHub Copilot.
  https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/

## Secondary coverage — the insider framing and controls

- **TechCrunch — "Microsoft says AI agents are like insider threats as 'frontier models can't be trusted'"** (19 Oct 2026). Insider-threat framing; Entra Agent ID; Guardian Agents; Nadella's call to separate intelligence from authority and to stop trusting model providers by default.
  https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/
- **SiliconANGLE — "Microsoft targets the 'agentic insider' with new controls for rogue AI agents"** (19 Oct 2026). Guardian Agents, Entra Agent ID, Agent 365, Project Perception, Microsoft Execution Container, dynamic permissions/conditional access; the 60-local-agent-types (+35) discovery figure; Terrell Cox and Nadella quotes.
  https://siliconangle.com/2026/10/19/microsoft-targets-the-agentic-insider-with-new-controls-for-rogue-ai-agents/
- **CyberSecurityNews — "Microsoft Says AI Agents Cannot Be Trusted and Could Become Insider Security Threats"** (19 Oct 2026).
  https://cybersecuritynews.com/ai-models-as-insider-threats/
- **Unite.ai — "Microsoft Adds Guardian Agents to Project Perception for AI Insider Risk"** (19 Oct 2026). Guardian Agents within Project Perception; the managed-workforce framing.
  https://www.unite.ai/microsoft-adds-guardian-agents-to-project-perception-for-ai-insider-risk/

## Context — not Microsoft alone (same week)

- **AIwire (HPCwire) — "Cognizant and Google Cloud Expand Partnership to Scale Enterprise AI Agents"** (19 Oct 2026). Expanded partnership and a "Gemini Frontier" capability group to scale enterprise agent adoption.
  https://www.hpcwire.com/aiwire/2026/10/19/cognizant-and-google-cloud-expand-partnership-to-scale-enterprise-ai-agents/
- **TechCrunch — "Google brings agentic AI to Gemini, starting with businesses"** (8 Oct 2026). A unified Gemini business agent that can delegate to subagents, use multiple models, and take a workplace identity of its own.
  https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/

## Background rails (prior editions; referenced, not today's news)

- **Gartner — "Over 40% of Agentic AI Projects Will Be Canceled by End of 2027"** (press release, 2025-06-25). Escalating costs, unclear business value, inadequate risk controls.
  https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- **EU AI Act** — high-risk regime live since 2 August 2026 (human-oversight and logging duties); referenced as a standing rail.
- **Model Context Protocol (MCP) 2026-07-28** — Enterprise-Managed Authorization stable; the tool-connection layer, referenced as a standing rail.

---

*Note on verification: several source pages could not be fetched directly from the build environment (network egress proxy / DNS). The Microsoft Security primary post was read successfully and is the anchor for the quotes, product names and the 60-agent-types (+35) figure; secondary outlets corroborate the insider-threat framing and the Nadella/Cox quotes. Reconcile exact wording against the Microsoft primary post before any republication beyond this site.*
