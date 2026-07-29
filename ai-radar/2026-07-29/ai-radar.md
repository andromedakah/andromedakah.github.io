# 🗓️ AI Tech Radar — The Pilot Plant

**Wednesday, 29 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday the universal connector went final and everyone rushed to plug in. Today the sobering counter-arrives: plugging in is not producing. On **28 July, Cognizant launched a dedicated EMEA AI Unit** built around one brutal number — **IDC says 88% of AI-agent proofs-of-concept never reach broad production; for every 33 pilots a company launches, only four go live.** The same day, DoorDash published a rare *how-we-actually-scaled-agents* blueprint, and IBM's Think-2026 data hardened the picture: large enterprises will run **1,600+ agents by year-end,** **70%** say weak governance is *slowing* their transformation, only **18%** keep a complete agent inventory, and just **11%** feel ready for the scale coming. The consistent verdict across all of it: **"the failure is rarely the model — it is almost always the layer around the model."** Cognizant's CEO Ravi Kumar named the whole condition: **"AI capability is rising faster than enterprises can absorb it, and that gap is the defining problem of this moment."** The board's question: ***a beaker full of a beautiful reaction is not a plant — have we built the pilot plant that de-risks scale-up (the process, the evaluation harness, the governance, the control room), or did we call the PoC a win and join the 88% that never ship?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thesis — *the model commoditizes; own and govern the layer around it* — and today the market delivered the receipt. Yesterday MCP's stateless spec went final and the connector became universal, boring, load-bearing. Today the counter-story lands with hard numbers: **the standard is not the plant.** On **28 July, Cognizant launched a dedicated EMEA AI Unit** to attack the single most stubborn statistic in enterprise AI — **IDC's finding that 88% of AI-agent proofs-of-concept never reach broad production; for every 33 pilots launched, only four enter live operation.** The unit is deliberately **platform-, model- and cloud-independent,** delivered through a "Frontier Deployed Engineering" model (Foundation → Accelerate → Transform) — an admission that the hard part is not the model but the scale-up. In the same 24 hours, **DoorDash published a blueprint** for scaling agents — platform architecture, reusable components, an **evaluation harness that went from ~1 employee-submitted feedback to 2,000 auto-graded sessions a day** and cut pre-ship validation from hours to minutes, and centralized data governance so "the wrong table exposed to an agent" doesn't return a confident hallucination. And **IBM's Think-2026 study** (2,000 executives, 33 geographies, 19 industries, surveyed Jan–Apr 2026) put the governance gap in relief: large enterprises will run a digital workforce of **1,600+ AI agents by year-end,** but **seven in ten** say their existing governance is *slowing* the transformation, only **18%** hold a complete inventory of the agents already running, only **12%** have a centralized platform to manage the sprawl, **80%** report a CEO-driven mandate yet only **11%** feel ready — and the average firm logged **54 agent incidents** last year (IBM's own line: *"an unmonitored AI agent with production credentials can delete a database in nine seconds"*). The convergent verdict from the coverage is blunt and it is this radar's month-long refrain in someone else's words: **"the failure is rarely the model — it is almost always the layer around the model,"** and the production gap is **"not a technology gap… [but] a process design gap, a governance sequencing gap, and an evaluation infrastructure gap."** Cognizant's CEO **Ravi Kumar** named the condition whole: **"AI capability is rising faster than enterprises can absorb it, and that gap is the defining problem of this moment."** Meanwhile **Gartner** warns the same absorption gap will get expensive: only **17%** of organizations have fully deployed agents, **60%+** expect to within two years, but **more than 40% of agentic-AI projects will be cancelled by end-2027.** The regulatory clock stays loud — **EU AI Act Article 50 + GPAI enforcement lands 2 August (4 days;** €15M or 3% of turnover). Yesterday's universal connector (MCP), last week's frontier (**Claude Opus 5, #1, $5/$25**) and open-weight commodity (**Kimi K3**) are all beakers full of a beautiful reaction. The plant is what almost nobody has built.

