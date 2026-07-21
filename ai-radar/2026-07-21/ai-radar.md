# 🛂 AI Tech Radar — The Passport

**Tuesday, 21 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar watched the value settle onto the **signet ring** — the graduated, logged grant of authority under which a machine may act in your name. Today the question moves one step earlier in the chain: not *how much* authority the seal carries, but ***whose hand wears the ring*** — and *where* you check. This week a frontier vendor answered it in architecture. Google's new **Gemini Enterprise Agent Platform** gives every agent a **unique, cryptographically attested identity** (built on the open **SPIFFE** standard) and enforces it — with mutual-TLS and a unified **Agent Gateway** — **below the application tier, as an infrastructure primitive.** The reported contrast is the whole story: rivals position agent governance **at the application tier** — the front desk — where the agent is already inside the walls. Meanwhile the population you must identify has quietly inverted: **non-human identities now outnumber humans by roughly 45-to-1, and up to 109-to-1** in the average enterprise. The board's question sharpens: ***every agent in our estate is a traveler acting under someone's name — do we issue it a verifiable, expiring, revocable passport, and do we check that passport at the border, or only at the front desk after it's already inside?***

---

## 1 · Executive Summary (90-second read)

For three weeks this radar has argued one thesis — *the model is commoditizing; own and govern the layer around it.* Yesterday the value settled on **authorization** — the signet ring, the graduated grant of decision-authority (19 Jul was routing; 20 Jul was authority). Today it moves one link earlier: **identity.** A grant of authority is meaningless if you cannot prove *who is holding it,* and this week the identity layer became a shipping architecture. Google's **Gemini Enterprise Agent Platform** assigns every agent a **unique, cryptographically attested identity** on the **SPIFFE** standard, signs and logs **every** API call, data access and file operation to that identity, and enforces it with **mTLS** through an **Agent Gateway** — placed **below the application tier as an infrastructure primitive.** The reported architectural break with rivals: Anthropic and OpenAI have positioned agent-governance controls **at the application tier.** The stakes are set by a population inversion — **non-human identities (NHIs) now outnumber humans ~45:1 (Rubrik), and 109:1 in the average enterprise, up from 82:1 a year ago (Palo Alto Networks)** — while **78%** of organizations have no documented policy even to create or retire them. The standing countdowns run beneath: **Kimi K3's open weights on 27 July (6 days),** **MCP's final spec on 28 July (7 days),** and the **EU AI Act's GPAI enforcement on 2 August (12 days).**

1. **A grant of authority is only as good as the identity that holds it.** Yesterday's signet ring decided *how much* an agent may do in your name; today's question is *whose name, provably.* The industry answer is now explicit: **an agent is a first-class non-human identity** — its own principal, **cryptographically attested, short-lived at runtime, with the human preserved as the delegating subject via token exchange.** Google, Microsoft and AWS all shipped a version of this in the last two quarters; Gemini Enterprise is the sharpest statement of it because it puts the check **below the application tier.**

2. **The border, not the front desk.** The whole architectural argument reduces to *where* identity is verified. Enforce it at the **application tier** — the front desk, the dashboard — and the agent is already inside your walls before anyone asks who it is; a swipe-away control, easy to route around. Enforce it **below the application tier** — the border — with cryptographic identity and mTLS on **every** call, **regardless of how the agent was built or by whom,** and an unidentified or expired traveler never crosses. This is the same lesson as yesterday's roll, one layer down: value and liability both live in the layer you own, and identity is the layer under authority.

3. **The population already inverted — and it is ungoverned.** NHIs outnumber humans by **45:1 to 109:1** (up to **144:1** in cloud-native estates), **78%** of organizations have no documented policy to create or remove them, and about **two-thirds** have already suffered a breach through a compromised non-human identity. Adoption confirms the gap: **96%** of enterprises run AI agents, but only **12%** have a centralized platform to govern them and **94%** say sprawl is compounding security risk (OutSystems, 1,879 IT leaders). You are already running an unbordered realm full of unidentified travelers.

**Bottom line:** yesterday the value settled on the signet ring — the grant of authority. Today it moves to the **passport** — the verifiable, expiring, revocable *identity* that carries the seal, and the **border** where you check it. When agents outnumber your people 45-to-1 and every one acts under some name, "how capable is the model" is a commodity question; **"can we prove whose identity took this action, and did we verify it at the border or the front desk"** is the one that decides whether your roll is evidence or fiction. **Issue every agent a passport. Name its human sponsor. Check it at the border. Keep the manifest — and be able to seize the passport.**

