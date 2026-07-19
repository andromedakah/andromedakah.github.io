# 🛰️ AI Tech Radar — The Triage Tent

**Sunday, 19 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar watched the model itself have its **aluminum moment** — Kimi K3 made frontier capability cheap, open, and self-hostable, and the metal everyone treated as precious became a commodity. The thesis we drew was that value migrates *off the ingot and onto the airframe you build with it.* Today that airframe stopped being an abstraction and shipped as a product. Reporting this weekend describes **Microsoft's "Project Perception"** — an AI cybersecurity platform, positioned squarely against **Anthropic's Claude Mythos** — whose entire competitive edge is **not a model at all.** It is an **orchestration layer** that routes each security task to the cheapest model that can do it — Microsoft, OpenAI or Anthropic — and calls a frontier model only for the few steps that truly need one, aiming to make automated vulnerability fixing *"cheap enough to run nonstop."* The day after intelligence became a commodity, the first flagship product built on that commodity competes on the **dispatch logic,** not the metal. The board's question sharpens: ***when every rival can buy the same intelligence for a few dollars a million tokens, is our advantage the model — or the triage layer that decides which model touches which job, and reserves the expensive one for where it actually earns its keep?***

---

## 1 · Executive Summary (90-second read)

For three weeks this radar has argued one thesis — *the model is commoditizing; own and govern the layer around it.* Yesterday the model itself commoditized in public (18 Jul, "the aluminum age" — Kimi K3). Today the thesis gets its first **shipping proof point.** Reporting over the weekend describes **Microsoft's Project Perception,** an AI security platform whose defining feature is an **orchestration layer** — it dispatches each vulnerability-hunting task to the best-fit, cheapest-adequate model and escalates to a frontier model only for the genuinely hard steps. It is the **model-neutral router (7 Jul) turned into a product,** aimed straight at **Anthropic's Claude Mythos.** It lands amid the same enforceable countdowns this radar has tracked all fortnight: **Kimi K3's open weights on 27 July (8 days), MCP's final spec on 28 July (9 days),** and the **EU AI Act's GPAI enforcement on 2 Aug (14 days).**

1. **The first flagship built on commodity intelligence competes on routing, not the model.** Project Perception reportedly combines models from **Microsoft, OpenAI and Anthropic** behind an **orchestration layer that "chooses which AI model handles each step, rather than sending every job through the most powerful — and most expensive — system."** A low-cost model handles triage, log parsing and inventory; a **frontier model is reserved** for complex exploit chains, authentication flows, and remediation plans that touch production. The goal is to make vulnerability fixing **cheap enough to run continuously,** not just on high-severity incidents — undercutting **Anthropic's Mythos 5** (listed at **$10 / $50 per million tokens,** access limited to vetted partners).

2. **This is the "airframe" from yesterday, made concrete.** The value in Perception is not any single model — every rival can buy the same intelligence, and after Kimi K3 can nearly download it. The value is the **dispatch logic:** the layer that knows which task is worth a frontier call and which is not, and can swap a cheaper or open model in without re-tooling. Independent commentators have been converging on the same point for weeks — as frontier capability converges, *"enterprise AI wins or loses at the orchestration layer."* Perception is that thesis shipped.

3. **A routing layer is also a governance layer — or it isn't, and that's the trap.** The same orchestration point that picks the cheapest model is the natural place to enforce policy: which model may see which data, what gets logged, where a human must sign off. Build it as a pure cost-router and you've optimized spend while multiplying an **ungoverned** surface — exactly the surface the **EU AI Act inspects in 14 days** (inventory, access control, logging, human oversight). Gartner still expects **40% of enterprise apps to embed task-specific agents by end-2026** and **>40% of agentic projects cancelled by end-2027** — the ones that survive will be the ones whose orchestration layer governs as deliberately as it routes.

**Bottom line:** yesterday the metal went cheap; today the first product proved where the value went — **the triage tent, not the surgeon.** When every competitor can buy or download the same frontier intelligence, your moat is the layer that decides *which* intelligence touches *which* job, reserves the expensive one for where it earns its keep, and enforces the governance the regulator will demand on 2 August. **Own the routing; make it govern as well as it saves.** The model is a commodity you rent by the token. The triage is yours to build — and it is where the margin, and the compliance, now live.

