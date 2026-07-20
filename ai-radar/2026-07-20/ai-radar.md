# 🛰️ AI Tech Radar — The Signet Ring

**Monday, 20 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar watched the value settle onto the **triage tent** — the routing layer that decides *which model* touches *which task,* the day after Kimi K3 made the model itself a commodity. Today the question moves one turn deeper: not which model does the work, but **how much authority the work is allowed to carry.** In the last two weeks three jurisdictions converged on the same demand — that an autonomous agent acting in your name must operate under a **defined, pre-agreed, logged grant of authority.** China's rules, in force **five days ago (15 July),** are the world's first to write it into law: a **three-tier decision-authorization framework** that sorts every agent action by consequence and scales the human sign-off to match. Illinois signed a frontier-audit law (**6 July**); the **EU AI Act's GPAI enforcement lands in 13 days (2 Aug).** The board's question sharpens: ***when an agent acts in our name, have we decided in advance which decisions it may make alone, which need a human, and which need the equivalent of the Great Seal — and do we keep the record of every act it took in our name?***

---

## 1 · Executive Summary (90-second read)

For three weeks this radar has argued one thesis — *the model is commoditizing; own and govern the layer around it.* Yesterday the value settled on the **routing layer** (19 Jul, "the triage tent"). Today it moves to the layer above routing: **authorization** — the grant of decision authority an agent wields when it acts in your name. And this week that layer stopped being a best practice and became **law.** China's **Implementation Opinions on the Standardized Application and Innovative Development of Intelligent Agents** (CAC with NDRC and MIIT) took effect **15 July** — the **world's first dedicated regulatory category for AI agents** — mandating a **three-tier decision-authorization framework** that classifies every agent action by consequence and scales human approval accordingly. Illinois enacted the first US state **frontier-model audit law** (SB 315, signed **6 July**). And the **EU AI Act's GPAI enforcement becomes applicable on 2 August — 13 days** — with fines to €15M or 3% of global turnover. The two standing countdowns still run beneath it: **Kimi K3's open weights on 27 July (7 days)** and **MCP's final spec on 28 July (8 days).**

1. **An autonomous agent acts *in your name* — and three regulators just made that a governed act.** China's rules define an agent as a system capable of **"autonomous perception, memory, decision-making, interaction, and execution"** and require a **three-tier authorization structure:** low-consequence actions the agent may take alone, consequential actions that need a human, and high-consequence actions that need a scaled, senior sign-off — plus **mandatory filing, compliance testing and product-recall** provisions for high-risk sectors (healthcare, transport, media, public safety). This is the graduated grant of authority — the **signet, the privy seal, and the Great Seal** — written as statute.

2. **The value (and the compliance) is in the authorization layer, not the model.** Gartner still expects **40% of enterprise apps to embed task-specific agents by end-2026** (from <5% in 2025) and **>40% of agentic projects cancelled by end-2027.** The projects that survive won't be the ones with the best model — after Kimi K3 everyone rents or downloads that — but the ones that can **say, and prove, exactly how much authority each agent holds.** Yesterday's triage tent sorted *which model;* today's signet ring sorts *which decisions an agent may make alone* — both are governance of the layer, not the metal.

3. **A grant of authority that isn't recorded isn't a grant — it's an exposure.** The other half of every one of these regimes is the **roll:** China's mandatory filing and recall powers, Illinois's **72-hour critical-incident reporting** and annual **third-party audit,** the EU's power to compel documentation (Art. 91), run evaluations (Art. 92) and demand mitigations (Art. 93). The authorization layer is the one place that sees every decision an agent takes in your name — which makes it the only place you can *keep the roll* the regulator will ask for. Build it and you have your evidence; skip it and you've handed out your seal with no record of who used it.

**Bottom line:** yesterday the value settled on the routing tent; today it moves to the **signet ring** — the graduated, pre-agreed, logged grant of authority under which an agent may act in your name. When an agent can perceive, decide and execute autonomously, "which model" is a commodity question; **"how much authority, and who signs off when it matters"** is the one three regulators are now enforcing. **Decide the grant in advance. Scale the sign-off to the consequence. Keep the roll.** The model you rent by the token; the authority is yours to grant — and, now, yours to prove.

