# 🗓️ AI Tech Radar — The Waterworks

**Sunday, 9 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> For a month this radar has said the same thing in a dozen costumes: the model is a commodity, so own the layer around it. This week fitted the controls for that layer — the airlock (6 Aug), the keyring (7 Aug), the proving ground (8 Aug). Today the ground shifts under all of them. The industry just crossed a line it will not cross back: **2026 is the first year the world spends more compute *running* AI than *training* it.** AMD's Lisa Su, at the company's largest event of the year, put a number on it — the industry now processes **roughly 35 quadrillion tokens a month, about 160× more than two years ago, with inference now around 60% of compute** — and Deloitte's 2026 predictions put inference at **about two-thirds of all AI compute**, up from a third in 2023. Goldman Sachs says the meter is only warming up: **token demand is forecast to multiply ~24× to 120 quadrillion tokens a month by 2030.** The dam-building era — who trains the biggest model — is ending; the **waterworks era** — who runs and governs the flow, cheaply and safely, at every tap — has begun. The board's question this morning: ***we spent two years asking who has the tallest dam; our bill now comes from the water running through our taps, and it is set to multiply twenty-fold — do we own our waterworks, or are we about to be metered to death on someone else's?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thing: the model is a commodity, so the durable advantage is the **layer you own around it.** This week made that concrete with controls — the airlock at the door your data leaves through (6 Aug), the keyring to everything your agents may reach (7 Aug), the proving ground where you validate them before go-live (8 Aug). Today the argument gets its macro proof. The AI economy has quietly flipped from a **buildout** to a **run-rate:** **2026 is the first year global inference compute surpasses training compute,** the moment the money stops being about *making* the model and starts being about *running* it — and running it is now the bill that grows every quarter you succeed.

**The crossover, in numbers.** At AMD's flagship event, **Lisa Su** framed 2026 as a historical milestone: **inference compute now exceeds training** for the first time, the industry runs **~35 quadrillion tokens a month (≈160× two years ago),** and **~60% of capacity is inference,** driven by agentic AI. Deloitte's 2026 TMT Predictions put inference at **~two-thirds of all AI compute** (up from ~33% in 2023 and ~50% in 2025), with an **inference-optimized chip market above $50B in 2026.** And this is the near-empty end of the curve: **Goldman Sachs forecasts token demand multiplying ~24× to 120 quadrillion tokens a month by 2030** — with the current run-rate already ahead of its own May-2026 model. The demand behind the meter is visible in the P&Ls: **OpenAI says enterprise is now >40% of its revenue,** on track to reach parity with consumer by year-end, as customers deploy "teams of agents," and its APIs process **>15 billion tokens a minute.**

**Why it matters more than a compute headline.** A buildout is a capital project a few labs finance and you rent; a run-rate is an **operating expense you carry, metered by the token, that scales with your success, not against it.** That inverts where advantage lives. In the dam-building years the question was "whose model is biggest"; in the waterworks years it is "**whose inference is cheapest, fastest, and safest per token of business value.**" The model stays rented and swappable — Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731. What you own — or fail to own — is the **waterworks:** routing, caching, batching, the small-model/large-model split, and the airlock-keyring-proving-ground controls that keep the flow clean. Anthropic's 2026 State of AI Agents report says **80% of organizations now report measurable ROI** from agents; the ones who keep it are the ones whose unit economics survive a 24× rise in throughput.

1. **The era changed, not just the chart.** Value is migrating from the **capital-intensive buildout** (training, owned by a few, rented by all) to the **operational layer** (inference, run by everyone). "Who has the best model" is last era's question; "who runs the flow cheapest and cleanest per unit of value" is this era's. Own the waterworks, rent the reservoir.

2. **Your AI cost just became opex that grows with success.** A pilot is cheap; a *successful* pilot at 24× throughput is the bill that kills projects. With inference already ~two-thirds of compute and ~55% of cloud AI spend, and demand forecast to multiply ~24× by 2030, **the token line is now a first-class P&L item** — model it before you scale, not after.

