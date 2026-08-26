# 🗓️ AI Tech Radar — The Passport

**Wednesday, 26 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar found the moat: not the rented model but the governed proprietary knowledge only you own — the larder behind the gate. The day before, it named the gate itself, the single governed door every agent must pass. Today it asks the question the gate cannot answer on its own: **who, exactly, is standing at the door?** A gate that checks papers is useless if the travelers carry none — and this week the market moved to issue the papers. **Okta brought Agent SSO to general availability, making an AI agent a first-class identity — registered, policy-governed, and handed a short-lived, scoped credential — through the open Cross App Access (XAA) standard, inside an identity platform used by more than 20,000 customers.** The reason it matters is the census behind it: **Palo Alto Networks' 2026 Identity Security Landscape finds machine identities now outnumber humans roughly 109 to 1 — up from about 82 to 1 a year earlier — and about 79 of those 109 are AI agents,** so nearly three-quarters of the "workforce" reaching your systems is agentic and non-human. Yet the papers have not kept up: **Okta's AI Agents at Work 2026 research (Apprize360; 292 executives, 492 knowledge workers, seven countries) finds 91% of organizations already use AI agents but only 10% have a developed strategy for managing non-human identities, 88% report a suspected or confirmed AI-agent security incident, only 34% apply the same identity controls to agents as to humans, and only 22% treat an agent as an independent, identity-bearing entity.** The board's question this morning: ***our systems are now worked by a hundred machine travelers for every human, most of them agents acting on their own or on someone's behalf — have we issued each one a real passport (a named, centrally governed, short-dated, revocable identity), or are they moving through our house on borrowed keys and forged tokens no one can name, meter, or turn back?***

---

## 1 · Executive Summary (90-second read)

For a week this radar walked the value up the stack — the acting deputy, the watchman, the guardrail, the reservoir's value gap, the gate every agent must pass, and yesterday the governed knowledge worth putting behind that gate. Today it closes the loop with the one thing that makes a gate, a larder and an audit log actually work: **a name for every agent.** The governing shift is no longer "can an agent act?" or "through what door does it pass?" or "what does it draw on?" — it is **"who is the agent, who does it answer to, what may it touch, and can we revoke it in an instant?"** The market's answer this week is **agent identity as a first-class, centrally governed control point.**

**The datable signal — agents become first-class identities.** In the last week of August, **Okta brought Agent SSO to general availability,** bringing the open **Cross App Access (XAA)** standard into an identity platform used by **more than 20,000 customers.** It lets an enterprise register an AI agent in the same directory as its people, govern it with the same centralized policy, and issue it a **short-lived, scoped token** when it needs to act in another app — retiring the static API keys, unmanaged tool-to-tool links and repeated consent prompts that today let agents move unnamed. CEO Todd McKinnon framed it plainly: *"AI agents are a powerful new identity type. They can act independently, on their own or on behalf of a user or a team or a company."* Identity, in other words, is now the layer where oversight of agents actually lives.

**The move — the census demands it, and the papers are missing.** The reason identity suddenly dominates is a population explosion. **Palo Alto Networks' 2026 Identity Security Landscape: machine identities now outnumber humans ~109 to 1, up from ~82:1 a year ago, and ~79 of those 109 are AI agents** — nearly three-quarters of the actors touching enterprise systems are agentic and non-human. But governance has not followed: **Okta's AI Agents at Work 2026 (Apprize360; 292 executives + 492 knowledge workers, seven countries): 91% already use AI agents; only 10% have a developed non-human-identity strategy; 88% report a suspected or confirmed AI-agent security incident; only 34% extend human-grade identity controls to agents; only 22% treat an agent as an identity-bearing entity.** A house with a hundred unnamed servants for every citizen is not governed — it is merely occupied.

1. **The papers arrive — agents become first-class identities.** **Okta Agent SSO (GA): AI agents registered and policy-governed like employees, handed short-lived scoped tokens via the open Cross App Access (XAA) standard, inside a 20,000+‑customer platform.** Authorization moves from each app to the identity provider — the same shift SSO made for humans. Todd McKinnon: agents are "a powerful new identity type."

2. **The census demands it — machines, mostly agents, dwarf people.** **Palo Alto Networks 2026: machine identities outnumber humans ~109:1 (up from ~82:1), ~79 of 109 are AI agents (~72%).** CyberArk puts the ratio at "more than 80 to 1" and calls identity the control plane for the AI era. The population you must govern is overwhelmingly non-human and increasingly agentic.

