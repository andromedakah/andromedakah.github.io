# 🗓️ AI Tech Radar — The Deputy

**Tuesday, 18 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday this radar counted the crossings — and found that 95% of enterprise AI pilots never reach the far bank where value is booked. Today it looks at the ones that *did* cross, and finds they have quietly changed what AI **is** inside the company. It is no longer a clever adviser you consult and then act upon; it is a **deputy that acts** — signs, spends, ships, opens tickets, writes and merges code in your name. The tell is a hard number OpenAI published on 13 August in *"From assistance to execution: How enterprises put AI to work"*: **as of June, Codex — an agent, not a chatbot — generated 64% of combined Codex-and-ChatGPT output tokens among enterprise customers**, and the heaviest-using "frontier firms" now produce **8.3× as many output tokens per user as typical firms, up from 2.6× in January.** The majority of enterprise AI output is no longer answers to read; it is **work already done.** And the moment AI stops advising and starts acting, the governing question flips: not *"is the answer good?"* but ***"who is this deputy, exactly what did we authorize it to touch, and can we prove — in a ledger — what it did in our name?"*** The board's question this morning: ***for every agent now acting inside our operation, do we know its identity, its mandate, and its audit trail — or have we pinned our seal on servants we cannot name?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued the model is a commodity and the moat is the layer you own around it; yesterday it showed how few organizations ever finish the crossing from pilot to value. Today the map turns to what changes for the 5% who *do* cross: **AI has shifted from assistance to execution — from a thing that suggests to a thing that acts** — and that shift, not the next model, is the event that should reorganize your controls. When an agent only advises, its worst failure is a bad idea you can decline. When an agent *acts,* its failure is an action already taken in your name. The scarce discipline this week is not a smarter engine. It is **governing the deputy** — its identity, its mandate, and its ledger.

**The datable signal — the majority of the work is now the agent's.** On **13 August 2026, OpenAI published *"From assistance to execution: How enterprises put AI to work"*** (an Enterprise Signal report), and the numbers mark a threshold. **As of June, Codex generated 64% of the combined Codex-and-ChatGPT output tokens among enterprise customers** — most enterprise AI output is now produced by an agent doing multi-step work, not a chatbot answering a prompt. The gap between leaders and laggards is widening fast: **"frontier firms" (top 10% by usage) now generate 8.3× as many output tokens per active user as typical firms — up from a 2.6× gap in January,** roughly a tripling in five months. And execution is spreading far beyond engineering: since February, Codex weekly-active users grew **108× in legal, 41× in sales and recruiting, 26× in marketing — versus 5× in engineering.** The delegation of real work to agents is the story, and it is accelerating unevenly. As Moor Insights' **Patrick Moorhead** put it this week (17 Aug), **"AI has moved out of the demo phase and into production."**

**Why it matters more than any single launch.** An acting agent is a new kind of actor in your enterprise — one with credentials, tool access and initiative — and the security world has a name for the gap it opens: **non-human identity.** In modern estates, non-human identities already outnumber human users by roughly **45 to 1** (and up to **144 to 1** in cloud-native environments); an autonomous agent can hold credentials for CRM, email, cloud and payments *at once,* and unlike a fixed service account it plans, picks tools and adapts as a task unfolds. That is why the most consequential enterprise release of the moment is not a model but an **identity layer:** Google's **Gemini Enterprise Agent Platform** gives each agent a **fully managed, unique identity,** with access tokens **cryptographically bound to the agent's X.509 certificate** (so a stolen token is unreplayable), agents that **cannot be impersonated** and no long-lived keys — plus per-action authorization and full audit. The engine, meanwhile, kept getting cheaper and more agentic underneath it all: **Gemini 3.7 Flash** (13 Aug) is built "for agents, not chatbots" (AutomationBench **30.4%** vs 17%, at a **50%** introductory price cut), **OpenAI's GPT-5.6 Sol Ultrafast** (Cerebras-powered) hit **~750 tokens/sec** for agent loops (17 Aug), and open-weight **GLM-5.3** and **Qwen3.8** shipped 14 August. Intelligence and speed are abundant. **Accountability for what the agent does with them is the scarce thing.**