---

## 2 · Allegory of the Day — "The Passport"

*Topic: This week Google's Gemini Enterprise Agent Platform made agent identity an infrastructure primitive — every agent gets a unique, cryptographically attested identity on the SPIFFE standard, every action is signed and logged to it, and it is enforced with mutual-TLS through an Agent Gateway placed below the application tier, so governance holds regardless of how the agent was built. Coverage frames this as a deliberate break from rivals, who position agent-governance controls at the application tier. It lands as non-human identities outnumber humans by 45-to-1 (and up to 109-to-1 in the average enterprise), while most organizations lack any documented policy to issue or revoke them. The lesson for the enterprise: when the machines acting in your name outnumber your people many times over, the value and the liability live in the identity you can verify — and in where you verify it.*

For most of history you could cross a frontier on your face and your word. Then realms grew crowded, and the crowd made the word worthless — too many travelers, too many claiming to be someone they were not. So the sovereign issued a **passport:** a document that did two things a spoken claim could not. It **named** the bearer and **vouched** for them — *let this person pass; they travel under our protection* — and it was **verifiable,** sealed and later stamped and photographed, so that a guard could *authenticate* it rather than simply believe it. A passport was never a mere convenience. It was the difference between a realm that knew who was inside it and one that merely hoped.

Four disciplines made the passport trustworthy, and they are exactly the parts a modern estate forgets. First, it was **issued by an authority,** not self-declared — you did not write your own. Second, it **named a sponsor** — the state, or the noble, whose protection you carried, so that authority was always traceable back to a responsible party. Third, it **expired** — a safe-conduct was good for a season and a route, not forever, because a credential that never lapses is a key that never stops opening the door. And fourth — the one everyone skips — it was checked **at the border.** The guard at the gate, whose only job was to verify identity, decided who entered the realm. The innkeeper, deep inside the walls, merely wrote your name in his ledger *after* you had already arrived. A realm that checked papers only at the front desk of each inn had no border at all: anyone who slipped the gate roamed free, and a forged or expired paper was caught, if ever, by a clerk with no power to turn anyone away.

Here is the part the board must sit with. An autonomous agent is a traveler you have let loose in your realm — and there are now forty-five of them for every one of your people, in some estates more than a hundred. Yesterday you decided how much authority each traveler's seal could carry. But a seal is worthless if you cannot verify *whose hand wears the ring,* and you cannot verify it at the front desk — by then the traveler is already inside, already acting in your name. Gemini Enterprise is, almost literally, the passport-and-border system rebuilt for software: a **cryptographically attested identity** issued to every agent by the infrastructure (not self-asserted), naming its **human sponsor** through token exchange, **short-lived** by design, and checked **at the border** — below the application tier, on every call, with mutual-TLS — rather than at the front desk of each app.

**The moral:** when the machines acting in your name outnumber your people many times over, do not ask first *how capable* each one is — capability is the cheap metal now. Ask *can I prove who it is, and where do I check?* Issue every agent a **passport:** an identity that is attested rather than claimed, that names a human sponsor, that **expires,** and that you can **seize.** Then — the half most will skip — check it **at the border, not the front desk:** make identity an infrastructure primitive below the application tier, so an unidentified or expired traveler never crosses, no matter which app or vendor built it. And **keep the manifest** — the record of who crossed — because that manifest is the roll from yesterday, and it is only as trustworthy as the identities written on it.

**The question it forces:** *Every agent in our estate acts under some identity — is that identity issued and attested by our infrastructure, does it name a human sponsor, does it expire, and can we seize it? And do we verify it at the border — below the application tier, on every call — or only at the front desk, after the traveler is already inside our walls and acting in our name?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- Non-human identities now outnumber our people **45-to-1, and up to 109-to-1,** yet **78%** of organizations have no documented policy even to create or retire them. **Can we produce, today, an inventory of every agent and service identity acting in our name — who sponsors it, when it expires, and how we revoke it** — or are we running an unbordered realm full of unidentified travelers?
- The architectural question of the week is *where* identity is verified — **at the border (below the application tier, on every call) or at the front desk (the app, the dashboard).** **Where do we check?** If governance lives only in each application, an agent is already inside our walls before anyone asks who it is.
- **96%** of us run agents but only **12%** have a centralized platform to govern them. **Is agent identity something we own as infrastructure** — attested, short-lived, revocable, uniform across every agent however it was built — **or a setting inside each vendor's console** that stops at that vendor's edge?

