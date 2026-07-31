# 🗓️ AI Tech Radar — The Last Mile

**Friday, 31 July 2026 · Cross-sector edition · Audience: C-level + Engineering**

> The month's countdown is now measured in hours: **EU AI Act Article 50 transparency and the Commission's GPAI enforcement powers switch on Sunday, 2 August — two days out** (€15M or 3% of global turnover). And the research that landed this week names, with hard numbers, exactly what that audit will find. On **29 July, ChatSee published a study of 10,000+ enterprise AI failure events** and the headline reframes the whole risk conversation: **hallucination is now under 10% of failures.** The dominant failure family is **resolution and escalation breakdowns — 31.1%** — and **execution and action failures are up 62%** on the 2024 baseline. As enterprises move from AI that *answers* to AI that *acts,* the risk migrates from wrong words to unfinished work. ChatSee CEO **Sekhar Sarukkai** put it exactly: *"The enterprise AI question is no longer only whether a model can answer correctly, but whether the AI system can retrieve the right context, take the right action, escalate at the right time, and bring work to resolution."* His example is the whole edition in one sentence: **"A banking customer can report suspicious activity, receive a polite and compliant response, and still never be escalated for human review. That is a serious enterprise failure even if the model never hallucinated."** This is the radar's month-long refrain — *own and govern what doesn't commoditize* — arriving at the layer that matters most this weekend: the model's answer is a solved, near-free commodity (**Opus 5** #1 at **$5/$25**; **GPT-5.6 Sol** on Cerebras at **~750 tokens/sec**; **Kimi K3** open weights), but the **last mile** — the handoff from answer to *completed, escalated, resolved, disclosed* action — is where value is realized, where 88% of pilots still die, and where the 2 August auditor will look. The board's question: ***when the regulator arrives on Sunday and the customer arrives every day, can we prove that our agents took the right action, escalated at the right moment, and closed the loop — or is our last mile an ungoverned gap where the answer was right and the work never happened?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thesis — **the model commoditizes; own and govern the layer around it** — and this week two facts snapped it into focus at the same time. First, the model's *answer* is now cheap, fast and effectively solved: **Claude Opus 5** sits #1 at **$5/$25**, **Claude Sonnet 5** runs **$2/$10** through 31 August (then $3/$15), **GPT-5.6 "Sol"** streams at **~750 tokens/sec** on Cerebras (10–15× typical frontier API speed), and **Kimi K3** is downloadable open weights. Answering correctly is no longer the hard part. Second, on **29 July ChatSee published a study of 10,000+ enterprise AI failure events** that names where the hard part moved: **fewer than 10% of failures are hallucinations.** The single largest failure family is now **resolution and escalation breakdowns at 31.1%,** and **execution/action failures are up 62%** versus the Q2 2024 baseline. The through-line, in the words of ChatSee CEO **Sekhar Sarukkai:** *"The enterprise AI question is no longer only whether a model can answer correctly, but whether the AI system can retrieve the right context, take the right action, escalate at the right time, and bring work to resolution."* When AI only *answered,* a wrong word was the whole risk; when AI *acts,* the risk is a wrong action taken, a human escalation missed, a case left unresolved — the **last mile** from a correct answer to a completed, governed outcome. That is exactly the gap the rest of the market's data describes: **MIT** finds **95% of gen-AI pilots deliver no measurable business impact;** **IDC** finds **88% of agent proofs-of-concept never reach broad production;** **Gartner** expects **40%+ of agentic projects cancelled by end-2027** even as **40% of enterprise apps** carry embedded agents by year-end (up from <5% in 2025). None of that is a model-quality problem — it is a last-mile problem: the work doesn't complete, escalate or resolve reliably, and nobody can prove it did. And the last mile is precisely what becomes enforceable in **two days.** On **Sunday 2 August, EU AI Act Article 50 transparency** (you must disclose a person is dealing with an AI; AI-generated content must be machine-readable-marked; deepfakes labeled) and the **Commission's GPAI enforcement powers** switch on across all 27 member states — the higher of **€15M or 3% of global turnover** (Article 99). The high-risk Annex III paperwork was deferred to **2 December 2027** by the Digital Omnibus, but the transparency-and-GPAI teeth are live this weekend. As BCG framed it, the Act is a **"wake-up call"** to assess AI readiness — and **over half of organizations still lack a systematic inventory** of the AI systems they run. The evidence the auditor wants is a last-mile record: what the agent did, whether it escalated, whether it disclosed, and whether the work resolved.

