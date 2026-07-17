# 🛰️ AI Tech Radar — The Standard Coupling

**Friday, 17 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar warned that a hallmark on the metal is not the safety of the spoon — *keep your own scales.* Today the plumbing beneath every enterprise agent quietly becomes a public standard. In **11 days — on 28 July 2026** — the biggest revision of the **Model Context Protocol (MCP)** since Anthropic shipped it in November 2024 goes final: a **stateless core** that removes the session handshake so any request can land on any server behind a plain load balancer; **Enterprise-Managed Authorization** already promoted to *stable* (18 June) so an agent logs in once through your identity provider instead of scattering API keys; and **MCP Apps**, which let a tool ship an interactive HTML interface a host renders in a sandboxed iframe. Beta SDKs for Python, TypeScript, Go and C# have been out since 29 June. The connective tissue for agents is becoming boring, load-bearing infrastructure — the best thing that can happen to a technology. But the week's other headline is the fine print: security researchers at **Akamai** warn the same standard consolidates the attack surface — the stateless model, the rich UIs and the long-running tasks open fresh avenues for **customer-data exposure, phishing through trusted AI experiences, control-bypass and background-task abuse.** This is a firefighter's question in modern dress: ***when every hose finally couples to every hydrant, have we made the city safer — or have we just made one flaw in the coupling everybody's flaw, and forgotten that the fitting never decided where the water goes?***

---

## 1 · Executive Summary (90-second read)

For three weeks this radar has argued one thesis — *the model is commoditizing; own and govern the layer around it.* Two days ago the standards war for that layer (15 Jul, "the gauge war"); yesterday, who certifies the model itself (16 Jul, "the assayer's mark"). Today the connective standard beneath both stops being a moving target and gets **bolted down.** On **28 July 2026 — 11 days away** — MCP's largest revision since its November-2024 debut becomes final, and it is unmistakably an *enterprise* release: stateless, identity-governed, UI-capable. It lands **five days before** the EU AI Act's mandatory GPAI enforcement (2 Aug 2026, 16 days). Two countdowns, one lesson.

1. **The agent plumbing just became enterprise-grade — and boring.** The 2026-07-28 spec makes MCP **stateless**: it drops the `initialize` handshake and the `Mcp-Session-Id` header, carries client context in `_meta` on every request, and lets any request hit any instance behind a round-robin load balancer — no sticky sessions, no shared session store. **Enterprise-Managed Authorization** went **stable on 18 June**: one SSO login through your IdP, not personal keys pasted into local agent configs. **MCP Apps** let servers ship sandboxed HTML UIs whose every action runs through the same audit-and-consent path as a tool call. This is the moment a protocol turns into infrastructure.

2. **Standardization is a win *and* a consolidation of risk.** When every hose couples to every hydrant, mutual aid scales — but a defect in the shared coupling is now everyone's defect. **Akamai's** security readout on the new spec is blunt: the stateless state, the interactive **MCP Apps**, and the long-running **Tasks** create new avenues for **unauthorized access to customer data, user-targeted phishing through trusted AI experiences, bypass of enterprise security controls, and service disruption through background-processing abuse.** A formal deprecation policy (Active → Deprecated → Removed, 12-month minimums) even standardizes how features *leave* — Roots, Sampling and Logging are already on the clock.

3. **The coupling never decides where the water goes — you do.** A standard fitting lets any engine feed any hydrant; it does not decide *what you spray, at what pressure, or who is allowed to open the valve.* MCP now standardizes **connection, identity and UI.** It does not standardize **which tools your agents may reach, what data they may touch, or what they are for** — and those are exactly the deployer duties the EU AI Act makes enforceable in 16 days (inventory, access control, logging, human oversight). Gartner still expects **40% of enterprise apps to embed task-specific agents by end-2026** and **>40% of agentic projects to be cancelled by end-2027** — the gap is governance, not plumbing.

