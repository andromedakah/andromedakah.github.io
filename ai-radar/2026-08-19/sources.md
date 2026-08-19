# Sources — AI Tech Radar, 19 August 2026 ("The Ballast")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or outlet that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Note: several primary publisher pages (OpenAI, CNBC and various trade outlets) were unreachable from the compile environment behind the network egress proxy; those items were verified by cross-referencing multiple reputable outlets and are flagged accordingly.

## The story — AI's center of gravity moves to production (enterprise + inference)

### The demand load — enterprise revenue overtakes consumer

- OpenAI, "The next phase of enterprise AI" — https://openai.com/index/next-phase-of-enterprise-ai/
- OpenAI, "Enterprise signals: What frontier firms are doing differently" — https://openai.com/signals/enterprise-data/
- CNBC, "OpenAI CFO Friar tells investors that enterprise is bigger than consumer" — https://www.cnbc.com/2026/08/14/openai-cfo-friar-tells-investors-that-enterprise-bigger-than-consumer.html
- TheStreet, "OpenAI's CFO notes shift in business revenue" — https://www.thestreet.com/investing/openai-enterprise-revenue-passes-consumer-friar-ipo
- Yahoo Finance, "OpenAI Says Enterprise AI Is Already 40% of Its Revenue Amid 'Agentic Workflow' Shift" — https://finance.yahoo.com/sectors/technology/articles/openai-says-enterprise-ai-already-183912683.html
- Unite.AI, "OpenAI Tells Investors Enterprise Revenue Has Overtaken Its ChatGPT Consumer Business" — https://www.unite.ai/openai-tells-investors-enterprise-revenue-has-overtaken-its-chatgpt-consumer-business/
- TechTimes, "OpenAI Enterprise Revenue Tops Consumer for First Time: $40 Billion ARR Two Quarters Early" — https://www.techtimes.com/articles/324562/20260815/openai-enterprise-revenue-tops-consumer-first-time-40-billion-arr-two-quarters-early.htm
- Briefs.co, "OpenAI Enterprise Revenue Now Top Source" — https://www.briefs.co/news/enterprise-customers-are-now-openai-s-biggest-revenue-source/
- Aroged, "The enterprise sector brings more revenue to OpenAI than the consumer sector" — https://www.aroged.com/2026/08/15/the-enterprise-sector-brings-more-revenue-to-openai-than-the-consumer-sector/

Claims sourced here (as reported): On 14 August 2026, OpenAI CFO Sarah Friar told investors that enterprise revenue had, for the first time, overtaken consumer revenue; that the company was at roughly a $40 billion annualized run-rate; that business-customer revenue rose ~32% in a single month; and that this pulled the consumer/enterprise crossover roughly two full quarters ahead of the prior forecast of parity by year-end. Separately, OpenAI's "The next phase of enterprise AI" states that enterprise now makes up more than 40% of the company's revenue, driven by enterprises adopting "teams of agents," and carries the Denise Dresser quotation ("I have never seen this level of conviction spread so quickly and consistently within the industries."). Figures are relayed via multiple secondary outlets as reported (primary OpenAI and CNBC pages were unreachable behind the egress proxy) and should be re-verified at source before republishing.

### The other lab — Anthropic leans enterprise-agent too

- Anthropic / Claude, "How enterprises are building AI agents in 2026" — https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026
- Anthropic, Newsroom — https://www.anthropic.com/news
- Anthropic, "The Briefing: Enterprise Agents" (virtual event) — https://www.anthropic.com/events/the-briefing-enterprise-agents-virtual-event

Claims sourced here (as reported): On or about 18 August 2026, Anthropic published "How enterprises are building AI agents in 2026," alongside enterprise-agent material including a Claude Managed Agents case study (around 17 August). Cited as corroborating evidence that both frontier labs' growth is bending toward enterprises running agents in production.

### The compute load — inference spend beats training in 2026

