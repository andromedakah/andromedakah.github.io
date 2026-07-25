# 🖼️ AI Tech Radar — The Provenance

**Saturday, 25 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday the radar told you to keep a **village green** — an open-weight model you can self-host, the commons no landlord can revoke — and named the nearest one: **Kimi K3,** whose full open weights publish **in two days (27 July).** Today a cloud settles over the deed to that green. On **22 July, White House OSTP Director Michael Kratsios** posted that the United States has "information that **Moonshot AI distilled Anthropic's Fable** for the development of its K3 model," using "a sophisticated internal platform to conduct **large scale distillation** against U.S. models" while "rotating access to avoid detection," and separately alleged Moonshot **accessed export-restricted Nvidia GB300 chips in Thailand.** Treasury Secretary **Scott Bessent** raised the stakes to policy: *"Open source is not open season on American IP,"* with **"sanctions and Entity List designations… on the table."** And then the counter-current: a wall of independent researchers called the claim thin — the timeline is punishing (**Fable went public 1 July; K3 launched ~15 July**), model *outputs* are not copyrighted, and distillation is a common industry practice (Musk testified xAI distilled OpenAI to build Grok). Anthropic itself has **not** publicly tied K3 specifically to Fable. The board's question: ***the open-weight fallback we were told to keep is a masterwork of contested provenance — brilliant, cheap, self-hostable, and now under a sanctions cloud that may or may not hold. Do we hang it in the gallery on faith, refuse it on a headline, or do what a serious collector does — demand the chain of custody, price the title risk, and never bet the gallery on a single canvas whose deed we can't defend?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thesis — *the model commoditizes; own and govern the layer around it* — and yesterday it named the safety valve: keep a **village green,** an open-weight model you can self-host so no single vendor sets all your terms, with **Kimi K3** (open weights **27 July, 2 days**) and **DeepSeek V4** as the nearest greens. Today the deed to the nearest green is contested. On **22 July** the **White House** and **Treasury** turned the long-running "distillation" dispute into a live sanctions threat aimed squarely at **Moonshot AI,** maker of Kimi K3. OSTP Director **Michael Kratsios** posted that the US has information Moonshot **distilled Anthropic's Fable** to build K3 via a purpose-built platform designed to **evade detection,** and that Moonshot **accessed export-restricted Nvidia GB300s in Thailand.** Treasury Secretary **Scott Bessent** framed the doctrine — *"Open source is not open season on American IP"* — and put **sanctions and Entity List designations** on the table for "covert, industrial-scale distillation… that crosses the line into IP theft." The evidence base is public and thin, and the pushback was immediate and expert: the release window is brutally tight (**Fable 1 July → K3 ~15 July**), a model's *outputs* are not copyrighted, distillation is **routine** across the industry (Musk testified xAI distilled OpenAI for Grok), and Anthropic — which in **February** said DeepSeek, Moonshot and MiniMax used **~24,000 fabricated accounts** to run **>16 million** Claude interactions — has **not** publicly connected K3 to Fable. A Moonshot engineer's retort: *"We trained a brand new frontier model in JUST 15 DAYS."* The point for the enterprise is not who is right; it is that **the provenance of your open-weight fallback is now a first-class risk** — legal (sanctions, IP, indemnity), and reputational — the week before its weights hit your servers. The standing countdowns run beneath, one day closer: **MCP's final spec (28 July, 3 days)** and the **EU AI Act's GPAI enforcement (2 August, 8 days).**

1. **The "village green" now comes with a title dispute — provenance is a risk you must price, not assume.** The open-weight fallback this radar told you to keep is real, cheap and capable — and, in the case of the flashiest one, under a **US government distillation accusation** with **sanctions and Entity List** threats attached (Kratsios & Bessent, 22 July). Whether or not the claim survives scrutiny, a self-hosted model you cannot walk back from is exactly where **contested provenance** becomes *your* exposure: export-control, sanctions, IP-indemnity and procurement-trust risk that lands on the deployer, not the lab. You inherit the chain of custody of every model you run.

