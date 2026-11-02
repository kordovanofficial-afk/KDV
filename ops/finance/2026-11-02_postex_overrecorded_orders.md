# Orders where Shopify shows more cash than we received (PostEx Sync)
CFO (Ayesha Naqvi) · Nov 2 2026 · L0, read-only. Nothing was changed. Source: Shopify Admin GraphQL `orders{totalOutstandingSet totalReceivedSet netPaymentSet transactions events}`, all orders placed Aug 1 – Oct 31 2026 PKT (350 Aug–Sep + 137 Oct), read Nov 2.

**Answer:** It is **14 orders, not 6: PKR 116,366** recorded as received that never came in. October has 6 orders (86,616), the CRO's figure. August–September has 8 more (29,750), all between Aug 31 and Sep 15. No order before Aug 31 is affected. Real money is fine: every customer paid what they owed, and nobody is owed a refund. Only Shopify's "received" figure is wrong.

| Order | Current total | Recorded as received | Real cash (how paid) | What PostEx collected | Shopify shows | Real balance | Over-recorded |
|---|---|---|---|---|---|---|---|
| KDV#22898 | 28,200 | 85,000 (85,400 − 400 refunded) | 28,200 (Visa, card) | nothing: fully prepaid | −56,800 | 0 | **56,800** |
| KDV#22890 | 17,850 | 29,249 | 17,850 (8,951 bank advance + 8,899 COD) | 8,899 (seen) | −11,399 | 0 | **11,399** |
| KDV#22863 | 13,500 | 22,600 | 13,500 (4,400 bank advance + 9,100 COD) | 9,100 (seen) | −9,100 | 0 | **9,100** |
| KDV#22906 | 4,570 | 8,890 | 4,570 (COD) | not visible; expected 4,570 | −4,320 | 0 | **4,320** |
| KDV#22929 | 2,400 | 5,898 | 2,400 (1,749 XPay + ~651 COD) | not visible; expected ~651 | −3,498 | 0 | **3,498** |
| KDV#22862 | 1,749 | 3,248 | 1,749 (COD) | not visible; expected 1,749 | −1,499 | 0 | **1,499** |
| KDV#22677 | 28,800 | 43,200 | 28,800 (14,400 bank advance + 14,400 COD), jacket | 14,400 (seen) | −14,400 | 0 | **14,400** |
| KDV#22715 | 10,500 | 15,750 | 10,500 (5,250 bank advance + 5,250 COD) | 5,250 (seen) | −5,250 | 0 | **5,250** |
| KDV#22751 | 5,050 | 7,600 | 5,050 (2,500 bank advance + 2,550 COD) | 2,550 (seen) | −2,550 | 0 | **2,550** |
| KDV#22665 | 2,750 | 5,250 | 2,750 (COD) | not visible; expected 2,750 | −2,500 | 0 | **2,500** |
| KDV#22707 | 2,200 | 4,400 | 2,200 (COD) | 2,200 (seen) | −2,200 | 0 | **2,200** |
| KDV#22724 | 2,050 | 3,850 | 2,050 (COD) | not visible; expected 2,050 | −1,800 | 0 | **1,800** |
| KDV#22674 | 3,450 | 4,450 | 3,450 (COD) | not visible; expected 3,450 | −1,000 | 0 | **1,000** |
| KDV#22719 | 5,050 | 5,100 | 5,050 (5,000 bank advance + 50 COD) | 50 (seen) | −50 | 0 | **50** |
| **Total** | | | | | | | **116,366** |

"Seen" = the hourly sync recorded PostEx's own `invoicePayment` figure for that order. "Not visible" = only the webhook ran, and it recorded the order total instead. Confirm those 6 figures from PostEx's settlement statement.

**Three ways this happened (all in `tools/postex-worker/worker.js`):**
1. **Customer paid an advance, then the sync captured twice** (22890, 22863, 22677, 22715, 22751, 22719). The hourly poll correctly captured the COD balance. Minutes later the webhook captured the full order total again: the "already paid" check only skips `paid`, and these orders were `partially_paid`.
2. **Staff edited the order, then the sync captured the pre-edit total** (22906, 22862, 22665, 22724, 22674, plus 22929 on top of a part-prepayment). The webhook falls back to `order.total_price` when PostEx sends no amount.
3. **Fully paid by card, then captured as COD anyway** (22898). It was `partially_refunded` after a 400 refund, so it passed the check. 22707 is a pure same-minute duplicate with no edit and no advance.
- Also: the 6 bank advances (**PKR 49,252**) were never entered in Shopify as payments. The duplicate captures happen to "cover" them, which is why the numbers looked plausible.

**Proposed correction, in plain words (Founder decides, L3; nothing done yet):**
1. **Do not refund anyone and do not touch the card gateway.** On 22898 and 22929 a refund through XPay would send real money to the customer. Any correction goes only on the "cash on delivery" record.
2. **Test on one small order first** (KDV#22719, 50). Record a refund of the over-recorded amount on the "cash on delivery" gateway, no items, no restock, customer notification **off**. Then check that ShopifyQL net sales for that day did not change. If net sales moved, stop: keep Shopify as it is and correct the books in Mr. Tahir's ledger only, with a note on each order.
3. If the test is clean, apply the same to the other 13, smallest first, each amount from this table. Afterwards every order should show outstanding 0.
4. **From now on, the cash figure comes from the PostEx settlement statement and the bank, not Shopify's "received".** Until the fix is deployed, Mr. Tahir checks any edited or advance-paid order the day after delivery.

**Not checked:** orders placed Nov 1–2 (too young; none delivered yet), and orders before Aug 1.
