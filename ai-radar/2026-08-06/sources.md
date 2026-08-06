# Sources — AI Tech Radar, 6 August 2026 ("The Airlock")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or official that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Details drawn directly from Anthropic's product documentation are marked "as documented."

## The story — own the checkpoint: Anthropic Inference hooks for Claude Enterprise

### The launch — Inference hooks (beta), 5 August 2026

- Anthropic / Claude, "Inference hooks: inline data loss prevention for Claude Enterprise" (blog announcement) — https://claude.com/blog/claude-enterprise-inference-hooks
- Claude Platform Docs, "Inference hooks" — https://platform.claude.com/docs/en/manage-claude/inference-hooks
- Claude Platform Docs, "Configure Inference hooks" — https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration
- Claude Platform Docs, "Develop an Inference hooks integration" (request/verdict schemas, signature verification) — https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint
- Unite.AI, "Anthropic Puts Inline Data Loss Prevention Inside Claude Enterprise" — https://www.unite.ai/anthropic-puts-inline-data-loss-prevention-inside-claude-enterprise/
- The Next Web, "Anthropic built an inspection layer that lets enterprises block sensitive data before it reaches Claude" — https://thenextweb.com/news/anthropic-inference-hooks-dlp-claude-enterprise
- Releasebot, "Anthropic Release Notes — August 2026" — https://releasebot.io/updates/anthropic
- Zscaler, "Zscaler Integrates With Claude Inference Hooks to Scale AI While Addressing Risks" — https://www.zscaler.com/blogs/product-insights/zscaler-integrates-claude-inference-hooks-scale-ai-while-addressing-risks
- Palo Alto Networks, "Prisma AIRS — Unified Data Protection for Claude" — https://www.paloaltonetworks.com/blog/2026/08/prisma-airs-unified-data-protection-for-claude/
- Standard Webhooks specification (signing standard referenced by Inference hooks) — https://www.standardwebhooks.com/

Claims sourced here: Inference hooks launched in beta for Claude Enterprise (coverage dates the launch to 5 August 2026, as reported). Per the Claude Platform Docs (as documented): a Claude Enterprise organization can route every governed prompt to its own AI security server — an HTTPS service the organization or its security vendor operates — for an allow-or-deny verdict before inference runs, and a denied request never reaches the model. The hook runs on Anthropic's servers after the request leaves the client and before the model runs, so it applies to every governed request uniformly with nothing to install on user devices; the request is signed per the Standard Webhooks specification; the AI security server responds within a configurable verdict timeout that defaults to 5 seconds. The server sees the conversation transcript, tool calls and their results, and text extracted from attachments, but never raw file or image bytes, system prompts, or Anthropic-internal context. On deny, the request is rejected, the user sees a blocked-by-policy message, and the denial is recorded in the organization's Activity Feed. Enforcement can be phased with shadow mode (observe without blocking), a rollout percentage, and role exclusions; the organization sets failure handling (block or allow when the server is unreachable). One hook governs claude.ai, Cowork and Claude Code across web, desktop and CLI; Inference hooks are not available on Amazon Bedrock or Google Cloud, voice mode is not covered, verdicts are allow or deny only (no rewrite or redaction), and today the only hook event is the prompt, with response-side enforcement planned as a later event. Named DLP integration partners (Netskope, Palo Alto Networks, Proofpoint, Zscaler, or an in-house AI security server) are relayed from trade coverage as reported.

## The demand signal — why the checkpoint shipped now

- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up from Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- Salesforce Ben, "Salesforce Q1 Results: Agentforce Hits $1B ARR" — https://www.salesforceben.com/salesforce-q1-results-agentforce-hits-1b-arr-as-benioff-takes-aim-at-ai-doubters/
- Enterprise DNA, "Salesforce Cuts Jobs Again as Agentforce Hits $1.2B ARR" — https://enterprisedna.co/resources/news/salesforce-agentforce-1-2-billion-arr-layoffs-third-round-2026/
- Salesforce, "Salesforce Delivers Record Fourth Quarter Fiscal 2026 Results" — https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/
- PwC, "PwC's AI Agent Survey" — https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html

