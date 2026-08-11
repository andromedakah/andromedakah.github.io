# Sources — AI Tech Radar, 11 August 2026 ("The Signet Ring")

Every claim in this edition traces to a public source below. Figures are attributed to the organization or outlet that published them. Lines explicitly marked as "the radar's framing" are editorial and are not attributed to any third party. Where a figure or characterization is reported via secondary coverage, it is marked "as reported." Note: several primary publisher pages were unreachable at compile time due to an outbound network policy; those items were verified by cross-referencing multiple reputable outlets and are flagged accordingly.

## The story — agents move from acting on the web to acting in your name, and identity becomes the control surface

### The trap — an agent wearing your identity (Google Gemini Spark + Chrome)

- Engadget, "Gemini Spark now has Chrome web-browsing capabilities" — https://www.engadget.com/2229209/gemini-spark-now-has-chrome-web-browsing-capabliities/
- Digital Trends, "Gemini Spark can now use Chrome logins and saved passwords to run errands on your behalf" — https://www.digitaltrends.com/computing/gemini-spark-can-now-use-your-chrome-logins-and-saved-passwords-run-errands-on-your-behalf/
- 9to5Google, "Gemini Spark can now use Chrome to auto browse, AI Pro access goes international" (30 Jul 2026) — https://9to5google.com/2026/07/30/gemini-spark-chrome-auto-browse/
- Dataconomy, "Google adds Chrome web browsing to Gemini Spark in US rollout" (4 Aug 2026) — https://dataconomy.com/2026/08/04/google-chrome-browsing-gemini-spark-us-rollout/
- Notebookcheck, "Google Gemini Spark now uses your saved Chrome passwords" — https://www.notebookcheck.net/Google-Gemini-Spark-now-uses-your-saved-Chrome-passwords.1357683.0.html
- AndroidPure, "Gemini Spark can now use your Chrome logins and saved passwords" — https://www.androidpure.com/gemini-spark-chrome-auto-browse/

Claims sourced here (as reported): On 30 July 2026, Google enabled Gemini Spark to operate a user's real desktop Chrome — using the accounts they are already signed into and the passwords saved in Chrome's password manager — to complete web errands on their behalf, rolling out in the US (desktop Chrome first), with an accompanying expansion of Google AI Pro to more than 160 additional countries. Google describes two browsing modes: a remote cloud browser that pauses whenever a site asks the user to sign in, and local Chrome, where (per Google's documentation) the agent "has access to all the same sites that you do, including sites you are signed into." Sensitive steps such as payments are handed back to the user, and the agent is meant to resist prompt injection. The "signet ring" allegory (a great house that hands its errand-runners the master's own ring until it learns to strike each one its own seal) is the radar's framing.

### The discipline — issuing each agent its own identity (Snowflake Cortex AI Gateway + Natoma)

- SiliconANGLE, "Snowflake debuts Cortex AI Gateway to govern and monitor enterprise AI agents" (28 Jul 2026) — https://siliconangle.com/2026/07/28/snowflake-debuts-cortex-ai-gateway-govern-monitor-enterprise-ai-agents/
- VentureBeat, "Snowflake launches Cortex AI Gateway to control AI agents and prevent runaway enterprise costs" — https://venturebeat.com/security/snowflake-launches-cortex-ai-gateway-to-control-ai-agents-and-prevent-runaway-enterprise-costs
- Snowflake blog, "Snowflake Launches Cortex AI Gateway and Advanced AI Security at Black Hat 2026" — https://www.snowflake.com/en/blog/enterprise-ai-security-agentic-mcp-governance/
- Snowflake press release, "Snowflake Advances the Trusted Agentic Enterprise Era with Unified Monitoring and Cost Management" (28 Jul 2026) — https://www.snowflake.com/en/news/press-releases/snowflake-advances-the-trusted-agentic-enterprise-era-with-unified-monitoring-and-cost-management/
- Forkast / Tech.Yahoo, "Snowflake's Cortex AI Gateway Signals MCP Gateways Are Crystallizing as Infrastructure" — https://forkast.news/snowflakes-cortex-ai-gateway-signals-mcp-gateways-are-crystallizing-as-infrastructure/
- Snowflake press release, "Snowflake Announces Intent to Acquire Natoma, Providing Secure Connectivity For The Agentic Enterprise" (May 2026) — https://www.snowflake.com/en/news/press-releases/snowflake-announces-intent-to-acquire-natoma-providing-secure-connectivity-for-the-agentic-enterprise/

Claims sourced here (as reported): On 28 July 2026, around Black Hat 2026, Snowflake launched its Cortex AI Gateway, a centralized control layer for enterprises to govern their AI agent fleets. It builds on Snowflake's May 2026 acquisition of Natoma — a 27-person startup whose centralized MCP gateway "enforces identity, policy, and audit at the tool-call level" — governing how first-party agents (Snowflake CoWork, CoCo) and third-party agents (Claude Code, Cursor, Amazon Bedrock, Azure AI Foundry, ChatGPT, LangChain, LlamaIndex, and others) access models, data, MCP servers and enterprise tools; it logs each tool call, query and action and attributes token counts to the specific agent, team and workload. The launch shipped with seven identity partners: 1Password, Aembit, Cyera, Linx Security, Okta, SailPoint and Saviynt. The Mayank Upadhyay quotation ("Agent interoperability only works when enterprises can trust how agents from different platforms access data, invoke tools and take action on behalf of users… The future of the agentic enterprise will not be built in closed agent ecosystems and Snowflake is the trusted control plane that enables secure enterprise work") is attributed to Snowflake's Chief Security and Trust Officer via this coverage.

