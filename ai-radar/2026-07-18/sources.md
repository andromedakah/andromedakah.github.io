# Sources — AI Tech Radar, 18 July 2026 ("The Aluminum Age")

Every claim in this edition traces to a public source below. Figures are attributed to the organization that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage — or rests on a vendor's self-reported benchmarks — it is marked "as reported." Benchmark numbers for a model this new are provisional and, in several cases, self-reported by Moonshot AI or drawn from early independent evaluators; treat them as directional.

## The story — Moonshot AI's Kimi K3 (specs, benchmarks, price, open weights)

- Simon Willison, "Kimi K3, and what we can still learn from the pelican benchmark" — https://simonwillison.net/2026/Jul/16/kimi-k3/
- TechCrunch, "Moonshot's upcoming Kimi 3 is expected to close the gap with Anthropic's Opus 4.8" — https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/
- VentureBeat, "China's Moonshot AI releases Kimi K3, the largest open-source model ever, rivaling top U.S. systems" — https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems
- Tom's Hardware, "China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena — Moonshot AI delivers largest open-weight AI model ever" — https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3
- Constellation Research, "Moonshot AI launches Kimi K3" — https://www.constellationr.com/insights/news/moonshot-ai-launches-kimi-k3
- latent.space, "[AINews] Kimi K3 2.8T-A50B: the largest open model ever released; Opus 4.8-class at Sonnet 5 pricing" — https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest
- MLQ News, "Moonshot AI Releases Kimi K3, a 2.8-Trillion-Parameter Open-Weight Model Rivaling Top U.S. Systems" — https://mlq.ai/news/moonshot-ai-releases-kimi-k3-a-28-trillion-parameter-open-weight-model-rivaling-top-us-systems/

Claims sourced here: On 16 July 2026 Moonshot AI released Kimi K3, a 2.8-trillion-parameter mixture-of-experts model — the largest open-weight model released to date — with a reported ~50B active parameters (896 experts, 16 routed per token, hence the "A50B" designation), a 1-million-token context window, and multimodal (text/image/video) input. The model is live via the Kimi app, web Playground, and API (model id `kimi-k3`). Moonshot has committed to releasing the full weights on Hugging Face by 27 July 2026 under a Modified MIT license (weights were not downloadable at launch). The result was achieved despite roughly three years of escalating US semiconductor export controls.

## Benchmarks and rankings

- Codersera, "Kimi K3 Benchmarks: How It Stacks Up vs Fable 5, GPT-5.6 Sol & Opus 4.8 (2026)" — https://codersera.com/blog/kimi-k3-benchmarks-comparison-2026/
- Graphify Guides, "Kimi K3: Architecture, Benchmarks, Pricing, and Open Weights" — https://graphify.net/ai-coding/llms/kimi-k3/
- NxCode, "Kimi K3 Benchmarks Explained: A Coding-Agent Evaluation Guide" — https://www.nxcode.io/resources/news/kimi-k3-benchmarks-coding-agent-evaluation-guide-2026
- OfficeChai, "Kimi K3 Beats Fable 5, GPT 5.6 On Some Benchmarks In Frontier-Level Performance" — https://officechai.com/ai/kimi-k3-benchmarks/
- OpenLM.ai, "Kimi K3" — https://openlm.ai/kimi-k3/
- Constellation Research (as above), and the trendingtopics.eu coverage below.

Claims sourced here (as reported / self-reported): Kimi K3 took the #1 spot in the Frontend Code Arena with 1,679 points, ahead of Claude Fable 5 (1,631), GPT-5.6 Sol (1,618) and GLM-5.2 (1,587). It leads Program Bench (77.8, edging GPT-5.6 Sol's 77.6 and Fable 5's 76.8) and SWE Marathon (42.0, ahead of Opus 4.8's 40.0 and GPT-5.6 Sol's 39.0), scores 88.3 on Terminal-Bench 2.1, 81.2 on FrontierSWE, 67.5 on DeepSWE, and ~1,668 Elo on GDPval v2 (2nd, behind Fable 5's 1,760 and GPT-5.6 Sol's 1,748). On independent aggregate indices it lands roughly 3rd–4th overall — beating Claude Opus 4.8, trailing only Claude Fable 5 and GPT-5.6 Sol. Fable 5 still leads the aggregate Intelligence Index, GDPval and AA-Briefcase.

## Pricing and cost comparison

- kie.ai, "Kimi K3 Pricing: $3/$15 per 1M Tokens (2026)" — https://kie.ai/blog/kimi-k3-pricing
- apidog, "Kimi K3 Pricing: API Costs and the Cache-Hit Math" — https://apidog.com/blog/kimi-k3-pricing/
- OpenRouter, "Kimi K3 — API Pricing & Benchmarks" — https://openrouter.ai/moonshotai/kimi-k3
- the-decoder, "Kimi's open model K3 nears GPT-5.6 Sol and Fable 5 while signaling the end of super cheap Chinese AI" — https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/
- R&D World, "China's Kimi K3 comes close to Fable benchmarks at one-third the token price" — https://www.rdworldonline.com/chinas-kimi-k3-comes-close-to-fable-benchmarks-at-one-third-the-price/