---

## 2 · Allegory of the Day — "The Signet Ring"

*Topic: In the last two weeks three jurisdictions converged on a single requirement — that an autonomous AI agent acting on an organization's behalf must operate under a defined, graduated, auditable grant of decision authority. China's Implementation Opinions on intelligent agents (CAC/NDRC/MIIT), effective 15 July 2026, are the world's first to codify it: a three-tier decision-authorization framework that scales human sign-off to the consequence of the action, with mandatory filing and recall for high-risk sectors. Illinois enacted a frontier-audit law (6 July); the EU AI Act's GPAI enforcement becomes applicable 2 August. The lesson for the enterprise: when a machine can act in your name, the value and the liability both live in the grant of authority you define in advance — and in the record you keep of every act taken under it.*

For most of recorded history, a ruler who could not be in two places at once governed through a **seal.** A signet ring pressed into hot wax did something almost magical: it made a document act *as if the sovereign's own hand had signed it.* The bearer of the seal wielded the ruler's authority. Which is why, in any well-run realm, the seal was never a single thing casually lent. The English crown kept a **ladder of seals.** Routine business moved under the **signet** and the **privy seal** — a clerk could act, a minor writ could issue, and the kingdom did not have to wait on the king. But the gravest acts — a treaty, a grant of land, a writ that could end a life — required the **Great Seal of the Realm,** and the Great Seal did not travel in a courtier's pocket. It was held by the **Lord Chancellor,** applied with ceremony, and never to routine work. The higher the consequence, the higher the seal, and the higher the seal, the more senior the human who had to be present when it was pressed.

Two things made the system trustworthy, and both are the parts people forget. The first is that every sealed act was **entered on a roll** — the Chancery kept the Patent Rolls and the Close Rolls, a permanent, ordered record of every instrument issued in the sovereign's name. You could always go back and ask: *by whose authority, and under which seal, was this done?* The second is that the grant could be **revoked.** A seal could be recalled from a deputy who abused it; and when a reign ended, the Great Seal was ceremonially **defaced** — broken — so that no one could ever again act in the dead king's name. The authority was real, but it was leased, logged, and revocable.

Here is the part the board must sit with. The power of the seal was never in the wax or the silver. It was in the **discipline around it:** the ladder that matched the seal to the consequence, the officer who had to be present for the gravest acts, the roll that recorded every use, and the ability to break the ring when trust was gone. An autonomous agent is a signet ring you hand to a machine. China's three-tier framework is, almost literally, the crown's ladder of seals rewritten for software: routine actions under the signet (the agent acts alone), consequential ones under the privy seal (a human approves), the gravest under the Great Seal (a scaled, senior sign-off) — with a filing that is the roll and a recall power that is the breaking of the ring.

**The moral:** when a machine can act in your name, do not ask first *how capable* it is — everyone's ring is cast from the same cheap metal now. Ask *how much of your authority it carries, and under which seal.* Build the **ladder of seals:** define, in advance, which decisions an agent may make alone, which need a human, and which need the equivalent of the Great Seal and the officer who holds it. Then — the half most will skip — **keep the roll,** because a grant of authority you cannot reconstruct is not a grant, it is an exposure. And keep the power to **break the ring.**