3. **The controls only pay off if the flow is metered and governed.** The airlock, keyring and proving ground presume a pipe you can see, price and shut. In the waterworks era, **unit economics and governance are the same discipline:** an unmetered, ungoverned flow is both a runaway bill and an uncontained risk. Meter every tap, or the era's growth curve becomes your loss curve.

**Bottom line:** the month said *own the layer around the commodity model.* Today the whole market proved why: the buildout is over, the run-rate has begun, and **the bill has moved from the dam you rent to the water you pump.** Rent the reservoir — it is cheaper every quarter and never your moat. **Own the waterworks:** the routing, caching and small-model splits that make a token cheap; the meter that turns a mystery bill into a managed one; and the airlock, keyring and proving ground that keep the flow clean — because in a year the world crossed into inference-first and token demand is set to rise twenty-fold, the enterprises that thrive are the ones metered by design, not by surprise.

---

## 2 · Allegory of the Day — "The Waterworks"

*Topic: 2026 is the first year global inference compute surpasses training compute. At AMD's flagship 2026 event, CEO Lisa Su framed it as a historical milestone: the industry now processes roughly 35 quadrillion AI tokens a month — about 160× the volume of two years ago — with inference now accounting for around 60% of compute, a shift she attributed to the rise of agentic AI. Deloitte's 2026 TMT Predictions estimate inference at about two-thirds of all AI compute in 2026 (up from ~33% in 2023 and ~50% in 2025), with the inference-optimized chip market exceeding $50 billion in 2026. Goldman Sachs forecasts AI token demand multiplying roughly 24× to about 120 quadrillion tokens a month between 2026 and 2030, with a 2028 waypoint near 47 quadrillion and a current run-rate already running ahead of its May-2026 estimate. OpenAI says enterprise is now more than 40% of its revenue, on track to reach parity with consumer by end-2026 as customers deploy "teams of agents," with its APIs processing more than 15 billion tokens a minute. Anthropic's 2026 State of AI Agents report finds 80% of organizations reporting measurable ROI from agents. Inference is estimated to be roughly 55% of cloud AI spending in 2026. The lesson: the training buildout — who owns the biggest model — is a capital project a few labs finance and everyone rents; the inference run-rate — who runs the flow cheapest, fastest and cleanest per token of business value — is an operating expense the enterprise carries and must own. The waterworks allegory — a city that spent years raising a great dam, only to discover its fortune now turns on the water metered through every tap — is the radar's own illustration.*

Picture a city that spent a decade and a fortune raising a **great dam.** It was the wonder of the age: everyone measured a city's greatness by the height of its dam, and the newspapers ran the numbers every season — this city's wall a little taller than that one's, the reservoir behind it a little deeper. Fortunes were staked on the masonry. And it was not vanity; a city with no reservoir has no water at all. But a reservoir, however vast, waters no one while it merely *sits* behind the wall. It matters only when the water **runs** — through the mains, down the pipes, out of ten thousand taps into kitchens and workshops and hospital wards. For years the city could pretend otherwise, because so little water was actually flowing that the dam was the only thing worth talking about. This is the year the pretence ended. This is the year the city, for the first time, spent **more of its effort moving water through the taps than raising the wall.**

And the water is *running* now. The city waterman — call him Su of the great foundry — stood up at the year's great gathering and read out the meter: the mains now carry something on the order of **thirty-five thousand-thousand barrels a month, near enough a hundred-and-sixty times what they carried two years ago,** and **three barrels in five now go to the taps, not the reservoir.** The city's own accountants (the ones from the house of Deloitte) confirmed it: **two of every three buckets of effort now go to the flow, not the wall,** where three years back it was one in three. And the bankers — Goldman's people, who are paid to see around corners — warned that this is the near-dry end of the curve: on their reckoning the flow will **multiply some twenty-four-fold by the decade's end.** The great trading houses already feel it in their ledgers: one of them (call it the house of the Open Door) reports that **more than two of every five coins it now takes come from the workshops, not the households** — because the workshops have started running *teams* of tireless water-drinking machines, and a machine never closes the tap.

