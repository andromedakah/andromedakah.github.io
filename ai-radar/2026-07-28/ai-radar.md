# 🗓️ AI Tech Radar — The Mailroom

**Tuesday, 28 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> For a month this radar carried a countdown at the foot of every brief — *"MCP's final spec goes live 28 July."* Today it lands. At the top of the day the **Model Context Protocol 2026-07-28 specification went final** — the largest revision since MCP's November-2024 debut, and an unmistakably enterprise release. It rips out the thing that made the old protocol feel safe by accident: **state.** Sessions are gone, the handshake is gone, and **any request can now land on any server** behind a plain load balancer. The standard is now boring, universal, load-bearing infrastructure — **~97M monthly SDK downloads, 10,000+ live servers,** governed by the Linux Foundation. But the same change that makes it scale hands you a bill. As Akamai's threat-research lead put it, going stateless means **"critical security boundaries are now entirely dependent on how developers implement them"** — the protocol used to hold the guardrail; now *"implementation choices will dictate the overall security posture."* The board's question: ***the universal connector we standardized on just moved the security boundary from the wire into our own building — have we built the mailroom to receive it, or are we still trusting a postmaster who no longer remembers our name?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thesis — *the model commoditizes; own and govern the layer around it* — and today the most load-bearing layer of all stopped being a countdown and became a standard. At the top of **28 July,** the **Model Context Protocol (MCP) 2026-07-28 specification went final:** the biggest revision since the protocol's debut, delivered as enterprise plumbing. Its headline is **statelessness** — six coordinated proposals remove the `Mcp-Session-Id` header and the `initialize` handshake, so **"any MCP request can land on any server instance,"** and the sticky routing and shared session stores that horizontal deployments once needed are gone at the protocol layer. Three legacy features (Roots, Sampling, Logging) are **deprecated on a 12-month clock;** authorization is rewritten to align with **OAuth 2.1 and OpenID Connect;** and two extensions — **MCP Apps** (sandboxed HTML UIs) and **Tasks** (long-running work) — ship on the same audit path as a tool call. This is not a fringe protocol: **~97M monthly SDK downloads,** **10,000+ active servers,** and since December 2025 it is stewarded by the **Agentic AI Foundation** under the Linux Foundation (OpenAI and Block among the co-founders). The catch is the whole story. Akamai's **Maxim Zavodchik** warned that the move to a stateless model with rich UI apps and async tasks means **"critical security boundaries are now entirely dependent on how developers implement them"** — the update *"eliminat[es] older protocol-level risks,"* but *"implementation choices will now dictate the overall security posture,"* opening the door to workflow hijacking, cross-tenant access, privilege escalation, secrets leakage, header-based control bypass, hit-and-run DoS against long-running tasks, and phishing through insecure UI panels. The standard standardized the envelope; it did not secure what's inside — and it just handed you the boundary. Meanwhile the market puts a number on the layer: **Gartner** says AI-platform-and-model spend grows **63.4% to $64B in 2026,** with the biggest long-run winners being *"vendors that help enterprises manage where and how AI is used."* And the readiness gap is stark: in **Arctera's** governance survey, **78%** expect AI communications risk to rise but only **19%** have the logging and detection to *prove* what their AI did. The regulatory clock stays loud: **EU AI Act Article 50 + GPAI enforcement lands 2 August (5 days;** €15M or 3% of turnover). Yesterday's open-weight commodity (**Kimi K3**) and last week's frontier jump (**Claude Opus 5, #1 at launch, $5/$25**) are the powder; MCP is the pipe it flows through.

1. **The universal connector went stateless — and the security boundary moved into your building.** MCP is now the default way agents reach tools (~97M downloads, 10,000+ servers), and the 2026-07-28 spec makes it scale like ordinary web infrastructure. But statelessness plus MCP Apps plus async Tasks means the protocol no longer holds the guardrail: **"critical security boundaries are now entirely dependent on how developers implement them."** Adopt the standard — you have no real choice — but the receiving end is now yours to secure.

