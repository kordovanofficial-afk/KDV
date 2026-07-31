# Kordovan Ads Playbook — Pakistan / COD reality

Read this BEFORE any ads work, and before trusting a number in a vendored skill.
Every figure here comes from our own account and store, not from generic
US/EU benchmarks. Account in scope: **`995683712074843` (Kordovan 2025, PKR)** — only.

---

## 1. The one fact that governs everything: COD

Pakistan is a cash-on-delivery market. An "order" is not revenue — it is a
*promise* that someone will accept a parcel.

- 5,203 cancelled orders in store history. 425 serial refusers identified,
  **323 tagged `FRAUD RISK`** and excluded from ads.
- Historically **~40% of placed orders never deliver**.
- Recent window (Jul 19–25 2026): 5 of 28 orders voided = **18% cancellation** —
  better, likely because the refuser exclusion is now live. Track this monthly.

**Consequences, non-negotiable:**
1. **Judge every campaign on DELIVERED orders in Shopify**, never Meta's purchase
   count. Meta counts the promise.
2. Every ad set excludes `KV — COD Refusers EXCLUDE 120253660257910428`.
3. Never seed a lookalike on pixel purchasers — that teaches Meta to find
   refusers. Seed on **delivered repeat buyers** (`120253659969900428`).
4. `PAYONLINE10` (prepaid discount) must NEVER appear in ad copy. It is delivered
   only via the WhatsApp order-confirmation message.

---

## 2. Our real benchmarks (PKR) — use these, ignore the skills' USD numbers

Measured on this account. Refresh quarterly.

| Metric | Warm / retargeting | Cold (value LLA) |
|---|---|---|
| CTR | **3.2 – 4.5%** | **0.9 – 1.3%** |
| CPC (all) | **PKR 5 – 8** | **PKR 32 – 52** |
| CPM | **~PKR 283** | **PKR 416 – 492** |
| Cost per landing page view | **~PKR 5.35** | **~PKR 56** |

Store-side baseline (Shopify, Jul 19–23 — a healthy window):
- Sessions **330–400/day** · conversion rate **~1.33%**
- Checkout completion **53%** of sessions that reach checkout
- Wallet AOV **~PKR 2,475** · blended AOV historically ~PKR 4,525

> ⚠️ A cold CPM of ~450 is roughly 1.6x our warm CPM. Some of that is learning-phase
> inflation, but do not assume it collapses — re-measure before scaling.

---

## 3. Unit economics — the maths that decides if cold traffic is viable

Chain, using our own measured rates:

```
cost per LPV  ->  LPV per order (1 / site CR)  ->  placed CPA  ->  delivered CPA
                  = 1 / 1.33% = ~75 LPV        ->              ->  placed / 0.6
```

**Cold:** 75 LPV x PKR 56 = **~PKR 4,200 placed CPA** -> **~PKR 7,000 delivered CPA**
**Warm:** 75 LPV x PKR 5.35 = **~PKR 400 placed CPA** -> **~PKR 670 delivered CPA**

Against a PKR 2,475 wallet, **cold prospecting is currently under water and
retargeting is extremely profitable.** That is the single most important economic
fact in this account, and it is the opposite of what a generic playbook assumes.

**Missing input — ask the user:** gross margin per wallet (COGS). Without it the
break-even is a guess. At an assumed 50% margin, break-even delivered CPA is
~PKR 1,240, i.e. cold must improve ~5.6x or AOV must rise to work.

**Levers, in order of leverage:**
1. **Raise AOV** — bundles (wallet + belt/keychain), free-delivery threshold at
   PKR 2,500 already nudges this. A 2-item order fixes the maths faster than any
   targeting change.
2. **Raise site CR** — at 2.5% CR the cold placed CPA halves to ~PKR 2,200.
   Cheaper than buying better traffic.
3. **Lower cost per LPV** — better creative (CTR up = CPM down), not more budget.

---

## 4. Attribution — Meta overstates by ~2x

Jul 19–22: Meta claimed **PKR 37,850** revenue on PKR 3,820 spend (**~9.9x ROAS**).
Shopify attributes **7 orders / ~PKR 18,500**, one later cancelled → **real ~4.3x**.

The gap is view-through credit for orders that actually came from Google, direct
and organic Instagram. **Budget against 4–5x, not the dashboard.**
Cross-check monthly: Shopify `customerJourneySummary.firstVisit.utmParameters`
vs Meta's reported purchases.

---

## 5. Delivery mechanics that bite us specifically

From the vendored `meta-ads-analyzer` references — the three that apply here:

- **Learning phase = ~50 results / 7 days.** At PKR 5,000/day optimising for
  Purchase we land around 40–45/week — **just under**. Expect "Learning limited"
  and chronic instability. Prefer FEWER, larger ad sets over more small ones.
