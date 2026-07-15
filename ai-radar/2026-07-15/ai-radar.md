# 🛰️ AI Tech Radar — The Gauge War

**Wednesday, 15 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar warned you to *govern the goal, not the gauge* — to stop mistaking the metric for the mission. Today the word "gauge" changes meaning, and the warning gets bigger. The fight this week is not over how to *measure* an agent; it is over the **track width the whole industry runs on**. On the strength of a report from *The Information* — "Google and Microsoft Team Up to Beat Back Anthropic and OpenAI" — the enterprise incumbents have made their move in the standards war for the agent-tooling layer. **A bloc of Google, Microsoft, Salesforce, ServiceNow, Snowflake, Databricks, GitHub, Nvidia, Cisco and Hugging Face is rallying behind ARD — Agentic Resource Discovery — the "phone book" that decides which tools an agent can even find**, and it sits directly above the connection layer that Anthropic's MCP already owns as the de facto default (~97M monthly SDK downloads; MCP-backed agents in production at 78% of enterprise AI teams, as reported). Notably absent from ARD's backer list: **Anthropic and OpenAI.** This is the 19th-century railway gauge war with GPUs — and the board question is the one every rail baron eventually faced: ***if the standard our whole agent estate is laid on loses the war in twelve months, how much track do we have to relay — and do we own the interchange that would let our agents keep running regardless of who wins?***

---

## 1 · Executive Summary (90-second read)

The commoditization thesis this radar has argued for three weeks — *own and govern the layer around the model, because the model is a commodity* — just found its clearest battleground yet: **the standard that connects agents to your tools.** This week, per *The Information*, the enterprise-software incumbents stopped competing model-by-model and started fighting standards-by-standard. The vehicle is **ARD (Agentic Resource Discovery)**, an open specification — v0.9 draft, Apache-2.0 — for how an agent *discovers* which tools, MCP servers, skills and other agents exist on a network before it connects to them. Publishers post a machine-readable `ai-catalog.json` at `/.well-known/ai-catalog.json`; registries crawl and index those catalogs; agents query them at runtime. **The backer list reads like an anti-frontier coalition: Google, Microsoft, Salesforce, ServiceNow, Snowflake, Databricks, GitHub, Nvidia, Cisco, GoDaddy, Hugging Face — and neither Anthropic nor OpenAI.**

1. **The battle moved up a layer — from the model to the plumbing.** Anthropic's **MCP** won the *connection* layer (how an agent talks to a tool) and became the de facto default in ~18 months. The incumbents are not trying to beat MCP head-on; they are contesting the layer *above* it — **discovery** (how an agent finds tools in the first place) — with ARD, and the layer beside it — **agent-to-agent** — with Google's A2A (150 organizations in production, now under the Linux Foundation). Whoever runs the registry decides which vendors an agent can surface. That is the switchyard, not the track.

2. **This reaches you as lock-in risk, not a spec-sheet detail.** Every enterprise now runs agents on *someone's* stack. GitHub has already shipped **agent finder** — built on ARD, live on all Copilot plans — so Copilot discovers and calls MCP servers, skills and tools at runtime from any catalog you point it at. Convenient, and quietly load-bearing: your agents' reach is now defined by a registry someone else may control. Bet the whole estate on one company's gauge and you inherit its fate in a war a bloc you're not in is deciding.

3. **Adoption is racing ahead of the standard settling.** Gartner still expects **40% of enterprise apps to embed task-specific agents by end-2026** (from <5% in 2025), and Salesforce's Agentforce alone hit **$800M ARR, up 169% YoY** — even as **56% of CEOs report no significant financial benefit from AI yet** (PwC 2026) and Gartner projects **>40% of agentic-AI projects cancelled by end-2027** on governance and ROI. You are laying track fast, on a gauge that is still being fought over.

**Bottom line:** in a gauge war the prize is never the best gauge — it is the junction everyone must pass through. The move that survives it is not to pick the winner; it is to **own the interchange**: your own registry and allow-list, and a model- and standard-neutral abstraction, so that whoever wins ARD-vs-MCP-vs-A2A, your agents keep running. Own the interchange, not the track.

---

## 2 · Allegory of the Day — "The Gauge War"

*Topic: This week the enterprise incumbents (Google, Microsoft, Salesforce, ServiceNow, Snowflake, Databricks, GitHub, Nvidia, Cisco, Hugging Face) rallied behind ARD — Agentic Resource Discovery, the discovery layer for AI agents — in a standards battle framed by* The Information *as a move to "beat back" Anthropic and OpenAI, whose MCP is the de facto connection standard. The lesson for the enterprise: standards wars are won by coalitions, not by the best design, and the safe move is not to guess the winner but to own the interchange that speaks every gauge.*