1. **The majority of enterprise AI output is now the agent's, not the chatbot's.** Codex = **64%** of combined enterprise output tokens; frontier firms pull away at **8.3×.** Treat this as a governance event, not a productivity stat: **the work is increasingly being *done* by software acting in your name, and every act needs an owner, a boundary and a record.**

2. **When AI acts, identity becomes the control plane.** An acting agent is a non-human identity with real privileges — and there are already ~45 of them per human. **The frontier control is no longer "which model" but "who is this agent, what may it touch, and can we prove what it did?"** Google shipping cryptographically-bound per-agent identity is the tell that the market agrees.

3. **The engine keeps commoditizing — and getting built for action.** **Gemini 3.7 Flash** for agents (13 Aug), **GPT-5.6 Sol Ultrafast** at ~750 tok/s (17 Aug), open-weight **GLM-5.3/Qwen3.8** (14 Aug), **Grok 4.6** at $2/$6 (12 Aug), **Grok 3** retired (15 Aug). The trust gate is live to meet the acting agent: **EU AI Act transparency duties since 2 August** (disclose AI, label output, log it) and the **AITSC consortium (12 Aug).**

**Bottom line:** the model is a commodity, the moat is the layer you own — and this week the data showed that the layer now doing the work is the **acting agent.** The shift from assistance to execution is the real threshold of 2026: it moves AI from *advice you evaluate* to *action taken in your name,* and it makes **agent identity, mandate and audit** the control plane that matters. **Name every deputy, bound what each may do, and keep the ledger of what it did — because you can no longer un-take an action your agent has already performed.**

---

## 2 · Allegory of the Day — "The Deputy"

*Topic: On 13 August 2026, OpenAI's report "From assistance to execution: How enterprises put AI to work" reported that, as of June, Codex (an agent) generated 64% of combined Codex-and-ChatGPT output tokens among enterprise customers, that "frontier firms" now generate 8.3× as many output tokens per active user as typical firms (up from 2.6× in January), and that Codex weekly-active users grew 108× in legal, 41× in sales/recruiting and 26× in marketing since February versus 5× in engineering — evidence that enterprise AI is shifting from assistance (suggesting) to execution (acting). The consequence: an acting agent is a non-human identity with real privileges — such identities already outnumber humans ~45:1 (up to 144:1 in cloud-native estates) — which is why Google's Gemini Enterprise Agent Platform gives each agent a unique, cryptographically-bound identity that cannot be impersonated, with per-action authorization and audit. The lesson: when AI stops advising and starts acting, the control plane becomes identity, mandate and audit — name the deputy, bound what it may do, and keep the ledger. The deputy/badge/ledger allegory is the radar's own illustration.*

For as long as the great house could remember, it had kept **counselors.** Clever men and women sat at the long table and gave their advice — where to plant, whom to trust, what price to hold — and the master listened, and weighed, and then *he* acted, or did not. A counselor's power ended at his lips. His worst counsel, taken, might cost the house a season; his worst counsel, *declined,* cost nothing at all. The whole art of keeping counselors was the art of listening well and choosing for yourself, and the house had grown skilled at it over long years. The counselor spoke; the hand that acted was always your own.

This season the house did a thing it had never done. It pinned a **deputy's badge** on a servant and sent him out into the town to act *in the master's name* — to buy and to sign, to open the counting-house door, to give orders that tradesmen obeyed as though the master himself had spoken. And it did not stop at one. Soon there were deputies everywhere — in the market, in the granary, in the letter-room answering post before dawn — until, if you troubled to count, there were **forty deputies wearing the badge for every one member of the family,** each able to touch the strongroom, the seal, the ledgers and the outer gate at once. The house had discovered that a deputy who *acts* does in an hour what a counselor advising took a week to shape. Most of the day's business, before long, was done not by the family at all but by badged servants moving through the town on the family's authority.