- Gartner via TechTimes, "Gartner Marks First Year Inference Spending Beats AI Training: 55 Cents of Every Cloud Dollar" — https://www.techtimes.com/articles/323879/20260811/gartner-marks-first-year-inference-spending-beats-ai-training-55-cents-every-cloud-dollar.htm
- InfotechLead, "AI Agent Inference Costs to Rise More Than 5X by 2028 as AI Spending Hits $2.59 Trillion" — https://infotechlead.com/artificial-intelligence/ai-agent-inference-costs-to-rise-more-than-5x-by-2028-as-ai-spending-hits-2-59-trillion-97797
- Pure AI, "Will Inference and AI Agents Break Enterprise GenAI Budgets?" — https://pureai.com/articles/2026/06/16/will-inference-and-ai-agents-break-enterprise-genai-budgets.aspx
- NeuralWired, "Gartner: AI Inference Cost Won't Drop Your Bill in 2026" — https://neuralwired.com/2026/06/20/gartner-llm-inference-cost-enterprise/
- DigitalApplied, "AI Spending Forecasts 2026: Gartner, IDC & Stanford" — https://www.digitalapplied.com/blog/ai-spending-forecasts-2026-gartner-idc-stanford-compiled

Claims sourced here (as reported, approximate): Gartner forecasts that 2026 is the first year inference spending exceeds training — within AI-optimized IaaS, ~$23.3 billion of inference against ~$19 billion of training, a segment expanding ~96.4% to ~$42.276 billion — with inference accounting for roughly 55 cents of every AI-cloud dollar. Agentic reasoning can cost at least five times (and up to ~30×) more tokens per task than a basic chatbot interaction, while per-token prices have fallen as much as ~280-fold since 2022, so total enterprise spend rises even as unit prices fall. IDC expects AI-infrastructure spending to reach ~$487 billion in 2026 (+53% year-over-year).

### The scale — the tokens (running, not building)

- AMD Investor Relations, "AAI 2026: AMD Delivers Full-Stack Compute for the Agentic AI Era" — https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era
- Frontier Enterprise, "AI agents are changing where enterprise computing happens" — https://www.frontier-enterprise.com/ai-agents-are-changing-where-enterprise-computing-happens
- IT Pro, "AMD hops on the agentic bandwagon at Advancing AI 2026" — https://www.itpro.com/technology/artificial-intelligence/amd-hops-on-the-agentic-bandwagon-at-advancing-ai-2026
- AI Magazine, "AMD: Advancing AI Data Centres, Networks and Robots" — https://aimagazine.com/articles/amd-unveils-next-gen-ai-hardware-software

Claims sourced here (as reported): At AMD's Advancing AI 2026 keynote, AMD reported that more than 35 quadrillion tokens are now consumed each month (an increase of nearly 160× in two years), and that in 2026, for the first time, the world is using more AI compute to run models than to train them, with roughly 60% of global AI compute capacity used for inference this year. Jeetu Patel (President and Chief Product Officer, Cisco) is quoted saying "Humans click, but agents swarm" while discussing how agentic AI reshapes inference workloads.

## The engine — commodity models, priced per token

- LLM Gateway, "New AI Model Releases — August 2026 Timeline" — https://llmgateway.io/timeline
- llm-stats.com, "LLM News Today (August 2026)" — https://llm-stats.com/ai-news
- AI Release Tracker, "Latest AI Model Releases — August 2026" — https://aireleasetracker.com/latest
- Evertune, "AI Model Release Tracker" — https://www.evertune.ai/resources/ai-model-tracker
- Google Developers Blog, "Scaling AI Agent Infrastructure with the MCP Stateless updates" — https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/

Claims sourced here (as reported, standing context): Gemini 3.7 Flash shipped on or about 13 August 2026 built "for agents." The standing engine field carried as context — Claude Opus 5, OpenAI GPT-5.6 Sol, xAI Grok 4.6 (at $2/$6 per million tokens), open-weight Z.ai GLM-5.3 and Alibaba Qwen3.8 (14 August), Moonshot Kimi K3 and DeepSeek V4-Pro — is relayed from model-tracker and vendor coverage as the rented, swappable, per-token-priced model layer.

