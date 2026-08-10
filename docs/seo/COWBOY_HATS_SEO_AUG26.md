# Cowboy hats SEO — Aug 10 2026

Second SEO pass after jackets. **Different problem, different fix**: hats
already rank well. Jackets had a CTR problem at page-two positions; hats have
good CTR at position 5 and need depth to climb, plus a stock problem that
outweighs everything on this page.

## 1. The data — 12 months, queries containing "hat"

| Query | Impressions | Position | CTR | Clicks |
|---|---|---|---|---|
| **cowboy hat** | **5,423** | 5.55 | **6.69%** | 363 |
| cowboy hat pakistan | 1,478 | 4.61 | **23.3%** | 345 |
| **cow boy hat** *(misspelling)* | **914** | 5.65 | **5.69%** | 52 |
| cowboy hats | 814 | 5.62 | 8.48% | 69 |
| cowboy hat price in pakistan | 790 | 2.93 | 21.5% | 170 |
| leather hats | 579 | 7.67 | 5.01% | 29 |
| **leather hat** | 551 | **3.80** | **5.81%** | 32 |
| cowboy hats pakistan | 523 | 3.86 | **29.1%** | 152 |
| hat price in pakistan | 186 | **3.56** | **1.08%** | 2 |

~13,500 impressions and ~1,450 clicks a year.

### The pattern
**Pakistan-qualified queries convert brilliantly (23–29% CTR). Generic ones do
not (5–7%).** For `cowboy hat` the SERP is full of international retailers, so
a Pakistani shop earns fewer clicks at the same position — that part is
structural and not fixable with a title.

But two are genuinely underperforming for their position and are fixable:
- `leather hat` — **position 3.80, 5.81% CTR.** Should be 10–12%.
- `hat price in pakistan` — **position 3.56, 1.08% CTR.** Should be ~10%.

`cow boy hat` at 914 impressions is a misspelling worth keeping in mind — it
cannot go in a title without looking illiterate, but Google matches it to the
correct spelling anyway.

## 2. What was wrong

| Defect | Count |
|---|---|
| **Products with NO SEO title or description at all** | **4 of 6** |
| Product body descriptions **identical, word for word** | **6 of 6** |
| `productType` inconsistent (`Hats` ×5, empty ×1) | 1 |
| Collection SEO title over 60 chars (truncated) | 1 |
| Collection body carried `&amp;nbsp;` artifacts and an empty `<!---->` | 1 |

Six products sharing one description verbatim is duplicate content inside a
single collection — the weakest possible signal for a category that is trying
to rank first.

## 3. What was applied

**Collection** — new title `Leather Cowboy Hats in Pakistan — From Rs 4,800 |
Kordovan` (57 chars, carries the price the highest-intent queries ask for), new
meta, and a rewritten body covering:
- **How to size a hat** (measure above the ears, size up between sizes) — the
  single most useful thing on a hat page and the reason people abandon
- Style guide: crushable / suede / studded / Clifford
- What a leather hat should cost in Pakistan, and what under Rs 2,500 means
- Care — crown-down storage, drying, conditioning
- **Karachi shop mention** for `cowboy hats near me` and `cowboy hat karachi`
- Internal links to leather caps and accessories

**All 6 products** — unique SEO title, unique meta with price, and a genuinely
different body per product written around what actually distinguishes it
(crushable vs suede nap vs crazy-horse patina vs the heavier Clifford build).
`productType` normalised to `Hats`.

⚠️ **Free delivery is only claimed on the two Rs 10,500 Clifford hats.** The
threshold is Rs 5,500, so the Rs 4,800 and Rs 9,000 hats do not qualify and
their copy says cash on delivery only. Hats are **not** prepaid-only — that
restriction applies to jackets, so COD is stated correctly here.

## 4. 🔴 The stock problem outweighs all of the above

| Product | Price | Total inventory | First variant buyable |
|---|---|---|---|
| Crushable Western Cowboy Hat | 4,800 | 15 | ❌ **no** |
| Suede Western Cowboy Hat, Brown | 4,800 | **0** | ❌ **no** |
| Studded Band, Burgundy | 9,000 | **0** | ❌ **no** |
| Clifford Faded Black | 10,500 | 1 | ✅ |
| Clifford Rustic Brown | 10,500 | 3 | ✅ |
| Black Stripe Cowboy Hat | 4,800 | 1 | ❌ **no** |

**Four of six are unbuyable. Two are at literal zero. Total stock across the
category is about 20 units.**

These are `tracksInventory: true` with real zeros — unlike the jackets, where
zero meant "untracked, always available". This is genuine sold-out.

The category pulls **2,027 impressions a month at position 5 with 13.2% CTR**,
and most of that traffic lands on something it cannot buy.

**Question for the user: are hats made to order like the jackets, or real
stock?**
- If made to order → untrack inventory as we did for jackets and all six
  become buyable immediately.
- If real stock → the category needs restocking before any ranking gain is
  worth having.

## 5. Honest ceiling on "rank #1"

The on-page work is done to standard. It does not guarantee position 1, and it
would be dishonest to claim it does:

- `cowboy hat` at position 5.55 is competing with international retailers who
  have far more domain authority. On-page work can realistically move this to
  3–4, not 1.
- `cowboy hat pakistan` at 4.61 and `cowboy hats pakistan` at 3.86 are
  genuinely winnable — the intent is local and the competition is thinner.
- `leather hat` at 3.80 with 5.81% CTR should improve on CTR alone.

**And ranking first while four of six products are sold out would make things
worse, not better** — higher impressions against an out-of-stock page trains
Google that the result disappoints.

Remaining gaps not addressed here: no image alt-text audit on hat images, no
FAQ schema on the collection (the theme has no collection FAQ block), and the
messy handle `copy-of-kordovans-crushable-...` which is not worth the redirect
risk to change.