2. **A contested provenance cuts both ways — don't refuse a masterwork on a headline, and don't hang it on faith.** The expert pushback is substantive, not partisan cheerleading: the **Fable-1-July → K3-15-July** window makes "strictly distillation" implausible (researcher **Braden Hancock:** *"I don't think you get a model this strong and this quickly… doing strictly distillation"*), model outputs aren't copyrighted, and distillation is standard practice. The discipline is neither reflex — it is to **demand the paper trail:** license clarity, training-data provenance, an indemnification posture, and a documented reason you can defend to a regulator or an auditor for every weight you deploy.

3. **The answer is portfolio, not purity — keep more than one green, and never bet the gallery on one canvas.** A collector never lets one disputed attribution sink the collection. Provision **at least two** self-hostable open-weight options of **different provenance** (e.g. an MIT-licensed **DeepSeek V4** alongside any Kimi K3 you qualify), keep your **context, prompts and eval gate portable** across them, and make swapping a model a *switch,* not a migration. Then a sanctions designation, a license fight or a broken chain of custody is a bad week, not a shuttered gallery.

**Bottom line:** yesterday's lesson stands — keep a village green — but today adds the fine print a serious owner already knows: **a green with a contested deed is still a liability.** Treat model provenance as a governed attribute: demand the chain of custody, price the title risk, hold **more than one** open-weight option of different origin, and keep your context and eval gate portable — so no single disputed masterwork can take the whole gallery down with it.

---

## 2 · Allegory of the Day — "The Provenance"

*Topic: On 22 July 2026 the White House and Treasury escalated a long-running dispute over AI "distillation" into a live sanctions threat against Moonshot AI, maker of the open-weight Kimi K3. OSTP Director Michael Kratsios said the US has information that Moonshot distilled Anthropic's Fable to build K3 using a purpose-built platform designed to evade detection, and that Moonshot accessed export-restricted Nvidia GB300 chips in Thailand; Treasury Secretary Scott Bessent said "open source is not open season on American IP," with sanctions and Entity List designations "on the table." Independent researchers pushed back hard: the release window (Fable public 1 July, K3 ~15 July) makes large-scale distillation implausible, model outputs are not copyrighted, and distillation is common practice (Musk testified xAI distilled OpenAI for Grok); Anthropic has not publicly tied K3 to Fable, though in February it accused three Chinese labs of using ~24,000 fake accounts for >16M Claude interactions. Kimi K3's full open weights publish 27 July. The lesson for the enterprise: the open-weight fallback you were told to keep is a masterwork of contested provenance — welcome the brilliance, but govern the chain of custody.*

In the world of great paintings, connoisseurs learned a hard lesson the market keeps re-teaching: **the value of a masterwork lives as much in its paper trail as in its paint.** A canvas can be dazzling — the brushwork unmistakable, the pigment right for the period, every expert agreeing it is a work of the first rank — and still be nearly **unhangable,** because no one can prove where it has been. **Provenance** is that proof: the unbroken **chain of custody** from the artist's studio to your wall — every owner, every sale, every export stamp, every catalogue it appeared in. When the chain is whole, a museum hangs the work, an insurer covers it, a buyer pays in full. When the chain is broken — a gap in the record, a disputed attribution, a whisper that the thing was **looted or copied** — the painting does not lose its beauty. It loses its **title.** And a masterpiece you cannot prove you may lawfully own is a masterpiece you cannot safely hang.

Here is the cruelty of it, and the discipline it forces. **The accusation need not be proven to do its damage.** The moment a credible authority questions a work's provenance, the price falls, the sale freezes, the insurer hesitates — the cloud itself is the cost, whether or not it ever resolves into a verdict. And provenance disputes are treacherous precisely because they **cut both ways:** some are open-and-shut theft, and some are political, thin, or mistaken — a rival's insinuation, an attribution that collapses the moment a scholar checks the dates and finds the timeline impossible. A serious collector treats both with the same cold method: not faith, not reflex, but **the file** — the documented history you can lay on a regulator's desk. They demand the export papers, they check the catalogue, they read the dates, they buy title insurance, and — the part the amateur skips — **they never let one contested canvas anchor the whole collection.** The great houses survive not by owning only spotless works, but by owning **many,** so that the day one attribution is challenged, the gallery still opens.

