# Lost orders post-mortem — November 1–21 2026 (CEO, for Alex + Founder)
Source: Shopify Admin, all 184 orders created Nov 1–21 (pulled Nov 21). Read-only.

## Headline
- 184 orders → **12 are internal TEST orders** (keychain/WhatsApp flow tests, Founder's account, cities "test"/"asdasd") → **172 real**.
- 5 cancelled orders were **replaced** by a new order from the same customer (not lost).
- **Truly lost: 26 of 172 = 15.1% (Rs 105,544 of Rs 929,944 = 11.3%)** vs Jan–Oct 33.5%. 27 COD orders still in transit → final will be a bit higher.
  - Cancelled before dispatch: 17 (Rs 71,224) — most within 0–2h of ordering (changed mind) or no reason recorded.
  - Refused at the door: 9 (Rs 34,320) — **7 of 9 came from Meta ads** (H1 Mocha ×3, gloves ads ×2, catalogue, S2 video), cheap wallet/glove impulse buys.

## Where the leak is
| Segment | Orders | Lost | Rate |
|---|---|---|---|
| Inside our 9 ad cities | 121 | 16 | **13%** |
| **Outside the 9 cities** (Chishtian, Taunsa, Bhiria, Mardan, Kasur, Khanewal, Toba Tek Singh…) | 51 | 15 | **29%** |
| From Meta ads | 88 | 16 | 18% |
| From Google | 45 | 6 | 13% |
| Direct | 29 | 3 | 10% |
- 30% of orders come from OUTSIDE the 9 cities even though ads target only 9 cities: ad sets use location type "home + recent + frequently in" (travellers) and catalogue/organic reach.
- **WhatsApp confirmation reply rate is only ~18%** (26 of 144 shipped orders confirmed). Confirmed orders refused 1/26 (4%); unconfirmed 8/118 (7%).
- Data quality: staff mark door refusals as cancel reason **"FRAUD"** (all 9) and pre-dispatch cancels as "CUSTOMER" with no note → we can't see WHY.

## Recommendations (for the Founder's yes; Alex lens below)
1. **Call before dispatch** (Ahsan, ~2–3 calls/day): any COD order that is (a) outside the 9 cities OR (b) not WhatsApp-confirmed within 12h → one call; no answer after 2 tries = hold, don't ship. Free; directly attacks the 29% segment.
2. **Ads: location type "home" only** (drop "recent/frequently in") on all ad sets → fewer out-of-area impulse orders. Targeting change, no spend change.
3. **Record the real reason** on every cancel (SOP for Tahir/Ahsan: "changed mind / price / duplicate / unreachable / refused-no reason / wrong item"); stop using "FRAUD" for refusals.
4. **Tag test orders** `TEST` and never create them on the live checkout without the tag (12 this month polluted the numbers).
5. Re-read Dec 1 when the 27 in-transit orders resolve.

## [Alex lens]
The bucket is less leaky than we feared: 15%, not 33%. The confirmations are working. What's left is concentrated: cheap impulse buys from ads, shipped to towns outside our 9 cities, from people who never answer WhatsApp. Don't fix the whole business, fix that segment: call before you ship, and stop paying Meta to find travellers. One thing this week: Ahsan calls every unconfirmed out-of-area order before it leaves.
