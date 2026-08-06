# 🗓️ AI Tech Radar — The Airlock

**Thursday, 6 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> Yesterday's edition ("The Dark Warehouse") ended on a wall the whole month had been building toward: you cannot govern, defend, or document an estate you cannot see, and the enterprise can see only about a third of its own AI. Today a frontier vendor shipped the first tool that answers the very next question — *once you can see what leaves for the model, can you stop the wrong thing from leaving?* On **5 August 2026 Anthropic launched Inference hooks (beta) for Claude Enterprise:** a control point that routes **every governed prompt to the organization's own AI security server for an allow-or-deny verdict before inference runs — and a denied request never reaches the model.** The server sees the conversation transcript, including **tool calls and their results,** and returns allow or deny within a configurable timeout (5 seconds by default); it can run in **shadow mode** (observe without blocking), roll out to a **percentage** of traffic, and **exclude roles.** Crucially, the verdict is **yours** — you or your DLP vendor (Netskope, Palo Alto Networks, Proofpoint, Zscaler, or an in-house server) operate the check; Anthropic merely built the socket. This is the month's thesis made concrete: **own the control layer around the commodity model.** The board's question this morning: ***the model is rented and swappable — but the checkpoint that decides what of ours ever reaches it: do we own that, on our ground, or have we left the one door our secrets leave through un-manned?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued one thing from a dozen angles: the model is becoming a commodity, so the durable advantage is the **layer you own around it** — the meter, the router, the MCP plane, the dossier, the discovery scan. Every edition described the layer; almost none of it existed as a product you could buy. **Today one piece shipped.** On **5 August 2026 Anthropic launched Inference hooks (beta) for Claude Enterprise** — the first vendor-native **control point the enterprise itself owns and operates in the path between its data and the rented model.**

**What it is, precisely.** When an employee submits a prompt on a governed surface (claude.ai chat, **Claude Code, Cowork**), Anthropic routes the **conversation transcript to your organization's own AI security server** — an HTTPS service you or your security vendor run — and **waits for an allow-or-deny verdict before inference runs. A denied request never reaches the model.** The check runs on Anthropic's servers after the request leaves the client, so it covers **every governed request uniformly with nothing installed on user devices;** it is signed (Standard Webhooks) and answered within a timeout you set (5s default). Your server sees the transcript, **tool calls and their results,** and text extracted from attachments — but **never raw file or image bytes, system prompts, or Anthropic-internal context.**

**Why it matters more than a feature note.** The month's problem was that governance of the model layer was a slide, not a switch. Snyk showed the estate is ~3× the model list and two-thirds dark; Gravitee showed **88% of organizations had an agent incident while 82% of executives felt protected** — the gap between *feeling* governed and *being* governed. Inference hooks close a slice of that gap with an actual mechanism: a **checkpoint you control** at the exact boundary where your data leaves your walls for a brain you don't own.

1. **The control point is yours, not the vendor's.** The novelty is not that Anthropic added a guard — it's that Anthropic built the socket so **your** guard stands in the path and **your** server holds the stamp. You decide allow/deny; you keep the failure policy (block or allow when your server is unreachable); you own the log. Model safety is the vendor's; **data control is now demonstrably yours.**

