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

## 4. 🔴 Three deleted product URLs are 404ing

Confirmed against Shopify — these handles return null, so the URLs are dead
while Google still ranks them:

| Dead URL | Was worth | Suggested redirect |
|---|---|---|
| `/products/copy-of-the-access-minimal-wallet` | **21 clicks/mo, 236 impressions, position 6.9** | `/collections/mens-leather-wallets` |
| `/products/durable-mens-leather-gloves-light-brown-kordovan-1` | 4 clicks, 454 impressions | `/products/durable-mens-leather-gloves-light-brown-kordovan` |
| `/products/new-wallet` | 4 clicks | `/collections/mens-leather-wallets` |

Two others that dropped out of the top 40 were checked and are **fine** —
`crazy-horse-long-wallet-unisex-kordovan-light` and
`copy-of-the-travel-mate-trolley-bag` both still exist.

Pointing the first one at `mens-leather-wallets` is deliberate: it sends the
equity to the page that is already ranking rather than letting it die.

The store already has a redirect practice (10+ existing redirects), so this is
consistent with how it is normally handled.

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
