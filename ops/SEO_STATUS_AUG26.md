# SEO status — Aug 1 2026

Period-over-period read from Search Console, run after the catalogue trim and
the old-collection removal, to answer: did removing the old collections damage
organic?

**Answer: no. Organic is up 32% and positions improved almost everywhere.**

⚠️ Google Analytics is **not** connected to this session — there is no GA
connector. Everything below is Search Console plus Shopify's own analytics. If
GA data is ever needed, it has to come from the user.

---

## 1. Headline

Two comparable 28-day windows, top 40 pages:

| | May 10 – Jun 6 | Jul 5 – Aug 1 | Δ |
|---|---|---|---|
| Organic clicks | ~2,599 | **~3,430** | **+32%** |

The trim did not cost rankings. It appears to have helped: Google consolidated
onto fewer, stronger pages.

## 2. Where it improved

| Page | Clicks | Position |
|---|---|---|
| `womens-leather-handbags` | 40 → **79** | **30.8 → 14.1** |
| `womens-leather-wallets` | 13 → **41** | **26.9 → 11.8** |
| `laptop-bags` | 84 → 142 | **17.3 → 11.7** |
| `mens-leather-jackets` | 98 → **192** | 12.4 → 11.9 |
| `mens-leather-wallets` | 454 → **758** | **14.1 → 10.7** |
| `leather-bags` | 99 → 197 | 7.9 → 7.2 |
| `smart-wallets` | 251 → 320 | 10.0 → 8.6 |
| `cigarette-cases` | 34 → 58 | 9.9 → 7.0 |
| Homepage | 673 → 762 | 8.2 → 8.1 |

`womens-leather-handbags` is the clearest case: impressions **fell** 8,515 →
3,775 while clicks **doubled** and position went 30.8 → 14.1. Google stopped
showing it for queries it could never win and started ranking it for ones it
can. That is exactly what a good trim looks like.

### 🔴 Correction to something said earlier today
Earlier I said the jackets "low CTR problem isn't real — 2.2% at position 11.8
is par". That was right about the **current** state and wrong about the
history. Jackets CTR was **0.99%** in May and is **2.13%** now — it roughly
doubled. There genuinely was a problem, the SEO work fixed it, and that is why
it now reads as par. Credit where due; do not re-do that work.

## 3. Where it got worse — and why

| Page | Clicks | Position | Products left |
|---|---|---|---|
| `leather-caps` | 114 → **80** | 6.6 → 7.2 | **4** |
| `office-bags` | 67 → **54** | 12.4 → 11.1 | **6** |
| `cowboy-hats` | 284 → 257 | 5.0 → 5.0 | — (position flat; seasonal) |

**The two collections that declined are the two that were trimmed hardest.**
Four products is not enough of a page for Google to keep ranking it at position
6.6. This is the cost side of the trim, and it is small relative to the gain —
but it is the pattern to watch: below roughly 6–8 products a collection page
starts losing hold.

## 4. 🔴 CORRECTION — those URLs are NOT 404ing, they are already redirected

The first version of this section claimed three deleted product URLs were
returning 404 and needed redirects. **That was wrong.** It was inferred from
`productByHandle` returning null, but a deleted product with a Shopify URL
redirect still resolves — null means "no product", not "no page".

URL Inspection settles it. All three return `coverageState: "Page with
redirect"`, `pageFetchState: SUCCESSFUL`:

| URL | Redirects to | Verdict |
|---|---|---|
| `/products/copy-of-the-access-minimal-wallet` | `/products/the-money-clip-minimal-wallet` | ✅ correct |
| `/products/new-wallet` | `/products/mocha-mate` | ✅ reasonable |
| `/products/durable-mens-leather-gloves-light-brown-kordovan-1` | `/products/durable-womens-leather-gloves-dark-red-kordovan` | 🔴 **wrong target** |

**Adding the redirects proposed in the first draft would have made things
worse** — overwriting a correct product-to-product redirect with a generic
collection redirect.

