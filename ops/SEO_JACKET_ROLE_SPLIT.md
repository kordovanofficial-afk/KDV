# Jacket SEO — keyword role split (19 Aug 2026)

Fixes the cannibalisation between the two pages that both rank for every
Pakistani jacket head term. **Shopify content only — no theme files touched.**

## The problem

For every valuable head term, both pages ranked at once and neither won:

| Query | Brands article | Collection | Impressions (90d) |
|---|---|---|---|
| leather jackets in pakistan | 11.3 | 8.6 | 1,332 |
| leather jacket pakistan | 12.6 | 8.5 | 1,536 |
| leather jacket in pakistan | 12.0 | 6.5 | 633 |
| leather jackets pakistan | 12.3 | 10.3 | 473 |
| pure leather jackets in pakistan | 8.2 | 12.3 | 164 |

Google picks one page per query, kept switching, and neither accumulated
enough authority to break the top five. Root cause of position 8–13.

## The split (locked — keep it this way)

- **`/collections/mens-leather-jackets` owns TRANSACTIONAL.**
  `leather jackets in pakistan`, `leather jacket men`, `leather jacket price`,
  `buy leather jacket`. It is the page that should rank for anyone shopping.
- **`/blogs/jackets/top-10-leather-jacket-brands-in-pakistan` owns COMPARISON.**
  `top 10`, `best`, `brands`. It already holds ~position 2 for those.

Anchor text is the signal that declares this. **Do not link from the article to
the collection with brand-comparison anchor text, and do not link from the
collection to the article with transactional anchor text.**

## What changed

### Collection (`gid://shopify/Collection/438804021488`)
- `descriptionHtml` rewritten — opens with "Genuine leather jackets for men,
  made in Pakistan" so the head phrase appears as a unit; links to the article
  with the comparison anchor "comparison of the top leather jacket brands in
  Pakistan".
- **New metafield `custom.editorial`** (`multi_line_text_field`, raw HTML) —
  ~400 words rendered below the grid by `sections/main-collection.liquid:129`.
  Covers choosing a cut, sizing for a Pakistani winter, what the leather is,
  and prepaid/delivery terms. Angle is deliberately *product selection*, not
  brand comparison, so it does not duplicate the article.
- Why it matters: the collection was thinner than the article, which is part of
  why the article kept winning the coin toss. It now has the depth to deserve
  the term.
- ⚠️ The theme's fallback editorial block (same file, line 132) says "cash on
  delivery nationwide" — wrong for jackets, which are prepaid only. The new
  metafield overrides it on this collection. **Other collections still show the
  fallback.**
- SEO title/description left alone — `Men's Leather Jackets Pakistan — From
  Rs 22,000 | Kordovan` is already performing (CTR 1.97% → 3.90% since the
  early-August pass).

### Article (`gid://shopify/Article/590763229424`)
- `global.description_tag` replaced. Was generic legacy copy ("find affordable
  options") that matched neither the article nor the comparison intent. Now:
  "An honest comparison of the ten leather jacket brands worth knowing in
  Pakistan, with the price bands that tell you whether you are buying real
  leather or plastic."
- `global.title_tag` **deliberately unchanged** — it holds ~position 2 for its
  term and contains "Brands", which is the differentiator. Do not touch it.
- Body: added an early signpost after the disclosure box and a closing CTA,
  both linking to the collection with the anchor "men's leather jackets in
  Pakistan"; changed the mid-article anchor from "Browse men's leather jackets"
  to the same phrase.
- JSON-LD: `dateModified` → 2026-08-19, `description` synced to the new meta,
  `about` narrowed from "Leather jackets in Pakistan" to "Leather jacket brands
  in Pakistan" (reinforces the comparison role).
- Everything else byte-identical — verified after the write: all 4 images and
  srcsets, all 10 brand entries, the 6-question FAQPage block.

## Not done, deliberately

- **Blog tags left alone.** `leather jacket price in pakistan`, `leather jacket`
  etc. spawn thin `/blogs/jackets/tagged/*` archives (one seen at position 60,
  5 impressions). Removing the tags would 404 those URLs for negligible gain.
  Revisit only if a noindex rule for tag archives is added to `theme.liquid`,
  which currently has none.
- `/collections/all/mens-jacket` (11 impressions, position 27.7) is a
  tag-filtered duplicate. Add to the redirect list when the catalogue-trim
  redirects are built.

## Measuring it

Re-check in Search Console ~3–4 weeks (mid Sept, before the season). Success =
the collection holds the head terms alone and the article stops appearing for
them. Watch that the article's own terms (`top 10`, `best`, `brands`) do not
slip — if they do, the de-targeting went too far.

Peak season for context: Pakistan did **215,256 jacket impressions / 7,746
clicks** between 1 Nov 2025 and 28 Feb 2026, ~7× current volume.
