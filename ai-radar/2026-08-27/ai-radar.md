# 🗓️ AI Tech Radar — The Lingua Franca

**Thursday, 27 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar issued the papers: a real, centrally governed identity for every agent — the passport that names the traveler at the door. But a named traveler who cannot make himself understood is no more useful than an anonymous one. Today the radar asks the question the passport leaves open: **once you can name the agent, in what language does it speak — to your tools, to your data, and to every other agent it must work with?** And this week the market did something quieter and more consequential than any model release: it moved the answer out of any one vendor's vault. **Google's Agent2Agent (A2A) protocol — the open standard for agents to discover, task and collaborate with one another — formally joined the Linux Foundation's Agentic AI Foundation (AAIF), placing it under vendor-neutral governance alongside Anthropic's Model Context Protocol (MCP), the standard that connects agents to tools and data.** The two tongues an enterprise agent must speak — *agent-to-agent* and *agent-to-tool* — now live in the same neutral library, backed by every major cloud and lab. The scale behind the urgency is Gartner's: **by 2028 the average Global Fortune 500 enterprise will run more than 150,000 AI agents (up from fewer than 15 in 2025) — yet only 13% believe they have the governance right, and fewer than half can even inventory the agents they already run (SAP LeanIX).** The board's question this morning: ***when our systems fill with a hundred thousand agents that must talk to each other and to every tool we own, are we building them to speak the open, neutrally-governed lingua franca that any vendor's agent can understand — or are we wiring each one to a private dialect and a bespoke interpreter, betting the whole estate on one prince's dictionary that he can rewrite or lock whenever he likes?***

---

## 1 · Executive Summary (90-second read)

For a week this radar walked the value up the stack — the watchman, the guardrail, the reservoir's value gap, the gate every agent must pass, the governed knowledge worth defending, and yesterday the passport that names every agent. Today it names the layer that makes all of them *interoperate:* **the common tongue.** The governing shift is no longer "can an agent act?" or "who is the agent?" — it is **"in what language does the agent speak, who controls that language, and can any vendor take it away from us?"** The market's answer this week is **agent interoperability as an open, vendor-neutral standard — placed deliberately beyond any single vendor's control.**

**The datable signal — the protocol layer consolidates under neutral governance.** In the last days of August, **Google's Agent2Agent (A2A) protocol formally joined the Linux Foundation's Agentic AI Foundation (AAIF),** placing the open standard for agent-to-agent communication under the same vendor-neutral governance as **Anthropic's Model Context Protocol (MCP),** which standardizes how agents reach tools and data. Two protocols, two jobs — *agents talking to agents,* and *agents talking to tools* — now sit in one neutral home backed by **Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Block and Shopify.** Linux Foundation Executive Director **Jim Zemlin:** *"By joining the Linux Foundation, A2A is ensuring the long-term neutrality, collaboration and governance that will unlock the next era of agent-to-agent powered productivity."* The lingua franca of the agent economy just became a public good rather than a private moat.

**The move — the scale demands a shared language, fast.** The reason interoperability suddenly dominates is a population explosion of agents that must coordinate. **Gartner: by 2028 the average Global Fortune 500 enterprise will run more than 150,000 AI agents (up from fewer than 15 in 2025); only 13% believe they have the right governance.** And you cannot govern — or connect — what you cannot see: **SAP LeanIX's 2026 agentic survey finds 98% of firms have deployed or plan to deploy agents, but fewer than half have any inventory visibility into them.** A hundred thousand agents each wired to its tools and peers with bespoke, per-vendor glue is an integration bill and a lock-in trap that compounds with every new agent; a hundred thousand agents speaking one open tongue is an architecture.

1. **The settlement — one neutral home for both tongues.** **A2A (agent↔agent) joins Anthropic's MCP (agent↔tools/data) under the Linux Foundation's AAIF.** A2A reached v1.0 in April 2026, is used by 150+ organizations, ships in major cloud platforms and is in enterprise production; AAIF has grown from fewer than 40 members at its December 2025 launch to more than 250. The standards stay distinct — they are not merged — but they now share vendor-neutral governance no single lab controls.

