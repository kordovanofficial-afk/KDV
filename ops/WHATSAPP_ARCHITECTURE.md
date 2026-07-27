# WhatsApp automation — architecture (single-owner build)

**Decision Jul 26 2026:** built entirely within this project. No other AI, no
third party gets Shopify credentials or customer data. The office laptop runs a
bridge whose only job is to hold the WhatsApp session — it never sees an order.

---

## The one hard constraint

**Baileys cannot run on Cloudflare Workers.** It needs a WebSocket held open 24/7,
in-memory session state and full Node crypto. Workers are stateless and
short-lived. So something must run on an always-on machine.

**Decision (user, Jul 26 2026): NOT the office laptop.** It closes at night, and
the user wants to be able to check the system whenever they like. The bridge runs
on a **free always-on cloud VM** (Oracle Always Free, or GCP e2-micro), managed by
pm2 so it survives reboots, exposed through a free Cloudflare Tunnel.

Pairing does not need SSH or TeamViewer: the bridge serves the QR as a **web page**
(`/qr?k=ADMIN_KEY`), so the team opens a link on any phone and scans. There is also
a live **`/status?k=ADMIN_KEY`** page — connection state, queue depth, sends,
last error — for checking in at any time.

`tools/wa-bridge/` is deliberately dumb: send text, forward replies. It holds no
Shopify token, no order data, no customer list. If that box is compromised or the
code is shared, nothing about the business goes with it.

Two secrets, deliberately separate: `BRIDGE_SECRET` (Worker ⇄ bridge, in headers)
and `ADMIN_KEY` (browser pages only). The send secret must never appear in a URL,
browser history or a screenshot of the status page.

```
                    ┌─────────────────────────────────────┐
Shopify webhooks ──►│  kordovan-postex-sync Worker        │
PostEx status    ──►│  ALL logic · ALL Shopify writes     │
Hourly cron      ──►│  KV: state + dedupe                 │
                    └──────────────┬──────────────────────┘
                                   │ POST /send  {to, text, ref}
                                   ▼      (Cloudflare Tunnel, free)
                    ┌─────────────────────────────────────┐
                    │  wa-bridge  ·  free always-on VM    │
                    │  Baileys session · jitter · queue   │
                    └──────────────┬──────────────────────┘
                                   │ POST /wa-inbound  {from, text}
                                   ▼
                            WhatsApp ⇄ customer
```

---

## ⚠️ What can and cannot be built

| Ask | Verdict |
|---|---|
| Order placed → confirm / cancel | ✅ Phone is on the order |
| Delivery status updates | ✅ Worker already sees every PostEx transition |
| Delivered → review request | ✅ |
| **Abandoned checkout → discount** | ✅ **High value.** Phone captured at checkout |
| **Add-to-cart → discount** | ❌ **Not possible.** See below |

### Why add-to-cart messaging cannot work
Adding to cart captures **no identity** — no phone, no email, nothing. Almost all
Kordovan traffic is guest COD, so there is no one to message. Any tool promising
this either (a) only covers logged-in customers, which is a tiny slice here, or
(b) is guessing. It is not a limitation of our build; the data does not exist.

**The recoverable gap is checkout, not cart.** Store data Jul 19–23: ~12 sessions
add to cart daily, ~8–12 reach checkout, ~5 complete. The people who reach
checkout give us a phone number — those are reachable and worth chasing. The
cart-only visitors are anonymous. Chase the ones we can identify.

---

## 🔴 Availability — the laptop closes, orders do not

The office laptop shuts at closing time; online orders arrive at 2am. Two layers
solve this, and **layer 1 is mandatory either way** — any host can go down.

### Layer 1 — the queue lives in the WORKER, not the bridge (build this)
The Worker never sends directly. It **enqueues in KV** and drains on its existing
hourly cron:

```
event → Worker writes {to, text, ref, attempts} to KV queue
     → every cron tick: if bridge /health is up, drain oldest first
     → send fails or bridge offline? leave it queued, retry next hour
     → give up after 24h, tag the order 📞 NO WHATSAPP — CALL
```

Nothing is ever lost to a closed laptop. It also makes the system survive
reboots, power cuts and internet drops — which a 24/7 server would not fix by
itself.

**How big is the real gap?** Smaller than it looks, because we already refuse to
message between 21:00 and 09:00 PKT. A 2am order was never going to be messaged
at 2am. If the laptop runs ~11:00–20:00, the only true delay is orders placed
20:00–21:00 and 09:00–11:00 — a couple of hours, same day. For a COD
confirmation that is acceptable.

### Layer 2 — optional: move the bridge to a free always-on host
Only needed if same-morning is not good enough.

| Option | Cost | Reality |
|---|---|---|
| **Oracle Cloud Always Free** | Free forever | 4 ARM cores / 24GB. Best option. Needs a card for identity check (not charged). ARM capacity is often unavailable in popular regions — may take a few tries. |
| **Google Cloud e2-micro** | Free forever | 1 small VM, US regions. Reliable to get, tighter on RAM but fine for Baileys. |
| Render / Railway free | Free | ❌ Sleeps on idle, which kills the WebSocket. Useless here. |
| Old Android + Termux | Free | Works, but Android kills background processes. Fragile. |
| Cheap VPS | ~$4/mo | Simplest, but breaks the FREE-only rule. User's call. |

Moving the bridge changes nothing in the architecture — same files, same
contract. Only the tunnel address changes.

**Recommendation:** build layer 1 now and run on the laptop. Live with it for two
weeks. If the delay actually costs orders, move to Oracle then — with real data
rather than a guess.