1. **88% of pilots die before production — and not because the reaction failed.** The model works in the beaker; the pilot demos beautifully. What kills it at scale is the layer around it — the process it's bolted onto, the evaluation harness that isn't there, the governance sequencing nobody did. IDC: 33 pilots in, four out. **The scarce asset is scale-up engineering, and it is exactly the layer this radar has told you to own.**

2. **The governance you skipped is now the thing slowing you down.** IBM's inversion is the tell: 1,600+ agents per enterprise by year-end, but **70% say weak governance is *slowing* the transformation** — governance stopped being the brake you resented and became the bottleneck you can't scale past. Only 18% can even inventory their agents; 54 incidents a year is the cost of shipping the reaction without the control room.

3. **Everyone is selling you the pilot plant now — build or rent it, but don't skip it.** Cognizant's platform-neutral unit, DoorDash's home-built harness, IBM's control-gap alarm and Gartner's 40%-cancellation forecast all point one way: the differentiator is the scale-up layer, not the model. **Own it as an asset** (process redesign, eval gate, agent inventory, audit log, orchestration) — because the vendor renting it to you is the one you're meant to stay neutral about, and the 2 August evidence you owe in 4 days lives in exactly this layer.

**Bottom line:** yesterday the connector went universal; today the data says universality doesn't ship product. A pilot proves the *reaction;* only a plant proves the *process* — and 88% of firms are mistaking the first for the second. **Build the pilot plant** — the process, the evaluation harness, the governance, the control room — before you call the PoC a win.

---

## 2 · Allegory of the Day — "The Pilot Plant"

*Topic: On 28 July 2026 Cognizant launched a dedicated EMEA AI Unit built around IDC's finding that 88% of AI-agent proofs-of-concept never reach broad production (for every 33 pilots, only four go live), delivered through a deliberately platform-, model- and cloud-independent "Frontier Deployed Engineering" model. In the same window DoorDash published a blueprint for scaling agents (platform architecture, reusable components, an evaluation harness that grew from ~1 human feedback to 2,000 auto-graded sessions a day, centralized data governance), and IBM's Think-2026 study reported that enterprises will run 1,600+ agents by year-end while 70% say weak governance is slowing them, only 18% keep an agent inventory, and only 11% feel ready. The convergent verdict: "the failure is rarely the model — it is almost always the layer around the model," and the production gap is "a process design gap, a governance sequencing gap, and an evaluation infrastructure gap." Cognizant CEO Ravi Kumar: "AI capability is rising faster than enterprises can absorb it, and that gap is the defining problem of this moment." The lesson for the enterprise: a working pilot proves the reaction, not the process — value lives in the scale-up engineering, the layer you own.*

Every chemical engineer learns the humbling lesson early: **a reaction that works beautifully in a beaker will, more often than not, fail when you try to run it by the ton.** The chemist mixes two reagents in a flask, the yield is 95%, the product is pure, and everyone in the room believes the hard part is done. It isn't. At scale, everything the beaker hid comes for you: heat that dissipated instantly in a flask now cooks the batch from the inside; mixing that was trivial with a stir bar becomes a fluid-dynamics problem; trace impurities that didn't matter in grams poison the catalyst in tons; a runaway that was a warm flask becomes an explosion. This is why industry invented the **pilot plant** — a deliberately small production line, built not to make product cheaply but to *learn how the process breaks* before you commit a factory to it. The word we now use for every tentative first try — a *pilot* — comes from exactly this: the plant you build to prove you can scale, precisely because the lab result never proves it.

Notice what the pilot plant actually is. It is **not the reaction** — the chemistry is the same molecule it always was, and often it's a commodity anyone can buy. The pilot plant is the *engineering around the reaction:* the heat exchangers, the control loops, the sensors and interlocks, the sampling regime that catches a bad batch before it ships, the operating procedure that a shift worker can follow at 3 a.m. without a PhD. It is unglamorous, it is expensive, and it is the entire difference between a promising result and a running business. The lab chemist who skips it — who reads a 95% beaker yield and orders the full factory — is the one whose plant never runs, or runs once and burns. Scale-up has a name in the industry for the place these projects die: **the valley of death,** and the graveyard is enormous. Most lab successes never cross it, and the ones that do cross it on the back of pilot-plant engineering, not on the back of a better molecule.