2. **The scale — why a shared language, not bespoke glue.** **Gartner: 150,000+ agents per Fortune 500 enterprise by 2028 (from <15 in 2025), only 13% with adequate governance; SAP LeanIX: 98% use or plan agents, <50% can inventory them.** N agents × M tools of custom integration does not survive those numbers. The open protocol is the only wiring that scales.

3. **The direction — identity and security move into the standard.** The **MCP roadmap (22 Aug 2026)** names *agent identity and enterprise security* a top priority — standardized ways to recognize and trust agent identities via **DPoP and Workload Identity Federation** — folding yesterday's passport into the wire protocol itself. The **EU AI Act** (Article 50 transparency + Article 12 reconstructability logging, live since 2 Aug, fines up to €15M/3%) is easier to meet when agents speak an auditable, standardized language.

**Bottom line:** the passport named the traveler; the lingua franca is how that named traveler actually works — with your tools, your data, and every other agent in and beyond your walls. **When an enterprise will soon run six figures of agents that must interoperate, the control point is not any one model or vendor but the standard they speak — and the decisive fact this week is that the two core standards now live under neutral, vendor-neutral governance, so building on them is no longer a bet on one company.** An enterprise wiring each agent to a proprietary dialect and a bespoke interpreter is buying an integration bill that compounds and a lock-in it will curse in two years. **Stop hand-wiring agents to private protocols and start building on the open, neutrally-governed lingua franca: adopt A2A for agent-to-agent and MCP for agent-to-tool, insist your vendors speak them, and keep your agent architecture portable — because when the model is rented, the knowledge is the moat, and the agent is named, the language they all speak is the one thing you want owned by everyone and controlled by no one.**

---

## 2 · Allegory of the Day — "The Lingua Franca"

*Topic: In the last week of August 2026, the dominant enterprise-AI thread was the consolidation of the agent-interoperability protocol layer under vendor-neutral governance. Google's Agent2Agent (A2A) protocol — the open standard for agent-to-agent discovery, tasking and collaboration — formally joined the Linux Foundation's Agentic AI Foundation (AAIF), placing it alongside Anthropic's Model Context Protocol (MCP), which standardizes agent-to-tool/data connections. AAIF, launched December 2025, has grown from fewer than 40 members to more than 250, backed by Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Block and Shopify; A2A reached v1.0 in April 2026, is used by 150+ organizations, ships in major clouds and is in enterprise production (IBM's ACP merged into A2A in 2025). Linux Foundation ED Jim Zemlin framed the aim as "long-term neutrality, collaboration and governance." Gartner projects the average Global Fortune 500 enterprise will run more than 150,000 AI agents by 2028 (up from fewer than 15 in 2025), with only 13% confident in their governance; SAP LeanIX finds 98% of firms deploy or plan agents but fewer than half can inventory them. The MCP roadmap (22 Aug 2026) names agent identity and enterprise security a top priority. The lesson: after building the gate every agent must pass, the governed larder behind it, and the passport that names each agent, the remaining question is the language every agent speaks — and this week the market settled it on open, neutrally-governed standards. The lingua franca allegory is the radar's own illustration.*

There was a great trading crossroads where the houses had grown rich, and richer still once each began sending out **tireless couriers** to do its business — to carry messages between houses, to fetch from warehouses, to strike bargains at counters across the city. But every house had raised its couriers to speak only its own **house dialect.** So at every doorway sat a **hired interpreter,** translating this house's courier to that house's clerk, this dialect to that tongue, one painstaking pairing at a time. When a house kept ten couriers and dealt with ten others, it paid for a hundred interpreters; and the city was heading, everyone agreed, for a day when a single great house would field not ten couriers but a hundred thousand — at which point the interpreters would outnumber the goods, and no one would be able to say which courier had spoken to whom, or in whose words.

