# WhatsApp bridge — setup, step by step

You have an Oracle Cloud account. From here it is **4 parts**. Read each line,
do exactly that, then move to the next. Nothing here needs any coding knowledge.

Total time: about 20 minutes, most of it waiting.

---

# PART 1 — Make a key so you can get into the server

Do this **before** creating the server. It saves a lot of pain later.

**1.1** Log into <https://cloud.oracle.com>

**1.2** Top-right of the page, find the **`>_`** icon (Developer tools →
**Cloud Shell**). Click it. A black terminal opens at the bottom of the browser.
Wait until it shows a `$` prompt.

**1.3** Click inside that black area and paste this, then press Enter:

```
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N "" <<< y >/dev/null 2>&1; cat ~/.ssh/id_rsa.pub
```

**1.4** It prints one long line starting `ssh-rsa AAAA…`.
**Select that whole line and copy it.** Keep it on your clipboard.
Leave this Cloud Shell window open — you come back to it in Part 3.

---

# PART 2 — Create the free server

**2.1** Top-left **☰ menu** → **Compute** → **Instances**

**2.2** Blue button **Create instance**

**2.3** **Name:** type `kordovan-whatsapp`

**2.4** Find the box **Image and shape**. Click **Edit** (or *Change image*).
- Click **Change image** → choose **Canonical Ubuntu** → pick **22.04** → **Select image**
- Click **Change shape** → tab **Ampere** → tick **VM.Standard.A1.Flex**
  → set **OCPUs = 1**, **Memory = 6 GB** → **Select shape**

> ⚠️ **"Out of capacity for shape VM.Standard.A1.Flex"** — this happens to almost
> everyone; Oracle's free ARM capacity is heavily oversubscribed. Dubai has only
> one availability domain so there is nothing to switch to. Fix: click
> **Previous** → **Change shape** → tab **Specialty and previous generation** →
> **VM.Standard.E2.1.Micro** → **Select shape** → **Create**.
> Also Always Free, and fine for this. It has 1GB RAM, so the installer adds a
> 2GB swap file automatically — without it `npm install` runs out of memory.

**2.5** Scroll to **Networking**. A brand-new Oracle account has no network yet,
so the default "Select existing…" options are empty and greyed out. You must
create one — three clicks:

- Under **Primary network** → tick **Create new virtual cloud network**
  *(leave the auto-filled names exactly as they are)*
- Under **Subnet** → tick **Create new public subnet**
  — the word **public** matters
- Scroll to **Public IPv4 address assignment** → turn
  **Automatically assign public IPv4 address** **ON**

> The warning *"You must select a public subnet to assign a public IPv4 address"*
> disappears once the subnet is set to public. Ignore the IPv6 section entirely.

**2.6** Scroll to **Add SSH keys**. Choose **Paste public keys**.
Paste the long `ssh-rsa AAAA…` line you copied in step 1.4.

**2.7** Click **Create** (bottom left). Wait ~1 minute until the square turns
from orange **PROVISIONING** to green **RUNNING**.

**2.8** On that page, find **Public IP address** — something like `140.238.x.x`.
**Copy it.**

---

# PART 3 — Install everything (three lines)

**3.1** Go back to the black **Cloud Shell** window from Part 1.

**3.2** Paste this, replacing `YOUR_IP_HERE` with the IP from step 2.8, Enter:

```
ssh -o StrictHostKeyChecking=no ubuntu@YOUR_IP_HERE
```

The prompt changes to `ubuntu@kordovan-whatsapp:~$`. **You are now on the server.**

**3.3** Paste this one line and press Enter:

```
sudo apt-get update -qq && sudo apt-get install -y -qq git && git clone -q https://github.com/kordovanofficial-afk/KDV.git && cd KDV/tools/wa-bridge && bash install.sh
```

That is it. It downloads everything itself — no files to open, nothing to copy.

Now wait. It takes 3–5 minutes and prints progress as it goes. Do not close the
window.

**3.4** When it finishes it prints a green **DONE** box with three things.
**Copy that whole box somewhere safe** — it contains your passwords.

# PART 4 — Link WhatsApp

**4.1** From the DONE box, open the **first** link in any browser. It looks like:
```
https://something-random.trycloudflare.com/qr?k=XXXXXXXX
```
A QR code appears.

**4.2** ⚠️ **First check this:** on the business phone open
**WhatsApp → Settings → Linked devices**. Count what is listed. WhatsApp allows
about four. **If it is full, remove one you do not recognise** — otherwise
linking ours will silently kick out your POS bot.

**4.3** Still on that screen: **Link a device** → scan the QR on your browser.

**4.4** The web page changes to **✅ WhatsApp is linked**. Done.

**4.5** Bookmark the **second** link (the `/status` one). That is your dashboard —
connected or not, messages waiting, anything that went wrong.

---

# PART 5 — Send me this

From the DONE box, send me the two lines that start:
```
BRIDGE_URL=...
BRIDGE_SECRET=...
```

Then I connect the Worker and build the order messages.

---

## If something goes wrong

| What you see | What to do |
|---|---|
| "Out of capacity" creating the server | Use **VM.Standard.E2.1.Micro** instead (step 2.4) |
| Networking dropdowns empty / greyed out | Fresh account has no network. Pick **Create new virtual cloud network** + **Create new public subnet** (step 2.5) |
| "You must select a public subnet…" warning | Subnet is set to private. Choose **Create new public subnet** (step 2.5) |
| `Permission denied (publickey)` | The key in step 2.6 was not pasted correctly. Delete the instance, redo Part 2 |
| Install stops with a red error | Copy the last 10 lines and send them to me |
| Web address does not open | On the server run: `pm2 logs tunnel --lines 30 --nostream` and send me the output |
| Status page says `disconnected` | Wait 30 seconds and refresh. If it stays, open the `/qr` link and scan again |

**Getting back to the server later:** open Cloud Shell (`>_` icon) and run
`ssh ubuntu@YOUR_IP` again.

**Handy once you are on the server:**
- `pm2 list` — is everything running
- `pm2 logs wa-bridge --lines 30` — what the bridge is doing
- `pm2 restart wa-bridge` — turn it off and on again
