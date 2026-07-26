# WhatsApp bridge — setup on the office laptop

Follow in order. Nothing here needs coding — copy, paste, run.

**What this is:** a small program that holds a WhatsApp connection and does two
things — sends a message when told to, and forwards customer replies onward. It
has **no access to Shopify**, no order data, no customer list. All the thinking
happens in the Cloudflare Worker.

---

## Step 1 — Install Node.js
Download the **LTS** version from <https://nodejs.org> and install it.
Check it worked: open Command Prompt / Terminal and run `node -v`.
You should see something like `v20.x` or higher.

## Step 2 — Put the files on the laptop
Copy this whole `wa-bridge` folder somewhere permanent, e.g. `C:\kordovan\wa-bridge`.
**Do not put it inside the POS bot's folder** — they must stay separate.

## Step 3 — Install
Open Command Prompt **in that folder** and run:
```
npm install
```
One-time, takes a minute.

## Step 4 — Settings
Rename `.env.example` to **`.env`** and open it in Notepad.
Change only this line, to any long random text (letters and numbers, no spaces):
```
BRIDGE_SECRET=change-me-to-a-long-random-string
```
📌 **Keep a copy of that value** — the exact same text goes into Cloudflare later.
Leave everything else as it is.

## Step 5 — Start it and link WhatsApp
```
npm start
```
A QR code appears in the window. On the phone with the business WhatsApp:
**WhatsApp → Settings → Linked devices → Link a device → scan it.**

⚠️ **Before scanning, look at that Linked devices list.** WhatsApp allows about
four. If it is already full, linking this will silently kick out the oldest —
which could be your POS bot. Remove something unused first if needed.

When it says `[wa] connected`, it is live. **Leave this window open.**

## Step 6 — Check it
Open a browser on the laptop: <http://localhost:8787/health>
You should see `{"ok":true,"connected":true,...}`.

## Step 7 — Give it an address on the internet
The Cloudflare Worker needs to reach this laptop. Cloudflare Tunnel does that for
free, with no router changes.

1. Download `cloudflared` from
   <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/>
2. In a **second** Command Prompt window:
```
cloudflared tunnel --url http://localhost:8787
```
3. It prints an address like `https://something-random.trycloudflare.com`.
   **Send me that address** and I will wire the Worker to it.

> The quick tunnel above is fine for testing but the address changes every
> restart. Once it works I will give you the steps for a permanent named tunnel.

---

## Keeping it running
- The laptop must stay **on and awake**. Set power settings to never sleep.
- Both windows (`npm start` and `cloudflared`) must stay open.
- If the laptop restarts, start both again. Orders are unaffected — the Worker
  treats a failed send as non-fatal and never blocks the delivery sync.

## If something breaks
| Symptom | Fix |
|---|---|
| `LOGGED OUT, delete auth dir and re-scan` | Delete the `auth` folder, `npm start`, scan again |
| `/health` shows `"connected":false` | Check the laptop's internet, wait 30s — it retries automatically |
| Nothing sends between 9pm and 9am | Working as designed. Messages queue until morning |
| `FATAL: BRIDGE_SECRET is not set` | Step 4 — the file must be named `.env`, not `.env.example` |

## Safety built in
- **3–10 second random gap** between messages, never in bursts
- **Only 09:00–21:00 PKT**; anything else waits for morning
- Checks the number is on WhatsApp **before** sending
- Only handles 1:1 chats — ignores groups, status and our own messages
- Never replies on its own; it only forwards to the Worker, which stays silent
  unless the sender matches an order awaiting confirmation
