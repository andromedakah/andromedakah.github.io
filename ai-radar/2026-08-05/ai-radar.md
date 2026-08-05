# 🗓️ AI Tech Radar — The Dark Warehouse

**Wednesday, 5 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday the market and the regulator asked the enterprise for the same papers — the dossier of what its AI does, on whose data, under whose oversight. Today the industry answered the question nobody had asked out loud: **can the enterprise even see what it would have to document?** Three reports landed on the same theme within 24 hours, and the answer is no. **Snyk's 2026 State of Agentic AI Adoption (covered 5 August, across 3,044 enterprise environments and ~1.39M code repositories) finds the real AI attack surface is roughly three times what a model inventory shows — enterprises are blind to about two-thirds of their own AI estate, and the ratio held constant in every region.** **46.9% of AI-using organizations now run agentic architectures** (agents, MCP servers, or both), and the full-stack share **has nearly doubled since January.** **SAP's own writing** calls agent sprawl a board-level issue: **98% of companies have deployed or plan agents, but fewer than half have any inventory of them** (SAP LeanIX), while **Gartner** projects the average Fortune 500 will run **more than 150,000 agents by 2028 with only 13% confident in their governance today.** And **Gravitee's State of AI Agent Security 2026** names the gap in one line: **88% of organizations had a confirmed or suspected AI-agent security incident last year — while 82% of executives feel confident their policies protect them.** Read together, they describe one building: a lit shop floor (the model list the board discusses) and, behind it, a dark warehouse three times the size, filling faster than anyone counts. The board's question this morning: ***the dossier we were told to hold presumes we can see the estate — but if two-thirds of it is in the dark and doubling, what exactly are we documenting, defending, or insuring?***

---

## 1 · Executive Summary (90-second read)

Yesterday's edition ("The Two Windows") ended on the dossier — the provable record of what your AI does, which the market pays a premium for and the regulator now demands. Today three independent reports, all surfacing within a day, expose the precondition nobody costed: **you cannot document, govern, or defend an estate you cannot see — and the enterprise can see only about a third of its own AI.** The month's thesis (own and govern the layer around the commodity model) meets its hard floor: first, find the layer.

**The blind spot is measured, and it is two-thirds.** **Snyk's 2026 State of Agentic AI Adoption**, covered on **5 August** and drawn from **3,044 enterprise environments and roughly 1.39 million code repositories,** finds that the **full AI surface is about three times what a model inventory shows** — beyond the LLMs sit agent frameworks, **MCP servers,** retrieval systems, vector databases, datasets and supporting tools that no one is tracking. Most security programs, asked what AI they run, produce a **list of models and miss two-thirds of the picture.** The ratio "held constant across every region," so this is structural, not a local lapse. And it is accelerating: **46.9% of AI-using organizations now run agentic architectures** (agents, MCP servers, or both), more than half of them the full stack, a share that **has nearly doubled since Snyk's January 2026 report.**

**The sprawl is now a board problem, by the vendors' own admission.** **SAP** published a piece this month titled, plainly, *"AI Agent Sprawl: Why AI Governance Is Now a Board-Level Issue,"* and shipped an **AI Agent Hub** to discover and govern agents and MCP servers — because its **LeanIX Agentic AI Survey 2026** finds **98% of companies have deployed or plan to deploy agents, but fewer than half have any inventory of them.** **Gartner** puts a number on where this goes: the average **Fortune 500 enterprise will run more than 150,000 AI agents by 2028,** while **only 13% believe they have the right governance in place** today.

1. **The dossier presumes an inventory — and the inventory is two-thirds dark.** Snyk's three-to-one ratio means the Article 11 file, the six-month log, the data-sovereignty proof all rest on a map that omits most of the territory. You cannot write the manifest of a warehouse you have not lit.

2. **Confidence is inverted from control.** **Gravitee's State of AI Agent Security 2026:** **88% of organizations had a confirmed or suspected AI-agent incident in the past year,** yet **82% of executives feel confident their policies protect them;** only **14.4%** put every agent live with full security approval, only **21%** have runtime visibility, and roughly **48% of production agents run unsecured.** The estate **doubled in about four months** while coverage barely moved.

