# 🗓️ AI Tech Radar — The Powder Magazine

**Monday, 27 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday the radar told you to read the regulatory notice to the last line — that the AI Act's 2 August date **split,** and an extension to file is not an extension to pay. Today the story moves from the calendar to the loading dock. At **00:00 UTC this morning** the largest open-weight model ever built — **Kimi K3** (2.8T MoE, Modified MIT) — went **free and ownerless,** downloadable by any firm, nation or adversary. And in the same window two governments handed you its blast rating: a **joint UK AISI / US CAISI cyber assessment** found K3 scores **32% on exploit development** (against 76% for top US models) and drove a simulated 32-step corporate-network attack to **step 17 on average** — meaningfully behind the frontier, but with guardrails that, in the institutes' own words, *"did not prevent it from attempting cyber exploit development or offensive cyber operations."* And once weights are open, the developer *"loses all downstream control"* — the safety catch comes off with the crate. Meanwhile the frontier walked away again: **Anthropic's Claude Opus 5** (24 July) tops both Artificial Analysis indices at launch, at **half Fable 5's price.** The board's question: ***the day the cheap powder lands in our own yard — with a government's blast rating stamped on the crate and a safety catch that unscrews — are we the operator who owns the magazine, or the one who stacks it by the furnace because the vendor used to hold the key?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thesis — *the model commoditizes; own and govern the layer around it* — and this morning the commodity stopped being a countdown and became a fact on your dock. At **00:00 UTC on 27 July,** Moonshot AI published the **full open weights of Kimi K3** — a **2.8-trillion-parameter** mixture-of-experts model (~50B active, 16 of 896 experts firing per token, 1M-token context) under a **Modified MIT** license, the largest open-weight release in history (~**1.4 TB** in four-bit MXFP4). It is now downloadable, self-hostable and *modifiable* by anyone. In the same window, the **UK AI Security Institute (AISI)** and the **US Center for AI Standards and Innovation (CAISI)** published a **joint preliminary cyber assessment** of K3 — and the finding cuts two ways. The reassuring half: K3 **trails** the US frontier by a wide margin — **32% on ExploitBench** (41 post-2023 Chrome V8 vulnerabilities) versus **76%** for top US models, and it reached **step 17 of a 32-step** simulated corporate-network attack on average versus **28.5** for leading US closed-weight models. The alarming half: K3's **guardrails "did not prevent it from attempting cyber exploit development or offensive cyber operations,"** it completed the **full 32-step attack path in 1 of 10 attempts,** and — the structural point — publishing weights means the developer *"loses all downstream control; safeguards cannot be remotely updated or revoked."* On an open model the safety catch is a screw, not a weld. This lands the same week the frontier moved *away* from anyone hoping to win by owning the newest weights: **Claude Opus 5** (Anthropic, 24 July) took **#1 on Artificial Analysis's Intelligence and Agentic indices** at launch, at **$5/$25 per million tokens — half of Fable 5** — while Wall Street's **bond market grew anxious about the AI capex bill** (hyperscaler 2026 capex ~**$490B**, per Citi). The standing plumbing thread closes tomorrow: **MCP's final spec goes live 28 July (1 day),** and **EU AI Act Article 50 + GPAI enforcement lands 2 August (6 days).**

1. **The cheap, dual-use commodity is now in your yard — and its safety catch unscrews.** Kimi K3's open weights are live today. A government assay says the blast is real but *sub-frontier* (32% vs 76%; 17/32 vs 28.5 steps) — this is not a super-weapon. The hazard is not the raw power; it is that **open weights strip the operator-side controls closed models rely on.** The moment you self-host the commodity, the developer's guardrails stop being the vendor's problem and become yours — because they *"cannot be remotely updated or revoked,"* and a fine-tuner can remove them entirely.

