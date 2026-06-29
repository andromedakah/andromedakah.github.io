# AI Tech Radar — Structure Beats Scale
**Monday, 29 June 2026 · Cross-sector edition · Audience: C-level + Engineering**

> What changed, why it matters to the boardroom, what to ask in the room, and how it lands on legacy technology.

---

## 1 · Executive Summary — 90-second read

This week the frontier headline was *not* a bigger general model. Three moves, read together, say the value is migrating **away from raw scale** and toward the **specialized substrate** underneath it — your structured data, your power, and your access to compute.

1. **The frontier shipped behind a gate.** OpenAI previewed **GPT-5.6** (Sol / Terra / Luna) on 26 June — and the **US government requested a restricted preview, which OpenAI granted**, warning it "is not the norm." Frontier access is now something a state can throttle. Sol holds GPT-5.5's price ($5/$30 per 1M tokens); the real enterprise news is a revamped prompt cache (90%-off reads, 30-min guaranteed lifetime) to tame agentic cost curves.
2. **SAP bet €1B+ that LLMs are the wrong tool for business data.** Its acquisition of **Prior Labs** (the **TabPFN** team, pioneers of **Tabular Foundation Models**) is a bet that the data that actually runs companies — rows and columns in ERP, claims, ledgers — is best predicted by models built *for tables*, not by language models that "have only a rudimentary understanding of numbers and statistics."
3. **The ceiling is now energy, not algorithms.** The four largest clouds committed **>$710B** of AI capex for 2026; Morgan Stanley sees US data-center demand at **74 GW by 2028** against a **~49 GW shortfall**. Huang's framing: AI is **intelligence infrastructure** and "we need ~1,000× more energy." The SMR-nuclear pipeline for data centers nearly **doubled to 45 GW**.

**Bottom line:** the differentiator is shifting from *who rents the biggest model* to *who owns the right substrate* — the structured data that only you have, the power you've actually budgeted, and a multi-vendor access plan that survives a gated frontier.

---

## 2 · Allegory of the Day — "The Poet and the Actuary"

*Topic: tabular foundation models vs. LLMs for the data that runs the business.*

A firm hired a dazzling **poet**. He could speak on any subject, charm the board, and draft a beautiful memo before lunch. Everyone agreed he was the smartest hire in years. Then they handed him the **ledger** — rows of claims, prices, churn, defaults — and asked, *"what happens next quarter?"* He answered fluently, confidently… and wrong. He had never really read a table; he had only ever read *about* tables.

Down the hall sat a quiet **actuary**. She had never written a poem and never would. But she read the ledger cold — saw the distribution, weighed the tails, priced the risk — and she was *right*, again and again, because columns and probabilities were her native language.

**The moral:** for the data that actually runs your business, you don't need a bigger poet — you need a better statistician. LLMs are the poets of this era; magnificent with language, clumsy with your P&L. **SAP just paid more than a billion euros to hire the actuary.** The strategic question isn't "which model is smartest," it's *"am I paying poet prices for actuarial work?"*

---

## 3 · C-Level Engagement — Questions by Sector

**🌐 Cross-sector (any boardroom)**
- Of our AI use cases, which are **prediction-on-structured-data** problems we're currently solving with an LLM — and would a **tabular model** be more accurate *and* cheaper?
- GPT-5.6 shipped **government-gated**. Does our strategy assume continued, open access to a single frontier vendor — and what's our fallback if access is throttled?
- Is there a **power/compute line** in our AI business case, or are we assuming energy is free and infinite?

**🏦 Financial Services**
- Churn, credit, fraud, and pricing are **tabular, actuarial** problems. Are we paying LLM token prices for work a tabular foundation model does better — and with cleaner auditability?

**🧬 Healthcare / Life Sciences**
- Risk scoring and readmission prediction live in **structured EHR tables**. That's TFM territory — what's our validation gate before a tabular model touches a clinical decision? (High-risk EU rules land Dec 2027.)

**🏭 Manufacturing / Industrials**
- With a national **~49 GW power shortfall**, is our AI roadmap budgeted against an actual energy plan — or is ambition outrunning the grid?

**🛒 Retail / Consumer**
- Demand forecasting and assortment are tabular. If our moat is "we use the same frontier API as our competitor," **what exactly is the moat?**

**🏛️ Public Sector / Regulated**
- A frontier lab just complied with a government's request to restrict a launch. Does our **sovereignty plan** depend on assumptions about model access that a single policy decision could break?

---

## 4 · Technical Deep-Dive — Tabular Foundation Models vs. LLMs

The defining technical contrast of the week: **two completely different ways to predict from a table.**

**The LLM path:** serialize a table into text → tokenize → ask the model to "reason" about numbers it sees as strings. It works for tiny cases and demos, but the model has no native sense of distributions; it pattern-matches language, then guesses. Expensive per token, weak on the tails, hard to calibrate.