And here was the thing the house was slow to understand: **the moment the badge goes on, every question changes.** A counselor you judge by the wisdom of his words. A deputy you cannot judge that way at all, because by the time you hear of it the deed is already *done* — the coin already spent, the door already opened, the order already obeyed. So the questions that keep a house of deputies safe are not questions of wisdom but of **identity, mandate and record:** *Which deputy is this, exactly — and can a stranger pin on a borrowed badge and pass for him? What, precisely, did we authorize this one to do — and what did we forbid? And is there a ledger, honest and complete, of every act each deputy performed in our name, so that when the strongroom is short we can say whose hand was in it?* A house that sends out badges without answering those three has not become more efficient. It has become one confused morning away from ruin — not from a villain, necessarily, but from the ordinary chaos of authority given and never accounted.

The wise houses, watching the town fill with badged servants, did the unglamorous work at once. They gave every deputy a badge that **could not be forged or lent** — struck so that the man and the badge were one, and a token snatched from his pocket was worth nothing in another's hand. They wrote each deputy's **mandate** narrow and plain — *this one may buy grain and nothing else; that one may open the letter-room but never the strongroom* — so that authority did not spill past its purpose. And they kept a **ledger of every act,** posted and inspected, so that nothing done in the master's name went unrecorded. There was a magistrate at the town gate now, too, newly insistent that any servant acting for a house **declare himself as a deputy and not pose as the master,** and that his doings be logged — for the realm had learned that unnamed authority walking the streets is how counting-houses quietly empty.

**The moral:** when your cleverest servants stop advising and start *acting,* you have not merely gained speed — you have handed out your seal, and a seal in an unnamed hand is a wound waiting to happen. The counselor's era rewarded good listening; the deputy's era rewards good **governance of identity.** Name every deputy so none can be counterfeited. Bound every mandate so authority cannot wander. Keep the ledger so every act has an owner. And never forget the hard asymmetry that separates the two ages: a counsel declined costs nothing, but *an act taken in your name cannot be un-taken.*

**The question it forces:** *The majority of our AI's output is no longer advice we read and weigh — it is work already performed by agents acting in our name, and those agents now outnumber our people many times over. For every one of them, can we say who it is beyond forgery, exactly what we authorized it to touch, and produce the complete ledger of what it has already done — or have we pinned our seal on a crowd of servants we cannot name, bound or account for?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **How much of our AI output is now *action* rather than *advice* — and does each action have an owner?** OpenAI's own data puts agent (Codex) output at 64% of the enterprise mix. **For every agent acting in our name, can we name a human owner, a bounded mandate and an audit trail — or are we treating software that *does* things with the loose governance we used for software that only *suggested* things?**
- **Do our agents have real identities, or borrowed ones?** Non-human identities already outnumber people ~45:1, and an agent can hold CRM, email, cloud and payment credentials at once. **Does each agent have a unique, non-forgeable identity (not a shared service-account key), least-privilege access scoped per action, and credentials that can be revoked the instant it misbehaves — or could a stolen token act as our agent undetected?**
- **When an agent acts wrongly, how fast can we prove what it did and stop it?** The failure of an acting agent is an action already taken. **Can we, today, produce a complete ledger of every tool call, permission used, record touched and change made by a given agent — and kill its access in one move? If not, we are governing deputies as if they were counselors.**

### 🏦 Financial Services
- An agent that can *move* money or *submit* a trade is a different risk class from one that drafts a memo. **For every agent with write access to a system of record, can we prove per-action authorization, segregation of duties, and an immutable audit trail — the same controls we demand of any human with those privileges, applied to a population of non-human identities 45× larger?**
- Speed is now a control question. **With agent loops running at hundreds of tokens a second, how quickly would we detect an agent acting outside its mandate — and is our monitoring built for machine-speed action, not human-speed review?**

### 🧬 Healthcare / Life Sciences
- An acting agent that touches an EHR, orders a test, or writes to a clinical record carries patient-safety and liability weight the moment it acts. **Does every clinical or research agent run under a named identity with a mandate that bars unauthorized actions on protected data, with human sign-off gated on the consequential steps — and a log a regulator could read?**
- Delegated action must not outrun validation. **For any agent embedded in a care or discovery workflow, have we bounded exactly what it may execute autonomously versus what requires a clinician's hand — and can we prove that boundary held on every run?**