Claims sourced here (as reported): Kimi K3 API pricing is $3.00 per million input tokens (cache miss), $0.30 per million cache-hit input tokens, and $15.00 per million output tokens — described as "Opus-class at Sonnet-5 pricing." Against Claude Opus 4.8 (~$5 input / $25 output) K3 is cheaper on every axis, roughly 40% cheaper before caching; it is also cheaper than GPT-5.6 Sol (~$5 / $30), though OpenAI's cheaper Terra/Luna tiers undercut it at lower capability. R&D World frames K3 as reaching near-Fable benchmarks "at one-third the token price"; the-decoder reads the $3/$15 pricing as the "end of super-cheap Chinese AI" — still well under US frontier pricing, but above prior ultra-discounted Chinese models.

## The market read and geopolitics

- Axios, "China's open-weight Kimi model stuns AI world with frontier-level results" (16 July 2026) — https://www.axios.com/2026/07/16/moonshot-kimi-ai-china-model-openai-anthropic
- Axios, "China just erased America's AI lead" (17 July 2026) — https://www.axios.com/2026/07/17/china-ai-kimi-k3-open-source-anthropic-opus
- Yahoo/Investing.com, "Kimi K3 AI breakthrough: What Wall Street analysts say about China's OpenAI threat" — https://finance.yahoo.com/technology/ai/articles/kimi-k3-ai-breakthrough-wall-123003909.html
- Transformer News, "Open-source Kimi K3 model is no reason for China panic" — https://www.transformernews.ai/p/kimi-k3-is-no-reason-for-china-panic-export-controls-xi-jingping

Claims sourced here (as reported): Axios wrote that Kimi K3 "dazzling developers, jolting Silicon Valley and resetting the AI race overnight," that it "immediately vaulted into the top tier of global AI, beating Anthropic's Fable 5 and OpenAI's GPT-5.6 Sol in front-end coding tests," that it finished ahead of Opus 4.8 in broad text ranking "while costing 40% less," and that its "very existence puts pressure on the pricing power of U.S. labs, the enormous valuations built around their technological edge, and the case for spending hundreds of billions of dollars on ever-larger data centers." Wall-Street coverage characterized frontier reasoning convergence as "directionally negative for AI model lab terminal margins" and framed K3 as signaling "a hyper-competitive future where software intelligence becomes highly accessible, shifting financial power over to the platforms that distribute it and the enterprises that deploy it." (Some commentators, e.g. Transformer News, argue the result is less alarming than the headlines suggest.)

## Launch caveats

- Simon Willison (as above) — no public model card, license file, or downloadable weights at launch; the model can be token-heavy (one SVG test reportedly burned more than 16,000 output tokens).

## Standing countdowns (continuing threads from prior editions)

- Model Context Protocol blog, "The 2026-07-28 MCP Specification Release Candidate" — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- European Commission, "AI Act | Shaping Europe's digital future" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU Artificial Intelligence Act, "Implementation Timeline" — https://artificialintelligenceact.eu/implementation-timeline/
- beam.ai, "EU AI Act 2026: GPAI Enforcement & 3% Fines Begin" — https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines

Claims sourced here: The MCP 2026-07-28 specification (stateless core, Enterprise-Managed Authorization stable since 18 June, MCP Apps) goes final on 28 July 2026 (the MCP project's date). On 2 August 2026 the EU AI Act's enforcement and penalty powers over general-purpose AI (GPAI) providers become fully applicable, including fines of up to €15M or 3% of global annual turnover (Article 101), with obligations flowing down to deployers. The "9 days," "10 days" and "15 days" figures are simple counts from this edition's date (18 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own.

## Adoption context

- Gartner, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up From Less Than 5% in 2025" — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

Claims sourced here: Gartner projects 40% of enterprise applications will feature task-specific AI agents by end-2026 (up from less than 5% in 2025) and that more than 40% of agentic-AI projects will be cancelled by end-2027 due to governance, risk and unclear business value.

---

*Editorial lines marked as the radar's own (e.g. "When the precious metal becomes a commodity, the value migrates from the ingot to the airframe.") are the AI Tech Radar's framing and are not third-party quotes. The aluminum allegory — aluminum as the most abundant metal in Earth's crust yet a precious metal in the 19th century, the Napoleon III aluminum-cutlery legend, the ~6-pound aluminum apex of the Washington Monument (completed 1884, briefly displayed at Tiffany's), and the 1886 Hall-Héroult electrolytic smelting process and the ~99% price collapse that followed — is a well-worn historical illustration used allegorically, told approximately, and is not a sourced claim about AI. Kimi K3 benchmark figures are provisional and in several cases self-reported by Moonshot AI or drawn from early independent evaluators; they are marked "as reported" and should be treated as directional. Model names and version numbers (Kimi K3, Claude Fable 5, Claude Opus 4.8, GPT-5.6 Sol, GLM-5.2) reflect the products as described in the cited July 2026 coverage.*