- **Auction overlap.** The legacy broad `Retarget` ad set (PK 18–65, Advantage+ on)
  *contains* the audiences our Warm ad set targets. Meta picks one and excludes the
  other — this starves budget and blocks learning exit. Consolidate rather than add.
- **Breakdown effect.** Never pause a segment for higher *average* CPA. Meta
  optimises *marginal* cost. When it gives Bastion 74% of budget and starves Razor,
  that is usually correct. Frame kill decisions as hypotheses, and only after a
  full learning cycle.

---

## 6. Market specifics for creative

- **Payment badges that matter:** COD first, then Easypaisa / JazzCash. Visa and
  Mastercard are secondary here — do not lead with them.
- **Free delivery ≥ PKR 2,500.** Bastion (2,500) qualifies; Razor (2,450) does NOT.
  Never put a free-delivery badge on a Razor creative.
- **Cities that carry volume:** Karachi, Lahore, Islamabad/Rawalpindi.
- **Trust is the conversion lever, not novelty.** COD, lifetime warranty, 7-day
  returns and real reviews do more than discount urgency in this market.
- **WhatsApp is a primary channel**, not an afterthought — it is where the prepaid
  nudge and order confirmation happen.

---

## 7. Claims discipline (brand rule, not a market rule)

Not every product is hand-stitched, saddle-stitched, or made in Karachi. Never
write a universal craft claim into ad copy. Pull claims from the specific
product's Shopify description only — see the Bronco incident in `CLAUDE.md`.

---

## 6. Unit economics with REAL COGS (user-supplied, Jul 31 2026)

**COGS:** machine-made wallets **PKR 550–800** (use 675 avg). Purely handcrafted
**PKR 1,200–1,800** (use 1,500 avg). This replaces the 50%-margin guess in §3 —
actual gross margin on a PKR 2,500 wallet is **~73%**, on a PKR 4,200 one **~84%**.

### 🔴 The metric nobody was watching: per-product refusal rate

Shopify `returns` on a COD store = refused/RTO deliveries. It is **not**
discounting — discounts across every wallet are under 10% of gross. Refusal
varies more than 8x between products:

| Wallet (12m) | Price | Orders | Return % | Profit / PLACED order |
|---|---|---|---|---|
| The Aristocrat | 4,200 | 50 | **7.2%** | **~3,005** |
| Bronco Handcrafted | 6,200 | 43 | 27.7% | **~2,913** |
| The Truckkr | 3,800 | 62 | 22.1% | ~2,106 |
| Shelby & Thomas | 2,800 | 70 | 20.5% | ~1,500 |
| Plain Bifold Nappa | 2,400 | 55 | **13.3%** | ~1,485 |
| RFID Protected KODO | 2,300–2,500 | 59 | 33.4% | ~1,128 |
| The Razor // RFID | 2,450 | 31 | 34.4% | ~1,029 |
| The Mocha Mate | 3,200 | 227 | 49.2% | ~988 |
| Kodo Vertical 2.0 | 2,450 | 248 | 35.6% | ~968 |
| The Hunter HM | 3,200 | 32 | **63.4%** | ~855 |
| **The Bastion Bifold** | 2,500 | 405 | **48.1%** | **~720** |
| Rigor Wallet Lite | 1,499 | 109 | 41.7% | ~462 |

Profit/placed-order = net_sales − (units × COGS) − (failed deliveries ×
~PKR 250 RTO shipping), divided by orders placed. It is the **maximum CPA that
breaks even**, because ad spend is incurred per order PLACED, not per delivered.

**Pattern: higher price → dramatically lower refusal.** A PKR 4,200 wallet
refuses at 7%; a PKR 1,499 one at 42%. Cheap COD orders are impulse promises;
expensive ones are considered purchases. This inverts the instinct to advertise
the cheapest product to win volume.

### What this means for the current ads
Cold placed CPA is **PKR 1,979**. Cross-referenced against the table above,
cold prospecting is only profitable on **Bronco (2,913)** and **The Aristocrat
(3,005)** — and marginally on Truckkr. It loses money on everything else.

⚠️ **We have been advertising `AD_Bastion_Cold_PatinaAngle` (Bastion, ~720/order,
48% refusal — the worst economics of any major wallet) and
`AD_Razor_Cold_RFIDHook` (Razor, ~1,029/order, and the slowest-selling smart
wallet).** The creative is fine; the products behind it cannot carry a cold CPA.

### Smart Wallet category — demand ranking
| | 12-month orders | 90-day orders | Trend |
|---|---|---|---|
| The Mocha Mate | 227 | **69** | strong, current leader |
| Kodo Vertical 2.0 | **248** | 19 | historical champion, **collapsing** (14 in stock) |
| The Razor // RFID | 31 | 21 | new (Apr 2026), ramping, 81 in stock |
| RFID Protected KODO | 59 | 16 | steady |

