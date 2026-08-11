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
