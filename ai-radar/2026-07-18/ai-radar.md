# 🛰️ AI Tech Radar — The Aluminum Age

**Saturday, 18 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar bolted down the plumbing — a universal connector for agents — and warned that a standard fitting is not a safe deployment. Today the thing the plumbing carries, the model itself, has its **Hall-Héroult moment.** On **Thursday 16 July**, Beijing's **Moonshot AI** shipped **Kimi K3** — a **2.8-trillion-parameter** mixture-of-experts model (~**50B active**), a **1-million-token** context window, live on API at **Sonnet-5 pricing** and, by independent evaluators, **Opus-4.8-class:** it took the **#1 spot in the Frontend Code Arena**, beating Claude Fable 5 and GPT-5.6 Sol on front-end coding, and finished ahead of Opus 4.8 in broad text ranking **while costing ~40% less.** It is the **largest open-weight model ever released** — and Moonshot will publish the **full weights on 27 July under a Modified MIT license,** so any company or government can run it on its own hardware. Axios' verdict was blunt: *"China just erased America's AI lead."* This is the radar's three-week thesis arriving as a headline: **the model is the metal, and the metal just went from precious to commodity.** The firefighter's question of yesterday becomes a smelter's question today: ***when the ingot everyone built their valuation around can suddenly be smelted cheaply — or simply downloaded — where did the value go, and are we still holding the metal or building the airframe?***

---

## 1 · Executive Summary (90-second read)

For three weeks this radar has argued one thesis — *the model is commoditizing; own and govern the layer around it.* Yesterday the connector standardized (17 Jul, "the standard coupling"); the day before, who certifies the model (16 Jul, "the assayer's mark"). Today the thesis stops being a forecast and becomes a **price tag.** On **16 July** Moonshot AI released **Kimi K3** — frontier-class capability, open weights, mid-tier price — and the model layer had, visibly and in one day, its **aluminum moment:** the metal everyone treated as precious became a commodity. It lands amid the same two enforceable countdowns this radar has tracked all fortnight: **MCP's final spec on 28 July (10 days)** and the **EU AI Act's GPAI enforcement on 2 Aug (15 days).** One release, one lesson.

1. **Frontier capability is now open-weight, self-hostable, and priced like a commodity.** Kimi K3 is a **2.8T-parameter** MoE (~**50B active**, 896 experts, 16 per token), **1M-token** context, multimodal input. It is **#1 on the Frontend Code Arena** (1,679, ahead of Fable 5 at 1,631 and GPT-5.6 Sol at 1,618), tops **Program Bench** (77.8) and **SWE Marathon** (42.0), and lands **3rd–4th overall** on independent indices — beating **Opus 4.8**, trailing only Fable 5 and GPT-5.6 Sol. API price is **$3 / $15 per million tokens** ("Opus-class at Sonnet pricing"), and the **full weights ship open on 27 July (9 days).** Achieved despite three years of US semiconductor export controls.

2. **The value just migrated off the ingot — by the labs' own admission.** Axios: K3's *"very existence puts pressure on the pricing power of U.S. labs, the enormous valuations built around their technological edge, and the case for spending hundreds of billions on ever-larger data centers."* One analyst read the convergence as *"directionally negative for AI model lab terminal margins."* The plainest reading came from the coverage itself: K3 signals *"a hyper-competitive future where software intelligence becomes highly accessible, shifting financial power over to the platforms that distribute it and the enterprises that deploy it."* That last clause is the whole radar in one sentence.

3. **A commodity metal is a gift to the builder and a trap for the hoarder.** Cheap, abundant, open-weight intelligence is *good news* for the enterprise — it collapses your input cost and hands you a sovereign, self-hostable option no vendor can revoke. The trap is mistaking the metal for the moat. The model does not decide **what you build with it** — the proprietary data, the workflow, the distribution, and the governance the EU AI Act makes enforceable in **15 days** (inventory, access control, logging, human oversight). Gartner still expects **40% of enterprise apps to embed task-specific agents by end-2026** and **>40% of agentic projects cancelled by end-2027** — the gap is what you build, not what you smelt.

