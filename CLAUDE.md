# Kordovan — Project Memory

> 💰 **HARD RULE (user, permanent): FREE options ONLY.** Never recommend or set up
> anything paid — no paid apps, connectors, tools, or subscriptions. Always find the
> zero-cost path (free tiers, native Shopify, export-CSV-and-share, self-hosted/open-source).

> 🚫 **HARD RULE (user, Oct 25 2026): NEVER MENTION KARACHI in any new content** — ads, videos,
> captions, product/SEO copy, blog, emails, WhatsApp. Say "our workshop" instead.
> ✅ **CLEANED Oct 25 2026 (user: "clean up from everywhere except the ads"), verified 0 hits:**
> theme (8 files), 144 products (benefits/SEO/body/subtitle), 31 review lists (reviewer city
> Karachi → "Pakistan", never swapped for another city), 11 collections + 8 collection metafields,
> 6 blog articles (live bodies diffed byte-identical to intended), 5 pages + FAQs.
> 🚫 **NOT changed, by design:** Meta ads (user excluded them — H3 founder ad still says it) ·
> Shipping + Privacy POLICIES (connector lacks `write_legal_policies` — ✅ user edited them Oct 25) · checkout rate "EXPRESS NEXT DAY DELIVERY (KARACHI ONLY)" (operational, removing it
> would let other cities buy a service they cannot get). Replacement vocabulary: "our own
> workshop", "made in Pakistan", "the south / the coast" for climate copy, "Malir Cantt" alone.
> ✅ The 31 `custom.reviews` lists (185 lines) — user confirmed Oct 25 2026: **collected by the team by
> contacting customers**. Provenance settled; do not re-raise. Shipping + Privacy policies: user edited them.

> ✍️ **HARD RULE (user, Oct 26 2026): EVERY piece of customer-facing text goes through the HUMANIZER skill
> (plugin "Humanizer" by blader) before it ships** — ad copy, captions, on-screen video text, product/collection/SEO
> copy, blog articles, emails, WhatsApp messages, review-request scripts. Load the skill (`Skill` tool, name contains
> `humanizer`) and run the draft through it; facts, prices, terms and claims must survive unchanged. If the skill is not
> loaded in a session, say so and apply its rules manually (no AI tells: no "elevate/seamless/crafted for those who…",
> no rule-of-three padding, no em-dash chains, no stated takeaways, plain specific words, Pakistani English/Roman Urdu
> where natural). ⚠️ Do NOT cite the "Razor UGC post 295 likes" as evidence: user confirmed Oct 27 2026 it was a paid
> UGC ad with bogus likes and fake comments. Judge any voice/language choice on Shopify orders, never on likes.

Custom Shopify theme for **Kordovan**, a Pakistani full-grain leather brand
(wallets, bags, small leather goods). This file is the persistent context for
every session — read it first.

## 📚 Memory index — READ THE MATCHING FILE BEFORE THAT KIND OF WORK
This file holds only standing rules. The detailed history (measurements, IDs, decisions, gotchas) lives in
`docs/memory/` and is NOT loaded automatically. Before any task in an area, read its file first; it is the
source of truth for numbers and IDs. Append new findings to the matching file, not here (keep this file short).

| File | Read before | Holds |
|---|---|---|
| `docs/memory/ads.md` | ANY Meta ads work (also read `ops/ADS_PLAYBOOK_PK.md`) | Aug audit, catalogue ads, TOF-J, RT-J, TOF-M, TOF-C, audiences, city keys, all ad/ad set IDs and reads |
| `docs/memory/jackets.md` | jackets, footwear, made-to-order, reviews | payment + lead-time rules in full, margins, refusal data, jacket SEO, the fabricated-review file and the review-collection rules |
| `docs/memory/seo.md` | SEO, blog, collections, product data, Merchant Center | GSC findings, redirects, sitelinks, blog pattern, page-2 pass, product-data pass, wallets goal, backlinks |
| `docs/memory/ops.md` | PostEx Worker, WhatsApp, email/DNS, customers, shipping rates, discounts | Worker design rules, COD fee rates + IDs, free-shipping threshold locations, discount sprawl, tooling |
| `docs/memory/theme.md` | ANY theme / storefront code | repo layout, palette, logo, what each page is built from, sync gotchas, performance rules, kdv- collections |
| `docs/memory/media.md` | video, images, AI generation | video-book pointers, music sources, Higgsfield limits, Google Flow method |
| `docs/video/VIDEO_BOOK.md` | ANY video | the full video system |
| `docs/brand/BRAND_MOODBOARD.md` | ANY design | palette, type, UX rules |

