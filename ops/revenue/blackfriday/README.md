# Blessed Friday Sale 2026: price + stock-buffer batches (PREP, nothing applied)

Window: **Fri Nov 27 00:00 → Mon Nov 30 23:59 PKT**. Bag (+ Clifford hat) clearance only. Plan + approvals: `BF_PLAN_2026.md`.
Prepared Nov 21 from a live Shopify read. **No live writes were made; no scheduled tasks exist yet** (the Nov 23 check-in creates them).

## What is in it
- 16 products / 48 variants (all colours of each line get the sale price, as in 11.11; sold-out colours stay sold out).
- Shown as real **price + compare-at** (strikethrough): `price` = BF price, `compareAtPrice` = regular price. All 48 had `compareAtPrice: null` before, so revert sets it back to `null`.
- One price batch (16 aliased `productVariantsBulkUpdate`, under the ~29 cap).
- Lines: Cabin Trolley 29,390 · CEO Office 33,600 · Master's Laptop 8,640 · Bella Duff 6,820 · Forester 22,420 · Venture 6,880 · Gridle 10,070 · Bellezza 4,220 · Branson 24,700 · Ladies Clutch & Wallet 4,680 · Diva Tote 4,290 · Corporate Office 21,370 · DBLP 13,870 · Clifford hats (Faded Black + Rustic Brown) 6,820 · Executive Briefcase **Black only** 21,400.
- Margin floor (≥40% GM and ≥ PKR 1,000 GP) re-checked against live unit cost: every line passes **except the Executive Briefcase (GM 34.6%, GP 7,400)**, kept on purpose as the Founder's floor exception (Nov 11). Its Brown and Coffee Brown variants have **no unit cost** and are sold out, so they are left out (they stay at 28,600).
- NOT touched: jackets, wallets (men's), belts, gloves, footwear, other hats. Note that Ladies Clutch & Wallet and Bellezza carry productType "Women's Wallet"; they are in the approved BF table and creatives on purpose.
- Open flags from the plan: Master's (may be discontinued, kept at 20% per the table) and Branson (no product photo; not in the carousel) are still in. Drop a line by deleting its rows from `price_snapshot.json` and re-running `build.py`.

## Files
| File | What |
|---|---|
| `price_snapshot.json` | Pre-sale state per variant: ids, price, compare-at, unit cost, inventory item, `available` at location `36710940861`, BF price, GM/GP, floor check. **Source of truth for revert.** |
| `build.py` | Regenerates every file below from the snapshot (no network). |
| `apply_1.graphql` / `revert_1.graphql` | Prices + compare-at on / off. |
| `stock_buffer.json` | Per variant `real` and `added = 10 − real` (in-stock and below 10 only). |
| `stock_buffer_apply.graphql` | `inventoryAdjustQuantities`, reason `correction`, name `available`, `+added`, with `changeFromQuantity = real` as a guard. |
| `stock_buffer_revert.graphql` | Same, `−added`, no quantity guard. |

Stock buffer as read Nov 21: 41 variants, **+304 units**. Left alone: sold-out variants (0) and Master's Multicolor (16) + Ladies Clutch White & Brown (18), already ≥10.

## Run order
**Nov 26, ~23:30–23:50 PKT (before apply): refresh stock**
1. Re-read `inventoryLevel(locationId:"gid://shopify/Location/36710940861"){ quantities(names:["available"]) }` for the 48 variants and update `available` in `price_snapshot.json`. Also confirm price/compare-at/cost are unchanged (if a regular price changed, update `price`).
2. `python3 build.py`, commit the regenerated files. The buffer apply only works on fresh numbers: `changeFromQuantity` makes it fail (and change nothing) if stock moved since the read.

**Nov 27 00:00 PKT = Nov 26 19:00Z: APPLY**
1. `apply_1.graphql` → every `userErrors` must be empty.
2. `stock_buffer_apply.graphql` → `userErrors` empty; check each `quantityAfterChange` = 10. On a `changeFromQuantity` mismatch: re-read, rebuild, rerun (nothing was applied).
3. Spot-check 3 variants (price, compare-at, available). Commit `stock_buffer.json` as applied (it is the revert record).

**Dec 1 00:05 PKT = Nov 30 19:05Z: REVERT**
1. `revert_1.graphql` → prices back to regular, compare-at `null`.
2. `stock_buffer_revert.graphql` → subtracts exactly `added` per variant. **Never "reset to the old number"**: sales during the sale (online and WhatsApp store reports) must stay counted.
3. Re-read `available` for the 41 buffered variants.

## To-source rule (after revert)
Any variant whose `available` is **negative** after the revert sold beyond real stock. Same morning (Dec 1), send **Mr. Tahir** a to-source list (product, colour/size, qty = the negative amount, order numbers) as a ready-to-forward file in `downloads/`, logged in `ops/operations/TEAM_HANDOVER.md`. Those orders ship once sourced. Don't correct the negatives by hand; they clear as stock arrives.

## Reminders
- POS shows the same prices automatically (Founder OK). The Founder must not schedule his own price change.
- No "only X left" copy anywhere (the buffer makes stock numbers untrue).
- WELCOME10 must be non-combinable with product discounts before launch (35% + 10% breaks the floor).

## Change log — Nov 21 2026 (Founder: "start the blessed friday sale from today")
- Start moved from Nov 27 to **Sat Nov 21**; end unchanged (Mon Nov 30 23:59 PKT).
- `apply_1.graphql` applied (16 products / 48 variants, all userErrors empty). `stock_buffer_apply.graphql` applied (+304 units, 41 variants).
- Revert: Dec 1 00:05 PKT via send_later `trig_01VKvQUEkanNX7cBoyVgdfpN` (runs revert_1 + stock_buffer_revert by delta); backup report-only `trig_01BaNkaLyAC9J2LYGVTjujYU`.
- `/collections/sale` contains all 16 (productsCount showed 0 — stale counter, products list is correct).
- Meta: audience `120256204324970428` (bag/hat page viewers, 180D = Meta max; Founder asked 3–4 years, not possible). Campaign `120256204328140428`, ad set `120256204345990428` 2,000/day ABO, ends Nov 30 23:59, 9 cities, refusers excluded, purchase-optimised. Ads (utm_campaign bf_2026): clutch `120256204399950428`, diva `120256204414890428`, clifford `120256204418990428`, belladuff_grey `120256204422530428`, belladuff_red `120256204425380428`.
- Spend: 10 days x 2,000 = ~20,000 (was 5 x 2,000 = 10,000 approved). Read daily; pause losers at ad level per kill rule (bags: CPA ceiling not set yet — use ≥1,500 spend and 0 sales as the stop line pending CFO).
