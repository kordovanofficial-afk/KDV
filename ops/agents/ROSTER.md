# Kordovan — Agent Roster

Owner: CHRO. Every agent, every stage, every decision. Never delete rows.

**Hiring Floor (interview page):** https://claude.ai/artifact/UubufgPRvXCLYJFrQzP78s (db collections: `candidates`, `seats`, `decisions`, `transcripts`). Source: `ops/agents/hiring-floor.html`

| Seat | Agent file | Status | Since | Source | Notes |
|---|---|---|---|---|---|
| CEO | (the main session) | ACTIVE | Oct 31 2026 | — | Appointed by Founder |
| CHRO | `.claude/agents/chro.md` | PROBATION (to Nov 30 2026) | Oct 31 2026 | Custom build by CEO | "Noor Rehman". Hired by Founder Oct 31 2026. First task: wave 1 candidates |
| Creative Director (under CMO) | `.claude/agents/ad-director.md` | ACTIVE (pre-existing) | — | Custom | Video ad production packages. Reports to CMO once CMO is hired |
| CQRO | `.claude/agents/cqro.md` | PROBATION (to Nov 30 2026) | Oct 31 2026 | Custom build; structure from VoltAgent compliance-auditor.md (MIT) | "Hamna Qureshi". Hired by Founder Oct 31 2026: "monitor and give more authority that lies within her domain" → binding BLOCK (Founder-only override), direct fixes to L1 facts, standing audit rights, read-only Shopify/Meta/GSC. Register `approvals/REGISTER.md` |
| CRO | — | RE-SOURCING (Farhan rejected Oct 31) | — | — | Founder: "lacks clarity and accuracy, which is highly needed for this role" |
| CMO | — | RE-SOURCING (Mahnoor rejected Oct 31) | — | — | Founder: "shes the CMO and lacks commercial Judgement" |
| COO | — | PLANNED, wave 2 | — | — | — |
| CFO | — | PLANNED, wave 2 | — | — | — |
| CTO | — | PLANNED, wave 3 | — | — | — |

## Decision log
| Date | Candidate | Seat | Decision | Founder's note | Follow-up |
|---|---|---|---|---|---|
| Oct 31 2026 | Noor Rehman | CHRO | HIRE | (none) | Interview pushed on: CEO-scored self-assessment, GitHub data-leak screening, who settles exec disputes (Founder: execs must deliberate with real numbers BEFORE escalating, now in ORG_DESIGN §4a), failure detection. Probation 30 days |
| Oct 31 2026 | Hamna Qureshi | CQRO | HIRE | monitor and give more authority that lies within her domain.. | Interview: challenged on CLAUDE.md-only checking (answer: live read access, fixed at hire) and on being the 11.11 bottleneck (answer: batch approvals, pre-approved templates, 24h turnaround). Authority expanded per note; weekly CHRO monitoring |
| Oct 31 2026 | Farhan Malik | CRO | REJECT | lacks clarity and accuracy, which is highly needed for this role | Decided from the dossier (no interview). Re-source: verify every number live, one-page answer first |
| Oct 31 2026 | Mahnoor Abbasi | CMO | REJECT | shes the CMO and lacks commercial Judgement | Decided from the dossier. Re-source: every content decision tied to rupees and measured |

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
