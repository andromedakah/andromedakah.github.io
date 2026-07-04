# 🛰️ AI Tech Radar — Who Goes There?

**Saturday, 4 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> The fastest-growing workforce in your company has no badge. 2026's defining security story isn't a new exploit — it's that your AI agents act with human-level access and no human identity.

---

## 1 · Executive Summary (90-second read)

For two years the enterprise question about agents was *can they do the work?* This week the question the board is actually facing is sharper and more uncomfortable: **who are they, and what are they allowed to touch?** The adoption curve has raced ahead of the control curve, and the gap now has a name — the **enforcement gap** — and a number.

1. **Adoption has outrun control.** In the newest field data, **88% of organizations reported a confirmed or suspected AI-agent security incident in the past year** — yet **82% of executives believe their agents are adequately protected.** That 88-vs-82 spread is the enforcement gap: incidents are already routine while confidence stays high. In healthcare the incident rate is **92.7%.**

2. **Agents have privileges but no identity.** Only **21.9% of teams treat agents as independent, identity-bearing entities**; the rest run them on **shared API keys and inherited human credentials.** Only **7.2% of organizations have a named individual accountable for an agent's behavior**, and only **14.4% say all their agents went live with full security/IT sign-off.** Machines already outnumber humans **82 to 1** in the average enterprise, and **68% of organizations admit they lack identity-security controls for AI** (CyberArk).

3. **The vendors just made governance the gate.** Microsoft began rolling out **Entra Conditional Access for Agents and ID Protection for Agents in early July 2026** — extending Zero Trust so an agent is challenged, scoped, and monitored like any other identity. Google DeepMind's and Anthropic's guidance now frames agents as **potential insider threats** to be least-privileged and watched at runtime. The message from the platform layer is blunt: **an agent with no identity is a liability, not a feature.**

**Bottom line:** the competitive question is moving from *how many agents can we deploy* to *can we prove who each one is and bound what it can do.* The firms that give every agent a real, scoped, revocable identity now will be the ones allowed to scale it — the rest will discover their blast radius the hard way.

---

## 2 · Allegory of the Day — "The Master Key"

*Topic: agents inheriting broad human credentials vs. per-agent scoped identity (Zero Trust for non-human identities).*

A company was proud of its security. Every employee wore a **photo badge**; the turnstile clicked green only for a face that matched. Auditors admired the lobby.

Then the firm got busy and hired a **thousand temps overnight** — tireless, fast, working all hours. There was no time to badge each one. So the facilities manager did the practical thing: he propped a **single master key under the mat by the loading dock**, and told the temps to help themselves. The master key opened every door — the server room, the vault, the CEO's office — because it was easier than deciding which temps needed which rooms.

For a while it worked beautifully. The temps moved faster than the badged staff ever had. Then one night a temp opened a door it never should have, and no one could say *which* temp — because they'd all used the same key, left no distinct trace, and answered to no single manager. The badge system in the lobby, so admired by auditors, had been guarding the front door while the real workforce came and went through the back with a key that fit everything.

The fix was never to fire the temps. It was to **badge them too** — give each one its own credential, opening only the doors its job required, expiring at the end of its shift, logged to a supervisor who owned it. That badge is **agent identity**: a distinct, scoped, short-lived, revocable credential per agent — so "who opened this door?" always has an answer.

**The moral:** you don't get to call the lobby secure while the actual workers share a key under the mat. An identity you can't name is an incident you can't investigate.

**The question it forces:** *If one of our agents did something tomorrow it shouldn't, could we name which agent, on whose authority, and shut only it off — in minutes, not weeks?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- Do our agents run on **their own identities** or on **shared keys and borrowed human logins**? If an agent misbehaved, could we attribute the action to a single agent and revoke *just* it?
- We can likely quote our agent **adoption** number. What is our agent **monitoring-coverage** number — the share of agents in production under active runtime observation? (Industry mean is ~52%; roughly half run unwatched.)
- Who is the **named human accountable** for each production agent's behavior? If the honest answer is "unclear" or "shared," we are in the 92.8% without it.

