# Kordovan — Hosting & Email Migration Guide

**Goal:** cancel the TMDHosting "Starter" plan ($180/yr) and run email for free on
Zoho Mail — total yearly cost drops from ~$200 to ~$20 (just the domain).
The website is untouched throughout: it's hosted by Shopify, and we copy the DNS
records verbatim so the store (and your running ads) never blip.

**Final structure (decided):**

| Zoho mailbox (free seat) | Receives as aliases |
|---|---|
| `admin@kordovanleather.com` | `sales@`, `daraz@` |
| `asadj@kordovanleather.com` | `marketing@`, `social@` |
| `umair@kordovanleather.com` | — |
| `contact@kordovanleather.com` | — (public address on the new theme) |
| `corporate@kordovanleather.com` | — |

Mail is read via **Zoho webmail (mail.zoho.com)** and the **Zoho Mail mobile app**
(free plan has no IMAP, so Thunderbird is retired for daily use — it becomes the
offline archive of all old mail instead).

**Deleted already:** `customercare.usa@`, `shahid.butt@us.` ✓
**To retire with the hosting:** the `kordovan` system catch-all (check it first).

**Golden rule: never cancel the hosting until Phases 0–4 are done and tested.**
The hosting is paid up ~9 more months, so there is zero time pressure.

---

## Phase 0 — Prep (do now)

1. **Renew the domain** at TMD when it comes due (~1 month) — $19.99 as normal.
   (Optional next year: transfer to Cloudflare Registrar ≈ $10/yr. Never transfer
   within 45 days of a renewal/expiry.)
2. **Check the `kordovan` system mailbox** (552 MB) in cPanel webmail — it's the
   catch-all. Forward/save anything important to `admin@`.
3. **Archive all old mail locally in Thunderbird** (this replaces server migration
   and costs nothing):
   - In Thunderbird, for each account: right-click → **New Folder** under
     **Local Folders** (e.g. `Archive-admin`), then select all messages in each
     IMAP folder (Ctrl+A) and **drag them into the Local Folder** (or right-click
     → Copy To). Wait for each copy to finish.
   - Do this for every mailbox you care about (admin, asadj, umair, contact,
     corporate, sales, marketing, social, daraz + the catch-all if needed).
   - Result: complete offline history on your PC, independent of any server.
     Back up the Thunderbird profile folder to a USB/drive for safety.

## Phase 1 — Set up Zoho Mail (free)

1. Go to **zoho.com/mail** → Pricing → scroll to the bottom → **"Forever Free
   Plan"** (it's deliberately hard to find — 5 users, 5 GB each, one domain).
2. Sign up (suggest using `admin@kordovanleather.com` as the registration email —
   it still works on TMD right now).
3. **Add domain** `kordovanleather.com`. Zoho asks you to verify ownership:
   it shows a **TXT record** (like `zoho-verification=zb…`).
4. In **TMD cPanel → Zone Editor** for kordovanleather.com → **Add Record → TXT**,
   paste exactly what Zoho shows. Back in Zoho, click **Verify** (can take
   minutes–hours).
5. **Create the 5 users:** admin, asadj, umair, contact, corporate — each with a
   strong password. Enable 2FA on `admin@` (the org owner) at minimum.
6. **Create the aliases** (Zoho Admin Console → Users → select user → Email
   aliases → Add):
   - admin ← `sales@kordovanleather.com`, `daraz@kordovanleather.com`
   - asadj ← `marketing@kordovanleather.com`, `social@kordovanleather.com`
7. **Do NOT change MX records yet.** Mail keeps flowing to TMD until Phase 3.

## Phase 2 — Move DNS to Cloudflare (free) — prepared, not switched

Why: your DNS currently lives on TMD's nameservers, which die with the hosting.
Cloudflare Free replaces it permanently at $0.

1. Create a free account at **cloudflare.com** → **Add a site** →
   `kordovanleather.com` → Free plan. Cloudflare auto-scans existing records.
