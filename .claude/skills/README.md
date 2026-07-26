# Vendored skills

## SEO — 7 skills
Source: https://github.com/AgriciDaniel/claude-seo (MIT License, © 2026 agricidaniel).
Vendored Jul 18 2026 — 7 of 25 skills cherry-picked for the Kordovan SEO pass
(guidance markdown + references only).

**Intentionally omitted:** the repo's `scripts/*.py` and extensions — they depend
on paid APIs (DataForSEO, Ahrefs, Firecrawl — violates the project FREE-only rule)
or duplicate our own free GSC connector (`tools/gsc-mcp-worker/`). Where a
SKILL.md mentions those scripts or "DataForSEO", skip that step and use the
Kordovan GSC connector / Shopify MCP data instead.

---

## Meta Ads diagnosis — 1 skill
Source: https://github.com/mathiaschu/meta-ads-analyzer (MIT License, © 2026 Mathias Chu).
Vendored Jul 26 2026. `SKILL.md` + all 9 `references/` docs: breakdown effect,
learning phase, auction overlap, pacing, bid strategies, ad auctions, ad relevance
diagnostics, performance fluctuations, core concepts.

**Intentionally omitted:** the repo's `mcp/` server and `scripts/setup.sh` +
`refresh_token.sh`. They stand up a *second* Meta Marketing API connection needing
its own Meta Business App, long-lived token and app secret. We already have the
**Facebook Ads MCP** connected to account `995683712074843`, so the MCP layer is
redundant and the setup scripts would only add credential-handling risk. The value
here is the diagnostic framework, and that is 100% in the markdown.

---

## Ad strategy & creative — 16 skills + 5 agents
Source: https://github.com/zubair-trabzada/ai-ads-claude (MIT License, © 2026 Zubair Trabzada).
Vendored Jul 26 2026. All 15 sub-skills plus the `ads` orchestrator; the 5 subagent
definitions live in `.claude/agents/`.

**Local fixes applied on vendoring** (the upstream files do not load as-is):
- `ads/SKILL.md` shipped with **no YAML frontmatter** — added `name` + `description`.
- Five skills had prose `name:` values that did not match their directory
  (`Scroll-Stopping Hook Generator`, `Audience Persona Builder`,
  `Platform-Specific Ad Copy Generator`, `Google Ads Keyword Strategy`,
  `Video Ad Script Writer`) — renamed to their slugs so they resolve.

**Relevance to Kordovan, honestly graded:**
- **Live use:** `ads-hooks`, `ads-copy`, `ads-creative`, `ads-video`, `ads-testing`,
  `ads-landing`, `ads-audit`, `ads-budget`, `ads-funnel`, `ads-audience`.
- **Situational:** `ads-competitors` (pair it with the `ads_library_search` tool we
  already have — free), `ads-strategy` / `ads-quick` (whole-account passes),
  `ads-report-pdf` (needs `reportlab`, a free lib — see `tools/ads-report/`).
- **Parked:** `ads-keywords` is Google Ads only. We run no Google Ads, and organic
  keyword work is already served by the GSC connector.

---

## ⚠️ Read the ads skills against project rules, not as gospel
These are generic US/EU-market playbooks. Where they conflict with `CLAUDE.md`,
`CLAUDE.md` wins:
- Any suggestion to buy a tool/app/subscription → **FREE-only rule** overrides.
- Their CPM/CPC/CPA benchmarks are USD Western-market and are **wrong for PKR
  Pakistan** — use our own actuals in `ops/ADS_LAUNCH_JUL26.md`.
- They judge success on *orders placed*. We judge on **delivered orders in
  Shopify**, because ~40% COD refusal makes placed-order ROAS meaningless here.
- Never let generated copy mention `PAYONLINE10`.
- Only ad account `995683712074843` is ever in scope.
