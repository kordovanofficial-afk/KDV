# Social Agent — IG / FB comments + DMs

Started Aug 1 2026. Goal: stop the user hand-answering every Instagram comment,
Facebook comment, Messenger DM and Instagram DM.

**Cost target: PKR 0.** Cloudflare Workers free tier (100k req/day), Workers AI
free tier (~10k neurons/day), Meta Graph API (free). No paid app, ever.

---

## 1. Two layers, and why the order matters

| | Layer 1 — native | Layer 2 — custom agent |
|---|---|---|
| Built on | Meta Business Suite automations | Cloudflare Worker + Graph API |
| Code | none | `tools/social-agent-worker/` |
| App Review | **not needed** | **required** |
| Live in | today | ~2–4 weeks |
| Handles | ~60–70% (predictable intents) | the rest + live store data |

Layer 2 does **not** replace Layer 1. Native automations answer instantly and
cost no compute; the agent handles what the keyword matcher gets wrong.

Guide for Layer 1: **`docs/social/SOCIAL_AUTOMATION.html`** (delivered Aug 1).

## 2. 🔴 Sequencing correction — App Review cannot start first

I originally framed this as "Layer 1 and App Review in parallel". That was
wrong in one respect: **Meta requires a screencast of the working integration**
in the submission. You cannot submit against an app that does nothing.

Real order:
1. Layer 1 live (relief starts immediately, independent of everything below)
2. Create the Meta app, wire webhooks, build the Worker
3. Test in **Development mode** — works only for people with a role on the app,
   which is fine because that is us
4. Record the screencast, submit App Review
5. Approved → switch app to Live → real customers hit the agent

Layer 1 genuinely runs in parallel. The review clock does not start until step 4.

## 3. Permissions needed (all Advanced Access → all App Review)

| Permission | For |
|---|---|
| `pages_manage_engagement` | reply to / hide FB comments |
| `pages_read_engagement` | read FB post + comment content |
| `pages_messaging` | Messenger send/receive |
| `pages_show_list` | resolve the Page |
| `instagram_basic` | resolve the IG business account |
| `instagram_manage_comments` | read + reply to IG comments |
| `instagram_manage_messages` | IG DMs |

Business Verification is a prerequisite. The business (`1031503725694826`) already
runs ads with a verified Page and IG account, so this should be a short step —
but app-level verification is separate from ad-account standing and must be
confirmed, not assumed.

⚠️ **`instagram_basic` is also what the Facebook Ads MCP connector is missing** —
`ads_get_ig_accounts` returns `[]`. Same permission, different app. Getting it
here does not fix the connector.

## 4. 🔴 No unofficial path — do not look for one

The WhatsApp bridge works because Baileys speaks the real WhatsApp protocol.
There is no equivalent for IG/FB that does not mean driving the web UI with a
headless browser, which is against Meta's terms and risks the **account that
carries the ad spend**. Not a trade worth making. Official API or nothing.

## 5. Architecture (Layer 2)

```
Meta webhook  ──► Cloudflare Worker  ──► classify intent
 (comments,          │                      │
  messages)          │                      ├─ template  → reply immediately
                     │                      ├─ needs data→ Shopify / PostEx → reply
                     │                      ├─ unclear   → Workers AI → draft
                     │                      └─ sensitive → escalate, never auto-reply
                     │
                     └─► KV: dedupe, rate limit, conversation state
```

Reuses patterns already proven in `tools/postex-worker/worker.js`:
- `X-Hub-Signature-256` verification on every inbound webhook
- **parse the request body BEFORE returning the Response** — the
  `ctx.waitUntil` body-stream bug that silently broke order webhooks for weeks
  (see `ops/WHATSAPP_ARCHITECTURE.md`); do not repeat it here
- KV dedupe markers keyed on the event id — Meta retries, and the duplicate
  flood that reached real customers in July came from exactly this gap
- an admin diagnostics route behind `WEBHOOK_TOKEN`, like `?probe=1`

### What it can do that the native tools cannot
1. **Live Shopify data** — real stock and price per variant. Worker already
   holds `SHOPIFY_*` credentials.
2. **Real order status** — PostEx tracking is already wired (`/track`).
   ⚠️ Same allowlist rule as the storefront: status/city/timestamps only. `dist`
   carries name, phone, address and COD amount and must never be echoed.
3. **Roman Urdu** — keyword matching cannot tell that "bhai rate btao" and
   "kitne ka hai" are one question. A model can.
4. **Hand off to WhatsApp** — where orders actually close in this market, and
   where the confirmation automation already lives.

### Guardrails, non-negotiable
- **Draft-first for the first week.** Agent writes, user approves from phone.
  Full auto only on intents proven correct.
- **Never auto-reply** on: complaints, refunds, damaged goods, anything naming
  a specific order in public, anything about a person.
- **Never post a price the agent did not read from Shopify** in that request.
- **Never invent stock.** Unknown → hand to a human.
- One reply per comment, ever. KV-enforced.

## 6. Open questions for the user

1. Does a Meta app already exist under the business, or is this a fresh one?
2. After a week of Layer 1: which intents does the keyword matcher get wrong,
   and which frequent questions have no automation? **That list is the spec** —
   Layer 2 gets built from the real inbox, not from assumptions.

## 7. Status

- [x] Layer 1 guide written and delivered — `docs/social/SOCIAL_AUTOMATION.html`
- [ ] Phase 0 (Shopify shipping rate) — **user, blocks Layer 1 go-live**
- [ ] Layer 1 switched on
- [ ] Meta app created / identified
- [ ] Worker built
- [ ] Screencast + App Review submitted
- [ ] Approved, app Live
