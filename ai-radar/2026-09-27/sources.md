# Sources — AI Tech Radar, 27 September 2026 ("The Two Admiralties")

All figures are relayed from vendor announcements, analyst research, regulator communications
and reputable secondary coverage surfaced via web search, and are marked **"as reported"** in the
brief. Anthropic items (Claude Opus 5.5) were verified directly against anthropic.com. Several
other primary/reputable pages — openai.com, CNN, CNBC, Axios, Bloomberg, the Washington Post,
and the EU AI Act sites — could not be fetched directly (the compile environment's network egress
proxy blocked them); their **headlines and dates were confirmed via the search index**, but exact
quote wording and specific figures should be reconciled against the primary publications before
republishing. Items flagged UNVERIFIED below rest only on lower-quality aggregators and are **not
cited as fact** in the brief.

## The frontier ships get cheaper — Claude Opus 5.5 (22 Sep 2026) — verified (primary)
- Claude Opus 5.5 — Anthropic (pricing $4/$20 per 1M tokens; ~40% cheaper and ~40% faster than
  Opus 5; Terminal-Bench 4.0 66.4% vs 52.3%; OSWorld 2.0 81.8% vs 74.0%; GDPval-AA v2.1 1846 Elo
  vs 1708; GitHub CPO Mario Rodriguez: "used among the fewest tokens and steps measured"):
  https://www.anthropic.com/news/claude-opus-5-5
- Anthropic news index: https://www.anthropic.com/news

## The builders ask to be governed — UN Security Council (23 Sep 2026)
- Altman and Amodei press the UN Security Council to adopt international AI safety standards — CNN:
  https://edition.cnn.com/2026/09/23/tech/altman-amodei-ai-safety-un-security-council
- Altman, Amodei and the UN on AI safety — CNBC:
  https://www.cnbc.com/2026/09/23/altman-amodei-un-ai-safety.html

## "Pace the frontier" + the agent-swarm warning (12 Sep 2026)
- Anthropic's Amodei on pacing AI; Altman "I agree with Dario that we need to pace the frontier" — Axios:
  https://www.axios.com/2026/09/12/anthropic-ai-amodei-pacing
- Amodei says it's time to slow the pace of improving AI models — Bloomberg:
  https://www.bloomberg.com/news/articles/2026-09-12/anthropic-ceo-says-it-s-time-to-slow-pace-of-improving-ai-models
- Amodei calls for an AI industry slowdown — Washington Post:
  https://www.washingtonpost.com/technology/2026/09/12/anthropic-ceo-dario-amodei-calls-ai-industry-slow-down/
- "AI swarm could take over the entire internet in 6–12 months" / commits to slowdown plan; Gary
  Marcus (NYU) called the claim "nonsensical" — VentureBeat:
  https://venturebeat.com/security/anthropic-ceo-says-ai-swarm-could-take-over-the-entire-internet-in-6-12-months-commits-to-ai-slowdown-plan

## Governance split — the two admiralties
- US pushes a looser approach to AI regulation while the EU pushes new law — Al Jazeera:
  https://www.aljazeera.com/news/2026/9/2/us-pushes-looser-approach-to-ai-regulation-while-eu-pushes-new-law
- G20 adopts the "Carolina Principles" (all 20 agreed, China signed; Commerce Sec. Howard Lutnick;
  White House adviser Michael Kratsios: "should not treat every emerging technology as a
  first-of-a-kind policy problem") — implicator.ai:
  https://www.implicator.ai/g-20-adopts-carolina-principles-ai-regulation/
- Commission starts enforcing AI Act rules and new transparency requirements (2 August) — European Commission:
  https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- Enforcement of the AI Act (fines up to €35M/7% for prohibited practices; up to €15M/3% for
  GPAI-obligation breaches) — European Commission:
  https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act
- EU AI Act — up-to-date developments (incl. reported "Digital Omnibus" delay of standalone
  high-risk Annex III obligations to 2 Dec 2027 and embedded-product Annex I AI to 2 Aug 2028;
  **verify exact dates before citation**): https://artificialintelligenceact.eu/
- EU AI Act enforcement reference — DLA Piper:
  https://intelligence.dlapiper.com/artificial-intelligence/?t=08-enforcement&c=EU

## MCP and agent tooling / standards
- MCP roadmap (HTTP-native transport, agent identity — DPoP, Workload Identity Federation — and
  formal governance) — Model Context Protocol blog: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
- The 2026-07-28 MCP specification (stateless / horizontally scalable):
  https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP roadmap (docs): https://modelcontextprotocol.io/development/roadmap
- Model Context Protocol (governance under the Linux Foundation's Agentic AI Foundation) — Wikipedia:
  https://en.wikipedia.org/wiki/Model_Context_Protocol

## Enterprise agent adoption vs the reality gap
- The 2026 State of AI Agents Report (~80% seeing measurable ROI; barriers: integration 46%, data
  quality 42%, change management 39%) — Anthropic (standing context, not new this week):
  https://resources.anthropic.com/2026-state-of-ai-agents
  · https://resources.anthropic.com/hubfs/The%202026%20State%20of%20AI%20Agents%20Report.pdf
- Gartner: over 40% of agentic-AI projects will be canceled by end of 2027 (also: ≥15% of
  day-to-day work decisions made autonomously via agentic AI by 2028; 33% of enterprise apps
  including agentic AI by 2028):
  https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

## Enterprise agentic access layers — context (Dreamforce 2026, 15–17 Sep)
- Salesforce launches "AIforce" ("AI replaces the UI") and the Koa CRM reasoning model; multi-model
  (Anthropic + Google) support — Salesforce Ben:
  https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/

## Other model releases reported in-window (moderate confidence — primary blocked)
- OpenAI GPT-6 Sol & Luna (reportedly 22 Sep; DevDay 2026 scheduled 29 Sep) — CNBC (Astra headline
  confirmed, body blocked); model-tracker specs UNVERIFIED, do not cite exact numbers:
  https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html · https://openai.com/index/devday-2026/

## Prior rails (background)
- Gartner: 40% of enterprise apps will feature task-specific AI agents by 2026:
  https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- EU regulatory framework for AI (penalties, high-risk regime) — European Commission:
  https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

---

*Editorial framing — the "two admiralties" allegory (the law of the AI seas split into a strict
EU chart and a light-touch G20 chart on the same waters; build to the strictest chart, keep your
papers portable, and read the shipwrights' own "pace the frontier" plea as weather) — is expressly
the radar's own reading, not a sourced claim about any named company or government beyond the
reported EU AI Act, G20, UN, OpenAI, Anthropic and Gartner items above. Figures are marked "as
reported"; blocked-source items should be reconciled against the primary publications before
republishing.*