---

## 2 · Allegory of the Day — "The Triage Tent"

*Topic: Reporting over the weekend of 18–19 July 2026 describes Microsoft's "Project Perception," an AI cybersecurity platform positioned against Anthropic's Claude Mythos, whose defining feature is not a proprietary model but an orchestration layer that routes each task to the cheapest capable model and reserves a frontier model for the few hardest steps — the day after Kimi K3 made frontier intelligence itself a commodity. The lesson for the enterprise: when the scarce resource becomes abundant, the value moves to the system that decides where the still-costly capacity is spent.*

On the battlefields of the Napoleonic wars, a wounded soldier's fate was decided less by the skill of any one surgeon than by a colder and more radical idea: **who gets seen, and in what order.** Before **Dominique-Jean Larrey,** surgeon-in-chief of the Grande Armée, the wounded were treated by rank, by chance, or by whoever shouted loudest — and the scarce, exhausting hours of a skilled surgeon were spent almost at random. Larrey's innovation was not a sharper scalpel. It was a **system of sorting** — from the French *trier,* to sort — that assessed every casualty by the *severity and urgency of the wound,* and by that alone. The lightly hurt were patched and sent back. The hopeless were made comfortable. And the surgeon's irreplaceable hands were reserved for the cases where they would actually change the outcome — friend or enemy, general or private, it made no difference to the sorting.

Larrey paired it with the **"flying ambulance,"** light carts that reached the wounded fast and moved them to the right level of care. At **Borodino in 1812,** amid a scale of carnage that would have swamped any surgical tent run first-come-first-served, the system let a handful of surgeons do the work of many — because the scarce resource, the surgeon's time, was **spent only where it was worth spending.** Every case that a dresser or an orderly could handle was routed away from the surgeon, so that the surgeon's hours went to the exploit chains, so to speak, and not the log parsing.

Here is the part the board must sit with. Larrey's triage did not make the surgeon less skilled or less necessary — it made the surgeon's scarce time **enormously more valuable,** by ensuring none of it was wasted. The genius, and the thing that got copied into every army and every emergency room on Earth, **was the sorting system, not the surgery.** Microsoft's Project Perception is a triage tent for machine intelligence. Frontier capability, after Kimi K3, is no longer the scarce surgeon it was a year ago — but the *best* capability, called on the *right* step, still costs real money and still matters. The value Perception competes on is the **triage:** the layer that reads each incoming job, sends the routine mass to a cheap model, and reserves the frontier model for the wound that will actually kill the patient.

**The moral:** when the scarce resource becomes abundant, the fortune moves to whoever decides *where the still-costly capacity is spent.* Do not build your moat on owning the surgeon — everyone can hire one now, or download one next week. Build it on the **triage tent:** the orchestration layer that routes every task to the cheapest capability that suffices, escalates only where it pays, and — this is the half most people skip — **governs the sorting itself,** so that which model sees which data, what is logged, and where a human must sign off are decisions the tent makes on purpose, not by accident. Larrey's list of who-gets-the-surgeon was also, quietly, a **record of every decision made** — which is exactly what the regulator will ask you for.

**The question it forces:** *If every competitor can now buy or download the same frontier intelligence, is our advantage the model we license — which is a commodity — or the triage tent we build around it: the orchestration layer that decides which model touches which job, reserves the expensive one for where it earns its keep, and keeps the auditable record of every routing decision the regulator will demand on 2 August?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- The first flagship product built on newly-commoditized intelligence (Project Perception) competes on its **orchestration layer, not its model.** **Where in our stack does the value actually sit** — in the model we license, or in a routing/triage layer we own that reserves expensive capability for where it pays? If we can't point to the layer, we're paying surgeon rates for log-parsing.
- Perception routes each task to the **cheapest-adequate model and escalates only when needed.** **Have we instrumented our own AI workloads** to know which calls genuinely need a frontier model and which are burning premium tokens on routine work — and could we cut cost 50%+ by triaging, as Microsoft is betting?
- A routing layer is the natural **governance choke-point.** **Is our orchestration layer enforcing policy** — which model may see which data, what is logged, where a human signs off — or is it a pure cost-router that optimizes spend while multiplying an ungoverned surface the EU AI Act inspects in **14 days?**