### 🏦 Financial Services
- A payments, trading or credit agent acting under a shared, long-lived, over-scoped credential is the classic non-human-identity breach — and **two-thirds of enterprises have already had one.** **Does every such agent carry its own attested, short-lived passport that names a human sponsor,** so the auditor (and the EU AI Act, in 12 days) can trace each transaction to a provable identity rather than a shared service account?
- Regulators will ask *who* moved the money, not *which model.* **Can we tie every consequential financial action to a unique agent identity on the manifest** — or would the trail dead-end at a machine credential a dozen agents share?

### 🧬 Healthcare / Life Sciences
- A clinical or diagnostic agent touching patient data must be as identifiable as any clinician with badge access. **Does each agent hold a distinct, attested identity with a named human sponsor and an expiry,** so an action on a patient record is never anonymous and never open-ended?
- China's agent rules name **healthcare** a high-risk sector requiring filing; the record you file is only as good as the identities in it. **Are our agent passports issued and verified by infrastructure** — or self-asserted at the app layer, where a compromised app forges the traveler?

### 🏭 Manufacturing / Industrials
- On the plant floor, an OT agent adjusting a setpoint should be as strongly identified as a badged operator. **Is agent identity enforced at the network border with mutual authentication** — the equivalent of the guard at the gate — **rather than trusted because it reached the control application?**
- Your moat is process authority, exercised by identifiable actors. **Can we name and revoke the specific agent behind any physical action,** or do agents share inherited machine credentials that no manifest can tell apart?

### 🛒 Retail / Consumer
- Customer-facing agents issue refunds and make promises in your brand's name. **Does each carry a passport that names its human sponsor and expires,** so a compromised or manipulated agent can be identified and stopped at the border rather than discovered later through a chargeback?
- Peak season multiplies agents faster than governance. **Can we issue and revoke agent identities centrally** — or does every new storefront tool mint its own untracked travelers?

### 🏛️ Public Sector / Regulated
- For any agent touching citizen data, identity is accountability. **Is every such agent a first-class identity — attested, sponsored, expiring, revocable — verified below the application tier,** the way a public body must know who acted on a citizen's record?
- The EU AI Act's AI Office can compel documentation and evaluations in **12 days.** **Is our manifest built on identities we issue and can prove,** or on self-declared app-tier credentials a regulator would rightly distrust?

---

## 4 · Technical Deep-Dive — The Passport, the Sponsor, and the Border

Strip the week's news down and the claim is architectural: **when machines acting in your name outnumber your people 45-to-1, the governed object is not the model and not even the grant of authority — it is the identity that carries it, and the layer at which you verify that identity.** Read it as the passport-and-border system in three parts — the passport itself (an attested identity, not a claim), the sponsor (a human, named through delegation), and the border (the layer where you check).

- **The passport (attested identity — the actual object).** Gemini Enterprise gives every agent a **unique, cryptographically attested identity** built on **SPIFFE** (Secure Production Identity Framework for Everyone), and signs and logs **every** API call, data access and file operation to it. The engineering point is *attested, not asserted:* the identity is issued and cryptographically verifiable by the infrastructure, so an agent cannot simply *claim* to be trusted the way an app-tier token or a shared service account lets it. This is the industry consensus written into a product: an agent is **its own principal, cryptographically attested, short-lived at runtime.**
- **The sponsor (the human, preserved through delegation).** A passport names who vouches for the bearer. The equivalent is **the human preserved as the delegating subject via token exchange:** the agent acts with its own identity, but that identity carries a traceable line back to the person (or system) that authorized it. This is what keeps yesterday's roll meaningful — an act on the manifest names *both* the agent and its sponsor, so authority is always traceable to a responsible party, not to an anonymous machine credential.
- **The border (where you verify — the half most skip).** The whole difference between Gemini's approach and the app-tier approach is *location.* Placing **Agent Identity and the Agent Gateway below the application tier as infrastructure primitives** means identity is checked with **mTLS on every call, regardless of how an agent was built or by whom** — the guard at the gate. Positioning governance **at the application tier** means the check happens at the front desk, after the agent is already inside, and only for agents that pass through that particular app. Same seam as every edition this fortnight: own the layer under the commodity, and enforce there.