## ⚡ Standing rules digest (details in the files above)
- **Brand:** Quiet Heritage palette (Alabaster `#F7F2EA`, Espresso `#241C16`, Cognac `#A0623A` CTA, Saddle Tan `#C08B5C`),
  Fraunces headings + Inter body. Horse mark is a registered trademark: never trace or reuse it outside our own assets.
- **Theme deploys:** `kordovan` branch = LIVE store (theme `165057069296`). Build on the session's `claude/*` branch and
  **ask before every push/merge to `kordovan`**. Work on `claude/*` is invisible on the store until merged; say so.
  Theme files stay at repo root (never under `theme/`). Header/footer = `site-header` / `site-footer`.
- **Made to order = all 30 jackets + all 24 footwear.** 100% paid online (card / debit card / JazzCash), never "50% to
  book". Lead time "about 3 weeks to your door", always with the reason (cut for one customer, winter is peak season).
  MTO never shows "7-day returns" (shows "Lifetime warranty"). Any new shoe MUST get `custom.made_to_order`.
- **Changing a fact = sweep every surface:** `descriptionHtml`, `seo.description` (it is what Google Merchant Center
  publishes), every metafield (`custom.fits`, `custom.editorial`…), collections' hero AND editorial, theme, Worker copy.
  `seo:` is a FULL REPLACE: always send title AND description. Keep `seo.description` ≤ ~160 chars.
- **Shipping:** free delivery over **Rs 5,500**; COD costs Rs 250 more (rates on the default profile). Threshold lives in
  `theme.js` renderShip, `main-cart.liquid`, `pdp-jsonld.liquid`: change all three together.
- **Meta ads:** only account `995683712074843`. Every ad set = the 9 cities (no radius) + excludes COD Refusers
  `120253660257910428`. `targeting` is a full replace (fetch + merge). Ad creatives are immutable (new creative → new
  ad → pause old). Meta over-reports ~2x vs surviving Shopify revenue. Money changes need explicit user OK each time;
  customer PII uploads need OK each time. Write kill thresholds in rupees before launch, with the events-per-week maths.
- **Reviews:** never invented. Publish only with provenance (the customer's own rating and words, consent, a date).
  Never offer anything in exchange for a review.
- **Copy accuracy:** vegan bags are not leather; croc/snake belts are textured, not exotic skin; The Stallion boot says
  1-year warranty (no lifetime claim) and its material is unresolved; never assert a feature you cannot verify.
  Never publish exact competitor prices (bands only).
- **Measurement:** judge ads on 14-day windows; never compare order survival across cohorts of different ages; never
  count a cancelled-before-dispatch order as a refusal; pull the query breakdown before calling a page an opportunity.
- **Video:** Claude does all edit work; user supplies footage + voice. Music on every video (CC0 from Hugging Face
  `SoundSafari/Public-Domain-Music`); ads use CC0 only. Never show a real ID in footage. Never name Ridge in ads.
  AI footage: start from the real product photo and check colour, stitching and the horse mark frame by frame.
- **Mocha Mate Higgsfield stills** are for Instagram posts only, never ads, unless the user asks again.
- No PRs unless asked. No model IDs in commits.

## 🚦 Hard constraints (do not violate)
- ⚠️ **ROLES FLIPPED Jul 25 2026 — `165057069296 "KDV/kordovan"` IS NOW THE LIVE
  `MAIN` THEME.** The user published it (theme record shows role MAIN, updated
  2026-07-25T02:45Z); the old live theme `162105917680` is now UNPUBLISHED and is
  the fallback/rollback copy. The old "never touch 162105917680" rule is obsolete
  — that ID is no longer serving customers.
- 🔴 **Consequence: pushing `kordovan` now deploys STRAIGHT TO THE LIVE STORE.**
  There is no draft buffer any more. Every theme commit is a production release
  during paid-ads spend. Review carefully; prefer a mockup or a duplicate theme
  for anything structural.
- Shopify GitHub integration deploys from the **`kordovan`** branch.
- **Work on `kordovan`** (the source of truth).
- 🛑 **ASK BEFORE EVERY PUSH TO `kordovan` (user, Aug 19 2026 — supersedes the old
  "user authorized per-step deploys" rule).** Each push is a live release while ads
  are running, so confirm every time; a yes on one deploy is NOT standing permission
  for the next. Build on the session's `claude/*` branch, then ask to merge.
- ⚠️ **Sessions are often scoped to a `claude/*` branch while Shopify deploys only
  from `kordovan`** — so work is INVISIBLE on the store until that merge. Say so
  when handing off, or the user checks the site and sees the old version.
- Do not create PRs unless explicitly asked.

