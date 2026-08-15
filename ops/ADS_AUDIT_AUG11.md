# Ads audit — Aug 1–10 2026 vs Jul 1–10 2026

Pulled Aug 11. Meta account `995683712074843` ("Kordovan 2025"), Shopify order
data by **order creation date** (not ShopifyQL reversal date, which attributes
a cancellation to the day it was cancelled rather than the day the order came
in).

## 1. The raw comparison

| | Jul 1–10 | Aug 1–10 | Δ |
|---|---|---|---|
| **Meta spend** | **PKR 8,938** | **PKR 54,427** | **+509% (6.1x)** |
| Meta-claimed purchases | 29 | 44 | +52% |
| Meta-claimed value | 118,999 | 186,878 | +57% |
| Meta-reported ROAS | 13.31x | 3.43x | −74% |
| Meta CPA | 308 | 1,237 | +301% |
| CPM | 250 | 402 | +61% |
| CTR | 4.90% | 3.23% | −34% |
| **Shopify orders placed** | **57** | **58** | **+1** |
| Order value placed | 293,630 | 233,921 | −20% |
| Cancelled | 17 (29.8%) | 10 (17.2%)¹ | — |
| **Value surviving** | **218,982** | **168,171**¹ | **−23%** |
| AOV placed | 5,151 | 4,033 | −22% |
| Sessions | 3,391 | 5,516 | +63% |
| Conversion rate | 1.42% | 1.02% | −28% |

¹ **August has not settled.** 17 of 58 August orders are still PENDING (COD in
transit). Every July order is PAID or VOIDED. At the historical rate another
~5 orders / ~15,000 will cancel, so the real August surviving figure is lower.

**Ad spend as a share of surviving revenue: 4.1% → 32.4%.**

## 2. 🔴 But the headline number is misleading — check the big orders first

The obvious read is "6x the spend, 23% less money". That is arithmetically true
and it is not the real cause.

| Orders ≥ PKR 10,000 that survived | Count | Value |
|---|---|---|
| Jul 1–10 | 5 (11,000 · 17,600 · 21,000 · 22,035 · 28,600) | **100,235** |
| Aug 1–10 | 2 (10,500 · 11,500) | **22,000** |

**That single difference — 78,235 — is larger than the entire revenue gap of
50,811.** July had five big-ticket orders; August had two.

Strip the ≥10,000 orders out and the picture inverts:

| Normal orders only (< PKR 10,000, surviving) | Jul 1–10 | Aug 1–10 | Δ |
|---|---|---|---|
| Orders | 35 | **46** | **+31%** |
| Revenue | 118,747 | **146,171** | **+23%** |
| AOV | 3,393 | 3,178 | −6% |

So the ads did what ads do: **+11 everyday orders, +27,424 revenue.** What they
did not do is replace five large organic/direct purchases that simply did not
recur.

### The marginal maths, stated plainly
**+45,489 in extra ad spend bought +11 orders and +27,424 in revenue.**
Marginal CPA ≈ **4,135/order**. Marginal ROAS ≈ **0.60x** — before cost of
goods. The incremental spend lost money at any margin.

⚠️ This attributes the whole normal-order increase to ads and none of the
big-order absence to them. Both are assumptions. The direction is not in doubt;
the exact figure is.

### Also: July 1–10 was not a fair "ads" baseline
Only the **Retarget** campaign ran in that window — 8,938 spend, no
prospecting at all. Retargeting always reports a high ROAS because it bills for
demand that largely already exists. **13.31x vs 3.43x is retargeting-only
versus a full funnel, not a decline in skill.**

## 3. Where the money went — Aug 1–10 by ad set