1. **The answer is solved and nearly free — the last mile is where value and risk now live.** A correct model output is a commodity you rent by the token (Opus 5 $5/$25; Sol at 750 tok/s; Kimi K3 open weights). What is scarce, proprietary and failure-prone is the handoff from a good answer to a *completed, escalated, resolved, disclosed* action — and ChatSee's data says that handoff, not hallucination, is where enterprise AI breaks.

2. **The failure mode inverted: fewer than 10% hallucinations, 31.1% escalation breakdowns, +62% execution failures.** As AI moves from answering to acting, "the model was wrong" gives way to "the model was right and the work still didn't happen" — the customer who reports fraud, gets a compliant reply, and is never escalated. You cannot fix that by buying a smarter model; you fix it by governing the last mile.

3. **Sunday's audit is a last-mile audit — and most firms can't produce the record.** Article 50 transparency and GPAI enforcement land **2 August** (€15M or 3%); the evidence they demand is proof of disclosure and of what your agents did and escalated — yet over half of firms have no AI inventory. **Govern the last mile — action, escalation, resolution, disclosure, logged — or inherit both the unfinished work and the fine.**

**Bottom line:** the model has won the argument nobody is having anymore — it can answer. The unglamorous, expensive, decisive stretch is the **last mile:** turning a correct answer into a completed action, escalated to a human at the right moment, brought to resolution, and disclosed on the record. That is where 88% of pilots die, where ChatSee's 10,000 failures cluster, and where Sunday's auditor will look. **Own and govern the last mile, or keep shipping right answers that never become finished work.**

---

## 2 · Allegory of the Day — "The Last Mile"

