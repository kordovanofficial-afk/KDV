# WhatsApp order automation — plan (Jul 26 2026)

Goal: confirm orders before dispatch and keep buyers updated, to cut COD refusal
and RTO cost. Status: **PLAN ONLY — nothing built, decisions needed first.**

---

## 🔄 REVISED Jul 26 2026 — check the existing app BEFORE building anything

The user already runs a WhatsApp automation app on this same Shopify store for
POS: receipts, review reminders, 90-day win-back discounts, all automatic.

**Key reframe: POS orders and online orders are the same Shopify objects in the
same store.** Almost every WhatsApp/Shopify app triggers on `orders/create` and
filters by sales channel. So online-order messaging is very likely a *scope
setting already in that app*, not a build. Check that first — it makes most of
the plan below unnecessary and costs nothing extra.

**What the app cannot know: PostEx delivery status.** It only sees Shopify
events. Our Worker is the only thing that sees PostEx transitions.

### The hybrid — the actual recommendation
Let the Worker create the trigger the app already reacts to:

```
PostEx status change → kordovan-postex-sync Worker
                     → writes a TAG on the Shopify order
                       (wa-dispatched / wa-out-for-delivery / wa-delivered)
                     → Shopify Flow (free, already in use for FRAUD RISK)
                     → the WhatsApp app's Flow action sends the message
```

Nothing new is paid for, no Meta Business verification, no template approval, no
new API. It reuses three things already running: the Worker, Shopify Flow, and
the app. The Worker already writes to Shopify (it marks orders paid and adds
notes), so adding `tagsAdd` is a few lines.

⚠️ **Verify first — how was the app connected?** If setup involved **scanning a
QR code** with the phone's WhatsApp, it is a WhatsApp *Web session* integration
(Baileys / whatsapp-web.js class), NOT the official Cloud API. Those violate ToS
and get numbers permanently banned. Low POS volume may fly under the radar;
adding every online order plus delivery updates raises that risk a lot. If it is
QR-based, do not scale it — migrate to the official API instead.

## ⚠️ The FREE-only rule conflict — read first (applies ONLY if building fresh)

**The WhatsApp Cloud API is not free for business-initiated messages.** Meta
charges per *utility template* (order/shipping notifications). There is no free
tier that covers proactive messaging at our volume. This is a direct conflict
with the project's permanent FREE-only rule, so it is the user's call, not an
assumption to make quietly.

Three honest paths:

| Path | Cost | Automation | Verdict |
|---|---|---|---|
| **A. Manual WhatsApp Business app** | Free | None | Works at 5–6 orders/day. Already roughly what we do. Breaks the moment ads scale. |
| **B. Cloud API, service-window-first** | Near-free | Partial | Clever, fragile. See below. |
| **C. Cloud API, full utility templates** | Paid, small | Full | What the user actually described. Recommended. |

### ❌ NOT an option: unofficial libraries
Baileys / whatsapp-web.js / any "free WhatsApp API" that drives a logged-in
session. It violates WhatsApp ToS and gets numbers **permanently banned**. Losing
the number the whole business runs on is not a risk worth a few thousand rupees.
Do not use these regardless of who recommends them.

### How Path B squeezes the cost down
Messages a customer *starts* are free, and everything sent inside the following
24-hour service window is free too. So: on the thank-you page, a prominent
**"Confirm your order on WhatsApp"** button with a pre-filled message. The
customer taps → their message opens a free 24h window → our confirmation, the
prepaid nudge and the dispatch note all ride free inside it.

Limits: only works if they actually tap, and the window closes after 24h — so
out-for-delivery (2–5 days later) still needs a paid template. Use B for the
confirmation step, C for delivery-day messages.

---

## Rough economics (verify current Meta rates for Pakistan before committing)