Claims sourced here (as reported): Gartner projects that 40% of enterprise applications will feature task-specific AI agents by 2026, up from less than 5% in 2025. Salesforce's Agentforce annual recurring revenue is reported at roughly $1.2 billion, up about 205% year over year (Q1 fiscal 2027, mid-2026), having earlier reached about $800 million (up 169%). PwC's AI Agent Survey found that 88% of surveyed senior executives plan to increase their AI-related budgets because of agentic AI.

## Why you need it — the confidence gap (carried forward from 5 August)

- Gravitee, "State of AI Agent Security 2026 Report: When Adoption Outpaces Control" — https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control
- VentureBeat, "The enforcement gap: 88% of enterprises reported AI agent security incidents last year" — https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds

Claims sourced here (as reported): Gravitee's State of AI Agent Security 2026 found that 88% of organizations reported a confirmed or suspected AI-agent security incident in the past year, while 82% of executives feel confident their existing policies protect them.

## The regulatory backdrop — EU AI Act enforcement, still live

- European Commission (Press corner), "Commission starts enforcing AI Act rules and new transparency requirements on 2 August" — https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714
- Help Net Security, "EU begins enforcing AI Act, putting AI models under the microscope" (4 August 2026) — https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/
- Wilson Sonsini, "EU AI Act Enforcement Phase Begins" — https://www.wsgr.com/en/insights/eu-ai-act-enforcement-phase-begins.html
- EU Artificial Intelligence Act, "Article 11: Technical Documentation" — https://artificialintelligenceact.eu/article/11/
- EU Artificial Intelligence Act, "Article 26: Obligations of Deployers of High-Risk AI Systems" — https://artificialintelligenceact.eu/article/26/

Claims sourced here (as reported): EU AI Act enforcement has been live since 2 August 2026, with the AI Office empowered to request documentation from GPAI providers, evaluate models, demand risk-mitigation measures, and fine up to the higher of €15 million or 3% of worldwide annual turnover (Article 99), with €7.5 million or 1.5% for incorrect information. More than 180 organizations — including Anthropic, Google, Microsoft, OpenAI, Amazon, IBM, Mistral AI and Cohere — signed the GPAI Code of Practice; France designated CNIL as its national competent authority. On 4 August 2026 CNIL issued formal information requests to 14 financial institutions running credit-scoring algorithms, demanding the Article 11 technical documentation; the CNIL specifics rest on secondary coverage.

## The vacuum — commodity models (context)

- LLM-Stats, "AI Updates Today (August 2026) – Latest AI Model Releases" — https://llm-stats.com/llm-updates
- Evertune, "AI Model Release Tracker" — https://www.evertune.ai/resources/ai-model-tracker
- FelloAI, "Best AI Models in August 2026: ChatGPT, Claude, Gemini & Grok" — https://felloai.com/best-ai-models/

Claims sourced here (as reported): Claude Opus 5 (released 24 July 2026), ranked first with an Intelligence Index of 61 and an Agentic Index of 55.3 at $5/$25 per million tokens; Google Gemini 3.6 Flash (released 21 July 2026); GPT-5.6 Sol; Kimi K3 open weights; and DeepSeek V4-Flash-0731 (released 31 July 2026, MIT-licensed open weights) are relayed from model-tracker and vendor coverage as reported.

---

*Editorial lines marked as the radar's own (e.g. "The model is the vacuum outside — rented and swappable. The airlock is yours, or it is no one's: the one chamber where your data crosses to the model, and where deny means the outer door never opens.") are the AI Tech Radar's framing and are not third-party quotes. The airlock allegory — a pressurized vessel whose cargo crosses to the vacuum only through a two-door chamber where the ship's own inspector calls allow or deny — is a common illustration used allegorically, told approximately, and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported"; details drawn from Anthropic's product documentation are marked "as documented." Product, firm and institution names (Anthropic, Claude, Claude Code, Cowork, Netskope, Palo Alto Networks, Proofpoint, Zscaler, Gartner, Salesforce, PwC, Gravitee, the European Commission, the EU AI Office, CNIL, OpenAI, Google, DeepSeek, Moonshot) reflect the sources as described in the cited 2026 material.*