**Bottom line:** adopt the standard — a stateless, SSO-governed, auditable MCP is a genuine gift, and refusing it is the Baltimore mistake of owning a hose that couples to nothing. But do not confuse a standard connector for a safe deployment. **Own what the coupling leaves to you:** the allow-list of servers and tools, the identity and least-privilege policy behind that single SSO login, the audit trail on every UI action, and the shutoff. The fitting is now universal; the water pressure is still yours to set.

---

## 2 · Allegory of the Day — "The Standard Coupling"

*Topic: On 28 July 2026 the largest revision of the Model Context Protocol goes final — a stateless core, Enterprise-Managed Authorization already stable, and sandboxed MCP Apps — turning the agent-to-tool layer into standardized enterprise infrastructure. Security researchers warn the same standardization consolidates the attack surface. The lesson for the enterprise: a universal connector is a real gift, but it standardizes the *fitting,* never the *fire* — where the water goes, at what pressure, and who may open the valve remain yours to govern.*

On a February morning in 1904, a fire broke out in the heart of Baltimore. It should have been containable. It was not — it burned for some thirty hours and took roughly 1,500 buildings across seventy-odd city blocks. What turned a fire into *the* fire was a detail no one thinks about until the day it kills you: **the couplings didn't fit.** Engine companies raced in from Washington, Philadelphia, New York, even further — and when their crews ran hose to Baltimore's hydrants, the threads wouldn't mate. There were dozens of incompatible coupling standards across American cities. Willing help, working pumps, plenty of water — and firefighters standing in the street unable to connect, watching a city burn for want of a common thread.

Baltimore is why your fire hydrants are standardized today. The disaster forced the trade to do what it had resisted for decades: agree on a **national standard thread**, so that any engine could couple to any hydrant in any city. It was a triumph of the unglamorous — a boring specification that turned a patchwork of local fittings into a network where mutual aid finally *worked at scale.* That is precisely what MCP's 28 July spec does for agents: it makes the connector stateless, identity-aware and universal, so any compliant agent can couple to any compliant tool behind ordinary infrastructure. The right people banded together — the Agentic AI Foundation under the Linux Foundation, with OpenAI, Google, Microsoft, AWS and Block among the founders — and bolted the thread down. Welcome it. An estate whose agents couple to nothing is the 1904 mistake.

But the firefighters who came after Baltimore learned the second half of the lesson, and it is the whole point for your board. **A standard coupling standardizes the *fitting* — never the *fire.*** Once every hose mates to every hydrant, three things become permanently your job, and no thread will do them for you. **Where the water goes:** the coupling doesn't decide which building to save, or which tool an agent may reach, or which data it may touch. **The pressure:** open the same universal fitting carelessly and you don't fight the fire, you blow out the windows — least privilege behind that one convenient SSO login. And **who may open the valve:** a universal connector is a universal connector *for an attacker too*, which is exactly why the researchers warn that the richer the standardized surface — stateless state, interactive apps, background tasks — the more a single flaw in the common coupling becomes everyone's flaw at once.

**The moral:** the cities that survived the next fire were not the ones with the fanciest engines. They were the ones that adopted the common thread *and* kept drilling on where the water goes, at what pressure, and who holds the hydrant key. Adopt the standard — it is the best thing to happen to enterprise agents this year. But own the fireground: the allow-list, the least-privilege identity, the audit trail on every action, and the shutoff. The coupling is now universal. The fire is still yours to fight.

**The question it forces:** *When our agents run on a universal, stateless, SSO-governed connector, do we still own the three things the standard will never do for us — which tools and data each agent may reach, the least-privilege identity behind that single login, and the audit-and-shutoff on every action — or have we mistaken a standard fitting for a safe deployment?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- MCP's largest revision goes final in **11 days (28 July)** and makes the agent connector stateless, SSO-governed and UI-capable. **Do we know how many MCP servers and tools our agents can already reach today** — and do we have an allow-list, or are we about to standardize the plumbing on top of an unmapped estate?
- The same standard **consolidates the attack surface** (Akamai: data exposure, phishing through trusted AI UIs, control-bypass, background-task abuse). **Who owns the security review of every MCP server and MCP App we connect** — before the universal coupling makes one flaw everyone's flaw?
- The connector standardizes *connection, identity and UI* — never *which data an agent may touch or what it is for.* Those are **EU AI Act deployer duties, enforceable in 16 days (2 Aug).** Is our access control, logging and human-oversight evidence ready, independent of the protocol?

