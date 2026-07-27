# Sources — AI Tech Radar, 27 July 2026 ("The Powder Magazine")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or official that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." The UK AISI / US CAISI joint assessment is described by its authors as "preliminary," and the Kimi K3 distillation question referenced from yesterday's edition remains contested.

## The story — the open-weight commodity lands, with a government blast rating

### Kimi K3 open weights go live (27 July 2026, 00:00 UTC)

- TechTimes, "Kimi K3 Open Weights Drop July 27: Near-Frontier Coding, Undisclosed Hallucination Risk" — https://www.techtimes.com/articles/321499/20260724/kimi-k3-open-weights-drop-july-27-near-frontier-coding-undisclosed-hallucination-risk.htm
- TechTimes, "Kimi K3 Open Weights Arrive Sunday: Self-Hosting Cuts China Data Risk the API Never Can" — https://www.techtimes.com/articles/321551/20260725/kimi-k3-open-weights-arrive-sunday-self-hosting-cuts-china-data-risk-api-never-can.htm
- TECHi, "Kimi K3's open weights arrive July 27. The catch is 1.4TB" — https://www.techi.com/kimi-k3-open-weights-inference-economics/
- VentureBeat, "China's Moonshot AI releases Kimi K3, the largest open-source model ever, rivaling top U.S. systems" — https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems
- Simon Willison, "Kimi K3, and what we can still learn from the pelican benchmark" — https://simonwillison.net/2026/Jul/16/kimi-k3/
- buildfastwithai, "AI News Today July 27 2026: 16 Biggest Stories" — https://www.buildfastwithai.com/blogs/ai-news-today-july-27-2026

Claims sourced here (as reported): Moonshot AI published the full open weights of Kimi K3 at 00:00 UTC on 27 July 2026 under a Modified MIT license — a 2.8-trillion-parameter mixture-of-experts model (~50B active parameters, 16 of 896 experts firing per token, 1M-token context, multimodal), the largest open-weight release in history, roughly 1.4 TB in four-bit MXFP4 quantization. It had been accessible via Moonshot's hosted API and kimi.com since 16 July 2026.

### The UK AISI / US CAISI joint cyber assessment

- UK AI Security Institute (AISI), "Preliminary Assessment of Kimi K3's Cyber Capabilities" — https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities
- NIST, "UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities" — https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities
- MLQ News, "UK and US AI Safety Institutes Find Kimi K3 Scores 32% on Cyber Exploits vs. 76% for US Models" — https://mlq.ai/news/uk-and-us-ai-safety-institutes-find-kimi-k3-scores-32-on-cyber-exploits-vs-76-for-us-models/
- Cryptopolitan, "Kimi K3 lags US frontier models on cyberattack tasks, UK-US labs find" — https://www.cryptopolitan.com/kimi-k3-lags-us-models-cyberattack-tasks/
- the-decoder, "Kimi K3 trails frontier US models by a wide margin on cyber exploits, and distillation may explain why" — https://the-decoder.com/kimi-k3-trails-frontier-us-models-by-a-wide-margin-on-cyber-exploits-and-distillation-may-explain-why/
- XenoSpectrum, "Why Is Kimi K3's Cyberattack Capability Less Than Half of the US Level? What the 32% vs. 76% Gap Reveals About Testing Conditions" — https://xenospectrum.com/en/kimi-k3-cyber-capability-benchmark/
- Zerberus, "Open-Weight AI Models Are Bypassing Safety Filters: What the UK AISI Kimi K3 Evaluation Means for Enterprise AI Security" — https://www.zerberus.ai/blog/open-weight-ai-safety-filters-aisi-kimi-k3-enterprise-security/
- intellectia.ai, "UK's AISI and US' CAISI Jointly Assess Kimi K3's Cyber Capabilities" — https://intellectia.ai/news/stock/a-joint-preliminary-evaluation-by-the-uks-aisi-and-the-us-caisi-finds-kimi-k3-trails-leading-us-frontier-closed-weight-models-on-cyber-capability-ai-security-institute