Here is the turn the wise city sees and the proud one misses. In the dam-building years, greatness was **capital:** you raised the wall once, and the wall was the moat, and only a handful of cities could afford one — so everyone else *rented* their water from those that could. Renting the reservoir was never the shame; it was the sense — you would no sooner build your own dam than mint your own coin. But a rented reservoir is exactly why the **waterworks** — the pumps, the mains, the valves, the meters, the filters at every tap — is the part that is *yours,* and the part on which your whole fortune now turns. Because the flow is metered by the barrel, and the barrels are about to multiply twenty-fold, the city that thrives is not the one with the tallest rented wall but the one whose waterworks **wastes nothing:** no leaks in the mains, the right pressure at each tap and no more, the cheap local spring used for the washing and the deep reservoir kept for the drinking, a **meter on every tap so no workshop's bill is a mystery,** and a **filter and a shut-off valve** on the line so that what runs to the ward is clean and can be stopped in a heartbeat. The proud city, still admiring its wall, wakes to a water bill it never metered and cannot explain — and discovers, too late, that success was the thing that drowned it, because every new workshop it opened only opened more taps.

**The moral:** for a decade the world asked *whose dam is tallest,* and it was the right question for a decade — a city with no reservoir has no water. But the reservoir is rented now, cheaper every season, and never again your moat; the fortune has moved to the **flow.** The wise city rents the reservoir without shame and **owns its waterworks** — meters every tap, fixes every leak, filters and valves every line — so that when the water multiplies twenty-fold the growth is a fortune and not a flood. Rent the reservoir; **own the pumps, the meters and the valves,** because in the year the world began spending more to move the water than to raise the wall, the bill stopped coming from the masonry and started coming, barrel by metered barrel, from your own taps.

**The question it forces:** *Our AI spend has quietly flipped from a thing we build to a thing we run — metered by the token, growing with every agent we ship, and forecast to multiply many times over. Do we actually own our waterworks — do we know our cost per token, route cheap work to cheap models, cache and batch what we can, and meter and govern every tap — or are we still staring at whose model is biggest while the water bill runs, unmetered, toward a number our success alone will make ruinous?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **Do we know our cost per token — and per unit of business value?** 2026 is the first inference-first year; inference is ~two-thirds of AI compute and demand is forecast to multiply ~24× by 2030. **Is our AI spend modelled as a scaling operating expense, or still booked as a one-off pilot cost that will surprise us at volume?**
- The advantage moved from the dam to the flow. **Are we still competing on "whose model is biggest" — or on whose inference is cheapest, fastest and cleanest per token: routing, caching, batching, and the right small-model/large-model split?**
- Growth is the risk here. **If a successful pilot's throughput rose 20×, would our unit economics still work — or would our own success be the thing that makes the project uneconomic?**

### 🏦 Financial Services
- Every scoring, fraud and advice agent is a tap that runs on real customer volume. **Do we price each agent by tokens-per-decision, and have we set a cheaper model for the routine calls and the frontier model only for the hard ones — or is every query paying frontier rates?**
- Inference is also where the regulated data flows. **Is every metered tap also a governed one — airlock on egress, keyring on access — so the cost meter and the compliance meter are the same meter?**

### 🧬 Healthcare / Life Sciences
- Clinical and triage agents cannot trade safety for a cheaper token, but they can waste tokens badly. **Have we separated the cheap, high-volume work (summarisation, intake) from the costly, careful work (decision support) so we neither overpay nor under-verify?**
- Throughput is coming whether budgeted or not. **If patient-facing agents scaled to every clinic, is our inference cost per encounter known and survivable — or discovered on the invoice?**

### 🏭 Manufacturing / Industrials
- Line-side and supply-chain agents run continuously — the definition of a running tap. **Do we run inference where it is cheapest and closest (edge, local, batched) for the always-on work, and reserve the deep reservoir for the exceptions?**
- Engines keep getting cheaper. **When we swap the model under a running agent, do we re-benchmark cost *and* quality per token — or assume last quarter's economics still hold for this quarter's engine?**

### 🛒 Retail / Consumer
- Recommendation, search and support agents are the highest-volume taps in the building. **At peak, do we know the token cost of serving one shopper — and does caching and a small-model tier keep it from scaling linearly with traffic?**
- Success is the stress test. **On the busiest day of the year, does our inference bill rise with revenue or faster than it — and which one have we actually measured?**