In the 19th century the railways exploded across Britain and America — and every company laid its own track width. Stephenson's lines ran on 4 feet 8½ inches; Brunel's Great Western ran on a broad 7-foot gauge that, most engineers agreed, rode faster and smoother. It did not matter. A train built for one gauge could not run on another's rails. At every **break-of-gauge** town, where one company's track met another's, every passenger and every crate of freight had to be unloaded from one train and reloaded onto the next — a tax in time, money and breakage paid at every boundary. The nation's commerce stalled at the seams.

The fight that followed was not about which gauge was *best.* It was about which gauge everyone would *agree on* — and the companies with the most miles of track already laid banded together to make **their** gauge the standard. Because once the country's rails all matched their yards, every train in the land, no matter whose, terminated at **their** stations, bought coal at **their** depots, and paid tolls on **their** junctions. Brunel's superior broad gauge, with fewer miles behind it, was voted out of existence. The best design lost. The biggest coalition won.

That is the week's news with the serial numbers filed off. The agent-tooling layer is the rail network. **MCP is the gauge Anthropic laid first,** and most of the track now uses it. **ARD is the switchyard the incumbents have just banded together to control** — the discovery layer that decides which tools a train can even find — and the coalition is precisely the set of firms with the most track already in the ground: Google, Microsoft, Salesforce, ServiceNow, Snowflake, GitHub, Nvidia, Cisco. The two firms *not* invited to set the gauge are the two whose model business the coalition would most like to route around. This is not mainly a technical disagreement. It is a fight over whose yards the tracks lead to.

**The moral:** in a gauge war, the prize is never the best gauge — it is the junction everyone must pass through, and the tolls collected there. If you relay your entire estate to one company's gauge, you have handed your fate to whoever wins a war you are not a combatant in. The rail barons who survived the gauge wars intact were the ones who **owned the interchange** — the break-of-gauge station that could handle any train, transfer any load, and keep freight moving no matter which standard prevailed. You cannot pick the winner of a standards war in advance. You can build the junction that doesn't care who wins.

**The question it forces:** *If the agent-tooling standard our estate is built on lost the gauge war within twelve months, how much of our track would we have to relay — and do we own an interchange layer (our own registry, our own allow-list, a model-neutral abstraction) that would let our agents keep running regardless of who wins?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- The incumbents just formed a bloc around **ARD** to "beat back" the frontier labs whose **MCP** we probably already depend on. **Which gauge is our agent estate actually laid on today** — and if it lost the standards war, what would relaying the network cost us in quarters, not weeks?
- GitHub's **agent finder** already lets Copilot discover and call tools at runtime from a registry. **Do we run our own registry and allow-list** — deciding what our agents can find and invoke — or are we letting a vendor's catalog define our agents' reach?
- **56% of CEOs report no significant financial benefit from AI yet** (PwC 2026) even as we spend to keep up. **Are we investing in the interchange we own** — the neutral layer that survives a standards war — or in more track on a gauge someone else controls?

### 🏦 Financial Services
- Model risk and third-party risk management already require you to know your dependencies. **Can we produce a dependency map of every agent standard, registry and connector our trading, fraud and advice agents rely on** — and name the single points of failure if one loses the war?
- Runtime discovery means an agent can find and call a tool no one hardcoded or vetted. **Have we constrained agent discovery to an approved internal registry**, so a customer-facing agent can never reach an unvetted service mid-transaction?

### 🧬 Healthcare / Life Sciences
- A patient-facing or clinical-decision agent that dynamically discovers tools at runtime is a validation and safety problem. **Can we prove our clinical agents only ever discover and invoke resources from a controlled, versioned catalog** — not the open web's registries?
- If the standard our clinical stack is built on is deprecated by the winning coalition, **do we have a validated, standard-neutral fallback**, or a single regulatory-and-safety point of failure?

### 🏭 Manufacturing / Industrials
- Operational agents on the plant floor are landing faster than anyone is cataloging them. **Do we know which standard each embedded agent speaks** — and could an "optimized" agent discover and call a tool outside our control envelope?
- CE-marked and embedded systems carry long lifecycles. **Have we avoided hard-wiring a decade-long product line to one agent gauge** that may not survive the war?

