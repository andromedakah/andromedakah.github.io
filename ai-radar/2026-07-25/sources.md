# Sources — AI Tech Radar, 25 July 2026 ("The Provenance")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or official that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." This is a contested, developing story — the US government's allegations and the researchers' rebuttals are both presented, and neither is asserted here as settled fact.

## The story — a US distillation accusation clouds the open-weight fallback

### The accusation: White House OSTP and Treasury (22 July 2026)

- Michael Kratsios (Director, White House OSTP), post on X — https://x.com/mkratsios47/status/2079933645888880708
- TechCrunch, "Treasury threatens sanctions after White House claims Moonshot distilled Anthropic's Fable" — https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/
- CyberScoop, "White House accuses Chinese company of distilling Anthropic's Fable" — https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/
- Cryptopolitan, "White House accuses Moonshot of distilling Anthropic's Fable for Kimi K3" — https://www.cryptopolitan.com/white-house-moonshot-anthropic-fable-kimi-k3/
- Cryptobriefing, "White House accuses Moonshot AI of using Anthropic's Fable to build Kimi K3" — https://cryptobriefing.com/moonshot-ai-distillation-allegations/
- SiliconANGLE, "Senior White House official accuses Moonshot AI of copying Anthropic's leading frontier model" — https://siliconangle.com/2026/07/23/senior-white-house-official-accuses-moonshot-ai-copying-anthropics-leading-frontier-model/
- Seeking Alpha, "Trump official says Moonshot built Kimi K3 through theft of Anthropic's Fable" — https://seekingalpha.com/news/4616700-kratsios-says-moonshot-built-kimi-k3-through-industrial-distillation-of-anthropics-fable
- The Hill, "White House official accuses Chinese startup of distilling Anthropic model, accessing banned Nvidia chips" — https://thehill.com/policy/technology/5984510-white-house-moonshot-ai-anthropic-nvidia/
- SiliconANGLE, "U.S. Treasury Secretary Bessent threatens sanctions against Chinese AI model makers" — https://siliconangle.com/2026/07/21/u-s-treasury-secretary-bessent-threatens-sanctions-chinese-ai-model-makers/
- CNBC, "Bessent says U.S. could sanction China over AI model 'theft'" — https://www.cnbc.com/2026/07/21/bessent-china-ai-sanctions.html
- Gizmodo, "US Treasury Chief Threatens Sanctions on Chinese AI Labs Over 'IP Theft' Concerns" — https://gizmodo.com/us-treasury-chief-threatens-sanctions-on-chinese-ai-labs-over-ip-theft-concerns-2000788553
- Quartz, "Scott Bessent warns China of sanctions over AI model theft" — https://qz.com/bessent-china-ai-sanctions-distillation-072126

Claims sourced here (as reported): On 22 July 2026, White House OSTP Director Michael Kratsios posted that the US has "information that Moonshot AI distilled Anthropic's Fable for the development of its K3 model," describing "a sophisticated internal platform to conduct large scale distillation against U.S. models, allowing them to quickly switch between multiple methods of access to avoid detection," and separately alleged Moonshot had "acquired GB300-equipped servers and has accessed GB300s in Thailand, likely to train its AI models" (Nvidia GB300s are export-restricted to China). He characterized it as "large-scale, covert industrial distillation aimed at stealing proprietary U.S. technology and undermining American research." Treasury Secretary Scott Bessent said "Open source is not open season on American IP" and that when Chinese firms "conduct covert, industrial-scale distillation attacks that cross the line into IP theft, sanctions and Entity List designations will be on the table."

### The pushback: independent researchers dispute the claim (23 July 2026)

- TechCrunch, "Experts say exploiting Anthropic's Fable isn't how Kimi K3 got so good" — https://techcrunch.com/2026/07/23/experts-say-exploiting-anthropics-fable-isnt-how-kimi-k3-got-so-good/
- South China Morning Post, "Global AI experts push back on US 'distillation' claims against Moonshot's Kimi K3 model" — https://www.scmp.com/tech/tech-war/article/3361625/global-ai-experts-push-back-us-distillation-claims-against-moonshots-kimi-k3-model
- AI Weekly, "Researchers doubt Kimi K3 was distilled from Anthropic's Fable" — https://aiweekly.co/alerts/researchers-doubt-kimi-k3-was-distilled-from-anthropics-fable
- Bitcoin World, "Experts Question Claims That Kimi K3 Reached Frontier Level By Copying Anthropic's Fable" — https://bitcoinworld.co.in/experts-question-kimi-k3-anthropic-fable-distillation-claims/
- PetaPixel, "The US is Concerned Over 'IP Theft' by Chinese AI Labs" — https://petapixel.com/2026/07/22/the-us-is-concerned-over-ip-theft-by-chinese-ai-labs/
- pbxscience, "How Do You Build an AI Model by 'Distilling' Another AI? And Did China's Kimi Really Do It?" — https://pbxscience.com/how-do-you-build-an-ai-model-by-distilling-another-ai-and-did-chinas-kimi-really-do-it/

Claims sourced here (as reported): A number of AI researchers disputed the claim that distillation from Fable primarily explains Kimi K3's capabilities, some calling the accusations "political" and "reckless" and noting that an AI model's outputs are not copyrighted. Researcher Braden Hancock said, "I don't think you get a model this strong and this quickly on the heels of Fable doing strictly distillation." A Moonshot AI employee (Randy Xian) pointed to the narrow window — Fable went public on 1 July and K3 launched ~15 July — asking how a "brand new frontier model" could be trained "in JUST 15 DAYS." Coverage notes distillation is common across the industry, with Elon Musk having testified earlier in 2026 that xAI distilled OpenAI models to develop Grok.