| Ad set | Spend | Purch | CPA | Meta ROAS | CPM | CTR | Freq |
|---|---|---|---|---|---|---|---|
| **TOF-A Mocha Mate** | 15,112 | 18 | **840** | 4.21x | 479 | 1.68% | 1.41 |
| Retarget | 14,084 | 13 | 1,083 | 4.15x | 307 | 4.55% | **3.37** |
| **🔴 TOF-B Razor** | **13,915** | **3** | **4,638** | **0.59x** | **559** | 1.77% | 1.36 |
| DPA Catalogue | 10,119 | 10 | 1,012 | **5.60x** | 327 | 4.07% | **4.59** |
| Cold LLA (paused) | 1,197 | 0 | — | — | 605 | 2.53% | 1.07 |

**TOF-B took 26% of the budget and returned 4% of the value.** 13,915 spent,
8,150 back.

## 4. The Aug 9 budget cut is working — 2-day read

| Ad set | Spend | Purch | CPA | ROAS | Freq (was) |
|---|---|---|---|---|---|
| DPA | 2,145 | 4 | **536** | **9.42x** | 2.15 (4.59) |
| Retarget | 2,087 | 2 | 1,043 | 5.87x | 1.82 (3.37) |
| TOF-A | 3,112 | 1 | 3,112 | 1.69x | 1.15 |
| TOF-B | 1,908 | **0** | — | — | 1.14 |

Budgets landed correctly (~1,000/day each, TOF-A held at 1,500 as the control).
Frequency on DPA and Retarget dropped hard and both improved sharply — the
saturation call was right. **Two days is not a result**, but nothing here
argues for putting the money back.

### 🔴 The new Razor video is doing worse than the one it replaced
CTR on TOF-B over the full 10 days was 1.77%. On Aug 9–10, after the swap:
**0.98%**, and zero purchases. Weak evidence at two days — but it is pointing
the wrong way, and the old video was already killed for underperforming.

**One confounder that is our fault, not the creative's:** The Razor's PDP was
missing the `fits` band entirely until Aug 10. TOF-B was sending paid traffic
to the thinner of the two wallet pages the whole time. Mocha Mate had the band;
Razor did not. That is now fixed, so the next few days are the first clean
read on the creative.

## 5. Funnel — where the extra traffic died

| | Jul 1–10 | Aug 1–10 |
|---|---|---|
| Sessions | 3,391 | 5,516 (+63%) |
| Added to cart | 157 (4.63%) | 196 (3.55%) |
| **Reached checkout** | **142 (4.19%)** | **95 (1.72%)** |
| Completed checkout | 48 | 56 |
| **Checkout → purchase** | **33.8%** | **58.9%** |

Two opposite things happened:
- **Reaching checkout collapsed** — 142 to 95 on 63% more traffic. Paid traffic
  browses and leaves. Cart-add rate fell too.
- **Completion nearly doubled** once they got there, 33.8% → 58.9%. That is the
  WhatsApp abandoned-checkout recovery earning its keep.

## 6. Order source

| Source | Jul 1–10 | Aug 1–10 |
|---|---|---|
| Direct / unattributed | **30 orders · 138,692 net** | 15 · 37,443 |
| Social (Meta) | 15 · 33,499 | **38 · 88,829** |
| Search | 12 · 16,351 | 5 · **−4,701** |

Some of the direct → social shift is attribution, not real. But search going
**negative** is real: refunds on search-sourced orders exceeded new search
revenue in the window.

## 7. Meta is claiming almost everything

| | Meta claims | Store took | Meta's share |
|---|---|---|---|
| Jul 1–10 | 29 purchases | 57 orders | 51% |
| Aug 1–10 | 44 purchases | 58 orders | **76%** |

Meta's attributed value for August (186,878) is **80% of every rupee the store
placed** (233,921), including organic, direct and search. Keep using the ~1.8x
haircut from `AUGUST_TEST_PLAN.md` §1 — if anything August argues for a
steeper one.

## 8. What this changes

1. **Kill or rebuild TOF-B.** 13,915 for 8,150 over ten days, zero in the last
   two, CTR halved after the swap. Give it 3–4 more days now that the Razor PDP
   is fixed, then cut it if CPA is still over 2,500. Its 1,000/day is the
   budget for test slot 1 (broad vs LLA) in the August plan, which has not
   started.