### 🏛️ Public Sector / Regulated
- Citizen-service agents must be both affordable and accountable at scale. **Is every token both metered (for the public purse) and governed (for the public trust) — or are we scaling a service whose cost and whose risk are equally unmeasured?**
- Budgets are annual; token demand is not. **Have we modelled a multi-year inference run-rate against a fixed budget — or will the twenty-fold curve meet a flat line and stall the service?**

---

## 4 · Technical Deep-Dive — Rent the Reservoir, Own the Waterworks

Read this month as one argument reaching its proof. The airlock (6 Aug) governs **egress;** the keyring (7 Aug) governs **access;** the proving ground (8 Aug) governs **pre-production validation.** Each is a control you own around a rented model. Today the market shows *why the whole thesis holds:* the economics themselves have moved from the model to the layer around it. The AI economy crossed from a **buildout** (train the biggest model — capital, concentrated, rented) to a **run-rate** (serve the tokens — operating expense, distributed, yours). The architecture splits cleanly into three: the **reservoir** (the rented, swappable model), the **waterworks** (the inference layer you own — routing, caching, metering, governance), and the **flood you must plan for** (a demand curve forecast to multiply ~24×).

- **The reservoir — the commodity engine (rented, swappable).** The menu is unchanged and cheaper by the week — **Claude Opus 5** (#1, Intelligence Index 61 / Agentic Index 55.3, $5/$25), **Gemini 3.6 Flash**, **GPT-5.6 Sol**, **Kimi K3**, **DeepSeek V4-Flash-0731** (MIT). Renting it is not the shame; it is the sense. But the reservoir is not where the money is any more, and it was never your moat. In an inference-first year, a bigger reservoir does not lower your water bill — only a better waterworks does.
- **The waterworks — the inference layer (where the advantage moved).** This is the part you own or fail to own: **model routing** (cheap model for routine calls, frontier model only for the hard ones), **caching** (never pay twice for the same answer), **batching and quantisation** (more tokens per watt), **the small-model/large-model split** at the edge and in the core, and — inseparable from all of it — the **meter** on every tap and the **airlock, keyring and proving ground** that keep the flow clean. Lisa Su's milestone (**inference now exceeds training; ~35 quadrillion tokens/month, ~160× in two years, ~60% of capacity**) and Deloitte's **~two-thirds of AI compute** are not trivia; they are the reason this layer, not the model, is now the P&L.
- **The flood you must plan for — the demand curve.** Goldman Sachs forecasts token demand multiplying **~24× to 120 quadrillion tokens/month by 2030,** with a **2028 waypoint near 47 quadrillion** and a current run-rate already ahead of its May-2026 model. OpenAI's enterprise revenue crossing **>40%** on "teams of agents," and **>15 billion tokens/minute** through its APIs, is the same wave landing on P&Ls. The point that matters: **your inference bill scales with your success,** so a waterworks that wastes nothing at 1× may drown you at 24×. Plan the flood before it arrives.

The strategic core: **the model is the reservoir; the waterworks is where you earn — or lose — the margin on every token.** For a month the misread has been "own a great model and you have won." After this week the read is sharper: **the model is rented and getting cheaper, and the fortune has moved to the flow.** "We use the best model" is not the answer to "will this scale profitably and safely"; ***"we route, cache and meter every token, and we govern every tap"*** is the answer.

```
        THE WATERWORKS — rent the reservoir, own the flow
        2026: first year the world spends more compute RUNNING models than TRAINING them.
        Inference ≈ two-thirds of AI compute · token demand forecast ~24× by 2030.

   ┌──────────────────────────────┐            ┌──────────────────────────────┐
   │  THE RESERVOIR — rented model │            │  THE TAPS — production        │
   │  Opus 5 · Gemini 3.6 Flash ·  │            │  every agent · every request  │
   │  GPT-5.6 Sol · Kimi K3 ·      │            │  metered by the token         │
   │  DeepSeek V4-Flash (MIT)      │            │  the bill scales with success │
   │  cheaper every week · not the moat         └───────────────▲──────────────┘
   └───────────────┬──────────────┘                            │ clean, cheap flow
                   │ water in                                   │ out to every tap
                   ▼                                            │
   ┌───────────────────────────────────────────────────────────┴──────────────┐
   │  THE WATERWORKS — the inference layer you OWN                              │
   │  → ROUTE: cheap model for routine, frontier only for the hard             │
   │  → CACHE + BATCH: never pay twice · more tokens per watt                   │
   │  → METER every tap: cost per token = a first-class P&L line               │
   │  → GOVERN: airlock (egress) · keyring (access) · proving ground (pre-prod) │
   │  the cost meter and the compliance meter are the SAME meter                │
   └───────────────────────────────────────────────────────────────────────────┘

   PLAN FOR THE FLOOD: Su/AMD ~35 quadrillion tokens/mo (~160× in 2yr, ~60% inference) ·
   Deloitte ~two-thirds of compute · Goldman ~24× by 2030 (120q/mo) · OpenAI enterprise >40%.

   TRAP: admire the tallest dam → ship agents → discover an unmetered flood of a bill.
   WIN : rent the reservoir → own the waterworks → meter every tap → grow without drowning.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — admire the dam, drown in the flow | The discipline — own the waterworks |
|---|---|
| Compete on "whose model is biggest" | Compete on cost, speed and safety per token of value |
| One flat model for every call, at frontier rates | Route: cheap model for routine, frontier for the hard |
| Pay again for every repeated answer | Cache and batch — never pay twice, more tokens per watt |
| AI cost booked as a one-off pilot expense | Cost per token as a first-class, scaling P&L line |
| Cost meter and risk controls run separately | One metered, governed tap — cost and compliance together |

### Why owning the flow beats owning a bigger reservoir

Every control this month presumed a pipe you can see, price and shut. The inference crossover is what makes that pipe the whole business. A bigger model does not cut your token bill; a better waterworks does. And the reason the meter and the governance belong together is structural: an unmetered flow is a runaway cost *and* an ungoverned one — the same tap that hides a $2M surprise hides the prompt that should never have left. Route, cache and meter, and the airlock–keyring–proving-ground controls stop being a compliance tax and start being the thing that makes the flow both cheap and clean. The correct read of this week is not "AMD sold more chips" but "**the advantage in AI just moved from the model you rent to the flow you run** — so own the flow."

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine, 28 Jul the mailroom, 29 Jul the pilot plant, 30 Jul the commonplace book, 31 Jul the last mile, 1 Aug the tide table, 2 Aug the loose cannon, 3 Aug the customs house, 4 Aug the two windows, 5 Aug the dark warehouse, 6 Aug the airlock, 7 Aug the keyring, 8 Aug the proving ground). This week fitted the controls; today shows the economics that make them the business. On legacy estates the temptation is to keep every call on one flat frontier model because it is simplest — the retrofit is specific and unglamorous: **instrument the meter first** (cost per token, per agent, per unit of business value — you cannot manage a flow you cannot read); **route** the routine, high-volume calls to a cheaper model and reserve the frontier reservoir for the hard ones; **cache and batch** relentlessly so you never pay twice; **put the meter and the governance on the same tap** so cost and compliance are one dashboard, not two; and **model the flood** — re-run your unit economics at 10× and 24× throughput before you scale, not after the invoice. Then be honest about the wall: a bigger rented model is not a cost strategy, and "we use the best model" is not an answer to "will this scale profitably."

**The clean mental model:** *The model is the reservoir — rented, swappable, cheaper every quarter, and never your moat. The waterworks is yours to own: the routing, caching, batching and small-model splits that make a token cheap; the meter that turns a mystery bill into a managed line; and the airlock, keyring and proving ground that keep the flow clean and stoppable. The world crossed into inference-first this year, and the water is forecast to multiply twenty-fold — so rent the reservoir and own the waterworks, or be metered to death on someone else's.*

### Watch list this week
- **The crossover — inference now exceeds training.** **Lisa Su (AMD)** framed 2026 as the first year global **inference compute surpasses training;** the industry runs **~35 quadrillion tokens/month (~160× in two years),** with **~60% of capacity on inference,** driven by agentic AI. **Deloitte 2026 TMT:** inference **~two-thirds of AI compute** (from ~33% in 2023, ~50% in 2025); inference-chip market **>$50B in 2026.**
- **The flood — demand is far from peaking.** **Goldman Sachs:** token demand multiplying **~24× to 120 quadrillion tokens/month by 2030** (2028 waypoint ~47q); current run-rate already ahead of its May-2026 estimate. Inference is **~55% of cloud AI spending in 2026.**
- **The P&L signal — enterprise is the buyer.** **OpenAI:** enterprise now **>40% of revenue,** on track to consumer parity by year-end, on "teams of agents"; APIs process **>15 billion tokens/minute.** **Anthropic 2026 State of AI Agents:** **80% report measurable ROI;** 57% run multi-stage workflows; 81% plan to expand.
- **The controls — why they compound here.** Meter + govern the same tap: airlock (egress, 6 Aug), keyring (access, 7 Aug), proving ground (pre-prod, 8 Aug). Unmetered flow = runaway cost *and* uncontained risk.
- **The regulatory backdrop — still live.** EU AI Act GPAI enforcement running since **2 Aug;** AI Office powers; **€15M or 3%.** The governed tap and the metered tap are increasingly the same requirement.
- **The engine, for context.** Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 (MIT) — the rented, swappable reservoir. Own the waterworks, not the wall.

---

## 5 · Quotes That Catch the Eye

> 2026 marks a historical milestone: for the first time, global inference compute is set to surpass training compute — the industry now runs on the order of 35 quadrillion tokens a month, roughly 160× two years ago, with the majority of capacity now inference, driven by agentic AI.
> — **Lisa Su, Chair & CEO, AMD**, at the company's 2026 flagship event (as reported)

> AI token demand is forecast to multiply roughly 24× — to about 120 quadrillion tokens a month — between 2026 and 2030 as agents move into production.
> — **Goldman Sachs Research** (as reported)

> Enterprise is now more than 40% of our revenue and on track to reach parity with consumer by the end of the year, as customers move to teams of agents that coordinate and take action inside their tools.
> — **OpenAI**, "The next phase of enterprise AI" (as reported)

> "The model is the reservoir — rented, swappable, cheaper every quarter, never your moat. The waterworks is yours: route, cache and meter every token, and govern every tap, because in an inference-first year the bill comes from the water, not the wall."
> — *the radar, on the inference era*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Inference vs training compute, 2026 | **First year inference compute surpasses training** | AMD / Lisa Su (as reported) |
| Monthly AI token volume | **~35 quadrillion tokens/month (~160× in two years)** | AMD / Lisa Su (as reported) |
| Inference share of capacity | **~60% (AMD); ~two-thirds of AI compute (Deloitte)** | AMD / Deloitte 2026 TMT Predictions (as reported) |
| Inference share of compute over time | **~33% (2023) → ~50% (2025) → ~66% (2026)** | Deloitte 2026 TMT Predictions (as reported) |
| Inference-optimized chip market, 2026 | **>$50B** | Deloitte 2026 TMT Predictions (as reported) |
| Token-demand forecast, 2026→2030 | **~24× to ~120 quadrillion tokens/month (2028 ~47q)** | Goldman Sachs Research (as reported) |
| Inference share of cloud AI spending, 2026 | **~55%** | Analyst coverage (as reported) |
| OpenAI enterprise revenue share | **>40% of revenue; on track to consumer parity by end-2026** | OpenAI (as reported) |
| OpenAI API throughput | **>15 billion tokens/minute** | OpenAI (as reported) |
| Organizations reporting measurable agent ROI | **~80%** (57% run multi-stage workflows; 81% plan to expand) | Anthropic, 2026 State of AI Agents (as reported) |
| EU AI Act — enforcement & penalties | **GPAI enforcement live 2 Aug; €15M or 3% (€7.5M or 1.5% for incorrect info)** | European Commission (as reported) |
| The engine (context) | **Opus 5 · Gemini 3.6 Flash · GPT-5.6 Sol · Kimi K3 · DeepSeek V4-Flash-0731 (MIT)** | Vendor / model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Instrument the meter before you scale a single agent further.** You cannot manage a flow you cannot read. Stand up cost-per-token telemetry **per agent and per unit of business value,** and re-run every production and near-production agent's unit economics at **10× and 24× throughput** — the curve the whole market is now on. Report one number to the board: *our fully-loaded inference cost per unit of business value, and where it lands if this workload's throughput rises twenty-fold.* The projects that belong in the cancelled column will show themselves here, cheaply, before the invoice does.

2. **Build the waterworks: route, cache, and split the reservoir.** Stop paying frontier rates for routine work. Put a **router** in front of your agents (cheap model for the common calls, frontier reservoir only for the hard ones), **cache** repeated answers so you never pay twice, **batch and quantise** the always-on work, and push high-volume, low-stakes inference to the **cheapest, closest** place it can safely run. The model stays rented and swappable — Opus 5 for Gemini or GPT-5.6 as the price/quality moves — so keep the waterworks model-neutral and re-benchmark **cost *and* quality per token** on every swap.

3. **Put the meter and the governance on the same tap.** In the waterworks era, unit economics and safety are one discipline: an unmetered flow is a runaway bill *and* an uncontained risk. Wire your cost meter to the same control points you fitted this week — the **airlock** (egress), the **keyring** (access), the **proving ground** (pre-production) — so one dashboard shows what each tap costs *and* whether it is clean. Then demand the same of every vendor and every model you rent: *show me the per-token cost, the routing, and the governance* — because in the year the world crossed into inference-first and demand is set to rise twenty-fold, the enterprises that thrive are the ones metered and governed by design, not the ones still measuring the height of a wall they rent.

---

*AI Tech Radar · generated 9 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The inference-crossover details (that 2026 is the first year global inference compute is set to surpass training compute; that AMD CEO Lisa Su, at the company's 2026 flagship event, characterized monthly AI token processing as roughly 35 quadrillion tokens — about 160× the volume of two years earlier — with inference accounting for around 60% of capacity and the shift driven by agentic AI) are relayed from AMD event coverage and analyst and press reporting as reported. The compute-share and chip-market figures (that Deloitte's 2026 Technology, Media & Telecommunications Predictions estimate inference at about two-thirds of all AI compute in 2026, up from roughly 33% in 2023 and 50% in 2025, and that the inference-optimized chip market will exceed $50 billion in 2026) are relayed from Deloitte's 2026 TMT Predictions and secondary coverage as reported. The token-demand forecast (that Goldman Sachs Research projects AI token demand multiplying roughly 24× to about 120 quadrillion tokens a month between 2026 and 2030, with a 2028 waypoint near 47 quadrillion and a current run-rate ahead of its May-2026 estimate) is relayed from Goldman Sachs Research and press coverage as reported. The estimate that inference is roughly 55% of cloud AI spending in 2026 is relayed from analyst coverage as reported. The OpenAI figures (that enterprise is now more than 40% of OpenAI's revenue and on track to reach parity with consumer by end-2026 as customers deploy "teams of agents," with APIs processing more than 15 billion tokens a minute) are relayed from OpenAI's "The next phase of enterprise AI" and press coverage as reported. The adoption figures (that Anthropic's 2026 State of AI Agents report finds about 80% of organizations reporting measurable ROI, 57% running multi-stage agent workflows, and 81% planning to expand) are relayed from Anthropic's 2026 State of AI Agents report and secondary coverage as reported. The EU AI Act enforcement facts (GPAI enforcement live from 2 August 2026; the penalty ceiling of the higher of €15 million or 3% of worldwide annual turnover, and €7.5 million or 1.5% for incorrect information) are relayed from the European Commission as reported. The model details (Claude Opus 5, Intelligence Index 61 / Agentic Index 55.3 at $5/$25; Google Gemini 3.6 Flash; GPT-5.6 Sol; Kimi K3 open weights; and DeepSeek V4-Flash-0731, MIT-licensed) are relayed from model-tracker and vendor coverage as reported. The waterworks allegory — a city that spent years raising a great dam only to find its fortune now turns on the water metered through every tap — is the radar's own illustration and is not a sourced claim about any specific company.*
