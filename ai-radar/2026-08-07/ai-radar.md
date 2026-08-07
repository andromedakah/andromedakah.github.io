# 🗓️ AI Tech Radar — The Keyring

**Friday, 7 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday's edition ("The Airlock") fitted a control point at the one door your data leaves through — a checkpoint you own that can deny a prompt before it reaches the model. But a prompt going out is only half the crossing. The other half is what the agent is allowed to *reach and act on* once it is working: your Slack, your Figma, your Jira, your database. Today the enterprise gets the second fitting, and it is about **keys, not doors.** On the strength of **MCP's Enterprise-Managed Authorization extension (stable since 18 June 2026),** and with the **7-28 MCP specification now final,** **Okta's Cross App Access (XAA) reaches general availability for Workforce customers through the Okta Integration Network in August 2026** — and **Anthropic has made Okta a featured identity provider for Claude, Claude Code and Cowork.** The mechanism: instead of every tool minting its own key and every employee clicking "allow" at every door, an **admin authorizes a connector once for the whole organization,** and each agent is issued a token **scoped to that user's identity, groups and roles** — exposing only the tools and data the org pre-approved, revocable centrally in one motion. The board's question this morning: ***our agents already outnumber our people roughly a hundred to one — so who holds the keyring to everything they can touch: a thousand apps each minting their own, or one steward we already trust, on a standard every vendor can implement?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thing: the model is a commodity, so the durable advantage is the **layer you own around it.** Yesterday that thesis got its first bolt — Inference hooks, the airlock that decides what of yours leaves for the model. Today it gets the matching fitting on the other side of the crossing: **who decides what your agents are allowed to reach and do once they are working.** On the back of **MCP's Enterprise-Managed Authorization (EMA) extension — stable since 18 June 2026 — and the now-final 7-28 MCP specification, Okta's Cross App Access (XAA) hits general availability for Workforce customers via the Okta Integration Network in August 2026,** and **Anthropic has named Okta a featured identity provider for Claude, Claude Code and Cowork.**

**What it is, precisely.** XAA extends OAuth so that an AI agent's access to enterprise apps is governed by the **identity provider you already run,** not by a jumble of per-app consent screens. An **admin authorizes a connector once for the whole organization;** thereafter, when an employee's agent asks for a tool, the client exchanges an identity assertion (an ID-JAG) for an access token **scoped to that user's groups and roles,** and the MCP server exposes **only the tools and data the organization pre-approved.** No per-server "allow" prompts, no standing keys handed to each app, and **when someone leaves, the grant dies at the identity provider** — one motion, every tool. Early doors already fitted to the standard include **Asana, Atlassian, Canva, Figma, Granola, Linear and Supabase** (Slack in progress); clients include **Claude, Claude Code, Cowork and VS Code.**