### 🏭 Manufacturing / Industrials
- On the floor, an agent that *acts* — adjusts a setpoint, releases an order, schedules maintenance — is closer to an actuator than an adviser. **Do our operational agents have identities, mandates and interlocks the way any control system does, and an audit trail tying every action to an accountable owner?**
- You govern who may touch a machine. **Apply that to software that now touches machines: is every acting agent scoped to least privilege, monitored at machine speed, and revocable in one move if it behaves outside its envelope?**

### 🛒 Retail / Consumer
- Agents are already acting in pricing, merchandising and customer service. **When an agent changes a price, issues a refund, or messages a customer in our name, is there a bounded mandate and a ledger — or could a mis-scoped agent take thousands of actions before anyone notices?**
- Delegation is spreading fastest outside engineering (marketing Codex use up 26×). **Do the non-technical teams now running agents understand they are deploying software that *acts,* and are those agents governed to the same identity-and-audit standard as anything with access to customer data?**

### 🏛️ Public Sector / Regulated
- Public trust cannot survive an unaccountable action taken in the state's name. **Does every agent acting on citizen-facing processes have a declared identity (per the EU AI Act's disclosure duty), a mandate that forbids unauthorized action, and a complete, inspectable log of what it did?**
- Authority given must be authority accounted. **For each deployed agent, do we hold the identity, the least-privilege scope, the audit trail and the one-move revocation that let us answer, after the fact, exactly which agent did what — or have we delegated public authority to software we cannot name?**

---

## 4 · Technical Deep-Dive — From Assistance to Execution

Read the stack, once more, as layers priced very differently — but this week look past *which layer you buy* to **what the top of the stack now does,** because it just changed. At the **bottom** is the *engine* — the raw model, abundant, cheap, and now increasingly *built for action* rather than conversation. Above it are the **rails** — agent infrastructure (MCP and its kin), trending to free. Above those sit the layers this month's editions mapped — the **pilotage** (context, reliability), the **last mile** (distribution), the **business model** (how the vendor gets paid), and the **crossing** (integration, data, adoption, governance) that carries a pilot to value. And sitting *on top of all of them* now is a new kind of actor: the **acting agent** — software that does not return an answer for a human to act on, but *takes the action itself.* The engineering point is blunt: **the unit of AI work in the enterprise has shifted from a completion you read to an action the agent performs — and an action taken in your name demands identity, authorization and audit that a completion never did.**

- **The engine — abundant, cheap, and re-tooled for action.** On **13 August**, **Gemini 3.7 Flash** shipped built "for agents, not chatbots," lifting **AutomationBench to 30.4%** (from 17%) and **DeepSWE to 65.3%** (from ~49%) at a **50% introductory price cut** ($0.75/$3.75 per 1M through year-end). On **17 August**, **OpenAI's GPT-5.6 Sol Ultrafast** (Cerebras-powered) reached **~750 output tokens/sec** — throughput matters because an agent's loop of tool calls is latency-bound, not just intelligence-bound. Open-weight **GLM-5.3** and **Qwen3.8** landed 14 August; **Grok 4.6** tied GPT-5.6 Sol Max at **$2/$6** (12 Aug); **Grok 3** was retired 15 August. Atop Opus 5, Kimi K3 and DeepSeek V4-Pro, the engine is a swappable, cheapening part — now optimized for the thing it will spend most of its cycles doing: *acting.*
- **The rails and the higher layers — necessary, and now carrying real authority.** The **Model Context Protocol's 2026-07-28 specification** went stateless (SDKs past 1B total downloads) — the plumbing an agent uses to reach tools and systems. But a rail that lets an agent *act* on your CRM, your repo and your payments is no longer neutral plumbing; it is a **grant of authority,** and it needs identity and scope attached. This is the seam the market moved on this week.
- **The acting agent — where identity becomes the control plane.** This is the "layer" the OpenAI data exposed. **The work is now the agent's:** **Codex = 64%** of combined enterprise output tokens (June); **frontier firms at 8.3×** typical (from 2.6× in Jan); Codex WAU up **108× legal / 41× sales / 26× marketing** vs 5× engineering since February. **The new actor is a non-human identity:** they outnumber humans **~45:1** (up to **144:1** cloud-native), each potentially holding CRM/email/cloud/payment credentials and adapting its own tool use. **The control that answers it is identity, not intelligence:** Google's **Gemini Enterprise Agent Platform** gives each agent a **unique managed identity,** tokens **cryptographically bound to X.509 certificates** (unreplayable if stolen), agents that **cannot be impersonated,** **no long-lived keys,** **per-action authorization** and **full audit.** That is the shape of the frontier control for an enterprise whose agents now act.

