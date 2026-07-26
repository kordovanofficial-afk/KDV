# WhatsApp order confirmation — build spec & interface contract

Two systems, two builders, one HTTP contract. This file is the agreement so both
sides can be built independently without stepping on each other.

---

## The split — and why it falls here

| | Owner | Why |
|---|---|---|
| **Baileys box** (office laptop) — holds the WhatsApp session, sends text, receives replies | The other AI | It built the POS bot, knows that codebase, and can test on the machine. |
| **Worker + all Shopify writes** — decides what to send, tags orders, cancels orders, dedupes | This project | It already polls PostEx, holds Shopify credentials + KV, and carries the COD/FRAUD-RISK rules. |

### 🔴 The Baileys box must NEVER write to Shopify
All order mutations — tags, notes, cancellation — happen in the Worker, one place,
with one set of guardrails. The box is a **dumb pipe**: it sends text and forwards
replies. Reasons:

1. **Cancellation is irreversible.** `orderCancel` cannot be undone. It must exist
   in exactly one code path with all the checks below, not in two systems that can
   drift apart.
2. The other AI then needs **no Shopify credentials at all** — smaller blast radius
   if that laptop is ever compromised or the code is shared.
3. Dedupe/idempotency needs one source of truth (KV). Two writers race.

---

## Contract A — Worker ➜ Baileys box (send a message)

```http
POST https://<tunnel-host>/send
X-KV-Secret: <shared secret>
Content-Type: application/json

{
  "to": "923001234567",          // digits only, country code, no + and no leading 0
  "text": "Your order KDV#22412 …",
  "ref": "22412:awaiting_confirm" // echoed back; used for logging/dedupe
}
```

**Response — must distinguish "no WhatsApp" from "failed":**
```json
{ "ok": true,  "sent": true }
{ "ok": true,  "sent": false, "reason": "not_on_whatsapp" }   // ← drives the CALL tag
{ "ok": false, "error": "session_disconnected" }
```

Box responsibilities:
- Check `onWhatsApp()` **before** sending. Never send blind to dead numbers — that
  pattern looks like scraping and is a ban signal.
- Random **3–10s jitter** before each send. Never burst.
- Queue anything outside **09:00–21:00 PKT** until morning.
- Reject requests without the correct `X-KV-Secret`.

## Contract B — Baileys box ➜ Worker (a customer replied)

```http
POST https://kordovan-postex-sync.kordovan-official.workers.dev/wa-inbound
X-KV-Secret: <shared secret>

{ "from": "923001234567", "text": "confirm", "ts": 1785000000 }
```

Box responsibilities:
- Forward **only 1:1 customer messages**. Never groups, never status broadcasts,
  never messages from the team's own number.
- Forward raw text. **Do not interpret it** — the Worker decides what counts as a
  confirm or a cancel. One parser, one place.
- Fire-and-forget; a non-200 must not crash the session.

⚠️ Both sessions on this number receive **all** inbound messages, including POS
customers replying to receipts and general enquiries. The Worker answers only
senders who match an order awaiting confirmation and stays silent otherwise, so
the team's existing manual reply workflow is untouched.

---

## Phone normalisation (Pakistan) — get this right or nothing matches

Shopify stores `+923001234567`; some orders carry `03001234567`; WhatsApp JIDs are
`923001234567@s.whatsapp.net`. Normalise **both sides** to bare `923XXXXXXXXX`:

1. Strip everything non-digit.
2. Leading `0092` → `92`; leading `00` → drop.
3. Leading `0` (e.g. `03001234567`) → replace with `92`.
4. Bare `3001234567` (10 digits starting 3) → prefix `92`.
5. Valid PK mobile = `92` + `3` + 9 digits = **12 digits total**. Anything else →
   treat as unreachable and tag for a manual call.

---

## Order state — visible in Shopify admin as tags

Follows the existing emoji-tag convention (`⛔ FRAUD RISK`) so staff read it at a glance.

| Tag | Meaning | Set when |
|---|---|---|
| `⏳ WA SENT` | Confirmation asked | Message delivered |
| `✅ WA CONFIRMED` | Customer said yes | Reply parsed as confirm |
| `🚫 WA CANCELLED` | Customer said no → order cancelled | Reply parsed as cancel + all checks pass |
| `📞 NO WHATSAPP — CALL` | Not reachable on WhatsApp | `sent:false, not_on_whatsapp` |
| `⚠️ WA NO REPLY` | Silent after 12h | Follow-up sweep |

`📞 NO WHATSAPP — CALL` is the requirement "if a customer doesn't have WhatsApp it
stays untouched" — but *actively surfaced* so the team knows to phone, rather than
silently doing nothing.

---

## 🔴 Cancellation guardrails — every one is mandatory

`orderCancel` is irreversible. All of these must pass:

1. **Identity:** the reply must come from a number that normalises to the phone on
   that order. Never cancel on a sender we cannot match. This is the security
   property that makes the whole thing safe.
2. **Exact keyword** only — `cancel` / `منسوخ`, matched on the whole trimmed
   message. Never substring: "don't cancel it" must not cancel it.
3. **Unfulfilled only.** If already dispatched, do NOT cancel — tag
   `↩️ WA CANCEL AFTER DISPATCH` and let the team handle the RTO.
4. **COD only** (`financial_status: pending`). Anything paid goes to a human.
5. **One order.** If the sender has several awaiting confirmation, do not guess —
   reply asking which order number, and tag for the team.
6. **Restock** on cancel, reason `CUSTOMER`, and write a note recording the
   message text and timestamp.
7. **Time bound:** only within 24h of the confirmation request. Later replies are
   ambiguous — tag, don't act.

Confirmation is safe to automate; cancellation is destructive. When in doubt the
system must **tag and defer to a human**, never guess.

---

## Build order
1. Worker: send + tags + `📞 NO WHATSAPP` (no reply handling). Value on day one.
2. Box: `/send` endpoint + jitter + `onWhatsApp()` + business hours.
3. Cloudflare Tunnel so the Worker can reach the laptop.
4. Worker: `/wa-inbound`, confirm parsing, `✅ WA CONFIRMED`.
5. Cancellation last, with every guardrail above, tested on a dummy order first.

## Open risks
- **Linked-device limit:** WhatsApp allows ~4 companion devices. Check
  Settings → Linked devices. Extending the *existing* session avoids this entirely;
  a second session does not.
- **Office laptop = single point of failure.** If it sleeps or loses power, sends
  stop. The Worker must treat send failures as non-fatal and retry, never block
  the PostEx sync.
- **One number carries everything.** POS receipts, online orders, delivery
  updates and the public contact line are all the same account. A ban takes all of
  it. Accepted by the user with eyes open (Jul 26 2026).
