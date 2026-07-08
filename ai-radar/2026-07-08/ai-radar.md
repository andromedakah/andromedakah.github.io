# 🛰️ AI Tech Radar — Behind the Wall

**Wednesday, 8 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> The connector grew up. For two years MCP was the "USB-C of AI" — a handy developer convenience for plugging a model into a tool. This week it became load-bearing enterprise infrastructure: the **Enterprise-Managed Authorization** extension went stable (log in once through your identity provider, every connector auto-provisioned), and the sweeping **stateless 2026-07-28 specification** lands in three weeks. That is the good news. The catch is the part no press release leads with: a standard becomes infrastructure the day it becomes load-bearing — and the new spec **moves the safety boundary out of the protocol and onto you.** The socket got universal. The danger moved behind the wall.

---

## 1 · Executive Summary (90-second read)

The plumbing this radar keeps flagging just became a utility. **On 18 June 2026 the Model Context Protocol's Enterprise-Managed Authorization (EMA) extension reached "stable,"** giving enterprises a way to provision every MCP connector centrally through their existing identity provider — a user logs in once and every approved tool is wired up, with no per-app OAuth click-through. Okta shipped first (via its Cross App Access protocol); Anthropic wired it into Claude's shared MCP layer, VS Code into the client, and Asana, Atlassian, Canva, Figma, Linear, Supabase and Slack onto the server side. Two weeks later the ecosystem is staring at the **2026-07-28 spec** — the biggest revision since MCP launched — which rebuilds the protocol to be **stateless** so any server instance can sit behind an ordinary load balancer. The agent's interface layer has, quietly, become enterprise infrastructure.

1. **Convenience became a control plane — and that's a feature.** EMA does for agent tools what single sign-on did for SaaS: access decisions move into the **IdP admin console**, producing *one auditable trail across every connector* instead of a thousand personal OAuth grants no one can see. This is exactly the seam this radar has argued for all week — per-agent identity (4 Jul), one governance plane (7 Jul) — now shipping as a named standard with Anthropic, Microsoft and Okta behind it. If your agents authorize themselves tool-by-tool today, you have neither the policy nor the audit trail the 2 August EU AI Act regime will ask for.

2. **The stateless rewrite is a gift to operations — and a transfer of liability.** The 2026-07-28 spec kills the session handshake so agent servers scale like any stateless web tier. But statelessness means the protocol **no longer remembers who is who**: it hands the client tracking identifiers and state objects to pass back. Security analysts are blunt that this *"shifts critical security responsibilities from the protocol itself to developers and platform operators"* — predictable identifiers become a workflow-hijacking and cross-tenant risk, and the new `Mcp-Method` / `Mcp-Name` headers open protocol-confusion and header-leakage paths. You have a **12-month window**; the boundary the protocol used to hold is now yours to hold.

3. **Which makes the gateway the panel, not an option.** Standardization that you don't govern is just a bigger attack surface with better documentation. The mature posture is to route every MCP call through **one policy-and-audit gateway** wired to your IdP: EMA for centralized authorization, the gateway for per-agent identity, egress control, header hygiene, and the immutable log. Adopt the standard *and* own the wiring behind it — because the same maturity that made connection trivial made the failure mode yours.

**Bottom line:** the winning question is no longer *"can our agents reach the tools?"* — the standard just made that trivial. It's *"who owns the wiring behind the socket?"* MCP growing up is genuinely good news; it also silently reassigns the security boundary from a spec you don't control to an operator you do. Adopt EMA, put a governed gateway in front of it, and staff the panel before the 28 July spec — and the 2 August regulator — arrive.

---

## 2 · Allegory of the Day — "Behind the Wall"

*Topic: a convenient standard (MCP) is maturing into load-bearing enterprise infrastructure; the convenience is real, but maturity silently transfers the safety burden from the standard to whoever operates it.*

When electricity was young, every device shipped with its own wiring and its own way of drawing power. Connecting anything was an expert act, bespoke and slow. Then the world standardized the **wall socket** — identical prongs, identical voltage — and connection became magic: any appliance, any room, plug it in and it works. Nobody thinks about it. That is exactly the delight of Enterprise-Managed Authorization: one login and every tool your agent needs is simply *there*, no per-app ritual, "pretty magical," as the engineers building it put it.