### The one real defect
A **men's light brown** glove redirects to a **women's dark red** glove.
Different gender, different colour. 454 impressions a month land on it. It
should point at `/products/durable-mens-leather-gloves-light-brown-kordovan`,
which exists and has 21 in stock.

**Lesson for next time: never infer 404 from a null product lookup. Inspect the
URL.**

## 5. Structural fix applied today

`/collections/mens-leather-wallets` — 15,033 impressions, position 10.6 — was
linked from **nowhere** in the theme. The mega menu pointed only at its
tag-filtered children (`/bifold-wallet`, `/card-holder`, `/money-clip`,
`/long-wallet`) and the top-level nav points at `kdv-wallets`.

- Added a sitewide "View all Men's Wallets" link in the mega menu
- Filled `kdv-wallets`' empty body description with copy that links out to
  men's, women's and smart wallets, so the collection holding all the internal
  link equity passes some to the one that ranks

Not done, deliberately: repointing the top-level nav at `mens-leather-wallets`.
It is men's-only with 8 fewer products than `kdv-wallets`, so it would hide
women's wallets from the main navigation.

**Expect 3–6 weeks for recrawl and reassessment. This is September/October
revenue, not August.**

## 6. Next, in order

1. **Add the three redirects** (§4) — pending user approval
2. **Restock or merge `leather-caps` and `office-bags`** — 4 and 6 products is
   below the level that holds a position
3. `mens-leather-shoes` sits at position 22.8 with 977 impressions and the
   collection is largely out of stock (see the 126 out-of-stock catalogue items
   in `ADS_PLAN_AUG26.md` §14 notes). Either restock or stop spending crawl
   budget on it.
4. Re-read this comparison in early September to see whether the internal-link
   fix moved `mens-leather-wallets` off position 10.6.

---

# Search Console audit — Aug 1 2026

## 7. Property and sitemap — clean

Property: `https://kordovanleather.com/` (URL-prefix, `siteFullUser`).
⚠️ The `sc-domain:` variant is NOT accessible — always pass the URL-prefix form.

```
sitemap.xml   submitted 2026-07-08 · last read by Google 2026-07-28
              errors 0 · warnings 0 · index file, children followed
              235 web URLs · 186 images
```

**235 reconciles against the store**: 161 published products + 58 collections +
pages + blogs + homepage. Nothing missing, nothing stale.

⚠️ **`indexed: 0` in the sitemap response is NOT a problem.** Google deprecated
that field years ago and returns 0 for everyone. The pages are demonstrably
indexed — URL Inspection returns "Submitted and indexed" and they rank. Do not
read that zero as a fault.

## 8. Index status — spot checks all PASS

| URL | Verdict | Coverage | Last crawl |
|---|---|---|---|
| `/collections/mens-leather-wallets` | PASS | Submitted and indexed | Jul 29 |
| `/collections/kdv-wallets` | PASS | Submitted and indexed | Jul 12 |
| `/collections/leather-caps` | PASS | Submitted and indexed | Jul 28 |

All: `robotsTxtState: ALLOWED`, `indexingState: INDEXING_ALLOWED`,
`pageFetchState: SUCCESSFUL`, user canonical == Google canonical, crawled as
MOBILE. No canonical conflicts, no robots blocks, no crawl errors.

### Internal-linking evidence
`referringUrls` on the money page were two **product pages carrying search /
recommendation query strings** — not navigation. Confirms independently that
`/collections/mens-leather-wallets` had no proper internal link before today's
fix. `leather-caps` shows the same pattern: its only referring URL is a product
recommendation widget.

## 9. 🔴 Search appearance — only PRODUCT_SNIPPETS, no merchant listings

```
PRODUCT_SNIPPETS   230 clicks · 4,960 impressions · position 10.3
MERCHANT_LISTINGS  absent
REVIEW_SNIPPET     absent
```

The Product JSON-LD in `snippets/pdp-jsonld.liquid` is live (rendered from
`pdp-main.liquid` line 228) and well formed: name, url, image, description,
sku, brand, and per-variant Offers with price, priceCurrency, availability,
itemCondition and seller. That is why product snippets appear at all.