2. **You cannot win the race by owning the newest weights — the frontier walks away.** The same week the largest *open* model went free, the *frontier* jumped: Opus 5 topped both indices at launch for half of Fable 5's price. Chasing "own the best model" is a treadmill — the vendor keeps the newest, always-locked powder, and it's more capable than what you can own. The durable asset is not the charge; it is **the magazine you keep it in** — the sandbox, egress controls, credential separation, eval gate and audit log that govern *whatever* weights you run, frontier or open.

3. **When custody transfers to you, so does the assay — read the government's blast rating, then build the magazine.** AISI/CAISI did your first-pass hazard rating for free; that is the assayer's mark, not the containment. On infrastructure you own, separate the detonator from the charge (least-privilege credentials and network egress kept apart from the raw model), log every "stick" in and out, and cap the blast radius by default. The estates that self-host safely in 2026 are the ones that treated the open weight as **licensed explosive, not free software.**

**Bottom line:** the commodity you were told to want arrived free this morning — and arrived dual-use, with a government's blast rating and a safety catch that comes off. Owning it is not the prize; it is the moment the safety burden moves onto your books. Don't stack the powder by the furnace. Own the magazine.

---

## 2 · Allegory of the Day — "The Powder Magazine"

*Topic: At 00:00 UTC on 27 July 2026, Moonshot AI published the full open weights of Kimi K3 — a 2.8-trillion-parameter mixture-of-experts model under a Modified MIT license, the largest open-weight release ever. In the same window, a joint preliminary assessment by the UK AI Security Institute (AISI) and the US Center for AI Standards and Innovation (CAISI) found K3 trails leading US frontier models on cyber tasks (32% on ExploitBench vs 76%; step 17 of a 32-step simulated network attack vs 28.5 for top US closed models) but that its guardrails "did not prevent it from attempting cyber exploit development or offensive cyber operations," and that once weights are open "the developer loses all downstream control; safeguards cannot be remotely updated or revoked." The same week, Anthropic's Claude Opus 5 (24 July) topped both Artificial Analysis indices at launch at half Fable 5's price, and bond markets grew anxious over hyperscaler AI capex (~$490B in 2026, per Citi). The lesson for the enterprise: an open-weight model is cheap, dual-use, and comes with a removable safety catch — owning it transfers the safety custody to you, so own the containment, not the race.*

Cheap, powerful explosive is one of the most productive commodities the industrial age ever made — it cut the railway tunnels, sank the mines, drove the canals, moved the mountains. And precisely because it was so useful and so cheap, no serious society responded to it by banning it, and none was foolish enough to treat it as harmless. They did a third thing: they built the **magazine.** A powder magazine is not the powder — it is the discipline *around* the powder. A licensed, isolated store, sited a measured distance from anything that matters. A magazine-keeper who signs for every keg. A logbook of every stick in and every stick out. Quantity limits, so a single accident cannot take the whole works. And the one rule every powderman learns first: **the detonator lives apart from the charge.** The charge alone is inert; the blasting cap alone is a firecracker; it is the two *together,* carelessly stored, that level a building. Keep them separate and the productive commodity stays productive.

Here is the part the enterprise keeps missing. When the powder was sold only under the manufacturer's lock — delivered, stored and detonated on the vendor's bonded site — the *vendor* kept the magazine, and the operator never had to think about custody. The day the powder is sold **loose, by the barrel, to take back to your own yard,** the economics improve wonderfully and the *entire safety burden silently changes hands.* You are now the magazine-keeper. The safety catch the manufacturer fitted? On loose powder it is a screw, not a weld — anyone in your yard can back it out. And no recall can reach a barrel already in a thousand yards: once it is loose, *"the maker loses all downstream control."* This is exactly what the inspectorate meant this week when it stamped the blast rating on the crate — a real, if sub-frontier, charge — and warned in the same breath that the catch does not hold and cannot be re-tightened from the factory.

