# Kordovan — Agent Roster

Owner: CHRO. Every agent, every stage, every decision. Never delete rows.

**Hiring Floor (interview page):** https://claude.ai/artifact/UubufgPRvXCLYJFrQzP78s (db collections: `candidates`, `seats`, `decisions`, `transcripts`). Source: `ops/agents/hiring-floor.html`

| Seat | Agent file | Status | Since | Source | Notes |
|---|---|---|---|---|---|
| CEO | (the main session) | ACTIVE | Oct 31 2026 | — | Appointed by Founder |
| CHRO | `.claude/agents/chro.md` | PROBATION (to Nov 30 2026) | Oct 31 2026 | Custom build by CEO | "Noor Rehman". Hired by Founder Oct 31 2026. First task: wave 1 candidates |
| Creative Director (under CMO) | `.claude/agents/ad-director.md` | ACTIVE (pre-existing) | — | Custom | Video ad production packages. Reports to CMO once CMO is hired |
| CQRO | `ops/agents/candidates/cqro.md` (draft) | SCREENED + WORK SAMPLE DONE, awaiting CEO review before Hiring Floor | Oct 31 2026 | Custom build; structure from VoltAgent compliance-auditor.md (MIT) | "Hamna Qureshi" `cqro-hamna`, self-scored avg 4.2. Brief `briefs/cqro.md` |
| CRO | `ops/agents/candidates/cro.md` (draft) | SCREENED + WORK SAMPLE DONE, awaiting CEO review before Hiring Floor | Oct 31 2026 | Custom build; structure from VoltAgent growth-loops.md + wshobson business-analyst.md (MIT) | "Farhan Malik" `cro-farhan`, self-scored avg 4.2. Brief `briefs/cro.md` |
| CMO | `ops/agents/candidates/cmo.md` (draft) | SCREENED + WORK SAMPLE DONE, awaiting CEO review before Hiring Floor | Oct 31 2026 | Custom build; structure from VoltAgent + wshobson content-marketer.md (MIT) | "Mahnoor Abbasi" `cmo-mahnoor`, self-scored avg 4.0. Brief `briefs/cmo.md` |
| COO | — | PLANNED, wave 2 | — | — | — |
| CFO | — | PLANNED, wave 2 | — | — | — |
| CTO | — | PLANNED, wave 3 | — | — | — |

## Decision log
| Date | Candidate | Seat | Decision | Founder's note | Follow-up |
|---|---|---|---|---|---|
| Oct 31 2026 | Noor Rehman | CHRO | HIRE | (none) | Interview pushed on: CEO-scored self-assessment, GitHub data-leak screening, who settles exec disputes (Founder: execs must deliberate with real numbers BEFORE escalating, now in ORG_DESIGN §4a), failure detection. Probation 30 days |

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