Claims sourced here (as reported): A joint preliminary cyber assessment by the UK AI Security Institute (AISI) and the US Center for AI Standards and Innovation (CAISI) found Kimi K3 trails leading US frontier closed-weight models on cyber tasks — scoring 32% on ExploitBench (a Carnegie Mellon benchmark of 41 post-2023 Chrome V8 vulnerabilities) versus 76% for top US models, and reaching step 17 of a 32-step "The Last Ones" (TLO) simulated corporate-network attack (~20 hosts across four subnets) on average versus 28.5 for leading US closed-weight models and step 11 for peer open model GLM-5.2, completing the full 32-step path in 1 of 10 attempts within a 100-million-token budget. The institutes reported that K3's guardrails "did not prevent it from attempting cyber exploit development or offensive cyber operations," and coverage noted that when weights are released publicly "the developer loses all downstream control, and safeguards cannot be remotely updated or revoked." The assessment is described by its authors as preliminary; the "distillation may explain the gap" framing is one analysis (the-decoder), relayed as reported.

## The frontier moved away — Claude Opus 5 (24 July 2026)

- Anthropic / coverage: Coursiv, "Claude Opus 5: Benchmarks, Pricing, and Full Guide (July 2026)" — https://coursiv.io/blog/claude-opus-5
- Codersera, "Claude Opus 5: Benchmarks, Pricing & How It Compares (2026 Launch Guide)" — https://codersera.com/blog/claude-opus-5-launch-guide-2026/
- Fello AI, "Claude Opus 5: Pricing, Benchmarks & Effort Setting" — https://felloai.com/claude-opus-5/
- ExplainX, "Claude Opus 5 Launch — Benchmarks, Price, Fast Mode" — https://www.explainx.ai/blog/claude-opus-5-launch-july-2026
- The PC Enthusiast, "Anthropic Launches Claude Opus 5, Bringing Near-Fable AI Performance at Half the Price" — https://thepcenthusiast.com/anthropic-claude-opus-5-launch/
- BenchLM, "Claude Opus 5 Benchmarks, Pricing & Speed (July 2026)" — https://benchlm.ai/models/claude-opus-5

Claims sourced here (as reported): Anthropic released Claude Opus 5 on 24 July 2026, priced at $5 per million input tokens and $25 per million output tokens (identical to Opus 4.8, about half of Claude Fable 5's $10/$50), with a low/medium/high effort setting. Opus 5 scored 43.3% on Frontier-Bench agentic coding (beating Fable 5 and OpenAI's GPT-5.6 Sol), and independent testing from Artificial Analysis ranked it #1 on both its Intelligence Index and its Agentic Index on launch day. The characterization that Opus 5 "excels at verifying its work and iterating carefully until it succeeds" is attributed to Anthropic via coverage (as reported).

## The capex bill reaches the bond market

- CNBC, "Bond market anxiety is growing over AI capex budgets" (24 July 2026) — https://www.cnbc.com/2026/07/24/bond-market-anxiety-ai-capex-spending.html
- CNBC, "1 hyperscaler megacap down, 3 to go. Alphabet raises the stakes on AI spending" (24 July 2026) — https://www.cnbc.com/2026/07/24/1-hyperscaler-megacap-down-3-to-go-alphabet-raises-the-stakes-on-ai-spending.html
- Yahoo Finance, "Citigroup forecasts Big Tech's AI spending to cross $2.8 trillion by 2029" — https://finance.yahoo.com/news/citigroup-forecasts-big-techs-ai-111915251.html
- Futurum Group, "AI Capex 2026: The $690B Infrastructure Sprint" — https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/

