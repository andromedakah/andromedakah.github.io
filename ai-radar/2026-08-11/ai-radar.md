# 🗓️ AI Tech Radar — The Signet Ring

**Tuesday, 11 August 2026 · Cross-sector edition · Audience: C-level + Engineering**

> For a month this radar has said one thing in a dozen costumes: the model is a commodity, so own the layer around it. This week fitted the controls for that layer — the airlock on egress (6 Aug), the keyring on access (7 Aug), the proving ground before go-live (8 Aug), the waterworks on the economics (9 Aug) — and yesterday the loading dock, as agents began going out onto the open web (10 Aug). Today the question sharpens from *which doors an agent may open* to ***whose name it acts in.*** On **30 July, Google gave Gemini Spark the run of your real Chrome — your logged-in accounts and your saved passwords — to run errands on your behalf,** now rolling out on desktop in the US. The tell is not the feature; it is the shortcut. The fastest way to let an agent act in the world is to hand it *your own identity* — your sessions, your credentials, your signet — and let every deed it does read, in the ledger, as a deed done by *you.* The board's question this morning: ***when our agents act on our behalf, do they press their own seal — a distinct, scoped, logged, revocable identity we issued them — or do we hand them the master's signet ring, so that nothing they sign can ever be told apart from what we signed ourselves?***

---

## 1 · Executive Summary (90-second read)

For a month this radar has argued the model is a commodity, so the durable advantage is the **layer you own around it.** This week made that concrete: the airlock at the door your data leaves through (6 Aug), the keyring to the rooms your agents may enter (7 Aug), the proving ground where you validate them before go-live (8 Aug), the waterworks that meter the flow (9 Aug), and yesterday the loading dock, as agents crossed from answering to acting on the open web (10 Aug). Today the story turns from *access* to **identity:** not which doors an agent may open, but **whose authority it acts under — and whether your ledger can tell the agent's deeds from your own.**

**The datable signal.** On **30 July 2026, Google gave Gemini Spark the ability to drive your real desktop Chrome** — using the accounts you are already signed into and the passwords saved in Chrome's password manager — to complete web errands on your behalf, now rolling out in the US. Google's own documentation is candid about what this means: run through your local Chrome, the agent "has access to all the same sites that you do, including sites you are signed into." It is the most convenient possible way to let an agent act — and the most dangerous, because the agent is no longer acting *as itself.* **It is acting as you.** Every session it borrows, every form it submits, every password it uses is stamped with *your* identity, and no audit log downstream can separate what the agent did from what you did.

**Why it matters more than one product feature.** The enterprise is discovering the same fork at scale, and racing to take the other road. On **28 July, at Black Hat 2026, Snowflake launched its Cortex AI Gateway** — built on its acquisition of **Natoma,** whose centralized MCP gateway "enforces identity, policy, and audit at the tool-call level" — governing how first-party and third-party agents (Claude Code, Cursor, Bedrock, Azure AI Foundry, ChatGPT, LangChain, LlamaIndex) access data, tools and models, and shipping with **seven identity partners** (1Password, Aembit, Cyera, Linx Security, Okta, SailPoint, Saviynt). The whole design premise is the opposite of the consumer shortcut: **give each agent its own identity, scoped and logged, so every deed is attributable to the agent that did it** — never fold the agent into a human's credentials. The gap this closes is already gaping: reportedly only **19% of organizations** classify an AI agent as equivalent to a human insider, yet **80%** have already seen agents act beyond their intended scope.

1. **The most convenient identity for an agent is your own — which is exactly why it is the trap.** Gemini Spark driving your Chrome with your saved passwords is the seductive shortcut: no provisioning, no scoping, instant reach. But an agent wearing your identity is an agent whose every action is indistinguishable from yours — you have handed it your signet ring, and the wax it presses is your wax. Convenience is the whole danger.

2. **Attribution is the property you cannot buy back later.** The hardest agent problem in the field is telling *which actions were the agent versus the user.* Solve it at issuance — strike each agent its own seal — or you never solve it: once the agent has acted in your name, no forensic tool can un-mix the two. A cleverer model does nothing for this; a distinct, scoped, revocable identity does everything.

3. **The engine keeps commoditizing under all of it.** Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 (MIT), and Alibaba's open-weight Qwen3.8-Max make the brain cheaper and more interchangeable by the week. The durable advantage is not which brain you rent but the **signet office** — the identity, scope, log and revocation — you build around it.

