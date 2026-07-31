# Road to PKR 1,000,000 — August 2026

Researched Aug 1 2026 while the lookalikes populate. Every number is either from
the store/ad account or a cited external benchmark. Nothing here is guesswork
dressed as insight.

---

## 1. The framing is wrong, and that is good news

**PKR 1M is not a stretch target. It is a recovery.**

| Month | Net revenue | Orders | AOV |
|---|---|---|---|
| **Aug 2025** | **1,252,127** | 301 | 5,547 |
| Sep 2025 | 1,244,387 | 183 | 8,369 |
| Oct 2025 | 1,091,333 | 213 | 6,433 |
| **Nov 2025** | **1,727,910** | 405 | 5,456 |
| Dec 2025 | 1,638,722 | 305 | 6,379 |
| Jan 2026 | 1,309,389 | 395 | 4,819 |
| Feb 2026 | 918,438 | 299 | 5,395 |
| Mar 2026 | 1,065,283 | 329 | 3,932 |
| Apr 2026 | 902,107 | 196 | 6,036 |
| May 2026 | 844,963 | 237 | 4,381 |
| Jun 2026 | 849,549 | 212 | 5,474 |
| **Jul 2026** | **465,245** | **155** | **4,415** |

Six of the last twelve months cleared 1M. **August 2025 did 1.25M** — so the
target is *below* the same month last year. July 2026 was the worst month in the
window: down 45% on June and **63% year-on-year**.

The question is not "how do we do something we have never done". It is "what
broke between April and July".

## 2. What broke: traffic

| Month | Sessions | Unique visitors |
|---|---|---|
| Mar | 27,598 | 22,473 |
| Apr | 16,745 | 13,767 |
| May | 13,571 | 10,706 |
| Jun | 12,843 | 10,083 |
| **Jul** | **11,882** | **9,545** |

**Down 29% since April.** Orders track it almost exactly (196 → 155). This is a
top-of-funnel volume problem, not a conversion problem — and it is why
retargeting cannot be scaled to fix it (see `ADS_PLAN_AUG26.md` §8).

## 3. The arithmetic to 1M

July: ~684,000 gross → **219,000 lost to returns** → 465,245 net.
**Returns are consuming 32% of revenue before anything else happens.**

To reach **1,000,000 net**:

| Return rate | AOV | Orders needed | vs July's 155 |
|---|---|---|---|
| 32% (today) | 4,415 | **333** | +115% |
| 18% (achievable) | 4,415 | **276** | +78% |
| 18% | 5,500 (historical) | **222** | **+43%** |
| 15% | 5,500 | **214** | +38% |

**No single lever gets there. The combination does** — and the order-count
increase required drops from +115% to +43% once refusal and AOV are fixed. That
is the whole strategy: fix the two multipliers first so the traffic recovery has
less work to do.

---

## 4. 🔴 FREE SHIPPING THRESHOLD IS SET BELOW AOV — fix today

**Current threshold: PKR 2,500. Current AOV: PKR 4,415.**

The threshold sits **43% BELOW** average order value, so essentially every
customer already qualifies. It is doing **nothing** — no nudge, no basket
building, while giving away shipping on orders that would have paid it.

Benchmark: the optimal threshold is **15–30% ABOVE** current AOV, and delivers a
**15–25% AOV lift**, visible within 7–14 days.

**Recommended: PKR 5,200–5,700.** At the midpoint, a 15% AOV lift takes 4,415 →
~5,077 with zero extra ad spend.

⚠️ Requires changing the Shopify shipping rate AND the copy on
`snippets/shipping.liquid`, `snippets/returns.liquid`, the footer, and the
`docs/legal/shipping-policy.html` already pasted into Shopify. **Do not change
one without the others** — a policy that contradicts the storefront is the
problem we just spent an evening fixing.

## 5. Refusal — the biggest single lever, already half-built

External benchmarks for Pakistan:
- National e-commerce RTO: **18–20%**
- COD specifically: **20–40%**
- **Prepaid: 5–15%**

**Kordovan sits at ~32–41% — the worst end of the COD band.**

Published result for the exact intervention already built: WhatsApp order
confirmation before dispatch plus automated out-for-delivery notification takes
**30% RTO down to 15–18% within the first month**.

At July volume that alone is worth **~PKR 96,000/month**, and it scales with
every order added afterwards. **Nothing else in this document has a better
return on effort, and the machinery is already live.**