**The TFM path (TabPFN-style):** a model **pre-trained on millions of synthetic tabular datasets** learns the *shape* of how tables behave. At inference it does **in-context learning** — you hand it your labeled rows and the new rows, and it predicts in a **single forward pass, with no per-task training**. No feature pipeline to build, no model to retrain per use case.

```
        STRUCTURED DATA  (ERP · claims · ledger · EHR · sensor logs)
                 │                              │
                 ▼                              ▼
    ┌─────────────────────┐         ┌─────────────────────────┐
    │   LLM PATH          │         │   TFM PATH (TabPFN)      │
    │ table → text →      │         │ rows in-context →        │
    │ tokens → "reason"   │         │ one forward pass →       │
    │ → guess (eloquent)  │         │ calibrated prediction    │
    └─────────────────────┘         └─────────────────────────┘
                 │                              │
          eloquent, costly,            accurate on tabular,
          weak on numbers              no per-task training
```

**Why it matters for legacy estates.** Your most valuable, most *owned* data already lives in tables — the data warehouse, the ERP, the mainframe export, the spreadsheet that runs a department. Until now, squeezing a prediction out of it meant a **bespoke ML project per use case**: feature engineering, training, tuning, MLOps. A tabular foundation model flips that to **write-once, predict-many** — point it at a clean table and get a calibrated prediction without building a new model each time. The legacy bottleneck stays the same as with agents: **data accessibility and quality**, not the model. The clean table is the asset; the model is the easy 20%.

**Watch list:** TabPFN-style models (Prior Labs / SAP), SAP-RPT-1 and the SAP knowledge-graph + agent hub, and the broader "small specialized model beats giant general model on narrow structured tasks" pattern. Pair it with the agentic stack: agents *do*, RAG lets them *know* text, and TFMs let them *predict* over your tables.

---

## 5 · Quotes That Catch the Eye

> "The greatest untapped opportunity in enterprise AI wasn't large language models — it was AI built for the **structured data** that runs the world's businesses."
> — SAP CTO, on the Prior Labs acquisition

> "We need roughly **1,000× more energy** for AI compute." — Jensen Huang, NVIDIA CEO · AI as *intelligence infrastructure*

> "[The restricted preview] **is not the norm** for future launches." — OpenAI, after the US government requested a gated GPT-5.6 release

> "LLMs are the poets of this era — brilliant with language, clumsy with your P&L. Your ledger needs an actuary." — the radar's framing of the TFM shift

> "RAG for *knowing*, MCP for *doing*, TFMs for *predicting*." — the cleanest mental model for the 2026 enterprise stack

---

## 6 · Numbers to Quote in a Meeting

| Metric | Value | Source |
|---|---|---|
| GPT-5.6 Sol price (input / output, per 1M tok) | **$5 / $30** | OpenAI / aipricing.guru |
| GPT-5.6 Terra · Luna | **$2.50/$15 · $1/$6** | OpenAI / VentureBeat |
| GPT-5.6 cache-read discount / min lifetime | **90% off · 30 min** | OpenAI API docs |
| SAP investment in Prior Labs (TabPFN) | **>€1B over 4 yrs** | SAP News |
| 2026 hyperscaler AI capex (AMZN+MSFT+GOOG+META) | **>$710B** | Morgan Stanley |
| US data-center demand by 2028 / power shortfall | **74 GW / ~49 GW** | Morgan Stanley Research |
| Data-center SMR-nuclear pipeline (2024 → Apr 2026) | **25 → 45 GW** | IEA |
| AI initiatives delivering expected ROI | **25%** | IBM CEO Study |
| Agent deployments with negative ROI at 12 months | **22%** | Forrester 2026 |
| Median time-to-value, agent deployments | **5.1 months** | BCG / Forrester |
| Orgs with an agent running in production | **31%** | S&P Global Market Intelligence |
| EU AI Act high-risk obligations applicable | **2 Aug 2026** (~5 wks) | EU Commission |

---

## 7 · So What — Three Moves for the Next 30 Days

1. **Sort your AI portfolio by data type.** Route **prediction-on-tables** (churn, fraud, pricing, demand, risk) to **tabular models**; reserve LLMs for language and reasoning. Stop paying poet prices for actuarial work.
2. **Put energy in the business case.** The 2026 ceiling is **power, not algorithms** — every serious AI roadmap now needs a compute/energy line and a "what if we can't get the megawatts?" answer.
3. **Stress-test your frontier-access assumption.** GPT-5.6's government-gated launch proves access can be throttled overnight. Keep a **multi-vendor + open-weight fallback** so one policy decision can't stall the roadmap.

---

*AI Tech Radar · generated 29 June 2026 · sources in [sources.md](sources.md)*
