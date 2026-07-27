# Meta Ads — Wallet Launch (Jul 2026)

Account: **Kordovan 2025 · 995683712074843** (PKR) — the ONLY account in scope.
Pixel/dataset: `1865080707652548`. Budget: **PKR 5,000/day** (~150k/month).

## Structure (both created PAUSED — user adds video creative, then publishes)

| | Campaign ID | Ad Set ID | Budget/day |
|---|---|---|---|
| **Cold — Wallet Launch** | `120254085340610428` | `120254085361120428` | PKR 3,800 |
| **Retarget — Warm** | `120254085373920428` | `120254085374720428` | PKR 1,200 |

Both: OUTCOME_SALES · OFFSITE_CONVERSIONS (Purchase) · WEBSITE · ABO · autobid ·
attribution 7-day click + 1-day view · PK · age 20–55 · Advantage+ audience OFF.

**Cold targeting:** LLA 1% Value `120253661268330428` + LLA 3% Value `120253661269660428`
**Warm targeting:** ATC 180D `120252468021190428`, IC 180D `120252468024210428`,
ViewContent 90D `120252468026250428`, All Visitors 180D `120252468018150428`
**Excluded on BOTH (mandatory rule):** COD Refusers `120253660257910428` +
Purchasers 180D `120252468019140428`

## Ads — ALL 4 CREATED, ALL PAUSED (user adds video, checks, publishes)

| Ad ID | Ad name (= `utm_content`) | Ad set | Creative ID |
|---|---|---|---|
| `120254085488780428` | `AD_Bastion_Cold_PatinaAngle` | Cold | `981461181613343` |
| `120254085520050428` | `AD_Razor_Cold_RFIDHook` | Cold | `1050075114629389` |
| `120254085489810428` | `AD_Bastion_RT_StillHere` | Retarget | `1478447687652398` |
| `120254085492090428` | `AD_Razor_RT_FinishOrder` | Retarget | `1519494712778431` |

All: SHOP_NOW · `conversion_domain=kordovanleather.com` · image = the product's
Shopify hero shot, standing in as a placeholder until the user swaps in video.
Ad names are deliberately space-free so `utm_content` stays clean in analytics.

Destination links (the full UTM string is baked into each creative's link, so
nothing needs pasting into the "URL parameters" field):
- Bastion → `/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet`
- Razor → `/products/the-razor-rfid-smart-leather-wallet-kordovan`

## URL tracking — already appended to every ad's destination link
```
utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{placement}}&utm_adset={{adset.name}}
```
`{{placement}}` resolves to e.g. `Instagram_Stories`, `Facebook_Mobile_Feed`,
`Instagram_Reels`; `{{site_source_name}}` → `fb` / `ig` / `an` / `msg`.
Read in Shopify Analytics → Sessions by UTM, or GA4 → Traffic acquisition.
⚠️ The Marketing API does not read `link_url` back on SHARE creatives, so this
string could not be machine-verified after creation — eyeball it once in Ads
Manager (Ad → Destination → Website URL) before publishing.

## Copy per ad
- **Bastion cold** — "Built to Age, Not Wear Out". Patina/ageing angle; claims
  taken verbatim from the PDP (distressed cow leather, transparent ID window,
  cash-fold, handcrafted in Pakistan, lifetime warranty). Rs 2,500.
- **Razor cold** — "Slim, Leather, RFID-Safe". Skimming hook + elastic hold
  system + six finishes. Rs 2,450 vs Rs 2,999 compare-at (a real listed sale).
- **Bastion retarget** — "The Bastion — Still In Stock". Price reassurance, COD,
  free delivery over Rs 2,500.
- **Razor retarget** — "Your Razor Is Waiting". Colour choice + finish-the-order.

Every claim was checked line-by-line against the live Shopify description — no
"saddle-stitched" or blanket full-grain wording, per the sitewide claims rule.

## Products in scope (stock-led decision)
Bastion (127 units) + Razor (81, has 18% compare-at = sale angle). Luke (39)
optional 3rd for creative rotation. **Kodo Vertical 2.0 EXCLUDED — 14 units, Black 0.**

## Before publishing — user checklist
1. Swap the placeholder image for the video on each ad (video is the plan).
2. Confirm the Instagram identity on each ad. `ads_get_ig_accounts` returns `[]`
   for this account (missing `instagram_basic` grant on the API app), but Meta
   did mint an `effective_instagram_media_id` for all four creatives, so IG
   placements should deliver under the Page's linked IG account. Verify in the
   ad's Identity section rather than assuming.
3. Eyeball the destination URL + UTM string (see warning above).
4. Confirm both ad sets still exclude "KV — COD Refusers EXCLUDE" — mandatory.

Housekeeping: orphan creative `1824947595555604` (Razor cold v1, replaced for an
unsupported "hand-finished edges" claim) is unused and could not be deleted —
`ads_creative_delete` is not rolled out for this account. Ignore it; delete in
Ads Manager if the library gets noisy.