Claims sourced here (as reported): Bond-market anxiety grew over hyperscaler AI capital expenditure after Alphabet lifted its AI-buildout capex forecast, with credit spreads widening for Google, Amazon and Meta as fixed-income investors demanded more yield. Citigroup's updated forecast puts hyperscaler AI capex at roughly $490B by end-2026; the four largest hyperscalers (Amazon, Google, Microsoft, Meta) collectively plan ~$250B in 2026, up from ~$100B in 2025 (a ~77% year-over-year increase); OpenAI's ~$20B ARR represents roughly 3% of the projected 2026 hyperscaler capex total. Figures relayed via July 2026 market reporting as reported.

## The standing threads

### EU AI Act — Article 50 transparency and GPAI enforcement (2 August 2026)

- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European Commission, "Transparency obligations under Article 50 of the AI Act" (FAQ) — https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- EU Artificial Intelligence Act, "The EU AI Act's Transparency Rules: A Practical Guide to Article 50" — https://artificialintelligenceact.eu/transparency-rules-article-50/
- Sidley (Data Matters), "EU AI Act Transparency Obligations: Preparing for Compliance by 2 August 2026" — https://datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026/
- ComplianceHub, "What Actually Comes Due on August 2, 2026: EU AI Act Article 50 Transparency and the Digital Omnibus Reset" — https://compliancehub.wiki/eu-ai-act-article-50-transparency-digital-omnibus-2026/

Claims sourced here: On 2 August 2026, Article 50 transparency obligations (chatbot/agent disclosure, machine-readable marking of AI-generated content, deepfake labeling) become enforceable across all 27 member states, and the Commission's GPAI enforcement powers apply — both carrying the higher of €15 million or 3% of global turnover under Article 99. The Digital Omnibus deferred the high-risk obligations of Chapter III (Annex III standalone systems to 2 December 2027; Annex I embedded products to 2 August 2028) but did not move the transparency or GPAI dates.

### MCP final spec (28 July 2026)

- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Model Context Protocol blog, "Beta SDKs for the 2026-07-28 MCP Spec Release Candidate Are Here" — https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/
- The Register, "Model Context Protocol prepares to break with its stateful past" — https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/
- WorkOS, "The biggest MCP spec update ships July 28: What changes for AI agent authentication" — https://workos.com/blog/mcp-2026-spec-agent-authentication

Claim sourced here: The MCP 2026-07-28 specification — the protocol's largest revision, moving the core to a stateless architecture with hardened authorization — goes final on 28 July 2026.

### Supporting governance figure (continuing thread)

- OutSystems survey of ~1,900 IT leaders (only 12% of enterprises say they can actually govern their AI agents) — relayed via coverage (as reported).

---

*Editorial lines marked as the radar's own (e.g. "An open-weight model is licensed explosive, not free software. The government stamps the blast rating; you build the magazine — and you store the detonator apart from the charge.") are the AI Tech Radar's framing and are not third-party quotes. The powder-magazine allegory — the historical practice of governing cheap, dual-use industrial explosive not by prohibition but by physical custody (a licensed, isolated store; a magazine-keeper; a logbook; quantity and distance limits; and storing the detonator/blasting cap apart from the charge) — is a well-worn illustration used allegorically, told approximately, and is not a sourced claim about any specific explosives regime or about AI. The "1 day" and "6 days" figures are simple counts from this edition's date (27 July 2026) to 28 July and 2 August 2026 respectively and are the radar's own. Regulation, product, firm, benchmark and institute names (Moonshot AI, Kimi K3, GLM-5.2, the UK AI Security Institute, the US Center for AI Standards and Innovation, NIST, Anthropic, Claude Opus 5, Claude Fable 5, GPT-5.6 Sol, Artificial Analysis, ExploitBench, "The Last Ones"/TLO, Citigroup, the European Commission, MCP, OutSystems) reflect the sources as described in the cited 2026 material. This is a developing story: the AISI/CAISI assessment is described by its authors as "preliminary," and the Kimi K3 distillation question remains contested.*