Here is the part the board needs. The moment the socket became universal and everyone plugged everything in, the danger didn't disappear — it **moved behind the wall.** The exposed, hand-wired hazard became a hidden one: the gauge of the wiring, the grounding, the fuse box, the load rating, and the question of who is liable when the circuit overloads and the wall catches fire. Standardizing the plug didn't remove the risk; it **relocated it** — from the visible connection, which anyone can now make safely, to the wiring behind the drywall, which only the building's owner controls and only a certified electrician can be trusted with. A universal socket in a building with no fuse box and no inspector isn't convenience. It's a fire waiting for a busy Tuesday.

The AI parallel is exact. **MCP's Enterprise-Managed Authorization is the universal socket** — plug in once, everything connects. **The stateless 2026-07-28 spec is the day the socket went load-bearing** — the whole building now runs on it. And the security boundary the old protocol quietly held for you — sessions, per-connector consent, who-is-who — has **moved behind the wall**, into identifiers and headers and state your developers now manage and your operators now own. The convenience is real and worth having. But the firm that installs the universal socket and never builds the fuse box has not modernized; it has **standardized its way to a single, invisible point of failure.**

**The moral:** the socket is the easy part — own the panel. When a standard becomes infrastructure, connection gets trivial and the wiring becomes your problem; adopt the plug and staff the electrician, or the first overload is on you.

**The question it forces:** *We're about to plug every agent into a universal socket. Who owns the wiring behind it — the identity, the audit log, the load rating — or did we standardize connection and leave the fuse box unbuilt?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- We're adopting a standard that makes connecting agents to tools trivial. **Who owns the wiring behind it** — the centralized authorization, the audit trail, the per-agent identity? If the answer is "each app does its own," we've installed sockets with no fuse box.
- The 2026-07-28 spec **moves the security boundary from the protocol onto our builders.** Does our engineering leadership know that, and do we have the 12 months of runway budgeted — or will we discover it in an incident?
- Can we produce, today, **one auditable list of every MCP connector our agents can reach and who approved it**? If not, that gap is both a security hole and the 2 August EU AI Act evidence we can't yet produce.

### 🏦 Financial Services
- Statelessness replaces sessions with client-held identifiers. If those are predictable, that's a **cross-tenant and workflow-hijacking risk** against systems touching positions and client records. Has security reviewed the new spec against our threat model, or are we assuming the protocol still protects us?
- EMA centralizes tool authorization in our IdP. Is our **identity provider actually the control plane for agents** — with policy, revocation and audit — or are traders' agents still collecting personal OAuth grants no one can see or pull?

### 🧬 Healthcare / Life Sciences
- A single auditable trail across every connector is the compliance artifact we've been missing. Have we made **EMA + a governed gateway the only path** an agent can reach a clinical or patient-data tool — so access is centrally granted, logged, and revocable?
- The new headers (`Mcp-Method`, `Mcp-Name`) can leak sensitive inputs if misused. Do we have **header hygiene and egress controls** on the wire before an agent carries PHI through them?

### 🏭 Manufacturing / Industrials
- MCP is becoming the standard socket for plant-floor and design tools. Are we adopting it **behind one governed gateway** so a maintenance agent and a design copilot share one auth, one audit, one identity fabric — or wiring each integration bespoke again?
- 70% of developers report trouble integrating agents with existing systems. Is the stateless, load-balancer-friendly spec a chance to **retrofit our legacy estate once, cleanly** — or another migration we'll defer until it's forced?

### 🛒 Retail / Consumer
- Every connector our support and merchandising agents touch is a door into customer and pricing data. Does **first-login provisioning through our IdP** mean central control — or just faster, unlogged sprawl if we skip the gateway?
- Could we standardize on MCP to run **cheap agents on routine tools and reserve privileged connectors behind stricter policy** — or is everything getting the same blanket access because the socket made it easy?

### 🏛️ Public Sector / Regulated
- Sovereignty means the **audit trail and the authorization decisions live in systems we control.** Does EMA-through-our-IdP satisfy that, and does our gateway keep the log immutable and on our side of the seam?
- **EU AI Act GPAI enforcement powers take effect 2 August 2026** (max €15M or 3% of global turnover; Article 50 transparency also live). A governed MCP gateway that logs every agent-to-tool call is both our control plane *and* our compliance evidence. Is it one system — or none?

---

## 4 · Technical Deep-Dive — When the Adapter Becomes the Foundation