This week the enterprise was handed exactly this problem in software. The open-weight model you were told to keep as your fallback — the brilliant, cheap, self-hostable one — arrived with a **cloud over its deed:** a government authority alleging the masterwork was **copied** from another's, a threat of **sanctions and an Entity List** that would freeze the sale, and a chorus of scholars insisting the dates don't fit and the charge is thin. You cannot resolve the dispute; you are not the court. But you are the collector, and the collector's disciplines are wholly in your hands. **Demand the file** (license, training-data provenance, an indemnity you can point to). **Price the title risk** (what does a sanctions designation or an IP claim cost a model you've wired into production and cannot instantly un-hang?). And above all, **do not anchor the gallery on one canvas** — hold more than one open-weight work, of different provenance, so a disputed deed is a removed painting, not a shuttered museum.

**The moral:** welcome the masterwork — refusing a brilliant, cheap, self-hostable model on a headline is its own kind of poverty, and the accusation against it may well not hold. But hang nothing you cannot prove you may lawfully hang. Keep the **file** (provenance, license, indemnity you can show an auditor), keep the **portfolio** (more than one green, of different origin), and keep your **context and eval gate portable** so any single canvas can come down without closing the gallery. A collection built on one disputed masterpiece is one accusation away from dark walls; a collection built on documented, diversified works keeps its doors open no matter which attribution is challenged next.

**The question it forces:** *The fallback we were told to keep is a masterwork with a contested deed — and the accusation, true or not, is already a cloud. Do we hang it on faith, refuse it on a headline, or do what the great houses do — demand the chain of custody, price the title risk, insure what we can, and hold enough works of enough origins that no single disputed canvas can ever take the whole gallery down?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- The open-weight fallback we were told to keep now carries a **US distillation accusation** with **sanctions and Entity List** threats attached (Kratsios, Bessent, 22 July). **Do we treat model provenance as a governed attribute** — chain of custody, license, training-data origin, indemnity — for every model we deploy, or do we hang masterworks on faith?
- The expert pushback is substantive (the **1 July → 15 July** window makes strict distillation implausible; outputs aren't copyrighted). **Can we tell the difference between a real title defect and a political cloud** — and have we written down the reason we can defend for each model we run, rather than reacting to whichever headline is loudest?
- A self-hosted model is one we **cannot instantly un-hang.** **Have we provisioned more than one open-weight option of different provenance** (an MIT-licensed alternative alongside any contested one), with context and eval gate portable across them — so a sanctions designation is a switch, not a shutdown?

### 🏦 Financial Services
- Sanctions and Entity List exposure is a **compliance event,** not just a tech choice. **If a model we self-host were designated tomorrow, could we name every workflow it touches and cut over cleanly** — or is it wired so deep that a designation becomes an operational and regulatory incident?
- Vendor and model **due diligence** now includes AI provenance. **Do our third-party-risk and procurement checks capture a model's chain of custody, license and IP-indemnity posture** the way they capture a counterparty's — before it reaches production, not after an accusation?

### 🧬 Healthcare / Life Sciences
- Provenance discipline is the same instinct as **chain of custody** for a specimen or a data set. **Do we hold documented provenance for the open-weight models in our clinical or research stack** — origin, license, training-data claims — to the standard our regulators already expect for everything else?
- The masterwork may be brilliant *and* contested. **If our best-performing open model fell under a sanctions cloud, do we have a qualified, differently-sourced fallback** that keeps the service running without a scramble?

### 🏭 Manufacturing / Industrials
- The accusation bundles **distillation with export-controlled GB300 chips in Thailand** (Kratsios). **Is our AI supply chain — models and the hardware they were trained on — mapped well enough** that we would not be blindsided by a sanctions action against a component we depend on?
- Open weights are still the strongest hedge against lock-in. **Have we qualified at least two self-hostable open models of different provenance** (e.g. DeepSeek V4 under MIT alongside any Kimi K3 we vet) for the lines we cannot afford to have fenced *or* frozen?

### 🛒 Retail / Consumer
- A contested-provenance model in a **customer-facing** agent is a brand and legal exposure, not just a benchmark line. **Have we checked the license and provenance of the open model behind our storefront agent** — and could we swap it without rebuilding the experience?
- Provenance is now a buying criterion. **Do our model-selection rules weigh chain of custody and IP-indemnity,** so we are not one accusation away from pulling a live customer feature?

### 🏛️ Public Sector / Regulated
- Governments are treating AI provenance as **national-security and IP policy** ("open source is not open season on American IP" — Bessent). **For any citizen-facing or sovereign deployment, do we require documented provenance and a defensible license posture** for every model, including open weights?
- The EU AI Act's GPAI enforcement lands in **8 days,** and provenance is exactly the kind of evidence it expects. **Is our model inventory — origin, license, evaluation, audit log — built on infrastructure we own,** so we can answer a regulator about *where our models came from,* not only what they do?

---

## 4 · Technical Deep-Dive — The Masterwork, the Cloud, and the File

Read this week's story as a single lesson about **provenance as a governed attribute of a model,** in three parts — the masterwork (a capable open-weight model you would genuinely want), the cloud (a government accusation, contested, that threatens its title), and the file (the chain-of-custody discipline that lets you deploy brilliance without inheriting someone else's fight).