*Topic: On 29 July 2026 ChatSee published a study of more than 10,000 enterprise AI failure events finding that fewer than 10% of failures are hallucinations, that the largest failure family is resolution and escalation breakdowns (31.1%), and that execution and action failures are up 62% on the 2024 baseline — evidence that as enterprises move from AI that answers to AI that acts, the dominant risk shifts from incorrect content to failed task completion. ChatSee CEO Sekhar Sarukkai framed it as whether the system can "retrieve the right context, take the right action, escalate at the right time, and bring work to resolution," illustrated by a banking customer who reports suspicious activity, gets a compliant reply, and is never escalated — "a serious enterprise failure even if the model never hallucinated." It lands two days before EU AI Act Article 50 transparency and GPAI enforcement become binding on 2 August (€15M or 3% of turnover), with the answer itself now a cheap commodity (Opus 5 #1 at $5/$25; GPT-5.6 Sol at ~750 tokens/sec; Kimi K3 open weights). The lesson for the enterprise: the model's answer is solved and nearly free; the value, the failure and the audit all live in the last mile — the completed, escalated, resolved, disclosed action — so own and govern the last mile.*

Ask any logistics operator where the money and the misery are and they will tell you the same thing: not the ocean, not the rail, not the thousand-mile line-haul — the **last mile.** A container can cross the Pacific for pennies a kilo, ride a train across a continent, and clear a sorting hub in minutes, all of it automated, cheap and reliable to four-nines. Then the parcel has to get from the local depot to your actual door — up the stairs, past the gate, into the right hands — and *that* stretch, the shortest of the whole journey, routinely eats **most of the delivery cost and nearly all of the failure.** The last mile is where the package that traveled flawlessly for a week is left at the wrong address, marked "delivered" while it sits in a lobby, handed to someone who never signed for it, or dropped at a door with no one to receive it. The line-haul is a solved commodity; the last mile is the unglamorous, expensive, human-shaped stretch where the whole journey is actually kept or lost.

Notice *why* the last mile is hard, because it is not the reason people assume. It is not that the trucks are slow or the parcels wrong — the goods are fine, the network is fast, the routing is correct. It is that the last mile is where the standardized, automatable middle finally meets the messy specificity of a real destination: this door, this recipient, this signature, this exception. Every hard thing lives there — proof of the right handoff, the judgment to leave it or not, the escalation when the recipient isn't home, the record that it actually arrived. A carrier that pours its investment into faster planes and cheaper line-haul while treating the last mile as an afterthought builds a spectacular network that keeps failing at the doorstep — fast, cheap, and somehow the customer still never got the box. The value was never in moving the parcel a thousand miles; it was in the last hundred yards nobody wanted to own.

So read this week honestly. The **line-haul of AI is a solved, near-free commodity:** a #1 model for five dollars, an open-weight colossus you can download, an inference engine streaming seven hundred and fifty tokens a second. Producing a correct answer and moving it across the network is the part that got cheap and reliable. And ChatSee's 10,000 failures are the doorstep: **fewer than one in ten is a wrong parcel** (a hallucination); **31.1% are the parcel that arrived and was never handed over** (the escalation that didn't happen); execution failures — **the wrong door, the unsigned delivery** — are up **62%.** Sarukkai's banking customer is the parcel marked "delivered" while it sits in the lobby: she reported fraud, received a flawless, compliant, non-hallucinated reply, and was **never escalated for human review.** The answer traveled a thousand miles perfectly and failed in the last hundred yards — and no faster plane fixes a doorstep problem.

**The moral:** the line-haul is rented and cheap; the last mile is owned and it is where the journey is won or lost. The model's answer has commoditized — this radar has said so for a month — and the value, the risk and now the *regulation* have all migrated to the last mile: the completed action, the escalation at the right moment, the case brought to resolution, the delivery disclosed and signed for. Build and own that stretch and a correct answer becomes finished work you can prove; neglect it and you run a magnificent network that leaves the box at the wrong door, all day, at machine scale — and on Sunday, an auditor who checks the doorstep, not the plane.

**The question it forces:** *For every agent we run, can we show it did more than answer — that it took the right action, escalated to a human at the right moment, brought the work to resolution, and disclosed that a person was dealing with an AI? Where is the last-mile record — the proof of delivery — and could we produce it on Sunday, 2 August? Have we built and governed the last mile on infrastructure we own, or are we shipping perfect answers into an ungoverned final stretch where the work quietly never gets done?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **The answer is solved; the last mile isn't.** ChatSee finds under 10% of AI failures are hallucinations while escalation breakdowns are 31.1% and execution failures are up 62%. **For our top agents, can we show the work actually completed, escalated and resolved — not just that the model answered well** — or do we only measure the line-haul and not the doorstep?
- Sarukkai: the question is whether the system can *"take the right action, escalate at the right time, and bring work to resolution."* **Who owns the last mile in our AI stack** — the person accountable for escalation policy, action approval, resolution tracking and the audit trail — or is that final stretch nobody's job?
- Article 50 transparency and GPAI enforcement land **Sunday, 2 August** (€15M or 3%), and BCG calls the Act a **"wake-up call."** **Can we produce, on demand, the last-mile record the auditor wants — disclosure, actions taken, escalations made — given that over half of firms have no AI inventory at all?**

### 🏦 Financial Services
- Sarukkai's own example is yours: a customer reports suspicious activity, gets a compliant reply, and is **never escalated.** **For any agent near fraud, complaints, suspicious-activity or suitability, is escalation to a human a governed, logged, testable step — and can we prove it fired every time it should have** — the exact evidence 2 August will ask for in two days?
- The failure that costs you is the *unfinished* one, not the mis-spoken one. **Before we scale, have we defined what "resolved" means for each agent workflow and instrumented the handoff to a human** — or are we booking a polite non-answer as a closed case?

### 🧬 Healthcare / Life Sciences
- A clinical agent that gives a correct-sounding answer but fails to escalate an urgent case is a last-mile failure with a patient at the end of it. **Where is the audit trail proving the right action was taken and escalated at the right moment — and the alarm when a case is answered but not resolved?**
- Execution failures are up 62% as agents move from advising to acting. **For agents touching orders, referrals or records, have we bounded what actions they may take and required a human handoff on the consequential ones** — before an unfinished workflow becomes an incident in someone's chart?

### 🏭 Manufacturing / Industrials
- Your value is a completed job, not a well-phrased work order. **Do our agents close the loop — dispatch, confirm, escalate the exception, verify resolution — or do they generate a correct instruction and leave the last mile (did it actually get done?) to chance?**
- ChatSee: the dominant failure is now the dropped handoff, not the wrong fact. **Are we instrumenting the exception path — what happens when the agent can't complete or must hand to a technician** — or is a stalled task silently logged as success?

### 🛒 Retail / Consumer
- A storefront agent that answers beautifully but never completes the return, the refund or the escalation is the parcel marked "delivered" that never arrived. **Do we measure resolution and escalation for customer-facing agents — and disclose that a person is dealing with an AI** — with Article 50 transparency live in two days?
- The cheapest, fastest model won't save a broken last mile. **Are we investing in faster answers when the failures are at the doorstep** — the handoff, the follow-through, the resolution the customer actually experiences?

### 🏛️ Public Sector / Regulated
- For citizen services, an unescalated case is a person who asked for help and never got it, on the record. **Can we account for every agent's actions, escalations and resolutions — and the disclosure that they were dealing with an AI** — the precise accountability 2 August enforcement expects?
- BCG calls the Act a "wake-up call" and most bodies lack an AI inventory. **Are we standing up governed, auditable last-mile records (action, escalation, resolution, disclosure) before we scale,** or racing a pilot to a headline and inheriting an ungoverned final stretch we can't prove?

---

## 4 · Technical Deep-Dive — Own the Last Mile, Not Just the Answer

Read this week as one lesson about **the last mile being the layer that decides the outcome,** in three parts — the line-haul (the model's answer, now a cheap and solved commodity), the doorstep (why the failure moved from wrong words to unfinished work), and the last mile (the owned, governed handoff the audit and the customer both judge).

- **The line-haul (commodity, and effectively solved).** Producing and moving a correct answer keeps getting cheaper and faster: **Claude Opus 5** #1 at **$5/$25** (24 Jul); **Claude Sonnet 5** at **$2/$10** through 31 Aug (then $3/$15); **GPT-5.6 "Sol"** at **~750 tokens/sec** on Cerebras (10–15× typical frontier API speed); **Kimi K3** open weights (27 Jul); the **MCP 2026-07-28** connector final (28 Jul). Answering correctly is now table stakes — the thousand-mile leg that got automated, cheap and reliable. It is not where the journey is lost.
- **The doorstep (where the failure moved).** ChatSee's study of **10,000+ enterprise AI failure events** (29 Jul) inverts the risk picture as AI shifts from answering to acting. **Hallucination is under 10%** of failures. The largest family is **resolution and escalation breakdowns at 31.1%** — the parcel that arrived and was never handed over. **Execution and action failures are up 62%** on the 2024 baseline — the wrong door, the unsigned delivery, the tool call that fired incorrectly. Sarukkai's frame: the question is no longer whether the model answers correctly but whether the system can *"retrieve the right context, take the right action, escalate at the right time, and bring work to resolution."* The banking customer who reports fraud, gets a compliant reply, and is never escalated is the whole failure mode in one story — and it sits atop the standing production gap (**MIT 95% no measurable impact; IDC 88% of PoCs never scale; Gartner 40%+ cancelled by 2027**).
- **The last mile (the layer to build and own).** The fix is not a better model; it is a governed final stretch. **Instrument completion** (define "resolved" per workflow and measure it, not just "answered"). **Instrument escalation** (a policy for when a human must take the parcel, tested and logged, so the fraud report always reaches a person). **Bound execution** (what actions an agent may take, with approval on the consequential ones, so a wrong tool call can't fire unchecked). **Log and disclose** (a per-action record of what was done, escalated and resolved, plus the Article 50 disclosure that a person is dealing with an AI). The four crafts of the last mile: **complete, escalate, bound, prove.**

The strategic core: **you don't win by moving the answer faster; you win by owning the doorstep.** Everyone rents the same fast, cheap line-haul now — that's what "commodity" means. What is scarce, proprietary and auditable is the last mile: the record that a correct answer became a completed, escalated, resolved, disclosed action. After this week, "our model is the best/cheapest/fastest" is not a strategy; *"we govern and can prove the last mile — completion, escalation, bounded action, disclosure"* is.

```
        THE LAST MILE — own the doorstep, not just the line-haul
        The line-haul is cheap and solved; the last mile is where the journey is won.

   ┌─────────────────────────────────────────────────────────┐
   │  THE LINE-HAUL — the model's answer (commodity, solved)   │  ✅ RENTABLE
   │  Opus 5 #1 $5/$25 · Sol ~750 tok/s · Kimi K3 open weights  │
   │  fast, cheap, reliable — and not where the journey fails   │
   └─────────────┬─────────────────────────────────────────────┘
                 │  the answer arrives at the depot ↓
                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │  THE DOORSTEP — where the failure moved                   │  ⚠ THE REAL GAP
   │  answering is solved; ACTING is where it breaks           │
   │  ChatSee (10,000+ failures): hallucination <10%           │
   │  escalation breakdowns 31.1% · execution failures +62%    │
   │  "answered, compliant — and never escalated"              │
   └─────────────┬─────────────────────────────────────────────┘
                 │  govern the final stretch you own →
                 ▼
   ┌───────────────────────────────────────┐
   │  OWN THE LAST MILE                     │  the layer to own
   │  COMPLETE — define & measure "resolved" │  proof of delivery:
   │  ESCALATE — human handoff, tested/logged│  action, escalation,
   │  BOUND — what actions, approval gated   │  resolution, disclosure
   │  PROVE — per-action log + Art. 50        │  — your 2 Aug evidence
   └───────────────────────────────────────┘

   TRAP: buy a faster answer, ignore the doorstep → unfinished work, no audit.
   WIN : rent the line-haul, OWN the last mile → completed, escalated, proven.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — chase a faster answer | The discipline — own the last mile |
|---|---|
| Measure the model (accuracy, latency, price) | Measure the outcome (completed, escalated, resolved) |
| A polite, compliant non-answer books as success | "Resolved" is defined per workflow and verified |
| Escalation to a human is implicit and untested | Escalation is a governed, tested, logged step |
| Agents may take any action the tools allow | Actions are bounded; consequential ones need approval |
| No record of what the agent did or disclosed | Per-action log + Article 50 disclosure — your 2 Aug evidence |

### Why the last mile is a process problem, not a model problem

Every force this radar tracked all month assumed the leverage was upstream — a better model, an open weight, a universal connector, a memory layer. This week names the stretch furthest downstream: the answer is solved and cheap, and the durable asset is what happens *after* it — the delivery. The reassuring reading tempts the trap — "our model is excellent, so we're covered" — exactly backwards. The model is the interchangeable line-haul; the last mile is the proprietary, failure-prone, governable one. A firm that hears "the model is smart enough now" ships faster answers into an ungoverned doorstep; a firm that reads ChatSee's data builds and governs the delivery. The model didn't become less important; it became the *cheap* part — necessary line-haul, not the finished journey.

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine, 28 Jul the mailroom, 29 Jul the pilot plant, 30 Jul the commonplace book). Yesterday's book named the memory that compounds; today names the stretch where a good answer becomes finished work — the last mile. On legacy estates the danger is a team that bolts a brilliant, cheap model onto a system-of-record, measures it on answer quality, and never instruments completion, escalation or resolution — so the agent answers beautifully and the work quietly stalls: the fraud report acknowledged but not escalated, the return promised but not processed, the exception logged as "handled." The retrofit is the last mile: define "resolved" for each workflow and measure it, make human escalation a tested and logged step, bound what actions the agent may take and gate the consequential ones, and record every action plus the Article 50 disclosure — *before* the scale-up, not after the unfinished case becomes an incident and the fine.

**The clean mental model:** *The line-haul is rented and cheap; the last mile is owned and it decides the outcome. The model's answer has commoditized — build and own the last mile (complete, escalate, bound, prove), because that is where the value is realized and the audit will look.*

### Watch list this week
- **The failure mode inverts (ChatSee, 29 Jul).** 10,000+ enterprise AI failure events: hallucination <10%; resolution/escalation breakdowns 31.1% (largest family); execution/action failures +62% on the 2024 baseline — as AI moves from answering to acting, the risk is failed task completion. ChatSee raised $6.5M (True Ventures) to build "failure memory" for agents.
- **The answer got cheap and fast.** Claude Opus 5 #1 at $5/$25; Claude Sonnet 5 at $2/$10 through 31 Aug then $3/$15 (benchmark token spend before the cliff); GPT-5.6 "Sol" at ~750 tok/s on Cerebras (10–15× typical); Kimi K3 open weights; MCP 2026-07-28 connector final.
- **The production gap is a last-mile gap.** MIT: 95% of gen-AI pilots deliver no measurable impact. IDC: 88% of agent PoCs never reach broad production. Gartner: 40%+ agentic projects cancelled by end-2027; 40% of enterprise apps carry embedded agents by year-end (up from <5% in 2025).
- **Enterprises industrializing the last mile.** Anaplan's Agentic Enterprise (a single auditable source of enterprise truth); Cognizant's EMEA AI Unit (built around the 88% production gap); Huawei Cloud's Agentic Infrastructure (agent runtime + memory) — the market is productizing scale-up and delivery, not just models.
- **The clock — EU AI Act Article 50 + GPAI enforcement, Sunday 2 August (2 days;** €15M or 3% of turnover). Chatbot/agent disclosure, machine-readable AI-content marking and deepfake labeling become enforceable across 27 states; the Commission's GPAI enforcement powers switch on. High-risk Annex III deferred to 2 Dec 2027 (Digital Omnibus). BCG calls it a "wake-up call"; over half of firms still lack an AI inventory.

---

## 5 · Quotes That Catch the Eye

> The enterprise AI question is no longer only whether a model can answer correctly, but whether the AI system can retrieve the right context, take the right action, escalate at the right time, and bring work to resolution.
> — **Sekhar Sarukkai**, CEO & co-founder, ChatSee, on the study of 10,000+ enterprise AI failure events, 29 July 2026 (as reported)

> A banking customer can report suspicious activity, receive a polite and compliant response, and still never be escalated for human review. That is a serious enterprise failure even if the model never hallucinated.
> — **Sekhar Sarukkai**, ChatSee, on why failed task completion is the new dominant risk, 29 July 2026 (as reported)

> As enterprises move from AI systems that answer questions to AI systems that perform work, the dominant risk is shifting from incorrect content to failed task completion.
> — **ChatSee research summary**, on 10,000+ enterprise AI failure events, July 2026 (as reported)

> [The EU AI Act is] a wake-up call for leaders to assess AI readiness.
> — **BCG**, on the approaching 2 August enforcement phase (as reported)

> "The line-haul is cheap and solved; the last mile is owned, and it is where the journey is won or lost. Own the last mile."
> — *the radar, on the completion layer*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Enterprise AI failure events studied | **10,000+** | ChatSee, 29 Jul 2026 (as reported) |
| Failures that are hallucination-related | **Under 10%** | ChatSee (as reported) |
| Largest failure family — resolution/escalation breakdowns | **31.1%** | ChatSee (as reported) |
| Execution / action failures vs Q2 2024 baseline | **+62%** | ChatSee (as reported) |
| ChatSee funding round (True Ventures) | **$6.5M** | ChatSee / PR Newswire (as reported) |
| Gen-AI pilots delivering no measurable business impact | **95%** | MIT (NANDA) (as reported) |
| AI-agent PoCs that never reach broad production | **88% (33 in → 4 out)** | IDC (as reported) |
| Agentic-AI projects to be cancelled by end-2027 | **40%+** | Gartner (as reported) |
| Enterprise apps with embedded AI agents by year-end | **40% (up from <5% in 2025)** | Gartner (as reported) |
| Organizations lacking a systematic AI inventory | **Over half** | Readiness research / coverage (as reported) |
| Claude Opus 5 — launch rank / pricing | **#1 · $5 / $25 per 1M tokens** | Anthropic / Artificial Analysis (as reported) |
| Claude Sonnet 5 — pricing (cliff 31 Aug) | **$2 / $10 → $3 / $15 per 1M tokens** | Anthropic / coverage (as reported) |
| GPT-5.6 "Sol" on Cerebras — throughput | **~750 tokens/sec (10–15× typical)** | OpenAI / Cerebras / coverage (as reported) |
| Kimi K3 full open weights — live | **27 Jul 2026** | Moonshot / coverage |
| MCP 2026-07-28 final spec — live | **28 Jul 2026** | MCP blog / coverage |
| EU AI Act Article 50 + GPAI enforcement | **2 Aug 2026 (2 days) · €15M or 3%** | European Commission |
| High-risk (Annex III) obligations — deferred to | **2 Dec 2027 (Digital Omnibus)** | European Commission / coverage |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Measure the outcome, not the answer — find out where your last mile fails.** For your top agents, stop reporting model accuracy and latency alone and start measuring completion, escalation and resolution: what share of cases actually finished, how often a human handoff fired when it should have, how many "answered" tickets were never resolved. ChatSee's data (escalation breakdowns 31.1%, execution failures +62%, hallucination <10%) exists because the answer is solved and the doorstep isn't — and most firms have never looked at the doorstep.

2. **Govern the last mile — complete, escalate, bound, prove — that is your 2 August evidence.** Define what "resolved" means for each workflow and instrument it; make human escalation a tested, logged step so the fraud report always reaches a person; bound the actions an agent may take and gate the consequential ones on approval; and record every action plus the Article 50 disclosure that a person is dealing with an AI. That per-action record is exactly what Sunday's transparency-and-GPAI enforcement (€15M or 3%) asks for — and over half of firms can't produce it because they have no inventory.

3. **Own the last mile as a model-neutral asset — rent the answer, keep the delivery.** Stand up completion, escalation and audit as infrastructure you own, separate from any one model, so swapping Opus 5 for Kimi K3 for GPT-5.6 Sol changes the line-haul, not the doorstep. The answer will keep getting cheaper and faster; the durable moat — and the auditable record — is proof that your agents took the right action, escalated at the right moment, and brought the work to resolution.

---

*AI Tech Radar · generated 31 July 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The reported facts are relayed from ChatSee's 29 July 2026 research announcement and associated coverage, the European Commission's EU AI Act material and Article 50 guidance, and market reporting on models, adoption and the production gap, and are marked "as reported" where they rest on secondary reporting. The ChatSee figures (a study of more than 10,000 enterprise AI failure events finding that fewer than 10% of failures are hallucination-related, that resolution and escalation breakdowns are the largest failure family at 31.1%, and that execution and action failures are up 62% relative to the Q2 2024 baseline; CEO Sekhar Sarukkai's quotations; the $6.5M True Ventures round) are relayed from ChatSee's 29 July 2026 research release (via PR Newswire / Morningstar / citybiz and associated coverage) as reported. The MIT figure (95% of gen-AI pilots delivering no measurable business impact), the IDC figure (88% of AI-agent proofs-of-concept never reaching broad production; 33 pilots for every four in live operation) and the Gartner figures (more than 40% of agentic-AI projects cancelled by the end of 2027; 40% of enterprise applications carrying embedded AI agents by year-end, up from less than 5% in 2025) are relayed via July 2026 coverage as reported. Claude Opus 5 (24 July 2026, #1 at launch, $5/$25 per million tokens), Claude Sonnet 5 pricing ($2/$10 through 31 August 2026, then $3/$15), GPT-5.6 "Sol" throughput on Cerebras (up to ~750 tokens per second, described as 10–15× typical frontier API speeds), Kimi K3 open weights (27 July 2026) and the MCP 2026-07-28 specification (final 28 July 2026) are relayed from July 2026 coverage as reported. Anaplan's Agentic Enterprise, Cognizant's EMEA AI Unit and Huawei Cloud's Agentic Infrastructure are relayed from 2026 announcements and coverage as reported. The EU AI Act Article 50 / GPAI enforcement date (2 August 2026; the higher of €15 million or 3% of global annual turnover under Article 99; chatbot/agent disclosure, machine-readable marking of AI-generated content and deepfake labeling) and the deferral of high-risk Annex III obligations to 2 December 2027 under the Digital Omnibus are relayed from the European Commission and associated coverage; the BCG "wake-up call" characterization and the "over half of organizations lack a systematic AI inventory" readiness figure are relayed from coverage as reported. The "2 days" figure is a simple count from this edition's date (31 July 2026) to 2 August 2026 and is the radar's own. The last-mile allegory — the well-known logistics reality that the final leg of delivery, from the local depot to the customer's door, is disproportionately the most expensive and failure-prone stretch of the journey while the long-distance line-haul is comparatively cheap and reliable — is the radar's own illustration, told approximately, and is not a sourced claim about any specific carrier or study.*