The defining architectural fact of this week is that **MCP stopped being a convenience and became infrastructure.** Two moves did it. First, **Enterprise-Managed Authorization went stable (18 Jun 2026)**: instead of every user click-through-authorizing every server, the enterprise IdP holds a registry of approved MCP servers and their policies, and a user's connectors are provisioned on first login — with access decisions and a single audit trail living in the IdP admin console. Second, the **2026-07-28 specification** rebuilds the protocol to be **stateless**: it removes the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header, so any server instance can serve any request behind a plain round-robin load balancer, with metadata riding in `_meta` on each call and new `Mcp-Method` / `Mcp-Name` headers enabling gateway-level routing. That is precisely the shape of real infrastructure — and infrastructure changes who is responsible for safety.

**The old world held the boundary for you.** Persistent sessions meant the protocol remembered who was who; per-connector OAuth meant consent was explicit, if noisy. It didn't scale and it wasn't governable — but the spec carried the state. **The new world hands you the wiring.** Statelessness replaces sessions with tracking identifiers and state objects the client passes back, which — as security analysts warn — *"shifts critical security responsibilities from the protocol itself to developers and platform operators."* Predictable identifiers invite workflow hijacking and cross-tenant actions; the new headers invite protocol-confusion attacks and leakage of keys, tokens or PII. The upside is real (session hijacking ends, unsolicited server prompts are barred, auth aligns with OAuth 2.0 / OIDC), but the boundary is now behind *your* wall.

```
        WHEN THE ADAPTER BECOMES THE FOUNDATION  —  what moved, and to whom

                    ┌──────────────────────────────────────┐
                    │   MCP GROWS UP  (this week)            │
                    │  EMA stable · stateless 2026-07-28 spec│
                    └───────────────────┬────────────────────┘
                                        │
              ┌─────────────────────────┴──────────────────────────┐
              ▼                                                     ▼
   ┌────────────────────────┐                       ┌──────────────────────────────┐
   │  THE SOCKET (the win)   │                       │  BEHIND THE WALL (now yours)  │
   ├────────────────────────┤                       ├──────────────────────────────┤
   │ • login once via IdP    │                       │ • state = client-held IDs;    │
   │ • every connector wired │                       │   predictable → hijack risk   │
   │ • one policy + audit     │                      │ • Mcp-Method / Mcp-Name headers│
   │   trail in the console  │                       │   → confusion + leakage        │
   │ • OAuth/OIDC-aligned auth│                      │ • per-agent identity YOU issue │
   │ • scales stateless       │                      │ • egress + header hygiene YOURS│
   │                         │                       │ • immutable audit log YOURS    │
   │  connection is trivial  │                       │  the safety boundary moved     │
   └───────────┬────────────┘                        └───────────────┬──────────────┘
               ▼                                                      ▼
       adopt the standard                                  route it through ONE
       (don't hand-wire agents)                            governed gateway + IdP
                                                           = own the panel
```

*(An inline SVG version of this diagram ships in the web edition.)*

### Why "can our agents reach the tools?" is the wrong question

The standard just made reach trivial — EMA provisions connectors on first login and the stateless spec lets them scale anywhere. Optimizing for *connection* now is like celebrating that every room has a socket while no one has checked the fuse box. **The right question is "who owns the wiring behind the socket?"** — the identity each agent carries, the policy that gates each connector, the hygiene on the headers, and the immutable log of every call. That answer is where safety and compliance actually live once the protocol stops holding them for you.

### How it lands on legacy estates

The panel is, once again, a **gateway retrofit** — the same architectural seam this radar keeps arriving at from every direction. On 4 July it issued per-agent identity ("Who Goes There?"); on 5 July it was the deployment layer; on 6 July it was the spend meter; on 7 July it was the model-neutral router. Today it is the **MCP control plane**: EMA wires centralized authorization into your IdP, and a governed gateway in front of every MCP call carries the per-agent identity, the egress and header controls, and the audit trail the stateless spec no longer provides. Build it once and authorization, portability, cost, and now protocol-level security all run through the same seam. Adopt the standard and skip the gateway, and you've standardized your way to a bigger, better-documented attack surface.

**The clean mental model:** *EMA is the universal socket — plug in once, everything connects. The stateless spec is the day the socket went load-bearing. The security boundary moved behind the wall, into identifiers and headers you now own. Don't just admire the socket; build the fuse box and hire the electrician — one governed gateway, wired to your IdP.*

