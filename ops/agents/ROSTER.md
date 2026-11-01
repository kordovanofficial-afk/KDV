# Kordovan — Agent Roster

Owner: CHRO. Every agent, every stage, every decision. Never delete rows.

**Hiring Floor (interview page):** https://claude.ai/artifact/UubufgPRvXCLYJFrQzP78s (db collections: `candidates`, `seats`, `decisions`, `transcripts`). Source: `ops/agents/hiring-floor.html`

| Seat | Agent file | Status | Since | Source | Notes |
|---|---|---|---|---|---|
| CEO | (the main session) | ACTIVE | Oct 31 2026 | — | Appointed by Founder |
| CHRO | `.claude/agents/chro.md` | PROBATION (to Nov 30 2026) | Oct 31 2026 | Custom build by CEO | "Noor Rehman". Hired by Founder Oct 31 2026. First task: wave 1 candidates |
| Creative Director (under CMO) | `.claude/agents/ad-director.md` | ACTIVE (pre-existing) | — | Custom | Video ad production packages. Reports to CMO once CMO is hired |
| CQRO | `.claude/agents/cqro.md` | PROBATION (to Nov 30 2026) | Oct 31 2026 | Custom build; structure from VoltAgent compliance-auditor.md (MIT) | "Hamna Qureshi". Hired by Founder Oct 31 2026: "monitor and give more authority that lies within her domain" → binding BLOCK (Founder-only override), direct fixes to L1 facts, standing audit rights, read-only Shopify/Meta/GSC. Register `approvals/REGISTER.md` |
| CRO | `.claude/agents/cro.md` | PROBATION (to Dec 1 2026) | Nov 1 2026 | Custom build; structure from VoltAgent assumption-mapping.md (MIT) | "Sana Iqbal". Hired by Founder Nov 1 2026. Read-only Shopify/Meta/GSC. First task: final 11.11 recommendation on live data |
| CMO | `.claude/agents/cmo.md` | PROBATION (to Dec 1 2026) | Nov 1 2026 | Custom build; structure from VoltAgent landing-page-copywriter.md (MIT) | "Omar Shafiq". Hired by Founder Nov 1 2026. Read-only Shopify/Meta/GSC. Creative Director (ad-director) now reports here |
| COO | `.claude/agents/coo.md` | PROBATION (to Dec 1 2026) | Nov 1 2026 | Custom build (CHRO, wave 2) | "Zain Haider". Hired by Founder Nov 1 2026. Read-only Shopify incl. inventory |
| CFO | `.claude/agents/cfo.md` | PROBATION (to Dec 1 2026) | Nov 1 2026 | Custom build (CHRO, wave 2) | "Ayesha Naqvi". Hired by Founder Nov 1 2026. Read-only Shopify + Meta. Sets the binding margin floor |
| CTO | — | PLANNED, wave 3 | — | — | — |

## Decision log
| Date | Candidate | Seat | Decision | Founder's note | Follow-up |
|---|---|---|---|---|---|
| Oct 31 2026 | Noor Rehman | CHRO | HIRE | (none) | Interview pushed on: CEO-scored self-assessment, GitHub data-leak screening, who settles exec disputes (Founder: execs must deliberate with real numbers BEFORE escalating, now in ORG_DESIGN §4a), failure detection. Probation 30 days |
| Oct 31 2026 | Hamna Qureshi | CQRO | HIRE | monitor and give more authority that lies within her domain.. | Interview: challenged on CLAUDE.md-only checking (answer: live read access, fixed at hire) and on being the 11.11 bottleneck (answer: batch approvals, pre-approved templates, 24h turnaround). Authority expanded per note; weekly CHRO monitoring |
| Oct 31 2026 | Farhan Malik | CRO | REJECT | lacks clarity and accuracy, which is highly needed for this role | Decided from the dossier (no interview). Re-source: verify every number live, one-page answer first |
| Oct 31 2026 | Mahnoor Abbasi | CMO | REJECT | shes the CMO and lacks commercial Judgement | Decided from the dossier. Re-source: every content decision tied to rupees and measured |
| Nov 1 2026 | Sana Iqbal | CRO | HIRE | (none) | Replaced Farhan. CEO verified every work-sample number against Shopify before the interview |
| Nov 1 2026 | Omar Shafiq | CMO | HIRE | (none) | Replaced Mahnoor. Known work-sample error (hat order value) to be corrected in first task |
| Nov 1 2026 | Zain Haider | COO | HIRE | (none) | Wave 2 |
| Nov 1 2026 | Ayesha Naqvi | CFO | HIRE | (none) | Wave 2 |