3. **The estate is growing fastest exactly where it is darkest.** Agents and MCP servers — the parts no one inventories — are the parts multiplying. Snyk's full-stack share nearly doubled since January; Gravitee's agent count doubled in a quarter; SAP and Gartner both frame the next 24 months as sprawl outrunning governance.

**Bottom line:** the market rewards a provable, governed AI layer and the regulator demands its dossier — but both assume you can *see* the layer, and today's data says two-thirds of it is unlit and growing. **Light the warehouse before you promise the manifest: run discovery across the whole AI surface — every agent, every MCP server, every dataset — assign an owner, and only then is the dossier a document rather than a hope. You cannot govern, defend, or sell what you cannot see.**

---

## 2 · Allegory of the Day — "The Dark Warehouse"

*Topic: On 5 August 2026, Snyk's 2026 State of Agentic AI Adoption (across 3,044 enterprise environments and ~1.39 million code repositories) reported that the real enterprise AI attack surface is roughly three times what a model inventory shows — organizations are blind to about two-thirds of their own AI estate, a ratio that held constant across every region — because beyond the models sit agent frameworks, MCP servers, retrieval systems, vector databases and datasets that go untracked; 46.9% of AI-using organizations now run agentic architectures, a full-stack share that has nearly doubled since January 2026. In the same window, SAP published "AI Agent Sprawl: Why AI Governance Is Now a Board-Level Issue" and launched an AI Agent Hub, its LeanIX Agentic AI Survey 2026 finding 98% of companies have deployed or plan AI agents but fewer than half have any inventory of them, while Gartner projects the average Fortune 500 will run more than 150,000 agents by 2028 with only 13% confident in their governance. Gravitee's State of AI Agent Security 2026 found 88% of organizations had a confirmed or suspected AI-agent security incident last year while 82% of executives feel confident their policies protect them; only 14.4% put all agents live with full security approval, only 21% have runtime visibility, and about 48% of production agents run unsecured, with the agent estate doubling in roughly four months. The lesson: the dossier the market rewards and the regulator demands presumes an inventory, and the enterprise can see only about a third of its own AI, so the first move is not to document but to discover — light the warehouse before you promise the manifest.*

Picture a prosperous merchant house with a handsome shop on the square. On the counter sits a neat ledger, and in it the owner has written every bolt of cloth and cask of wine displayed on the **lit shop floor.** When the board of the house asks whether the stock is in order, the owner opens that ledger and says yes, with real confidence — the shelves match the book, the book matches the shelves, and everything the eye can see is accounted for. This is a truthful ledger. It is also a small one, because the shop floor was never where the house kept most of its goods.

Behind the shop is a **warehouse three times the size,** and it is dark. Nobody planned it that way; it simply filled. Every night more crates arrive — an agent here, an MCP server there, a retrieval store, a vector database, a dataset copied for a project that shipped and was forgotten — and they are stacked in the black beyond the last lantern, because the shop floor had no more room and the back room asked no one's permission. The owner is not lying to the board; the owner **cannot see the warehouse,** and so reports on the only room that is lit. Ask the house what it holds and it recites the shop-floor ledger — and misses two-thirds of the building. Worse, the dark room is the one *growing:* the crates on the floor sit still, but the warehouse doubles while no one is counting.

Now recall who comes calling. The **thief** does not rob the lit counter under the shopkeeper's eye; the thief works the **unlit warehouse,** where no one will notice a missing crate for months — which is why, in this house, the strongroom was breached long before anyone believed it could be (88 in a hundred such houses were robbed last year, while 82 in a hundred owners told their boards the locks were sound). And the **assessor** — the one who came yesterday demanding the manifest of the whole building, not just the front counter — will not accept a shop-floor ledger as an account of the house. She will walk to the warehouse door, find it dark, and note that the merchant cannot say what is inside. **The lit ledger the owner was so proud of is not wrong; it is simply not an inventory of the house.** It is an inventory of the part of the house that was easy to see.

There is only one first move, and it is not to write a finer ledger. It is to **carry a lantern into the warehouse and count** — to walk every aisle, open every crate, name an owner for each, and light the room so it stays lit as new goods arrive. Only after the warehouse is lit does the ledger become a manifest, the manifest become a dossier, and the dossier become the thing the market pays for and the assessor accepts. A merchant who documents only the shop floor has not governed the house; he has governed the easy third of it, and left the thief and the assessor the other two-thirds in the dark.