So the disciplined operator does three unglamorous things the excited one skips. First, **read the government's blast rating** — the assay tells you this is a working charge, not a toy, and not the strongest on the market either; calibrate the magazine to the real number, neither panicking nor waving it through. Second, **build the magazine before the powder arrives, not after** — the isolated store (a hardened sandbox), the distance rule (network egress controls), the logbook (an audit trail of every call), the quantity cap (blast-radius limits on what any one agent can touch). Third, and most important, **store the detonator apart from the charge** — keep the model's credentials, its tool-authority and its path to your production systems *separate* from the raw weights, on the principle of least privilege, so that even a charge with its catch removed has nothing to set off. Meanwhile the excited operator, chasing the *biggest* charge, discovers the manufacturer always keeps a bigger, safer, locked one for itself — and that renting the newest powder was never the same as owning the yard it detonates in.

**The moral:** welcome the cheap commodity — an open-weight model you can self-host is a genuine strategic good, and this radar has argued for a month that you should hold one. But an open weight is licensed explosive, not free software. The blast rating is the government's job; the **magazine is yours.** Read the assay, build the containment before the crate lands, and store the detonator apart from the charge — because a safety catch that unscrews is only as good as the yard you keep the powder in.

**The question it forces:** *The cheap powder is in our own yard this morning, with a government's blast rating stamped on the crate and a safety catch we now know unscrews. Have we built the magazine — the sandbox, the egress rule, the logbook, the detonator kept apart from the charge — or did we carry the barrel in because the API price was good and the vendor used to hold the key?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- Kimi K3's open weights are **live today,** with a joint AISI/CAISI assessment saying the model is capable of assisting offensive cyber work and that its **guardrails don't hold and can't be revoked once open.** **If we self-host any open-weight model, who owns the "magazine"** — the sandbox, egress controls, credential separation, audit log — and can they show it existed *before* the weights landed?
- The frontier moved the same week (Opus 5 #1 at launch, half Fable 5's price). **Are we chasing "own the best model" — a treadmill the vendor always wins — or owning the containment and eval gate that govern whichever model we run?**
- The government did our **first-pass blast rating** for free. **Have we read the actual numbers** (sub-frontier: 32% vs 76%, 17/32 steps) so we neither panic-ban a useful commodity nor wave through a real dual-use capability?

### 🏦 Financial Services
- An open-weight model fine-tuned in-house has **no vendor safety catch and no remote kill switch.** **For any self-hosted model touching customer data or trading systems, have we separated its credentials and network egress from the raw weights** — the detonator apart from the charge — so a stripped guardrail sets off nothing?
- Bond markets are repricing the **AI capex bill** (~$490B hyperscaler spend in 2026; credit spreads widening). **Does our AI business case survive a world where the cheap open commodity is on our own metal and the ROI question has reached the balance sheet, not just the pilot?**

### 🧬 Healthcare / Life Sciences
- Dual-use is not abstract in a lab: a capable open model plus wet-lab or protocol access is a governed combination. **For any open-weight model we host near sensitive research, is the "quantity cap" real** — hard limits on what one agent can reach — rather than a policy PDF?
- Open weights mean **no recall.** **If a hosted model is later found to assist a harmful workflow, what is our containment and rollback plan today,** given the maker cannot patch it for us?

### 🏭 Manufacturing / Industrials
- You already run powder magazines — literally, and in OT security. **Apply the same discipline to open-weight AI: licensed store, keeper, logbook, distance rule.** Is our AI supply-chain map precise enough to say which models are vendor-locked (magazine held by them) versus self-hosted (magazine held by us)?
- Suppliers will ship you agents built on open weights to cut cost. **Do procurement terms require a blast rating (a cyber/safety assessment) and proof of containment** for any open-weight model embedded in what they sell us?

### 🛒 Retail / Consumer
- A cheap open model is tempting for a storefront chatbot or content engine. **Have we weighed the Article 50 transparency duty (live 2 August, 6 days) AND the open-weight safety custody together** — the disclosure *and* the magazine — rather than one without the other?
- Marketing will want the frontier's quality at the commodity's price. **Do we have a model-neutral abstraction** so switching between Opus 5 (locked, frontier) and K3 (open, self-hosted) is a routing decision, not a rebuild?

### 🏛️ Public Sector / Regulated
- A sovereign, self-hostable frontier-class model is exactly what many public bodies wanted — and it now carries a dual-use cyber rating from two allied governments. **Can we adopt the sovereignty benefit and own the containment,** so the same weight that serves citizens can't be repurposed against them?
- Two AI *security institutes* just published a joint assay. **Is our procurement wired to require and read such assessments** — treating a government blast rating as a standard artifact, like a safety data sheet — before any open model enters a regulated system?

---

## 4 · Technical Deep-Dive — The Magazine, Not the Powder

Read this week's story as one lesson about **owning the containment, not the charge,** in three parts — the powder (what actually landed, and why it's a genuine commodity), the assay (what two governments measured, and why the number matters less than the missing catch), and the magazine (the discipline you now owe because custody just changed hands).