### 🏦 Financial Services
- Model-routing across **three vendors** (as Perception reportedly does) is a cost and continuity win — but it means **regulated data can flow to whichever model the router picks.** **Does our orchestration layer pin data-residency and model-eligibility per task,** or does "cheapest model wins" quietly send a sensitive workload somewhere it shouldn't go?
- If a competitor can run AI security or analysis **"nonstop" at a fraction of our cost** by triaging models, our per-incident economics just changed. **Have we re-run the unit cost of every always-on AI workload** — fraud, AML, monitoring — under a route-to-cheapest-adequate model, and is that the source of edge rather than the model itself?

### 🧬 Healthcare / Life Sciences
- A triage-style router lets you keep **PHI on a cheap on-prem or open model** for routine steps and reserve a frontier call only for the hard ones. **Have we designed our orchestration to minimize where sensitive data touches a third-party frontier model,** and can we prove that routing to an auditor?
- Cheap, continuous AISecurity/analysis is a genuine safety win — and a validation burden. **When a router escalates a case to a frontier model, is there a logged, human-oversight checkpoint** for anything clinical, or does the sorting happen silently — the exact evidence the EU AI Act demands in **14 days?**

### 🏭 Manufacturing / Industrials
- The Perception logic — cheap model for the mass, frontier model for the exploit chain — maps directly onto the shop floor: **a cheap/edge model for routine OT triage, a frontier call only for the rare complex fault.** **Have we mapped which industrial AI tasks are "log-parsing" and which are "exploit chains,"** and are we routing accordingly instead of paying frontier rates for everything?
- Your moat is **process knowledge, not the model.** **Is our orchestration layer encoding how we actually triage and escalate** — the proprietary judgment of which fault needs the expert — or have we outsourced that judgment to a single vendor's model?

### 🛒 Retail / Consumer
- Model-routing can collapse the cost of always-on AI (support, personalization, fraud) by reserving frontier calls for the few high-value moments. **Have we re-priced every AI feature under a triage model** — cheap model by default, frontier only where it lifts conversion or catches real fraud — rather than a flat premium-model bill?
- A router that picks the cheapest model per task is only as good as **the data and rules that steer it.** **Does our differentiation live in that steering logic and our proprietary customer data** — which a competitor can't copy — or in a model everyone can now rent for a few dollars a million tokens?

### 🏛️ Public Sector / Regulated
- An orchestration layer that spans **multiple vendors' models** is attractive for cost and continuity — but for a public body it is also a **data-governance and sovereignty decision made per task.** **Does our router enforce which models (and which jurisdictions) may handle citizen data,** or does cost alone decide? 
- The EU's own **Action Plan on Cybersecurity and AI (7 Jul)** points at exactly this class of tool — advanced models evaluated before market, structured access for defenders. **Is our orchestration layer keeping the auditable record** of which model handled which task, ready for the GPAI enforcement powers that become applicable in **14 days?**

---

## 4 · Technical Deep-Dive — The Surgeon, the Sorting, and the Ledger

Strip the branding away and Project Perception is a bet on a single architectural claim: **once intelligence is abundant, the value is in the routing, not the model.** Read it as Larrey's triage tent in three parts — the surgeon whose time is still costly, the sorting that decides where it's spent, and the ledger that records the decision.