### 🏦 Financial Services
- Enterprise-Managed Authorization replaces scattered API keys with **one SSO login through your IdP.** Convenient — and a single, high-value valve. **Have we applied least privilege and step-up controls behind that login**, or does one identity now open every tool an agent can reach?
- MCP Apps render **interactive third-party UIs inside a trusted AI surface** — a textbook phishing vector for a bank. **Do we treat an MCP App like any other third-party integration** (review, sandbox, monitor), or does "it came through the agent" wave it past our controls?

### 🧬 Healthcare / Life Sciences
- A universal connector makes it trivially easy to wire an agent to a new data source. **Can we prove PHI can't traverse an MCP coupling we didn't explicitly approve** — the "where the water goes" the standard will never decide for us?
- Background **Tasks** run long, asynchronous work out of sight. **Do we have logging and human oversight on unattended clinical-adjacent tasks**, or does "the task completed" substitute for "the task was safe"?

### 🏭 Manufacturing / Industrials
- Stateless MCP lets agent tooling scale on ordinary infrastructure — real operational leverage. **Have we mapped which OT and MES systems an agent could reach once the coupling is universal**, and fenced the ones that must never be one connector away?
- Standards outlive the systems that adopt them, but a **deprecation policy** now puts features on a 12-month clock (Roots, Sampling, Logging). **Are our integrations built to survive a deprecation cycle**, or hard-wired to a feature that's already flagged for removal?

### 🛒 Retail / Consumer
- MCP Apps can put a branded, interactive UI in front of a customer through an agent. **Can we show a customer-facing MCP App can't be spoofed or repurposed for phishing** by our own review — not the vendor's assurance?
- A universal connector makes swapping tools easy — including swapping *us* out. **Does our value sit in a tool an agent can trivially replace**, or in the data, workflow and trust the coupling can't copy?

### 🏛️ Public Sector / Regulated
- The standard is stewarded by a **US-anchored foundation** (OpenAI, Google, Microsoft, AWS, Block among founders). **Is depending on it a sovereignty question** for our services — and do we have a governance seat, a mirror, or an exit if the standard moves against our interest?
- The EU AI Act's deployer obligations land in **16 days** and are *not* discharged by adopting a good protocol. **Is our AI inventory, access control and audit trail ready for inspection** regardless of how mature the plumbing becomes?

---

## 4 · Technical Deep-Dive — What the Standard Couples, and What It Leaves to You

Strip the excitement away and the 28 July spec is an infrastructure question: **which parts of the agent-to-tool problem does the standard now solve for everyone, and which parts does it deliberately hand back to you?** Read it as three couplings the standard makes — and three fires it does not fight.

- **The thread (stateless core).** The spec removes the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header; client context now rides in `_meta` on every request. Any request can land on **any** server instance behind a plain round-robin load balancer — no sticky sessions, no shared session store. This is the *universal thread*: MCP tooling now scales on ordinary cloud infrastructure.
- **The hydrant key (Enterprise-Managed Authorization).** Promoted to **stable on 18 June**, EMA makes your identity provider the authority for MCP access: the client obtains an Identity Assertion JWT grant (ID-JAG) during SSO and exchanges it for a server token — no per-server consent screen, no personal API keys in local configs. One key, centrally governed. Convenient, and a single high-value valve.
- **The standard hose (MCP Apps).** Servers can ship interactive HTML that the host renders in a **sandboxed iframe**; UI templates are declared ahead of time so hosts can prefetch, cache and security-review them, and every UI-initiated action travels the **same JSON-RPC audit-and-consent path** as a direct tool call. Rich, and a new surface.