### The February 2026 backdrop: Anthropic's earlier allegation

- Fortune, "Anthropic, China, DeepSeek: theft, Claude, distillation, copyright, national security" — https://dc.fortune.com/2026/02/24/anthropic-china-deepseek-theft-claude-distillation-copyright-national-security

Claims sourced here (as reported): In February 2026 Anthropic named DeepSeek, Moonshot AI and MiniMax, stating the three companies used approximately 24,000 fabricated accounts to generate more than 16 million Claude chat interactions in violation of its terms of service and regional access restrictions. As of this edition's coverage, Anthropic had not publicly said it possesses evidence tying Kimi K3 specifically to distillation from Fable.

## The masterworks — the open-weight fallbacks in question

### Kimi K3 (open weights 27 July 2026)

- Cryptobriefing, "Kimi K3 launches with 2.8 trillion parameters, open weights dropping July 27" — https://cryptobriefing.com/kimi-k3-open-weights-july-27/
- Nathan Lambert (Interconnects), "Kimi K3: The open-weights escalation" — https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation
- ExplainX, "Kimi K3 API Guide: 2.8T Model, Pricing, 1M Context (2026)" — https://explainx.ai/blog/kimi-k3-moonshot-beta-leaks-july-2026

Claim sourced here (as reported): Moonshot AI's Kimi K3 is a 2.8-trillion-parameter open-weight model; Moonshot committed to publishing its full open weights on 27 July 2026 under a Modified MIT license.

### DeepSeek V4 (open-weight MoE; MIT)

- Morph, "DeepSeek V4: 1.6T MoE, 1M Context, $0.87/M Output. Architecture, Benchmarks, Pricing (2026)" — https://www.morphllm.com/deepseek-v4
- DataCamp, "DeepSeek V4: Features, Benchmarks, and Comparisons" — https://www.datacamp.com/blog/deepseek-v4
- Codersera, "DeepSeek V4-Pro Review: Benchmarks, Pricing, Verdict (2026)" — https://codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/
- OpenRouter, "DeepSeek V4 Pro — API Pricing & Benchmarks" — https://openrouter.ai/deepseek/deepseek-v4-pro

Claims sourced here (as reported): DeepSeek V4 is an open-weight mixture-of-experts model family under the MIT license. V4-Pro has 1.6T total parameters (49B active), prices at ~$0.87/M output, scores ~80.6% on SWE-bench Verified — the highest open-weights entry — and is roughly 29× cheaper per output token than Claude Opus 4.8. It remains a differently-sourced (MIT-licensed) open-weight option alongside any Kimi K3 an enterprise qualifies.

## The standing counterparts (continuing threads from prior editions)

### MCP final spec (28 July 2026)

- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- WorkOS, "Everything your team needs to know about MCP in 2026" — https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026

Claim sourced here: The MCP 2026-07-28 specification — the protocol's largest revision — goes final on 28 July 2026.

### EU AI Act GPAI enforcement (applicable 2 August 2026)

- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Artificial Intelligence Act, "Enforcement of Chapter V under the EU AI Act" — https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/
- beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines

Claims sourced here: From 2 August 2026 the European Commission's enforcement powers over general-purpose AI (GPAI) providers become fully applicable — including the power to request documentation (Article 91), conduct independent evaluations (Article 92), request measures including risk mitigation (Article 93), and impose fines of up to €15 million or 3% of global annual turnover (Article 101). Obligations reach deployers, not only model providers.

### Supporting adoption/governance figures (continuing threads)

- OutSystems survey of ~1,900 IT leaders — relayed via coverage (only 12% of enterprises say they can actually govern their AI agents). See TechTimes, "Gemini Enterprise Agent Platform Leads Enterprise AI Governance as OpenAI Starts Billing for Agents" — https://www.techtimes.com/articles/320956/20260719/gemini-enterprise-agent-platform-leads-enterprise-ai-governance-openai-starts-billing-agents.htm
- Gartner, "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027" — https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

Claims sourced here: a 2026 OutSystems survey of ~1,900 IT leaders found only 12% of enterprises say they can actually govern their AI agents (as reported); Gartner predicts more than 40% of agentic-AI projects will be canceled by end-2027.

---

*Editorial lines marked as the radar's own (e.g. "An open-weight model is a masterwork, and a masterwork is only as hangable as its provenance…") are the AI Tech Radar's framing and are not third-party quotes. The provenance allegory — the art-market principle that a painting's value and title depend on an unbroken, documented chain of custody; that a contested or broken provenance freezes a sale and depresses value regardless of the work's quality; that provenance disputes may be genuine theft or thin and political; and that serious collectors survive by demanding the file, insuring title, and diversifying rather than anchoring on one disputed work — is a well-worn illustration used allegorically, told approximately, and is not a sourced claim about any specific artwork or about AI. This is a developing and disputed story: the US government's allegations (Kratsios, Bessent) and the researchers' rebuttals are both relayed as reported, and neither the distillation claim nor the GB300 claim is asserted here as established fact. The "2 days," "3 days" and "8 days" figures are simple counts from this edition's date (25 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own. Firm, official and product names (Moonshot AI, Anthropic, OpenAI, xAI, DeepSeek, Kimi K3, Fable, Nvidia GB300, MCP, OutSystems, Gartner, the White House OSTP, the U.S. Treasury, Michael Kratsios, Scott Bessent, Braden Hancock) reflect the sources as described in the cited 2026 material.*