For a while each house tried to win by making *its* dialect the one everyone learned. A powerful merchant-prince would publish his tongue for free, coax the others into teaching it to their couriers — and then, once enough of the city depended on it, quietly change a word, or charge for the dictionary, or bind the best phrases to his own warehouses. The houses that had bet everything on one prince's dialect woke to find their couriers fluent in a language they no longer controlled, spoken at a toll they had not agreed to. A common tongue owned by one house, they learned, is not a common tongue at all; it is a leash the owner can shorten whenever he likes.

The crossroads that kept its footing did something wiser. It settled not on one dialect but on **two open tongues** — one for couriers to speak *to one another,* so any house's courier could find, task and answer any other's; and one for couriers to speak *to the warehouses and counters,* so any courier could fetch from any house's stores without a private key cut for each. And — this was the decisive part — it placed both **dictionaries not in any prince's vault but in a neutral public library,** kept by a guild that no single house could rule, funded by all and captured by none. The tongues stayed **two, and distinct** — talking-to-agents and talking-to-tools are different crafts — but they shared one honest, unlockable home. Now a house could raise its couriers on the common tongues and know the words would not be changed against it, nor the dictionary ransomed, nor the language die if one prince fell out of love with it.

But the cautionary half of the tale was the houses that heard "adopt the common tongue" and still got it wrong. Some kept a **private fork** of the dictionary "for convenience," and drifted until their couriers could no longer be understood abroad. Some spoke the open tongue at the front gate but wired their inner rooms with the old bespoke glue, so the portability stopped at the threshold. And some adopted the words but never wrote down **who said what to whom** — fluent couriers leaving no record a magistrate could read. A common tongue is only worth the neutrality that keeps it open, the discipline that keeps you speaking it everywhere, and the ledger that records what was said in it. Words without a register are just faster rumor.

**The moral:** when the crossroads fills with a hundred thousand couriers who must understand one another and every counter in the city, the thing you must not own privately — and must not let anyone else own privately either — is the **language they speak.** The model is a rented stove, the knowledge is your larder, the gate is your one door, the passport names each courier — and the **lingua franca** is what lets the named courier actually work: an open tongue for agent-to-agent, an open tongue for agent-to-tool, both kept in a neutral library no vendor can lock. Build your couriers to speak it and they can work with anyone's, forever, at no toll. Wire them to a prince's private dialect and you have bought a leash and called it a language.

**The question it forces:** *Our systems are filling with agents that must talk to each other and to every tool we own — soon a hundred thousand of them. Are we raising them to speak the open, neutrally-governed lingua franca (A2A for agent-to-agent, MCP for agent-to-tool), so any vendor's agent can understand ours and no one can change the words against us — or are we hand-wiring each agent to a proprietary dialect and a bespoke interpreter, quietly betting the whole estate on one prince's dictionary that he can rewrite, ransom, or retire whenever it suits him?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **Do our agents speak an open tongue — or a private dialect?** A2A (agent-to-agent) and MCP (agent-to-tool) now sit under one vendor-neutral foundation. **Are we building on those open standards, or wiring agents to a single vendor's proprietary protocol we don't control and can't take with us?**
- **Would our agent estate survive a Fortune-500-scale count?** Gartner projects 150,000+ agents per large enterprise by 2028, yet only 13% feel governed and fewer than half can inventory what they run. **Does our agent architecture scale on a shared standard, or on bespoke glue that multiplies with every new agent?**
- **Is the language in a neutral library or a prince's vault?** The decisive fact this week is *governance,* not the protocol itself. **If our core agent vendor changed its terms or its spec tomorrow, how much of our estate would we have to rewire — and could a competitor's agents still talk to ours?**