## Sourcing log (wave 1, Oct 31 2026)
| Repo / file | Licence | Screen | Used for |
|---|---|---|---|
| VoltAgent/awesome-claude-code-subagents `categories/04-quality-security/compliance-auditor.md` | MIT | PASS (structure only) | CQRO |
| VoltAgent `categories/08-business-product/content-quality-editor.md` | MIT | **FAIL**: executable payload (`npm install -g unslop`) | — |
| VoltAgent `categories/07-specialized-domains/risk-manager.md` | MIT | PASS, not used (finance frameworks, no fit) | — |
| VoltAgent `categories/08-business-product/growth-loops.md` | MIT | PASS (structure only) | CRO |
| wshobson/agents `plugins/business-analytics/agents/business-analyst.md` | MIT | PASS (structure only) | CRO |
| VoltAgent `categories/08-business-product/content-marketer.md` | MIT | PASS after stripping fabricated sample stats | CMO |
| wshobson/agents `plugins/content-marketing/agents/content-marketer.md` | MIT | PASS after stripping paid tools / "use PROACTIVELY" | CMO |
| contains-studio/agents (growth-hacker, tiktok-strategist, instagram-curator, legal-compliance-checker) | none found | **FAIL**: no licence | — |
Read via WebFetch (summarised pages, not byte-level). No text copied.

## Sourcing log (wave 1 re-source after rejections, Oct 31 2026)
Spec = the Founder's notes. CRO bar: clarity + accuracy. CMO bar: commercial judgment. Briefs updated to v2. Work samples use only `briefs/DATA_PACK_2026-10-31.md` and dated CLAUDE.md figures.
| Repo / file | Licence | Screen | Used for |
|---|---|---|---|
| VoltAgent `categories/08-business-product/assumption-mapping.md` | MIT (LICENSE read: Copyright (c) 2025 VoltAgent) | PASS (structure only: graded assumption register) | CRO `cro-sana` |
| VoltAgent `categories/08-business-product/landing-page-copywriter.md` | MIT | PASS after removing "query context manager" JSON protocol, competitor-page research and testimonial guidance | CMO `cmo-omar` |
| VoltAgent `categories/08-business-product/telegram-ads-analyst.md` | MIT | PASS on safety, rejected on fit (Telegram ad buying; benchmarks cited to the contributing vendor's own product) | — |
| wshobson/agents `plugins/customer-sales-automation/agents/sales-automator.md` | MIT | PASS on safety, rejected on fit (B2B cold email, "Use PROACTIVELY") | — |
| 0xfurai/claude-code-subagents | MIT | No business/marketing agents found | — |
Stage record: Requisition v2 (Oct 31) → Sourcing (Oct 31) → Screening 7/7 PASS both (Oct 31) → Work sample scored (Oct 31, CHRO; CEO re-score pending) → candidate JSON + draft agent file written → **awaiting CEO review and push to `candidates/cro-sana`, `candidates/cmo-omar`; `seats/cro` and `seats/cmo` → status "interviewing"**.

## Sourcing log (wave 2: COO + CFO, Nov 1 2026)
Hiring bar carried from wave 1: five lines first, every number sourced and dated, assumptions boxed, commercial judgment, plus one idea the Founder has not asked for (Founder in Sana's interview). Work samples use only `briefs/DATA_PACK_2026-10-31.md` and dated CLAUDE.md figures.
| Repo / file | Licence | Screen | Used for |
|---|---|---|---|
| VoltAgent `categories/07-specialized-domains/risk-manager.md` | MIT | PASS after removing Bash, "context manager" JSON protocol, template result figures and autonomous "implement" steps (structure only: control + KRI + cost of failure) | COO `coo-zain` |
| wshobson/agents `plugins/startup-business-analyst/agents/startup-analyst.md` | MIT | PASS after removing "use PROACTIVELY", slash-command integrations, web research and US benchmark figures (structure only: quality standards) | CFO `cfo-ayesha` |
| wshobson/agents `plugins/customer-sales-automation/agents/customer-support.md` | MIT | PASS on safety items read, **rejected on fit + rules**: paid helpdesk stack (Zendesk, Intercom, Gorgias), autonomous outreach with no approval step | — |
| VoltAgent `categories/08-business-product/customer-success-manager.md` | MIT | Rejected on fit (SaaS account management; sample results read as real figures) | — |
Read via WebFetch (summarised pages, not byte-level). No text copied. No inventory/supply-chain agent found in VoltAgent, wshobson or the aggregator search.
Stage record: Requisition (Nov 1, `briefs/coo.md`, `briefs/cfo.md`) → Sourcing (Nov 1) → Screening 7/7 PASS both (Nov 1) → Work sample scored by CHRO (COO 4/4/5/4/5 = 4.4; CFO 5/4/4/4/4 = 4.2; CEO re-score pending) → `candidates/coo-zain.{json,md}`, `candidates/cfo-ayesha.{json,md}` written → **awaiting CEO review and push to `candidates/coo-zain`, `candidates/cfo-ayesha`; `seats/coo` and `seats/cfo` → status "interviewing"**.
Conflicts raised with the CEO (not resolved quietly): (1) `briefs/cro.md` RACI lists CRO A/R on discount codes vs the CFO seat's "discount control": proposed split = CRO owns offer + code hygiene, CFO owns the binding margin floor; (2) "ad spend ~4,000/day" is the rate since Oct 24 only; October was ~3,000/day for 23 days; (3) Mocha Mate 43 units (Oct 24) vs 25 (Oct 31) vs data pack 72 units / 101 orders; (4) Bellezza cost 2,350 carries the wallet buffer though bags carry none (Founder said 2,200).