2. **It is inline, not after-the-fact.** Compliance and audit tools tell you what already happened. Inference hooks stop a prompt **before it reaches the model** — the difference between an inventory (yesterday's dark-warehouse discovery) and an **enforcement point.** Seeing the estate was step one; controlling the crossing is step two.

3. **It is real, and it is early — know the gaps.** It's **beta,** Claude Enterprise only; it does **not** run on Amazon Bedrock or Google Cloud; **voice is not covered;** verdicts are allow/deny only (**no redaction or rewrite**); and today's only event is the prompt — real-time **response-side** blocking is still on the roadmap, though your server already sees tool results in the transcript. A partial airlock is not a sealed hull.

**Bottom line:** the month said *own the layer around the commodity model;* today the enterprise can buy the first bolt of it. **Stand up the AI security server, put it in shadow mode this week, and make the allow/deny verdict yours** — because the model is rented and swappable, but the one door your secrets leave through should be manned by your crew, on your ground, and it should exist for every model vendor you use, not just the one that shipped the socket first.

---

## 2 · Allegory of the Day — "The Airlock"

*Topic: On 5 August 2026 Anthropic launched Inference hooks (beta) for Claude Enterprise — a control point that routes every governed prompt to the organization's own AI security server for an allow-or-deny verdict before inference runs, so that a denied request never reaches the model. The check runs on Anthropic's servers after the request leaves the client and applies uniformly with nothing installed on devices; the server sees the conversation transcript, tool calls and their results, and text extracted from attachments, but never raw file or image bytes, system prompts, or Anthropic-internal context. It is signed (Standard Webhooks), answered within a configurable timeout (5 seconds by default), and can run in shadow mode (observe without blocking), at a rollout percentage, or with role exclusions; the organization sets the failure policy (block or allow when the server is unreachable). Verdicts are allow or deny only (no rewrite/redaction); response-side enforcement is planned; it is Claude-Enterprise-only, not on Bedrock or Google Cloud, and voice is not covered. Named DLP integrations include Netskope, Palo Alto Networks, Proofpoint and Zscaler, or an in-house server. The lesson: the model is rented and swappable, but the checkpoint that decides what of yours ever reaches it should be owned and operated by you — the vendor built the socket; the enterprise must staff the door.*

Picture a great vessel — a ship of the deep or of space, it hardly matters — carrying something precious inside: a hold kept at **one atmosphere of your own pressure,** your cargo, your charts, your crew's private words. Outside the hull is a medium you do not control and cannot breathe: the open sea, the vacuum, the rented brain that lives beyond your walls. Between the two there is exactly one lawful passage, and it is not a door but a **chamber with two doors that are never open at once** — the airlock. Nothing crosses from your pressurized world to the void except by stepping into that chamber, having the inner door seal behind it, and waiting.

For years the enterprise had no airlock. Whatever an employee typed simply **left** — through an open hatch, into the vacuum, to a brain the company did not own — and the only record was a logbook the harbormaster kept *after* the crossing, useful for grief and useless for prevention. You could audit what had escaped; you could not hold it at the threshold. This is the difference between a ledger and a lock, and for a month this radar has said the ledger is not enough: **you can light the warehouse and still watch its goods walk out the open door.**

What shipped this week is the fitting for a real airlock, welded into the hull at the one place your cargo leaves for the void. A message steps into the chamber; the inner door seals; and — this is the whole of it — **your own inspector,** not the vendor's, reads what is in the chamber and calls *allow* or *deny.* On *allow,* the outer door opens and the message goes out to the brain. On *deny,* the outer door **never breaks seal;** the message is returned to your pressurized interior, and nothing of yours reaches the void. You can run the chamber with the outer lock disengaged for a while, watching what *would* pass without stopping anyone (the crew calls this shadow mode); you can open it to a fraction of traffic first; you can exempt a trusted few. And you decide what happens when the inspector is asleep — hold everyone at the inner door, or let them through unread — because it is **your** airlock, and the failure drill is yours to write.

Two truths keep the crew honest. The first: the vendor built the **socket,** not the guard. The remarkable thing is not that the shipwright added a safety hatch — it is that the shipwright cut a fitting into the hull so that **your** door, **your** lock, **your** inspector could stand in the only passage to the void, and the vendor agreed to dock its craft to your airlock rather than make you breathe its air on its terms. That is the month's thesis in iron: **own the layer around the commodity model.** The second truth is soberer: this airlock is **new, and not yet whole.** It seals the main passage but not every hatch — it does not fit the other two ships in your fleet (the ones you board through Bedrock and Google Cloud); it cannot yet inspect a sealed crate you can only see the label of (an image); it watches what comes *back in* only by reading it on the next outbound cycle, not the instant it returns; and it can bar the door but not quietly repack the cargo. A partial airlock is a real airlock and a great advance — but a captain who calls a partial airlock a sealed hull will drown on the hatch he forgot.

**The moral:** the model is the vacuum outside — vast, powerful, rented, and swappable; you will change which void you open onto more than once, and it was never yours to own. The **airlock is yours,** or it is no one's: the single chamber where your pressurized world meets the void, where your inspector holds the stamp, where *deny* means the outer door does not open. For a month the counsel was to own the layer around the model; today it becomes a concrete drill — **build the airlock, staff it with your own crew, run it in shadow first, and demand the same fitting from every vessel you rent** — because a hull with an open hatch to the vacuum is not saved by a magnificent engine, and the one door your secrets leave through is the one door you must never leave un-manned.

**The question it forces:** *When our people speak to the rented brain, is there a chamber between our pressurized world and the void — and who holds the stamp inside it, us or the vendor? If the answer is "the model provider keeps us safe," we have described their engine, not our airlock. Where is the single passage our data takes to every model we use; whose inspector calls allow or deny before it crosses; what happens when that inspector is unreachable — and have we demanded the same fitting from every vessel in the fleet, or sealed one hatch and called the hull tight?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **Do we own the checkpoint, or does the vendor?** Inference hooks put the allow/deny verdict on **your** server, at the boundary where data leaves for the model. **Is there a single control point every prompt to every model passes through — and do we hold the stamp, or have we outsourced the one decision that keeps our data ours?**
- Yesterday's data was the alarm: **88% of organizations had an agent incident while 82% of executives felt protected** (Gravitee). **Would a checkpoint we run in shadow mode this month confirm we're the exception — or show us, in live traffic, exactly what is leaving that we assumed never did?**
- The model is rented and swappable; the control layer is not. **Are we building the airlock as a standing, model-neutral capability — one we can demand from Anthropic, OpenAI, Google and any vendor — or bolting a one-off to a single product and calling the hull tight?**

### 🏦 Financial Services
- Credit, underwriting and fraud prompts carry regulated and material non-public data straight to a rented model. **Can we route every such prompt through our own DLP verdict before inference — deny the ones carrying classified material — the way Inference hooks now allow, or does that data leave un-inspected today?**
- CNIL demanded the Article 11 dossier; a checkpoint is where the log is written *and* the leak is stopped. **Do we set the failure policy to fail-closed (block when the inspector is unreachable) for the systems that touch customer money — and can we prove it?**
- The check covers chat, Claude Code and Cowork but **not** Bedrock or Google Cloud today. **On which surfaces does our sensitive traffic actually run — and where does the airlock not yet fit, so we know the open hatches before an auditor does?**

### 🧬 Healthcare / Life Sciences
- PHI and trial data are the classic "must never leave un-inspected" cargo. **For every clinician or researcher prompt to a model, is there a chamber that reads it and can deny before it crosses — and does our scanner catch PHI in free text, not just in tagged fields?**
- Inference hooks see extracted text but **not raw image bytes** — a screenshot of a record is not inspected. **How much of our sensitive content moves as images, and what is our plan for the hatch the airlock cannot yet open?**

### 🏭 Manufacturing / Industrials
- Formulas, tolerances and supplier terms are trade secrets that leak in a single careless prompt. **Do we have one authoritative checkpoint for AI traffic across engineering and the supply chain — with an owner — or many un-manned hatches on line-side tools?**
- Cheaper, better engines keep arriving (DeepSeek V4-Flash-0731 last week). **When a team swaps the model, does our airlock still govern the crossing — or does changing the void re-open the door?**

### 🛒 Retail / Consumer
- Customer PII flows through storefront and support agents at volume. **Can we deny, in real time, a prompt that would ship a customer's data to a model — and run the verdict at a latency our experience can absorb (a 5-second timeout is the default; what's ours)?**
- The market rewards provable trust. **Is "every prompt to every model passes our own allow/deny check" a claim we can make to a customer this quarter — or an aspiration with an open hatch behind it?**