### 🏦 Financial Services
- Agents in payments, trading and client service must interoperate across counterparties and regulators. **Are we adopting open agent protocols (A2A/MCP) so a partner's or regulator's systems can interoperate with ours without bespoke integration — and so we're not locked to one vendor's rails for a decade?**
- Interoperability without attribution is a control gap. **Does every agent-to-agent and agent-to-tool exchange leave an auditable, standardized record we could reconstruct — Article-12-grade — for a regulator?**

### 🧬 Healthcare / Life Sciences
- Clinical and research agents must exchange data across EHRs, labs and partners under strict privacy. **Are our agents speaking open, auditable standards so PHI moves through governed, inspectable channels — not a tangle of one-off connectors no one can review?**
- Vendor lock-in is a patient-safety and continuity risk. **If a clinical-agent vendor failed or changed terms, could our agents keep talking to our systems because they speak an open tongue, or would care workflows break?**

### 🏭 Manufacturing / Industrials
- Agents wired into OT, MES and multi-tier supplier systems must coordinate across organizational boundaries. **Do our supplier and internal agents share an open agent-to-agent protocol, or does every new partner mean another bespoke, brittle interpreter at the seam?**
- Long-lived industrial estates outlive vendor fashions. **Are we standing on neutrally-governed standards that will still be spoken in ten years, or a private dialect that could be deprecated?**

### 🛒 Retail / Consumer
- Pricing, fulfillment and service agents must talk to marketplaces, payment and logistics partners at speed. **Are we building on open protocols so we can plug into any partner's agents without re-integration — turning interoperability into a go-to-market advantage rather than a cost?**
- Consumer-facing agents proliferate fastest. **Can each new agent join our estate by speaking the common tongue, or does every launch add another custom connector to maintain?**

### 🏛️ Public Sector / Regulated
- Public systems demand vendor-neutrality, portability and auditability by mandate. **Are we procuring agents on open, neutrally-governed standards (A2A/MCP under the Linux Foundation) so citizen-facing automation is portable across vendors and auditable — not captured by one supplier?**
- Neutrality is a procurement principle, not a nicety. **Do our contracts require open agent protocols so a change of vendor doesn't strand a public service?**

---

## 4 · Technical Deep-Dive — The Two Tongues, the Neutral Library, and the Register

Read the stack once more as layers priced and governed very differently — but this week, past *which layer you buy,* past *who watches it,* past *through what door every agent passes,* past *what governed knowledge sits behind that door,* and past *who the agent is,* to the question every acting agent hits the instant it tries to do anything useful: **in what language does it speak, and who owns that language?** At the **bottom** is the *engine* — the rented, swappable model. Above it sit the **rails,** the **pilotage,** the **acting agent,** the **watchman,** the **guardrail,** the **gate,** the **larder** and the **passport.** All still true. What this week isolates is the layer that lets a named agent actually *work across the estate:* **the interoperability protocols — and, decisively, the neutral governance that keeps them open.** The engineering point is blunt: **a named agent that cannot speak a shared, open language is stranded; and a shared language owned by one vendor is a lock-in you have not priced yet. Two tongues, one neutral home.**