## The rails — the plumbing standardizes

- Official Model Context Protocol blog, "The 2026-07-28 Specification" — https://blog.modelcontextprotocol.io/posts/2026-07-28/
- ITdaily, "MCP protocol receives major update: more secure and production-ready" — https://itdaily.com/news/software/mcp-2026-update-specs/
- Gravitee, "Scaling AI Agents: Key Takeaways from the MCP Specification Release" — https://www.gravitee.io/blog/scaling-ai-agents-key-takeaways-from-the-model-context-protocol-mcp-specification-release

Claims sourced here: The MCP 2026-07-28 specification introduced a stateless protocol core (each request self-contained), an Extensions framework, the AWS-contributed Tasks extension for reliable long-running agents, MCP Apps, authorization hardening and a formal deprecation policy. The TypeScript and Python SDKs are each past one billion total downloads. Cited here as the rail the agent fleet runs on in production.

## The gate — the trust layer is live

- European Commission, "Commission starts enforcing AI Act rules and new transparency requirements on 2 August" — https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- Beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/
- MediaLaws, "EU AI Obligations for GPAI Providers: Compliance, Enforcement & Deadlines (2025–2027)" — https://www.medialaws.eu/eu-ai-obligations-for-gpai-providers-compliance-enforcement-deadlines-2025-2027/

Claims sourced here (as reported): As of 2 August 2026, the European Commission's enforcement and penalty powers over general-purpose AI (GPAI) providers became applicable — including powers to request documentation and information, conduct evaluations, request measures (compliance, risk mitigation, market restriction, recall and withdrawal), and impose fines up to the higher of €15 million or 3% of worldwide annual turnover under Article 101. The transparency duties (disclose AI interaction, machine-readable labeling of AI-generated content) also apply. Cited as the heavier bar a working AI system in production must meet, versus a demo.

## Prior-day context (background only)

Claims sourced here (context only): This week's earlier editions — "The Deputy" (18 Aug, the acting agent and identity/mandate/audit), "The Far Bank" (17 Aug, the crossing from pilot to value and MIT NANDA's 95% figure), "The Free Table" (16 Aug, the vendor business model), "The Last Mile" (15 Aug, distribution) and "The Harbor Pilot" (14 Aug, the pilotage/context layer) — are referenced only as prior-day background to the center-of-gravity thesis.

---

*Editorial lines marked as the radar's own (e.g. "When the crowd stops being your customer and the guild starts, and the fire stops forging and starts sailing, your ballast has shifted. Steer to the weight you carry — an owner, an SLA, a metered bill — or you broach in the first real weather.") are the AI Tech Radar's framing and are not third-party quotes. The ship / ballast / trade-era allegory — a trading ship built for the wonder of the crowd whose ballast shifts when guild charters outweigh visitors' fares and when the furnaces burn to sail rather than to forge, requiring the captain to re-trim with a named master of the hold, a metered coal budget and rigging for standing crews, while a customs officer holds a working ship to a heavier standard — is a common illustration used allegorically and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported"; the OpenAI enterprise/consumer crossover figures, the Sarah Friar remarks, the Gartner inference/training and agentic-token figures, the IDC infrastructure figure, and the AMD token-scale figures rest partly on secondary coverage of egress-blocked primary pages and should be re-verified at source before republishing. Product, firm and institution names (OpenAI, Anthropic, Cisco, AMD, Gartner, IDC, Google, xAI, Z.ai/Alibaba/Qwen, Moonshot, DeepSeek, the European Commission) reflect the sources as described in the cited 2026 material. This edition's central datable development in the window is OpenAI CFO Sarah Friar's 14 August statement that enterprise revenue overtook consumer for the first time (~$40B ARR, ~two quarters early, >40% of revenue, "teams of agents"), set against Gartner's finding that 2026 is the first year inference spending beats training — together evidence that AI's center of gravity has shifted from consumer to enterprise and from building to running.*