2. **A standard standardizes the envelope, not the contents.** The spec hardens *authorization* (OAuth 2.1 / OIDC), which is real progress — but Akamai's list of what implementation choices now govern is a mailroom threat model: forged headers that bypass controls, cross-tenant delivery, secrets leakage, DoS against long-running tasks, and phishing through the new UI panels. The connector is safer at the wire and more dangerous at the endpoint. **You own the endpoint.**

3. **The market is paying for exactly this layer — govern it or rent it.** Gartner's $64B / +63.4% forecast names the winners as the vendors that help you *manage where and how AI is used.* Arctera's numbers say almost no one can yet *prove* what their AI did (19%). The MCP audit path (MCP Apps and Tasks on the same consent-and-log rail as a tool call) is the raw material for that proof — **if you own the gateway, the allow-list, and the log,** rather than trusting a vendor's default.

**Bottom line:** the countdown ended and the plumbing went public. A universal standard makes the connection boring and cheap — and quietly relocates the security boundary from the protocol onto you. Don't just plug in because everyone else has. **Build the mailroom** — the ID desk, the scanner, the locked boxes, the logbook — before the first stateless letter arrives.

---

## 2 · Allegory of the Day — "The Mailroom"

*Topic: On 28 July 2026 the Model Context Protocol (MCP) 2026-07-28 specification went final — the largest revision since the protocol's 2024 debut. It makes MCP stateless (the `Mcp-Session-Id` header and the initialize handshake are removed, so "any MCP request can land on any server instance"), deprecates three legacy features on a 12-month clock, rewrites authorization to align with OAuth 2.1 / OpenID Connect, and adds MCP Apps (sandboxed HTML UIs) and a Tasks extension for long-running work. MCP is now the de facto connector — ~97M monthly SDK downloads, 10,000+ active servers, stewarded by the Agentic AI Foundation under the Linux Foundation. Akamai's Maxim Zavodchik warned that going stateless with rich UI apps and async tasks means "critical security boundaries are now entirely dependent on how developers implement them," and that while the update removes older protocol-level risks, "implementation choices will now dictate the overall security posture." The lesson for the enterprise: a universal standard standardizes the connection, not the safety of what flows through it — adopt the protocol, but own the mailroom.*

Once the world agreed on how to address a letter, mail stopped being a favor and became a utility. A standardized envelope, a standard address block, a stamp that means the same thing at every counter — that boring agreement is what lets a note leave a village desk and arrive on another continent, handled by clerks who never met the sender and never will. The genius of a universal postal standard is precisely that **no clerk has to remember you.** Each letter carries everything it needs on its own face; any window can process it; the line moves; the system scales to a planet. This is what "stateless" means, said in ink: the counter keeps no memory of your last visit, so **any counter will do** — and if you need continuity, *you* carry the claim ticket, the tracking number, the receipt. The post holds nothing on your behalf between letters.

That universality is a genuine good, and no serious enterprise should refuse it — refusing the standard envelope in 2026 is refusing to receive mail. But here is the part the excited adopter misses. In the old world of the small local post, a postmaster who knew your face provided a kind of security *by accident:* he'd notice a stranger asking for your mail, hold a suspicious parcel, recognize a forged hand. The moment the system goes universal and stateless — any clerk, any window, no memory — **that accidental security evaporates,** and it does not come back for free. The standard guarantees the envelope will move: reliably, cheaply, behind any counter. It guarantees **nothing** about whether the return address is real, whether the parcel is a bomb dressed as a gift from a brand you trust, whether the box at your end is locked, or whether anyone wrote down what arrived. The universal post moves letters; it does not run your mailroom.

So the disciplined operator, on the day the universal standard arrives, does the unglamorous thing the excited one skips: **builds the mailroom before the first letter lands.** An ID desk that verifies the sender rather than trusting the letterhead — because a forged return address (a spoofed header, a mismatched body) is the oldest trick, and the new spec's own authors moved authorization to OAuth precisely so you'd check the issuer. An inbound scanner that opens the suspicious parcel — because the new "rich panels" (MCP Apps) can carry a phishing payload behind a trusted-looking face, and an async "please hold this" slip (a Task) can be a hit-and-run flood aimed at jamming the dock. Locked boxes, one per recipient, so a letter meant for one tenant never lands in another's tray, and a courier who slips a master key cannot open the whole wall. And above all a **logbook** — every delivery signed for — because when the regulator asks in five days *what your AI did and who reviewed it,* the answer lives in that book, and today only about one enterprise in five can even open one. The universal standard hands you the audit rail (MCP Apps and Tasks ride the same consent-and-log path as any tool call); the mailroom is where you actually use it.