**Bottom line:** the month's thesis said *own the layer around the commodity model.* Today that layer grows a new wall — the one between *your* identity and your *agents'.* Google poured a frictionless path that runs your agents on your own credentials; Snowflake and a rank of identity vendors poured the opposite — a control plane that issues each agent its own seal and logs every deed at the tool call. **Rent the brain; own the signet office** — the place where every agent gets its own stamp, scoped and revocable, and every act is written to the agent that did it — because a business that hands its fleet the master's ring has not deployed AI, it has signed a blank cheque in its own hand and called it delegation.

---

## 2 · Allegory of the Day — "The Signet Ring"

*Topic: On 30 July 2026, Google gave Gemini Spark the ability to operate a user's real desktop Chrome — using the accounts they are already signed into and the passwords saved in Chrome's password manager — to run web errands on their behalf, now rolling out in the US; Google's documentation notes that in local mode the agent has access to all the same sites the user does, including those they are signed into, while sensitive steps such as payments are handed back and the agent is meant to resist prompt injection. It lands against the enterprise moving the opposite way: on 28 July, at Black Hat 2026, Snowflake launched its Cortex AI Gateway, built on its acquisition of Natoma — a centralized MCP gateway that enforces identity, policy and audit at the tool-call level — with seven identity partners (1Password, Aembit, Cyera, Linx Security, Okta, SailPoint, Saviynt), the design premise being that each agent should carry its own scoped, logged identity rather than borrow a human's. Reported surveys put only ~19% of organizations classifying an AI agent as equivalent to a human insider, ~44% expecting malicious use of agents to raise data-theft risk, and ~80% already seeing agents act beyond intended scope. The lesson: as agents act on our behalf, the dangerous shortcut is to lend them our own identity; the discipline is to strike each agent its own seal — scoped, logged and revocable. The signet-ring allegory — a great house that hands its errand-runners the master's own ring until it learns to strike each one its own seal — is the radar's own illustration.*

Picture a great house in an age before signatures, when a man's authority travelled in a **ring.** The master's signet — a carved stone that pressed his mark into hot wax — was not jewellery; it *was* the master, in every place he could not stand himself. A letter sealed with it was his word. A contract stamped with it was his bond. A door opened to it because the porter knew that wax as surely as the master's face. For a hundred years the ring lived on one hand, and left it only for the steward's, because the whole house understood the terrible simplicity of the thing: **whoever holds the signet is the master, for as long as he holds it, in every matter the wax can seal.**

Then the house changed its business and hired a thousand **errand-runners** — tireless, quick, sent out a hundred a day to fetch and settle and sign on the master's behalf. And here the house met a fork it did not know it was at. The runners needed authority to act; the master could not walk beside each one. The *fast* way — the way that needed no thought and no waiting — was to press the master's own ring into each runner's hand as it went out the door. And oh, it worked: the runner reached every counting-house that honoured the master, opened every door that knew his wax, closed every deal in his name before nightfall. It was the most convenient thing in the world. It was also the moment the house lost the one thing a great house cannot lose: **the power to say who did what.** For now the daybook filled with deeds sealed by the master's mark that the master never made — and when one runner was turned, or bribed, or simply mistaken, and pressed that ring on a ruinous bargain, the ledger said only, in the master's own wax, *the master agreed.* There was no line to trace, no seal to melt but the master's own, no way to call back one runner's authority without unmaking the master's own name. The house had a thousand hands wearing its one face, and could no longer tell its face from its hands.

So the wise houses did the older, slower, unglamorous thing. They built a **signet office** — a plain room with a stern clerk and a rack of blank rings — and they made a law: *no runner ever carries the master's ring; every runner is struck its own.* The runner presents itself at the office; the clerk cuts it a seal of its own — a distinct mark, no other runner's, carved for the errands it is trusted with and no more; stamps it with an hour it expires; writes in the daybook which runner holds which seal; and hands it out. Now every deed in the ledger bears the mark of the hand that made it. The counting-house that takes a runner's seal knows it is *that runner,* acting in the master's house but under its own name, for the narrow business it was struck to do — and if the runner strays, or is turned, the clerk melts *that one seal* in a heartbeat, and the master's ring never leaves the master's hand, and every other runner keeps working. This month a great firm of the north (call it the house of snow) opened exactly such an office for the whole agentic trade, and stood a rank of locksmiths behind the clerk; and a great firm of the search (call it the house that indexes the world) offered the other road — press the master's own ring into the runner's hand and let it out the door. **The point is not which firm built which; it is that every house now stands at the fork, and one road cannot be walked back.**

