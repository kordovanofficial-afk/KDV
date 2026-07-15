# ops/ — agent & session operations

Working notes, playbooks, and operational state for the Kordovan rebuild that
don't belong in the theme or in `docs/` (which is brand/design/SEO deliverables).

`CLAUDE.md` at the repo root remains the **persistent project memory** — read it
first every session. This folder is for longer-lived operational detail that
would clutter `CLAUDE.md`:

- **playbooks/** — repeatable procedures (deploy steps, GSC key rotation, Meta
  audience refresh, customer-cleanup queries) once they stabilize.
- **state/** — point-in-time snapshots worth committing (e.g. SEO scores per
  phase, audience sizes) — NOT session-local exports (those stay in scratchpad).

> Data exports (cancelled_orders.jsonl, serial_cod_refusers.csv, META_*.csv,
> customer CSVs) are session-local in the scratchpad — they contain PII and are
> **not** committed here.