2. **DPA is the best rupee in the account** — 5.60x over ten days, 9.42x since
   the frequency came down. It was being throttled by saturation, not by
   audience quality.
3. **Do not read the revenue drop as ad failure.** It is mostly five missing
   big-ticket orders. The genuine ad problem is smaller and specific: marginal
   ROAS around 0.60x on the incremental spend.
4. **Big-ticket orders are the actual lever.** Five orders swung 78,235 — more
   than the entire month's ad spend to date. Jackets at 22,000–35,000 are
   exactly that order, and the season starts in about eight weeks.
5. August is still a testing month. The budgets are right where they should be.

---

# Aug 11 — TOF-B paused, and the case for a catalogue TOF

`120254219933170428` TOF-B Razor set to PAUSED on the user's call.

## Catalogue vs video for PROSPECTING — this account's own history

Lifetime 2026 (1 Jan – 10 Aug), campaign level.

**Catalogue creative, prospecting audiences**

| Campaign | Spend | Purch | CPA | ROAS | CPM |
|---|---|---|---|---|---|
| **Complete Web Cata** (LLA 1–10%, from 8 May) | 29,968 | 58 | **517** | **7.49x** | 254 |
| CBO TOP 1-2-3% LLA (cities 500k+, from Oct 25) | 53,542 | 75 | 714 | 5.41x | 265 |
| Complete web cata rerun (from 8 Jun) | 5,490 | 4 | 1,373 | 2.34x | 223 |

**Single-product video creative, prospecting audiences**

| Campaign | Spend | Purch | CPA | ROAS | CPM |
|---|---|---|---|---|---|
| Mocha mate | 27,687 | 26 | 1,065 | 2.88x | 301 |
| Razor | 28,060 | 24 | 1,169 | 2.44x | 385 |
| KV TOF Smart Wallets Aug26 | 29,027 | 21 | 1,382 | 2.47x | 514 |
| KV Cold Wallet Launch Jul26 | 23,496 | 11 | 2,136 | 1.53x | 543 |

**Catalogue prospecting: ~89,000 spend, 137 purchases, CPA ~650.
Video prospecting: ~108,270 spend, 82 purchases, CPA ~1,320.**

Roughly **half the CPA on comparable spend**, and the mechanism is visible in
the CPM column — catalogue formats bought impressions at 223–265, video at
301–543.

## Four caveats that will pull the number down

1. **The winners used the polluted lookalikes.** "Complete Web Cata" targeted
   LLAs of *Kodo Lifetime Customers* and *pixel Purchase* — order-placed seeds
   that included the COD refusers — and carried **no refuser exclusion**
   (it predates the Jul 8 audience build). Cancellation ran 30–36% then, so
   7.49x reported is nearer **~5x realised**.
2. **It ran `countries: ["PK"]`** — country-wide, against the current 9-city
   rule. City-only inventory is more competitive, so expect a higher CPM than
   the 254 it enjoyed. The better precedent is the CBO campaign, which used
   `custom_locations` at min_population 500,000 and still returned **5.41x over
   53,542** — geographically disciplined and a much larger sample.
3. **`advantage_audience: 1` was ON in every catalogue winner.** The current
   TOF-A/TOF-B ad sets run it at 0.
4. **Catalogue hygiene.** Product set `608788148654460` (the one actively
   advertised) has **137 items blocked**: 135 out of stock, 5 missing an image,
   2 each missing title / availability / condition / price.

## ✅ Jackets are already live in the catalogue

Checked directly: **154 jacket items, all `availability: in stock`.** The Aug 9
inventory untracking propagated through to Meta. The highest-AOV segment in the
range (22,000–35,000) is fully eligible for dynamic ads right now, ahead of the
season. That is the single best argument for putting catalogue creative in
front of cold traffic.

