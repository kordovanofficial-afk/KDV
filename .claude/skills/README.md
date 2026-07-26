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

**PRUNED Jul 26 2026 to 7 skills** — user directive: "keep ourselves focused on the
things that matter truly in details for our market only." Kept the ones that make
things we actually ship; deleted the ones that generate strategy decks we don't need
or assume platforms/currencies we don't use.

- **KEPT:** `ads-hooks`, `ads-copy`, `ads-creative`, `ads-video`, `ads-testing`,
  `ads-landing`, `ads-audit`.
- **DELETED:** `ads` (orchestrator for the deleted set) · `ads-keywords` (Google Ads
  only — we run none) · `ads-strategy` + `ads-quick` (URL-inferred whole-account
  passes; we have real first-party data that beats inference) · `ads-audience`
  (invents personas from a website; our audiences are built from actual delivered
  buyers) · `ads-budget` (allocates across Google/LinkedIn/TikTok in USD $1K–$10K —
  wrong platforms, wrong currency) · `ads-funnel` (multi-platform TOFU/MOFU/BOFU;
  ours is already built and Meta-only) · `ads-competitors` (Western swipe-file
  method) · `ads-report-pdf` (agency client deliverable — we are the client).
- Also deleted `.claude/agents/` (5 agents existed only to fan out `ads-strategy`)
  and `tools/ads-report/`.

---

## ⚠️ Read the ads skills against project rules, not as gospel
These are generic US/EU-market playbooks. **`ops/ADS_PLAYBOOK_PK.md` holds our real
PKR benchmarks, COD unit economics and attribution correction — it overrides any
number in these skills.** Where they conflict with `CLAUDE.md`, `CLAUDE.md` wins:
- Any suggestion to buy a tool/app/subscription → **FREE-only rule** overrides.
- Their CPM/CPC/CPA benchmarks are USD Western-market and are **wrong for PKR
  Pakistan** — use our own actuals in `ops/ADS_LAUNCH_JUL26.md`.
- They judge success on *orders placed*. We judge on **delivered orders in
  Shopify**, because ~40% COD refusal makes placed-order ROAS meaningless here.
- Never let generated copy mention `PAYONLINE10`.
- Only ad account `995683712074843` is ever in scope.
