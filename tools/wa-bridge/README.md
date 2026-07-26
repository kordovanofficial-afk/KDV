# WhatsApp bridge — setup on a free always-on server

**Nothing runs on the office laptop.** This lives on a small free cloud server
that never sleeps. You link WhatsApp by opening a web page and scanning — no
TeamViewer, no SSH for the team.

**What this is:** a small program that holds a WhatsApp connection. It sends a
message when the Worker tells it to, and forwards customer replies back. It has
**no Shopify access**, no order data, no customer list. All the thinking happens
in the Cloudflare Worker.

---

## Step 1 — Get a free server (once, ~15 min)

**Oracle Cloud Always Free** is the recommendation: free forever, genuinely
always-on, far more powerful than we need.

1. Sign up at <https://signup.cloud.oracle.com>. A card is required for identity
   verification — **the Always Free resources are not charged**. Pick the region
   closest to Pakistan (Mumbai / Dubai / Singapore).
2. Menu → **Compute → Instances → Create Instance**
3. Image: **Ubuntu 22.04**  ·  Shape: **VM.Standard.A1.Flex**, 1 OCPU / 6 GB
   (that is inside Always Free)
4. Under SSH keys choose **Generate a key pair** and **download the private key** —
   you need it to log in. Keep it safe.
5. Create. Note the **Public IP address** it gives you.

> ⚠️ If it says "out of capacity" for A1.Flex — common in busy regions — either
> try again later, pick another region, or use the smaller **VM.Standard.E2.1.Micro**
> (also Always Free) which is plenty for this.
>
> Alternative if Oracle is painful: Google Cloud's free **e2-micro** works too.

## Step 2 — Connect to it
On Windows use **PowerShell**:
```
ssh -i C:\path\to\your-key.key ubuntu@YOUR_SERVER_IP
```
Say `yes` when it asks about the fingerprint.

## Step 3 — Install Node.js
Paste this whole block and press Enter:
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs git
node -v
```
It should print `v20.x` or higher.

## Step 4 — Put the bridge on the server
```bash
mkdir -p ~/wa-bridge && cd ~/wa-bridge
```
Then create the two files. Easiest way: run `nano server.js`, paste the contents
of `server.js`, press `Ctrl+O` `Enter` `Ctrl+X`. Repeat with `nano package.json`.

Then:
```bash
npm install
```

## Step 5 — Settings
```bash
nano .env
```
Paste this, replacing both passwords with your own long random text:
```
BRIDGE_SECRET=some-long-random-text-here
ADMIN_KEY=a-different-long-random-text
WORKER_INBOUND=https://kordovan-postex-sync.kordovan-official.workers.dev/wa-inbound
AUTH_DIR=./auth
PORT=8787
```
`Ctrl+O` `Enter` `Ctrl+X`.

📌 **Keep both passwords.** `BRIDGE_SECRET` goes into Cloudflare later.
`ADMIN_KEY` is what you use to open the status page.

## Step 6 — Keep it running forever
```bash
sudo npm install -g pm2
pm2 start server.js --name wa-bridge
pm2 save
pm2 startup
```
That last command prints one more command — **copy it, paste it, run it**. That
makes the bridge restart automatically if the server ever reboots.

Check it: `pm2 logs wa-bridge`

## Step 7 — Give it a web address
```bash
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -o cloudflared
chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/
pm2 start cloudflared --name tunnel -- tunnel --url http://localhost:8787
pm2 save
pm2 logs tunnel
```
> On an E2 (Intel) shape use `cloudflared-linux-amd64` instead of `arm64`.

In the logs you will see an address like
`https://something-random.trycloudflare.com`. **That is your bridge address.**

## Step 8 — Link WhatsApp (this is the QR step)
Open in any browser, phone or laptop:
```
https://YOUR-TUNNEL-ADDRESS/qr?k=YOUR_ADMIN_KEY
```
The pairing QR appears on screen. On the business phone:
**WhatsApp → Settings → Linked devices → Link a device** → scan it.

⚠️ **Look at that Linked devices list first.** WhatsApp allows about four. If it
is full, linking this will silently kick out the oldest — possibly the POS bot.
Remove something unused first.

When the page says **✅ WhatsApp is linked**, you are done.

## Step 9 — Send me the address
Send me the `https://…trycloudflare.com` address and I will wire the Worker to it.

> The quick tunnel address changes if the tunnel restarts. Once everything works
> I will give you the steps for a permanent named tunnel so it never changes.

---

## Checking on it any time
```
https://YOUR-TUNNEL-ADDRESS/status?k=YOUR_ADMIN_KEY
```
Shows: connected or not, how many messages are waiting, whether the 09:00–21:00
sending window is open, how many sent, and the last error if any. Refreshes itself.
Bookmark it.

## If something breaks
| Symptom | Fix |
|---|---|
| Status shows `disconnected` | Wait 30s, it retries by itself. If it persists, open `/qr` and re-link |
| `LOGGED OUT` in the logs | `cd ~/wa-bridge && rm -rf auth && pm2 restart wa-bridge`, then scan `/qr` again |
| Nothing sends 9pm–9am | Working as designed. Messages queue until morning |
| Tunnel address stopped working | `pm2 logs tunnel` shows the new one; send it to me |
| `FATAL: BRIDGE_SECRET and ADMIN_KEY…` | Step 5 — the file must be `.env` in `~/wa-bridge` |

Useful: `pm2 restart wa-bridge` · `pm2 logs wa-bridge` · `pm2 list`

## Safety built in
- **3–10 second random gap** between messages, never bursts
- **09:00–21:00 PKT only** — anything else queues until morning
- Checks the number is on WhatsApp **before** sending
- 1:1 chats only — ignores groups, status and our own messages
- Never replies on its own; it forwards to the Worker, which stays silent unless
  the sender matches an order awaiting confirmation