**Why it matters more than a feature note.** The month's problem was that governance of the AI layer was a slide, not a switch. Yesterday's airlock stopped the wrong thing from *leaving.* But an agent is not just an egress pipe — it is a worker with a keyring, and **the enterprise now runs roughly 109 machine identities for every human, of which about 79 are AI agents** (Palo Alto Networks' 2026 Identity Security Landscape) — up from ~82:1 a year earlier. Every one of those agents needs keys to real systems. Hand those keys out per-app, per-click, and you have rebuilt the non-human-identity sprawl every CISO report this year has flagged. XAA + EMA put the whole keyring back on **one steward you already trust.**

1. **The keyring is yours, held at the identity provider you already own.** The novelty is not that agents can reach tools — it's that the decision about *which* tools, for *which* identity, at *what* scope, now sits in your IdP and its group/role model, not in a thousand app-by-app consents. Authorize once for the org; provision by identity; **revoke everywhere in one turn of the ring.**

2. **It is a standard, not a point integration.** XAA is an OAuth extension; EMA is a stable MCP extension; the 7-28 spec is final. That means the same keyring pattern can govern **any tool and any model vendor** that implements it — the asset is the standard, not the one product that shipped first.

3. **It is real, and it is early — know the gaps.** Okta is the **first** identity provider (others still to wire in); it governs only tools that expose an **MCP/EMA front door** (homegrown and legacy systems are still on ad-hoc locks); and it controls **access, not payload** — it decides which rooms an agent may enter, not what the agent does inside one, nor whether the data it carries out should have left (that is yesterday's airlock). A keyring is not a full security program.

**Bottom line:** the month said *own the layer around the commodity model.* Yesterday you fitted the airlock at the door your data leaves through; today you take back the **keyring** to everything your agents can reach — and you hold it through the identity provider you already trust, on a standard any vendor can implement. **Wire your IdP to XAA, authorize connectors at the org level, scope by group and role, and make "revoke everywhere in one motion" a drill you have actually run** — because your agents outnumber your people a hundred to one, and a hundred workers with un-tracked keys is not a workforce, it is an unlocked house.

---

## 2 · Allegory of the Day — "The Keyring"

*Topic: In August 2026 Okta's Cross App Access (XAA) reaches general availability for Workforce customers through the Okta Integration Network, built on the Model Context Protocol's Enterprise-Managed Authorization (EMA) extension, which went stable on 18 June 2026, with the 7-28 MCP specification now final; Anthropic has named Okta a featured identity provider for Claude, Claude Code and Cowork. XAA extends OAuth so that an AI agent's access to enterprise applications is governed by the organization's own identity provider rather than by per-application consent prompts: an administrator authorizes a connector once for the whole organization, and each request exchanges an identity assertion for an access token scoped to the user's groups and roles, so the tool exposes only the data and actions the organization pre-approved, and access is revoked centrally when the person leaves. Early servers implementing the standard include Asana, Atlassian, Canva, Figma, Granola, Linear and Supabase (Slack in progress); clients include Claude, Claude Code, Cowork and VS Code; Okta is the first identity provider, with others to follow. The context is scale: machine identities, including AI agents, now outnumber human identities roughly 109 to 1, of which about 79 are AI agents, up from about 82 to 1 a year earlier. The limits: it governs access, not the payload (that is a separate data-loss checkpoint) and not the agent's behaviour once inside a tool; it reaches only tools that expose an MCP/EMA front door; and Okta is the first of several identity providers. The lesson: your agents outnumber your people, and the durable control is not the model but the keyring — held by one steward you already trust, on a standard every vendor can implement. The keyring allegory — a great house whose steward holds one ring and cuts each key to a single room — is the radar's own illustration.*

Picture a great house at the hour its staff triples overnight. Where yesterday there were a hundred people who knew the rooms and each other, today there are ten thousand new workers — tireless, quick, literal — and every one of them needs to get into rooms to do a job: the ledger room, the drawing room, the room where the plans are kept, the cellar with the good wine and the bad debts. This is not a metaphor for ambition; it is arithmetic. In the modern estate the new workers — the agents — already **outnumber the people who hired them roughly a hundred to one.** A house cannot run if every new worker must be walked to every door by the master.

So how, until now, did a worker get into a room? Badly. Each door had **its own lock, cut by whoever built the room,** and the worker collected keys the only way on offer: by standing at each door and being asked, *"do you allow this?"* — and saying yes, because the work waited. The keys piled up on a hundred belts. Nobody kept the roster of who held what. A key cut for one afternoon opened the room for a year. A worker who left took a belt of live keys into the night. And because the locks were all different, there was no single turn of the hand that could call the keys back. This is the world every security report of the year has been shouting about: a house with **more keys than it has doors, and no one holding the ring.**

What comes of age this month is the oldest fix in the book, made new: **one keyring, held by the house's own steward.** The estate re-fits its doors to a common lock — not the master's design, not each room's whim, but a **shared standard** the whole trade has agreed on (the crews call it MCP's enterprise-managed authorization; the fitting that lets your steward turn it, Cross App Access). Now a worker who needs a room does not haggle at the door. It presents itself **once, at the steward's office** — the steward you already employ, who already keeps the roster of who is on which crew. The steward reads the roster, and cuts a key **to exactly that room and no other,** stamped with the hour it expires, written in the daybook. The worker goes to the door; the door accepts the steward's key because the lock is the shared standard; the worker does its task and no more. And when the worker leaves the house, the steward **turns the ring once** — and every key that worker ever held goes cold, at every door, in a single motion.

Two truths keep the household honest. The first: the power is not that agents can open doors — they always could, badly. The power is that **the keyring came home to the steward you already trust,** and that the doors now speak a common lock, so one office issues, scopes, logs and revokes for the whole house. Authorize a connector once for the estate, and every worker on the right crew gets the rooms their crew is allowed — no more, governed by the identity you already run. That is the month's thesis turned to iron again: **own the layer around the commodity model** — and this layer is the keyring. The second truth is soberer: **not every door is re-fitted yet.** The common lock accepts keys only from doors that have installed it (a good first set — Asana, Atlassian, Canva, Figma, Linear, Supabase, with more arriving), while the old cellars you built yourself still wear their ad-hoc locks. Your steward is the first of several the trade will recognize, not yet the only one. And a keyring governs *which rooms a worker may enter* — it does not watch what the worker does once inside, nor decide whether what it carries out the door should leave (that is the airlock you fitted yesterday). A keyring is a great advance and not a whole security program.

**The moral:** the model is the commodity engine outside — you will change which one you rent more than once, and it was never the seat of your control. The **keyring is yours,** or it is a thousand loose keys on a hundred untracked belts. In a house where the workers outnumber the people a hundred to one, the question is never "can the agent reach the tool" — of course it can — but "**who cut that key, to what room, for how long, and can we call it back tonight?**" Bring the keyring home to the steward you already trust, fit your doors to the shared lock, issue by identity and scope, and rehearse the one motion that pulls every key at once — because a house with more keys than doors and no one holding the ring is not staffed, it is burgled at leisure.

**The question it forces:** *Our agents outnumber our people roughly a hundred to one — so who holds the keyring to everything they can touch? If the answer is "each app hands out its own keys and the user clicks allow," we have described the sprawl, not the control. Is there one steward — the identity provider we already run — that issues every agent's access, scoped to who the person is, logged, and revocable everywhere in a single motion? Which of our doors speak the shared lock and which are still on ad-hoc keys — and if a person left tonight, how many live keys would walk out with them?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **Who holds the keyring?** XAA and EMA put agent access on **your** identity provider, scoped to identity and revocable at the org level. **Is there a single steward that decides which tools every agent may reach — or does each app hand out its own keys while our people click "allow" at every door?**
- The scale is the alarm: **machine identities, including AI agents, now outnumber humans roughly 109 to 1, and about 79 of those 109 are AI agents** (Palo Alto Networks). **If most of our "workforce" is now non-human and key-holding, is our identity governance built for a hundred agents per person — or still for the people?**
- The keyring is a **standard,** not a product. **Are we adopting the access pattern as model- and tool-neutral — one we can demand of every vendor and IdP — or bolting one integration to one product and calling it governed?**

### 🏦 Financial Services
- Agents that touch core banking, trading and customer systems must reach **only** what their role allows. **Can we scope every agent's access to groups and roles at the identity provider, so a support-desk agent can never open the trading room — and prove it to an examiner?**
- The offboarding test is the acid test. **When an employee or a contractor leaves, does every key their agents held go cold in one motion at the IdP — or are there standing tokens on a dozen apps we would have to chase down by hand?**
- CNIL is already asking for the Article 11 dossier. **Is the daybook of who authorized which connector, for which identity, at what scope, a record we could hand a supervisor today?**

### 🧬 Healthcare / Life Sciences
- PHI and trial systems are the rooms with the strictest guest lists. **Does an agent reach a patient record only through an identity-scoped, pre-approved grant — never a broad, standing key a clinician clicked through once?**
- Least privilege is a duty of care here. **Can we cut each agent's key to exactly the data and actions its task needs — and expire it — rather than granting the whole cabinet because per-app consent offered nothing finer?**

### 🏭 Manufacturing / Industrials
- Line-side and supply-chain tools are a thicket of homegrown locks. **Which of our systems expose an MCP/EMA front door the keyring can govern today — and which legacy cellars are still on ad-hoc keys that no steward can see or revoke?**
- Cheaper, better engines keep arriving. **When a team swaps the model, does our agent-access keyring stay put on our IdP — or does changing the engine scatter the keys again?**

### 🛒 Retail / Consumer
- Storefront and support agents touch customer PII at volume. **Is each agent's reach into customer systems scoped to its role and logged — or do a hundred agents share broad keys because wiring least privilege per app was too slow?**
- Trust is the product. **Could we tell a customer, truthfully, that every agent touching their data holds a key our own identity provider issued, scoped and revocable — not a standing grant on a third-party app?**

### 🏛️ Public Sector / Regulated
- Citizen data carries the strictest duty and the least tolerance for a key that outlives its need. **Is agent access to citizen systems issued by our identity provider, scoped to duty, time-bounded, and revocable centrally — with a per-grant record in our own log?**
- Enforcement is live and case-by-case. **Could we show an auditor not just what our AI did, but the keyring that decides what it is even allowed to reach — the standard, the steward, the scope, and the revocation drill?**

---

## 4 · Technical Deep-Dive — Own the Keyring, Rent the Model

Read this week as the second fitting on the layer you own. Yesterday's airlock (Inference hooks) governed **egress** — what of yours leaves for the model. Today's keyring (XAA on MCP's EMA) governs **access** — what your agents may reach and act on. Both answer the same board question from opposite sides of the crossing, and both put the control on ground you already hold. The architecture splits cleanly: the **workers** (the agents, now outnumbering people ~100:1), the **keyring** (identity-provider-managed access you own), and the **doors not yet re-fitted** (the honest gaps).

- **The workers — agents at machine scale (rented brains, your identity).** The engines are a menu you rent — **Claude Opus 5** (#1, Intelligence Index 61 / Agentic Index 55.3, $5/$25), **Gemini 3.6 Flash**, **GPT-5.6 Sol**, **Kimi K3**, **DeepSeek V4-Flash-0731** (MIT). But the agents built on them are **workers with keyrings,** and they already run at machine scale: **~109 machine identities per human, ~79 of them AI agents** (Palo Alto Networks 2026), up from ~82:1 a year earlier. The engine is not where your risk lives; the **keys those workers hold** are.
- **The keyring — access you own (comes of age this month).** With **XAA** (an OAuth extension, GA for Okta Workforce via the Integration Network in August 2026) on top of **MCP's EMA** (stable 18 Jun; 7-28 spec final), agent access to enterprise tools is governed by **your identity provider.** An admin **authorizes a connector once for the whole org;** each request exchanges an identity assertion (**ID-JAG**) for an access token **scoped to the user's groups and roles;** the MCP server exposes **only pre-approved tools and data;** there are **no per-server consent prompts;** and **offboarding revokes every grant centrally.** Okta is the **first** identity provider; **Anthropic makes it a featured IdP** for Claude, Claude Code and Cowork. Early servers: **Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase** (Slack in progress). The point that matters: **the keyring is on your IdP,** governed by the group/role model you already run.
- **The doors not yet re-fitted — the honest gaps.** Okta is the **first** IdP, not the only one; the keyring reaches only tools with an **MCP/EMA front door** (homegrown and legacy systems stay on ad-hoc locks); and it governs **access, not payload or behaviour** — it decides which rooms an agent may enter, not what it does inside, nor whether what it carries out should leave (that is yesterday's airlock). New standard, tooling still rolling out. A keyring on some doors is a real advance and a partial house.

The strategic core: **the model is the worker's brain; the keyring is your house.** For a month the misread has been "our model is capable and safe, so our agents are governed" — which confuses the engine with the access. After this week, "the model is smart" is not the answer to "what is our agent allowed to touch"; ***"every agent's access is issued by the identity provider we own, scoped to who the person is, and revocable everywhere in one motion"*** is the answer — and XAA on MCP's EMA is where you can finally build it.

```
        THE KEYRING — own the access, rent the model
        Agents outnumber people ~100:1. Every one needs keys to real tools. One steward holds the ring.

   ┌──────────────────────────────┐        ┌──────────────────────────────┐
   │  YOUR WORKERS — the agents    │        │   THE DOORS — enterprise apps │
   │  Claude · Claude Code · Cowork│        │   Asana · Atlassian · Figma · │
   │  · VS Code (rented brains)    │        │   Linear · Supabase · Canva · │
   │  ~109 machine ids / human     │        │   Slack (in progress)         │
   │  ~79 of them AI agents        │        │   each fitted to the shared   │
   └───────────────┬──────────────┘        │   lock (MCP EMA)              │
                   │ agent asks for a tool  └───────────────▲──────────────┘
                   ▼                                        │ scoped key opens ONE room
   ┌───────────────────────────────────────────────────────┴──────────────┐
   │  THE KEYRING — Cross App Access on MCP EMA · YOUR identity provider    │
   │  admin authorizes a connector ONCE for the whole org                  │
   │  → identity assertion (ID-JAG) → access token SCOPED to groups/roles   │
   │  → server exposes ONLY pre-approved tools/data · no per-app consent    │
   │  → offboard = REVOKE EVERYWHERE in one motion · your own daybook       │
   └───────────────────────────────────────────────────────────────────────┘

   DOORS NOT YET RE-FITTED (know them): Okta is the FIRST IdP (others coming) ·
   only tools with an MCP/EMA door · governs ACCESS, not payload or behaviour ·
   standard is new, tooling still rolling out.

   TRAP: "each app hands out its own keys, the user clicks allow" → sprawl, standing keys, no recall.
   WIN : own the keyring → one steward, scoped by identity, revocable everywhere, every vendor.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — a thousand keys, no ring | The discipline — own the keyring |
|---|---|
| Each app mints its own key; the user clicks "allow" | One steward (your IdP) issues every agent's access |
| Standing tokens that outlive the task and the person | Scoped, time-bounded grants; revoke everywhere in one motion |
| Access decided per-app, per-click, untracked | Access decided by identity, group and role, logged |
| One integration bolted to one product | A standard (XAA/EMA) any tool and any model vendor can accept |
| "The model is safe, so the agents are governed" | The model is the brain; the keyring is the house you own |

### Why owning the keyring beats a smarter agent

Every control this month presumed a place to stand. The meter, the router, the MCP plane, the dossier, the discovery scan, the airlock — each was a layer you own around a commodity engine. The keyring adds the missing verb on the access side: **revoke.** And the reason it must live on **your** identity provider is that access granted per-app moves and multiplies with every app and every model you add — a thousand keys, no ring. Put the keyring on the IdP you already run, on a standard (XAA over OAuth, EMA in MCP) any vendor can implement, and agent access stays governed whichever engine you rent and whichever tool you add. The correct read of this week is not "Okta shipped an integration" but "**the enterprise can now hold the keyring** — so build the pattern, not the point solution."

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine, 28 Jul the mailroom, 29 Jul the pilot plant, 30 Jul the commonplace book, 31 Jul the last mile, 1 Aug the tide table, 2 Aug the loose cannon, 3 Aug the customs house, 4 Aug the two windows, 5 Aug the dark warehouse, 6 Aug the airlock). Yesterday you fitted the airlock at the door your data leaves through; today you bring the keyring home to the steward you already trust. On legacy estates the locks are everywhere and none of them match — so the retrofit is unglamorous and specific: **wire your identity provider to XAA** and start with the tools that already expose an MCP/EMA door (Asana, Atlassian, Figma, Linear, Supabase, and the rest); **authorize connectors at the org level** and provision by group and role, not by per-app consent; **scope and time-bound** every grant; and **rehearse the offboarding motion** — prove that one revocation at the IdP kills every key an identity's agents hold. Then map the doors still on ad-hoc locks — homegrown systems, legacy apps, other IdPs not yet wired — honestly, as the next fittings, not as a house already secured.

**The clean mental model:** *The model is the worker's brain — rented, swappable; you'll change which one you hire more than once. The keyring is yours: the one ring, held by the steward you already trust, that issues each agent a key scoped to who the person is, logged, and revocable everywhere in a single motion. The trade agreed the lock this month (XAA on MCP's EMA); the enterprise must bring the keyring home — start with the doors already fitted, scope by identity, and rehearse the one turn that calls every key back.*

### Watch list this week
- **The launch — Okta Cross App Access GA + MCP EMA.** XAA reaches **GA for Okta Workforce via the Integration Network in August 2026,** on top of **MCP's Enterprise-Managed Authorization** (stable **18 Jun**; **7-28 spec final**). Admin **authorizes once for the org;** access token **scoped to groups/roles;** **no per-app consent;** **central revocation.** **Anthropic makes Okta a featured IdP** for Claude, Claude Code, Cowork. Servers: **Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase** (Slack in progress); clients: Claude, Claude Code, Cowork, VS Code.
- **The gaps — be honest.** Okta is the **first** IdP (others coming); only tools with an **MCP/EMA door;** governs **access, not payload/behaviour;** standard new, tooling rolling out.
- **The scale — why it shipped now.** **~109 machine identities per human, ~79 of them AI agents** (Palo Alto Networks 2026), up from ~82:1 a year earlier. **Gartner: 40% of enterprise apps will feature task-specific agents by 2026** (from <5% in 2025). **~31% of enterprises have ≥1 agent in production** (S&P Global/McKinsey); **IDC: 88% of AI PoCs never reach widescale deployment.** More agents, more keys — the keyring exists because the sprawl exploded.
- **The regulatory backdrop — still live.** EU AI Act enforcement running since **2 Aug;** AI Office GPAI powers; **€15M or 3%;** **180+ orgs** signed the GPAI Code of Practice; CNIL's **4 Aug** action (14 banks, Article 11). Scoped, revocable, logged access is exactly what a supervisor asks to see.
- **The engine, for context.** Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 (MIT) — the rented, swappable brain. Own the keyring, not the engine.

---

## 5 · Quotes That Catch the Eye

> "Enterprise-managed auth gives MCP the foundation it needs to scale across an enterprise, with Okta as our first identity provider partner. When an admin authorises a connector once for the whole organisation, every employee gets instant access to more of their tools through Claude, governed by the IDP they already trust."
> — **Mayank Malhotra, Anthropic**, on Enterprise-Managed Authorization and Okta (as reported)

> "Logging in once and automatically having all your MCP connectors automatically set up is pretty magical."
> — **Tom Moor, Head of Engineering, Linear**, on the Enterprise-Managed Authorization experience (as reported)

> Machine identities, including AI agents, now outnumber human identities roughly 109 to 1 — and about 79 of those 109 are AI agents.
> — **Palo Alto Networks, 2026 Identity Security Landscape** (as reported)

> "The model is the worker's brain — rented and swappable. The keyring is yours, or it is a thousand loose keys on a hundred untracked belts: one steward, scoped by identity, revocable everywhere in a single motion."
> — *the radar, on owning the access layer*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Machine identities per human (incl. AI agents) | **~109 : 1 (≈79 of them AI agents)** | Palo Alto Networks, 2026 Identity Security Landscape (as reported) |
| Machine-to-human identity ratio, a year earlier | **~82 : 1 (+~33% in a year)** | Palo Alto Networks (as reported) |
| Cross App Access — availability | **GA for Okta Workforce via the Integration Network, August 2026** | Okta / trade coverage (as reported) |
| MCP Enterprise-Managed Authorization — status | **Stable since 18 Jun 2026; 7-28 MCP spec final** | Model Context Protocol Blog (as documented) |
| How access is scoped | **Token scoped to the user's groups and roles; org authorizes connector once** | Model Context Protocol Blog (as documented) |
| Offboarding | **Central revocation at the identity provider — one motion, every tool** | Model Context Protocol Blog / Okta (as reported) |
| First identity provider | **Okta (via Cross App Access); others to follow** | Model Context Protocol Blog / Okta (as reported) |
| Early servers implementing EMA | **Asana · Atlassian · Canva · Figma · Granola · Linear · Supabase (Slack in progress)** | Model Context Protocol Blog (as documented) |
| Enterprise apps with task-specific AI agents by 2026 | **40% (up from <5% in 2025)** | Gartner (as reported) |
| Enterprises with ≥1 AI agent in production | **~31%** | S&P Global Market Intelligence / McKinsey (as reported) |
| AI proofs-of-concept never reaching widescale deployment | **88%** | IDC (as reported) |
| EU AI Act enforcement — status | **Live since 2 Aug; 180+ signed GPAI Code; CNIL 4 Aug: 14 banks, Art. 11** | European Commission / regulatory coverage (as reported) |
| Penalty ceiling (Art. 99) / incorrect information | **€15M or 3% · €7.5M or 1.5%** | European Commission |
| The engine (context) | **Opus 5 · Gemini 3.6 Flash · GPT-5.6 Sol · Kimi K3 · DeepSeek V4-Flash-0731 (MIT)** | Vendor / model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Bring the keyring home — wire your identity provider to Cross App Access this month.** XAA is GA for Okta Workforce via the Integration Network; EMA is a stable MCP extension and the 7-28 spec is final. Start with the tools that already expose an MCP/EMA front door (Asana, Atlassian, Figma, Linear, Supabase, and the growing list), **authorize connectors once at the org level,** and let your IdP — not a hundred per-app consent screens — decide which agents reach which tools. You will replace consent-fatigue and un-tracked tokens with a single roster you already keep.

2. **Scope by identity and rehearse the one motion that revokes everywhere.** The control that keeps your house yours is least privilege plus recall: cut each agent's access to the **groups and roles** the person actually holds, **time-bound** the grant, and — the acid test — **prove that a single revocation at the identity provider kills every key that person's agents hold, at every tool.** Report to the board one metric: *the share of agent access issued and revocable through our own IdP.*

3. **Make it standard, not point — and map the doors still on ad-hoc locks.** The asset is the pattern (XAA over OAuth, EMA in MCP), not the one product that shipped first: demand the same identity-scoped access from **every** tool and **every** model vendor, so swapping Opus 5 for Gemini or GPT-5.6 never scatters the keys. Then list the doors this fitting does not yet close — **other identity providers not yet wired, homegrown and legacy systems with no MCP/EMA door, and the payload-and-behaviour questions the keyring does not answer** (that is the airlock and your monitoring) — assign each an owner, and treat them as the next fittings. Own the keyring, hold it at the steward you already trust, and demand the shared lock on every door — because a house with more keys than doors and no one holding the ring is not staffed, it is unlocked.

---

*AI Tech Radar · generated 7 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The access-layer details (that Okta's Cross App Access reaches general availability for Workforce customers through the Okta Integration Network in August 2026; that it is built on the Model Context Protocol's Enterprise-Managed Authorization extension, which went stable on 18 June 2026, with the 7-28 MCP specification now final; that Anthropic has named Okta a featured identity provider for Claude, Claude Code and Cowork; that Cross App Access extends OAuth so that an administrator authorizes a connector once for the whole organization and each request exchanges an identity assertion for an access token scoped to the user's groups and roles, exposing only pre-approved tools and data with no per-server consent prompts and central revocation on offboarding; and that early servers implementing the extension include Asana, Atlassian, Canva, Figma, Granola, Linear and Supabase, with Slack in progress, and clients include Claude, Claude Code, Cowork and VS Code) are drawn from the Model Context Protocol Blog "Enterprise-Managed Authorization" and "7-28 release candidate" pages as documented, with the Cross App Access general-availability timing and Okta partnership relayed from Okta and August 2026 trade coverage (SiliconANGLE, InfoQ, TechTimes, Web Developer and vendor materials) as reported. The identity-scale figures (that machine identities, including AI agents, now outnumber human identities roughly 109 to 1, of which about 79 are AI agents, up from about 82 to 1 a year earlier) are relayed from Palo Alto Networks' 2026 Identity Security Landscape as reported. The market figures (Gartner's projection that 40% of enterprise applications will feature task-specific AI agents by 2026, up from less than 5% in 2025; that roughly 31% of enterprises have at least one AI agent in production per S&P Global Market Intelligence and McKinsey; and IDC's finding that 88% of AI proofs-of-concept never reach widescale deployment) are relayed from analyst and press coverage as reported. The EU AI Act facts (enforcement live from 2 August 2026; the AI Office's GPAI powers; the penalty ceiling of the higher of €15 million or 3% of worldwide annual turnover under Article 99, and €7.5 million or 1.5% for incorrect information; that more than 180 organizations signed the GPAI Code of Practice; and CNIL's 4 August information requests to 14 financial institutions demanding Article 11 documentation) are relayed from the European Commission and August 2026 regulatory coverage as reported; the CNIL specifics rest on secondary coverage. The model details (Claude Opus 5, Intelligence Index 61 / Agentic Index 55.3 at $5/$25; Google Gemini 3.6 Flash; GPT-5.6 Sol; Kimi K3 open weights; and DeepSeek V4-Flash-0731, MIT-licensed) are relayed from model-tracker and vendor coverage as reported. The quotes from Mayank Malhotra (Anthropic) and Tom Moor (Linear) are relayed from trade coverage of the Enterprise-Managed Authorization launch as reported. The keyring allegory — a great house whose steward holds one ring and cuts each key to a single room — is the radar's own illustration and is not a sourced claim about any specific company.*