### The gap — agent identity outpacing controls (surveys / OWASP)

- Akeyless, "Research Shows AI Agents Are Outpacing Identity Security" (2026 AI agent identity survey) — https://www.akeyless.io/blog/2026-ai-agent-identity-security-survey/
- Kiteworks, "Agentic AI Credential Security: Machine Identity Is the Next Breach Vector" — https://www.kiteworks.com/cybersecurity-risk-management/agentic-ai-machine-credentials-breach/
- Non-Human Identity Management Group, "Scoped credentials for AI agents cut identity and privilege abuse" — https://nhimg.org/articles/scoped-credentials-for-ai-agents-cut-identity-and-privilege-abuse/
- Security Boulevard, "AI Agent Identity Management: A 2026 CISO Playbook" — https://securityboulevard.com/2026/05/ai-agent-identity-management-a-2026-ciso-playbook/
- OWASP, "Top 10 for Agentic Applications" (identity and privilege abuse) — https://owasp.org/

Claims sourced here (as reported, approximate): Reported surveys put only about 19% of organizations classifying an AI agent as equivalent to a human insider, about 44% expecting malicious use of AI agents to increase data-theft risk, and about 80% already seeing AI agents act beyond their intended scope. The OWASP Top 10 for Agentic Applications names identity and privilege abuse a core agentic risk (agents inheriting permissions, misusing delegated credentials, or executing unauthorized actions when identity boundaries are weak). The core operational risks reported — over-broad scopes, token theft from agent runtime memory, prompt-injection coercion, and the audit-trail attribution problem of telling agent actions from user actions — frame this edition's argument. These figures are relayed from vendor and community survey coverage and are approximate.

## The buyer — enterprise AI is real money (Microsoft FY26 Q4)

- Microsoft, "Microsoft Cloud and AI strength fuels fourth-quarter results" (29 Jul 2026) — https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4/
- Microsoft Investor Relations, FY26 Q4 press release & webcast — https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast

Claims sourced here (as reported): In fiscal fourth-quarter 2026 results reported 29 July 2026, Microsoft said Microsoft 365 Copilot passed 30 million paid seats and Azure grew 43% year over year and passed $100 billion in annualized revenue. The Satya Nadella quotation ("We are advancing the frontier on the cost-to-outcome curve, ensuring every customer can turn tokens into business results") is relayed from Microsoft's official channels and press coverage.

## The regulatory backdrop — EU AI Act enforcement, still live

- European Commission, "Commission starts enforcing AI Act rules and new transparency requirements from 2 August" — https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- European Commission press release (IP/26/1714) — https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1714

Claims sourced here (as reported): The European Commission and national authorities began enforcing the AI Act on 2 August 2026, with GPAI oversight and transparency obligations, and penalties up to the higher of €15 million or 3% of worldwide annual turnover. The observation that an agent which cannot prove its identity or produce an audit trail of its data access is hard to defend under such regimes is relayed from agent-identity compliance coverage as reported.

## The engine — commodity models (standing context)

- LLM-Stats, "AI Updates (August 2026) — Latest AI Model Releases" — https://llm-stats.com/llm-updates
- OpenAI, "Advancing the price-performance frontier with GPT-5.6" — https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/
- Google Cloud, Gemini enterprise release notes — https://docs.cloud.google.com/gemini/enterprise/docs/release-notes

Claims sourced here (as reported): Claude Opus 5, Google Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 (MIT-licensed open weights) and Alibaba Qwen3.8-Max (open weights, frontier-parity claim) are relayed from model-tracker and vendor coverage as standing context — the rented, swappable "runner."

---

*Editorial lines marked as the radar's own (e.g. "The model is the runner — rented, swappable, cheaper every quarter, never your moat. The signet office is yours…") are the AI Tech Radar's framing and are not third-party quotes. The signet-ring allegory — a great house that hands its errand-runners the master's own ring until it learns to strike each one its own seal — is a common illustration used allegorically, told approximately, and is not a sourced claim about any specific company or product. Where a quotation or figure is attributed via secondary coverage rather than a primary release, it is marked "as reported." Product, firm and institution names (Google, Snowflake, Natoma, Okta, SailPoint, Saviynt, 1Password, Aembit, Cyera, Linx Security, Microsoft, Alibaba, DeepSeek, the European Commission, Anthropic, OpenAI, Moonshot) reflect the sources as described in the cited 2026 material. This edition's central datable developments in the window are Google's 30 July enabling of Gemini Spark to operate a user's real Chrome with their logins and saved passwords, and Snowflake's 28 July Cortex AI Gateway (on the Natoma acquisition) enforcing agent identity at the tool-call level — treated as the two roads at one fork: lend an agent your own identity, or issue it its own. It is set against continued model commoditization (Qwen3.8-Max and the open-weight field), strong enterprise-AI demand (Microsoft FY26 Q4) and live EU AI Act enforcement.*
