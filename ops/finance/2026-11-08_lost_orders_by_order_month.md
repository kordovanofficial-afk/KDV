# Lost orders by the month the order was PLACED (2026, Shopify, PKT months) — pulled Nov 8 2026

Counts, not rupees. "Cancelled before dispatch" = cancelled + unshipped. "Refused at door" = cancelled + shipped (RTO).
"Returned/unpaid" = fully refunded (not cancelled) + expired card payment. Source: Shopify ordersCount by created_at.

| Month | Orders | Cancelled pre-dispatch | Refused at door | Returned/unpaid | Lost | Lost % | Refused % of shipped |
|---|---|---|---|---|---|---|---|
| Jan | 395 | 93 | 54 | 0 | 147 | 37.2% | 17.9% |
| Feb | 299 | 63 | 36 | 0 | 99 | 33.1% | 15.3% |
| Mar | 329 | 55 | 54 | 3 | 112 | 34.0% | 19.7% |
| Apr | 196 | 29 | 21 | 0 | 50 | 25.5% | 12.6% |
| May | 237 | 64 | 25 | 1 | 90 | 38.0% | 14.5% |
| Jun | 212 | 46 | 16 | 1 | 63 | 29.7% | 9.6% |
| Jul | 155 | 44 | 13 | 0 | 57 | 36.8% | 11.7% |
| Aug | 218 | 64 | 26 | 0 | 90 | 41.3% | 16.9% |
| Sep | 154 | 39 | 11 | 1 | 51 | 33.1% | 9.6% |
| Oct | 137 | 16 | 4 | 3 | 23 | 16.8% | 3.3% (5 still unresolved) |
| Nov 1–8 | 70 | 9 | 0 | 0 | 9 | too early (19 in transit) | — |
| **Jan–Oct** | **2,332** | **513** | **260** | **9** | **782** | **33.5%** | **14.2%** |

Caveats: pre-dispatch cancels include some duplicate/fake orders (same customer re-ordering), so the "real customer lost"
rate is a little lower. Sana's Oct 25.3% was by VALUE and counted the 2 expired jacket card payments (52,200); by COUNT Oct is 16.8%.