Here is the turn the wise house sees and the proud one misses. The runners themselves are **rented** — their tireless wits come from the great foundries, and grow cheaper and more alike by the week — so no house wins by hiring a cleverer runner; a clever runner wearing the master's ring is only a faster way to lose the ledger. Renting the runner is the sense. But precisely *because* the runner is rented and swappable, the **signet office is the part that is yours** — the one place where you decide what authority each runner carries, in whose name, for how long, and where every seal it presses is written back to the hand that made it. The proud house hands out the master's ring at the door because it is quick, and buys the daybook a thousand deeds it cannot account for. The wise house makes each runner earn its own small seal, and keeps a ledger it could set before any magistrate: *this deed, this runner, this hour, this errand.*

**The moral:** when your traffic turns from a master who acts to a fleet that acts *for* him, the ring on one hand becomes a thousand hands wearing one face — and a house that cannot tell its face from its hands cannot be governed at all. Do not lend the runner your ring because it is fast. Build the signet office and make it yours: a seal struck for each runner, scoped to its errand, stamped with its hour, written in the daybook, and meltable alone. Rent the runner; **own the signet office** — because in the season the machines began signing in your name, the danger was never that they were clever; it was that you could no longer tell their wax from your own.

**The question it forces:** *Our agents have started acting on our behalf — signing, submitting, transacting in our name. Do they each press their own seal — a distinct, scoped, logged, revocable identity we issued and can melt alone — or have we handed them the master's ring for convenience, so that nothing our machines do can ever be told apart from what we did ourselves?*

---

## 3 · C-Level Engagement — Questions by Sector

### 🌐 Cross-sector (any boardroom)
- **When one of our agents acts, whose identity does the log record — the agent's, or a person's?** The hardest agent problem in the field is telling which actions were the agent versus the user. **Does every agent carry its own scoped, logged identity, or are our agents borrowing human credentials and sessions so that nothing they do can be attributed to them?**
- The brain keeps commoditizing (Opus 5, Gemini 3.6 Flash, Qwen3.8-Max at frontier parity). **Are we still shopping for the cleverest runner — or building the signet office: the identity, scope, log and revocation that make any rented runner safe to send out in our name?**
- **If one agent were compromised tomorrow, could we revoke it alone — in seconds — without disrupting a single human or a single other agent?** If revoking the agent means rotating a person's password, the agent was never a first-class identity.

### 🏦 Financial Services
- Agents that pull filings, check balances or move money are signing in the institution's name. **Does each one act under its own scoped identity with an audit trail a regulator could read line by line — or are they inheriting an employee's access, so a compromised agent is indistinguishable from a compromised banker?**
- Delegated authority is the oldest control you have. **Is every agent's reach bound to the narrow business it was issued for (least privilege by identity), or have we handed the fleet broad, human-shaped credentials because it was faster to ship?**

### 🧬 Healthcare / Life Sciences
- Clinical and research agents touch PHI at machine speed. **Can we prove, per action, which agent accessed which record and why — or would the log simply show a clinician's identity that a clinician never used?**
- A stolen or over-scoped agent seal is a breach that wears a caregiver's face. **Do we issue agents their own revocable identities, so we can cut off one agent instantly — or would containing an incident mean locking out the people it impersonated?**

### 🏭 Manufacturing / Industrials
- Procurement and supply-chain agents sign orders and settle accounts with suppliers. **Does each agent transact under its own identity, scoped and logged, or under a buyer's login — so the ledger can tell an agent's purchase order from a human's?**
- Non-human identities already outnumber humans across the estate. **Are our agents governed as first-class identities with their own lifecycle (issue, scope, expire, revoke) — or bolted onto human accounts we can neither scope tightly nor revoke cleanly?**

### 🛒 Retail / Consumer
- Pricing, catalog and support agents act at the highest volume in the business. **At peak, is every agent acting under its own attributable identity — or as a shared service account no incident responder could ever pin an action to?**
- The convenient path is the consumer one: let the agent use a human's saved logins. **Would we know if an agent, fed a forged instruction, transacted in a customer's or employee's name — and could we revoke just that agent without locking the person out?**