### 🏦 Financial Services
- Agents touching payments, ledgers, and customer PII on **inherited service accounts** are a regulatory finding waiting to happen. Do our agent identities carry **least-privilege scopes and full audit trails** that would survive a supervisory exam?
- Can we produce, on demand, a **complete inventory** of every agent, its entitlements, and its sponsor — the way we already can for privileged human users?

### 🧬 Healthcare / Life Sciences
- The sector's agent-incident rate is the **highest measured (92.7%)**. For any agent touching PHI or clinical workflows, is access **scoped to the minimum** and **monitored at runtime**, or does it inherit a clinician's broad entitlements?
- Where an agent influences a care or coverage decision, can we **reconstruct exactly what it accessed and why** for a regulator or an ethics review?

### 🏭 Manufacturing / Industrials
- OT/ICS environments were never designed for thousands of autonomous non-human actors. Are agents that reach into **MES, SCADA, or supplier systems** isolated with their own identities, or riding shared integration credentials with a plant-wide blast radius?

### 🛒 Retail / Consumer
- Customer-facing and merchandising agents often hold **standing access to order, pricing, and loyalty systems.** Are those credentials **short-lived and scoped per task**, or long-lived keys an attacker could harvest through a prompt-injection?

### 🏛️ Public Sector / Regulated
- With platform vendors shipping **agent-native Zero Trust** (Entra Conditional Access for Agents, July 2026), should our **procurement and ATO/authorization criteria now require per-agent identity, least privilege, and runtime monitoring** as table stakes — not add-ons?

---

## 4 · Technical Deep-Dive — Zero Trust for Non-Human Identities

The defining technical shift of 2026 is that the **fastest-growing population of "users" in the enterprise is not human.** Machine identities already outnumber people ~**82 : 1**, and AI agents are the fastest-growing class within that. Yet most agents are wired up the way a quick integration always was: **give it a service account, hand it an API key, let it inherit a human's OAuth scopes.** That was tolerable when the "machine" was a nightly batch job with a fixed script. It is dangerous when the machine **reasons, chains tools, and can be steered by untrusted input** (a poisoned document, a malicious webpage, a prompt-injection).

**The core principle — treat every agent as its own identity, and trust nothing implicitly:**

- **Distinct identity per agent.** Not a shared key; a unique, nameable principal — so every action attributes to exactly one agent.
- **Least privilege, scoped to the task.** The agent gets only the entitlements this job needs, not the union of everything its human sponsor can do.
- **Short-lived, revocable credentials.** Tokens that expire fast and can be killed instantly — no standing master key to harvest.
- **A policy gate on every call.** Conditional access evaluates *this agent, this action, this context* at request time — the way MFA gates a human login.
- **Runtime monitoring & audit.** Every tool call logged and watched, because an agent can be *turned* mid-task even if it was benign at deploy.

```
      ❌ TODAY (shared master key)                ✅ ZERO TRUST FOR AGENTS
   ┌──────────┐                              ┌──────────┐
   │  Agent A │─┐   shared service account   │  Agent A │──► own scoped identity ──►┐
   ├──────────┤ │   / static API key          ├──────────┤                          │
   │  Agent B │─┼──►  ●  ───► EVERYTHING       │  Agent B │──► own scoped identity ──►│─► POLICY GATE
   ├──────────┤ │   (ledgers, PII, prod)      ├──────────┤                          │   (per call:
   │  Agent C │─┘   broad blast radius        │  Agent C │──► own scoped identity ──►┘    who/what/context)
   └──────────┘   no per-agent attribution    └──────────┘                              │
                                                                         RUNTIME MONITOR + AUDIT ──► only
                                                                         the doors the task needs, short-lived,
                                                                         revocable, fully attributable
```

*(An inline SVG version of this diagram ships in the web edition.)*

### How it lands on legacy technology