### 🛒 Retail / Consumer
- Recommendation, pricing and service agents multiply weekly. **Who owns the registry that decides what those agents can discover**, and can we show that customer data never flows to a tool an agent found on an uncontrolled catalog?
- If our commerce agents run on a vendor's discovery layer, **what happens to conversion the day that vendor changes its catalog terms** — and do we have an interchange that would let us switch gauges without re-platforming?

### 🏛️ Public Sector / Regulated
- Public-service agents demand auditability and sovereignty. **Can we guarantee our agents discover and invoke only resources from a registry we operate and audit** — not a foreign-controlled switchyard?
- The EU AI Act's logging and human-oversight duties become enforceable for GPAI in **18 days (2 August 2026)**. **Does our agent-discovery layer produce the audit trail** — what was found, chosen and called, and why — that an inspector could follow end to end?

---

## 4 · Technical Deep-Dive — The Layers of the Gauge War

The agent stack is not one standard; it is a **layered rail network**, and this week's news is a move on a specific layer. Read the stack from the bottom up and the strategy becomes obvious.

- **Connection layer — MCP (Anthropic).** *How an agent talks to a tool.* Open-sourced November 2024; the de facto default in ~18 months. As reported: ~97M monthly SDK downloads, MCP-backed agents in production at 78% of enterprise AI teams, ~28% of Fortune 500 running MCP servers. This is the gauge already in the ground — and it is Anthropic's.
- **Agent-to-agent layer — A2A (Google).** *How agents talk to each other.* ~150 organizations in production; governance handed to the **Linux Foundation's Agentic AI Foundation (AAIF)**, which also houses MCP, Block's *goose* and OpenAI's *AGENTS.md*. Neutral governance on paper; a Google-origin gauge in practice.
- **Discovery layer — ARD (the new front).** *How an agent finds which tools exist at all.* A v0.9 draft (Apache-2.0), announced 17 June 2026, backed by Google, Microsoft, GitHub, GoDaddy, Hugging Face, Nvidia, Salesforce, ServiceNow, Databricks, Snowflake and Cisco. Publishers host `ai-catalog.json` at `/.well-known/ai-catalog.json`; registries crawl and index the catalogs; agents issue a runtime search (`POST /search`) to find resources by task, then connect — typically over MCP.

Here is the strategic core, and why *The Information* frames it as a move against the frontier labs: **MCP won the connection layer for Anthropic, so the incumbents are not attacking it — they are wrapping it.** Whoever controls the *discovery* layer controls which servers, tools and agents get surfaced to every agent at runtime — and therefore which vendors get used and which get buried. Own the switchyard and you route the traffic, whoever laid the track. That is why the coalition around ARD is exactly the roster of firms with the most enterprise "track" already down, and why the two absentees are the two whose gauge the coalition would like to route around.