**Bottom line:** welcome the aluminum age — a frontier-class, open-weight, self-hostable model at a third of yesterday's price is a genuine windfall, and refusing to touch it because it's cheap or Chinese is the ingot-hoarder's mistake. But do not confuse a cheap metal for a durable business. **Own the airframe, not the ingot:** the proprietary data K3 can't see, the workflow it can't own, the governance it can't discharge, and the model-neutral abstraction (7 Jul) that lets you swap today's precious metal for next week's commodity without re-tooling the plant. The metal is cheap now. What you build with it is still yours to make valuable.

---

## 2 · Allegory of the Day — "The Aluminum Age"

*Topic: On 16 July 2026 Moonshot AI released Kimi K3, the largest open-weight model ever — frontier-class capability (Opus-4.8-class, #1 in the Frontend Code Arena), open weights on 27 July, at mid-tier "Sonnet" pricing. Independent coverage read it as evidence that top-tier model intelligence is commoditizing and that financial power is shifting to those who distribute and deploy, not those who own the weights. The lesson for the enterprise: when a precious metal becomes a commodity, the value does not vanish — it migrates from the ingot to what you build with it.*

For most of the 19th century, aluminum was one of the most precious metals on Earth — and that is the strange part, because it is the *most abundant metal in the planet's crust.* The scarcity was never the element; it was the *unlocking.* Isolating pure aluminum was so difficult that a bar of it outshone silver in a display case, and the legends of its prestige are famous: Napoleon III is said to have reserved aluminum cutlery for his most honored guests and let the rest make do with gold. When the United States finished the **Washington Monument in 1884**, it capped the apex with a small pyramid of aluminum — around six pounds of it — chosen deliberately as a show of wealth, and briefly displayed at Tiffany's like a jewel. That was the last moment aluminum was treasure.

Two years later, in **1886**, a young American named Charles Martin Hall and a Frenchman named Paul Héroult, working independently, cracked the same electrolytic process for smelting aluminum cheaply from its ore. The price did not drift down — it **fell off a cliff,** dropping something like 99% in a decade, from a metal dearer than silver to one you would eventually wrap a sandwich in. Everyone who had built their position on *owning aluminum ingots* — on the scarcity itself — watched their treasure turn to tin in a few short years. The metal that capped a national monument as a jewel became foil, cans, window frames, and, within a generation, the **airframe of every aircraft that mattered.** The abundance the earth had always held was finally let out.

Here is the part the board must sit with: **the value did not disappear when the price collapsed — it migrated.** It moved off the ingot and into what people *built* with the suddenly-cheap metal. The fortunes of the aluminum age were not made by the smelters hoarding bars; they were made by aerospace, packaging, construction, and electrification — the industries that treated cheap aluminum as *feedstock* and built airframes, grids and supply chains on top of it. Kimi K3 is the Hall-Héroult process for frontier intelligence: a 2.8-trillion-parameter, open-weight model that any firm or nation can soon smelt on its own hardware, at a third of yesterday's token price, doing work that a year ago only a closed, premium ingot could do. The precious-metal era of the model — the era of scarcity-priced weights and valuations built on the technological edge — is ending in real time, exactly as the labs' own coverage now admits.

**The moral:** the firms that won the aluminum age were the ones who stopped mourning the price of the ingot and started building the airframe. Welcome the cheap metal — a frontier-class, open-weight, self-hostable model is a windfall, and refusing it because it's cheap is the smelter's nostalgia for scarcity. But your moat was never the metal. It is the **airframe** you build with it: the proprietary data no open weight can see, the workflow and distribution the model can't own, the governance the regulator makes you prove, and the plant flexible enough to run tomorrow's commodity in place of today's. When the ingot is cheap, the engineering is the business.

**The question it forces:** *If a frontier-class model is now a commodity metal — open-weight, self-hostable, priced like a mid-tier tool — is our moat still the ingot we license, which anyone can now smelt or download, or the airframe we build with it: the data, the workflow, the distribution and the governance the cheap metal can never copy?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- An open-weight model just landed at **Opus-4.8-class capability and Sonnet-5 price,** with **full weights free on 27 July (9 days).** **Does any part of our strategy — or our vendor's valuation — depend on frontier model capability staying scarce and expensive?** If so, that assumption expired on Thursday.
- The coverage is explicit that financial power is **"shifting to the platforms that distribute and the enterprises that deploy."** **What, specifically, is our airframe** — the proprietary data, workflow, distribution and trust a commodity model can't replicate — and are we investing there, or still paying a premium for the ingot?
- Kimi K3 is a **sovereign, self-hostable** option no vendor can revoke or price-gouge. **Have we evaluated an open-weight model as a governed fallback** for cost, continuity and data-residency — and is our stack **model-neutral (7 Jul)** enough to adopt one without re-tooling?

### 🏦 Financial Services
- A cheap, self-hostable frontier model is tempting for cost — but it is a **Chinese open-weight** model, and the weights land 27 July. **Do we have a security-and-provenance review gate** (weights integrity, supply-chain, data-egress) before any open model touches a regulated workload, or does "it's cheaper" wave it through?
- If our differentiation was "we have access to the best model," that edge just **commoditized.** **Does our moat sit in proprietary data, execution and client trust** — the things a downloadable model can't copy — or in a model advantage a competitor can now match for $3 per million tokens?

### 🧬 Healthcare / Life Sciences
- An open-weight, self-hostable model can keep **PHI entirely on-premise** — a genuine data-residency win. **Have we assessed K3 as a governed on-prem option,** with the same validation, human-oversight and logging evidence the EU AI Act demands in **15 days?**
- Commodity intelligence lowers the cost of building — and of building *badly.* **When the model is nearly free, is our bottleneck now clinical validation and governance** rather than model access, and are we resourced for *that* work rather than another model contract?

### 🏭 Manufacturing / Industrials
- Self-hostable frontier weights are the aluminum-as-feedstock moment for the shop floor: **cheap intelligence you can run at the edge, air-gapped from the internet.** **Have we mapped where an on-prem open model unlocks OT/MES use cases** a cloud-only, per-token vendor made uneconomic?
- The ingot is cheap; the **airframe is your process knowledge.** **Is our advantage the model, or the proprietary data and workflow of how we actually build** — and are we digitizing the latter while the former commoditizes?

### 🛒 Retail / Consumer
- Per-token cost just dropped toward commodity, and an **open-weight floor lands 27 July.** **Are we still on a pricing plan that assumes premium model scarcity,** and have we re-run the unit economics of every AI feature at commodity input cost?
- A competitor can now rent the same frontier capability for **$3 per million tokens.** **Does our differentiation live in the model, or in proprietary customer data, catalog, and experience** the cheap metal can't reproduce?

### 🏛️ Public Sector / Regulated
- A **top-tier open-weight model any nation can self-host** reframes AI sovereignty: capability no longer requires a US hyperscaler contract. **Is an on-prem open model part of our sovereign-AI and continuity plan** — and have we weighed the provenance and security trade-offs of a Chinese-origin model deliberately, not by default?
- The EU AI Act's deployer duties land in **15 days** and apply **however cheap or open the model is.** **Is our inventory, access control and oversight evidence ready** for an estate that may now run open weights on its own metal, outside any vendor's audit trail?

---

## 4 · Technical Deep-Dive — The Metal, the Process, and What You Build With It

Strip the geopolitics away and Kimi K3 is a supply-shock in one input to your stack: **the model.** Read it as the aluminum story in three parts — the metal that was precious, the process that made it cheap, and the airframe that is where the value actually goes.

- **The metal (frontier capability).** K3 is a **2.8-trillion-parameter** mixture-of-experts model — the largest open-weight model ever released — with a reported **~50B active** parameters (896 experts, 16 routed per token), a **1M-token** context window, and text/image/video input. On independent evaluation it is **frontier-class:** **#1 in the Frontend Code Arena** (1,679, ahead of Fable 5 and GPT-5.6 Sol), top of **Program Bench** (77.8) and **SWE Marathon** (42.0), **~1,668 Elo on GDPval v2** (2nd), and **3rd–4th overall** — beating Opus 4.8, trailing only Fable 5 and GPT-5.6 Sol.
- **The process (open weights + commodity price).** This is the Hall-Héroult step. API is live now at **$3 / $15 per million tokens** (with a $0.30 cache-hit input rate) — *"Opus-class at Sonnet pricing,"* roughly **40% under Opus 4.8** and about **one-third of Fable-tier** token cost. The **full weights publish on 27 July under a Modified MIT license,** so any firm or government can **self-host** it — a floor no per-token vendor can undercut, achieved despite three years of US export controls.
- **The airframe (what stays yours).** The model is now feedstock. What it does **not** commoditize is the airframe you build on it: **proprietary data** the open weights have never seen; the **workflow and distribution** that turn a capable model into a product; the **governance** the EU AI Act makes enforceable in 15 days; and the **model-neutral abstraction (7 Jul)** that lets you pour this week's commodity metal into the same mold you used for last week's premium ingot.

The strategic core: **a commodity metal is a windfall for the builder and a reckoning for the hoarder.** If your advantage — or your vendor's valuation — rested on *owning scarce, premium model capability,* that scarcity just broke. If your advantage rests on what you *build* with cheap capability, this is the best week of the year: your dominant input cost fell, and you gained a sovereign, self-hostable option no vendor can revoke or reprice.

```
        THE ALUMINUM AGE  —  when the precious metal (the model) becomes a commodity
        Kimi K3 is the Hall-Héroult moment for frontier intelligence

   ┌───────────────────────────────────────────────┐   ┌──────────────────────────┐
   │ THE PRECIOUS METAL — closed, premium weights    │   │  THE AIRFRAME             │
   │ scarcity-priced capability; valuations on "edge"│   │  (where value migrates)   │
   ├───────────────────────────────────────────────┤   │                           │
   │ THE PROCESS — Kimi K3, open weights 27 Jul      │   │  PROPRIETARY DATA the     │
   │ 2.8T (~50B active) · 1M ctx · Opus-class        │   │  open weights can't see.  │
   │ #1 Frontend Code Arena · beats Opus 4.8          │   │                           │
   ├───────────────────────────────────────────────┤   │  WORKFLOW & DISTRIBUTION  │
   │ THE PRICE COLLAPSE — $3/$15 per 1M tokens        │   │  the model can't own.     │
   │ "Opus-class at Sonnet pricing" · ~40% under Opus │   │                           │
   ├───────────────────────────────────────────────┤   │  GOVERNANCE the regulator │
   │ ABUNDANCE — self-hostable, sovereign, everywhere│   │  makes you prove (15 days)│
   │ a floor no per-token vendor can undercut         │   │  + model-neutral plant.   │
   └───────────────────────────────────────────────┘   └──────────────────────────┘

   TRAP: hoard the ingot — bet the moat on the model → the metal just went commodity.
   WIN : build the airframe — own data, workflow, governance → value migrates to you.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — the model is the moat | The discipline — the model is feedstock, the airframe is the moat |
|---|---|
| "We have access to the best model" | Proprietary data and workflow a downloadable model can't copy |
| Paying a scarcity premium for capability | Commodity input cost + a sovereign, self-hostable fallback |
| One vendor's model hard-wired into the product | A model-neutral abstraction (7 Jul) that swaps metals without re-tooling |
| "It's cheap, ship it" — open weights waved through | Provenance, weights-integrity and data-egress review before production |
| Assuming a cheaper model discharges compliance | Inventory, access control, logging, oversight — your EU AI Act evidence |

### Why a cheaper model doesn't shrink your governance — it grows your estate

A commodity metal does not reduce the work; it *moves* it. When frontier capability was scarce and expensive, cost was the natural governor on how many models ran where. Remove that governor — free weights, $3 tokens, self-hosting — and the number of places a capable model can run *explodes,* much of it outside any vendor's audit trail. Every one of those places is a named EU AI Act deployer duty that becomes enforceable in **15 days.** The abundance is real and welcome; so is the fact that it multiplies exactly the surface the regulator will inspect. Cheap aluminum did not make aircraft *simpler* to certify — it made there be far more aircraft.

### How it lands on legacy estates

This is the same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the spend meter, 7 Jul the model-neutral router, 8 Jul the MCP control plane, 9 Jul the deployment-labor market, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe that walks out, 13 Jul govern the goal not the gauge, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling). Today it names the metal: **the model commoditized.** On legacy estates the danger is *ingot-nostalgia* — a multi-year contract or an architecture hard-wired to one premium model, built when capability was scarce and now overpriced against a downloadable equal. The retrofit is the same control plane this radar has urged all fortnight, now aimed at the metal: a **model-neutral router (7 Jul)** so you can pour K3 or Fable 5 or the next release into the same mold, a **spend meter (6 Jul)** to prove the commodity price through to the P&L, and a **provenance-and-governance gate** so cheap, open weights don't slip into production unreviewed.

**The clean mental model:** *When the precious metal becomes a commodity, the value migrates from the ingot to the airframe. Adopt the cheap, open metal — refusing it is the smelter's nostalgia — but build your moat in the data, workflow and governance the metal can't copy.*

### Watch list this week
- **Kimi K3 (Moonshot AI)** — released **16 July**; **2.8T** parameters (largest open-weight model ever), **~50B active** (896 experts, 16/token), **1M** context, multimodal input; **#1 Frontend Code Arena** (1,679); tops Program Bench (77.8) and SWE Marathon (42.0); **3rd–4th overall**, beats Opus 4.8, trails Fable 5 & GPT-5.6 Sol.
- **The price and the weights** — API live at **$3 / $15 per 1M tokens** ($0.30 cache-hit input), *"Opus-class at Sonnet pricing,"* ~40% under Opus 4.8; **full weights open on 27 July** under a **Modified MIT** license — self-hostable, sovereign floor.
- **The market read** — Axios: **"China just erased America's AI lead"**; K3's existence *"puts pressure on the pricing power of U.S. labs, the enormous valuations built around their technological edge, and the case for spending hundreds of billions on ever-larger data centers"*; analyst: *"directionally negative for AI model lab terminal margins."*
- **The caveats** — at launch there was **no public model card, license file, or downloadable weights** (Simon Willison), and the model can be **token-hungry** (one SVG test burned 16,000+ output tokens); the-decoder reads the $3/$15 price as *"the end of super-cheap Chinese AI"* — cheaper than US frontier, pricier than prior Chinese discounts.
- **The connector counterpart** — **MCP 2026-07-28 spec** goes **final in 10 days** (stateless core, Enterprise-Managed Authorization stable 18 Jun, MCP Apps); the plumbing standardizes as the metal commoditizes.
- **The mandatory counterweight** — EU AI Act **GPAI enforcement applicable 2 Aug 2026 (15 days)**; €15M or 3% of global turnover (Art. 101); reaches deployers — and applies however cheap or open the model is.
- **Adoption cadence** — Gartner: 40% of enterprise apps embed task-specific agents by end-2026 (from <5% in 2025); >40% of agentic projects cancelled by end-2027 — governance and value, not model access, are the constraint.

---

## 5 · Quotes That Catch the Eye

> Its very existence puts pressure on the pricing power of U.S. labs, the enormous valuations built around their technological edge, and the case for spending hundreds of billions of dollars on ever-larger data centers.
> — **Axios**, on Kimi K3, 16–17 July 2026 (as reported)

> China just erased America's AI lead.
> — **Axios** headline, 17 July 2026 (as reported)

> K3 signals a hyper-competitive future where software intelligence becomes highly accessible, shifting financial power over to the platforms that distribute it and the enterprises that deploy it.
> — **Coverage of the Kimi K3 release**, July 2026 (as reported)

> The convergence of reasoning capabilities at the frontier is directionally negative for AI model lab terminal margins.
> — **Wall Street analyst**, on Kimi K3 and model-lab economics, July 2026 (as reported)

> "When the precious metal becomes a commodity, the value migrates from the ingot to the airframe. Adopt the cheap, open metal — but build your moat in the data, workflow and governance it can't copy."
> — *the radar, on the commoditizing model*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Kimi K3 released | **16 Jul 2026** | Moonshot AI / coverage |
| Total parameters (largest open-weight model ever) | **2.8 trillion** | Moonshot / coverage |
| Active parameters (MoE, 896 experts, 16/token) | **~50 billion** | Coverage (as reported) |
| Context window | **1,000,000 tokens** | Moonshot / coverage |
| Frontend Code Arena rank | **#1** (1,679) | Coverage (as reported) |
| Overall independent ranking | **3rd–4th** (beats Opus 4.8) | Coverage (as reported) |
| API price (input / output per 1M) | **$3 / $15** ($0.30 cache-hit) | Moonshot / coverage |
| Price vs Claude Opus 4.8 | **~40% cheaper** | Coverage (as reported) |
| Full open weights (Modified MIT) publish | **27 Jul 2026 (9 days)** | Moonshot / coverage |
| Achieved despite US export controls of | **~3 years** | Coverage (as reported) |
| MCP's largest revision goes final | **28 Jul 2026 (10 days)** | Model Context Protocol blog |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (15 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |
| Enterprise apps embedding task-specific agents by end-2026 | **40%** (from <5% in 2025) | Gartner |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Re-price your stack at commodity metal — and add the open model as a governed fallback.** Kimi K3 proves frontier-class capability now costs ~$3 per million tokens and will be free to self-host on 27 July. Re-run the unit economics of every AI feature at commodity input cost, and — through your **model-neutral router (7 Jul)** — qualify an open-weight model as a **sovereign fallback** for cost, continuity and data-residency. An estate hard-wired to one premium ingot is paying a scarcity premium that no longer exists.

2. **Name your airframe and invest there, not in the ingot.** The coverage says it plainly: value is shifting to those who **distribute and deploy.** Write down, in one page, the assets a downloadable model can't copy — your **proprietary data, workflow, distribution and customer trust** — and move budget from renting model capability toward compounding *those.* If you can't name your airframe, the aluminum age is coming for your margin, not your competitor's.

3. **Gate the cheap metal before it reaches production.** Abundance multiplies the estate: free weights and $3 tokens mean a capable model can now run in far more places, much of it outside a vendor's audit trail — exactly the surface the EU AI Act inspects in **15 days.** Stand up a **provenance-and-governance gate** for any open model (weights integrity, supply-chain and data-egress review, plus the inventory, access-control, logging and human-oversight evidence you'll need on 2 Aug), so the windfall doesn't arrive as an ungoverned sprawl.

---

*AI Tech Radar · generated 18 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The Kimi K3 specifications and results — 2.8-trillion total parameters (largest open-weight model released to date), a reported ~50B active parameters across 896 experts (16 routed per token), a 1-million-token context window, multimodal (text/image/video) input, #1 in the Frontend Code Arena (1,679, ahead of Claude Fable 5 and GPT-5.6 Sol), leading Program Bench (77.8) and SWE Marathon (42.0), ~1,668 Elo on GDPval v2, a 3rd–4th overall independent placement beating Claude Opus 4.8, API pricing of $3/$15 per million tokens with a $0.30 cache-hit input rate ("Opus-class at Sonnet pricing," ~40% under Opus 4.8), and a full-weights release on 27 July 2026 under a Modified MIT license — are relayed from Moonshot AI's release and secondary coverage (Axios, TechCrunch, Tom's Hardware, VentureBeat, the-decoder, latent.space, Simon Willison and others) and are marked "as reported" where they rest on secondary coverage or self-reported benchmarks. The market-impact characterizations ("China just erased America's AI lead"; pressure on US labs' pricing power and valuations; "directionally negative for terminal margins"; "shifting financial power to the platforms that distribute and the enterprises that deploy") are quoted from that coverage and marked "as reported." Launch caveats (no public model card, license file or downloadable weights at release; token-heavy behavior) are relayed from Simon Willison; the "end of super-cheap Chinese AI" framing is the-decoder's. The MCP 2026-07-28 final-spec date is the MCP project's; the EU AI Act mechanics (GPAI enforcement applicable 2 August 2026; €15M or 3% of turnover; Art. 101) are relayed from the European Commission. The Gartner figures (40% embed by end-2026; >40% cancelled by end-2027) are Gartner's. The "9 days," "10 days" and "15 days" figures are simple counts from this edition's date (18 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own. The aluminum allegory — aluminum as the most abundant metal in the crust yet a precious metal in the 19th century, the Napoleon III cutlery legend, the ~6-pound aluminum apex of the Washington Monument (1884), and the 1886 Hall-Héroult electrolytic process and subsequent ~99% price collapse — is the radar's own historical illustration, told approximately, and is not a sourced claim about AI.*