**The moral:** welcome the universal standard — a stateless, load-bearing MCP is a real strategic good, and this radar has argued for a month that the connective layer is exactly what to build on. But a standard standardizes the *envelope,* not the safety of what's inside, and the day it went stateless it moved the security boundary out of the wire and into your building. Plug in — and build the mailroom: the ID desk, the scanner, the locked boxes, and the logbook. The post will move the letter; only you can keep the mailroom.

**The question it forces:** *The universal connector we standardized on went stateless today — no counter remembers us, any request lands anywhere, and the protocol's authors say the security boundary is now ours to implement. Have we built the mailroom — verified senders, scanned the new panels, locked the per-tenant boxes, signed the logbook — or did we plug in because everyone else did and assume the post office still knew our name?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- MCP's stateless spec went final today, and its own security researchers say **"critical security boundaries are now entirely dependent on how developers implement them."** **Who owns our "mailroom"** — the MCP gateway, the sender-verification (OAuth issuer checks), the per-tenant isolation, and the audit log — and can they show it exists, not just that we've "adopted MCP"?
- Gartner says the biggest winners are **vendors that help you manage where and how AI is used,** and the market for that layer is **$64B (+63.4%)** this year. **Are we building that management layer as an owned asset — gateway, allow-list, eval gate, log — or renting it from the vendor whose model we're meant to stay neutral about?**
- Only **19%** of organizations can *prove* what their AI produced and who reviewed it. **In 5 days the EU AI Act's transparency and GPAI enforcement lands — is our MCP audit path wired to produce that evidence, or is "we're compliant" a claim we cannot open a logbook to support?**

### 🏦 Financial Services
- Stateless MCP means the risks are cross-tenant access, privilege escalation and secrets leakage at the *implementation* layer. **For any agent touching customer accounts or trading systems, are our MCP servers running behind an owned gateway that verifies the issuer, scopes credentials per tenant, and logs every call** — or behind a vendor default we've never read?
- The connector is now OAuth 2.1 / OIDC-aligned. **Does our identity team treat every agent-to-tool call as an authenticated, least-privilege transaction** — the same discipline we already apply to payments — rather than a trusted internal hop?

### 🧬 Healthcare / Life Sciences
- MCP Apps introduce sandboxed UI panels that can carry phishing or malicious scripts if implemented loosely. **For any clinical or research agent that renders a panel to a human, have we scanned and consent-gated those UIs** — the inbound scanner on the mailroom — rather than trusting them because they look official?
- Async Tasks can be flooded (hit-and-run DoS). **For long-running agent jobs on sensitive pipelines, do we rate-limit and monitor the task queue,** so a jammed dock can't take down a workflow patients depend on?

### 🏭 Manufacturing / Industrials
- You standardized on universal couplings and fittings on the plant floor precisely so any part interoperates — and you still run the safety inspection. **Apply the same to MCP: adopt the universal standard, but own the inspection point** — the gateway where you enforce which tool sees which data, what's logged, and who signs off.
- Suppliers will ship you agents that "just speak MCP." **Do procurement terms require proof of a secured MCP implementation** — issuer verification, tenant isolation, audit logging — for any agent embedded in what they sell you, given the protocol no longer enforces it for them?

### 🛒 Retail / Consumer
- A storefront agent on stateless MCP is cheap to scale behind a plain load balancer — and exposed at the endpoint. **Have we weighed the Article 50 transparency duty (live in 5 days) AND the MCP mailroom together** — the disclosure *and* the secured connector — rather than one without the other?
- Marketing will want agents wired to every tool overnight. **Do we have an owned MCP gateway and allow-list** so adding a connector is a governed decision with a log, not a silent new door into the building?