```
        THE GAUGE WAR  —  the standards battle for the agent-tooling layer
        who sets the gauge — and whose yards the tracks lead to

   ┌──────────────────────────────────────────┐   ┌───────────────────────────┐
   │ DISCOVERY — ARD          (the new front)  │   │  THE INTERCHANGE YOU OWN  │
   │ how an agent FINDS tools                   │   │                           │
   │ ai-catalog.json · registries · POST/search │   │  your own registry +      │
   │ Google·MS·Salesforce·GitHub·Nvidia·Cisco   │   │  allow-list, and a model- │
   ├──────────────────────────────────────────┤   │  and standard-neutral     │
   │ CONNECTION — MCP     (de facto default)    │   │  abstraction.             │
   │ how an agent TALKS to a tool               │   │                           │
   │ Anthropic · ~97M downloads/mo              │   │  Speaks every gauge.      │
   ├──────────────────────────────────────────┤   │  Switch on demand.        │
   │ AGENT-TO-AGENT — A2A   (150 orgs · LF)     │   │  Never stranded by a war  │
   │ how agents TALK to each other              │   │  a bloc you're not in     │
   │ Google · Linux Foundation (AAIF)           │   │  is deciding.             │
   └──────────────────────────────────────────┘   └───────────────────────────┘

   TRAP: bet the estate on one gauge → relay the whole network if it loses.
   WIN : own the interchange → your agents run whoever wins the gauge war.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — bet the estate on one gauge | The discipline — own the interchange |
|---|---|
| Agents wired directly to one vendor's connectors and catalog | A registry and allow-list you operate, deciding what agents can discover and call |
| Discovery delegated to a vendor's registry you don't control | Runtime discovery constrained to your catalog — agents surface only what you permit |
| Standard hard-coded into products with multi-year lifecycles | A model- and standard-neutral abstraction between your agents and the gauge |
| "MCP won, so we're safe" / "the incumbents will win, so switch" | Assume neither — build the junction that keeps running whoever wins |
| No inventory of which standard each agent speaks | A dependency map: every agent, its standard, its registry, its single points of failure |

### Why runtime discovery is also a governance event

Dynamic discovery is genuinely useful — GitHub's agent finder means you configure *policies* (which registries to trust) instead of hand-wiring every tool. But it inverts the old safety model: instead of a human vetting a fixed tool list, an agent **finds and calls tools at runtime** based on the task. GitHub's own framing is the right instinct — *"agent finder only ever surfaces what your enterprise permits."* That is the whole game. If discovery is constrained to a registry you run, dynamic discovery is a productivity win and an audit source. If it is delegated to an open, vendor-controlled catalog, you have agents reaching services nobody inventoried — the exact inventory-and-oversight gap the EU AI Act starts fining for GPAI in **18 days (2 August 2026)**.

### How it lands on legacy estates

This is the same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the spend meter, 7 Jul the model-neutral router, 8 Jul the MCP control plane, 9 Jul the deployment-labor market, 10 Jul the vanishing interface, 11 Jul the unattended night shift, 12 Jul the moat with no walls, 13 Jul govern the goal not the gauge, 14 Jul the learner's permit). The standards war makes the router thesis literal: the abstraction layer you own is your **interchange**. On legacy estates the danger is silent lock-in — agents hard-wired to whatever gauge the vendor shipped, with no map of the dependency and no switch. The retrofit is the same discipline as the 7 July router, extended one layer up: **stand up your own registry, put an allow-list in front of discovery, and route agents through a neutral abstraction** so a standards outcome you don't control never strands a live workflow.

**The clean mental model:** *A standards war is won by the biggest coalition, not the best design — so don't bet the estate on guessing the winner. Own the interchange: your registry, your allow-list, a neutral abstraction. Then whoever wins ARD-vs-MCP-vs-A2A, your trains keep running.*

### Watch list this week
- **ARD (Agentic Resource Discovery)** — v0.9 draft, Apache-2.0, announced 17 Jun 2026; the discovery layer above MCP. Backers: Google, Microsoft, GitHub, GoDaddy, Hugging Face, Nvidia, Salesforce, ServiceNow, Databricks, Snowflake, Cisco. Anthropic and OpenAI absent. Mechanism: `ai-catalog.json` at `/.well-known/`, crawling registries, runtime `POST /search`.
- **The Information framing (July 2026)** — "Google and Microsoft Team Up to Beat Back Anthropic and OpenAI"; incumbents using standards battles to encircle the frontier labs on the agent-tooling layer (as reported).
- **GitHub agent finder** — built on ARD, live on all Copilot plans; Copilot discovers and calls MCP servers, skills and tools at runtime from catalogs you point it at; enterprise managed settings define what agents may discover.
- **MCP position** — de facto default in ~18 months; ~97M monthly SDK downloads; MCP-backed agents in production at 78% of enterprise AI teams; ~28% of Fortune 500 running MCP servers (as reported).
- **A2A / AAIF** — Google's Agent2Agent at ~150 orgs in production, under the Linux Foundation's Agentic AI Foundation, which also houses MCP, Block's *goose* and OpenAI's *AGENTS.md*.
- **Adoption vs. settling** — Gartner: 40% of enterprise apps embed agents by end-2026 (from <5%), >40% of agentic projects cancelled by end-2027; Salesforce Agentforce $800M ARR, +169% YoY; 56% of CEOs report no significant AI benefit yet (PwC 2026).
- **Secondary thread** — EU AI Act GPAI enforcement becomes applicable **2 Aug 2026 (18 days)**; €15M or 3% of global turnover; runtime discovery is now part of your inventory-and-oversight obligation.

---

## 5 · Quotes That Catch the Eye

> "Google and Microsoft Team Up to Beat Back Anthropic and OpenAI" — traditional tech giants using standards battles to encircle the frontier labs on the agent-tooling layer.
> — **The Information**, on the enterprise standards war, July 2026 (as reported)

> "Agent finder only ever surfaces what your enterprise permits." — GitHub Copilot's runtime discovery, built on the open ARD specification, is governed by the same managed settings that govern Copilot.
> — **GitHub Changelog**, on agent finder / ARD (as reported)

> In roughly 18 months, Anthropic's Model Context Protocol quietly became the default way agents connect to enterprise tools — ~97M monthly SDK downloads, and MCP-backed agents in production at 78% of enterprise AI teams.
> — **Industry coverage of MCP adoption**, July 2026 (as reported)

> **56% of CEOs report no significant financial benefit from AI to date; only one in eight (12%) report both cost and revenue gains.**
> — **PwC 29th Global CEO Survey, 2026** (n=4,454 across 95 countries)

> "In a gauge war the prize isn't the best gauge — it's the junction everyone must pass through. Don't bet the estate on the winner; own the interchange."
> — *the radar, on the standards war*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| ARD (Agentic Resource Discovery) spec announced | **17 Jun 2026 (v0.9 draft)** | Google Developers Blog / AgenticResourceDiscovery.org |
| Companies backing ARD (Anthropic & OpenAI absent) | **11** (Google, MS, Salesforce, ServiceNow, Snowflake, Databricks, GitHub, Nvidia, Cisco, GoDaddy, Hugging Face) | ARD spec / coverage (as reported) |
| MCP monthly SDK downloads | **~97M** | Industry coverage (as reported) |
| Enterprise AI teams with MCP-backed agents in production | **78%** | Industry coverage (as reported) |
| Fortune 500 running MCP servers | **~28%** | Industry coverage (as reported) |
| Time for MCP to become the de facto default | **~18 months** | Industry coverage (as reported) |
| Organizations running Google's A2A in production | **~150** | Linux Foundation / coverage (as reported) |
| Enterprise apps embedding task-specific agents by end-2026 | **40%** (from <5% in 2025) | Gartner |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |
| Salesforce Agentforce ARR (Q4 FY2026) | **$800M, +169% YoY** | Salesforce (FY26 Q4 results) |
| CEOs reporting no significant financial benefit from AI yet | **56%** | PwC 29th Global CEO Survey 2026 |
| CEOs reporting both cost and revenue benefits from AI | **12%** (one in eight) | PwC 2026 |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (18 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Draw the gauge map — which standard is every agent actually laid on?** You cannot survive a standards war you can't see. Inventory every production and shadow agent and record, for each, the connection standard (MCP?), the discovery mechanism (a vendor registry? none?), the agent-to-agent protocol (A2A?), and the single point of failure if that gauge is deprecated. This is the same inventory the EU AI Act will demand in 18 days — one artifact, two payoffs.

2. **Own the interchange — stand up your own registry and allow-list.** Do not delegate discovery to a vendor's open catalog. Run an internal registry that publishes an approved `ai-catalog.json`, and constrain runtime discovery (GitHub agent finder and its peers) so agents surface *only* what you permit — GitHub's own default posture. This turns dynamic discovery from an ungoverned reach-into-the-open into a productivity win *and* an audit source, and it is the layer that keeps running whoever wins the war.

3. **Route through a neutral abstraction — extend the 7 July router one layer up.** For any workflow you can't afford to re-platform, put a model- and standard-neutral abstraction between your agents and the gauge, so switching connection or discovery standards is a config change, not a rebuild. Assume neither MCP nor ARD nor A2A is guaranteed to win; build the junction that doesn't care. In a gauge war the prize is the junction everyone must pass through — own it, don't rent it.

---

*AI Tech Radar · generated 15 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The ARD (Agentic Resource Discovery) mechanics — a v0.9 Apache-2.0 draft announced 17 June 2026; the `ai-catalog.json` at `/.well-known/` plus crawling registries and runtime search; the backer roster (Google, Microsoft, GitHub, GoDaddy, Hugging Face, Nvidia, Salesforce, ServiceNow, Databricks, Snowflake, Cisco) with Anthropic and OpenAI absent; and GitHub's agent finder built on it — are relayed from the Google Developers Blog, the AgenticResourceDiscovery.org spec site, the GitHub Changelog, Search Engine Journal, Developer-Tech and secondary coverage. The "beat back Anthropic and OpenAI" framing is per The Information's July 2026 report and secondary coverage and is marked "as reported." MCP-adoption figures (~97M monthly downloads; 78% of enterprise AI teams; ~28% of Fortune 500; ~18 months to default) and the A2A ~150-orgs figure rest on secondary coverage and are marked "as reported." The Salesforce Agentforce figure ($800M ARR, +169% YoY) is from Salesforce's FY26 Q4 results. The PwC figures (56% / 12%) are from PwC's 29th Global CEO Survey (2026, n=4,454). The Gartner figures (40% embed by end-2026; >40% cancelled by end-2027) are Gartner's. The EU AI Act mechanics (GPAI enforcement applicable 2 August 2026; €15M or 3% of turnover) are relayed from the European Commission. The railway-gauge-war allegory is the radar's own illustration and is not a sourced claim; the "18 days" figure is a simple count from this edition's date to 2 August 2026.*