2. **Cross-check every record against TMD cPanel → Zone Editor** — the scan can
   miss records. The ones that MUST exist (copy values verbatim from cPanel):
   - `A` record for `kordovanleather.com` (apex) → Shopify's IP (typically
     `23.227.38.x` — copy whatever cPanel shows)
   - `CNAME www` → `shops.myshopify.com` (or as shown in cPanel)
   - `CNAME account` → (as shown in cPanel — Shopify customer accounts)
   - Any other records cPanel has (TXT/SPF, etc.) — copy them all for now.
3. **Set the Shopify records to "DNS only" (grey cloud), not proxied (orange).**
   Shopify manages its own SSL; proxying can break checkout/SSL.
4. **Add the Zoho records in Cloudflare now** (so mail cuts over the moment the
   nameservers switch):
   - MX: `mx.zoho.com` priority 10 · `mx2.zoho.com` 20 · `mx3.zoho.com` 50
     (use exactly the hosts Zoho's setup page shows you)
   - TXT (SPF): `v=spf1 include:zohomail.com ~all`
     *(if cPanel had an old SPF record for TMD, do NOT copy that one — replace
     with this; a domain must have only ONE SPF record)*
   - TXT (DKIM): in Zoho Admin → Domains → DKIM → generate; paste the
     `zmail._domainkey` TXT it gives you.
   - TXT (DMARC): name `_dmarc`, value `v=DMARC1; p=none; rua=mailto:admin@kordovanleather.com`
     (monitor mode; tighten to `p=quarantine` after a month of clean reports).
5. **The switch:** Cloudflare shows you 2 nameservers. In TMD's **domain**
   management (Manage domain name → Nameservers — this is the domain product,
   not the hosting), replace TMD's nameservers with Cloudflare's pair.
   - Do this at night (PKT). Propagation: minutes to a few hours.
   - From this moment: website serves from the same Shopify records (no change,
     no downtime) and **new mail starts arriving in Zoho, not TMD**.

## Phase 3 — Cutover checks (same night + next morning)

- Website: open `kordovanleather.com`, `www.`, and log into a customer account —
  all load with the padlock (SSL) intact.
- From an outside account, send a test email **to all 9 addresses** (5 mailboxes
  + 4 aliases) → each arrives in the right Zoho inbox.
- Reply from Zoho webmail as `contact@` and as an alias (`sales@`) → arrives, and
  in Gmail "show original" shows SPF=pass, DKIM=pass.
- Place a test order on the store → Shopify's confirmation email still sends
  (Shopify sends these itself; unaffected by MX).
- Check Zoho's mobile app logins for all three of you.

## Phase 4 — Parallel safety window (1–2 weeks)

- The TMD hosting keeps running (already paid) but no longer receives new mail.
- Once in the window, glance at TMD webmail for any last stragglers delivered
  before the switch; forward anything needed to Zoho.
- Confirm nothing else references the hosting (it doesn't — the site was always
  on Shopify, and Phase 0 archived all old mail locally).

## Phase 5 — Kill the cost

- TMD client area → **Manage web hosting → Billing → disable auto-renew** on the
  Starter package. It lapses at the end of the paid term — $180/yr gone.
- Keep: domain registration ($19.99/yr) + Cloudflare DNS (free) + Zoho Free ($0).
- **New total: ~$20/yr.**

---

### Quick reference — final DNS at Cloudflare

| Type | Name | Value | Note |
|---|---|---|---|
| A | @ | (Shopify IP, copy from cPanel) | DNS only (grey cloud) |
| CNAME | www | shops.myshopify.com | DNS only |
| CNAME | account | (copy from cPanel) | DNS only |
| MX | @ | mx.zoho.com (10), mx2 (20), mx3 (50) | from Zoho setup page |
| TXT | @ | zoho-verification=… | domain verification |
| TXT | @ | v=spf1 include:zohomail.com ~all | the ONLY SPF record |
| TXT | zmail._domainkey | (from Zoho DKIM page) | DKIM |
| TXT | _dmarc | v=DMARC1; p=none; rua=mailto:admin@kordovanleather.com | monitor first |