- **The powder (a real commodity, genuinely worth having).** At **00:00 UTC on 27 July,** Moonshot AI released the full open weights of **Kimi K3** — **2.8T** parameters, mixture-of-experts (**16 of 896 experts** fire per token, **~50B active**), **1M-token context,** multimodal, under a **Modified MIT** license, ~**1.4 TB** in four-bit MXFP4. It is the largest open-weight release ever and, by prior independent evals, near-frontier on coding. Self-hostable by any firm or nation — the "village green" this radar has argued you should keep. That part is good, and unchanged.
- **The assay (a government blast rating — read both halves).** In the same window the **UK AISI** and **US CAISI** published a **joint preliminary cyber assessment.** The reassuring half: K3 **trails** the US frontier — **32% on ExploitBench** (41 post-2023 Chrome V8 CVEs) versus **76%** for top US models; on **"The Last Ones"** (TLO), a 32-step simulated corporate-network attack across ~20 hosts, K3 reached **step 17 on average** versus **28.5** for leading US closed-weight models (and ahead of peer open model GLM-5.2 at step 11). This is a working charge, *not* a super-weapon. The half that matters more: K3's **guardrails "did not prevent it from attempting cyber exploit development or offensive cyber operations,"** it completed the **full 32-step path in 1 of 10 attempts** (within a 100M-token budget), and — structurally — once weights are public **"the developer loses all downstream control; safeguards cannot be remotely updated or revoked."** The blast rating is real and sub-frontier; the safety catch is the story.
- **The magazine (the discipline that now falls to you).** When the model lived behind a hosted API, the **vendor kept the magazine** — the safety controls, the ability to patch or revoke. The day you download the weights, custody transfers: **you are the magazine-keeper.** That means a hardened **sandbox** (the isolated store), **network egress controls** (the distance rule), an **audit log** of every call (the logbook), **blast-radius limits** on any one agent (the quantity cap), and — the one rule powdermen learn first — **the detonator kept apart from the charge:** least-privilege credentials, tool-authority and production-system access held *separate* from the raw model, so a stripped guardrail has nothing to ignite. This is the same layer this radar has named all month, now with a security edge: own it before the crate lands.