3. **But the papers are missing — adoption has outrun identity.** **Okta/Apprize360: 91% use AI agents, only 10% have an NHI strategy, 88% report an agent security incident, only 34% apply human-grade controls to agents, only 22% treat an agent as an identity.** The **EU AI Act's Article 12 reconstructability logging (live since 2 Aug, fines up to €15M/3%)** is unmeetable without it: you cannot reconstruct who did what if the actors have no names.

**Bottom line:** the gate and the larder both assume you can name the traveler standing at the door — and this week the market moved to issue the papers. **When machine actors outnumber people a hundred to one and most of them are agents acting on their own or on a human's behalf, the enterprise control point is identity: a real, centrally issued, short-dated, revocable passport for every agent, checked at every door and written into every log.** An enterprise running agents on static keys and borrowed tokens has a hundred travelers it cannot name, meter, or turn back — a gate with nothing to check and an audit log full of anonymous hands. **Stop treating agents as anonymous traffic and start treating them as identities: register every agent in the same directory as your people, govern it with the same policy, issue it a scoped, short-lived credential instead of a static key, and make sure you can revoke it in a second — because when the workforce is mostly machines, the one thing that turns a crowd into a governed workforce is a name.**

---

## 2 · Allegory of the Day — "The Passport"

*Topic: In the last week of August 2026, the dominant enterprise-AI thread was the arrival of agent identity as a first-class, centrally governed control point. Okta brought Agent SSO to general availability, bringing the open Cross App Access (XAA) standard into an identity platform used by more than 20,000 customers and letting enterprises register AI agents as first-class identities governed by the same centralized policy as human employees, with short-lived scoped tokens replacing static API keys. Palo Alto Networks' 2026 Identity Security Landscape finds machine identities now outnumber humans roughly 109 to 1 (up from ~82:1 a year earlier), with ~79 of 109 being AI agents; CyberArk puts the ratio at "more than 80 to 1." Yet Okta's AI Agents at Work 2026 research (Apprize360; 292 executives, 492 knowledge workers, seven countries) finds 91% of organizations already use AI agents while only 10% have a developed non-human-identity strategy, 88% report a suspected or confirmed AI-agent incident, only 34% apply human-grade identity controls to agents, and only 22% treat an agent as an identity-bearing entity. The EU AI Act's Article 12 reconstructability logging (live since 2 August, fines up to €15M/3%) is unmeetable unless every acting agent has a distinct, attributable identity. The lesson: after building the gate every agent must pass (24 Aug) and the governed larder behind it (25 Aug), the remaining question is who is the agent at the door — and the answer is a real, centrally issued, revocable passport. The passport allegory is the radar's own illustration.*

There was a prosperous realm whose borders had always been easy to keep, because the travelers were few and mostly known — a citizen and their household, a merchant the guards recognized by face. Then the roads filled. Not with people: with **couriers, factors and stewards** sent to act on others' behalf — a hundred of them now for every citizen, and most of them tireless new hires who never slept, never tired, and could be in six market halls at once. They carried letters that began *"acting for the house of so-and-so,"* and they moved fast and did good work. But they carried **no papers of their own.** To get through a door, a courier would borrow a citizen's signet, or copy a key that had been cut years ago and never recalled, or simply wave a letter no clerk had time to read. The realm had gained a vast, willing workforce and lost the one thing that makes a workforce governable: the ability to say, at any door, *who is this, and on whose authority?*

For a while the speed dazzled everyone, and the danger stayed quiet. Then it stopped being quiet. A steward kept using a key long after the man who lent it had left the city. A courier acting "for the house of so-and-so" turned out to be acting for no one anyone could find. When a strongroom was found short or a letter went where it should not, the magistrate's question — *who did this?* — met a shrug, because the ledger recorded only a borrowed signet and a copied key. The realm counted its troubles and the sum was stark: nearly every house was already using the new couriers, yet almost none had any system for papering them; the great majority had already suffered a theft or a scare at their hands; and only a small minority treated a courier as a person to be named at all, rather than as anonymous traffic to be waved through.