So read this week honestly. The **reaction is spectacular and increasingly free:** a frontier model at #1 for five dollars, an open-weight colossus you can download, a universal connector that went final yesterday. Everyone has a beaker full of a beautiful reaction, and everyone's PoC demos like a 95% yield. And then **88% of them never reach production** — not because the reaction failed, but because nobody built the pilot plant. The failures are the classic scale-up failures wearing new clothes: **heat with nowhere to go** (an agent bolted onto a broken process just runs the broken process faster); **no sampling regime** (no evaluation harness, so a bad batch ships with full confidence — DoorDash's blunt warning that the wrong table returns a confident hallucination); **no interlocks** (54 incidents a year, a database deleted in nine seconds by an agent with production credentials nobody was watching); **no operating procedure** (1,600 agents and only 18% of firms can even list them). IBM's finding is the tell that this is a scale-up crisis and not a chemistry one: the *governance* — the plant engineering — is now the thing *slowing the reaction down,* because the firms poured the reagents in before they built the vessel to hold them.

**The moral:** a pilot proves the reaction; only a plant proves the process. The molecule — the model — has commoditized, and this radar has argued for a month that value migrates to what you build around it. This week names that "what" precisely: it is the **pilot plant** — the process redesign, the evaluation harness, the control room, the operating procedure, the inventory of what's running. Cognizant is selling it, DoorDash built it, IBM is warning you the reactor is already overpressured, and Gartner is pricing the explosions (40% of these projects cancelled by 2027). Build the plant. Don't be the chemist who read a beaker and ordered a factory.

**The question it forces:** *We have a beaker full of a beautiful reaction — a frontier model, an open weight, a universal connector — and a PoC that demos like a 95% yield. But 88% of pilots like ours never reach production, and the coverage says the failure is the layer around the model, not the model. Have we built the pilot plant — the process, the evaluation harness, the interlocks, the operating procedure, the inventory — or did we mistake a working beaker for a running plant and quietly join the valley of death?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **88% of AI-agent pilots never reach broad production (IDC); for every 33 we launch, four go live.** Of *our* agent pilots, how many are actually in production with a P&L owner — and for the rest, are we in the 88% because the model failed, or because we never built the pilot plant (the process, the evaluation harness, the governance)?
- IBM's inversion is the warning: 1,600+ agents per enterprise by year-end, but **70% say weak governance is *slowing* the transformation,** and only **18%** can inventory the agents already running. **Can we produce a complete list of the agents live inside our walls this week** — and if not, is our governance the brake we resent or the bottleneck we can't scale past?
- Cognizant's CEO calls the absorption gap "the defining problem of this moment," and Gartner says **40%+ of agentic projects will be cancelled by end-2027.** **Are we building the scale-up layer as an owned asset — or renting it, PoC by PoC, from the vendor whose model we're meant to stay neutral about?**

### 🏦 Financial Services
- An agent with production credentials "can delete a database in nine seconds" (IBM), and the average firm logged **54 agent incidents** last year. **For any agent near ledgers, payments or customer accounts, do we have the interlocks — least-privilege credentials, a kill switch, a complete audit log — or a beaker yield we've mistaken for a safe process?**
- The 88% failure is a *process design* gap, not a model gap. **Before we scale an agent, have we fixed the underlying process** — because "layering an agent onto a broken process produces a faster broken process," and in a regulated book that speed is the risk.

### 🧬 Healthcare / Life Sciences
- You already run pilot plants and validated scale-up for a living — GMP exists precisely because a lab result doesn't prove a process. **Apply the same discipline to clinical and research agents: where is the evaluation harness that catches a bad batch (a confident hallucination) before it reaches a clinician?**
- Only 11% of organizations feel ready for the agent scale coming (IBM). **For agents touching patient data or research pipelines, is our governance a validated control room, or paperwork we'll assemble after the incident?**

### 🏭 Manufacturing / Industrials
- Your engineers know the valley of death better than anyone: most lab successes never scale, and the ones that do scale on pilot-plant engineering, not a better molecule. **Are we resourcing the AI "pilot plant" — the process, sensors, interlocks and operating procedure — or funding beakers and expecting a factory?**
- DoorDash's harness turned pre-ship validation from hours to minutes and 1 human check into 2,000 auto-graded sessions a day. **Do we have an owned evaluation harness that measures agent quality at production scale**, or are we shipping on a demo and a hope?