Second-order moves, in order of leverage:
1. **Prepaid conversion.** Prepaid refuses at 5–15% vs COD's 20–40%. `PAYONLINE10`
   exists and is delivered via the WhatsApp confirmation — measure its uptake and
   consider raising the discount if it converts COD orders to prepaid.
2. **Address/phone screening before dispatch** — incomplete addresses and
   unreachable numbers are the highest-risk cohort.
3. **Per-product refusal is not uniform** — Bastion 48%, Aristocrat 7%. Product
   mix is a refusal lever (see `ADS_PLAYBOOK_PK.md` §6).

## 6. AOV — three tactics, benchmarked

| Tactic | Expected lift | Time to signal |
|---|---|---|
| Free shipping threshold (above) | **15–25%** | 7–14 days |
| 2 curated bundles on top SKUs | **12–18%** (+22% PDP CVR) | 30–60 days |
| Post-purchase upsell on thank-you page | **10–15%**, ~18% uptake | immediate |

Bundle candidates from actual data: wallet + keychain (Leather Key Chain, 61
units/yr) or wallet + belt. A 2-item order fixes the cold-traffic economics
faster than any targeting change — cold CPA is fixed per order, so every rupee
of AOV is margin.

Implement **one at a time, two weeks apart**, or you cannot attribute the lift.

## 7. Meta findings from the account itself

### Catalogue is healthy — and unused
Live pixel `1865080707652548` matches catalogue items at **99.94%**. Purchase,
AddToCart and ViewContent all firing with correct content IDs. That means
**Dynamic Product Ads / Advantage+ Catalogue ads are fully available and are not
being run.** For a 169-product store this is the standard highest-ROAS campaign
type in e-commerce, and it is exactly what the user wants the Retarget campaign
to be.

### Dead pixel is polluting catalogue health
`652254084055676` ("Kordovan 2025's Pixel (DO NOT USE)") is still **attached to
the catalogue**, match rate **0%**, and throws three `must_fix` missing-event
errors. It is what makes the catalogue report as unhealthy.
**Action: detach it from the catalogue.** Zero risk — it has never sent an event.

### Remaining real issue
`catalog_has_da_visibility_issues` — some items are not visible to ads. Worth a
pass through Commerce Manager before running catalogue ads.

---

## 8. Priority order for August

| # | Action | Effort | Expected |
|---|---|---|---|
| 1 | **Finish WhatsApp** — confirm/cancel proven, then watch refusal | done, needs monitoring | **32% → 18% returns ≈ +96k/mo** |
| 2 | **Free shipping threshold → 5,200–5,700** | 1 hour incl. copy | **AOV +15–25%** |
| 3 | **Detach dead pixel from catalogue** | 5 minutes | unblocks catalogue ads |
| 4 | **Launch TOF** (built, paused) + recover traffic | ready | orders |
| 5 | **Catalogue/DPA retargeting campaign** | half a day | typically best ROAS in account |
| 6 | **Post-purchase upsell** | 1 hour | AOV +10–15% |
| 7 | **Two bundles** | half a day | AOV +12–18% |
| 8 | Prepaid push via `PAYONLINE10` | monitoring | refusal 20–40% → 5–15% on converted orders |

**Items 1, 2 and 3 are the month.** They are cheap, fast, and they multiply
everything the ad spend then buys. Doing them before scaling budget is the
difference between profitable growth and expensive growth.

---

## Sources
- [DHL Pakistan — How Pakistani E-Commerce Sellers Can Reduce COD Returns](https://www.dhl.com/discover/en-pk/e-commerce-advice/e-commerce-best-practice/subscription-marketing/how-pakistani-e-commerce-sellers-can-reduce-cod-returns)
- [COD Return Rate in Pakistan: What's Normal & How to Fix It](https://trackmyorder.pk/blog/shopify-tips/cod-return-rate-pakistan-shopify)
- [Cash on Delivery in Pakistan: Rules, Fraud Prevention & How to Cut Your Return Rate](https://muhammadasad.com.pk/cod-pakistan-rules-fraud-prevention/)
- [The Complete Guide to Reducing RTO in COD E-commerce](https://www.egrow.com/en/blog/the-complete-guide-to-reducing-return-to-origin-rto-in-cod-e-commerce-2026)
- [Shopify — Average Order Value: Formula and 7 Ways (2026)](https://www.shopify.com/blog/average-order-value)
- [Shopify Free Shipping Statistics 2026 — Threshold Data & AOV Impact](https://easyappsecom.com/guides/shopify-free-shipping-statistics)
- [How to Increase AOV on Shopify With Bundles & Upsells](https://www.qeretail.com/blog/increase-aov-on-shopify)