- **The masterwork (why this is a real temptation, not a curiosity).** Moonshot AI's **Kimi K3** is a **2.8-trillion-parameter open-weight** model whose full weights publish **27 July** under a **Modified MIT** license — self-hostable, frontier-class, cheap. It is exactly the "village green" yesterday's edition prescribed, and **DeepSeek V4** (open MoE, **MIT,** **~80.6% SWE-bench Verified,** ~**$0.87/1M output,** ~**29× cheaper** than Opus 4.8) sits beside it as a second. The pull toward self-hosting an open frontier model is real and, in most respects, correct.
- **The cloud (the accusation, and why it is contested).** On **22 July** OSTP Director **Michael Kratsios** posted that the US has "information that **Moonshot AI distilled Anthropic's Fable** for the development of its K3 model," via "a sophisticated internal platform to conduct **large scale distillation** against U.S. models, allowing them to quickly switch between multiple methods of access to **avoid detection,**" and that Moonshot "**accessed GB300s in Thailand**" despite export controls. Treasury's **Scott Bessent** attached the policy — *"Open source is not open season on American IP"* — and floated **sanctions and Entity List designations.** But the technical case, on what has been made public, is **thin:** the release window is brutal (**Fable public 1 July, K3 ~15 July**), a model's *outputs* are not copyrighted, distillation is **common** (Musk testified xAI distilled OpenAI to build Grok), and researcher **Braden Hancock** put it plainly — *"I don't think you get a model this strong and this quickly on the heels of Fable doing strictly distillation."* Anthropic, which in **February** accused DeepSeek, Moonshot and MiniMax of using **~24,000 fabricated accounts** for **>16 million** Claude interactions, has **not** publicly tied K3 to Fable. A cloud, in other words — real enough to freeze a sale, unresolved enough that betting either way is a gamble.
- **The file (the discipline that makes this manageable).** You are not the court, and you do not need to be. You need the collector's file for every model you deploy: **provenance** (who trained it, on what, under what claims), **license clarity** (Modified MIT is not MIT — read it), an **indemnity posture** (does anyone stand behind the IP, and what happens to *you* if a claim lands), and a **portability guarantee** (context, prompts and eval gate that move across models, so any one canvas can come down). With the file in hand, a government accusation against one model is a risk you can **price and route around,** not a surprise that strands a production system you cannot un-wire.

The strategic core: **provenance is now a first-class attribute of a model, alongside cost and capability.** After this week, "we self-host the best open model we found" is not a complete answer; *"we self-host models whose chain of custody, license and indemnity we have documented, we hold more than one of different origin, and our stack can swap them in a day"* is.