**The moral:** the model list is the lit shop floor, and the board mistakes it for the business. The real estate — agents, MCP servers, retrieval stores, forgotten datasets — is the **dark warehouse, three times larger and doubling** where no one looks. You cannot insure, defend, sell, or *document* what you have never counted; the dossier the market rewards and the regulator demands is impossible until the room is lit. **Discovery comes before documentation. Light the warehouse before you promise the manifest.**

**The question it forces:** *When our board asks whether our AI is under control, are we opening the shop-floor ledger — the model list — and mistaking it for the house? If our real AI estate is three times what we can name, and the two-thirds we can't see is the part still growing, what is our lantern: who runs discovery across every agent, every MCP server, every dataset, assigns each an owner, and keeps the room lit — before the thief and the assessor find the dark warehouse for us?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **When we tell the board our AI is under control, are we reading the shop-floor ledger?** Snyk finds the real AI surface is ~3× the model list, and most security programs see only a third. **What is the honest ratio here — and who owns the lantern that lights the other two-thirds?**
- The perception gap is the danger: **82% of executives feel protected while 88% of organizations were breached through an agent** (Gravitee). **On what evidence do we believe we're the exception — a current inventory, or a confident memory?**
- Gartner: the average Fortune 500 will run **150,000+ agents by 2028; only 13% have the right governance now.** **Is discovery of every agent and MCP server a named, funded program with an owner — or a slide we agreed with and never staffed?**

### 🏦 Financial Services
- CNIL's first move demanded the **Article 11 dossier** for credit-scoring systems — but a dossier is impossible for an estate you can't see. **For every scoring, underwriting and fraud model, do we have the full component list (agents, MCP servers, retrieval stores, datasets), or only the model name a regulator would immediately look past?**
- Finance runs the most agents in production and the strictest audit. **Of our production agents, what share went live with full security approval — the sector-wide figure is 14.4% — and how many run today with no runtime visibility (only 21% have it) inside systems that touch customer money?**
- The estate doubles roughly every four months. **What is our re-inventory cadence — continuous discovery, or an annual spreadsheet already stale the week it's filed?**

### 🧬 Healthcare / Life Sciences
- Clinical and patient-facing AI is high-risk and audited, and it is exactly the kind of estate that sprawls quietly across research and care. **Have we lit the warehouse — every diagnostic agent, every retrieval store over patient data, every dataset copy — or are we documenting the lit third and calling it governance?**
- Roughly **48% of production agents run unsecured** (Gravitee). **For agents that read or act on patient data, can we prove — not assume — logging, oversight and access limits, or would a documentation request find the room dark?**

### 🏭 Manufacturing / Industrials
- Operational AI accretes as point tools on line-side and supply-chain systems — the classic dark warehouse. **Do we have one authoritative inventory of operational agents and MCP connectors, with an owner each, or a scatter of projects no one can enumerate?**
- Cheaper, better models keep arriving (DeepSeek V4-Flash-0731 last week). **When a team swaps an engine on a high-risk line, does our inventory update automatically — or does the crate go back into the dark the moment the model changes?**

### 🛒 Retail / Consumer
- Storefront agents that price, recommend or decide on customers multiply fast and are disclosure-bound (Article 50). **Can we list every consumer-facing agent and what data each touches — or is the customer-facing estate itself the part we can't see?**
- The market rewards provable trust; you cannot prove what you cannot count. **Are we running discovery as a standing capability, so the manifest the market pays for stays current as the warehouse fills nightly?**

### 🏛️ Public Sector / Regulated
- Citizen-facing AI carries the strictest accountability, and the AI Office can now enforce it across 27 states. **Is there a single, current inventory of every agent and MCP server acting on citizen data, each with a named owner — the exact thing 98% deploy and fewer than half can list?**
- Enforcement is case-by-case now (CNIL named 14 institutions, denied extensions). **Before a supervisor asks, could we produce a complete map of our AI estate this week — or would we, like most, hand over the lit third and hope?**

---

## 4 · Technical Deep-Dive — You Cannot Govern What You Cannot See