### Watch list this week
- **EMA stable (18 Jun 2026)** — centralized MCP authorization via your IdP; Okta first (Cross App Access), Anthropic/Claude and VS Code on the client, Asana/Atlassian/Canva/Figma/Linear/Supabase/Slack on the server.
- **MCP 2026-07-28 spec** — stateless core, extensions framework (MCP Apps, Tasks), OAuth/OIDC-aligned auth; effective 28 July, 12-month adaptation window.
- **New security surface** — client-held state identifiers and `Mcp-Method`/`Mcp-Name` headers shift the boundary to builders; review against your threat model now.
- **EU AI Act GPAI enforcement (2 Aug 2026)** — penalty powers and Article 50 transparency go live; a governed MCP gateway doubles as the audit log.

---

## 5 · Quotes That Catch the Eye

> "Logging in once and automatically having all your MCP connectors automatically setup is pretty magical."
> — **Tom Moor, Head of Engineering, Linear**, on Enterprise-Managed Authorization (Model Context Protocol blog, June 2026)

> The enterprise-ready specification "shifts critical security responsibilities from the protocol itself to developers and platform operators."
> — **SecurityWeek**, on the stateless MCP 2026-07-28 specification (July 2026)

> The stateless model makes "the state visible to the model rather than hidden away" — improving transparency while handing explicit state handling to application developers.
> — **Model Context Protocol**, 2026-07-28 specification notes

> "The socket is the easy part. Own the panel."
> — *the radar, on MCP becoming enterprise infrastructure*

> "A standard becomes infrastructure the day it becomes load-bearing — and infrastructure fails to whoever owns the wiring."
> — *the radar, on adopting the standard and the responsibility that comes with it*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| MCP Enterprise-Managed Authorization reached "stable" | **18 Jun 2026** | Model Context Protocol / Anthropic |
| MCP 2026-07-28 stateless specification takes effect | **28 Jul 2026** | Model Context Protocol |
| MCP spec release candidate published (validation window) | **21 May 2026** | Model Context Protocol |
| Window to adapt to the new MCP spec | **12 months** | SecurityWeek / Akamai (as reported) |
| Enterprise AI teams with MCP-backed agents in production | **~78%** | industry survey (as reported) |
| Fortune 500 running MCP servers | **~28%** | industry survey (as reported) |
| MCP SDK monthly downloads | **~97M** | as reported |
| MCP donated to Linux Foundation Agentic AI Foundation | **Dec 2025** | Linux Foundation (as reported) |
| Developers reporting trouble integrating agents with existing systems | **70%** | Gartner (as reported) |
| Enterprise apps embedding task-specific AI agents by EOY 2026 | **40%** | Gartner |
| Agentic AI projects to be cancelled by 2027 | **>40%** | Gartner |
| Combined Big-Three enterprise-AI deployment spend (MSFT/OpenAI/Anthropic) | **~$8B** | PYMNTS (as reported) |
| EU AI Act GPAI enforcement powers in force | **2 Aug 2026** | European Commission |
| EU AI Act max GPAI penalty | **€15M or 3% global turnover** | European Commission |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Make your IdP the control plane for agents — adopt EMA on purpose.** Enterprise-Managed Authorization is stable and shipping; the win is not convenience, it's the **single auditable trail** and central policy it puts in your identity provider. Require that every MCP connector an agent can reach is provisioned and revocable from the IdP admin console — not collected as personal OAuth grants no one can see. That list is also the 2 August EU AI Act evidence you'll otherwise scramble to produce.

2. **Brief engineering on the boundary shift — and budget the 12 months.** The 2026-07-28 spec moves the security boundary from the protocol onto your builders: client-held state identifiers and new headers are now *your* responsibility. Task security to review the stateless model against your threat model **before** it's the default — unpredictable identifiers, header hygiene (no keys/tokens/PII on the wire), and cross-tenant isolation. Treat this as a funded migration with a deadline, not a footnote in a dependency bump.

3. **Put one governed gateway behind the socket.** Adopt the standard, then own the wiring: route every MCP call through a single policy-and-audit gateway wired to your IdP, carrying per-agent identity, egress control, header hygiene, and an immutable log. It's the same seam this radar keeps flagging — identity, cost, portability — now also holding the protocol-level security the stateless spec handed you. Build the fuse box before you fill the building with sockets.

---

*AI Tech Radar · generated 8 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. Where a figure rests on secondary coverage or a single industry source (MCP adoption stats, SDK downloads, the $8B deployment figure, the 12-month window), it is marked "as reported." The SecurityWeek line is quoted from its analysis of the 2026-07-28 specification; the Linear quote is from the Model Context Protocol blog's Enterprise-Managed Authorization announcement.*