- **The surgeon (frontier capability, still costly per call).** Even after Kimi K3, the *best* model on the *hardest* step still costs real money — Anthropic's Mythos 5 is listed at **$10 / $50 per million tokens,** access restricted to vetted partners. Perception doesn't pretend that capability is free; it treats it as a **scarce surgeon** to be rationed. The frontier model is called for the steps that genuinely need it: a complex exploit chain, an authentication flow, a remediation plan that touches production.
- **The sorting (the orchestration layer — the actual product).** This is the value. Perception reportedly runs an **orchestration layer across Microsoft, OpenAI and Anthropic models** that "chooses which AI model handles each step, rather than sending every job through the most powerful — and most expensive — system." Routine triage, log parsing and inventory go to a **low-cost model;** only the hard steps escalate. The payoff is economic and strategic: it makes vulnerability fixing **cheap enough to run nonstop** rather than only on high-severity incidents — and it makes the *model* interchangeable, so a cheaper or open one can be swapped in without re-tooling.
- **The ledger (governance, the half most skip).** Larrey's triage was also a *record* of every decision. The orchestration layer is the one place that sees every task, every model choice, and every escalation — which makes it the natural place to enforce and log policy: which model may see which data, what is retained, where a human must approve. Built that way, the router *is* your EU AI Act evidence. Built as a pure cost-optimizer, it's an ungoverned sprawl that happens to be cheap.

The strategic core: **a routing layer is a windfall if it governs and a liability if it only saves.** If Perception (and its inevitable imitators) is right, the enterprise edge is no longer "we have the best model" — everyone does, cheaply — but *"we spend the expensive model only where it earns its keep, and we can prove every place it ran."*

