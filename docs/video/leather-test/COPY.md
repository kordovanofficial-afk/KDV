# COPY — `leather-test`

**Ad name:** `AD_Jackets_Cold_LeatherTest_Sep26`
**Account:** `995683712074843` (Kordovan 2025, PKR) — the only account in scope
**Destination:** `https://kordovanleather.com/collections/mens-leather-jackets`

---

## Primary text

> Press real leather with your thumb and it springs back. Coated plastic keeps the crease.
>
> Look at the pores — on real hide no two are alike. A printed grain repeats itself, and once you see the tile you cannot unsee it. Turn the pocket out: real leather is fibrous suede underneath, plastic is woven mesh.
>
> Run all three on ours. The Iconic is full-grain sheepskin, made to order in Karachi, from Rs 22,000.
>
> Paid online at checkout — each one is cut for one customer. Free delivery nationwide. Lifetime craftsmanship warranty.

The first sentence is 92 characters — it survives the mobile truncation point intact, so
the test lands before anyone taps "See more".

### Alternates for testing

**B — the objection first**
> Everyone in this market says "genuine leather". So here are three tests you can run on any jacket before you pay for it, including ours. Thumb press: real leather springs back, plastic keeps the crease. Pores: real hide never repeats, print always does. Pocket lining: suede underneath, not mesh. The Iconic, full-grain sheepskin, made to order in Karachi, from Rs 22,000. Paid online at checkout — each one is cut for one customer, so it can never be resold.

**C — the price frame**
> A Rs 22,000 jacket should survive being inspected. Press it with your thumb — real leather springs back, coated plastic keeps the crease. Check the pores for a repeat. Turn the pocket out and look for suede, not mesh. Full-grain sheepskin, made to order in Karachi. Free delivery nationwide, lifetime craftsmanship warranty.

Test one at a time against the same creative. Do not run three ads at PKR 1,000/day —
you will split a budget that is already too thin to leave learning.

---

## Headline

> **Full-grain sheepskin. From Rs 22,000**

35 characters — under the 40-character point where Meta starts truncating in feed.

*Alternates:* `Three ways to spot fake leather` (31) · `Made to order in Karachi` (24)

## Description

> **Made to order in Karachi**

24 characters — safe under the 30-character link-description limit.

## Call to action

> **`SHOP_NOW`**

`LEARN_MORE` tests worth running as a variant: this is a cold audience being taught
something, and the softer verb sometimes lifts CTR on an explainer creative. It will lower
intent per click, so judge it on delivered orders in Shopify, never on Meta's click count.

---

## AI disclosure

> ### `self_ai_disclosure` = **`OPT_IN`**

Shot 07 (the Karachi workshop, 2.0s) is generated with LTX-2.3. Seven of the eight shots
are filmed on a phone with the real jacket, but one generated shot is one generated shot,
and the disclosure field is not a judgement call about proportion.

**If you film the real workshop instead** — 6 seconds of the actual cutting bench, which
is the recommended upgrade in BRIEF.md — the package becomes 8/8 filmed and this flips to
**`OPT_OUT`**. Given that this specific ad's entire argument is *"we are the ones who let
you check"*, being able to set `OPT_OUT` is worth a trip to the workshop.

---

## Compliance checklist — confirm every line before publishing

- [ ] **No discount code in the creative.** `PAYONLINE10` goes out only in the WhatsApp
      order confirmation. It appears nowhere in the video, the primary text or the headline.
- [ ] **No cash-on-delivery badge, and never the bare word "prepaid".** Jackets are 100%
      online at checkout (card / JazzCash) as of 4 Sep 2026 — no deposit, no rider
      payment. **Always pair the term with the reason:** *"paid online, because each one
      is cut for one customer."* "Prepaid" alone reads as distrust in a COD market; the
      reason reads as craft.
- [x] **Landing page agrees with the ad.** Resolved 4 Sep 2026 — all 30 jacket
      descriptions, the PDP, cart, JSON-LD and the FAQ page now state the online-payment
      rule with its reason. The click no longer lands on a contradiction.
- [ ] **The jacket on screen is the Rs 22,000 jacket** (The Iconic, black sheepskin).
      The closing card names that price; label must match subject.
- [ ] **Claims limited to the jacket range** — full-grain sheepskin, made to order in
      Karachi, lifetime craftsmanship warranty, free delivery nationwide, from Rs 22,000.
      No "hand-stitched" or "saddle-stitched"; those belong to specific wallets.
- [ ] **PU comparison is unbranded.** No competitor logo, tag or recognisable garment in
      shots 02 and 04.
- [ ] **Ad set excludes** `KV — COD Refusers EXCLUDE` `120253660257910428`.
- [ ] **Cities only**, no `radius` on any of them: Karachi `1800796`, Lahore `1807162`,
      Islamabad `1796084`, Rawalpindi `1822222`. Never `countries: ["PK"]`.
- [ ] **`targeting` is a full replace via the API** — fetch the existing object and merge,
      or the audiences and exclusions are wiped.
- [ ] **Optimise on View Content**, not Purchase. At ~PKR 8,450 jacket CPA a
      Purchase-optimised ad set on PKR 1,000/day cannot reach 50 conversions a week and
      will never exit learning.
- [ ] **Judge on delivered orders in Shopify.** Jackets void at 57%; Meta counts the
      promise, PostEx counts the parcel. Historical jacket order counts overstate demand
      roughly 2x.