### 🏛️ Public Sector / Regulated
- Citizen data carries the strictest duty and the least tolerance for silent egress. **Is there a single, owned control point where citizen data is inspected before it reaches any model — with a fail-closed policy and a per-denial record in our own log?**
- Enforcement is live and case-by-case (CNIL, 14 banks, Article 11). **Could we show a supervisor not just what our AI did, but the checkpoint that stops what it must not do — the lock, not only the ledger?**

---

## 4 · Technical Deep-Dive — Own the Checkpoint, Rent the Model

Read this week's launch as the month's thesis crossing from slide to switch. The counsel has been constant — **own and govern the layer around the commodity model** — and until now that layer was mostly conceptual. Inference hooks make one piece buildable, and the architecture splits cleanly into three parts: the **vacuum** (the commodity model, rented and swappable), the **airlock** (the control point you own), and the **hatches still open** (the honest gaps you must not paper over).

- **The vacuum — the commodity model (rented, swappable, cheaper each week).** Still a menu you rent: **Claude Opus 5** (24 Jul; #1, Intelligence Index 61 / Agentic Index 55.3, $5/$25), Google **Gemini 3.6 Flash** (21 Jul), **GPT-5.6 Sol**, **Kimi K3** open weights, and — as of **31 July** — **DeepSeek V4-Flash-0731** (MIT, open weights). This is the powerful thing you do not own and will keep changing. Its safety is the provider's craft. But safety of the engine is not control of your data, and the vacuum was never where your advantage lived.
- **The airlock — the control point you own (shipped this week).** With **Inference hooks,** a governed prompt is sent to **your** AI security server for an **allow/deny verdict before inference runs;** a denied request **never reaches the model.** It runs on Anthropic's servers after the request leaves the client, so it covers **every governed request** (claude.ai, **Claude Code, Cowork;** web, desktop, CLI) uniformly, **nothing installed on devices;** it is **signed** (Standard Webhooks) and answered within a **timeout you set** (5s default). Your server sees the **transcript, tool calls and their results,** and extracted attachment text — **never raw bytes, system prompts, or internal context.** You choose **shadow mode** (observe), a **rollout percentage,** **role exclusions,** and the **failure policy** (block or allow when your server is unreachable). Beyond DLP it can archive transcripts, meter usage, or enforce **policy engines** (model allowlists, project scoping, working-hours). The point that matters: **the verdict is yours,** on your ground — the vendor supplied the socket, you supply the guard.
- **The hatches still open — the honest gaps.** It is **beta;** **Claude Enterprise only;** **not** on **Bedrock or Google Cloud;** **voice is not covered;** verdicts are **allow/deny only** (no redaction/rewrite); **raw image/file bytes are not inspected** (a screenshot slips through); and the only event today is the **prompt** — real-time **response-side** blocking is planned, though your server already sees tool results in the next transcript. A control point that governs one vendor and one modality is a real advance and a partial hull.

The strategic core: **model safety and data control are different jobs, and only one of them can be yours.** For a month the misread has been "our model provider is safe, so our AI is governed" — which confuses the vacuum's engineering with your airlock. After this week, "the vendor keeps the model safe" is not the answer to "who controls what our data does"; ***"every prompt to every model we use passes a checkpoint we own, which can deny before the model sees it"*** is the answer — and Inference hooks are the first place you can actually build it.

```
        THE AIRLOCK — own the checkpoint, rent the model
        The model is the vacuum outside. Your data crosses through ONE chamber, and you hold the stamp.

   ┌──────────────────────────────┐        ┌──────────────────────────────┐
   │  YOUR PRESSURIZED WORLD       │        │   THE VACUUM — the model      │
   │  employees · prompts · files  │        │   Opus 5 · Gemini 3.6 Flash · │
   │  Claude Code · Cowork · chat  │        │   GPT-5.6 Sol · Kimi K3 ·     │
   │  regulated data, trade secrets│        │   DeepSeek V4 (rented, swappable)│
   └───────────────┬──────────────┘        └───────────────▲──────────────┘
                   │ prompt leaves client                   │ allow → outer door opens
                   ▼                                        │
   ┌───────────────────────────────────────────────────────┴──────────────┐
   │  THE AIRLOCK — Inference hooks (beta, 5 Aug) · YOUR server holds stamp │
   │  transcript + tool calls/results → your AI security server            │
   │  → ALLOW / DENY before inference · deny NEVER reaches the model        │
   │  signed (Standard Webhooks) · 5s default timeout · your failure policy │
   │  shadow mode (watch) · rollout % · role exclusions · your own log      │
   └───────────────────────────────────────────────────────────────────────┘

   OPEN HATCHES (know them): beta · Claude Enterprise only · NOT Bedrock/GCP ·
   no voice · allow/deny only (no redaction) · raw image bytes not read ·
   response-side blocking still on the roadmap.

   TRAP: "the model vendor keeps us safe" → the engine is theirs, the leak is yours.
   WIN : own the airlock → deny before the model sees it, on your ground, every vendor.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — rent the checkpoint with the model | The discipline — own the airlock |
|---|---|
| "Our model provider is safe, so we're governed" | Model safety is theirs; the allow/deny verdict is ours |
| Audit what already left (a ledger, after the fact) | Deny before it crosses (a lock, inline) |
| One control bolted to one product | One checkpoint, model-neutral, demanded of every vendor |
| Fail open by default when the guard is down | Choose the failure policy deliberately — fail-closed where data is regulated |
| Call a partial airlock a sealed hull | Map the open hatches (Bedrock/GCP, voice, images) before an auditor does |

### Why a checkpoint you own beats a safer model

Every control this month presumed a place to stand. Discovery (yesterday) told you what leaves; the dossier (Monday's arc) recorded what your AI did; but neither could **stop a specific prompt at the threshold.** Inference hooks add the missing verb: **deny.** And the reason it must be *yours* is that a control point owned by the model vendor moves when you swap the model — rent the checkpoint with the engine and every model change re-opens the door. Own the airlock, on your ground, with a webhook contract any vendor can implement, and the crossing stays governed whichever void you open onto. That is why the correct read of this week is not "Anthropic added DLP" but "**the enterprise can now hold the stamp** — so build the pattern, not the point solution."

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (6 Jul the meter, 7 Jul the router, 8 Jul the MCP plane, 9 Jul the mercenary army, 10 Jul the switchboard, 11 Jul the night shift, 12 Jul the recipe, 13 Jul the cobra bounty, 14 Jul the learner's permit, 15 Jul the gauge war, 16 Jul the assayer's mark, 17 Jul the standard coupling, 18 Jul the aluminum age, 19 Jul the triage tent, 20 Jul the signet ring, 21 Jul the passport, 22 Jul the harvest, 23 Jul the company town, 24 Jul the enclosure, 25 Jul the provenance, 26 Jul the extension, 27 Jul the powder magazine, 28 Jul the mailroom, 29 Jul the pilot plant, 30 Jul the commonplace book, 31 Jul the last mile, 1 Aug the tide table, 2 Aug the loose cannon, 3 Aug the customs house, 4 Aug the two windows, 5 Aug the dark warehouse). Yesterday you lit the warehouse to *see* the estate; today you fit an airlock at the one door your data leaves through, and you decide what crosses. On legacy estates the hatches are everywhere — AI bolted onto systems no one has fully mapped — so the retrofit is unglamorous and specific: **route the AI traffic through a single control point you own** (start with the surfaces Inference hooks now cover — chat, Claude Code, Cowork), **run it in shadow mode** to learn what leaves before you block anything, **set the failure policy deliberately** (fail-closed where data is regulated), and **write the contract as model-neutral** so the same airlock governs the next engine you rent. Then map the open hatches — Bedrock, Google Cloud, voice, image content — honestly, and treat them as the next fittings, not as a hull already sealed.

**The clean mental model:** *The model is the vacuum outside — powerful, rented, swappable; you'll change which void you open onto more than once. The airlock is yours: the single chamber where your data crosses to the model, where your inspector calls allow or deny, where deny means the outer door never opens. The vendor built the socket this week; the enterprise must staff the door — in shadow first, fail-closed where it counts, and for every vessel in the fleet, not just the one that shipped the fitting.*

### Watch list this week
- **The launch — Anthropic Inference hooks (beta), 5 Aug.** Governed prompt → **your AI security server** → **allow/deny before inference;** deny **never reaches the model.** Covers claude.ai, **Claude Code, Cowork** (web/desktop/CLI); signed (Standard Webhooks); **5s** default timeout; **shadow mode,** rollout %, role exclusions; your **failure policy.** Server sees transcript + **tool calls/results** + extracted text, **never raw bytes/system prompts/internal context.** Integrations named: **Netskope, Palo Alto Networks, Proofpoint, Zscaler,** or in-house.
- **The gaps — be honest.** Beta; **Claude Enterprise only; not Bedrock/GCP;** **no voice;** allow/deny only (**no redaction**); **raw image bytes not inspected;** response-side blocking **on the roadmap.**
- **The demand signal — why it shipped.** **Gartner: 40% of enterprise apps will feature task-specific AI agents by end-2026** (up from <5% in 2025); **Salesforce Agentforce ~$1.2B ARR, +205% Y/Y;** **PwC: 88% of executives plan to raise AI budgets** on agentic AI. More prompts, more surfaces, more data leaving — the airlock exists because the traffic exploded.
- **The regulatory backdrop — still live.** EU AI Act enforcement running since **2 Aug;** AI Office GPAI powers; **€15M or 3%;** **180+ orgs** signed the GPAI Code of Practice; CNIL's **4 Aug** action (14 banks, Article 11). A checkpoint is where the log is written and the leak is stopped.
- **The vacuum, for context.** Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 (MIT) — the rented, swappable engine. Own the airlock, not the vacuum.

---

## 5 · Quotes That Catch the Eye

> Anthropic sends the conversation transcript to your AI security server and waits for an allow or deny verdict; a denied request never reaches the model.
> — **Claude Platform Docs**, "Inference hooks", describing the inline control flow, 2026 (as documented)

> Claude never sees the prompt if the company's security server blocks it. The data stays inside the enterprise perimeter.
> — **On Anthropic's Inference hooks launch**, in trade coverage of the 5 August 2026 beta, 2026 (as reported)

> 40% of enterprise applications will feature task-specific AI agents by 2026, up from less than 5% in 2025.
> — **Gartner**, on the agent traffic now crossing the boundary the airlock governs (as reported)

> "The model is the vacuum outside — rented and swappable. The airlock is yours, or it is no one's: the one chamber where your data crosses to the model, and where deny means the outer door never opens."
> — *the radar, on owning the checkpoint*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Inference hooks — what a deny does | **Denied request never reaches the model** | Claude Platform Docs, "Inference hooks" (as documented) |
| Verdict flow | **Prompt → your AI security server → allow/deny before inference** | Claude Platform Docs (as documented) |
| Default verdict timeout | **5 seconds (configurable)** | Claude Platform Docs (as documented) |
| Surfaces covered | **claude.ai chat · Claude Code · Cowork (web/desktop/CLI)** | Claude Platform Docs (as documented) |
| Not covered (today) | **Bedrock · Google Cloud · voice · raw image bytes · response-side** | Claude Platform Docs (as documented) |
| Rollout controls | **Shadow mode · rollout % · role exclusions · block/allow on failure** | Claude Platform Docs (as documented) |
| Named DLP integrations | **Netskope · Palo Alto Networks · Proofpoint · Zscaler · in-house** | Unite.AI / trade coverage (as reported) |
| Enterprise apps with task-specific AI agents by 2026 | **40% (up from <5% in 2025)** | Gartner (as reported) |
| Salesforce Agentforce ARR | **~$1.2B, +205% Y/Y** | Salesforce coverage / Salesforce Ben (as reported) |
| Executives planning to raise AI budgets on agentic AI | **88%** | PwC AI Agent Survey (as reported) |
| Agent incident vs. felt protection (why you need it) | **88% had an incident · 82% feel protected** | Gravitee State of AI Agent Security 2026 (as reported) |
| EU AI Act enforcement — status | **Live since 2 Aug; 180+ signed GPAI Code; CNIL 4 Aug: 14 banks, Art. 11** | European Commission / regulatory coverage (as reported) |
| Penalty ceiling (Art. 99) / incorrect information | **€15M or 3% · €7.5M or 1.5%** | European Commission |
| The vacuum (context) | **Opus 5 · Gemini 3.6 Flash · GPT-5.6 Sol · Kimi K3 · DeepSeek V4-Flash-0731 (MIT)** | Vendor / model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Build the airlock — stand up an AI security server and put it in shadow mode this week.** Inference hooks give you a socket; the guard is yours to supply. Point it at the DLP infrastructure you already run (Netskope, Palo Alto, Proofpoint, Zscaler, or in-house), turn on **shadow mode** so it observes live traffic without blocking, and read what your people are actually sending to the model. You will learn more about your true exposure in a week of shadow-mode logs than in a quarter of policy documents — and you will have built the enforcement point, not just the inventory.

2. **Own the verdict and set the failure policy deliberately.** The decision that keeps your data yours is allow/deny, and it must sit on **your** server, not the vendor's. Decide, per surface, what happens when your inspector is unreachable — **fail-closed** (block) for systems that touch regulated data or customer money, fail-open only where availability truly outweighs egress risk — and put a per-denial record in **your own log,** not just the vendor's. Report to the board a single metric: *the share of AI traffic that passes a checkpoint we control.*

3. **Make it model-neutral and map the open hatches — don't call a partial airlock a sealed hull.** The pattern is the asset, not the product: write the checkpoint as a webhook contract you can demand from **every** model vendor, so swapping Opus 5 for Gemini or GPT-5.6 never re-opens the door. Then list the hatches this fitting does not yet close — **Bedrock and Google Cloud surfaces, voice, image content, response-side blocking** — assign each an owner and a plan, and treat them as the next fittings. Own the airlock, staff it with your crew, and demand the same from every vessel you rent — because a hull with one open hatch to the vacuum is not a sealed ship.

---

*AI Tech Radar · generated 6 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The Inference hooks details (the beta launch for Claude Enterprise on 5 August 2026; that a governed prompt is routed to the organization's own AI security server for an allow-or-deny verdict before inference runs, with a denied request never reaching the model; that the check runs on Anthropic's servers after the request leaves the client and applies uniformly with nothing installed on devices; that it is signed per the Standard Webhooks specification and answered within a configurable timeout defaulting to 5 seconds; that the server receives the conversation transcript, tool calls and their results, and text extracted from attachments, but never raw file or image bytes, system prompts, or Anthropic-internal context; that it supports shadow mode, a rollout percentage, role exclusions, and an organization-set failure policy of block or allow when the server is unreachable; that it covers claude.ai chat, Claude Code and Cowork across web, desktop and CLI, but is Claude-Enterprise-only, is not available on Amazon Bedrock or Google Cloud, does not cover voice, offers allow/deny verdicts only with no redaction or rewrite, and that response-side enforcement is planned as a later event) are drawn from the Claude Platform Docs "Inference hooks" page as documented, with the launch date and named DLP integrations (Netskope, Palo Alto Networks, Proofpoint, Zscaler, or an in-house server) relayed from 5 August 2026 trade coverage in Unite.AI, The Next Web and vendor blogs as reported. The market figures (Gartner's projection that 40% of enterprise applications will feature task-specific AI agents by 2026, up from less than 5% in 2025; Salesforce Agentforce annual recurring revenue of roughly $1.2 billion, up about 205% year over year; and PwC's finding that 88% of surveyed executives plan to increase AI budgets because of agentic AI) are relayed from Gartner, Salesforce and PwC coverage as reported. The Gravitee figures (88% of organizations had a confirmed or suspected AI-agent security incident in the past year while 82% of executives feel their policies protect them) are carried forward from the 5 August edition as reported. The EU AI Act facts (enforcement live from 2 August 2026; the AI Office's GPAI powers; the penalty ceiling of the higher of €15 million or 3% of worldwide annual turnover under Article 99, and €7.5 million or 1.5% for incorrect information; that more than 180 organizations signed the GPAI Code of Practice; and CNIL's 4 August information requests to 14 financial institutions demanding Article 11 documentation) are relayed from the European Commission and August 2026 regulatory coverage as reported; the CNIL specifics rest on secondary coverage. The model details (Claude Opus 5, released 24 July 2026, ranked first with an Intelligence Index of 61 and Agentic Index of 55.3 at $5/$25; Google Gemini 3.6 Flash, released 21 July 2026; GPT-5.6 Sol; Kimi K3 open weights; and DeepSeek V4-Flash-0731, released 31 July 2026 under an MIT license) are relayed from model-tracker and vendor coverage as reported. The airlock allegory — a pressurized vessel whose cargo crosses to the vacuum only through a two-door chamber where the ship's own inspector calls allow or deny — is the radar's own illustration and is not a sourced claim about any specific company.*