```
        THE TRIAGE TENT  —  when intelligence is abundant, value is in the sorting
        Project Perception routes each task to the cheapest capable model; frontier only when it pays

   ┌──────────────────────────┐     ┌──────────────────────────────┐     ┌────────────────────────┐
   │  THE FLOOD OF TASKS       │     │   THE SORTING (the product)    │     │  THE FRONTIER SURGEON   │
   │  vuln scans, log parsing, │ ──▶ │   orchestration / triage layer │ ──▶ │  exploit chains, auth   │
   │  triage, inventory,       │     │   "which model handles which   │     │  flows, prod remediation│
   │  remediation drafts       │     │    step" — cheapest that works │     │  RARE · costly · rationed│
   └──────────────────────────┘     └───────────────┬──────────────┘     └────────────────────────┘
                                                     │  most tasks →
                                        ┌────────────▼───────────┐
                                        │  CHEAP / OPEN MODELS    │   ← the mass of work, run nonstop
                                        │  low-cost triage lane   │
                                        └────────────────────────┘
                                                     │
                                        ┌────────────▼───────────┐
                                        │  THE LEDGER (governance)│   which model saw which data,
                                        │  every routing decision │   what's logged, who signs off
                                        │  logged & auditable     │   → your EU AI Act evidence (14d)
                                        └────────────────────────┘

   TRAP: build a pure cost-router → cheap, fast, and an ungoverned surface the regulator inspects.
   WIN : build a triage tent that governs → reserve the surgeon, route the mass, log every call.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — the model is the product | The discipline — the routing is the product, and it governs |
|---|---|
| "We have access to the best model" | We spend the best model only where it earns its keep |
| Every task through one premium model | Cheapest-adequate model per task; frontier reserved and rationed |
| One vendor's model hard-wired in | A model-neutral router (7 Jul) that swaps cheap/open models in freely |
| Router optimizes cost only | Router enforces data-eligibility, logging and human sign-off |
| Escalations happen silently | Every routing decision logged — your EU AI Act ledger |

### Why cheaper-per-task doesn't shrink your governance — it grows the surface

Perception's whole promise is to make AI security **cheap enough to run nonstop.** But "nonstop" is the governance problem in three words. When each task was expensive, cost was the natural governor on how often and how widely a capable model ran. Route to the cheapest-adequate model and run continuously, and the number of places a model touches your data **explodes** — much of it automated, much of it invisible. Every one of those is a named EU AI Act deployer duty that becomes enforceable in **14 days.** The routing layer is the only vantage point that sees all of it, which is precisely why it must be the governance layer too, and not just the cost layer. Larrey's tent worked because the sorting *and the record* lived in the same place.

### How it lands on legacy estates

This is the same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the spend meter, 7 Jul the model-neutral router, 8 Jul the MCP control plane, 9 Jul the deployment-labor market, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe that walks out, 13 Jul govern the goal not the gauge, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age). Today names the layer where the value settles once the metal is cheap: **the triage tent.** On legacy estates the danger is a stack wired to send *every* AI task through one premium model — surgeon rates for log-parsing — with no vantage point that sees, prices, or governs the whole flow. The retrofit is the control plane this radar has urged all fortnight, now aimed at the routing: a **model-neutral router (7 Jul)** so any cheap or open model can serve the mass; a **spend meter (6 Jul)** to prove the triage through to the P&L; and a **governance ledger** so every escalation to the frontier model is logged, eligible, and overseen.

**The clean mental model:** *When the scarce resource becomes abundant, the value moves to the system that decides where the still-costly capacity is spent. Build the triage tent — route the mass to cheap models, reserve the frontier model for where it pays — and make the tent govern as deliberately as it saves.*

### Watch list this week
- **Project Perception (Microsoft)** — reported this weekend (16–19 July, not officially announced): an AI cybersecurity platform to find and fix software vulnerabilities, positioned against **Anthropic's Claude Mythos.** Its defining feature is an **orchestration layer** across **Microsoft, OpenAI and Anthropic** models that routes each step to the cheapest-adequate model and reserves a frontier model for the hardest steps — to make vulnerability fixing **cheap enough to run nonstop.** Pricing, availability and eligibility **not yet finalized or officially confirmed.**
- **The target — Anthropic Claude Mythos** — the frontier security model Anthropic chose not to release publicly (announced 7 Apr 2026), which autonomously surfaced thousands of vulnerabilities (e.g. **271 in Firefox,** exploits for 181; a **27-year-old** OpenBSD flaw). Access is via **Project Glasswing** (scoped defensive access, ~**$100M** in credits, partners incl. AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike, Linux Foundation). **Mythos 5** is listed at **$10 / $50 per 1M tokens,** vetted partners only — the premium ceiling Perception's routing aims to undercut.
- **The regulatory tailwind** — the EU's **Action Plan on Cybersecurity and AI** (presented **7 July 2026**) calls for advanced models to be evaluated before the EU market and for structured, governed access for defenders — pointing straight at this class of orchestrated security tool.
- **The commodity underneath** — **Kimi K3's open weights publish on 27 July (8 days),** the self-hostable floor that makes "route to a cheap/open model" a permanent option no vendor can revoke.
- **The connector counterpart** — **MCP 2026-07-28 spec** goes **final in 9 days** (stateless core, Enterprise-Managed Authorization stable, MCP Apps); the plumbing standardizes as routing becomes the battleground.
- **The mandatory counterweight** — EU AI Act **GPAI enforcement applicable 2 Aug 2026 (14 days)**; €15M or 3% of global turnover (Art. 101); the AI Office can compel documentation (Art. 91), require mitigations (Art. 93) and demand model access (Art. 92).
- **Adoption cadence** — Gartner: 40% of enterprise apps embed task-specific agents by end-2026 (from <5% in 2025); >40% of agentic projects cancelled by end-2027 — governance and value, not model access, remain the constraint.

---

## 5 · Quotes That Catch the Eye

> What sets the design apart is an orchestration layer that chooses which AI model handles each step, rather than sending every job through the most powerful — and most expensive — system.
> — **Coverage of Microsoft's Project Perception**, 17–18 July 2026 (as reported)

> The ability to mix models gives Microsoft a credible lever for controlling expense as usage scales — the difference between a tool reserved for high-severity incidents and one that hums along in the background, day after day.
> — **Coverage of Project Perception**, July 2026 (as reported)

> As frontier AI model capabilities converge, enterprise AI wins or loses at the orchestration layer.
> — **Enterprise-AI commentary**, July 2026 (as reported)

> [Kimi K3 signals] a hyper-competitive future where software intelligence becomes highly accessible, shifting financial power over to the platforms that distribute it and the enterprises that deploy it.
> — **Coverage of the Kimi K3 release**, July 2026 (as reported)

> "When the scarce resource becomes abundant, the value moves to the triage that decides where the still-costly capacity is spent. Own the sorting — and make it govern as well as it saves."
> — *the radar, on the orchestration layer*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Project Perception reported (not officially announced) | **16–19 Jul 2026** | Press coverage (as reported) |
| Model vendors orchestrated (MS / OpenAI / Anthropic) | **3** | Coverage (as reported) |
| Anthropic Mythos 5 price (input / output per 1M) | **$10 / $50** | Coverage (as reported) |
| Mythos vulnerabilities found in Firefox (exploits for 181) | **271** | Coverage (as reported) |
| Oldest flaw Mythos surfaced (OpenBSD) | **27 years** | Coverage (as reported) |
| Project Glasswing defensive access credits | **~$100M** | Coverage (as reported) |
| EU Action Plan on Cybersecurity & AI presented | **7 Jul 2026** | European Commission |
| Kimi K3 full open weights (Modified MIT) publish | **27 Jul 2026 (8 days)** | Moonshot / coverage |
| MCP's largest revision goes final | **28 Jul 2026 (9 days)** | Model Context Protocol blog |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (14 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |
| Enterprise apps embedding task-specific agents by end-2026 | **40%** (from <5% in 2025) | Gartner |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Instrument your AI workloads, then triage them.** Project Perception's whole bet is that most tasks don't need your most expensive model. Before the next model-contract renewal, **tag every AI call by whether it genuinely needs frontier capability** — and route the routine mass (triage, parsing, drafting) to a cheap or, after 27 July, self-hostable open model through your **model-neutral router (7 Jul).** The cost cut is real; the strategic point is that the *triage logic* becomes the asset, not the model.

2. **Make your router govern, not just save.** The orchestration layer is the one place that sees every task and every model choice — so make it enforce policy, not only price. **Wire data-eligibility, logging and human-sign-off checkpoints into the routing itself** (which model may see which data, what's retained, where a human approves), so that the same layer that saves money produces your **EU AI Act evidence.** A cost-only router optimizes spend while building an ungoverned surface the regulator inspects on **2 August.**

3. **Name the layer where your value lives — and defend it.** After Kimi K3 and Project Perception, "we have the best model" is not a moat; the orchestration and the proprietary data and rules that steer it are. **Write down, in one page, your triage tent** — the routing logic, the escalation rules, the data that makes them smart, the audit ledger — and move budget from renting model capability toward compounding *that.* If you can't point to the layer, you're paying surgeon rates for log-parsing and calling it strategy.

---

*AI Tech Radar · generated 19 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The Project Perception details — an AI cybersecurity platform reported (but not officially announced by Microsoft) around 16–19 July 2026, positioned against Anthropic's Claude Mythos, combining models from Microsoft, OpenAI and Anthropic behind an orchestration layer that routes each task to the cheapest-adequate model and reserves a frontier model for the hardest steps, aiming to make vulnerability fixing "cheap enough to run nonstop," with pricing/availability not finalized — are relayed from press coverage (TechRepublic, Windows News, Neowin, Newsbytes, Inshorts and others) and marked "as reported"; Microsoft has not publicly confirmed the product. The Claude Mythos details (announced 7 April 2026 and not released publicly; ~271 Firefox vulnerabilities with exploits for 181; a 27-year-old OpenBSD flaw; Project Glasswing scoped access with ~$100M in credits and partners including AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike and the Linux Foundation; Mythos 5 listed at $10/$50 per million tokens for vetted partners) are relayed from prior coverage (CNBC, Rest of World, Cloud Security Alliance and others) and marked "as reported." The Kimi K3 open-weights date (27 July 2026) is Moonshot AI's, relayed via coverage. The EU Action Plan on Cybersecurity and AI (presented 7 July 2026) and the EU AI Act mechanics (GPAI enforcement applicable 2 August 2026; €15M or 3% of turnover; Articles 91–93, 101) are relayed from the European Commission. The MCP 2026-07-28 final-spec date is the MCP project's. The Gartner figures (40% embed by end-2026; >40% cancelled by end-2027) are Gartner's. The "8 days," "9 days" and "14 days" figures are simple counts from this edition's date (19 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own. The triage allegory — Dominique-Jean Larrey as surgeon-in-chief of Napoleon's Grande Armée, his invention of battlefield triage (from the French "trier," to sort) and the "flying ambulance," and his work at Borodino (1812) — is the radar's own historical illustration, told approximately, and is not a sourced claim about AI.*