### 🏛️ Public Sector / Regulated
- Citizen-service agents that file and decide must be accountable by name. **Does every agent act under its own identity with a daybook we could defend to an auditor — or are we standing up services whose agents act in a civil servant's name, with no clean line between the two?**
- Accountability lives at issuance. **Do we control the office that strikes each agent's seal — its scope, its expiry, its revocation, its log — or have we let agents inherit staff credentials because no one owned agent identity?**

---

## 4 · Technical Deep-Dive — Rent the Brain, Own the Signet Office

Read this month as one argument adding one wall at a time. The airlock (6 Aug) governs **egress** of prompts; the keyring (7 Aug) governs **access** to tools — *which rooms* an agent may enter; the proving ground (8 Aug) governs **pre-production validation;** the waterworks (9 Aug) governs the **economics;** the loading dock (10 Aug) governs the agent's **reach onto the open web.** Today's brick governs a distinct surface the keyring only half-touched: **identity and attribution — not which doors an agent may open, but *whose name it acts under,* and whether your ledger can tell the agent's deeds from a human's.** The architecture splits into three: the **runner** (the rented, swappable model), the **signet** (the identity each agent acts under — yours to issue), and the **ledger** (the attribution trail that only survives if the signet is distinct).

- **The runner — the commodity brain (rented, swappable).** The menu is cheaper and more crowded by the week — **Claude Opus 5**, **Gemini 3.6 Flash**, **GPT-5.6 Sol**, **Kimi K3**, **DeepSeek V4-Flash-0731** (MIT), and **Alibaba Qwen3.8-Max** (open weights, frontier-parity claim). Renting the runner is the sense. But a cleverer runner wearing your identity is just a faster way to fill your ledger with deeds you cannot account for — only a distinct seal fixes that.
- **The signet — the identity you issue (where the new advantage sits).** This is the part you own or fail to own. The consumer shortcut shows the trap in its purest form: **Gemini Spark** (30 Jul) can drive your *real* Chrome using the accounts you are signed into and the passwords in Chrome's manager — Google's own docs note the local-mode agent "has access to all the same sites that you do, including sites you are signed into." Convenient, and identity-blind: the agent acts *as you.* The enterprise answer runs the other way. **Snowflake's Cortex AI Gateway** (28 Jul, Black Hat 2026), built on its **Natoma** acquisition, is a centralized MCP gateway that "enforces identity, policy, and audit **at the tool-call level,**" governing first- and third-party agents (Claude Code, Cursor, Bedrock, Azure AI Foundry, ChatGPT, LangChain, LlamaIndex) and shipping with **seven identity partners** (1Password, Aembit, Cyera, Linx Security, Okta, SailPoint, Saviynt). A real signet office does four things: **scope** (a seal cut for the narrow errand, least privilege by identity), **stamp** (a distinct mark, never a human's credentials), **log** (every deed written back to the agent that did it), and **revoke** (melt one seal in a heartbeat without touching any human or any other agent).
- **The ledger you must be able to defend — attribution.** The hardest problem in the field is telling *which actions were the agent versus the user.* It is not a downstream analytics task; it is decided at issuance. Fold an agent into a human's identity and the answer is lost before the first action — no SIEM, no forensic tool can un-mix wax pressed by the same ring. Strike the agent its own seal and every line of the ledger names the hand that made it.

The strategic core: **the brain is the runner; the signet office is where you decide in whose name your agents act, and keep a ledger you can defend.** For a month the misread has been "buy the cleverest model and you have deployed AI." After this week the read is sharper: **the model is rented and getting cheaper, and the risk and the control have moved to identity — the seal each agent carries and the trail it leaves.** "We use the best model" is not the answer to "when an agent acted in our name, can we prove it was the agent, and revoke just that agent"; ***"every agent carries its own scoped, logged, revocable seal, and every deed names the hand that made it"*** is the answer.

