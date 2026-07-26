# WhatsApp order automation — plan (Jul 26 2026)

Goal: confirm orders before dispatch and keep buyers updated, to cut COD refusal
and RTO cost. Status: **PLAN ONLY — nothing built, decisions needed first.**

---

## ⚠️ The FREE-only rule conflict — read first

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