- **The two tongues — distinct jobs, one neutral home.** **A2A (Agent2Agent)** standardizes how independent agents **discover, task and collaborate** with one another across vendors and frameworks; **MCP (Model Context Protocol)** standardizes how an agent connects to **tools, data and applications.** This week **A2A formally joined the Linux Foundation's Agentic AI Foundation (AAIF),** the same vendor-neutral home as MCP. The two specs are **not merged and not interchangeable** — they solve different problems — but they now share governance no single lab controls. A2A: v1.0 April 2026, **150+ organizations,** in major cloud platforms, enterprise production; IBM's ACP merged into A2A in 2025.
- **The neutral library — why governance is the story, not the protocol.** **AAIF (Linux Foundation), launched December 2025, has grown from fewer than 40 members to more than 250,** backed by **Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Block and Shopify.** The value is not that a standard exists — proprietary "open" standards exist and get quietly enclosed — but that the dictionary sits in a library **no single vendor can rewrite, ransom or retire.** Jim Zemlin (Linux Foundation): the move ensures "long-term neutrality, collaboration and governance." Building on a neutrally-governed standard is the difference between an architecture and a bet.
- **The register — scale, identity and the audit trail.** **Gartner: 150,000+ agents per Fortune 500 enterprise by 2028 (from <15 in 2025), only 13% adequately governed; SAP LeanIX: 98% use or plan agents, <50% can inventory them.** Bespoke N×M integration does not survive that. And interoperability without attribution is a gap: the **MCP roadmap (22 Aug 2026)** makes *agent identity and enterprise security* a top priority — **DPoP, Workload Identity Federation** — folding the passport into the wire itself, while the **EU AI Act's Article 12/50** (live since 2 Aug, fines up to €15M/3%) rewards a standardized, auditable language over opaque custom glue.

The strategic core: **when agents must interoperate at six-figure scale, the control point is the standard they speak — and this week the two core standards became open goods under neutral governance.** For a week the frame moved from "own the right layer" to "oversee without custody" to "build the gate" to "own the governed knowledge" to "name every agent"; this week's refinement is **the language every named agent speaks, kept where no vendor can lock it.** "We picked a great agent platform" is not an answer to "can your agents talk to anyone else's, and who controls the words"; ***"our agents speak A2A and MCP, standards governed by a neutral foundation no vendor controls, so our estate is portable and interoperable by construction"*** is the answer.

