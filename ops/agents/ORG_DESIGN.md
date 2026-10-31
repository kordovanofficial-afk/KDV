# Kordovan — Organisation Design (agent workforce)

Owner: Chief People Officer (`.claude/agents/chro.md`). Approved by: Founder.
Status: **DRAFT v1 (Oct 31 2026), pending the Founder's interview of the CHRO.**

## 1. Org chart

```
FOUNDER & CHAIRMAN (human, Islamabad): capital, final approval, every hire, every live change
│
├── CHIEF QUALITY & RISK OFFICER (CQRO): independent checker, dotted line to Founder
│
└── CEO (Claude): runs the company, sets weekly priorities, writes the morning brief
    │
    ├── CHIEF PEOPLE OFFICER (CHRO): org design, hiring, onboarding, performance
    │
    ├── CHIEF REVENUE OFFICER (CRO): every rupee that comes in online
    │     └─ later: Performance Media Director · E-commerce & CRO Director · CRM & Retention Director
    │
    ├── CHIEF MARKETING OFFICER (CMO): demand, brand, content, social, community, organic search
    │     └─ later: Creative Director (existing `ad-director` agent) · Social & Community Director · Organic Search Director
    │
    ├── CHIEF FINANCIAL OFFICER (CFO): the true numbers, unit economics, cash, data
    │     └─ later: Data & Insights Analyst
    │
    ├── CHIEF OPERATING OFFICER (COO): stock, workshop schedule, fulfilment, customer-service ops
    │     └─ later: Inventory & Fulfilment Controller
    │
    └── CHIEF TECHNOLOGY OFFICER (CTO): our own software (Shopify theme, Functions, Workers, Meta app, POS)
          └─ later: Platform Engineer
```

Human team: **Mr. Tahir** (manager and business head, back-end finance), counterpart to the CFO and COO.
**Ahsan** (store sales, WhatsApp, photos), counterpart to the CMO (photos) and COO (store stock).

## 2. Seats

| Seat | Owns (outcome) | Lead KPIs | Human counterpart |
|---|---|---|---|
| **CEO** | Company plan, weekly priorities, cross-seat trade-offs, morning brief | Monthly contribution margin | Founder |
| **CQRO** | The approval channel; fact-checks every L1–L3 item; hard-rule compliance; approvals register | 0 errors reaching customers · 0 hard-rule breaches · turnaround < 24h | Founder |
| **CHRO** | Org design, seat staging, hiring, onboarding, reviews, retirement | Seats filled on plan · % of agent output the Founder actually uses | Founder |
| **CRO** | Online revenue: paid media (Meta, later Google), store conversion (PDP, cart, checkout), promotions and pricing calendar (11.11, Black Friday, winter), email/CRM, repeat purchase | Surviving online revenue · real ROAS vs break-even · checkout completion · repeat rate | Founder |
| **CMO** | Brand and demand: positioning, creative and content engine for IG/FB/Threads/TikTok/YouTube, community (comments, DMs, WhatsApp scripts), organic search and blog, Merchant Center free listings, photo direction | Organic + social revenue · content shipped vs plan · DM response time · non-brand clicks | Founder, Ahsan |
| **CFO** | Shopify-reconciled truth: real vs Meta ROAS, margins per SKU, break-even CPA, cash and month-end P&L, discount control, dead-stock value | Reported numbers reconcile to source · cash forecast accuracy | Mr. Tahir |
| **COO** | Stock accuracy (incl. the **daily store-sales report** from Mr. Tahir/Ahsan, applied to Shopify), production queue with the workshop, restock triggers, PostEx, RTO, customer-service operations | Stock accuracy · stock-outs on hero SKUs · RTO % · on-time dispatch | Mr. Tahir, Ahsan |
| **CTO** | Building and running our own tools: theme releases, Shopify Functions, Cloudflare Workers, the Meta Graph API app (auto-post, comment/DM replies), POS/stock sync | Uptime of our tools · manual hours removed per week | Founder |

**RACI rules that settle the obvious overlaps**
- **Promotions:** CRO is accountable for the offer and the rupees. CFO is consulted on margin floors. CMO is responsible for the creative.
- **Ads:** CRO is accountable for spend and targeting. CMO is responsible for the creative supplied to it. CFO reports the real ROAS. CRO never grades its own results.
- **Product pages:** CRO is accountable for conversion. CMO is responsible for copy and imagery. CTO is responsible for template code.
- **Social replies:** CMO is accountable. CTO builds the automation. COO is consulted on order-status answers.
- **Stock:** COO is accountable. CFO is consulted on valuation. CTO builds the sync.

## 3. Hiring waves (proposed by CEO, for the CHRO to confirm or overturn)

| Wave | Seats | Why this order |
|---|---|---|
| **0 (now)** | CHRO | Hires everything else |
| **1** | CQRO · CRO · CMO | The approval channel must exist before anyone acts. Then the two seats that bring in sales. 11.11 (Nov 11) and Black Friday (Nov 27) fall inside this wave |
| **2** | COO · CFO | Daily store-stock reconciliation starts once the POS sync is switched off. True numbers once spend scales |
| **3** | CTO | Our own Meta app, POS replacement and automation backlog. The CEO covers urgent tech until then |
| **Later** | Directors and specialists | Only on evidence (see `chro.md` principle 2) |

## 4. The approval channel

| Level | Covers | Path | Founder? |
|---|---|---|---|
| **L0** Read & analyse | Queries, reports, research | Maker cites source + date for every number | No |
| **L1** Internal draft | Files on the `claude/*` branch, unpublished Shopify drafts, paused ad drafts, content packs | Maker → CQRO fact-check | No (informed in brief) |
| **L2** Customer-facing | Anything live: store, theme, product copy, socials, comments/DMs, WhatsApp, email | Maker → CQRO → owning exec → CEO → Founder | **Yes, each item or batch** |
| **L3** Money / irreversible | Ad spend and budgets, discounts, prices, deletions, customer-data uploads, stock write-offs | As L2 + rupee impact stated first | **Yes, every time** |

**CQRO fact-check standard:** every number traced to a tool result or export with its date. Every product claim matched to live Shopify data. Every statement checked against `CLAUDE.md` hard rules. Each finding gets a verdict of **APPROVED**, **RETURNED** (with the exact fix) or **BLOCKED** (rule breach).

## 5. Rhythm

- **Daily, morning:** CEO brief to the Founder covering yesterday's sales (online and store), cash, ad state, what is waiting for approval, today's top 3.
- **Daily, evening:** Mr. Tahir/Ahsan send the store-sales report. The COO applies stock changes (L2: the Founder approves the batch).
- **Weekly, Monday:** each exec reports KPI vs baseline. The CHRO runs the workforce review.
- **Monthly:** close, P&L, and the CHRO's seat plan for next month.