**The question it forces:** *When an agent acts in our name, have we defined the ladder of seals — which decisions it may make alone, which require a human, which require senior sign-off — scaled to the consequence, the way China now requires and the EU will enforce in 13 days? And do we keep the roll of every act taken under our seal, ready to show the auditor — and can we break the ring the moment we need to?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- Three jurisdictions in two weeks now demand a **graduated, logged grant of authority** for agents (China's three-tier rule is in force; the EU enforces in 13 days). **Can we state, per agent, which decisions it may make alone, which need a human, and which need senior sign-off** — or have we handed out our seal with no ladder and no roll?
- Gartner expects **40% of enterprise apps to carry agents by end-2026** and **>40% of agentic projects to be cancelled by 2027.** **Is our differentiation the authorization layer we own** — the rules that decide how much authority each agent wields — rather than the model, which every rival can now rent or download?
- China's rule pairs authorization with **mandatory filing and a recall power;** the EU with documentation, evaluation and mitigation powers. **Do we keep an auditable roll of every consequential act an agent took in our name, and can we revoke an agent's authority instantly** — or would a regulator's request find no record and no off-switch?

### 🏦 Financial Services
- A trading, credit or payments agent that can **"decide and execute" autonomously** is exactly the high-consequence case these rules target. **Have we set hard authorization tiers** — a spending/limit ladder where beyond a threshold a human must sign — and is every override logged to the standard an auditor (or the EU AI Act, in 13 days) will demand?
- Illinois now requires **72-hour critical-incident reporting** for large frontier developers, and the direction of travel reaches deployers. **Do we have a defined "critical AI incident" trigger and a clock** — or would an agent overstepping its authority surface days late, through a customer complaint rather than our own roll?

### 🧬 Healthcare / Life Sciences
- China explicitly names **healthcare** a high-risk sector requiring filing and compliance testing for agents. **Have we drawn the line where a clinical or diagnostic agent must stop and hand to a human,** and is that hand-off a logged, enforced authorization checkpoint rather than an advisory note?
- A cheap, always-on agent multiplies the places an autonomous decision touches a patient. **Does every consequential clinical action carry the equivalent of a Great-Seal sign-off** — a named human, recorded on the roll — or does the agent's authority quietly scale with its convenience?

### 🏭 Manufacturing / Industrials
- On the shop floor an agent may adjust a setpoint, hold a line, or trigger maintenance. **Have we mapped which OT actions an agent may take alone and which require a human** — the three-tier ladder applied to physical consequence — and is the boundary enforced in the control layer, not just documented?
- Your moat is **process authority, not the model.** **Does our authorization layer encode our own judgment of which decisions are safe to delegate** — the proprietary escalation rules a competitor can't copy — or have we let a vendor's default decide how much autonomy runs the plant?

### 🛒 Retail / Consumer
- Customer-facing agents already issue refunds, change orders and make promises in your name. **Have we set the authorization ladder** — the value or risk threshold beyond which a human approves — so a persuaded or manipulated agent can't commit the brand to something it shouldn't?
- A grant of authority is only as good as its **record and its revocation.** **Can we show which agent took which customer-facing action under what authority, and pull an agent's seal in minutes** if it starts misbehaving during peak?

### 🏛️ Public Sector / Regulated
- China's rules make agent authorization a **filed, testable, recallable** matter of law for sensitive sectors — the template others will copy. **For any agent touching citizen data or a citizen decision, have we defined the seal it acts under, filed the record, and preserved the recall** the way a public body must?
- The EU AI Act gives the AI Office powers to **compel documentation, run evaluations and demand mitigations** in 13 days. **Is our authorization layer keeping the roll** — which agent, which decision, whose sign-off — ready to produce on request, rather than reconstructed after the fact?

---

## 4 · Technical Deep-Dive — The Ladder, the Officer, and the Roll

Strip the jurisdictions apart and China, Illinois and the EU are converging on one architectural claim: **when a machine can act autonomously in your name, the governed object is not the model — it is the grant of authority.** Read it as the crown's seal discipline in three parts — the ladder that matches authority to consequence, the officer who must be present for the gravest acts, and the roll that records every use.

- **The ladder (graduated authorization — the actual control).** China's three-tier framework classifies every agent action by consequence and scales the human approval to match: routine acts run under the **signet** (the agent acts alone), consequential acts need the **privy seal** (a human in the loop), and the gravest, most irreversible acts need the **Great Seal** (a senior, scaled sign-off). The engineering point is that this is a *property of the authorization layer,* not the model: the same frontier model can run at any tier, and it is your ladder — not the vendor's — that decides how much authority a given task carries.
- **The officer (human sign-off, present by design).** The Great Seal never travelled without the Chancellor. The equivalent is a **named, present human** on the high-consequence tier — not a notification that can be swiped away, but an enforced checkpoint the agent cannot pass alone. This is exactly the "human oversight" the EU AI Act makes a deployer duty, and exactly the authority-limit China now requires you to *document and enforce before deployment.*
- **The roll (the record — the half most skip).** Every sealed act went on the Chancery rolls. The authorization layer is the one vantage point that sees every decision an agent takes in your name, which makes it the only place you can keep the roll: which agent, which action, under which seal, with whose sign-off. That roll *is* your evidence for Illinois's **72-hour incident report,** China's **filing,** and the EU's **documentation and evaluation** powers. And it is what makes the last power — **breaking the ring,** revoking an agent's authority — auditable rather than improvised.

The strategic core: **an authorization layer is a moat if it is graduated, enforced and recorded, and a liability if authority is flat, implicit and unlogged.** After Kimi K3 and the triage tent, "we have (or route to) the best model" is not a defense; *"we can state and prove exactly how much authority each agent holds, and revoke it"* is.

```
        THE SIGNET RING  —  when a machine acts in your name, govern the grant of authority
        China's 3-tier rule (in force 15 Jul) scales the human sign-off to the consequence of the act

   ┌───────────────────────────┐        THE LADDER OF SEALS (the control)
   │  THE FLOOD OF AGENT        │        ┌───────────────────────────────────────────┐
   │  DECISIONS                 │        │  ① SIGNET  — routine / low consequence      │
   │  reads, drafts, lookups,   │ ─────▶ │     agent acts ALONE · logged               │
   │  refunds, scheduling,      │        ├───────────────────────────────────────────┤
   │  setpoints, deploys,       │        │  ② PRIVY SEAL — consequential               │
   │  payments, clinical acts   │        │     a HUMAN approves · logged               │
   └───────────────────────────┘        ├───────────────────────────────────────────┤
                                         │  ③ GREAT SEAL — grave / irreversible        │
                                         │     SENIOR sign-off + filing · the officer  │
                                         │     is present (EU human-oversight duty)    │
                                         └──────────────────┬────────────────────────┘
                                                            │  every act →
                                            ┌───────────────▼───────────────┐
                                            │  THE ROLL  (the record)        │  which agent, which act,
                                            │  every sealed act recorded     │  under which seal, whose
                                            │  filing · 72h incident report  │  sign-off → your EU AI Act
                                            │  → auditable, and revocable    │  evidence (13 days)
                                            └───────────────────────────────┘
                                                            │
                                            ┌───────────────▼───────────────┐
                                            │  BREAK THE RING (revocation)   │  pull an agent's authority
                                            │  recall power · kill-switch    │  the instant trust is gone
                                            └───────────────────────────────┘

   TRAP: hand every agent one flat, implicit, unlogged grant → fast, and an ungoverned power of attorney.
   WIN : a ladder of seals that scales sign-off to consequence, keeps the roll, and can break the ring.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — capability is the question | The discipline — authority is the question, and it's graduated |
|---|---|
| "We use the most capable agent" | We know exactly how much authority each agent holds |
| One flat grant: the agent may do whatever it can | A ladder: alone / human-approved / senior sign-off, by consequence |
| Human oversight is a notification you can swipe away | The officer is present by design on the top tier — an enforced checkpoint |
| Actions happen; nobody keeps the record | Every consequential act on the roll — your filing and audit evidence |
| No way to pull authority fast | Break the ring: instant, auditable revocation |

### Why a cheaper, more autonomous agent grows the governance surface, not shrinks it

The same forces this radar has tracked all fortnight — commodity models (Kimi K3, 7 days), standardized plumbing (MCP, 8 days), cheap routing (yesterday's triage tent) — all point one way: **more agents, taking more actions, more autonomously, for less money.** Every one of those is a decision taken in your name. When each action was expensive and slow, scarcity was the natural governor on how much authority an agent effectively wielded. Make agents cheap and continuous and that governor disappears — which is precisely why China, Illinois and the EU are moving the governor *into law* as an explicit, graduated, logged grant of authority. The authorization layer is the only place that sees all of it, which is why it must be where you set the ladder and keep the roll.

### How it lands on legacy estates

This is the same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the spend meter, 7 Jul the model-neutral router, 8 Jul the MCP control plane, 9 Jul the deployment-labor market, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe that walks out, 13 Jul govern the goal not the gauge, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent). Today names the layer above routing: **the signet ring** — the grant of authority. On legacy estates the danger is an agent wired straight into a system of record with a **flat, implicit grant** — it can do whatever the credentials it inherited can do — and no vantage point that sees, tiers, or logs the decisions it takes. The retrofit is the control plane this radar has urged all fortnight, now aimed at authority: a **decision-authorization ladder** that scales sign-off to consequence; the **officer** (an enforced human checkpoint) on the top tier; a **roll** (the audit ledger, doubling as your EU AI Act evidence); and a **break-the-ring** revocation path wired to every agent identity.

**The clean mental model:** *An autonomous agent is a signet ring you hand to a machine. Decide in advance which seal it may use for which decision, keep the officer present for the gravest acts, record every use on the roll, and keep the power to break the ring.*

### Watch list this week
- **China — Implementation Opinions on intelligent agents (in force 15 July, 5 days ago).** Issued by the **CAC with the NDRC and MIIT;** the **world's first dedicated regulatory category for AI agents.** Defines agents as systems capable of **autonomous perception, memory, decision-making, interaction and execution;** mandates a **three-tier decision-authorization framework** scaling human approval to consequence; requires **filing, compliance testing and product-recall** for high-risk sectors (healthcare, transport, media, public safety).
- **Illinois — AI Safety Measures Act (SB 315, signed 6 July).** First US state to require **annual independent third-party audits** of frontier models by "large frontier developers" (**>$500M** annual revenue); published catastrophic-risk frameworks; **72-hour** critical-incident reporting; requirements effective **1 Jan 2028.** Anthropic backed it as a baseline.
- **The mandatory counterweight — EU AI Act GPAI enforcement applicable 2 Aug 2026 (13 days).** €15M or 3% of global turnover (Art. 101); the AI Office can compel documentation (Art. 91), run evaluations (Art. 92) and require mitigations (Art. 93); obligations flow down to deployers. Makes existing GPAI duties enforceable — no grace period for models placed on the market on/after 2 Aug 2025.
- **The commodity underneath — Kimi K3's open weights publish 27 July (7 days),** the self-hostable floor that makes more, cheaper, more autonomous agents inevitable — and the ladder of seals necessary.
- **The connector counterpart — MCP 2026-07-28 spec goes final in 8 days** (stateless core, Enterprise-Managed Authorization stable, MCP Apps); the plumbing every agent acts through, standardizing as authorization becomes the battleground.
- **Adoption cadence** — Gartner: 40% of enterprise apps embed task-specific agents by end-2026 (from <5% in 2025); >40% of agentic projects cancelled by end-2027 — governance and authority, not model access, remain the constraint.

---

## 5 · Quotes That Catch the Eye

> [Intelligent agents are systems capable of] autonomous perception, memory, decision-making, interaction, and execution.
> — **China's Implementation Opinions on intelligent agents** (CAC/NDRC/MIIT), effective 15 July 2026 (as reported)

> [The Illinois law] takes the safety practices leading labs already follow voluntarily — publishing a safety framework, transparent reporting, protecting whistleblowers — and helps establish a baseline that every leading AI developer is expected to meet.
> — **Anthropic**, on the Illinois AI Safety Measures Act, July 2026 (as reported)

> With federal AI legislation unlikely in the near-term, these states have effectively created a national compliance standard.
> — **Coverage of the US state AI laws**, July 2026 (as reported)

> Enterprise AI's center of gravity shifts from models to orchestration, governance, and ROI clarity.
> — **Enterprise-AI commentary**, July 2026 (as reported)

> "When a machine can act in your name, capability is the commodity — the grant of authority is the moat. Decide the seal in advance, keep the officer present, and keep the roll."
> — *the radar, on the authorization layer*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| China's agent rules (world-first agent category) in force | **15 Jul 2026 (5 days ago)** | CAC / NDRC / MIIT (as reported) |
| Decision-authorization tiers China now mandates | **3** | CAC Implementation Opinions (as reported) |
| Illinois AI Safety Measures Act (SB 315) signed | **6 Jul 2026** | State of Illinois / coverage |
| Illinois "large frontier developer" revenue threshold | **>$500M** | SB 315 (as reported) |
| Illinois critical-safety-incident reporting window | **72 hours** | SB 315 (as reported) |
| Illinois audit requirements take effect | **1 Jan 2028** | SB 315 (as reported) |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (13 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |
| Kimi K3 full open weights (Modified MIT) publish | **27 Jul 2026 (7 days)** | Moonshot / coverage |
| MCP's largest revision goes final | **28 Jul 2026 (8 days)** | Model Context Protocol blog |
| Enterprise apps embedding task-specific agents by end-2026 | **40%** (from <5% in 2025) | Gartner |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Draw the ladder of seals — per agent, before the next deploy.** Take every agent already acting in your name and classify its actions by consequence into three tiers: what it may do **alone** (routine, reversible), what needs a **human** (consequential), and what needs a **senior, named sign-off** (grave, irreversible). This is exactly what China now requires you to *document and enforce before deployment* — and it is a property of your authorization layer, not the model, so it survives every model swap.

2. **Put the officer on the top tier, and keep the roll.** For the highest-consequence tier, wire an **enforced human checkpoint** the agent cannot pass alone — present by design, not a swipe-away alert — and **log every consequential act** (which agent, which action, under which seal, whose sign-off). That roll is your evidence for Illinois's 72-hour incident report, China's filing, and the EU's documentation and evaluation powers on **2 August (13 days)** — one build, three regimes.

3. **Build the break-the-ring path now.** A grant of authority you cannot revoke is not governance. Before enforcement lands, make sure you can **pull any agent's authority in minutes** — a kill-switch wired to agent identity, tested — and name who can pull it. When trust in an agent goes, you want to break the ring on purpose and on the record, not scramble for it while the roll fills with acts you never authorized.

---

*AI Tech Radar · generated 20 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The regulatory facts are relayed from public sources and coverage and marked "as reported" where they rest on secondary reporting: China's Implementation Opinions on the Standardized Application and Innovative Development of Intelligent Agents (issued by the CAC with the NDRC and MIIT; effective 15 July 2026; described as the world's first dedicated regulatory category for AI agents; defining agents by autonomous perception, memory, decision-making, interaction and execution; mandating a three-tier decision-authorization framework and, for high-risk sectors including healthcare, transport, media and public safety, filing, compliance testing and product-recall provisions) are relayed from coverage (AI Governance Institute, Global Law Experts, IAPP, Rimon Law, Cointribune and others). The Illinois AI Safety Measures Act (SB 315, signed by Governor JB Pritzker on 6 July 2026; applying to "large frontier developers" with more than $500M in annual gross revenue; requiring annual independent third-party audits, published catastrophic-risk frameworks, and 72-hour critical-safety-incident reporting; with requirements taking effect 1 January 2028; supported by Anthropic) is relayed from coverage (The Hill, Crowell & Moring, Norton Rose Fulbright, StateScoop, Capitol News Illinois, Hunton and others). The EU AI Act mechanics (GPAI enforcement applicable 2 August 2026; €15M or 3% of global turnover; Articles 91–93 and 101; no grace period for models placed on the market on/after 2 August 2025; obligations reaching deployers) are relayed from the European Commission and analysis (artificialintelligenceact.eu, beam.ai, ComplianceHub, Pearl Cohen). The Kimi K3 open-weights date (27 July 2026) is Moonshot AI's, relayed via coverage; the MCP 2026-07-28 final-spec date is the MCP project's. The Gartner figures (40% of enterprise apps embed task-specific agents by end-2026, up from <5% in 2025; >40% of agentic-AI projects cancelled by end-2027) are Gartner's. The "5 days," "7 days," "8 days" and "13 days" figures are simple counts from this edition's date (20 July 2026) to 15 July, 27 July, 28 July and 2 August 2026 respectively and are the radar's own. The signet-ring allegory — the medieval English ladder of seals (signet, privy seal, and the Great Seal of the Realm held by the Lord Chancellor), the Chancery rolls (Patent and Close Rolls) as a record of sealed acts, and the ceremonial defacing of the Great Seal at the end of a reign — is the radar's own historical illustration, told approximately, and is not a sourced claim about AI.*