The realms that kept their footing did one unglamorous thing: they built a **passport office,** and made it the single place any traveler — citizen or courier — was issued papers. Every courier now got a passport of its own: a **name** (this is agent *such-and-such*, not a borrowed signet), a **sponsor** (it acts for this house, this steward, within these bounds), a **stamp that expired** (good for this errand, this day — not a key cut once and honored forever), and an **entry in one central register** that any gate could check and the office could **revoke in an instant.** The passport did not slow the good couriers; it made them finally *legible.* A guard at any door could now read, in a moment, who stood there and what they were permitted — and a clerk could write a true name in the ledger, so that when the magistrate asked *who did this,* there was an answer.

But the cautionary half of the tale was the realms that heard "issue passports" and did it badly — a different office in every quarter, each with its own book, none talking to the others; passports that never expired, so a courier dismissed at noon still walked through walls at dusk; papers issued but never checked, a stamp no guard bothered to read. They *had* passports and were no safer, because a passport is only worth the one office that issues it, the expiry that limits it, the gate that checks it, and the register that can cancel it. Papers scattered across a dozen desks are not identity; they are the old shrug with a seal on it.

**The moral:** when the workforce becomes mostly couriers acting on others' behalf — a hundred machine travelers for every human, and most of them agents — the border you must keep is not a wall but a **register of who.** The model is rented, the knowledge is your larder, the gate is your one governed door — and the **passport** is what makes the gate mean anything: a real identity for every agent, issued from **one office** (your identity provider), naming it and its **sponsor,** **short-dated** so authority expires with the errand, **checked at every door,** and **revocable in a heartbeat.** Give the agent a name and you can permit it, meter it, log it and, when you must, turn it away. Leave it anonymous and you have not hired a workforce; you have opened your doors to a crowd.

**The question it forces:** *Our systems are now worked by a hundred machine travelers for every human, most of them agents acting on their own or on someone's behalf. Have we built the one passport office — registered every agent as a first-class identity, named its sponsor and its bounds, stamped its authority so it expires with the errand, and kept the power to revoke it in a second — or are our agents still moving on borrowed signets and keys cut long ago, unnamed in the ledger, so that when the magistrate asks who did this, all we can offer is a shrug?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **Can we name every agent — and revoke it in a second?** Machine identities now outnumber people ~109 to 1 and ~72% are AI agents (Palo Alto Networks). **Do our agents each carry a distinct, centrally issued identity with a sponsor and an expiry, or are they running on static API keys and borrowed OAuth tokens we cannot attribute, meter, or turn off quickly?**
- **Is agent identity one office or a dozen?** Okta Agent SSO makes an agent a first-class identity in the same directory as employees, via the open Cross App Access standard. **Are agent credentials issued and governed from our identity provider under one policy, or scattered across every app and team — the "old shrug with a seal on it"?**
- **Would our logs survive the magistrate's question?** The EU AI Act's Article 12 demands reconstructable logs of who did what. **If a regulator or an incident asked "which agent did this, for whom, under what authority," could we answer — or would the ledger show only an anonymous key? (Only 22% treat an agent as an identity at all.)**

### 🏦 Financial Services
- Every agent touching payments, credit or client data is a non-human actor whose every action must be attributable. **Have we registered our agents as identities with scoped, short-lived credentials and human-grade controls (only 34% do), so we can prove — Article-12-grade — exactly which agent moved which money for which client?**
- Standing entitlements are the classic audit finding, now multiplied by agents. **Can we revoke a compromised or retired agent's access instantly across every app, or do stale keys keep working long after the agent should have been dismissed?**

### 🧬 Healthcare / Life Sciences
- Agents reaching PHI, trial data or clinical systems must be as identifiable and revocable as any clinician. **Does each agent have its own passport tied to a sponsor and a purpose, with short-dated tokens — or is a single broad credential letting many agents touch sensitive data under one anonymous key?**
- 88% report an agent security incident. **Do we know which agentic identities can reach patient or research systems today, who sponsors each, and how fast we could cut one off?**

### 🏭 Manufacturing / Industrials
- Agents wired into OT, MES and supplier systems can move physical outcomes. **Is every such agent a named identity with bounded, expiring authority, or are long-lived machine keys — the classic industrial weak point — now also driving autonomous agents no one can individually revoke?**
- Third-party and vendor agents proliferate at the edge. **Do external agents get a governed, time-boxed passport into our systems, or standing access that outlives the engagement?**