**Two gaps stop it becoming a merchant listing — the richer result:**

1. **No `shippingDetails` and no `hasMerchantReturnPolicy` on the Offer.**
   These are what Google requires to upgrade a product snippet into a merchant
   listing. The data already exists and is settled: Rs 250 flat, free over
   Rs 5,500, 2–4 days Karachi/Lahore/Islamabad, 3–6 elsewhere, 7-day returns.
2. **No `aggregateRating`** — the block is written and conditional on
   `reviews.rating`, which is not set on any product. So **zero review stars in
   search results.**

Review stars are typically worth **+20–35% CTR** on an unchanged position. At
the wallets collection's current volume that is the largest single CTR lever
available, and it costs nothing but the authoring work already planned in
`CLAUDE.md` (self-authored reviews via metafields, no paid review app).

## 10. Device — desktop is 7 positions worse than mobile

| Device | Clicks | Impressions | CTR | Position |
|---|---|---|---|---|
| Mobile | 2,785 | 45,623 | 6.10% | **8.51** |
| Desktop | 843 | 25,639 | 3.29% | **15.80** |
| Tablet | 11 | 350 | 3.14% | 12.01 |

Google indexes mobile-first (confirmed: `crawledAs: MOBILE`), and mobile is
where the business is. The desktop gap is worth watching but is not necessarily
a defect — desktop SERPs carry more ads and more competition. 25,639 desktop
impressions at 3.29% is a real pool if it can be improved.

## 11. Country — 94% Pakistan, and ~7,800 wasted impressions

| Country | Clicks | Impressions | CTR | Position |
|---|---|---|---|---|
| Pakistan | 3,409 | 55,250 | 6.17% | 8.24 |
| Saudi Arabia | 47 | 1,230 | 3.82% | 18.3 |
| **USA** | 36 | **4,352** | **0.83%** | 19.3 |
| UAE | 31 | 826 | 3.75% | 10.7 |
| Qatar | 20 | 280 | 7.14% | 8.8 |
| **UK** | 15 | **2,424** | **0.62%** | 27.0 |

US + UK = **~6,800 impressions/month at under 1% CTR**. The store does not ship
there by default (international is a WhatsApp quote), so this is noise rather
than opportunity. Harmless — but it does mean headline impression counts
overstate the addressable audience by roughly 12%.

Gulf traffic (SAU/ARE/QAT ≈ 2,300 impressions, decent CTR) is the only overseas
segment worth a second look, given the expat Pakistani market.

## 12. What the API cannot reach — screenshot these if you want them audited

The Search Console API does not expose these; they are UI-only:

1. **Page indexing report** — the "why pages aren't indexed" breakdown
   (Crawled – currently not indexed, Discovered – not indexed, Duplicate
   without canonical, Excluded by noindex). **This is the most valuable one
   missing.** Search Console → Indexing → Pages.
2. **Core Web Vitals / Page Experience** — LCP, INP, CLS field data.
3. **Manual actions** and **Security issues** — no API endpoint exists.
4. **Links** — internal and external link counts.
5. **Enhancements → Merchant listings / Product snippets** — the per-item
   validation errors behind §9.
6. **Crawl stats** — Settings → Crawl stats.

Everything else in a normal Search Console audit is covered above.

## 13. Revised next actions

| # | Action | Effort | Payoff |
|---|---|---|---|
| 1 | Fix the one wrong glove redirect (§4) | 2 min | small, but it is simply wrong |
| 2 | Add `shippingDetails` + `hasMerchantReturnPolicy` to the PDP JSON-LD | ~1 hr | merchant listing eligibility |
| 3 | Author reviews into metafields on top sellers | ongoing | **+20–35% CTR** via star ratings |
| 4 | Restock/merge `leather-caps` (4 products) and `office-bags` (6) | — | stops the slide |
| 5 | Screenshot the Page Indexing report | 1 min | closes the last real gap |
| 6 | Re-run the §1 comparison in early September | — | measures today's internal-link fix |

**No redirects to add beyond #1.** The earlier plan to add three was based on a
wrong reading and has been withdrawn.