The strategic core: **an identity layer is a moat if it is attested, sponsored, short-lived, revocable and verified at the border, and a liability if identity is claimed, shared, long-lived and checked (if at all) at the front desk.** After Kimi K3 and the signet ring, "we route to the best model, under a graduated grant" is not a defense; *"we can prove which identity took this action, whose human sponsored it, and that we verified it at the border"* is.

```
        THE PASSPORT  —  verify identity at the BORDER, not the front desk
        Gemini Enterprise: attested agent identity (SPIFFE) + mTLS gateway, BELOW the application tier

   ┌───────────────────────────┐        WHERE DO YOU CHECK?
   │  THE CROWD OF TRAVELERS    │        ┌───────────────────────────────────────────┐
   │  agents · service accts ·  │        │  FRONT DESK  — the application tier         │
   │  workloads · bots          │ ─────▶ │  identity checked after the agent is inside │
   │  NHIs outnumber humans      │        │  per-app · self-asserted · easy to bypass   │  ✗ TRAP
   │  45:1 — up to 109:1         │        ├───────────────────────────────────────────┤
   │  78% have NO issue/revoke   │        │  THE BORDER  — below the application tier   │
   │  policy                     │        │  attested identity (SPIFFE) · mTLS · gateway│
   └───────────────────────────┘        │  every call · however the agent was built   │  ✓ WIN
                                         └──────────────────┬────────────────────────┘
                                            THE PASSPORT     │
                                         ┌───────────────────▼────────────────────┐
                                         │  ① ATTESTED  — issued by infra, not      │
                                         │     self-claimed                         │
                                         │  ② SPONSORED — names a human (token       │
                                         │     exchange · delegating subject)       │
                                         │  ③ EXPIRING  — short-lived at runtime     │
                                         │  ④ SEIZABLE  — revoke instantly           │
                                         └───────────────────┬─────────────────────┘
                                                             │  every crossing →
                                            ┌────────────────▼───────────────┐
                                            │  THE MANIFEST (yesterday's roll)│  which identity,
                                            │  every act logged to an identity│  whose sponsor,
                                            │  → only as good as the passports│  when — your audit
                                            └─────────────────────────────────┘  evidence (12 days)

   TRAP: shared, long-lived, self-asserted credentials, checked at the front desk → travelers you can't name.
   WIN : an attested, sponsored, expiring, seizable passport, checked at the border → a realm that knows who's inside.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — identity is a claim, checked late | The discipline — identity is attested, checked at the border |
|---|---|
| "It reached the app, so it must be trusted" | Attested by infrastructure (SPIFFE), verified with mTLS on every call |
| Shared, long-lived machine credentials | Each agent its own principal, short-lived at runtime |
| The agent acts anonymously | Every action names both the agent and its human sponsor |
| Governance is a setting inside each app | Identity is an infrastructure primitive below the application tier |
| No way to know — or revoke — who's inside | Seize the passport: instant, central revocation |

### Why more, cheaper agents make identity the binding constraint

The forces this radar has tracked all fortnight — commodity models (Kimi K3, 6 days), standard plumbing (MCP, 7 days), cheap routing, graduated authority (yesterday) — all point one way: **more agents, acting more autonomously, minted faster than anyone is tracking.** That is precisely why the identity population has inverted: NHIs at **45:1 to 109:1,** and **144:1** in cloud-native estates. Each new agent is a new traveler in your realm. When agents were few and expensive, you could half-know them by hand. Make them cheap and continuous and the only way to know who is inside is to **issue every one a passport and check it at the border** — which is why the identity layer, not the model, is now the binding constraint on safe scale.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the spend meter, 7 Jul the model-neutral router, 8 Jul the MCP control plane, 9 Jul the deployment-labor market, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe that walks out, 13 Jul govern the goal not the gauge, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring). Today names the layer under authority: **the passport** — provable identity. On legacy estates the danger is an agent wired in with an **inherited, shared, never-expiring service credential** — indistinguishable from every other process using it, checked (if at all) at the application it happens to hit. The retrofit is the border this radar has urged all fortnight, now aimed at identity: **attested identities** issued by infrastructure (SPIFFE-style), the **human sponsor** carried through token exchange, **short-lived** credentials by default, an **Agent Gateway / mTLS** check below the application tier, and a **seize-the-passport** revocation path — feeding the same manifest that is your EU AI Act evidence in 12 days.

**The clean mental model:** *An autonomous agent is a traveler in your realm. Issue it a passport that is attested, sponsored, expiring and seizable — and check it at the border, below the application tier, not at the front desk after it's already inside.*

### Watch list this week
- **Google — Gemini Enterprise Agent Platform (agent identity as infrastructure).** Assigns every agent a **unique, cryptographically attested identity** on the **SPIFFE** standard; signs and logs **every API call, data access and file operation** to that identity; enforces with **mTLS / Context-Aware Access** through an **Agent Gateway**; places **Agent Identity and the Gateway below the application tier as infrastructure primitives.** Reported as a deliberate architectural break from rivals (Anthropic, OpenAI) who position agent governance at the application tier.
- **The population inversion — NHIs vs humans.** **45:1** (Rubrik Zero Labs), **109:1** average enterprise, up from **82:1** a year ago (Palo Alto Networks 2026 Identity Security Landscape), **144:1** cloud-native/DevOps (Entro). **78%** of organizations lack a documented policy to create or remove NHIs; **~two-thirds** have suffered a breach via a compromised NHI (industry data, as reported).
- **The governance gap — OutSystems (1,879 IT leaders, Apr 2026).** **96%** run AI agents; only **12%** have a centralized platform to manage them; **36%** have a centralized governance approach; **94%** say sprawl is compounding complexity, technical debt and security risk.
- **The commodity underneath — Kimi K3's open weights publish 27 July (6 days),** the self-hostable floor that makes more, cheaper, more autonomous agents — and more travelers — inevitable.
- **The connector counterpart — MCP 2026-07-28 spec goes final in 7 days,** aligning MCP authorization with OAuth 2.1 / OpenID Connect (servers as formal OAuth 2.1 resource servers) — the plumbing every agent authenticates through as identity becomes the battleground.
- **The mandatory counterweight — EU AI Act GPAI enforcement applicable 2 Aug 2026 (12 days).** €15M or 3% of global turnover (Art. 101); powers to compel documentation (Art. 91), run evaluations (Art. 92) and require mitigations (Art. 93); reaching deployers. Your manifest is only evidence if its identities are provable.

---

## 5 · Quotes That Catch the Eye

> Using the SPIFFE standard, each agent is granted a unique, cryptographically attested identity. Every API call, every data access request, every file operation the agent performs is signed, logged, and traceable to that identity.
> — **Coverage of Google's Gemini Enterprise Agent Platform**, July 2026 (as reported)

> [Gemini Enterprise places Agent Identity and Agent Gateway] below the application tier as infrastructure primitives, so governance is enforced regardless of how an agent was built or by whom.
> — **Coverage of Gemini Enterprise vs. app-tier rivals**, July 2026 (as reported)

> An agent is a first-class non-human identity — its own principal, cryptographically attested, short-lived at runtime, with the human preserved as the delegating subject via token exchange.
> — **Industry best-practice framing on agent identity**, 2026 (as reported)

> Machine identities now outnumber human identities by 109 to 1 in the average enterprise, up from 82 to 1 just a year earlier.
> — **Palo Alto Networks, 2026 Identity Security Landscape** (as reported)

> "A seal is worthless if anyone can wear the ring. Yesterday we decided how much authority the seal carries; today we prove whose hand wears it — and we check at the border, not the front desk."
> — *the radar, on the identity layer*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Non-human identities vs. humans (average enterprise) | **109:1** (from 82:1 a year ago) | Palo Alto Networks, 2026 Identity Security Landscape (as reported) |
| Non-human identities vs. humans (broad estimate) | **~45:1** | Rubrik Zero Labs (as reported) |
| Non-human identities vs. humans (cloud-native / DevOps) | **144:1** | Entro Labs (as reported) |
| Organizations with NO documented policy to create/remove NHIs | **78%** | Industry data (as reported) |
| Enterprises breached via a compromised non-human identity | **~two-thirds** | Industry data (as reported) |
| Enterprises running AI agents in production | **96%** | OutSystems (1,879 IT leaders, Apr 2026) |
| Enterprises with a centralized platform to govern agents | **12%** | OutSystems |
| Enterprises with a centralized agentic-governance approach | **36%** | OutSystems |
| Concern that AI sprawl raises security risk / tech debt | **94%** | OutSystems |
| Enterprise apps embedding task-specific agents by end-2026 | **40%** (from <5% in 2025) | Gartner |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |
| Kimi K3 full open weights (Modified MIT) publish | **27 Jul 2026 (6 days)** | Moonshot / coverage |
| MCP's largest revision goes final | **28 Jul 2026 (7 days)** | Model Context Protocol blog |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (12 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Take the census — inventory every traveler before you fortify anything.** You cannot issue passports to a crowd you can't count. Pull a list of every agent and non-human identity acting in your name — human sponsor, scope, credential type, expiry — and rank them by blast radius. Expect the count to shock: NHIs outnumber people **45:1 to 109:1,** and **78%** of organizations start from no policy at all. The census is the prerequisite for everything below, and it doubles as the opening page of your EU AI Act manifest, due-diligence-ready in **12 days.**

2. **Issue real passports — attested, sponsored, expiring, seizable.** Make every agent a **first-class identity:** issued and cryptographically attested by your infrastructure (SPIFFE-style), **not** a shared or self-asserted app-tier token; carrying its **human sponsor** through token exchange; **short-lived** by default so a credential can't outlive its purpose; and **revocable in minutes** — a seize-the-passport path, tested, with a named owner. Kill the long-lived shared service accounts that make two-thirds of NHI breaches possible.

3. **Move the checkpoint to the border.** Decide, deliberately, *where* identity is verified — and move it **below the application tier.** Enforce agent identity with mutual authentication at an **Agent Gateway / mesh,** on **every** call, **regardless of which app or vendor built the agent** — the guard at the gate, not the clerk at the front desk. That single architectural choice is what makes your manifest trustworthy: every act on the roll names a provable identity and its sponsor, verified at the perimeter, rather than a claim you accepted after the traveler was already inside your walls.

---

*AI Tech Radar · generated 21 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The technical facts are relayed from public sources and coverage and marked "as reported" where they rest on secondary reporting: Google's Gemini Enterprise Agent Platform details (a unique, cryptographically attested identity per agent built on the SPIFFE standard; every API call, data access and file operation signed, logged and traceable to that identity; enforcement via mTLS / Context-Aware Access and an Agent Gateway; Agent Identity and the Gateway placed below the application tier as infrastructure primitives; framed as an architectural contrast with Anthropic and OpenAI positioning governance at the application tier) are relayed from Google Cloud documentation and coverage (Tech Times, Infosecurity Magazine and others). The non-human-identity ratios and gaps (45:1 Rubrik Zero Labs; 109:1 average enterprise, up from 82:1, Palo Alto Networks 2026 Identity Security Landscape; 144:1 cloud-native, Entro Labs; 78% lacking documented NHI create/remove policy; roughly two-thirds breached via a compromised NHI; agent as a first-class NHI, cryptographically attested, short-lived, with the human as delegating subject via token exchange) are relayed from security-industry coverage (Okta, Cloud Security Alliance, The Hacker News, SecureW2, nhimg.org, Reco and others). The OutSystems figures (96% run AI agents; 12% with a centralized platform; 36% with a centralized governance approach; 94% concerned about sprawl; 1,879 IT leaders; State of AI Development 2026, April 2026) are OutSystems'. The Gartner figures (40% of enterprise apps embed task-specific agents by end-2026, up from <5% in 2025; >40% of agentic-AI projects cancelled by end-2027) are Gartner's. The Kimi K3 open-weights date (27 July 2026) is Moonshot AI's, relayed via coverage; the MCP 2026-07-28 final-spec date and OAuth 2.1 alignment are the MCP project's; the EU AI Act mechanics are the European Commission's. The "6 days," "7 days" and "12 days" figures are simple counts from this edition's date (21 July 2026) to 27 July, 28 July and 2 August 2026 respectively and are the radar's own. The passport allegory — the historical safe-conduct and passport (issued by a sovereign, naming and vouching for the bearer, sealed and verifiable, limited in time and route, checked at the border by a guard while an innkeeper merely recorded arrivals) — is the radar's own historical illustration, told approximately, and is not a sourced claim about AI.*