### 🛒 Retail / Consumer
- A storefront agent that demos beautifully and hallucinates a price or a promise at scale is the classic "impurity poisons the batch" failure. **Have we built the sampling regime — automated evals on real sessions — before we point an agent at customers,** with Article 50 disclosure live in 4 days?
- The vendors are all offering to build your scale-up layer now. **Do we own the orchestration, the eval gate and the agent inventory** so adding a connector or swapping a model is a governed change through *our* plant, not a fresh rebuild each time?

### 🏛️ Public Sector / Regulated
- Only 12% of enterprises have a centralized platform to manage agent sprawl, and 18% can inventory their agents. **For citizen-facing services, can we account for every agent, what it can touch, and what it did** — the exact evidence 2 August enforcement will ask for?
- The production gap is a *governance sequencing* gap — the plant must exist before the reagents go in. **Are we standing up the control room (inventory, audit log, human sign-off) before we scale,** or racing a pilot to a headline and inheriting the incident?

---

## 4 · Technical Deep-Dive — Build the Plant, Not Just the Reaction

Read this week as one lesson about **scale-up engineering being the scarce asset,** in three parts — the reaction (the model, now a commodity and not where projects die), the valley of death (why 88% of pilots never cross it, in the coverage's own words), and the pilot plant (the layer you build and own to get to production).

- **The reaction (commodity, and not the failure point).** The molecule keeps getting better and cheaper: **Claude Opus 5** launched #1 at **$5/$25** (24 Jul); **Kimi K3** open weights went live (27 Jul); and yesterday the **MCP 2026-07-28 spec went final,** a stateless, OAuth-aligned universal connector already supported by cloud gateways (AWS's AgentCore Gateway; the Tasks long-running-agent extension was contributed by AWS). None of that is where pilots die. The coverage is emphatic: **"the failure is rarely the model — it is almost always the layer around the model."** The reaction is spectacular. It is also not the product.
- **The valley of death (why 88% never cross it).** IDC: **88% of AI-agent PoCs never reach broad production; 33 pilots in, four out.** The named causes are pure scale-up failure: the gap is **"not a technology gap… [but] a process design gap, a governance sequencing gap, and an evaluation infrastructure gap,"** and **"layering an agent onto a broken process produces a faster broken process."** IBM quantifies the overpressure: **1,600+ agents per enterprise by year-end,** **70%** saying weak governance now *slows* the transformation, **18%** with a complete inventory, **12%** with a central platform, **11%** feeling ready, and **54 agent incidents** on average last year — *"an unmonitored AI agent with production credentials can delete a database in nine seconds."* Gartner prices the graveyard: **40%+ of agentic projects cancelled by end-2027.**
- **The pilot plant (the layer to build and own).** The firms crossing the valley built the plant first. DoorDash's blueprint is the template: **a platform** (reusable components so you don't rebuild the same infrastructure per agent), **an evaluation harness** (from ~1 human check to **2,000 auto-graded sessions/day,** validation hours→minutes — the sampling regime that catches a bad batch), **centralized data governance** (define quality and compute-authorization once, so the wrong table can't return a confident hallucination), and **the control room** (per-agent identity, least privilege, a complete audit log, a kill switch — the interlocks against the nine-second database). Cognizant packages the same as a service — deliberately **platform-, model- and cloud-independent** — because the plant, not the molecule, is the durable asset.

The strategic core: **you don't win by having the reaction; you win by building the plant that scales it.** Everyone has the model now — that's what "commodity" means. What separates the 12% that ship from the 88% that don't is the pilot-plant engineering: the process redesign, the evaluation harness, the governance sequencing, the control room. After this week, "our PoC works" is not a production strategy; *"we built the plant — process fixed, evals at scale, every agent inventoried and interlocked, on infrastructure we own"* is.

```
        THE PILOT PLANT — build the plant, not just the reaction
        A working pilot proves the reaction, not the process.

   ┌─────────────────────────────────────────────────────────┐
   │  THE REACTION — the model (commodity, cheap, not the      │  ✅ SOLVED / RENTABLE
   │  failure point)                                           │
   │  Opus 5 #1 $5/$25 · Kimi K3 open weights · MCP final      │
   │  "the failure is rarely the model"                        │
   └─────────────┬─────────────────────────────────────────────┘
                 │  scale it up →
                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │  THE VALLEY OF DEATH — where 88% of pilots die            │  ⚠ THE REAL GAP
   │  IDC: 33 pilots in → 4 out · not a technology gap:        │
   │  process design · governance sequencing · evaluation      │
   │  IBM: 1,600 agents · 70% governance slows them · 54       │
   │  incidents/yr · "delete a database in nine seconds"        │
   └─────────────┬─────────────────────────────────────────────┘
                 │  cross it on engineering, not a better molecule →
                 ▼
   ┌───────────────────────────────────────┐
   │  BUILD THE PILOT PLANT                 │  the layer to own
   │  process redesign (fix it before you    │  DoorDash template:
   │   automate it) · evaluation harness      │  1 → 2,000 auto-graded
   │   (sampling: catch the bad batch) ·      │  sessions/day; validation
   │   central data governance · control      │  hours → minutes
   │   room (identity, least-priv, audit,     │  Cognizant: platform-,
   │   kill switch — the interlocks)          │  model-, cloud-independent
   └───────────────────────────────────────┘

   TRAP: "the PoC works" → order the factory → join the 88% in the valley.
   WIN : "we built the plant" → process, evals, inventory, interlocks — owned.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — mistake the beaker for the plant | The discipline — build the pilot plant you own |
|---|---|
| "The PoC works" as a production claim | Process fixed, then automated — no faster broken process |
| Ship on a demo and a hope | An evaluation harness that auto-grades real sessions at scale |
| Agents sprawl; nobody can list them | A complete, current inventory of every agent running |
| An agent with prod credentials, unwatched | Least privilege, audit log, kill switch — the interlocks |
| Rent the scale-up layer PoC by PoC | Own the plant — platform-, model-, cloud-independent |

### Why the production gap is a scale-up problem, not an AI problem

Every force this radar tracked all month assumed the leverage was in the *reaction* — a better model, an open weight, a universal connector. This week reframes it: the reaction is solved and cheap, and projects die in *scale-up.* The reassuring reading tempts the trap — "our PoC hit 95%, we're basically in production" — exactly the lab chemist's error that gave the valley of death its name. The coverage says the opposite: the gap is process design, governance sequencing and evaluation infrastructure, none of which the beaker ever tested. A firm that hears "the model works" orders the factory; a firm that reads the failure data builds the pilot plant. The model didn't become less important; it became *insufficient* — necessary reagent, not finished product.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine, 28 Jul the mailroom). The 22 Jul "harvest" warned that a field of pilots is not a harvest; today's data puts a number on the unharvested field — 88% — and names the reason: no pilot plant. On legacy estates the danger is a team that runs a dazzling PoC on a system-of-record it never fixed, declares victory, and scales an agent that now runs the broken process faster, unevaluated and uninventoried, until it becomes one of the 54 incidents. The retrofit is the pilot plant: fix the process first, stand up an evaluation harness on real sessions, inventory and interlock every agent, and wire the whole control room to produce the Article 50 evidence due in 4 days — *before* the scale-up, not after the incident.

**The clean mental model:** *A pilot proves the reaction; only a plant proves the process. The model has commoditized — build and own the pilot plant (process, evaluation, inventory, interlocks), because that is where 88% of projects die and where the surviving 12% win.*

### Watch list this week
- **The production gap, quantified (IDC via Cognizant, 28 Jul).** 88% of AI-agent PoCs never reach broad production; 33 pilots in, four out. Cognizant's new EMEA AI Unit and platform-neutral "Frontier Deployed Engineering" (Foundation/Accelerate/Transform) are built to attack it.
- **The governance inversion (IBM Think-2026).** 1,600+ agents per enterprise by year-end; 70% say weak governance now *slows* transformation; 18% have a complete inventory; 12% a central platform; 11% feel ready; 54 incidents/yr on average.
- **The blueprint (DoorDash, 28 Jul).** Platform + reusable components + an evaluation harness (1 → 2,000 auto-graded sessions/day; validation hours→minutes) + centralized data governance — a rare public template for crossing the valley.
- **The price of not building it (Gartner).** 17% have fully deployed agents; 60%+ expect to within two years; but 40%+ of agentic projects will be cancelled by end-2027.
- **The standing plumbing — EU AI Act Article 50 + GPAI enforcement 2 August (4 days;** €15M or 3% of turnover) — atop yesterday's final **MCP 2026-07-28 spec** and the frontier/open-weight reactions (**Claude Opus 5** #1 $5/$25; **Kimi K3** open weights) that make the beaker cheap and the plant scarce.

---

## 5 · Quotes That Catch the Eye

> AI capability is rising faster than enterprises can absorb it, and that gap is the defining problem of this moment.
> — **Ravi Kumar S**, CEO, Cognizant, on the enterprise AI value gap, July 2026 (as reported)

> The failure is rarely the model. It is almost always the layer around the model.
> — **Enterprise-AI coverage of the production gap**, July 2026 (as reported)

> [The production gap] is not a technology gap. It is a process design gap, a governance sequencing gap, and an evaluation infrastructure gap.
> — **Analysis of why agent pilots fail in production**, July 2026 (as reported)

> An unmonitored AI agent with production credentials can delete a database in nine seconds.
> — **IBM**, Think-2026 study on the AI control gap, 2026 (as reported)

> "A pilot proves the reaction; only the plant proves the process. Own the scale-up."
> — *the radar, on the 88% production gap*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| AI-agent PoCs that never reach broad production | **88%** | IDC (via Cognizant, as reported) |
| Pilots-to-production ratio | **33 launched → 4 live** | IDC (via Cognizant, as reported) |
| Cognizant EMEA AI Unit — launched | **28 Jul 2026** | Cognizant |
| Cognizant delivery model | **Frontier Deployed Engineering (Foundation/Accelerate/Transform), platform-/model-/cloud-independent** | Cognizant |
| AI agents per large enterprise by year-end 2026 | **1,600+** | IBM Think-2026 (as reported) |
| Execs saying weak governance is *slowing* AI transformation | **70% (7 in 10)** | IBM Think-2026 (as reported) |
| Orgs with a complete, current agent inventory | **18%** | IBM Think-2026 (as reported) |
| Orgs with a centralized platform to manage agent sprawl | **12%** | IBM Think-2026 (as reported) |
| Orgs feeling ready for the agent scale coming | **11%** | IBM Think-2026 (as reported) |
| Average AI-agent incidents per org last year | **54** | IBM Think-2026 (as reported) |
| Orgs with fully deployed AI agents | **17%** | Gartner 2026 CIO survey (as reported) |
| Agentic-AI projects to be cancelled by end-2027 | **40%+** | Gartner (as reported) |
| DoorDash evaluation harness — quality signal | **~1 → 2,000 auto-graded sessions/day; validation hours → minutes** | DoorDash (as reported) |
| Claude Opus 5 — launch rank / pricing | **#1 · $5 / $25 per 1M tokens** | Anthropic / Artificial Analysis (as reported) |
| Kimi K3 full open weights — live | **27 Jul 2026** | Moonshot / coverage |
| MCP 2026-07-28 final spec — live | **28 Jul 2026 (yesterday)** | MCP blog / coverage |
| EU AI Act Article 50 + GPAI enforcement | **2 Aug 2026 (4 days) · €15M or 3%** | European Commission |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Audit the beakers: which pilots are actually in production, and why the rest aren't.** Pull every agent PoC into one table — in-production (with a P&L owner) vs. stalled — and for each stalled one, tag the *scale-up* cause: broken process, no evaluation harness, no governance sequencing, no owner. IDC says four in 33 make it; find out why yours are or aren't, and stop funding beakers you have no intent to scale.

2. **Build the evaluation harness and the agent inventory this month — they are your 2 August evidence.** Copy DoorDash's move: stand up automated evals on *real* sessions (the sampling regime that catches a confident hallucination before it ships), and produce a complete, current inventory of every agent running, what it can touch, and what it did. Only 18% of firms can do the second today; it is exactly the evidence Article 50 and GPAI enforcement ask for in 4 days.

3. **Own the pilot plant — don't rent scale-up PoC by PoC.** The vendors are all selling the scale-up layer now (Cognizant's platform-neutral unit is the signal). Take the help, but build the plant as an *owned, model-neutral asset:* the platform of reusable components, the eval gate, the central data governance, the control room (per-agent identity, least privilege, audit log, kill switch). Then swapping models (Opus 5, Kimi K3, whatever ships next) or connectors (MCP) is a governed change through *your* plant — not a fresh trip through the valley of death.

---

*AI Tech Radar · generated 29 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The reported facts are relayed from Cognizant's 28 July EMEA AI Unit announcement and related coverage (citing IDC), IBM's Think-2026 AI-control-gap study, DoorDash's engineering blueprint as relayed via July 2026 coverage, Gartner, and market reporting, and are marked "as reported" where they rest on secondary reporting. The IDC production-gap figures (88% of AI-agent proofs-of-concept never reach broad production; for every 33 pilots, four enter live operation) are relayed via Cognizant's 28 July 2026 announcement of its EMEA AI Unit and associated press coverage as reported; Cognizant's "Frontier Deployed Engineering" delivery model (service tiers Foundation, Accelerate, Transform) and the unit's platform-/model-/cloud-independence are from Cognizant's announcement. The IBM figures (a digital workforce of 1,600+ AI agents per large enterprise by year-end 2026; seven in ten executives saying existing governance is slowing their AI transformation; 18% maintaining a complete, current agent inventory; 12% with a centralized platform to manage agent sprawl; 80% reporting CEO-driven mandates; 11% feeling fully ready; an average of 54 agent incidents last year; and the line that "an unmonitored AI agent with production credentials can delete a database in nine seconds") are from IBM's Think-2026 study — a survey of ~2,000 senior technology and AI decision-makers across 33 geographies and 19 industries conducted January–April 2026 — as relayed via July 2026 coverage as reported. The characterizations that "the failure is rarely the model — it is almost always the layer around the model" and that the production gap is "a process design gap, a governance sequencing gap, and an evaluation infrastructure gap," and that "layering an agent onto a broken process produces a faster broken process," are relayed from July 2026 enterprise-AI coverage of the production gap as reported and are not attributed to any single named author. The DoorDash figures (an evaluation harness that expanded the quality signal from roughly one employee-submitted feedback to 2,000 auto-graded sessions per day, reducing pre-ship validation from hours to minutes, and centralized data-governance discipline) are from DoorDash engineering material as relayed via July 2026 coverage as reported. The Gartner figures (17% of organizations have fully deployed AI agents; 60%+ expect to within two years; more than 40% of agentic-AI projects will be cancelled by the end of 2027) are relayed from Gartner research and coverage as reported. Ravi Kumar S's quotation ("AI capability is rising faster than enterprises can absorb it, and that gap is the defining problem of this moment") is relayed from July 2026 coverage of Cognizant's AI strategy as reported. Claude Opus 5 (release 24 July 2026, #1 at launch, $5/$25 per million tokens), Kimi K3 (full open weights live 27 July 2026), and the MCP 2026-07-28 specification going final on 28 July 2026 are relayed from July 2026 coverage as reported; the EU AI Act Article 50 / GPAI enforcement date (2 August 2026; €15M or 3% of global annual turnover) is from the European Commission. The "4 days" figure is a simple count from this edition's date (29 July 2026) to 2 August 2026 and is the radar's own. The pilot-plant allegory — the chemical-engineering reality that a reaction proven in a beaker routinely fails at industrial scale, that industry builds pilot and demonstration plants to de-risk scale-up before committing a factory, that most lab successes never cross the "valley of death," and that the durable value lies in the scale-up engineering (process design, control systems, sampling and operating procedures) rather than in the reaction itself — is the radar's own illustration, told approximately, and is not a sourced claim about any specific plant, firm or product.*