## Legacy "Retarget" campaign — audited + fixed Jul 26 2026
Campaign `120228534676850428` / ad set `120228534676860428`. Despite the name it
retargets NOTHING: no custom audiences at all, broad PK 18–65 with
`advantage_audience: 1`. It was running with **no COD-refuser exclusion**, i.e.
advertising to the 3,891 refusers — a direct breach of the locked ad rule.
**FIXED:** `KV — COD Refusers EXCLUDE 120253660257910428` added and the ad set
re-activated (the API force-pauses on a targeting edit — always re-activate and
verify). Purchasers 180D deliberately NOT excluded here: repeat buyers are worth
keeping in a broad/warm pool. Learning phase reset on the edit — its CTR 6.88% /
CPC PKR 4.12 will wobble for a few days before it settles.

## Attribution reality check (Jul 19–22 actuals)
Meta claimed **PKR 37,850** revenue on PKR 3,820 spend (~9.9x). Shopify attributes
only **7 orders / ~PKR 18,500** to Meta over the same window, 1 later cancelled →
real ROAS ≈ **4.3x**. Meta overstates ~2x via view-through credit on Google/direct
orders. **Budget against 4–5x, not the dashboard number.**

## Rules
- Days 0–3: no edits (every change resets learning).
- Day 4: kill ads with 0 ATC after PKR 1,500 spend.
- Day 7: winner gets own ad set; add 2 creative variants.
- Day 10: judge on **delivered vs cancelled in Shopify**, not Meta (Meta counts
  orders placed; ~40% COD refusal inflates it).
- Thresholds: CPA < PKR 800 viable · < 500 scale · ROAS >= 3x placed.
- Never put PAYONLINE10 in ad copy (leaks the prepaid discount — it is delivered
  via WhatsApp order confirmation only).
- Do NOT use the old polluted LLAs (Lifetime Buyers Jun26, Kordovan 2025 Dataset,
  Lifetime Kodo Customers) — seeded on pixel purchasers incl. ~40% refusers.

## Forecast (base case, from Jul 1–23 actuals: CPA 428 blended, AOV 4,525)
Cold CPA will run higher than blended; AOV drops to ~3,000 on 2,450–2,500 wallets.
Expect ~8 placed orders/day → ~5 delivered → ~PKR 450k delivered revenue/month
on 150k spend (~3x on money banked). Margin on the two SKUs decides profitability.

---

## 🔧 Optimisation pass — Jul 28 2026 (executed via API)

Two days of data on the Jul 26 launch. Creative left untouched at the user's
instruction; every change below is a delivery/budget setting.

### What the data said
Normalised to daily spend (new campaigns ran 2 days, old Retarget 7):

| Campaign | PKR/day | Placed CPA | Cost/LPV | CTR |
|---|---|---|---|---|
| Retarget (old, since May 2025) | ~919 | **804** | **7.10** | **4.34%** |
| KV \| Cold \| Wallet Launch | **4,168** | 2,084 | 47.91 | 1.58% |
| KV \| Retarget \| Warm 30-180D | 1,070 | 2,141 | 19.12 | 2.25% |

The proven winner was funded at a fifth of the cold campaign.

Cold placement split (PKR 8,336): **Reels took 65%** — Instagram Reels 3,214
(CTR 0.82%, PKR 64/LPV) and **Facebook Reels 2,233 (CTR 1.19%, PKR 93/LPV,
ZERO purchases)** — while Feed ran at PKR 33/LPV and CTR 2.49%. The account's
"low CTR" was largely a weighted average dragged down by Reels, not a creative
failure. Audience Network showed 45–50% CTR on single-digit impressions —
misclick traffic that also pollutes the optimiser's training signal.

### Changes made
1. **Cold ad set `120254085361120428`** → Advantage+ placements replaced with
   manual: Facebook (feed, profile_feed, marketplace, video_feeds, story,
   search, instream_video) + Instagram (stream, story, explore, explore_home,
   **reels**, profile_feed, ig_search). Drops **Audience Network, Messenger and
   Facebook Reels**. Instagram Reels KEPT — it produced 3 of the 4 purchases and
   4 conversions is far too thin to kill a converting placement on.
2. **Warm ad set `120254085374720428` + campaign `120254085373920428`** → PAUSED.
   It was bidding against the old Retarget for the same warm pool and losing
   2.7x on cost per landing page view.
3. **Retarget campaign `120228534676850428`** → daily budget PKR 900 → **2,100**
   (absorbs the paused warm budget).

⚠️ Threads placement could not be set — the API rejects both `feed` and
`threads_feed` for `threads_positions`. Threads is therefore excluded from the
cold ad set. It was PKR 63 of spend on 7 LPVs, so the loss is negligible, but
worth revisiting since its cost/LPV (9.05) was the best of any placement.

⚠️ **The budget edit force-paused the Retarget campaign** (`status_forced_to_
paused: true`) — the same API behaviour seen on the Jul 26 targeting edit.
Reactivated and verified ACTIVE. **Always re-read status after any edit.**

### Not done (deliberately held)
- Inverting the cold/warm budget split further — wait until the above lands so
  the improvement is attributable.
- Splitting `AD_Razor_Cold_RFIDHook` into its own ad set. It has a **32.3%
  3-sec-play rate vs Bastion's 11.3%** and half the cost per video view, but
  received only 1,103 of 16,150 impressions because Meta allocated on two days
  of purchase data. Same video, new container — worth doing next.