Read three reports landing in one day as a single finding: **the governance layer everyone is racing to build assumes a map that doesn't exist.** The month's discipline — own and govern the layer around the commodity model, hold the dossier — has a precondition it never priced: **discovery.** The estate is three parts: the cargo (commodity models, the lit shop floor everyone can name), the dark warehouse (the two-thirds no one inventories), and the lantern (the discovery capability that must come *before* the dossier).

- **The cargo — the lit shop floor (commodity models, cheaper each week).** Still a swappable menu: **Claude Opus 5** (24 Jul; #1, Intelligence Index 61 / Agentic Index 55.3, $5/$25), Google **Gemini 3.6 Flash** (21 Jul), **GPT-5.6 Sol**, **Kimi K3** open weights, and — as of **31 July** — **DeepSeek V4-Flash-0731** (MIT, open weights), beating its own flagship on nine benchmarks at no price change. This is the part every board can recite, because it is lit. It is also **not the estate.** Snyk's point is precise: ask an enterprise what AI it runs and it names the models — the shop floor — and misses the warehouse behind.
- **The dark warehouse — the two-thirds no one sees.** Beyond the models sit **agent frameworks, MCP servers, retrieval systems, vector databases, datasets and supporting tools,** and Snyk's assessments across **3,044 environments and ~1.39M repositories** put the **full surface at ~3× the model inventory** — enterprises blind to about **two-thirds** of it, the ratio constant across every region. This is where the estate is *growing:* **46.9%** now run agentic architectures, full-stack share **nearly doubled since January;** Gravitee's agent count **doubled in ~four months.** And it is where the danger concentrates — **88% had an agent incident** while **82% of executives feel safe,** only **14.4%** approved every agent, only **21%** have runtime visibility, **~48%** of production agents run unsecured. SAP names it a **board-level issue;** Gartner projects **150,000+ agents per Fortune 500 by 2028, 13% governed.** The dark room is the real one.
- **The lantern — discovery, the move that must come first.** You cannot write an Article 11 file, retain a six-month log (Article 26), disclose under Article 50, or prove data sovereignty for a system you cannot enumerate. So the first craft is **DISCOVER** (scan the whole surface — models, agents, MCP servers, retrieval stores, datasets — not the model list); then **OWN** (a named accountable owner per item, the gap behind SAP's "fewer than half have an inventory"); then **ILLUMINATE CONTINUOUSLY** (re-inventory on the cadence the estate doubles — roughly quarterly, not annually); only then **DOCUMENT** (the dossier of yesterday's edition becomes possible). Vendors are shipping the lanterns now — SAP's **AI Agent Hub,** Snyk's Evo discovery — precisely because the dossier is undeliverable without them.

The strategic core: **discovery is the precondition of every other control, and it is the one most enterprises skipped.** The comforting misread is "we have an AI policy and we know our models" — which is a ledger of the lit third. The market pays for a provable estate and the regulator demands its dossier; both are impossible while two-thirds of the estate is dark and doubling. After today's data, "we know which models we run" is not the answer to "is your AI governed"; ***"we can produce, today, a complete and current inventory of every model, agent, MCP server and dataset we run, each with an owner"*** is the answer — and it is the thing the dossier is written *from.*

```
        THE DARK WAREHOUSE — you cannot govern what you cannot see
        The model list is the lit shop floor. The estate is 3x larger, and dark.

   ┌─────────────────────────────────────────────────────────┐
   │  THE LIT SHOP FLOOR — the model list the board recites   │  💡 ~1/3 OF THE
   │  Opus 5 (#1, $5/$25) · Gemini 3.6 Flash · GPT-5.6 Sol ·  │     REAL ESTATE
   │  Kimi K3 · DeepSeek V4-Flash-0731 (MIT)                  │
   └───────────────────────────┬───────────────────────────────┘
                               │  ask "what AI do you run?" → you get this ↓
   ┌───────────────────────────▼───────────────────────────────┐
   │  THE DARK WAREHOUSE — ~2/3 unseen, and the part growing   │  🌑 SNYK: FULL
   │  agent frameworks · MCP servers · retrieval · vector DBs  │     SURFACE ≈ 3x
   │  · datasets · forgotten copies                            │     MODEL LIST
   │  46.9% run agentic · full-stack ~2x since Jan             │
   │  88% breached vs 82% feel safe · 14.4% approved · 21% seen│
   │  ~48% of prod agents unsecured · estate 2x in ~4 months   │
   │  Gartner: 150,000+ agents/F500 by 2028 · 13% governed     │
   └───────────────────────────┬───────────────────────────────┘
                               │  light it before you promise the manifest ↓
   ┌───────────────────────────▼───────────────────────────────┐
   │  THE LANTERN — discovery, the move that comes first        │
   │  DISCOVER (whole surface, not the model list) · OWN (name  │
   │  an owner each) · ILLUMINATE CONTINUOUSLY (re-inventory as │
   │  it doubles) · then DOCUMENT (the dossier becomes possible)│
   └───────────────────────────────────────────────────────────┘

   TRAP: report the lit ledger as the house → thief & assessor work the dark 2/3.
   WIN : light the warehouse first → the dossier is a document, not a hope.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — a lit ledger, a dark house | The discipline — light the warehouse first |
|---|---|
| Report the model list as "our AI estate" | Discover the whole surface — agents, MCP servers, retrieval, datasets |
| Feel protected because a policy exists (82% do) | Assume breached until proven seen (88% were) |
| Inventory once a year in a spreadsheet | Re-inventory on the cadence it doubles (~quarterly) |
| Let agents ship without an owner | Name an accountable owner per item (fewer than half do) |
| Write the dossier from the model list | Write the dossier from a complete, current inventory |

### Why discovery is the precondition, not a step you can defer

Every control this month presumes visibility. The Article 11 file, the six-month log, Article 50 disclosure, the data-sovereignty proof the market pays a premium for — each is *written from an inventory,* and Snyk's three-to-one ratio says the inventory most enterprises hold covers a third of the estate. You cannot log a crossing you never knew happened, disclose an agent you cannot list, or prove sovereignty over data an untracked retrieval store is quietly reading. The dossier is not the first move; **the lantern is.** Skip it and every downstream control inherits the same two-thirds blind spot — a beautifully written manifest of the shop floor, and a dark warehouse behind it where the thief and the assessor both do their work.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine, 28 Jul the mailroom, 29 Jul the pilot plant, 30 Jul the commonplace book, 31 Jul the last mile, 1 Aug the tide table, 2 Aug the loose cannon, 3 Aug the customs house, 4 Aug the two windows). Yesterday the two windows demanded the dossier; today three reports show the dossier is written over a warehouse that is two-thirds dark. On legacy estates the sprawl is worst, because agents and MCP servers were bolted onto systems no one has fully mapped in years. The retrofit is unglamorous and first: **run discovery across the entire AI surface** — not the model list, but every agent, MCP server, retrieval store, vector database and dataset — **assign an owner to each,** stand it up as a **continuous** capability (the estate doubles in a quarter, so an annual scan is a stale scan), and *then* write the Article 11 file, wire the six-month logging and Article 50 disclosure, and prove sovereignty. Do discovery before documentation, because a dossier over a dark warehouse is a confident ledger of the wrong room.

**The clean mental model:** *The model list is the lit shop floor, and the board mistakes it for the house. The real estate — agents, MCP servers, retrieval stores, forgotten datasets — is a dark warehouse three times larger and doubling, and it is exactly where the thief and the assessor go. You cannot govern, defend, sell, or document what you cannot see. Carry a lantern into the warehouse and count — discovery before documentation — because the dossier the market rewards and the regulator demands is impossible until the room is lit.*

### Watch list this week
- **The measured blind spot — Snyk 2026 State of Agentic AI Adoption (5 Aug).** Across **3,044 environments** and **~1.39M repositories:** real AI surface **≈ 3× the model inventory** (blind to ~**two-thirds**), ratio constant across regions; **46.9%** run agentic architectures; full-stack share **nearly doubled since January.** Quote — Gabriel Brolo Tobar, Yalo: *"As AI-driven development accelerates, human oversight alone simply cannot keep pace."*
- **The perception gap — Gravitee State of AI Agent Security 2026.** **88%** had a confirmed/suspected agent incident last year vs **82%** of executives feeling protected; **14.4%** approved every agent; **21%** have runtime visibility; **~48%** of production agents unsecured; estate **doubled in ~4 months.**
- **The board-level framing — SAP + Gartner.** SAP: *"AI Agent Sprawl: Why AI Governance Is Now a Board-Level Issue,"* plus an **AI Agent Hub;** LeanIX survey: **98%** deploy/plan agents, **fewer than half** have an inventory. Gartner: **150,000+ agents per Fortune 500 by 2028; 13%** governed.
- **The regulatory backdrop — still live.** EU AI Act enforcement running since **2 Aug;** CNIL's **4 Aug** action (14 banks, credit scoring, **Article 11** documentation, **3 extensions denied**); **€15M or 3%;** deployer logs **≥6 months** (Article 26). The dossier is demanded; the inventory it needs is two-thirds dark.
- **The cargo, for context.** Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 — the lit shop floor. And OpenAI now books **>40% of revenue from enterprise,** on track to consumer parity by year-end — the demand filling the warehouse.

---

## 5 · Quotes That Catch the Eye

> As AI-driven development accelerates, human oversight alone simply cannot keep pace.
> — **Gabriel Brolo Tobar**, Senior Security Engineer, Yalo, in Snyk's 2026 State of Agentic AI Adoption, 5 August 2026 (as reported)

> The full AI surface is roughly three times what a model inventory shows — most security programs see only about a third of what their organization is actually running.
> — **On Snyk's 2026 State of Agentic AI Adoption**, across 3,044 environments and ~1.39M repositories, 5 August 2026 (as reported)

> 88% of organizations reported a confirmed or suspected AI-agent security incident in the past year — while 82% of executives feel confident their existing policies protect them.
> — **On Gravitee's State of AI Agent Security 2026**, on the gap between confidence and control, 2026 (as reported)

> AI agent sprawl is why AI governance is now a board-level issue.
> — **SAP News Center**, headline of its 2026 piece accompanying the launch of the AI Agent Hub (as reported)

> "The model list is the lit shop floor, and the board mistakes it for the house. The real estate is a dark warehouse three times larger — and it is exactly where the thief and the assessor go. Light the warehouse before you promise the manifest."
> — *the radar, on discovery before documentation*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Real AI surface vs. model inventory | **≈ 3× (blind to ~two-thirds)** | Snyk 2026 State of Agentic AI Adoption (as reported) |
| Snyk study base | **3,044 environments · ~1.39M repositories** | Snyk / Help Net Security / vmblog (as reported) |
| Organizations running agentic architectures | **46.9%** (full-stack share ~2× since Jan) | Snyk 2026 (as reported) |
| Orgs with an AI-agent incident last year | **88%** | Gravitee State of AI Agent Security 2026 (as reported) |
| Executives who feel their policies protect them | **82%** | Gravitee 2026 (as reported) |
| Agents put live with full security approval | **14.4%** | Gravitee 2026 (as reported) |
| Orgs with runtime visibility into agents | **21%** (≈48% of prod agents unsecured) | Gravitee 2026 (as reported) |
| Enterprise agent estate — growth | **Doubled in ~4 months** | Gravitee 2026 (as reported) |
| Companies deploying/planning agents vs. with an inventory | **98% deploy · <50% have an inventory** | SAP LeanIX Agentic AI Survey 2026 (as reported) |
| Fortune 500 agents by 2028 / with right governance | **150,000+ · 13%** | Gartner (as reported) |
| EU AI Act enforcement — status | **Live since 2 Aug; CNIL 4 Aug: 14 banks, Art. 11, 3 extensions denied** | European Commission / regulatory coverage (as reported) |
| Penalty ceiling (Art. 99) / incorrect information | **€15M or 3% · €7.5M or 1.5%** | European Commission |
| High-risk deployer log retention | **≥ 6 months (Article 26)** | EU AI Act Art. 26 (as reported) |
| OpenAI enterprise share of revenue | **>40%** (parity with consumer by year-end) | OpenAI / Yahoo Finance (as reported) |
| The cargo (context) | **Opus 5 · Gemini 3.6 Flash · GPT-5.6 Sol · Kimi K3 · DeepSeek V4-Flash-0731 (MIT)** | Vendor / model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Light the warehouse — run discovery across the whole AI surface, not the model list.** Today's data says your real estate is roughly three times what you can name and two-thirds of it is dark. Stand up a discovery scan that finds every model, agent, MCP server, retrieval store, vector database and dataset — the parts Snyk shows go untracked — and produce one authoritative inventory. Treat "could we hand a regulator a complete, current map of our AI this week?" as pass/fail. The dossier the market rewards and CNIL demands is written *from* this inventory; without it, you are documenting the shop floor and calling it the house.

2. **Close the confidence gap — assume breached until proven seen.** 82% of executives feel protected while 88% of organizations were breached through an agent. Replace confidence with evidence: for every agent, record whether it went live with security approval (only 14.4% do), whether you have runtime visibility (only 21% do), and who owns it (fewer than half can say). Report the *ratio of the estate you can actually see* to the board as a standing metric — not the model count, which is the lit third and the reassuring lie.

3. **Make discovery continuous and model-neutral — the warehouse fills nightly.** The estate doubles in roughly four months, so an annual inventory is stale before it's filed. Build discovery and ownership as a standing capability that survives an engine swap — so adding DeepSeek V4-Flash-0731 or swapping Opus 5 for Gemini never quietly returns a crate to the dark, and every new agent or MCP server lands on the inventory with an owner the day it ships. Own the lantern, keep the room lit, and *then* the whole month's discipline — the dossier, the log, the disclosure, the sovereignty proof — finally rests on ground you can see.

---

*AI Tech Radar · generated 5 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The Snyk figures (the 2026 State of Agentic AI Adoption drawing on roughly 3,044 enterprise environments and about 1.39 million code repositories; the finding that the full AI attack surface is approximately three times what a model inventory shows, leaving organizations blind to roughly two-thirds of their AI estate, with the ratio reported constant across every region measured; that 46.9% of AI-using organizations run agentic architectures built on AI agents, MCP servers, or both, with the full-stack share nearly doubled since Snyk's January 2026 report; and the quotation attributed to Gabriel Brolo Tobar, Senior Security Engineer at Yalo, "As AI-driven development accelerates, human oversight alone simply cannot keep pace") are relayed from Snyk's report and 5 August 2026 coverage in Help Net Security, vmblog and IT Pro as reported. The Gravitee figures (the State of AI Agent Security 2026 finding that 88% of organizations reported a confirmed or suspected AI-agent security incident in the past year while 82% of executives feel confident their existing policies protect them; that only 14.4% of organizations put all agents live with full security approval, only 21% have runtime visibility, roughly 48% of production agents run unsecured, and the enterprise agent estate doubled in about four months) are relayed from Gravitee's report and its 2026 coverage as reported. The SAP figures (the SAP News Center piece "AI Agent Sprawl: Why AI Governance Is Now a Board-Level Issue," the launch of the SAP LeanIX AI Agent Hub, and the SAP LeanIX Agentic AI Survey 2026 finding that 98% of companies have deployed or plan to deploy AI agents while fewer than half have an inventory of them) and the Gartner projections (an average of more than 150,000 AI agents per Fortune 500 enterprise by 2028, with only 13% of organizations confident they have the right governance) are relayed from August 2026 coverage as reported. The EU AI Act facts (enforcement live from 2 August 2026; CNIL's 4 August formal information requests to 14 financial institutions running credit-scoring algorithms, demanding the Article 11 technical documentation, with three extension requests denied; the penalty ceiling of the higher of €15 million or 3% of worldwide annual turnover under Article 99, and €7.5 million or 1.5% for supplying incorrect information; the deployer log-retention duty of at least six months under Article 26) are relayed from the European Commission and August 2026 regulatory coverage as reported; the CNIL specifics rest on secondary coverage. The OpenAI figure (enterprise now more than 40% of revenue, on track to reach parity with consumer by the end of 2026) is relayed from OpenAI and Yahoo Finance coverage as reported. The model details (Claude Opus 5 released 24 July 2026 and ranked first with an Intelligence Index of 61 and Agentic Index of 55.3 at $5/$25; Gemini 3.6 Flash released 21 July 2026; GPT-5.6 Sol; Kimi K3 open weights; DeepSeek V4-Flash-0731 released 31 July 2026 under an MIT license) are relayed from model-tracker and vendor coverage as reported. The dark-warehouse allegory — a merchant house whose lit shop-floor ledger accounts for only a third of a building whose dark back warehouse holds three times as much and grows fastest — is the radar's own illustration and is not a sourced claim about any specific company.*