- ~150–180 orders/month at current volume.
- Recent cancellation rate **18%** (Jul 19–25 actuals) ≈ **~28 RTOs/month**.
- Each RTO burns forward + return shipping, roughly **PKR 400–500** → **~PKR 12,600/month wasted**.
- If pre-dispatch confirmation catches even 40% of those → **~PKR 5,000/month saved**.
- Messaging cost at ~4 templates × 180 orders = ~720 messages/month.

Even at several rupees per message this is clearly net positive. **The saving is
in cancelling before we pay to ship, not in the messaging itself.**

---

## Message flow — start at 3, not 7

Over-messaging is the real risk: every ping is a chance to be blocked, and blocks
drag down the Meta quality rating until the number gets throttled or banned.

**Phase 1 (build this):**
1. **Order placed** → confirm/cancel buttons + item, price, address to verify.
   Kills fake and impulse orders *before* shipping cost is incurred.
2. **Out for delivery** → "rider arriving today, please keep **PKR X** ready."
   Highest-value single message. Most failed deliveries are cash-not-ready or
   nobody-home, not genuine refusal.
3. **Delivered** → thank-you + review request. Feeds the self-authored review
   metafields the PDP already renders.

**Phase 2 (only if Phase 1 proves itself):**
4. Dispatched + tracking number, linking to `/pages/track-order`.
5. Unconfirmed after 6h → single nudge. No reply after 24h → hold, don't ship.
6. RTO/failed → "we missed you, reply to reschedule."

Deliberately NOT sending: in-transit hops, arrived-at-hub. That is noise and
gets you blocked. The customer can self-serve on the tracking page.

---

## Architecture — reuses what already exists

Everything needed is already running; this is an extension, not a new system.

```
Shopify orders/create webhook ─┐
                               ├─→ kordovan-postex-sync Worker ──→ WhatsApp Cloud API
PostEx status (cron + webhook) ─┘         │
                                          ├─→ Shopify: tag order confirmed/cancelled
Meta webhook (button replies) ────────────┘     KV: dedupe + state
```

- The Worker already holds `POSTEX_TOKEN`, Shopify credentials and `SYNC_KV`, and
  already knows every status transition. Adding `WHATSAPP_TOKEN` + `PHONE_ID` is
  the only new config.
- Button replies land on a Meta webhook → Worker tags the Shopify order
  `wa-confirmed` / `wa-cancelled`.
- A Shopify Flow (like the existing FRAUD RISK one) can hold unconfirmed orders.
- KV prevents double-sends on cron re-runs — essential, duplicates get you blocked.

## Prerequisites the user must do
1. **Meta Business verification** — required for production messaging volume.
2. **A dedicated phone number** not currently active on the WhatsApp Business
   *app*, or migrate the existing one (it cannot run in both).
3. **Template approval** — each message pre-approved by Meta, 1–2 days each.
4. **Opt-in** — Meta requires consent. Add a checkout notice/checkbox, and keep
   the record. Not optional; violations cost the number.

## Rules to bake in
- Never put `PAYONLINE10` in a public template — prepaid nudge only inside the
  confirmation conversation, exactly as today.
- Urdu/English mix matching how the team already writes to customers.
- Every template must carry a real opt-out line.
- Tag COD refusers: a `FRAUD RISK` customer should get confirmation-required
  treatment, not a normal flow.


---

## Confirmed from live order data (Jul 26 2026)
Orders carry `hxs_courier_*` custom attributes written by the PostEx Shopify app:
- `hxs_courier_tracking` — the CN number (already read by the Worker)
- `hxs_courier_url` — **`https://postex.pk/tracking?cn={number}`**
  ← this is PostEx's real PUBLIC tracking URL, previously unknown and deliberately
  not guessed. Use it for the theme's `courier_tracking_url` fallback setting.
- `hxs_courier_label` — merchant invoice PDF (internal, do not expose)

Orders are tagged `PostEx` on dispatch — a usable Flow trigger for a
"your order has shipped" WhatsApp message with no Worker change at all.