### 🏛️ Public Sector / Regulated
- MCP is now stewarded by a Linux Foundation body and is genuinely open — the sovereign, non-proprietary plumbing many public bodies wanted. **Can we adopt that openness and own the security boundary,** so the same universal connector that serves citizens can't be turned into an unlogged side door?
- The evidence regulators will ask for — what the AI did, who reviewed it, where it went — is exactly the **19%** capability most lack. **Is our MCP audit log a standard, retained, queryable artifact** before enforcement lands, or a feature we assume the vendor keeps?

---

## 4 · Technical Deep-Dive — The Mailroom, Not the Post

Read today's release as one lesson about **owning the endpoint, not just adopting the standard,** in three parts — the standard (what actually shipped, and why statelessness is a genuine win), the boundary (what moved onto you the moment the protocol forgot your name), and the mailroom (the discipline you now owe on infrastructure you own).

- **The standard (a real, universal good).** At the top of **28 July,** the **MCP 2026-07-28 specification** went final — the largest revision since the protocol's 2024 debut. **Six coordinated SEPs** make the core **stateless:** the `initialize`/`initialized` handshake is removed (SEP-2575), the `Mcp-Session-Id` header and protocol-level sessions are gone (SEP-2567), and routing headers (`Mcp-Method`, `Mcp-Name`) let **"any MCP request land on any server instance,"** so a remote server that once needed sticky sessions and a shared session store now runs behind a **plain round-robin load balancer.** Three legacy features — **Roots, Sampling, Logging** — are deprecated with **at least a 12-month window** before removal. Authorization is rewritten to align with **OAuth 2.1 and OpenID Connect** (validate the `iss` parameter per RFC 9207; declare OIDC `application_type`). Two extensions ride the same audit-and-consent path as a tool call: **MCP Apps** (sandboxed HTML UIs, SEP-1865) and **Tasks** (long-running work, SEP-2663). This is load-bearing: **~97M monthly SDK downloads,** **10,000+ active servers,** stewarded since December 2025 by the **Agentic AI Foundation** under the Linux Foundation. That part is good, and it is why you adopt it.
- **The boundary (what moved onto you).** Statelessness is the right architecture — and it removes the accidental security the old session layer provided. Akamai's **Maxim Zavodchik** is blunt: going stateless *"and introducing rich UI apps and asynchronous tasks"* means **"critical security boundaries are now entirely dependent on how developers implement them,"** and while the update *"eliminat[es] older protocol-level risks, implementation choices will now dictate the overall security posture."* The concrete failure modes are a mailroom threat model: **workflow hijacking and cross-tenant access; privilege escalation and secrets leakage; header/body inconsistencies that bypass security controls; hit-and-run DoS against long-running tasks; and malicious script execution and phishing through insecure UI panels.** The wire got safer; the endpoint got more dangerous — and the endpoint is yours.
- **The mailroom (the discipline that now falls to you).** When state lived in the protocol, some safety came for free. Stateless, it doesn't. So build the receiving end on infrastructure you own: an **ID desk** (verify the OAuth issuer, don't trust the letterhead), an **inbound scanner** (review and consent-gate MCP Apps panels), **locked per-tenant boxes** (isolation and least-privilege credentials so one letter can't open the whole wall), **rate limits at the dock** (protect long-running Tasks from hit-and-run floods), and a **logbook** (an audit record of every call — the same rail MCP Apps and Tasks already ride). The spec hands you the audit path; the mailroom is where you use it.

The strategic core: **you don't win by adopting the standard; you win by owning the endpoint the standard now exposes.** Everyone will speak MCP — that's what "universal" means, and it's why the connector is finally boring. What differentiates you is the mailroom: the gateway, the issuer checks, the tenant isolation, the scanner and the log, sized to a protocol that no longer remembers anyone's name. After today, "we're MCP-native" is not a security posture; *"we run MCP behind a mailroom we own — verified senders, scanned panels, locked boxes, a signed logbook"* is.

```
        THE MAILROOM — own the endpoint, not just the standard
        A universal standard standardizes the envelope, not the safety inside.

   ┌─────────────────────────────────────────────────────────┐
   │  THE STANDARD — MCP 2026-07-28 spec, FINAL today          │  ✅ UNIVERSAL GOOD
   │  stateless core · sessions & handshake removed            │
   │  any request → any server · OAuth 2.1 / OIDC auth         │
   │  MCP Apps + Tasks · ~97M downloads · 10,000+ servers      │
   └─────────────┬─────────────────────────────────────────────┘
                 │  the protocol forgot your name →
                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │  THE BOUNDARY — moved from the wire into your building    │  ⚠ NOW YOURS
   │  "security boundaries entirely dependent on how           │
   │   developers implement them" (Akamai)                     │
   │  forged headers · cross-tenant · secrets leak · task DoS  │
   │  phishing through insecure UI panels                       │
   └─────────────┬─────────────────────────────────────────────┘
                 │  build the receiving end → on infra you own
                 ▼
   ┌───────────────────────────────────────┐
   │  BUILD THE MAILROOM                    │  the layer to own
   │  ID desk (verify issuer / OAuth) ·      │  audit rail is given:
   │  scanner (review MCP Apps panels) ·     │  MCP Apps + Tasks ride
   │  locked boxes (per-tenant, least-priv)· │  the same consent+log
   │  logbook (audit every call) · dock       │  path as a tool call —
   │  rate limits (task DoS)                 │  USE it
   └───────────────────────────────────────┘

   TRAP: "we're MCP-native" → plug in on vendor defaults → stateless door, no mailroom.
   WIN : "we own the endpoint" → gateway, issuer checks, scanner, locked boxes, log.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — adopt the standard, stop there | The discipline — own the endpoint the standard exposes |
|---|---|
| "We're MCP-native" as a security claim | MCP behind an owned gateway you actually control |
| Trust the sender's letterhead (headers) | Verify the OAuth issuer — check the `iss`, not the label |
| Render MCP Apps panels because they look official | Scan and consent-gate every UI panel before it runs |
| One shared credential, one shared box | Locked per-tenant boxes — isolation and least privilege |
| Assume the vendor keeps the log | Own the audit log — it's your Article 50 evidence in 5 days |

### Why a universal standard is a security event, not just an integration win

Every force this radar tracked all month — commodity models, open weights, agentic autonomy, provenance, the split AI Act calendar — assumed the *model* was the thing to govern. Today reframes the *connector* as the thing to secure. The reassuring reading tempts the trap: "MCP is now OAuth-aligned and Linux-Foundation-governed, so it's safe." But the spec's own security reviewers say the opposite of "safe by default": the move to stateless with rich UIs and async tasks means the protocol has *stopped* holding the boundary, and handed it to whoever runs the server. A firm that hears only "enterprise-ready" plugs in on defaults; a firm that reads the threat model builds a mailroom sized to it. The connector didn't get less important by going universal — it got more, because now everything flows through it and nothing in it remembers you.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine). Today the standing MCP thread — flagged as "behind the wall" (8 Jul) and "the standard coupling" (17 Jul) — reaches its enforcement date and confirms the warning: the connector went universal, and the security boundary moved onto you. On legacy estates the danger is a platform team that upgrades to the 2026-07-28 SDK "because it's the standard," points every agent at a fleet of MCP servers behind a load balancer, and inherits the vendor's defaults — no issuer verification, one shared credential across tenants, UI panels rendered unscanned, and no retained log — a universal front door with no mailroom behind it. The retrofit is the mailroom: an owned gateway that verifies senders, isolates tenants, scans panels, rate-limits tasks and logs every call — stood up *before* the SDK upgrade, and wired to produce the Article 50 evidence due in 5 days.

**The clean mental model:** *A universal standard standardizes the envelope, not the safety of what's inside. Adopt the protocol — and own the mailroom: the ID desk, the scanner, the locked boxes, and the logbook.*

### Watch list this week
- **MCP 2026-07-28 spec — FINAL today.** Stateless core (sessions and handshake removed; any request → any server), OAuth 2.1 / OIDC authorization, MCP Apps and Tasks extensions, three features deprecated on a 12-month clock. ~97M monthly downloads, 10,000+ servers, Linux-Foundation-governed. The connector is now boring, universal — and its security boundary is yours.
- **The security shift (Akamai / SecurityWeek).** Going stateless means "critical security boundaries are now entirely dependent on how developers implement them." Failure modes: cross-tenant access, privilege escalation, secrets leakage, header-based control bypass, task DoS, and phishing through UI panels. Treat the endpoint as the new attack surface.
- **The market prices the layer (Gartner, 20 July).** AI platforms and models spend grows **63.4% to $64B in 2026** (GenAI models +117%; specialized models +210%); the biggest winners are "vendors that help enterprises manage where and how AI is used."
- **The readiness gap (Arctera, 21 July).** 78% expect AI communications risk to rise; only 19% can *prove* what their AI produced and who reviewed it — the exact evidence Article 50 and GPAI enforcement will ask for.
- **The standing plumbing — EU AI Act Article 50 + GPAI enforcement 2 August (5 days;** €15M or 3% of turnover, no grace beyond narrow content-marking) — with **Kimi K3** open weights (live 27 July) and **Claude Opus 5** (#1 at launch, $5/$25) as the powder that now flows through the pipe.

---

## 5 · Quotes That Catch the Eye

> Since the protocol is transitioning to a stateless model and introducing rich UI apps and asynchronous tasks, critical security boundaries are now entirely dependent on how developers implement them.
> — **Maxim Zavodchik**, Senior Director of Threat Research, Akamai, on the MCP 2026-07-28 spec, July 2026 (as reported)

> While the update improves the foundation by eliminating older protocol-level risks, implementation choices will now dictate the overall security posture.
> — **Maxim Zavodchik**, Akamai, on where MCP security now lives, July 2026 (as reported)

> Any MCP request can land on any server instance, and the sticky routing and shared session stores that horizontal deployments needed before are no longer required at the protocol layer.
> — **MCP 2026-07-28 specification**, on the stateless core, July 2026 (as reported)

> Over the long-term, the biggest winners will be vendors that help enterprises manage where and how AI is used across the business.
> — **Arunasree Cheparthi**, Senior Principal Research Analyst, Gartner, 20 July 2026 (as reported)

> "A universal standard standardizes the envelope, not the safety of what's inside. Adopt the protocol — and own the mailroom."
> — *the radar, on the stateless MCP spec*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| MCP 2026-07-28 final spec — live | **28 Jul 2026 (today)** | MCP blog / coverage |
| MCP — stateless core | **6 SEPs · sessions & handshake removed · any request → any server** | MCP blog |
| MCP — deprecated legacy features | **Roots, Sampling, Logging (≥12-month window)** | MCP blog |
| MCP — authorization model | **OAuth 2.1 / OpenID Connect–aligned** | MCP blog |
| MCP adoption | **~97M monthly SDK downloads · 10,000+ active servers** | coverage (as reported) |
| MCP governance | **Agentic AI Foundation (Linux Foundation), since Dec 2025** | coverage (as reported) |
| AI platforms & models market, 2026 | **$64B (+63.4%, from $39B)** | Gartner |
| GenAI models spend growth, 2026 | **+117%** | Gartner |
| Domain-specific / specialized models growth, 2026 | **+210%** | Gartner |
| Orgs expecting AI communications risk to rise | **78%** | Arctera / Hanover Research (as reported) |
| Orgs able to *prove* what their AI produced | **19%** | Arctera / Hanover Research (as reported) |
| Orgs with core AI policies in place | **55%** | Arctera / Hanover Research (as reported) |
| Claude Opus 5 — launch rank / pricing | **#1 · $5 / $25 per 1M tokens** | Anthropic / Artificial Analysis (as reported) |
| Kimi K3 full open weights — live | **27 Jul 2026** | Moonshot / coverage |
| Fireworks AI — Series D raise | **$1.5B** | coverage (as reported) |
| EU AI Act Article 50 + GPAI enforcement | **2 Aug 2026 (5 days) · €15M or 3%** | European Commission |
| Enterprises that can centrally govern their AI agents | **12%** | OutSystems (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Stand up the mailroom before you upgrade the SDK.** Before pointing agents at the 2026-07-28 stateless servers, put an **owned MCP gateway** in front of them: verify the OAuth issuer on every call (don't trust the header), isolate credentials per tenant, scan and consent-gate MCP Apps UI panels, rate-limit long-running Tasks, and log every call. The protocol no longer holds the boundary — build the receiving end first, on infrastructure you own.

2. **Turn the audit rail into Article 50 evidence — you have 5 days.** MCP Apps and Tasks ride the same consent-and-log path as a tool call; that is the raw material for proving *what your AI did and who reviewed it* — the capability only 19% of organizations currently have. Make the MCP log a **standard, retained, queryable artifact** now, and fold it into the transparency and GPAI evidence due 2 August. Don't assume the vendor keeps it.

3. **Own the management layer the market is paying for — don't rent it.** Gartner's $64B / +63.4% forecast names the winners as those who help you *manage where and how AI is used.* Build that as an owned asset — the MCP gateway, the connector allow-list, the eval gate and the log — so that switching models (Opus 5, Kimi K3, whatever ships next) or connectors is a routing decision through *your* mailroom, not a vendor rebuild. Adopt the universal standard; own the endpoint it exposes.

---

*AI Tech Radar · generated 28 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The technical and security facts are relayed from the Model Context Protocol project's specification and blog, Akamai / SecurityWeek security coverage, Gartner, Arctera, Anthropic, Moonshot and market reporting, and are marked "as reported" where they rest on secondary reporting. The MCP 2026-07-28 specification details — a stateless core delivered via six coordinated SEPs (removal of the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header, routing headers `Mcp-Method`/`Mcp-Name`, so "any MCP request can land on any server instance"); deprecation of Roots, Sampling and Logging on at least a 12-month window; authorization rewritten to align with OAuth 2.1 and OpenID Connect (validate `iss` per RFC 9207, declare OIDC `application_type`); the MCP Apps (sandboxed HTML UI) and Tasks (long-running work) extensions; and a final release date of 28 July 2026 — are the MCP project's as relayed via the Model Context Protocol blog and July 2026 coverage. The adoption figures (~97M monthly SDK downloads and 10,000+ active servers as of early 2026, and MCP's December-2025 donation to the Agentic AI Foundation under the Linux Foundation with OpenAI and Block among the co-founders) are relayed from July 2026 coverage as reported. The security characterizations — Akamai Senior Director of Threat Research Maxim Zavodchik's statements that going stateless with rich UI apps and async tasks means "critical security boundaries are now entirely dependent on how developers implement them" and that "implementation choices will now dictate the overall security posture," and the enumerated failure modes (workflow hijacking, cross-tenant access, privilege escalation, secrets leakage, header/body control bypass, hit-and-run DoS against long-running tasks, and phishing through insecure UI panels) — are relayed from SecurityWeek and Akamai July 2026 coverage as reported. The Gartner figures (worldwide AI platforms and models end-user spending of $64B in 2026, up 63.4% from $39B in 2025; GenAI models +117%; specialized/domain-specific models +210%) and the quotation attributed to Gartner Senior Principal Research Analyst Arunasree Cheparthi are from Gartner's 20 July 2026 forecast as relayed via coverage. The Arctera "State of AI Governance 2026" figures (78% expect AI communications risk to rise; 19% have the logging/retention/detection controls to prove what their AI did; 55% have core AI policies) are from the Hanover Research–commissioned survey of ~500 professionals in finance, healthcare and energy/utilities across the Americas and EMEA, relayed via July 2026 coverage as reported. Claude Opus 5 (release 24 July 2026, #1 at launch, $5/$25 per million tokens) and Kimi K3 (full open weights live 27 July 2026) are relayed from July 2026 coverage as reported. The Fireworks AI $1.5B Series D and the EU AI Act Article 50 / GPAI enforcement date (2 August 2026; €15M or 3% of global annual turnover) are relayed from July 2026 reporting and the European Commission respectively. The OutSystems 12%-can-govern figure is relayed from prior 2026 research as reported. The "5 days" figure is a simple count from this edition's date (28 July 2026) to 2 August 2026 and is the radar's own. The mailroom allegory — the historical shift from a local post whose postmaster provided security by acquaintance to a universal, standardized postal system that guarantees the envelope moves but not the safety of its contents, and the resulting need to run one's own mailroom (sender verification, inbound scanning, locked per-recipient boxes, and a delivery logbook) — is the radar's own illustration, told approximately, and is not a sourced claim about any specific postal system or about MCP.*