```
        THE PROVENANCE — hang the masterwork, but keep the file
        An open-weight fallback is only as safe as its chain of custody

   ┌─────────────────────────────────────────────────────────┐
   │  THE MASTERWORK  — a real, capable open-weight model      │  worth wanting
   │  Kimi K3: 2.8T open weights (27 Jul, 2d), Modified MIT     │
   │  DeepSeek V4: open MoE, MIT, 80.6% SWE-bench, ~29× cheaper │
   │  self-hostable · frontier-class · the "village green"     │
   └─────────────┬─────────────────────────────────────────────┘
                 │  but the deed is contested →
                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │  THE CLOUD  — a govt accusation, thin & contested         │  ⚠ TITLE DISPUTE
   │  US: Moonshot "distilled Anthropic's Fable" to build K3   │
   │  Bessent: sanctions & Entity List "on the table"          │
   │  pushback: Fable 1 Jul → K3 15 Jul · outputs not © ·      │
   │  distillation is common · Anthropic hasn't tied K3 to Fable│
   └─────────────┬─────────────────────────────────────────────┘
                 │  you are the collector, not the court →
                 ▼
   ┌───────────────────────────────────────┐
   │  KEEP THE FILE + THE PORTFOLIO        │  provenance = a governed attribute
   │  chain of custody · license read      │  demand the paper trail; price the
   │  indemnity posture · ≥2 greens of      │  title risk; hold more than one green
   │  different origin · portable eval gate │  so one disputed canvas ≠ dark gallery
   └───────────────────────────────────────┘

   TRAP: hang one contested masterwork you can't un-hang → one accusation darkens the gallery.
   WIN : keep the file and a diversified portfolio → a removed painting, not a shuttered museum.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — hang one contested masterwork | The discipline — keep the file and the portfolio |
|---|---|
| Self-host the best open model you found, no questions | Document provenance, license and training-data claims first |
| Treat "open weights" as if origin doesn't matter | Treat provenance as a governed attribute, like cost or capability |
| One open model wired deep into production | ≥2 self-hostable models of **different** origin, ready to swap |
| Context and eval gate coupled to one model | Portable context and eval gate — a switch, not a migration |
| React to whichever accusation is loudest | A defensible, written reason for every model you deploy |

### Why provenance became a survival attribute, not a compliance footnote

Every force this radar tracked all month — commodity models, open weights as the fallback (yesterday), cheap routing — pushes enterprises toward **self-hosting open models,** which is right. But self-hosting inverts one thing: you can walk away from an API in an afternoon, while a model **wired into your own infrastructure** is one you must actively un-wire. That is precisely where a **contested provenance** stops being the lab's problem and becomes the deployer's — sanctions, IP claims and procurement-trust questions land on whoever is *running* the weights. Provenance discipline is what converts that from an existential surprise into a priced, routed-around risk. That a government is threatening sanctions over a model's origins in the same week its weights hit the shelf is the signal that "where did this model come from?" now sits next to "what does it cost?" on the selection checklist.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure). Today adds the collector's discipline to yesterday's village green: an open-weight fallback is only as safe as its **chain of custody.** On legacy estates the danger is grabbing the flashiest open model because it tops a benchmark, wiring it deep, and discovering only when an accusation lands that you cannot prove its origin, cannot cite its license cleanly, and cannot swap it out in a week. The retrofit is the collector's file: **document provenance,** read the license, note the indemnity, provision a **second green of different origin,** and keep your context and eval gate portable — all riding the production stack you already built.

**The clean mental model:** *An open-weight model is a masterwork, and a masterwork is only as hangable as its provenance. Welcome the brilliance, demand the chain of custody, price the title risk, and never anchor the gallery on a single canvas whose deed you can't defend.*

### Watch list this week
- **The distillation accusation (22 July).** OSTP Director **Michael Kratsios** alleged Moonshot **distilled Anthropic's Fable** to build **Kimi K3** via a detection-evading platform, and **accessed export-restricted Nvidia GB300s in Thailand;** Treasury's **Scott Bessent** put **sanctions and Entity List designations** on the table (*"open source is not open season on American IP"*). The technical case, as made public, is thin.
- **The expert pushback.** Researchers called the claim thin and, in some cases, *"political"* and *"reckless"*: the **Fable-1-July → K3-15-July** window makes strict distillation implausible (**Braden Hancock:** *"I don't think you get a model this strong and this quickly… doing strictly distillation"*), model outputs aren't copyrighted, and distillation is common practice (Musk testified xAI distilled OpenAI for Grok). A Moonshot engineer: *"We trained a brand new frontier model in JUST 15 DAYS."*
- **The February backdrop.** Anthropic in **February 2026** accused **DeepSeek, Moonshot and MiniMax** of using **~24,000 fabricated accounts** to run **>16 million** Claude interactions in violation of its terms — but has **not** publicly tied **Kimi K3** specifically to Fable distillation.
- **The masterworks themselves.** **Kimi K3** — 2.8T-param open weights publish **27 July (2 days),** Modified MIT. **DeepSeek V4** — open MoE, **MIT,** ~**80.6% SWE-bench,** ~**$0.87/1M output,** ~**29× cheaper** than Opus 4.8 — the differently-sourced second green.
- **The standing countdowns — MCP final spec 28 July (3 days)** (the vendor-neutral interoperability layer) and **EU AI Act GPAI enforcement applicable 2 Aug (8 days)** (€15M or 3% of global turnover; powers to compel documentation, run independent evaluations and require mitigations — provenance is exactly the evidence it will expect).

---

## 5 · Quotes That Catch the Eye

> We have information that Moonshot AI distilled Anthropic's Fable for the development of its K3 model. To do this they developed a sophisticated internal platform to conduct large scale distillation against U.S. models, allowing them to quickly switch between multiple methods of access to avoid detection.
> — **Michael Kratsios, Director, White House Office of Science and Technology Policy**, on X, 22 July 2026 (as reported)

> Open source is not open season on American IP. When [Chinese] firms conduct covert, industrial-scale distillation attacks that cross the line into IP theft, sanctions and Entity List designations will be on the table.
> — **Scott Bessent, U.S. Treasury Secretary**, on X, July 2026 (as reported)

> I don't think you get a model this strong and this quickly on the heels of Fable doing strictly distillation.
> — **Braden Hancock, AI researcher**, on the claim that Kimi K3 was built primarily by distilling Anthropic's Fable, July 2026 (as reported)

> Fable went public on July 1 and K3 launched on July 15. We trained a brand new frontier model in JUST 15 DAYS.
> — **A Moonshot AI engineer (Randy Xian)**, disputing the distillation timeline, July 2026 (as reported)

> "An open-weight model is a masterwork, and a masterwork is only as hangable as its provenance. Welcome the brilliance, demand the chain of custody, and never anchor the gallery on a single canvas whose deed you can't defend."
> — *the radar, on the provenance*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Date the US alleged Moonshot distilled Anthropic's Fable to build K3 | **22 Jul 2026** | Kratsios (White House OSTP), via coverage (as reported) |
| US response floated for confirmed "IP theft" distillation | **Sanctions + Entity List** | Bessent (US Treasury), via coverage (as reported) |
| Fabricated accounts Anthropic attributed to 3 Chinese labs (Feb 2026) | **~24,000** | Anthropic, via coverage (as reported) |
| Claude interactions those accounts generated | **>16 million** | Anthropic, via coverage (as reported) |
| Fable 5 public release → Kimi K3 launch window | **1 Jul → ~15 Jul (~15 days)** | coverage (as reported) |
| Kimi K3 parameters / license | **2.8T / Modified MIT** | Moonshot / coverage (as reported) |
| Kimi K3 full open weights publish | **27 Jul 2026 (2 days)** | Moonshot / coverage |
| DeepSeek V4-Pro on SWE-bench Verified (top open-weights) | **80.6%** | DeepSeek / coverage (as reported) |
| DeepSeek V4-Pro output price / vs Opus 4.8 | **$0.87 per 1M / ~29× cheaper** | coverage (as reported) |
| DeepSeek V4-Pro architecture / license | **1.6T MoE (49B active) / MIT** | DeepSeek / coverage |
| Enterprises that can actually govern their AI agents | **12%** | OutSystems, ~1,900 IT leaders (as reported) |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |
| MCP's largest revision goes final | **28 Jul 2026 (3 days)** | Model Context Protocol blog |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (8 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Open the file — make provenance a governed attribute of every model you run.** Before any open-weight model reaches production, document its **chain of custody:** who trained it, the **license read in full** (Modified MIT ≠ MIT), the training-data claims, and the **indemnity posture** (who, if anyone, stands behind the IP — and what a claim would cost *you* as the deployer). Add "model provenance" to your third-party-risk and procurement checklist next to cost and capability. A masterwork you can't document is a masterwork you shouldn't hang.

2. **Diversify the gallery — hold at least two greens of different origin.** Don't anchor a critical workflow on a single open model, least of all one under a live sanctions cloud. This quarter, **qualify two self-hostable open-weight models of different provenance** (e.g. MIT-licensed **DeepSeek V4** alongside any **Kimi K3** you vet), and keep your **context, prompts and eval gate portable** across them, so swapping one out is a switch, not a migration. Then an Entity List designation or an IP fight is a removed canvas, not a dark gallery.

3. **Price the title risk — and rehearse the un-hang.** Run the tabletop: *if a model we self-host were sanctioned or IP-challenged tomorrow, could we name every workflow it touches and cut over to the alternative in a week?* Write down the blast radius, the fallback, and the cutover steps now — and fold model origin and license into the **EU AI Act evidence** you owe before enforcement lands in 8 days. Provenance discipline is cheapest to build before the accusation, not after.

---

*AI Tech Radar · generated 25 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The technical and market facts are relayed from public coverage and are marked "as reported" where they rest on secondary reporting: the 22 July 2026 statements by White House OSTP Director Michael Kratsios (that the US has information Moonshot AI distilled Anthropic's Fable to build Kimi K3 via a purpose-built, detection-evading distillation platform, and that Moonshot accessed export-restricted Nvidia GB300 chips in Thailand) and by Treasury Secretary Scott Bessent ("open source is not open season on American IP," with sanctions and Entity List designations "on the table") are relayed from Kratsios's and Bessent's posts on X and from 21–23 July 2026 coverage (TechCrunch, CyberScoop, Cryptopolitan, Cryptobriefing, SiliconANGLE, Seeking Alpha, The Hill, SCMP, CNBC, Gizmodo, Quartz). The expert pushback — that the Fable-1-July / K3-~15-July window makes large-scale distillation implausible; that model outputs are not copyrighted; that distillation is a common industry practice (Elon Musk having testified that xAI distilled OpenAI models to build Grok); the direct quote attributed to researcher Braden Hancock; and the Moonshot engineer's "brand new frontier model in JUST 15 DAYS" retort — is relayed from 23 July 2026 coverage (TechCrunch, South China Morning Post, AI Weekly, Bitcoin World, PetaPixel). Anthropic's February 2026 allegation that DeepSeek, Moonshot AI and MiniMax used approximately 24,000 fabricated accounts to generate more than 16 million Claude interactions in violation of its terms — and the fact that Anthropic has not publicly connected Kimi K3 specifically to Fable — are relayed from Fortune and July 2026 coverage. Kimi K3's specifications (2.8T parameters, full open weights publishing 27 July 2026 under a Modified MIT license) are Moonshot AI's, relayed via coverage. DeepSeek V4 specifications (open-weight MoE, 1.6T total / 49B active parameters, MIT license, ~80.6% SWE-bench Verified as the top open-weights entry, ~$0.87/1M output, ~29× cheaper per output token than Claude Opus 4.8) are relayed from vendor and coverage sources (DeepSeek, morphllm, DataCamp, Codersera, OpenRouter). The OutSystems 12%-can-govern and Gartner >40%-cancelled figures are relayed from prior 2025–2026 research and coverage. The MCP 2026-07-28 final-spec date is the MCP project's; the EU AI Act mechanics are the European Commission's. The "2 days," "3 days" and "8 days" figures are simple counts from this edition's date (25 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own. The provenance allegory — the art-market principle that a painting's value and title depend on an unbroken, documented chain of custody; that a contested or broken provenance freezes a sale and depresses value regardless of the work's beauty; that provenance disputes can be either genuine theft or thin and political; and that serious collectors survive by demanding the file, insuring title, and diversifying rather than anchoring a collection on one disputed work — is the radar's own illustration, told approximately, and is not a sourced claim about any specific artwork or about AI.*