The strategic core: **the engine is cheap, the rails are free, and the newest actor in your enterprise is an agent that acts in your name.** For a month the misread was "own the right layer"; yesterday's was "finish the crossing." This week's correction is sharper still: **once you cross, the thing on the far bank is doing the work itself — so the discipline becomes governing the deputy.** "It's the smartest / cheapest / fastest agent" is not the answer to "who is this actor, what may it touch, and can we prove what it did"; ***"every agent has a non-forgeable identity, a bounded mandate and a complete audit trail, and we can revoke it in one move"*** is the answer.

```
        THE DEPUTY — when AI stops advising and starts ACTING,
        the control plane becomes IDENTITY, MANDATE and AUDIT.
        Most enterprise AI output is now the agent's, not the chatbot's.

   ASSISTANCE (the counselor)                 EXECUTION (the deputy)
   ┌──────────────────────────────┐           ┌──────────────────────────────┐
   │  AI SUGGESTS — a human acts   │           │  AI ACTS — in your name       │
   │  chat / completions you read  │  the work │  Codex = 64% of enterprise    │
   │  worst case: advice declined  │  crosses  │   output tokens (OpenAI, Jun) │
   │  = costs nothing              │─ ─ ─ ─ ─ ▶│  frontier firms 8.3× typical  │
   │  judged by: wisdom of words   │           │  worst case: act already taken│
   └───────────────┬──────────────┘           └───────────────┬──────────────┘
                   │                                           │ a NEW actor:
                   │                          non-human identity, ~45:1 vs humans
                   ▼ the question flips                        ▼ (144:1 in cloud)
   ┌───────────────────────────────────────────────────────────────────────────┐
   │  THE CONTROL PLANE — identity · mandate · audit                            │
   │  IDENTITY: unique, non-forgeable per agent (X.509-bound, unreplayable)     │
   │  MANDATE : least privilege, authorization scoped PER ACTION                │
   │  AUDIT   : full ledger of every tool call · one-move revocation            │
   │  ↳ Google Gemini Enterprise Agent Platform · Agent Identity (the tell)     │
   └───────────────────────────────────────────┬───────────────────────────────┘
                                                ▼ sits atop
   ┌──────────────────────────────┐   ┌────────────────────────────────────────┐
   │  THE ENGINE — built for action│   │  THE GATE — trust, live                 │
   │  Gemini 3.7 Flash (agents)    │   │  disclose the AI · label · LOG the act   │
   │  GPT-5.6 Sol Ultrafast 750t/s │   │  EU AI Act since 2 Aug · AITSC 12 Aug    │
   │  GLM-5.3 · Qwen3.8 · $2/$6    │   │  the magistrate: declare the deputy      │
   └──────────────────────────────┘   └────────────────────────────────────────┘
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The counselor vs. the deputy

| The counselor — AI that advises | The deputy — AI that acts |
|---|---|
| Judge the quality of the answer | Govern the identity of the actor |
| Worst case: bad advice you can decline | Worst case: an action already taken in your name |
| A shared login or service key will do | A unique, non-forgeable, revocable per-agent identity |
| Broad access "to be helpful" | Least privilege, authorization scoped per action |
| A chat log, if anyone keeps it | A complete audit ledger of every tool call, inspected |

### Why identity is the control, not capability

Every layer of the stack this month presumed the brain was cheap and swappable — and this week two things proved it while changing the question. First, the models got visibly *better at acting* (Gemini 3.7 Flash for agents, GPT-5.6 Sol Ultrafast for agent loops). Second, OpenAI's own telemetry showed that acting is now **the majority of enterprise AI output.** Put together, the constraint moves off capability entirely: the agent is smart enough and fast enough to act; the open question is whether you can *account* for what it does. That is not a model problem — it is an **identity, authorization and audit** problem, and it is exactly the problem a service account was never built to solve, because a service account performs fixed, predictable tasks while an agent **plans, chooses tools and adapts.** The correct read of this week is not "agents are getting powerful" — they plainly are — it is "**powerful agents are now acting in your name, so the control plane is who they are and what they may do, not how clever they are.**"

### How it lands on legacy estates

Same seam this radar keeps returning to — **be deliberate about what you own, rent and finance, and on what terms.** On legacy estates the danger is that agents inherit *human-shaped* access — a shared login, a broad role, a long-lived key — and then act at machine speed and machine scale through it. The retrofit is an **identity-and-authority discipline. Name every agent:** give each a unique, non-forgeable identity, never a shared service-account key. **Bound every mandate:** scope access to least privilege, authorize per action, and gate the consequential steps on a human hand. **Keep the ledger:** log every tool call, permission and change, and make the log inspectable and the access revocable in one move. **Post the magistrate:** under the EU AI Act's live duties, disclose when an agent is acting and label and log its actions. And keep the engine swappable underneath — re-benchmark Gemini 3.7 Flash, GLM-5.3, Qwen3.8 and the next release freely, because the brain is the commodity and *the governance of the acting agent is the moat.*

**The clean mental model:** *The model is the engine — abundant, cheap, and now built for action. The rails, pilotage, last mile, business model and crossing are the layers you buy, own or finish. And sitting on top of them now is a new actor — the agent that acts in your name, which the counselor era never had. This week OpenAI's own data said the majority of enterprise AI output is already the agent's, and Google shipped per-agent identity to govern it. When AI stops advising and starts acting, the control plane is identity, mandate and audit. Name every deputy, bound what it may do, keep the ledger — and remember that an act taken in your name cannot be un-taken.*

### Watch list this week
- **The signal — assistance becomes execution, measured.** **OpenAI's *"From assistance to execution"*** (13 Aug) reports **Codex at 64%** of combined enterprise output tokens (June), **frontier firms at 8.3×** typical (up from 2.6× in Jan), and Codex WAU up **108× legal / 41× sales / 26× marketing** vs 5× engineering since February — the majority of enterprise AI output is now the agent's (as reported).
- **The control — identity becomes the plane.** **Google's Gemini Enterprise Agent Platform** gives each agent a **unique managed identity,** tokens **cryptographically bound to X.509 certs** (unreplayable), agents that **cannot be impersonated,** no long-lived keys, per-action authorization and full audit — the enterprise answer to the acting agent (as reported).
- **The scale of the problem — non-human identities.** Non-human identities outnumber humans **~45:1** on average and up to **144:1** in cloud-native estates; a single agent can hold CRM/email/cloud/payment credentials and adapt its own tool use — the ungoverned population your agents now join (as reported).
- **The engine — built for action.** **Gemini 3.7 Flash** for agents (AutomationBench 30.4%, DeepSWE 65.3%, 50% intro price cut, 13 Aug); **GPT-5.6 Sol Ultrafast** ~750 tok/s (17 Aug); open-weight **GLM-5.3/Qwen3.8** (14 Aug); **Grok 4.6** $2/$6 (12 Aug); **Grok 3** retired (15 Aug) (as reported).
- **The gate — trust, live.** **EU AI Act** transparency duties enforceable since **2 Aug** (disclose AI, label output, log it; fines up to €15M/3%, up to €35M/7% for prohibited practice) — directly relevant to disclosing and logging agent action; **AITSC** consortium launched **12 Aug** (~50 founding enterprise security leaders).
- **The field — production is the frame.** **Patrick Moorhead** (Moor Insights, 17 Aug): "AI has moved out of the demo phase and into production," headlining the **Six Five Summit: AI Unleashed** (25–27 Aug, Marc Benioff opening) — the industry's own framing has moved from capability to deployment (as reported).

---

## 5 · Quotes That Catch the Eye

> AI has moved out of the demo phase and into production, and the enterprise leaders defining that shift are the ones building the platforms, the silicon, the cloud, and the agents that customers actually run.
> — **Patrick Moorhead, CEO & Chief Analyst, Moor Insights & Strategy**, on the enterprise-AI shift (17 Aug, as reported)

> Enterprise AI is moving from assistance to execution — and not all firms are making that transition at the same pace.
> — **OpenAI, *"From assistance to execution: How enterprises put AI to work"*** (13 Aug, as reported)

> As of June, Codex generated 64% of the combined Codex-and-ChatGPT output tokens among enterprise customers.
> — **OpenAI Enterprise Signal**, on the majority of enterprise AI output now being the agent's (as reported)

> "When your cleverest servant stops advising and starts acting, you have not merely gained speed — you have handed out your seal. A counsel declined costs nothing; an act taken in your name cannot be un-taken. Name every deputy, bound every mandate, keep the ledger."
> — *the radar, on identity as the control plane for the acting agent*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Enterprise AI output from Codex (an agent) vs ChatGPT | **64% of combined output tokens (as of June)** | OpenAI, "From assistance to execution" (13 Aug 2026, as reported) |
| Frontier-firm vs typical-firm AI usage gap | **8.3× output tokens/active user (up from 2.6× in January)** | OpenAI Enterprise Signal (as reported) |
| Codex weekly-active-user growth since February | **108× legal · 41× sales/recruiting · 26× marketing · 5× engineering** | OpenAI (as reported) |
| Non-human identities vs human users | **~45:1 average; up to 144:1 in cloud-native estates** | Industry / Cloud Security Alliance coverage (as reported) |
| Google Agent Identity (Gemini Enterprise Agent Platform) | **Unique per-agent identity; tokens X.509-bound & unreplayable; no impersonation; no long-lived keys; per-action auth + audit** | Google Cloud (as reported) |
| Gemini 3.7 Flash (built for agents) | **AutomationBench 30.4% (vs 17%); DeepSWE 65.3% (vs ~49%); 50% intro price cut ($0.75/$3.75 per 1M)** | Google / VentureBeat (13 Aug 2026, as reported) |
| GPT-5.6 Sol Ultrafast (Cerebras) | **~750 output tokens/sec; up to ~14× standard throughput** | OpenAI / coverage (17 Aug 2026, as reported) |
| Open-weight releases (14 Aug) · Grok 4.6 · Grok 3 retired | **GLM-5.3 · Qwen3.8 shipped; Grok 4.6 ties GPT-5.6 Sol Max at $2/$6 (12 Aug); Grok 3 deprecated 15 Aug** | Model-tracker / vendor coverage (as reported) |
| EU AI Act — transparency & penalties | **Live since 2 Aug: disclose AI, label output, log it; fines up to €15M/3%, up to €35M/7% for prohibited practice** | European Commission |
| AI Trust & Security Consortium (AITSC) | **Launched 12 Aug; ~50 founding enterprise security/tech leaders** | AIwire / HPCwire (as reported) |
| MCP 2026-07-28 specification | **Stateless core; TS & Python SDKs each past 1B total downloads** | Official MCP blog (28 Jul 2026) |
| The engines (context) | **Opus 5 · GPT-5.6 Sol · Gemini 3.7 Flash · Grok 4.6 · Kimi K3 · DeepSeek V4-Pro · GLM-5.3 · Qwen3.8** | Vendor / model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Inventory every acting agent and give each a real identity — no shared keys.** List every agent that can *do* something (not just answer): what it can touch, whose credentials it uses, and who owns it. Replace shared logins and long-lived service-account keys with a **unique, non-forgeable, revocable identity per agent.** OpenAI's own data says the majority of your AI output is already an agent's work — so this is not housekeeping, it is bringing your largest and fastest-growing population of actors under management. **You cannot govern a deputy you cannot name.**

2. **Bound the mandate and gate the consequential act.** For each agent, scope access to **least privilege** and **authorize per action,** not per session — and put a human hand on the steps that move money, change a system of record, or touch protected data. Grade agents on staying inside their envelope under real conditions, not on a clean demo. **An adviser you can second-guess; an actor you must pre-authorize — because the act is done before you hear of it.**

3. **Keep the ledger and rehearse the kill switch.** Stand up per-agent audit now: log every tool call, permission used and change made, make it inspectable, and prove you can **revoke an agent's access in one move.** Disclose and label agent action under the EU AI Act's live duties. Then run the drill: *a named agent acted outside its mandate at 3 a.m. — how fast can we say exactly what it did and stop it?* **If the answer is "not fast, and not exactly," you are running deputies with a counselor's controls — fix that before the next agent you deploy.**

---

*AI Tech Radar · generated 18 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The OpenAI figures (that its report "From assistance to execution: How enterprises put AI to work," published on or about 13 August 2026 as an Enterprise Signal report, found that as of June 2026 Codex generated ~64% of combined Codex-and-ChatGPT output tokens among enterprise customers; that "frontier firms" — the top ~10% of firms by AI usage — generated ~8.3× as many output tokens per active user as typical firms, up from a ~2.6× gap in January; and that Codex weekly-active users grew ~108× in legal, ~41× in sales and recruiting and ~26× in marketing since February versus ~5× in engineering) are relayed from OpenAI's report and multiple secondary outlets as reported; several primary publisher pages (OpenAI, and various trade outlets) were unreachable from the compile environment behind the network egress proxy and the figures were cross-referenced across multiple reputable outlets and should be re-verified at source before republishing. The Google Gemini Enterprise Agent Platform and Agent Identity details (that each agent receives a fully managed, unique identity; that access tokens issued for Google Cloud are cryptographically bound to the agent's X.509 certificates and made unreplayable to resist token theft; that agent identities cannot be impersonated and do not permit long-lived service-account keys; and that the platform provides per-action authorization and full audit) are relayed from Google Cloud documentation and blog coverage as reported; the platform's general availability was announced earlier in 2026 and Agent Identity is carried here as the standing enterprise mechanism for governing acting agents. The non-human-identity figures (that non-human identities outnumber human users by roughly 45:1 on average and up to ~144:1 in cloud-native environments, and that a single agent can simultaneously hold credentials across CRM, email, cloud infrastructure and payment systems) are relayed from Cloud Security Alliance and identity-industry coverage as reported and are approximate. The model and infrastructure details (Gemini 3.7 Flash shipped on or about 13 August 2026 "for agents," with AutomationBench ~30.4% versus ~17% and DeepSWE ~65.3% versus ~49%, at a 50% introductory price cut of $0.75/$3.75 per million tokens through year-end; OpenAI's GPT-5.6 Sol Ultrafast mode, powered by Cerebras, reaching ~750 output tokens per second and up to ~14× standard throughput, in limited preview around 17 August; open-weight Z.ai GLM-5.3 and Alibaba Qwen3.8 on 14 August; xAI Grok 4.6 tying GPT-5.6 Sol Max at the top of the Artificial Analysis intelligence index at $2/$6 per million tokens on 12 August; the retirement of Grok 3 on 15 August) and the standing engine field (Claude Opus 5, GPT-5.6 Sol, Moonshot Kimi K3, DeepSeek V4-Pro) are relayed from model-tracker and vendor coverage as reported and carried as standing context. The Patrick Moorhead quotation and the Six Five Summit: AI Unleashed details (Marc Benioff opening keynote; 25–27 August 2026) are relayed from the 17 August 2026 Six Five Media / GlobeNewswire announcement as reported. The EU AI Act facts (transparency and disclosure duties enforceable since 2 August 2026; machine-readable labeling of AI-generated content; penalties up to the higher of €15 million or 3% of worldwide annual turnover, and up to €35 million or 7% for prohibited practices) and the AITSC launch (12 August 2026, ~50 founding enterprise security and technology leaders) are relayed from the European Commission and AIwire/HPCwire as reported. The MCP details (the 28 July 2026 specification's stateless core and SDK adoption past one billion total downloads) are relayed from the official Model Context Protocol blog. Prior-day context — this week's editions on the crossing to value ("The Far Bank," 17 Aug), the business model ("The Free Table," 16 Aug), the last mile ("The Last Mile," 15 Aug) and the pilotage ("The Harbor Pilot," 14 Aug) — is referenced only as background. The deputy / badge / ledger allegory — a house that replaces advising counselors with badged deputies who act in its name, forty deputies per family member, a magistrate who requires each deputy to declare himself, and the discipline of non-forgeable identity, bounded mandate and a complete ledger — is the radar's own illustration and is not a sourced claim about any specific company.*