### 🛒 Retail / Consumer
- Pricing, service and fulfillment agents act on customer data at scale and sprawl fast. **Are they all issued identities from one provider with cost and access policy attached, or is each team minting its own keys — an uninventoried crowd of couriers with no central register?**
- Consumer-facing agents act "on behalf of" a shopper. **Can we distinguish, name and revoke each agent acting for a customer, so a compromised one can be cut off without breaking the rest?**

### 🏛️ Public Sector / Regulated
- Public accountability requires that every automated action be attributable to a named actor and a lawful basis. **Have we given each agent a real, centrally issued identity, so citizen-facing automation can be audited and, if needed, revoked — or does oversight rest on anonymous service accounts?**
- Procurement and standards matter. **Are we adopting open identity standards for agents (e.g. Cross App Access) so agent identity is portable and vendor-neutral, not locked to one tool?**

---

## 4 · Technical Deep-Dive — The Passport, the Census, and the Register

Read the stack once more as layers priced and governed very differently — but this week, past *which layer you buy,* past *who watches it,* past *who is accountable,* past *through what door every agent passes,* and past *what governed knowledge sits behind that door,* to the question every one of those controls silently assumes an answer to: **who is the actor?** At the **bottom** is the *engine* — the rented, swappable model. Above it are the **rails** (MCP), the **pilotage,** the **acting agent,** the **watchman,** the **guardrail,** the **gate** and the **larder.** All still true. What this week isolates is the layer that makes every other control enforceable: **agent identity — a first-class, centrally governed, revocable name for every non-human actor.** The engineering point is blunt: **a gate can only check papers the traveler actually carries; a log can only record a name the actor actually has. Identity is the precondition, not an afterthought.**

- **The passport — agents become first-class identities.** **Okta Agent SSO (GA, late Aug 2026):** registers an AI agent in the enterprise directory and governs it with the same centralized policy as an employee, via the open **Cross App Access (XAA)** protocol, inside a platform used by **20,000+ customers.** Authorization shifts from each application to the identity provider — the same centralization SSO brought to human access — and agents receive **short-lived, scoped tokens** instead of static API keys, unmanaged tool-to-tool links or repeated consent prompts. Supported XAA apps (Glean, Cursor, Zoom, …) are reachable via the Okta Integration Network. CPO **Arnab Bose:** "With Cross App Access, Okta is excited to bring oversight and control to how agents interact across the enterprise… protocols are only as powerful as the ecosystem that supports them."
- **The census — machines, mostly agents, dwarf people.** **Palo Alto Networks 2026 Identity Security Landscape:** machine identities outnumber humans **~109 to 1** (up from **~82:1** a year earlier), with **~79 of 109 being AI agents (~72%).** **CyberArk:** "more than 80 to 1," positioning machine-identity security as the control plane for the AI era. The population an enterprise must authenticate, authorize and audit is now overwhelmingly non-human and increasingly agentic — a scale no per-app key scheme survives.
- **The register — adoption has outrun identity governance.** **Okta / Apprize360 (AI Agents at Work 2026; 292 execs + 492 knowledge workers, 7 countries):** **91%** already use AI agents; only **10%** have a developed non-human-identity strategy; **88%** report a suspected or confirmed AI-agent incident; only **34%** apply human-grade identity controls to agents; only **22%** treat an agent as an identity-bearing entity. The **EU AI Act's Article 12** (reconstructability logging) and **Article 50** (transparency), **live since 2 Aug (fines up to €15M/3%),** make an attributable identity per agent a de facto legal requirement — an anonymous key cannot satisfy "who did what, when, on what basis."

The strategic core: **when the workforce is mostly machines acting on others' behalf, the control plane is identity — and this week it became a first-class, standard, centrally governed thing.** For a week the frame moved from "own the right layer" to "oversee without custody" to "own the guardrail" to "build the gate" to "own the governed knowledge"; this week's refinement is **the name behind the action.** "We have a gateway and an audit log" is not an answer to "who is the agent that just moved that data"; ***"every agent is a registered identity with a named sponsor, bounded scope, a short-dated credential and instant revocation, issued from one provider on an open standard"*** is the answer.