```
        THE LINGUA FRANCA — a named agent is stranded without a shared, open language.
        150,000 agents per enterprise by 2028 — the tongue they speak is the architecture.

   THE BABEL (why standards now)                 THE COMMON TONGUE (the settlement)
   ┌──────────────────────────────┐            ┌──────────────────────────────┐
   │  150,000+ agents / F500 by 2028 │          │  Two open tongues, one home:     │
   │  (up from <15 in 2025)          │  →  SO   │  A2A = agent ↔ agent             │
   │  only 13% feel governed         │  SPEAK → │  MCP = agent ↔ tools / data      │
   │  <50% can inventory agents      │  ONE     │  joined under Linux Foundation   │
   │  ▲ N×M bespoke glue collapses   │  TONGUE  │  ▼ AAIF · vendor-neutral         │
   └───────────────┬──────────────┘            └───────────────┬──────────────┘
                   │   the dictionary moves from a vault to a library │
                   ▼                                              ▼
   ┌───────────────────────────────────────────────────────────────────────────┐
   │  THE NEUTRAL LIBRARY — governance is the story, not the protocol             │
   │  A2A: v1.0 Apr 2026 · 150+ orgs · in major clouds · enterprise production    │
   │  AAIF: <40 → 250+ members · Google, Microsoft, Amazon, Anthropic, OpenAI,    │
   │  Bloomberg, Block, Shopify · no single vendor can rewrite/ransom/retire it   │
   │  MCP roadmap (22 Aug): agent identity + security (DPoP, Workload Identity)    │
   └───────────────────────────────────────────────────────────────────────────┘
                                                ▼ so
   ┌──────────────────────────────┐   ┌────────────────────────────────────────┐
   │  STOP: private dialects & glue │  │  START: build on the open tongues        │
   │  · one vendor's proprietary     │   │  · A2A for agent-to-agent                │
   │    protocol                     │  │  · MCP for agent-to-tool/data            │
   │  · bespoke N×M interpreters      │  │  · insist vendors speak them · stay      │
   │  · lock-in you'll curse in 2 yrs │   │    portable · log what's said            │
   └──────────────────────────────┘   └────────────────────────────────────────┘
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The private dialect versus the open tongue — the same agent, two very different bets

| Wiring agents to a proprietary protocol | Building on the open, neutral standards |
|---|---|
| One vendor's dialect you don't control | A2A + MCP, governed by a neutral foundation |
| Words can change, or be priced, against you | Spec evolves in the open; no unilateral lock |
| Bespoke N×M integration, per vendor pair | Speak-once, interoperate with any conformant agent |
| Estate stranded if the vendor pivots or fails | Portable across vendors and frameworks |
| Interop stops at the vendor's boundary | Agents talk across organizational boundaries |
| Audit trail is proprietary and opaque | Standardized, inspectable, Article-12-friendly |

### Why "the lingua franca" is the artifact that matters

For a year the reflex was to pick the best agent *platform;* this week's news says the enforceable unit of freedom is the *protocol* — and, more precisely, *who governs it.* An interoperability standard is model-agnostic and unglamorous — it makes no headline like a new frontier release — but it is what turns a captive fleet of agents into a portable, composable estate. That is why the signal is sharp: the two core agent standards, one for agent-to-agent and one for agent-to-tool, now sit in **one neutral foundation backed by every major cloud and lab,** precisely as Gartner projects six-figure agent counts per enterprise. The interesting artifact this week is not a smarter agent — it is **a common tongue no single vendor can lock.**

### How it lands on legacy estates

Same seam this radar keeps returning to — **be deliberate about what you own, rent and finance, and on what terms** — now applied to the wire between agents. Integration debt is the estate's oldest tax (every system pair its own connector), and agents threaten to multiply it a hundred-thousand-fold. The retrofit is **standardize, neutralize, register. Standardize:** adopt A2A for agent-to-agent and MCP for agent-to-tool, and make "speaks the open protocols" a procurement requirement, not a nice-to-have. **Neutralize:** prefer the neutrally-governed spec over a vendor's "open-ish" fork, so no supplier can enclose your wiring later. **Keep the register:** wire standardized identity (DPoP / Workload Identity Federation, per the MCP roadmap) and Article-12 logging into every exchange, so interoperability never outruns attribution. And keep the engine swappable behind it — because the model is the commodity, the knowledge is the moat, the passport names the agent, and *the open language they all speak is the freedom you keep.*

**The clean mental model:** *The model is a rented stove; your proprietary knowledge is the larder; the gateway is the one governed door; the passport names each agent. The lingua franca is how the named agent actually works — two open tongues (agent-to-agent, agent-to-tool) kept in a neutral library no vendor can lock. Build your agents to speak it and they interoperate with anyone's, at no toll, for good. Wire them to a private dialect and you have bought a leash and called it a language.*

### Watch list this week
- **The settlement — the protocol layer consolidates.** **A2A joins Anthropic's MCP under the Linux Foundation's AAIF;** two distinct tongues (agent↔agent, agent↔tool), one neutral home; A2A v1.0 Apr 2026, 150+ orgs, in major clouds, enterprise production (as reported).
- **The library — governance is the story.** **AAIF: <40 → 250+ members** (Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Block, Shopify); Jim Zemlin — "long-term neutrality, collaboration and governance" (as reported).
- **The scale — why a shared language.** **Gartner: 150,000+ agents / F500 enterprise by 2028** (from <15 in 2025), only 13% adequately governed; **SAP LeanIX: 98% use/plan agents, <50% can inventory them** (as reported).
- **The direction — identity moves into the wire.** **MCP roadmap (22 Aug 2026):** agent identity + enterprise security a top priority — DPoP, Workload Identity Federation, HTTP-native transport (modelcontextprotocol.io).
- **The ledger — compliance in statute (context).** **EU AI Act:** Article 12 reconstructability + Article 50 transparency live since 2 Aug, fines up to €15M/3%; high-risk deferred to Dec 2027 (Digital Omnibus, Reg 2026/1744). A standardized language is easier to audit (as reported).
- **The engine — cheap and multiplying (context).** Fastest month in AI history: **11+ models in 20 days.** Opus 5, Grok 4.6, GPT-5.6 / Luna, Gemini 3.7 Flash, open-weight GLM-5.3 / Qwen3.8 / Kimi K3 — the interchangeable engine is why the standard, not the model, is the control point (as reported).

---

## 5 · Quotes That Catch the Eye

> By joining the Linux Foundation, A2A is ensuring the long-term neutrality, collaboration and governance that will unlock the next era of agent-to-agent powered productivity.
> — **Jim Zemlin**, Executive Director, The Linux Foundation, on placing the Agent2Agent protocol under vendor-neutral governance (as reported)

> A2A empowers developers to build agents that seamlessly interoperate, regardless of platform, vendor or framework.
> — **Agent2Agent project** framing, on why an open agent-to-agent standard matters (as reported)

> By 2028, the average global Fortune 500 enterprise will have more than 150,000 AI agents in use — yet only 13% believe they have the right governance in place.
> — **Gartner**, on agent sprawl and the governance gap (as reported)

> "A named agent that cannot speak a shared, open language is stranded — and a shared language owned by one vendor is a leash you have not priced yet."
> — *the radar, on the lingua franca*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| The settlement — one neutral home for both tongues | **Google's Agent2Agent (A2A) protocol formally joined the Linux Foundation's Agentic AI Foundation (AAIF), placing agent-to-agent standards under the same vendor-neutral governance as Anthropic's MCP (agent-to-tool/data); the specs remain distinct, not merged** | Forbes / Axios / Linux Foundation / Yahoo (as reported) |
| A2A adoption | **A2A reached v1.0 in April 2026, is used by 150+ organizations, ships in major cloud platforms and is in enterprise production; IBM's ACP merged into A2A in 2025** | Linux Foundation / trade coverage (as reported) |
| The neutral library — AAIF membership | **AAIF (launched December 2025) has grown from fewer than 40 members to more than 250, backed by Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Block and Shopify** | Axios / Forbes / Linux Foundation (as reported) |
| The scale — agents per enterprise | **By 2028 the average Global Fortune 500 enterprise will run more than 150,000 AI agents (up from fewer than 15 in 2025); only 13% believe they have the right governance** | Gartner (as reported) |
| The gap — inventory & visibility | **98% of firms have deployed or plan to deploy AI agents, but fewer than half have any inventory visibility into them** | SAP LeanIX 2026 agentic survey (as reported) |
| The direction — identity in the wire | **MCP roadmap (22 Aug 2026) names agent identity and enterprise security a top priority — DPoP and Workload Identity Federation — plus HTTP-native transport unification** | modelcontextprotocol.io (roadmap) |
| The ledger — compliance (context) | **EU AI Act Article 12 (reconstructability logging) + Article 50 transparency live since 2 Aug; fines up to €15M or 3% of global turnover; high-risk deferred to Dec 2027 (Digital Omnibus, Reg 2026/1744)** | European Commission / legal coverage |
| The engine (context) | **Fastest month in AI history — 11+ models in 20 days. Opus 5 · Grok 4.6 · GPT-5.6 / Luna · Gemini 3.7 Flash · GLM-5.3 · Qwen3.8 · Kimi K3 (open-weight)** | Model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Standardize — make "speaks A2A and MCP" a hard requirement.** Bespoke, per-vendor integration is the tax that compounds with every new agent, and you are heading for six figures of them. **This month, adopt A2A for agent-to-agent and MCP for agent-to-tool as your default wiring, and write "must speak the open agent protocols" into every agent procurement and build.** Prove it on one cross-vendor agent workflow — an agent that must task another and reach an outside tool — and measure the integration effort you avoided.

2. **Neutralize — build on the neutrally-governed spec, not a vendor's fork.** The story this week is *governance,* not the protocol: an "open" standard one vendor controls can be enclosed later. **Prefer the Linux Foundation / AAIF-governed specifications over any single vendor's proprietary or forked variant, and treat vendor-neutral governance as a checklist item in architecture reviews.** Ask of every agent vendor: *if you changed your terms tomorrow, what would we have to rewire?* If the answer is "a lot," you are on a leash, not a language.

3. **Keep the register — wire identity and logging into every exchange.** Interoperability without attribution is a control gap that regulators and incidents will find. **Adopt standardized agent identity (DPoP / Workload Identity Federation, per the MCP roadmap) and Article-12-grade logging on every agent-to-agent and agent-to-tool exchange,** so the common tongue is always spoken into a ledger. Report two numbers to the board next quarter: the share of your agents built on open, neutrally-governed protocols, and the share of agent exchanges that leave a standardized, auditable record. **The model is rented, the knowledge is the moat, the agent is named — and the open language they all speak is the freedom you keep.**

---

*AI Tech Radar · generated 27 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The central development in the window is the consolidation of the agent-interoperability protocol layer under vendor-neutral governance — Google's Agent2Agent (A2A) protocol formally joining the Linux Foundation's Agentic AI Foundation (AAIF) alongside Anthropic's Model Context Protocol (MCP), placing the two core agent standards (agent-to-agent and agent-to-tool) under a neutral home no single vendor controls, with Linux Foundation Executive Director Jim Zemlin framing the aim as "long-term neutrality, collaboration and governance" — relayed from the Linux Foundation announcement and secondary coverage (Forbes, Axios, Yahoo/Forkast) as reported. The adoption figures (A2A reaching v1.0 in April 2026, used by 150+ organizations, shipping in major cloud platforms and in enterprise production, with IBM's ACP merged into A2A in 2025; AAIF growing from fewer than 40 members at its December 2025 launch to more than 250, backed by Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Block and Shopify) are relayed from those reports and secondary coverage as reported. The scale figures (that Gartner projects the average Global Fortune 500 enterprise will run more than 150,000 AI agents by 2028, up from fewer than 15 in 2025, with only 13% confident in their governance; and that SAP LeanIX's 2026 agentic survey found 98% of firms deploy or plan to deploy agents while fewer than half can inventory them) are relayed from Gartner and SAP as reported. The MCP roadmap facts (that the 22 August 2026 roadmap names agent identity and enterprise security a top priority, citing DPoP and Workload Identity Federation, alongside HTTP-native transport unification) are relayed from the Model Context Protocol blog. The EU AI Act facts (Article 50 transparency and Article 12 reconstructability logging applicable since 2 August 2026, fines up to the higher of €15 million or 3% of worldwide annual turnover, high-risk obligations deferred to December 2027 under the Digital Omnibus, Regulation 2026/1744) are relayed from the European Commission and legal coverage as reported. The model and pricing details (the fastest month in AI history with 11+ models in 20 days; Claude Opus 5, xAI Grok 4.6, OpenAI GPT-5.6 and GPT-5.6-Luna, Google Gemini 3.7 Flash, and open-weight Z.ai GLM-5.3, Alibaba Qwen3.8 and Moonshot Kimi K3) are relayed from model-tracker and vendor coverage as reported and carried as standing context. Prior-day context — this week's editions on agent identity ("The Passport," 26 Aug), the governed knowledge moat ("The Recipe," 25 Aug), the gatehouse/control plane ("The Gatehouse," 24 Aug), the reservoir/value gap ("The Reservoir," 23 Aug) and the two-edged security blade ("The Locksmith," 22 Aug) — is referenced only as background. Several primary and secondary pages (including the Linux Foundation, Forbes, Axios and a number of trade outlets) were unreachable from the compile environment behind the network egress proxy; those figures were cross-referenced across multiple reputable outlets and search summaries and should be re-verified at source before republishing. The lingua franca allegory — a trading crossroads whose houses once needed a hired interpreter at every doorway, until it settled on two open tongues (one for courier-to-courier, one for courier-to-warehouse) and placed both dictionaries in a neutral public library no single house could rule — is the radar's own illustration and is not a sourced claim about any specific company or product.*
