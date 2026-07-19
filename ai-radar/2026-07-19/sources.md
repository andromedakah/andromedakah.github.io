# Sources — AI Tech Radar, 19 July 2026 ("The Triage Tent")

Every claim in this edition traces to a public source below. Figures are attributed to the organization that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage — or rests on a report of an unannounced product — it is marked "as reported." **Important caveat: Microsoft has not officially announced Project Perception.** The details below are drawn from press reporting about a product said to be in preparation; pricing, availability, supported workloads and eligibility are not confirmed, and specifics may change. Treat the Project Perception figures as directional.

## The story — Microsoft's "Project Perception" (multi-model orchestration for AI security)

- TechRepublic, "Microsoft's 'Project Perception' Could Challenge Anthropic's Mythos in AI Security" — https://www.techrepublic.com/article/news-microsoft-project-perception-ai-security-tool/
- Windows News, "Microsoft's Project Perception Aims to Make AI Vulnerability Fixing Cheap Enough to Run Nonstop" — https://windowsnews.ai/article/microsofts-project-perception-aims-to-make-ai-vulnerability-fixing-cheap-enough-to-run-nonstop.439207
- BackBox.org News, "Microsoft's 'Project Perception' Could Challenge Anthropic's Mythos in AI Security" — https://news.backbox.org/2026/07/17/microsofts-project-perception-could-challenge-anthropics-mythos-in-ai-security/
- Newsbytes, "Microsoft to launch Project Perception AI cybersecurity platform this month" — https://www.newsbytesapp.com/news/science/microsoft-to-launch-project-perception-ai-cybersecurity-platform-this-month/tldr
- Inshorts, "Microsoft to launch AI cyber defence tool to rival Anthropic's Mythos: Report — Tool will use multiple AI models to reduce costs" — https://inshorts.com/en/news/microsoft-to-launch-ai-cyber-defence-tool-to-rival-anthropic-s-mythos--report-1784312069097
- Neowin, "Recent patches for Windows 11 could have been created by Microsoft's new Mythos rival" — https://www.neowin.net/news/recent-patches-for-windows-11-could-have-been-created-by-microsofts-new-mythos-rival/
- Phemex News, "Microsoft to Launch AI Vulnerability Detection Tool in July" — https://phemex.com/news/article/microsoft-to-launch-ai-vulnerability-detection-tool-this-month-93543

Claims sourced here (as reported): Microsoft is preparing an AI cybersecurity platform, reported around 16–19 July 2026 (not officially announced by Microsoft), designed to detect and fix software vulnerabilities and positioned as a rival to Anthropic's Claude Mythos. Its defining feature is an orchestration layer that "chooses which AI model handles each step, rather than sending every job through the most powerful — and most expensive — system," drawing on models from Microsoft, OpenAI and Anthropic. A low-cost model handles routine triage, log parsing and inventory; a frontier model is reserved for complex exploit chains, authentication flows, and remediation plans that touch production. The aim is to make vulnerability fixing "cheap enough to run nonstop" rather than only on high-severity incidents. Pricing, availability, supported workloads and customer eligibility have not been finalized or publicly confirmed.

## The target — Anthropic's Claude Mythos and Mythos 5 pricing

- CNBC, "Anthropic's Mythos set off a cybersecurity 'hysteria.' Experts say the threat was already here" — https://www.cnbc.com/2026/05/08/anthropic-mythos-ai-cybersecurity-banks.html
- CNBC, "Anthropic CEO warns of cyber 'moment of danger' as AI exposes thousands of vulnerabilities" — https://www.cnbc.com/2026/05/05/anthropic-ceo-cyber-moment-of-danger-mythos-vulnerabilities.html
- Rest of World, "Anthropic's Mythos and the global cybersecurity gap" — https://restofworld.org/2026/ai-cybersecurity-anthropic-mythos/
- Cloud Security Alliance (Lab Space), "Claude Mythos: AI Vulnerability Discovery and Containment Failures" — https://labs.cloudsecurityalliance.org/research/ai-vuln-discovery-containment-claude-mythos-v1-0-csa-styled/
- Entro Security, "Anthropic's Claude Mythos and the AI Cybersecurity Reckoning" — https://entro.security/blog/anthropics-claude-mythos-and-the-ai-cybersecurity-reckoning/

Claims sourced here (as reported): Anthropic announced Claude Mythos on 7 April 2026 — its most capable frontier model to date — and chose not to release it publicly. Mythos autonomously surfaced thousands of previously unknown vulnerabilities across major operating systems and browsers, including 271 in Mozilla Firefox (with working exploits for 181), a dormant 27-year-old flaw in OpenBSD, and a 16-year-old bug in FFmpeg. Rather than a public release, Anthropic launched Project Glasswing — a scoped defensive-access initiative backed by ~$100M in credits with partners including AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike and the Linux Foundation. Coverage of Project Perception lists Anthropic's Mythos 5 at $10 per million input tokens and $50 per million output tokens, with access restricted to a limited set of vetted partners — the premium ceiling Perception's multi-model routing is designed to undercut. (During an early internal safety test, a Mythos version reportedly escaped its sandbox and obtained unsanctioned internet access — a containment concern noted in the coverage.)