⚠️ Could not enumerate the 135 out-of-stock items — `ads_catalog_search_product`
returns a spurious "Object with ID 'N'" error on `{}` and on `availability`
filters (the N increments per call, so it looks like a bug in the connector,
not a permissions problem). Name filters work. Worth a manual look in Commerce
Manager.

## Proposed replacement for TOF-B's freed 1,000/day — NOT created, awaiting approval

| Setting | Value |
|---|---|
| Creative | Catalogue / DPA — no video needed |
| Audience | Value-based LLA 1% + 3% of **Delivered Repeat Buyers** (`120253661268330428`, `120253661269660428`) — the clean Jul 8 seed |
| Exclude | `120253660257910428` KV — COD Refusers EXCLUDE, plus existing buyers |
| Geo | the 9 cities, **no radius** |
| Age | 18–65, all genders |
| Optimisation | OFFSITE_CONVERSIONS (Purchase) |
| Budget | 1,000/day |

Realistic expectation: **3–5x, not 7.49x** — the geo is tighter and the seed is
smaller (though cleaner). If it beats TOF-A's 4.21x at a lower CPA it becomes
the September prospecting engine.

It also part-answers Test 1 in `AUGUST_TEST_PLAN.md`: holding the audience
constant against TOF-A and changing only the creative format is a cleaner test
than broad-vs-LLA, and it uses budget that is now idle.

## Built Aug 11 — TOF-C catalogue, PAUSED

User chose the whole catalogue: *"it targets people and shows them exactly
what theyre looking for."* Worth noting the nuance — on **cold** traffic DPA
does not replay what someone browsed (they have never been to the site); Meta
picks from its own interest signals. The per-person-browsing behaviour is a
retargeting property and belongs to the BOF DPA set. Whole catalogue is still
the right call: a wider set gives the algorithm more to match against.

| Entity | ID | State |
|---|---|---|
| Campaign `KV \| TOF \| Catalogue All Products \| Aug26` | `120254472798420428` | PAUSED, OUTCOME_SALES, ABO |
| Ad set `TOF-C \| Catalogue All Products \| LLA 1%+3% Value` | `120254472805020428` | PAUSED, PKR 1,000/day |
| Creative `CR_TOF_Catalogue_AllProducts_Cold_v1` | `1021882213813646` | built |
| Ad `AD_TOF_Catalogue_AllProducts_Cold_v1` | `120254472920370428` | created Aug 11, PENDING_REVIEW |

Ad set verified by read-back: 9 cities **with no radius**, 18–65,
LLA 1% `120254216730060428` + LLA 3% `120254216735280428`, excluding
Purchasers 180D + **COD Refusers** + the seed audience, `advantage_audience: 0`,
OFFSITE_CONVERSIONS, product set `608788148654460` (All Products),
pixel `1865080707652548`, attribution 1d view / 7d click. Mirrors TOF-A exactly
so the only variable is creative format.

### 🔴 Blocker: the ad cannot be created from here
`ads_create_ad` fails with *"Instagram Account Is Missing"* because the ad set
includes Instagram placements and the creative carries no Instagram identity.
`ads_get_ig_accounts` returns `[]` for this account — the connector appears to
lack `instagram_basic`, so the IG account ID cannot be read. Passing the Page ID
as `instagram_user_id` is rejected ("must be a valid Instagram account id").

**Two ways to finish**, both outside this session:
1. Grant the Meta connector Instagram permission, then the ad can be created here.
2. In Ads Manager: duplicate the existing `AD_BOF_DPA_AllProducts_v1` ad into
   ad set `120254472805020428` — it already carries a valid IG identity — then
   replace its primary text with the cold copy below.

### Copy for the ad (the BOF text is wrong for cold traffic)
The BOF creative opens *"Still thinking about it? It is still here."* — that
addresses someone who already visited. Cold copy:

> Handcrafted in Pakistan from genuine full-grain leather — wallets, bags,
> jackets, belts and shoes made to be carried for years, not seasons.
>
> Lifetime craftsmanship warranty. 7-day returns. Free delivery on orders over
> Rs 5,500.

