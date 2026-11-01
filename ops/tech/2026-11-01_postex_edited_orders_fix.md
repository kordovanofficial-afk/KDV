# PostEx Sync: edited and part-paid orders fix (v5.1)
Nov 1 2026 · CTO seat (CEO acting) · Founder approved writing the fix. **Not deployed.** Deploy is a separate L2 approval.
Diagnosis: CFO, confirmed by CQRO, `ops/finance/2026-11-01_margin_and_cash.md` §3 (6 orders, PKR 86,616 of cash recorded that never arrived).

## What changed (`tools/postex-worker/worker.js` only)
- **New `resolveCodCapture()`** is now the only place that decides the COD amount. It re-reads the order fresh (`/orders/{id}.json?fields=…total_outstanding…`) right before capture and:
  - **outstanding ≤ 0 → skip** as already handled, whatever the label (`paid`, `partially_paid`, `partially_refunded`, `pending`). This replaces the old `financial_status === 'paid'` guard in both the webhook and the poll.
  - **PostEx amount known and more than PKR 1 away from outstanding → no capture.** `noteCodMismatch()` writes the order note `⚠️ PostEx COD amount X ≠ Shopify outstanding Y, check manually`, once per order (KV `codmm:<orderId>`, 30-day TTL), so the hourly sweep does not repeat it.
  - **Otherwise capture Shopify's `total_outstanding`.** It is within PKR 1 of PostEx, and using it leaves the balance at exactly 0.
  - **`total_outstanding` missing → throw, no capture.** It fails closed and never falls back to `total_price`.
- **Webhook:** PostEx webhooks usually carry no amount, so the handler now calls `/track-order/{cn}` for `invoicePayment`. If that call fails, it uses the Shopify outstanding amount. `order.total_price` is gone from the money path.
- **Poll:** `postexData.invoicePayment || o.total_price` is replaced by `resolveCodCapture()`. A mismatch or skip sends no "delivered" WhatsApp and schedules no review, the same as the old "already paid" skip.
- **`/health`** now returns `{status, version: "5.1-edited-orders", ts}`.
- **Unchanged:** `runPrepaidDeliveryPass` (still never calls `markOrderPaid`), the `ppass:init` baseline, every dedup key (`wasent:`, `rvdone:`, `rvdue:`, `wapend:`), payment-aware WhatsApp copy, RTO notes, and `markOrderPaid` itself.
- **Out-for-delivery WhatsApp** (added at the coordinator's request). `msgOutForDelivery()` now quotes what the rider will actually collect: `total_outstanding`, falling back to `current_total_price`, and never `total_price`. If the amount due is 0 or less, it sends the "nothing to hand over" line. If neither field is present, it says "the amount due" and quotes no figure. `getOpenCODOrders()` now also requests `total_outstanding,current_total_price`. The prepaid pass's out-for-delivery call is unchanged and still uses the prepaid line.

## Test results
The real modified functions (`handleWebhook`, `runPollSync`, the default `fetch` export) were run in Node 22 against mocked Shopify REST, PostEx and KV. `node --check` passes. **15/15 pass.**

| Case | Result |
|---|---|
| (a) normal COD, poll and webhook (no amount in payload) | captured 3,200.00 |
| (b) edited order: total 85,400, outstanding 28,200, 0 paid. Webhook with PostEx lookup failing, and poll with PostEx 28,200 | captured **28,200.00**, not 85,400 |
| (c) outstanding 0 with status paid / partially_paid / partially_refunded / pending | skipped, 0 captures, 0 notes |
| (c2) KDV#22863 replay: poll, then webhook for the same order | **one** capture (9,100) |
| (d) PostEx 85,400 vs outstanding 28,200, run 2× poll + 1× webhook | 0 captures, **1** note `PostEx COD amount 85,400 ≠ Shopify outstanding 28,200, check manually`, order still pending |
| (d2) PostEx 28,200.50 vs outstanding 28,200 (inside the PKR 1 tolerance) | captured 28,200.00 |
| (e) `total_outstanding` missing | 0 captures (fails closed) |
| (f) `/health` | `version: "5.1-edited-orders"` |
| (g) poll sees "Out For Delivery" on the edited order (total 85,400, outstanding 28,200) | queued WhatsApp says **PKR 28,200** and contains no 85,400 |
| (g2) message unit test: only `current_total_price` set / outstanding 0 / neither field set | quotes 4,570 / "nothing to hand over" / "the amount due"; `total_price` 85,400 never shown |

Control run: the same suite against the pre-fix file failed 12 of the original 13 cases. It captured 85,400 in (b) and captured on `partially_paid` / `partially_refunded` in (c), which reproduces the CFO's diagnosis. Harness: scratchpad `postex-test/test.mjs` (session-local).

## Manual deploy steps (needs the Founder's yes first)
1. Open Cloudflare → Workers → `kordovan-postex-sync` → **Edit code**.
2. Select all, then paste the **whole** `tools/postex-worker/worker.js`.
3. Press **Deploy**. Saving does not deploy.
4. Open `https://kordovan-postex-sync.kordovan-official.workers.dev/health` and confirm it shows `"version":"5.1-edited-orders"`. Optionally diff `workers_get_worker_code` against the repo file.
5. After the next hourly run, check KV `last_sync` (or `/stats`) for errors.

⚠️ **Known accepted drift closes with this deploy.** The live Worker still sends the old **"4–7 working days"** prepaid WhatsApp text. The repo carries **"about 3 weeks"**, and the Founder declined a separate redeploy on Sep 6. Pasting this file replaces it with "about 3 weeks". That is expected and correct, not a side effect to worry about.

## Not done here (Founder decisions)
- Cleaning up the 6 existing over-recorded orders (L3: it changes financial records). The fix stops new ones only.
- Sizing earlier months: pull `orders{totalOutstandingSet}` for Aug–Oct and look for negative outstanding.