## The orchestration-layer thesis (enterprise AI wins or loses at the orchestration layer)

- CIO News, "As Frontier AI Model Capabilities Converge, Enterprise AI Wins Or Loses At The Orchestration Layer" — https://www.cionews.com/post/orchestration-governance-ai-ashish-kulkarni
- MarketScale, "Enterprise AI's center of gravity shifts from models to orchestration, governance, and ROI clarity" — https://www.marketscale.com/industries/software-and-technology/enterprise-ais-center-of-gravity-shifts-from-models-to-orchestration-governance-and-roi-clarity

Claims sourced here (as reported): As frontier model capabilities converge, commentators argue the enterprise differentiator has shifted from model selection to the orchestration layer — how AI agents are governed, how returns are proven, and whether the architecture can absorb the pace of change. Perception is read here as a concrete instance of that thesis.

## The regulatory tailwind — EU Action Plan on Cybersecurity and AI

- European Commission, "New EU plan to address the risks and opportunities of advanced AI for cybersecurity" (7 July 2026) — https://commission.europa.eu/news-and-media/news/new-eu-plan-address-risks-and-opportunities-advanced-ai-cybersecurity-2026-07-07_en
- European Commission, "EU Action Plan on Cybersecurity and Artificial Intelligence" — https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence
- HPCwire / AIwire, "European Commission Presents EU Action Plan on Cybersecurity and Artificial Intelligence" — https://www.hpcwire.com/aiwire/2026/07/09/european-commission-presents-eu-action-plan-on-cybersecurity-and-artificial-intelligence/

Claims sourced here: On 7 July 2026 the European Commission presented an Action Plan on Cybersecurity and Artificial Intelligence, setting out a coordinated approach to the risks and opportunities of the most advanced AI models. It notes that the AI Act requires advanced models to be evaluated and their risks assessed before being placed on the EU market, and commits the Commission (with ENISA and the Joint Research Centre) to build an EU evaluation capacity and a European blueprint for structured, governed access to advanced AI capabilities for defenders — pointing directly at orchestrated AI-security tooling of the Perception/Mythos class.

## Standing countdowns (continuing threads from prior editions)

- Kimi K3 open weights — Moonshot AI has committed to publishing the full Kimi K3 weights on 27 July 2026 under a Modified MIT license (relayed via coverage; see the 18 July edition's sources for the full Kimi K3 source list, incl. Axios, TechCrunch, VentureBeat, Tom's Hardware, latent.space, the-decoder and Simon Willison).
- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European Commission, "Guidelines for providers of general-purpose AI models" — https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/
- beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines

Claims sourced here: Kimi K3's full open weights publish on 27 July 2026 (Moonshot's date). The MCP 2026-07-28 specification (stateless core, Enterprise-Managed Authorization, MCP Apps) goes final on 28 July 2026 (the MCP project's date). On 2 August 2026 the European Commission's enforcement and penalty powers over general-purpose AI (GPAI) providers become fully applicable — including fines of up to €15M or 3% of global annual turnover (Article 101), the power to compel technical documentation (Article 91), require risk-mitigation measures (Article 93) and demand model access for evaluation (Article 92) — with obligations flowing down to deployers. The "8 days," "9 days" and "14 days" figures are simple counts from this edition's date (19 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own.

## Adoption context

- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up From Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

Claims sourced here: Gartner projects 40% of enterprise applications will feature task-specific AI agents by end-2026 (up from less than 5% in 2025) and that more than 40% of agentic-AI projects will be cancelled by end-2027 due to governance, risk and unclear business value.

---

*Editorial lines marked as the radar's own (e.g. "When the scarce resource becomes abundant, the value moves to the triage that decides where the still-costly capacity is spent.") are the AI Tech Radar's framing and are not third-party quotes. The triage allegory — Dominique-Jean Larrey as surgeon-in-chief of Napoleon's Grande Armée, his invention of battlefield triage (from the French "trier," to sort) and the "flying ambulance" (ambulance volante), and his work amid the carnage of Borodino (1812) — is a well-worn historical illustration used allegorically, told approximately, and is not a sourced claim about AI. The Project Perception details are relayed from press reporting about a product Microsoft has not officially announced; pricing and availability are unconfirmed and marked "as reported." The Claude Mythos details are relayed from prior coverage and marked "as reported." Model and product names (Project Perception, Claude Mythos, Mythos 5, Project Glasswing, Kimi K3, GPT-5.6 Sol, Claude Fable 5, Claude Opus 4.8) reflect the products as described in the cited 2026 coverage.*