```
        THE SIGNET RING — rent the runner, own the identity you issue
        Agents act ON YOUR BEHALF — the question turns from access to IDENTITY.
        Gemini Spark (30 Jul): drive YOUR Chrome, YOUR logins, YOUR saved passwords.

   ┌──────────────────────────────┐            ┌──────────────────────────────┐
   │  THE RUNNER — rented brain    │            │  THE LEDGER — attribution     │
   │  Opus 5 · Gemini 3.6 Flash ·  │            │  who did what, provable       │
   │  GPT-5.6 Sol · Kimi K3 ·      │            │  by the seal on each deed     │
   │  DeepSeek V4-Flash · Qwen3.8- │            │  decided at ISSUANCE, not     │
   │  Max (open, frontier parity)  │            │  reconstructed after the fact │
   │  cheaper every week · not the moat         └───────────────▲──────────────┘
   └───────────────┬──────────────┘                            │ every deed named
                   │ acts under                                 │ to the hand that made it
                   ▼                                            │
   ┌───────────────────────────────────────────────────────────┴──────────────┐
   │  THE SIGNET OFFICE — the identity you ISSUE and OWN                        │
   │  → SCOPE : a seal cut for the errand — least privilege by identity         │
   │  → STAMP : the agent's OWN mark — never a human's credentials/sessions     │
   │  → LOG   : every deed written back to the agent that did it (tool-call lvl)│
   │  → REVOKE: melt one seal in a heartbeat — no human, no other agent touched │
   │  Snowflake Cortex AI Gateway + Natoma · 7 identity partners · MCP tool-call│
   └───────────────────────────────────────────────────────────────────────────┘

   THE CONTROLS, STACKED: airlock (egress, 6 Aug) · keyring (access, 7 Aug) ·
   proving ground (pre-prod, 8 Aug) · waterworks (economics, 9 Aug) ·
   loading dock (web, 10 Aug) · signet (identity, today).

   TRAP: hand the runner the master's ring → its deeds read as YOURS → ledger lost.
   WIN : strike each runner its own seal → scoped, logged, revocable → ledger holds.
```

*(An inline SVG version of this diagram ships in the web edition.)*

### The trap vs. the discipline

| The trap — lend the master's ring | The discipline — strike each agent its own seal |
|---|---|
| Agents borrow human logins, sessions and saved passwords | Each agent carries its own distinct, issued identity |
| An agent's deeds are indistinguishable from a person's | Every deed is attributable to the agent that did it |
| Broad, human-shaped access because it shipped faster | Least privilege by identity — a seal cut for the errand |
| Revoking an agent means rotating a human's credentials | Melt one seal alone — no human, no other agent disturbed |
| Attribution reconstructed (and lost) after an incident | Attribution decided at issuance and logged at the tool call |

### Why owning the signet office beats owning a cleverer brain