The hard part is that **legacy identity infrastructure was built for humans** — provisioning that takes days, SSO and MFA tuned to interactive logins, entitlement reviews that run quarterly. Agents break every one of those assumptions: they are **created in seconds, exist in the thousands, and act at machine speed.** You cannot hand-provision them, and you cannot review them once a quarter.

Two legacy realities make it worse. First, **many enterprise systems only understand a "user" or a "service account,"** so the fastest path to wiring an agent in is to give it a human's credentials or a shared bot account — exactly the anti-pattern. Second, **legacy apps rarely emit the fine-grained logs** you need to see what an agent did inside them.

The retrofit is an **identity fabric / agent gateway** in front of the estate: a broker that (1) issues a distinct short-lived credential per agent, (2) translates that into whatever the legacy app understands, (3) enforces least-privilege policy on every call, and (4) captures the audit trail the underlying system never produced. It is the same shape as last week's cost-metering gateway — a **governance layer wrapped around systems that were never designed to be called by an autonomous, promptable actor.** The model is the easy part; the identity, the scoping, and the audit plumbing are the work.

**The clean mental model:** *you already badge your people. An agent is a worker too — badge it, scope it, watch it, and be able to fire just that one.*

---

## 5 · Quotes That Catch the Eye

> "The privileged access of AI agents will represent an entirely new threat vector."
> — **Clarence Hinton, Chief Strategy Officer, CyberArk**

> "The race to embed AI into environments has inadvertently created a new set of identity-security risks centered around the access of unmanaged and unsecured machine identities."
> — **Clarence Hinton, CyberArk** (2026 Identity Security Landscape)

> "When adoption outpaces control."
> — **Gravitee, *The State of AI Agent Security 2026*** (report subtitle / framing)

> "An identity you can't name is an incident you can't investigate."
> — *the radar's framing of the enforcement gap*

> "You don't get to call the lobby secure while the real workforce shares a key under the mat."
> — *the radar, on the master key*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Orgs reporting a confirmed/suspected agent incident (past year) | **88%** | Gravitee, *State of AI Agent Security 2026* |
| Executives who believe their agents are adequately protected | **82%** | Gravitee / VentureBeat (the "enforcement gap") |
| Agent-incident rate, healthcare | **92.7%** | Gravitee |
| Teams treating agents as independent, identity-bearing entities | **21.9%** | Gravitee |
| Orgs with a named human accountable for agent behavior | **7.2%** | Gravitee |
| Agents that went live with full security/IT approval | **14.4%** | Gravitee |
| Mean agent runtime-monitoring coverage | **~52%** | Gravitee |
| Machine-to-human identity ratio (avg enterprise) | **82 : 1** | CyberArk, Identity Security Landscape |
| Orgs lacking identity-security controls for AI | **68%** | CyberArk |
| Entra Conditional Access + ID Protection for Agents rollout | **early Jul 2026** | Microsoft / M365 Admin |
| Microsoft Agent 365 general availability | **1 May 2026** | Microsoft Security Blog |
| Agentic AI projects forecast cancelled by end-2027 | **>40%** | Gartner |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Inventory your agents as identities, not integrations.** Produce one list: every production agent, the credential it uses, its entitlements, and its named human sponsor. The agents you can't name or attribute are your first-priority risk — you're likely in the 92.8% without formal accountability.

2. **Kill the shared keys; issue scoped, short-lived identities.** Move agents off inherited human logins and shared API keys onto distinct, least-privilege, expiring credentials brokered through an identity fabric / agent gateway. If a vendor path fits (Entra Conditional Access for Agents, or equivalent), pilot it on your highest-privilege agents first.

3. **Close the enforcement gap with runtime monitoring.** Set a target monitoring-coverage number and report it to the board next to the adoption number. Treat every agent as a potential insider threat: log every tool call, alert on scope violations, and rehearse revoking a single agent in minutes.

---

*AI Tech Radar · generated 4 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own.*