## Message set

**Transactional** (safe, expected, low report risk):
1. Order placed → confirm/cancel ask
2. Out for delivery → "keep PKR X ready" ← highest RTO saving
3. Delivered → thanks + review request

**Marketing** (higher risk — see below):
4. Abandoned checkout → recovery discount, **once**, 2–4h after abandonment

### 🔴 Abandoned checkout is marketing, not transactional
This is the message most likely to be reported as spam, and reports are what kill
a Baileys number. Rules, non-negotiable:
- **One message. Ever.** No second nudge, no drip.
- Only if the checkout is 2–24h old and still incomplete.
- Never to a `FRAUD RISK` customer, and never to someone who got one this month.
- Use a **dedicated discount code** (e.g. `COMEBACK10`), never `PAYONLINE10` —
  that one stays reserved for the prepaid nudge inside order confirmation.
- Opt-out line on every message, honoured permanently in KV.

If reports start appearing, this is the first thing to switch off — the
transactional messages are worth far more and must not be risked for it.

---

## Contract A — Worker ➜ bridge

```http
POST https://<tunnel-host>/send      X-Bridge-Secret: <secret>
{ "to": "923001234567", "text": "…", "ref": "22412:confirm" }
```
```json
{ "ok": true,  "sent": true }
{ "ok": true,  "sent": false, "reason": "not_on_whatsapp" }   → drives the CALL tag
{ "ok": false, "error": "session_disconnected" }
```

## Contract B — bridge ➜ Worker

```http
POST https://kordovan-postex-sync.kordovan-official.workers.dev/wa-inbound
X-Bridge-Secret: <secret>
{ "from": "923001234567", "text": "confirm", "ts": 1785000000 }
```

The bridge forwards raw text and **never interprets it**. Only 1:1 messages —
never groups, never status, never our own sends. The Worker replies only to
senders it can match to an order awaiting confirmation and stays silent otherwise,
so the team's manual reply workflow is untouched.

---

## Phone normalisation (Pakistan) — silent killer if wrong

Shopify has `+923001234567`, some orders `03001234567`, WhatsApp
`923001234567@s.whatsapp.net`. Normalise **both sides** to bare `923XXXXXXXXX`:

1. Strip non-digits
2. `0092…` → `92…` · leading `00` → drop
3. Leading `0` → replace with `92`
4. Bare 10 digits starting `3` → prefix `92`
5. Valid = 12 digits, `92` + `3` + 9. Otherwise → unreachable, tag for a call.

---

## Order state — Shopify tags (matches the existing `⛔ FRAUD RISK` convention)

| Tag | Meaning |
|---|---|
| `⏳ WA SENT` | Confirmation asked |
| `✅ WA CONFIRMED` | Customer confirmed |
| `🚫 WA CANCELLED` | Cancelled on customer request |
| `📞 NO WHATSAPP — CALL` | Unreachable — team must phone |
| `⚠️ WA NO REPLY` | Silent after 12h |
| `↩️ WA CANCEL AFTER DISPATCH` | Too late to cancel — handle as RTO |

## 🔴 Cancellation guardrails — all mandatory

`orderCancel` is irreversible.

1. **Identity** — sender must normalise to the phone on that order. This is the
   check that makes auto-cancel safe rather than reckless.
2. **Exact keyword** on the whole trimmed message — "don't cancel it" must not cancel.
3. **Unfulfilled only** — else tag `↩️ WA CANCEL AFTER DISPATCH`.
4. **COD only** (`financial_status: pending`).
5. **Exactly one** matching open order, else ask which and tag for a human.
6. **Restock**, reason `CUSTOMER`, note the raw message + timestamp.
7. **Within 24h** of the ask.

Confirmation is safe to automate. Cancellation must **tag and defer to a human**
whenever anything is ambiguous.

---

## ✅ BUILT — Worker v6.0 (Jul 27 2026)
Bridge live on Oracle VM 84.235.252.73, WhatsApp linked, status page green.

Worker endpoints added:
| Route | Purpose |
|---|---|
| `POST /shopify-order?s=SYNC_SECRET` | Shopify orders/create → confirmation ask |
| `POST /wa-inbound` | bridge forwards replies (X-Bridge-Secret) |
| `GET /wa-status?s=SYNC_SECRET` | queue depth + bridge reachability |
| `GET /wa-drain?s=SYNC_SECRET` | force a queue drain (testing) |

KV namespaces: `waq:` queue · `wasent:` dedupe (30d) · `wapend:` phone→order (48h)
· `waopt:` opt-out (permanent).

Env needed on the Worker: **BRIDGE_URL**, **BRIDGE_SECRET** (secret).

Verified before shipping: every v5 function byte-identical except
`getOpenCODOrders`, which gained phone/customer/shipping_address/line_items —
the messages need them. The COD payment path is untouched.

## Build order
1. **`tools/wa-bridge/`** on the laptop + Cloudflare Tunnel ← start here
2. Worker: outbound sends, `⏳ WA SENT`, `📞 NO WHATSAPP — CALL`
3. Worker: `/wa-inbound` + confirm parsing
4. Cancellation, with every guardrail, tested on a dummy order first
5. Abandoned checkout recovery, last, watched closely

## Known risks
- **Laptop is a single point of failure.** Sends stop if it sleeps or reboots.
  The Worker treats send failure as non-fatal and never blocks the PostEx sync.
- **Linked-device limit** ~4. Check Settings → Linked devices before scanning.
- **One number carries everything** — POS, online, delivery, public contact. A ban
  takes all of it. Accepted by the user, eyes open, Jul 26 2026.