The strategic core: **the standard couples connection, identity and interface — it does not fight the fire.** Three things stay yours no matter how mature the protocol gets. **Where the water goes:** which servers, tools and data each agent may reach — the allow-list. **The pressure:** least privilege behind that single SSO login, so one convenient key does not open every valve. **Who may open the hydrant:** the security review and monitoring of every server and App you couple to, because — as Akamai warns — a universal connector is universal for an attacker too, and the richer the standardized surface, the more a single coupling flaw becomes everyone's flaw.

```
        THE STANDARD COUPLING  —  what the 28 July MCP spec couples, and what it leaves to you
        a standard fitting standardizes the connector, never where the water goes

   ┌───────────────────────────────────────────────┐   ┌──────────────────────────┐
   │ THE THREAD — stateless core                     │   │  THE FIREGROUND           │
   │ no handshake, no Mcp-Session-Id; ctx in _meta   │   │  (what stays yours)       │
   │ any request → any instance, plain load balancer │   │                           │
   ├───────────────────────────────────────────────┤   │  WHERE THE WATER GOES:    │
   │ THE HYDRANT KEY — Enterprise-Managed Auth       │   │  which servers, tools &   │
   │ SSO via your IdP (ID-JAG); no scattered keys    │   │  data each agent reaches. │
   │ stable 18 Jun → one key, one high-value valve    │   │                           │
   ├───────────────────────────────────────────────┤   │  THE PRESSURE: least      │
   │ THE STANDARD HOSE — MCP Apps                    │   │  privilege behind the one │
   │ sandboxed HTML UI; same audit/consent as a tool │   │  SSO login.               │
   │ rich surface → phishing / control-bypass risk    │   │                           │
   ├───────────────────────────────────────────────┤   │  THE VALVE: review &      │
   │ THE SHARED FLAW — one coupling, everyone's risk │   │  monitor every server &   │
   │ stateless state · Apps · Tasks = new abuse paths │   │  App; audit + shutoff.    │
   └───────────────────────────────────────────────┘   └──────────────────────────┘

   TRAP: bolt on the standard, assume it secures you → one coupling flaw is everyone's.
   WIN : adopt the thread, own the fireground → universal connector, governed water.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — a standard fitting is a safe deployment | The discipline — adopt the standard, own the fireground |
|---|---|
| "It connects, so it's governed" | An explicit allow-list of servers, tools and data each agent may reach |
| One convenient SSO login treated as one convenient permission | Least privilege and step-up behind EMA — the key isn't the policy |
| An MCP App waved through because "it came via the agent" | Every App reviewed and monitored like any third-party integration |
| Trusting the sandbox to make interactive UIs safe | Audit trail on every UI action; treat rich surfaces as phishing-capable |
| Assuming a mature protocol discharges compliance | Inventory, access control, logging, oversight — your EU AI Act evidence |

### Why a universal connector can't carry your governance

A standard thread is a networking win, not a policy. It guarantees that any compliant agent *can* couple to any compliant tool; it says nothing about whether it *should.* The stateless core scales your tooling and, by design, means any request can hit any instance — which is why identity and least-privilege move up in importance, not down. EMA centralizes the login but not the decision of what that login may do. MCP Apps standardize the audit *path* but not your review of what rides it. Every one of these is the "where the water goes / at what pressure / who holds the key" the coupling was never meant to answer — and every one of them is a named EU AI Act deployer duty that becomes enforceable in **16 days.** The protocol is the vendor's gift; the fireground is yours.

### How it lands on legacy estates

This is the same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the spend meter, 7 Jul the model-neutral router, 8 Jul the MCP control plane, 9 Jul the deployment-labor market, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe that walks out, 13 Jul govern the goal not the gauge, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark). Today it names the plumbing: **the coupling standardizes.** On legacy estates the danger is *coupling-trust* — the universal thread makes it a two-minute job to wire a decades-old core to an agent, and the very ease is the risk. The retrofit is the same control plane this radar has urged all fortnight, now aimed at the connector: an allow-list of approved servers and tools, least-privilege identity behind EMA, a security review gate for every MCP App, and an audit-and-shutoff on every action — the plumbing standardized, the fireground owned.

**The clean mental model:** *A standard coupling standardizes the fitting, not the fire. Adopt the universal thread — an estate whose agents couple to nothing is the 1904 mistake — but own where the water goes, the pressure, and who holds the key.*

### Watch list this week
- **MCP 2026-07-28 spec (final in 11 days)** — largest revision since MCP's Nov-2024 debut; **stateless core** (no handshake, no `Mcp-Session-Id`, context in `_meta`, any request → any instance); Extensions framework; Tasks graduated core → extension; **MCP Apps** (sandboxed HTML UI); authorization hardening (OAuth 2.0 / OIDC, RFC 9207 `iss` validation); formal deprecation policy.
- **Enterprise-Managed Authorization** — went **stable 18 June**; SSO via your IdP (ID-JAG grant), no per-server consent, no scattered keys; supported by an initial set of MCP servers; Okta / Anthropic / VS Code support.
- **Beta SDKs** — Python, TypeScript, Go and C# betas shipped **29 June** so teams can test the revision now; Tier-1 SDKs expected to ship support within the RC window.
- **The security readout** — Akamai flags the stateless model, MCP Apps and Tasks as new abuse avenues: **customer-data exposure, phishing through trusted AI experiences, control-bypass, background-task abuse**; SecurityWeek: "new enterprise-ready MCP spec brings new security challenges."
- **Deprecation on the clock** — Active → Deprecated → Removed with 12-month minimums; Roots, Sampling and Logging deprecated under the new policy.
- **Stewardship** — MCP donated to the **Agentic AI Foundation** (Linux Foundation) in Dec 2025; OpenAI, Google, Microsoft, AWS and Block among founders; 10,000+ MCP servers published as of early 2026 (as reported).
- **The mandatory counterweight** — EU AI Act **GPAI enforcement applicable 2 Aug 2026 (16 days)**; €15M or 3% of global turnover (Art. 101); reaches deployers. Governance gap persists — ~8% of organizations report a comprehensive AI-governance framework while ~88% use AI (as reported).
- **Adoption cadence** — Gartner: 40% of enterprise apps embed task-specific agents by end-2026 (from <5% in 2025); >40% of agentic projects cancelled by end-2027.

---

## 5 · Quotes That Catch the Eye

> The specification eliminates the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header — client information now travels in `_meta` on every request — so any MCP request can "land on any server instance" without sticky routing or shared session stores.
> — **Model Context Protocol blog**, on the 2026-07-28 stateless release candidate (final ships 28 July 2026)

> The introduction of application-managed state, rich interactive AI interfaces, and long-running asynchronous tasks creates new avenues for abuse — unauthorized access to customer data, user-targeted phishing through trusted AI experiences, the bypass of enterprise security controls, and service disruption.
> — **Akamai security research**, on the new enterprise-ready MCP specification (as reported)

> Enterprise-Managed Authorization lets organizations govern which MCP servers their developers can connect to through the same identity provider they already use for SSO — instead of asking every engineer to paste personal API keys into local agent configs.
> — **Coverage of MCP EMA going stable**, 18 June 2026 (as reported)

> More than 40% of agentic-AI projects will be cancelled by end-2027 — the constraints are governance, risk and unclear business value, not the plumbing.
> — **Gartner**, on agentic-AI adoption (as reported)

> "A standard coupling standardizes the fitting, not the fire. Adopt the universal thread — but own where the water goes, the pressure, and who holds the key."
> — *the radar, on the agent connector*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| MCP's largest revision goes final | **28 Jul 2026 (11 days)** | Model Context Protocol blog |
| Biggest revision since MCP's debut | **Nov 2024** | MCP / coverage |
| Stateless core removes | **Handshake + `Mcp-Session-Id`** | MCP blog |
| Enterprise-Managed Authorization stable | **18 Jun 2026** | InfoQ / coverage (as reported) |
| Beta SDKs shipped (Python/TS/Go/C#) | **29 Jun 2026** | Coverage (as reported) |
| New standardized surfaces flagged by Akamai | **Stateless state · Apps · Tasks** | Akamai / SecurityWeek (as reported) |
| Deprecation window (Active→Deprecated→Removed) | **≥ 12 months** | MCP blog |
| MCP servers published (early 2026) | **10,000+** | Coverage (as reported) |
| Stewarding foundation | **Agentic AI Foundation (Linux Foundation)** | Coverage (as reported) |
| EU AI Act GPAI enforcement becomes applicable | **2 Aug 2026 (16 days)** | European Commission (Art. 101) |
| Maximum GPAI penalty | **€15M or 3% of global turnover** | European Commission |
| Orgs with a comprehensive AI-governance framework | **~8%** (vs ~88% using AI) | Industry surveys (as reported) |
| Enterprise apps embedding task-specific agents by end-2026 | **40%** (from <5% in 2025) | Gartner |
| Agentic-AI projects projected cancelled by end-2027 | **>40%** | Gartner |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Adopt the standard — then map the fireground before you couple.** Say yes to the 28 July spec: a stateless, SSO-governed, auditable MCP is a genuine upgrade, and an estate whose agents couple to nothing is the 1904 mistake. But before the universal thread makes wiring trivial, produce the one artifact the protocol won't: an **allow-list of which MCP servers, tools and data each agent may reach.** Where the water goes is your decision, not the coupling's — and it is your EU AI Act inventory evidence in 16 days.

2. **Set the pressure behind the one SSO login.** Enterprise-Managed Authorization is convenient precisely because it centralizes the key — which is why least privilege matters *more*, not less. Put **step-up controls and scoped, least-privilege permissions** behind that single login so one convenient valve doesn't open every tool. And treat **every MCP App like any third-party integration**: review it, sandbox it, monitor it, and keep an audit trail on every UI action — the researchers' phishing-through-trusted-AI warning is about exactly this surface.

3. **Write the coupling's shutoff and deprecation plan now.** A universal connector is universal for an attacker too, and a shared standard puts features on a 12-month deprecation clock (Roots, Sampling, Logging already flagged). For every agent in production, document the **kill switch** (who can pull a server or App, how fast) and the **migration path** off deprecated features, and keep a **model- and tool-neutral abstraction** (7 Jul) so no single coupling becomes load-bearing lock-in. Own the thread, own the shutoff.

---

*AI Tech Radar · generated 17 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The MCP 2026-07-28 specification mechanics — the stateless core (removal of the `initialize`/`initialized` handshake and `Mcp-Session-Id`, context in `_meta`, any request landing on any instance), the Extensions framework, Tasks graduating from core to extension, MCP Apps (sandboxed HTML UI on the shared audit/consent path), authorization hardening (OAuth 2.0 / OpenID Connect, RFC 9207 `iss` validation), and the Active→Deprecated→Removed deprecation policy with 12-month minimums (Roots, Sampling, Logging deprecated) — are relayed from the Model Context Protocol blog and secondary coverage; the final-spec date of 28 July 2026 is the MCP project's, and the "11 days" figure is a simple count from this edition's date. Enterprise-Managed Authorization going stable on 18 June 2026 and the 29 June beta SDKs are relayed from InfoQ, TechTimes and secondary coverage and marked "as reported." The security-risk characterization (customer-data exposure, phishing through trusted AI experiences, control-bypass, background-task abuse) is relayed from Akamai and SecurityWeek and marked "as reported." The 10,000+ MCP servers figure, the Agentic AI Foundation stewardship (OpenAI, Google, Microsoft, AWS, Block among founders), and the ~8% comprehensive-governance / ~88% AI-use figures rest on secondary coverage and industry surveys and are marked "as reported." The EU AI Act mechanics (GPAI enforcement applicable 2 August 2026; €15M or 3% of turnover; Art. 101) are relayed from the European Commission; the "16 days" figure is a simple count from this edition's date to 2 August 2026. The Gartner figures (40% embed by end-2026; >40% cancelled by end-2027) are Gartner's. The 1904 Great Baltimore Fire / fire-hose-coupling standardization allegory is the radar's own historical illustration and is not a sourced claim about AI.*