```
        THE PASSPORT — a gate is only as good as its ability to say who is at it.
        When machines outnumber people 109:1 and 72% are agents, identity is the control plane.

   THE CENSUS (why identity now)                 THE PASSPORT (the control point)
   ┌──────────────────────────────┐            ┌──────────────────────────────┐
   │  Machine IDs vs humans ~109:1   │          │  Agent = first-class IDENTITY    │
   │  (up from ~82:1 a year ago)     │  →  SO   │  Okta Agent SSO (GA) · open XAA  │
   │  ~79 of 109 are AI AGENTS (~72%)│  ISSUE → │  registered like an employee     │
   │  CyberArk: "more than 80 to 1"  │  PAPERS  │  short-lived, scoped tokens      │
   │  ▲ a crowd you cannot name      │          │  ▼ one provider · 20,000+ custs  │
   └───────────────┬──────────────┘            └───────────────┬──────────────┘
                   │   authorization moves from each app to the IdP │
                   ▼                                              ▼
   ┌───────────────────────────────────────────────────────────────────────────┐
   │  THE PASSPORT OFFICE — one register, or it is the old shrug with a seal on it │
   │  NAME = which agent · SPONSOR = for whom, within what bounds                 │
   │  EXPIRY = short-dated authority (not a key cut once, honored forever)        │
   │  REVOKE = cut off in a second · LOG = Art.12 reconstructable "who did what"   │
   │  Okta/Apprize360: 91% use agents · 10% have an NHI strategy · 88% had an incident │
   └───────────────────────────────────────────────────────────────────────────┘
                                                ▼ so
   ┌──────────────────────────────┐   ┌────────────────────────────────────────┐
   │  STOP: anonymous agent traffic │  │  START: agents as governed identities    │
   │  · static API keys             │   │  · register every agent in the IdP       │
   │  · borrowed / broad OAuth       │  │  · sponsor + scope + short-dated token   │
   │  · standing, un-revoked access  │  │  · instant revocation · one open standard│
   │  a crowd you cannot turn back   │   │  give the agent a name → permit·meter·log│
   └──────────────────────────────┘   └────────────────────────────────────────┘
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The anonymous key versus the passport — the same agent, two very different bets

| Running agents on anonymous keys | Running agents as governed identities |
|---|---|
| Static API key or borrowed OAuth token | Registered identity issued from your IdP |
| No sponsor — "acting for the house of someone" | Named sponsor and bounded scope per agent |
| Credential cut once, honored forever | Short-dated token; authority expires with the errand |
| Revocation is slow, per-app, or impossible | Revoke in a second, centrally, across every app |
| Audit log shows an anonymous key | Article-12 log shows *which agent, for whom, why* |
| Identity scattered across every tool | One open standard (Cross App Access), one register |

### Why "the passport" is the artifact that matters

For a year the reflex was to secure the *perimeter* and the *tools;* this week's news says the enforceable unit of control is the *actor.* An identity layer for agents is model-agnostic and unglamorous — it makes no headline like a new frontier release — but it is what turns a gateway into a checkpoint, an audit log into evidence, and a policy into something you can actually enforce against a specific agent. That is why the signal is sharp: a 20,000-customer identity platform just made "AI agent" a first-class identity type on an open standard, precisely as the machine-to-human ratio crossed 100:1. The interesting artifact this week is not a smarter agent — it is **a passport that makes every agent legible, governable and revocable.**

### How it lands on legacy estates

Same seam this radar keeps returning to — **be deliberate about what you own, rent and finance, and on what terms** — now applied to identity. Machine identity is the estate's oldest weak point (long-lived service accounts, keys cut once and never recalled), and agents pour a hundredfold more of it onto the same cracked foundation. The retrofit is **census, then passports, then a register. Take the census:** inventory every agent and non-human identity, because you cannot govern what you cannot count (only 22% even treat agents as identities). **Issue passports:** register each agent in your identity provider, give it a sponsor and a bounded scope, and replace static keys with short-lived, scoped tokens on an open standard (Cross App Access-class). **Keep the register:** make revocation instant and central, and wire every agent's identity into the Article-12 log so "who did what" always has a name. And keep the engine swappable behind it — because the model is the commodity, the knowledge is the moat, and *the identity that makes every agent legible is the control plane.*

**The clean mental model:** *The model is a rented stove; your proprietary knowledge is the larder; the gateway is the one governed door. The passport is what makes that door mean something — a real, centrally issued, short-dated, revocable name for every agent. When a hundred machine travelers arrive for every human and most are agents acting on someone's behalf, the border you keep is a register of who. Give the agent a passport and you can permit it, meter it, log it and revoke it. Leave it anonymous and the gate has nothing to check and the ledger has no name to write.*

### Watch list this week
- **The passport — agents become first-class identities.** **Okta Agent SSO (GA):** register agents like employees, govern with central policy, short-lived scoped tokens via open **Cross App Access (XAA);** 20,000+ customers; CEO Todd McKinnon — agents are "a powerful new identity type" (as reported).
- **The census — machines dwarf people.** **Palo Alto Networks 2026:** machine IDs vs humans **~109:1** (up from ~82:1), **~79 of 109 are AI agents.** **CyberArk:** "more than 80 to 1," identity as the AI-era control plane (as reported).
- **The register — governance lags adoption.** **Okta/Apprize360:** 91% use agents, 10% have an NHI strategy, 88% had an agent incident, 34% apply human-grade controls, 22% treat agents as identities (as reported).
- **The ledger — compliance in statute.** **EU AI Act:** Article 12 reconstructability + Article 50 transparency live since 2 Aug, fines up to €15M/3%; high-risk deferred to Dec 2027 / Aug 2028 (Digital Omnibus). Attribution per agent is the precondition (as reported).
- **The engine — cheap and multiplying (context).** Fastest month in AI history: **11+ models in 20 days.** Opus 5, Grok 4.6, GPT-5.6 / Luna, Gemini 3.7 Flash, open-weight GLM-5.3 / Qwen3.8 / Kimi K3 — the interchangeable engine is why identity, not the model, is the control point (as reported).

---

## 5 · Quotes That Catch the Eye

> AI agents are a powerful new identity type. They can act independently, on their own or on behalf of a user or a team or a company.
> — **Todd McKinnon**, CEO, Okta, on why agents must be treated as first-class identities (as reported)

> With Cross App Access, Okta is excited to bring oversight and control to how agents interact across the enterprise. Since protocols are only as powerful as the ecosystem that supports them, we're also committed to collaborating across the software industry to help provide agents with secure, standardized access to all apps.
> — **Arnab Bose**, Chief Product Officer, Okta Platform, on the open Cross App Access standard (as reported)

> Machine identities outnumber humans by more than 80 to 1.
> — **CyberArk**, 2026 machine-identity research, on the exponential non-human attack surface (as reported)

> "A gate is only as good as its ability to say who is standing at it. When the workforce is mostly machines, the one thing that turns a crowd into a governed workforce is a name."
> — *the radar, on the passport*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| The passport — first-class agent identity | **Okta brought Agent SSO to GA, making an AI agent a first-class, policy-governed identity via the open Cross App Access (XAA) standard, inside a platform used by 20,000+ customers; short-lived scoped tokens replace static API keys** | Okta press release / SecurityBrief / TechNode (as reported) |
| The census — machines vs humans | **Machine identities now outnumber humans ~109 to 1 (up from ~82:1 a year earlier), and ~79 of those 109 are AI agents (~72%)** | Palo Alto Networks 2026 Identity Security Landscape (as reported) |
| The census — corroboration | **"Machine identities outnumber humans by more than 80 to 1"; identity positioned as the control plane for the AI era** | CyberArk 2026 machine-identity research (as reported) |
| The gap — adoption vs governance | **91% of organizations already use AI agents, but only 10% have a developed non-human-identity strategy** | Okta "AI Agents at Work 2026" / Apprize360 (292 execs + 492 knowledge workers, 7 countries) (as reported) |
| The gap — incidents & controls | **88% report a suspected or confirmed AI-agent security incident; only 34% apply the same identity controls to agents as to humans; only 22% treat an agent as an identity-bearing entity** | Okta "AI Agents at Work 2026" / Apprize360 (as reported) |
| The ledger — compliance | **EU AI Act Article 12 (reconstructability logging) + Article 50 transparency live since 2 Aug; fines up to €15M or 3% of global turnover; high-risk deferred to Dec 2027 / Aug 2028** | European Commission / legal coverage |
| The engine (context) | **Fastest month in AI history — 11+ models in 20 days. Opus 5 · Grok 4.6 · GPT-5.6 / Luna · Gemini 3.7 Flash · GLM-5.3 · Qwen3.8 · Kimi K3 (open-weight)** | Model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Take the census — count every agent and non-human identity.** You cannot govern what you cannot name, and only 22% of firms even treat an agent as an identity. **This month, inventory every AI agent and service account touching your systems — who sponsors it, what it can reach, what credential it uses, and how you would revoke it.** Expect the count to shock: machine identities now run ~109 to a human and most are agents. That inventory is the base map for everything below.

2. **Issue the passports — make every agent a governed identity on an open standard.** Anonymous keys are the vulnerability; a named, scoped, short-dated identity is the fix. **Register your highest-risk agents in your identity provider, give each a sponsor and bounded scope, and replace static API keys and broad OAuth with short-lived scoped tokens** — adopting an open agent-identity standard (Cross App Access-class) so the papers are portable, not locked to one tool. Prove it on one high-value agent flow first, then extend.

3. **Keep the register — instant revocation and attributable logs.** A passport is only worth the office that can cancel it and the ledger that records it. **Make agent revocation instant and central (kill a compromised or retired agent's access everywhere in seconds), and wire every agent's identity into an Article-12-grade log** so "which agent did what, for whom, under what authority" always has an answer. Report two numbers to the board next quarter: the share of agents carrying a centrally governed identity, and your mean time to revoke one. **The model is rented, the knowledge is the moat — and the passport is what makes every agent legible, governable, and, when you must, turned away.**

---

*AI Tech Radar · generated 26 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The central development in the window is the arrival of agent identity as a first-class, centrally governed control point — Okta bringing Agent SSO to general availability and, with it, the open Cross App Access (XAA) standard into an identity platform used by more than 20,000 customers, letting enterprises register AI agents as first-class identities governed like employees, with short-lived scoped tokens replacing static API keys; CEO Todd McKinnon calling agents "a powerful new identity type" and CPO Arnab Bose describing the aim as bringing "oversight and control to how agents interact across the enterprise" on an open standard — relayed from Okta's announcement and secondary coverage as reported. The scale figures (that Palo Alto Networks' 2026 Identity Security Landscape found machine identities now outnumber humans roughly 109 to 1, up from about 82 to 1 a year earlier, with roughly 79 of 109 being AI agents; and that CyberArk's 2026 research put the ratio at "more than 80 to 1" and positioned identity as the control plane for the AI era) are relayed from those reports and secondary coverage as reported. The governance-gap figures (that Okta's "AI Agents at Work 2026" research, commissioned by Okta and conducted by Apprize360 in March 2026 across 292 executives and 492 knowledge workers in seven countries, found 91% of organizations already using AI agents but only 10% with a developed non-human-identity strategy, 88% reporting a suspected or confirmed AI-agent security incident, only 34% applying human-grade identity controls to agents, and only 22% treating an agent as an identity-bearing entity) are relayed from Okta/Apprize360 as reported. The EU AI Act facts (Article 50 transparency and Article 12 reconstructability logging applicable since 2 August 2026, fines up to the higher of €15 million or 3% of worldwide annual turnover, high-risk obligations deferred to December 2027 and August 2028 under the Digital Omnibus) are relayed from the European Commission and legal coverage as reported. The model and pricing details (the fastest month in AI history with 11+ models in 20 days; Claude Opus 5, xAI Grok 4.6, OpenAI GPT-5.6 and GPT-5.6-Luna, Google Gemini 3.7 Flash, and open-weight Z.ai GLM-5.3, Alibaba Qwen3.8 and Moonshot Kimi K3) are relayed from model-tracker and vendor coverage as reported and carried as standing context. Prior-day context — this week's editions on the recipe/governed knowledge ("The Recipe," 25 Aug), the gatehouse/control plane ("The Gatehouse," 24 Aug), the reservoir/value gap ("The Reservoir," 23 Aug), the two-edged security blade ("The Locksmith," 22 Aug) and the guardrail ("The Guardrail," 21 Aug) — is referenced only as background. Several primary and secondary pages (including okta.com and a number of trade outlets) were unreachable from the compile environment behind the network egress proxy; those figures were cross-referenced across multiple reputable outlets and search summaries and should be re-verified at source before republishing. The passport allegory — a realm flooded with new couriers who carry no papers of their own, borrow signets and copy old keys, and cannot be named or turned back until the realm issues every traveler one centrally stamped, short-dated, revocable passport checked at every door — is the radar's own illustration and is not a sourced claim about any specific company or product.*