Every control this month presumed you could name and stop the actor. Identity is where that becomes possible — or impossible. A cleverer model cannot tell your ledger who acted; a distinct, scoped seal can. And the reason the signet, the keyring and the airlock belong together is structural: an agent acting in your name is an **identity** (the signet's concern), a **holder of scoped access** (the keyring's concern) and an **egress path** (the airlock's concern) at once — the same session that quietly exfiltrates a secret is the one whose deed, if it wears your identity, your ledger will attribute to *you.* Route every agent through one office that issues its seal, scopes it, logs it and can revoke it, and those controls become one accountable record. The correct read of this week is not "Google shipped a browsing feature" but "**identity just became the agent control surface** — so issue it, don't lend it."

### How it lands on legacy estates

Same seam this radar keeps returning to — **own and govern what doesn't commoditize** (airlock, keyring, proving ground, waterworks, loading dock, and now the signet). On legacy estates the temptation is the Gemini-Spark shortcut at enterprise scale: let each team point its agents at a service account, a shared login, a human's session — whatever ships this sprint. The retrofit is specific and unglamorous: **inventory every agent and the identity it currently acts under** (you will find far too many riding human or shared credentials); **issue each agent its own first-class identity** — a non-human identity with a real lifecycle (provision, scope, expire, revoke), through a gateway that enforces identity and audit at the tool-call level (Cortex/Natoma-style, or your own); **scope by least privilege** so a seal is cut for the errand, not the org; **log every action back to the agent** so the ledger names the hand; and **wire revocation you can pull on one agent alone.** Then be honest about the brain: Qwen3.8-Max and a cheaper DeepSeek prove again that the runner is a rented commodity — a bigger brain is not an identity strategy, and "we use the best model" is not an answer to "can we prove which agent acted in our name."

**The clean mental model:** *The model is the runner — rented, swappable, cheaper and more interchangeable every quarter, and never your moat. The signet office is yours to own: the place where each agent is struck its own seal, scoped to its errand, stamped with its own mark, written to the daybook and revocable alone. Agents crossed from acting on the web to acting in your name this quarter — so rent the runner and issue the seal, or hand out the master's ring for convenience and sign a blank cheque in your own hand.*

### Watch list this week
- **The trap, in the open — an agent wearing your identity.** **Google Gemini Spark** (30 Jul): drives your real desktop Chrome using your signed-in accounts and saved passwords to run errands on your behalf (US rollout; sensitive steps like payments handed back; meant to resist prompt injection). The tell: the fastest way to let an agent act is to lend it your own identity — and that is exactly the wall to build.
- **The discipline, at scale — issue the seal, log the deed.** **Snowflake Cortex AI Gateway** (28 Jul, Black Hat 2026), on the **Natoma** acquisition: a centralized MCP gateway enforcing identity, policy and audit **at the tool-call level,** governing first- and third-party agents, with **seven identity partners** (1Password, Aembit, Cyera, Linx Security, Okta, SailPoint, Saviynt).
- **The gap it closes.** Reported surveys: only **~19%** of organizations classify an AI agent as equivalent to a human insider; **~44%** expect malicious use of agents to raise data-theft risk; **~80%** have already seen agents act beyond intended scope. OWASP's Top 10 for Agentic Applications names identity and privilege abuse a core risk.
- **The runner — commoditization, again.** Opus 5, Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 (MIT), and **Alibaba Qwen3.8-Max** (open weights, frontier-parity claim) — the rented, swappable brain. Own the seal, not the runner.
- **The buyer — enterprise AI is real money.** **Microsoft FY26 Q4** (29 Jul): **Microsoft 365 Copilot past 30M paid seats,** Azure **+43% YoY** and past **$100B annualized.** Satya Nadella: turning "tokens into business results."
- **The regulatory backdrop — still live.** **EU AI Act** enforcement running since **2 Aug:** GPAI oversight, transparency duties, fines up to **€15M or 3%** of worldwide turnover — and an agent that cannot prove its identity or produce an audit trail of its access is, by design, hard to defend.

---

## 5 · Quotes That Catch the Eye

> Agent interoperability only works when enterprises can trust how agents from different platforms access data, invoke tools and take action on behalf of users. The future of the agentic enterprise will not be built in closed agent ecosystems — Snowflake is the trusted control plane that enables secure enterprise work.
> — **Mayank Upadhyay, Chief Security and Trust Officer, Snowflake**, on the Cortex AI Gateway launch (as reported)

> With auto browse in local Chrome, Spark has access to all the same sites that you do, including sites you are signed into.
> — **Google**, from its Gemini Spark documentation on the Chrome browsing feature (as reported)

> We are advancing the frontier on the cost-to-outcome curve, ensuring every customer can turn tokens into business results.
> — **Satya Nadella, Chairman & CEO, Microsoft**, on FY26 Q4 results (as reported)

> "The model is the runner — rented, swappable, cheaper every quarter, never your moat. The signet office is yours: strike each agent its own seal — scoped, logged, revocable — because agents crossed from acting on the web to acting in your name this quarter, and identity just became the control surface."
> — *the radar, on agents that act on your behalf*

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| Google Gemini Spark | **Drives your real Chrome — your logins & saved passwords — to run errands (30 Jul 2026)** | Engadget / Digital Trends / 9to5Google (as reported) |
| Snowflake Cortex AI Gateway | **MCP gateway enforcing identity, policy & audit at the tool-call level (28 Jul, Black Hat 2026)** | SiliconANGLE / VentureBeat (as reported) |
| Cortex AI Gateway — identity partners | **7 (1Password, Aembit, Cyera, Linx, Okta, SailPoint, Saviynt)** | Snowflake / press coverage (as reported) |
| Natoma (acquired by Snowflake) | **27-person startup; centralized MCP gateway, tool-call-level identity/policy/audit** | VentureBeat / Forkast (as reported) |
| Agents classed as human-equivalent insiders | **~19% of organizations** | AI agent identity surveys (as reported) |
| Orgs seeing agents act beyond intended scope | **~80%** | Non-human identity / agent security reporting (as reported) |
| Orgs expecting agent misuse to raise data-theft risk | **~44%** | AI agent identity surveys (as reported) |
| Microsoft 365 Copilot | **>30 million paid seats; Azure +43% YoY, >$100B annualized** | Microsoft FY26 Q4 (29 Jul 2026) |
| EU AI Act — penalties | **Up to €15M or 3% of worldwide annual turnover** | European Commission (as reported) |
| The engine (context) | **Opus 5 · Gemini 3.6 Flash · GPT-5.6 Sol · Kimi K3 · DeepSeek V4-Flash · Qwen3.8-Max** | Vendor / model-tracker coverage (as reported) |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Inventory which identity each of your agents acts under.** You cannot govern in whose name an agent signs if you have not looked. Map, per agent and per team, whether it acts under its own issued identity or borrows a human's or a shared service account — logins, saved credentials, live sessions, standing tokens. Report one number to the board: *how many of our agents act on human or shared identities today, so that their actions cannot be attributed to the agent.* The uncomfortable size of that number is the case for a signet office, made cheaply, before an incident makes it for you.

2. **Issue every agent its own scoped, revocable seal — never lend it a human's.** Stand up (or adopt) an agent-identity gateway — one that enforces identity, policy and audit at the tool-call level (Cortex/Natoma-style, or your own) — and give each agent a first-class non-human identity with a real lifecycle: **scope** it to the narrow errand (least privilege), **stamp** it distinctly, **log** every action back to the agent, and wire **revocation you can pull on one agent alone.** Treat the convenient path — pointing an agent at your own Chrome, your own logins, your own saved passwords — as the anti-pattern it is: fast today, unaccountable forever.

3. **Stack the controls, and keep the brain swappable.** The signet is one wall of a set — wire it to the same control points you fitted this month so one dashboard shows, per agent, *who it is* (signet), *what rooms it may enter* (keyring), *what leaves* (airlock), *what it did in pre-prod* (proving ground), *what it costs* (waterworks) and *what it touched on the web* (the dock). Then demand the same of every vendor and every model you rent — and re-benchmark the runner freely as Qwen3.8-Max, a cheaper DeepSeek and the next open-weight release reset the price, because the brain is a commodity and the identity you issue is the moat: rent the runner, own the seal.

---

*AI Tech Radar · generated 11 August 2026. All figures carry a source link in [sources.md](sources.md). Editorial framing lines are marked as the radar's own. The Google Gemini Spark details (that on 30 July 2026 Google enabled Gemini Spark to operate a user's real desktop Chrome, using the accounts they are signed into and the passwords saved in Chrome's password manager, to run web errands on their behalf, rolling out in the US, with sensitive steps such as payments handed back and the agent meant to resist prompt injection, and Google's documentation noting that in local mode the agent has access to all the same sites the user does, including those they are signed into) are relayed from Engadget, Digital Trends, 9to5Google, Dataconomy and Notebookcheck coverage as reported. The Snowflake details (that on 28 July 2026, around Black Hat 2026, Snowflake launched its Cortex AI Gateway, built on its acquisition of Natoma — a 27-person startup whose centralized MCP gateway enforces identity, policy and audit at the tool-call level — governing first- and third-party agents and shipping with seven identity partners: 1Password, Aembit, Cyera, Linx Security, Okta, SailPoint and Saviynt) are relayed from SiliconANGLE, VentureBeat, Forkast and Snowflake's own materials as reported, and the Mayank Upadhyay quotation is relayed from that coverage. The survey figures (that roughly 19% of organizations classify an AI agent as equivalent to a human insider, roughly 44% expect malicious use of agents to increase data-theft risk, and roughly 80% have already seen agents act beyond their intended scope) are relayed from AI-agent-identity and non-human-identity survey coverage as reported and are approximate. The Microsoft figures (that Microsoft 365 Copilot has passed 30 million paid seats and that Azure grew 43% year over year and passed $100 billion in annualized revenue in fiscal fourth-quarter 2026 results reported 29 July 2026) and the Satya Nadella quotation are relayed from Microsoft's FY26 Q4 disclosures and press coverage as reported. The EU AI Act enforcement facts (that GPAI oversight and transparency obligations have been enforced since 2 August 2026, with penalties up to the higher of €15 million or 3% of worldwide annual turnover) are relayed from the European Commission and secondary coverage as reported. The model details (Claude Opus 5, Google Gemini 3.6 Flash, GPT-5.6 Sol, Kimi K3, DeepSeek V4-Flash-0731 and Alibaba Qwen3.8-Max) are relayed from model-tracker and vendor coverage as reported and are carried as standing context. The signet-ring allegory — a great house that hands its errand-runners the master's own ring until it learns to strike each one its own seal — is the radar's own illustration and is not a sourced claim about any specific company.*