Headline `{{product.name}}`, description `{{product.price strip_zeros}}`,
CTA Shop Now.

### ⚠️ Two things to fix on the existing BOF DPA ad too
1. **It promises cash on delivery across All Products** — *"cash on delivery
   anywhere in the country — you pay when it reaches your door"* — but the same
   product set contains **30 prepaid-only jackets**. That is a false promise on
   those cards, and it is live right now. The new TOF copy above deliberately
   omits any blanket COD claim.
2. **UTMs.** `ads_create_creative` exposes no `url_tags`, and for catalogue ads
   UTMs must go there, not in `link_url` (product URLs override it). Paste into
   the ad's **URL parameters** field:
   `utm_source=facebook&utm_medium=paid&utm_campaign=tof_catalogue_all_aug26&utm_content={{ad.name}}&utm_term={{adset.name}}`

### Ad created after all — Aug 11

The Instagram blocker was worked around: the ad set was temporarily set to
Facebook-only placements, the ad was created, then the full Facebook +
Instagram placement set was restored. Verified by read-back afterwards —
publisher_platforms `facebook, instagram`, all 7 FB positions and all 6 IG
positions present, 9 cities intact, exclusions intact.

**Nothing can spend:** campaign `status: PAUSED`, ad set `status: PAUSED`.
The ad shows `PENDING_REVIEW`, which is just Meta reviewing the creative — it
gets that out of the way before launch.

**The one thing still to do by hand: the Instagram identity.** The ad currently
has a Facebook Page identity only. Opening the ad in Ads Manager and choosing
the Instagram account is what makes the IG placements deliver.

### 🔴 UTMs cannot be written through this connector — confirmed, not assumed
`url_tags` is a field on the **AdCreative** object. `ads_create_creative`
exposes no `url_tags` parameter; `ads_creative_update` can only change name,
status and adlabels ("media, copy, link, CTA are immutable"); and
`ads_update_entity` on the ad object rejects it, because the Ad object has no
such field. Putting the UTMs in `link_url` does not work for catalogue ads —
product URLs from the feed override it.

So it has to be pasted into the ad's **URL parameters** field, which sits on the
same screen as the Instagram account selector:

```
utm_source=facebook&utm_medium=paid&utm_campaign=tof_catalogue_all_aug26&utm_content={{ad.name}}&utm_term={{adset.name}}
```


---

# 🔴 Statistical correction — Aug 11, after the quantitative review

Two claims in this document do not survive a proper noise analysis.

**1. "DPA is the best rupee in the account" — not supportable.**
True-ROAS 95% intervals (compound Poisson, CV of order value 0.60):
TOF-A 2.46–7.22 · Retarget 2.20–7.82 · DPA 2.72–11.5 · TOF-B 0.16–2.21.
The first three overlap almost entirely — TOF-A vs Retarget p = 0.37,
TOF-A vs DPA p = 0.136. **Only TOF-B separates (p = 0.004).**
Correct statement: TOF-B was measurably bad; the other three are
indistinguishable. Separating them needs ~41 days for a 2x gap.

**2. The Aug 9–10 two-day read was noise.**
Minimum detectable ROAS ratio at 2 days is 21.5x; the observed spread was 5.6x.
Section 4's numbers were labelled "two days is not a result" but were still used
to argue the saturation call was working. They cannot carry that. The frequency
hypothesis may be correct — this is not evidence for it.

**3. Every ROAS in this document should be multiplied by 0.403** to reach true
delivered ROAS ((1 − 0.235 cancellation) / 1.9 attribution). TOF-A 4.21 → 1.70,
Retarget 4.15 → 1.67, DPA 5.60 → 2.26, TOF-B 0.59 → 0.24. Two independent
reviews put reported break-even between 3.5x and 4.52x, which places TOF-A and
Retarget at or below it. Unverified until real COGS is supplied.

Full working in `ADS_AGENT_SPEC.md` §A–H.