The strategic core: **you cannot win by owning the charge; you win by owning the magazine.** The frontier (Opus 5, #1 at launch, half Fable 5's price) will always keep the biggest, safest, locked powder for itself — so "own the best model" is a race the vendor wins. What travels with *you,* frontier or open, is the containment. After this week, "we self-host an open model to be sovereign" is not a complete answer; *"we self-host it inside a magazine we own — sandbox, egress, logbook, quantity cap, detonator apart from charge — sized to the government's blast rating"* is.

```
        THE POWDER MAGAZINE — own the containment, not the charge
        An open weight is licensed explosive, not free software.

   ┌─────────────────────────────────────────────────────────┐
   │  THE POWDER  — Kimi K3 open weights, LIVE 27 Jul 00:00 UTC │  ✅ REAL COMMODITY
   │  2.8T MoE · ~50B active · 1M ctx · Modified MIT · ~1.4 TB  │
   │  self-hostable by any firm, nation — or adversary          │
   └─────────────┬─────────────────────────────────────────────┘
                 │  read the government's blast rating →
                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │  THE ASSAY  — UK AISI / US CAISI joint cyber assessment   │  ⚠ DUAL-USE, SUB-FRONTIER
   │  32% exploit-dev (vs 76% US) · TLO step 17/32 (vs 28.5)   │
   │  BUT guardrails "did not prevent" offensive cyber attempts │
   │  open weights → maker "loses all downstream control"       │
   └─────────────┬─────────────────────────────────────────────┘
                 │  custody just changed hands → YOU keep it now
                 ▼
   ┌───────────────────────────────────────┐
   │  BUILD THE MAGAZINE                    │  the layer to own
   │  sandbox (isolated store) · egress      │  detonator APART
   │  controls (distance) · audit log        │  from the charge:
   │  (logbook) · blast-radius cap (quantity)│  least-privilege creds
   │  on infrastructure you own              │  ≠ raw weights
   └───────────────────────────────────────┘

   TRAP: "it's free software" → self-host with no containment → stripped catch, live yard.
   WIN : "it's licensed explosive" → build the magazine first → useful commodity, contained.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — treat it as free software | The discipline — treat it as licensed explosive |
|---|---|
| Download the weights, run them where it's convenient | Build the magazine (sandbox, egress, log) before the crate lands |
| Trust the shipped guardrails | Know the catch unscrews and can't be re-tightened remotely |
| Give the model your credentials to "just work" | Keep the detonator apart from the charge — least privilege |
| Chase the biggest/newest model to feel safe | Own the containment that governs any model, frontier or open |
| Read the headline ("trails US models — fine") | Read both halves of the assay: sub-frontier *and* catch missing |

### Why an open weight is a security object, not just a cost line

Every force this radar tracked all month — commodity models, open weights, agentic autonomy, provenance, the split AI Act calendar — assumed the model was a *capability* to acquire. This week reframes it as an *asset in custody.* The reassuring number (K3 trails the frontier) tempts the trap: "sub-frontier, so wave it through." But the institutes' real warning is not about the score — it is that open release removes the operator-side controls closed models rely on, permanently and irrevocably. A firm that reads only "trails US models" self-hosts with no magazine; a firm that reads the whole assay builds the containment sized to a real, if modest, blast. The distillation debate from yesterday even connects here (one analysis suggests distillation may explain the trailing cyber score) — provenance and hazard are two readings of the same crate.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension). Today adds the security custody to the provenance file: the open weight you were told to keep as a fallback is also a dual-use charge whose safety catch comes off. On legacy estates the danger is a data-science team that pulls 1.4 TB of weights onto a GPU box wired straight into the corporate network "to evaluate it," with the same broad service credentials every other job uses — powder stacked next to the furnace, detonator in the same crate. The retrofit is the magazine: an isolated eval sandbox, egress allow-lists, a call-level audit log, and credentials scoped to nothing that matters — built *before* the download, and sized to the government's published blast rating.

**The clean mental model:** *An open-weight model is licensed explosive, not free software. The government stamps the blast rating; you build the magazine — and you store the detonator apart from the charge.*

### Watch list this week
- **Kimi K3 open weights — LIVE today (27 July, 00:00 UTC).** The largest open-weight model ever (2.8T MoE, Modified MIT, ~1.4 TB in MXFP4) is now downloadable and modifiable by anyone. The "village green" is real — and so is the custody transfer.
- **The AISI/CAISI blast rating.** Two allied AI *security institutes* jointly rated K3's cyber capability: sub-frontier (**32% vs 76%;** TLO **17/32 vs 28.5**) but with guardrails that did not prevent offensive-cyber attempts and cannot be revoked once open. Treat a government assessment as a standard procurement artifact.
- **The frontier moved away (Opus 5, 24 July).** Anthropic's Claude Opus 5 took **#1 on Artificial Analysis's Intelligence and Agentic indices** at launch, at **$5/$25** — half Fable 5 — with a low/medium/high effort dial. You can't out-own the risk by buying the newest, locked powder.
- **The capex bill reaches the bond market.** Hyperscaler 2026 AI capex ~**$490B** (Citi); credit spreads widened after Alphabet lifted its forecast. The ROI reckoning (yesterday's thread) is now a balance-sheet conversation.
- **The standing plumbing — MCP final spec 28 July (1 day)** — and **EU AI Act Article 50 + GPAI enforcement 2 August (6 days;** €15M or 3% of turnover, no grace).

---

## 5 · Quotes That Catch the Eye

> [Kimi K3's guardrails] did not prevent it from attempting cyber exploit development or offensive cyber operations.
> — **UK AI Security Institute (AISI) & US CAISI**, joint preliminary assessment of Kimi K3, July 2026 (as reported)

> When an AI model's weights are released publicly, the developer loses all downstream control, and safeguards cannot be remotely updated or revoked.
> — **coverage of the UK AISI / CAISI assessment**, on why open release changes the safety calculus, July 2026 (as reported)

> [Claude Opus 5] excels at verifying its work and iterating carefully until it succeeds.
> — **Anthropic**, on Claude Opus 5, 24 July 2026 (as reported)

> Bond market anxiety is growing over AI capex budgets.
> — **CNBC**, headline, 24 July 2026 (as reported)

> "An open-weight model is licensed explosive, not free software. The government stamps the blast rating; you build the magazine — and you store the detonator apart from the charge."
> — *the radar, on the powder magazine*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Kimi K3 full open weights — live | **27 Jul 2026, 00:00 UTC** | Moonshot / coverage |
| Kimi K3 size / architecture | **2.8T MoE · ~50B active (16 of 896 experts) · 1M ctx** | Moonshot / coverage |
| Kimi K3 open-weights footprint (MXFP4) | **~1.4 TB** | coverage (as reported) |
| Kimi K3 — ExploitBench (exploit development) | **32%** (vs **76%** top US models) | UK AISI / CAISI |
| Kimi K3 — TLO 32-step simulated attack (avg) | **step 17 of 32** (vs **28.5** US closed) | UK AISI / CAISI |
| Kimi K3 — completed full 32-step attack path | **1 of 10 attempts** (≤100M-token budget) | UK AISI / CAISI |
| Peer open model GLM-5.2 on TLO (avg) | **step 11 of 32** | UK AISI / CAISI |
| Claude Opus 5 — pricing (in / out) | **$5 / $25 per 1M tokens** | Anthropic / coverage |
| Claude Fable 5 — pricing (reference) | **$10 / $50 per 1M tokens** | coverage (as reported) |
| Opus 5 — Frontier-Bench agentic coding | **43.3%** (beats Fable 5 & GPT-5.6 Sol) | coverage (as reported) |
| Opus 5 — launch-day rank | **#1 Intelligence & Agentic Index** | Artificial Analysis (as reported) |
| Hyperscaler AI capex, 2026 (Citi) | **~$490B** | coverage (as reported) |
| Four largest hyperscalers — 2026 capex | **$250B (+77% YoY)** | coverage (as reported) |
| OpenAI ARR as share of 2026 hyperscaler capex | **~3% ($20B)** | coverage (as reported) |
| EU AI Act Article 50 + GPAI enforcement | **2 Aug 2026 (6 days)** · €15M or 3% | European Commission |
| MCP final spec goes live | **28 Jul 2026 (1 day)** | Model Context Protocol blog |
| Enterprises that can actually govern their AI agents | **12%** | OutSystems, ~1,900 IT leaders (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Read the blast rating — then decide, calibrated, not by headline.** Pull the AISI/CAISI assessment into your model-risk file as a standard artifact. Read *both* halves: K3 is **sub-frontier** (32% vs 76%; 17/32 steps) — so don't panic-ban a genuinely useful open commodity — *and* its guardrails don't hold and can't be revoked once open — so don't wave it through as "free software." The right posture is neither prohibition nor complacency; it is containment sized to a real, modest, irrevocable hazard.

2. **Build the magazine before the crate lands.** For any open-weight model you self-host or evaluate, stand up the containment *first:* a hardened, isolated sandbox; network egress allow-lists; a call-level audit log; and hard blast-radius limits on what any one agent can touch. Above all, **store the detonator apart from the charge** — keep the model's credentials, tool-authority and production access on least privilege, separate from the raw weights, so a stripped guardrail ignites nothing. Powder does not go on the GPU box wired straight into the corporate network.

3. **Own the magazine, not the race — and put it on infrastructure you own.** Opus 5 topping the index at launch is the proof: the vendor always keeps a bigger, safer, locked model, so "own the best weights" is a treadmill. Invest instead in the model-neutral containment and eval gate that govern *whatever* you run — frontier or open — so switching from a locked Opus 5 to a self-hosted K3 is a routing decision, not a security rebuild. Fold this into the Article 50 / GPAI evidence due in **6 days:** the magazine is also your compliance artifact.

---

*AI Tech Radar · generated 27 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The technical and security facts are relayed from public coverage, the UK AI Security Institute / US CAISI joint assessment, Anthropic, and market reporting, and are marked "as reported" where they rest on secondary reporting. Kimi K3's specifications (2.8-trillion-parameter mixture-of-experts, ~50B active parameters with 16 of 896 experts firing per token, 1M-token context, Modified MIT license, ~1.4 TB in four-bit MXFP4, full open weights published 27 July 2026 at 00:00 UTC) are Moonshot AI's as relayed via July 2026 coverage. The UK AISI / US CAISI joint preliminary cyber assessment figures — 32% on ExploitBench (41 post-2023 Chrome V8 vulnerabilities) versus 76% for top US models; an average of step 17 of a 32-step "The Last Ones" simulated corporate-network attack (~20 hosts) versus 28.5 for leading US closed-weight models and step 11 for GLM-5.2; completion of the full 32-step path in 1 of 10 attempts within a 100-million-token budget; and the characterizations that K3's guardrails "did not prevent it from attempting cyber exploit development or offensive cyber operations" and that open release means "the developer loses all downstream control; safeguards cannot be remotely updated or revoked" — are relayed from the institutes' July 2026 joint blog and July 2026 coverage (NIST, AISI, MLQ, Cryptopolitan, the-decoder, XenoSpectrum) as reported. Claude Opus 5 details (release 24 July 2026; $5/$25 per million tokens versus Fable 5's $10/$50; a low/medium/high effort setting; 43.3% on Frontier-Bench agentic coding; and a launch-day #1 on Artificial Analysis's Intelligence and Agentic indices) are Anthropic's and independent testers' as relayed via July 2026 coverage. The AI-capex figures (~$490B hyperscaler spend in 2026 per Citi; $250B for the four largest, up ~77% year over year; OpenAI's ~$20B ARR as ~3% of that total; bond-market/credit-spread anxiety after Alphabet lifted its forecast) are relayed from July 2026 market reporting (CNBC, Citigroup via coverage) as reported. The EU AI Act Article 50 transparency and GPAI enforcement date (2 August 2026; €15M or 3% of global annual turnover under Article 99; high-risk obligations deferred to 2027–2028 by the Digital Omnibus) is relayed from the European Commission and July 2026 coverage. The MCP 2026-07-28 final-spec date is the MCP project's. The OutSystems 12%-can-govern figure is relayed from prior 2026 research as reported. The "1 day" and "6 days" figures are simple counts from this edition's date (27 July 2026) to 28 July and 2 August 2026 respectively and are the radar's own. The powder-magazine allegory — the historical practice of governing cheap, dual-use industrial explosive not by prohibition but by physical custody (a licensed, isolated store; a magazine-keeper; a logbook; quantity and distance limits; and storing the detonator apart from the charge) — is the radar's own illustration, told approximately, and is not a sourced claim about any specific explosives regime or about AI. This is a developing story: the AISI/CAISI assessment is described by its authors as "preliminary," and the Kimi K3 distillation question referenced yesterday remains contested.*
