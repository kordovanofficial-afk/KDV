# Kordovan — Google Search Console MCP connector · Setup (100% free)

This gives Claude live read access to your Search Console data via a small
Cloudflare Worker. No coding, all in the browser. Cost: **$0** (Cloudflare free
tier + Google Search Console API is free).

**Prereqs already done:** ✅ Google Cloud project `kordovan-seo` · ✅ Search Console
API enabled · ✅ service account `kdv-seo-reader@kordovan-seo.iam.gserviceaccount.com`
created + JSON key downloaded · ✅ service account added as a user in Search Console.

---

## Step 1 — Create the Worker
1. Go to **dash.cloudflare.com** → **Workers & Pages** → **Create** → **Create Worker**.
2. Name it `kdv-seo-mcp` → **Deploy** (deploys the default hello-world for now).
3. Click **Edit code**. Delete everything in the editor.
4. Open **`worker.js`** (in this folder), copy ALL of it, paste into the editor.
5. Click **Deploy** (top right).

## Step 2 — Add the secrets
In the Worker → **Settings** → **Variables and Secrets** → add these four
(click **+ Add**, choose **Secret** for the private key, **Text** is fine for the rest):

| Name | Type | Value |
|---|---|---|
| `GOOGLE_SA_EMAIL` | Text | `kdv-seo-reader@kordovan-seo.iam.gserviceaccount.com` |
| `GOOGLE_SA_PRIVATE_KEY` | **Secret** | the `private_key` value from your downloaded JSON (see note) |
| `MCP_SECRET` | **Secret** | a random string you invent, e.g. `kdv-9f3a7c2b1e` (no spaces) |
| `GSC_SITE` | Text | `sc-domain:kordovanleather.com` |

**Getting `GOOGLE_SA_PRIVATE_KEY`:** open the downloaded `.json` key file in a text
editor. Find `"private_key": "-----BEGIN PRIVATE KEY-----\n....\n-----END PRIVATE KEY-----\n"`.
Copy the **value between the quotes** (the whole `-----BEGIN…END-----` block, including
the `\n` bits) and paste it as the secret. The Worker handles the `\n` automatically.

**`GSC_SITE` note:** if your Search Console property is a **Domain** property, use
`sc-domain:kordovanleather.com` (above). If it's a **URL-prefix** property instead,
use the full URL, e.g. `https://www.kordovanleather.com/`. (You can run the
`gsc_list_sites` tool later to see the exact string Google expects.)

After adding all four → **Deploy** again so the secrets take effect.

## Step 3 — Get your Worker URL
On the Worker's overview page you'll see its URL, like
`https://kdv-seo-mcp.<your-subdomain>.workers.dev`.

Your **connector URL** = that, plus `/mcp/` + your `MCP_SECRET`:
```
https://kdv-seo-mcp.<your-subdomain>.workers.dev/mcp/kdv-9f3a7c2b1e
```
Quick test: open that URL in a browser (GET). You should see
*"Kordovan GSC MCP server — OK."* If you see "Not found", the `MCP_SECRET` in the URL
doesn't match the secret you set.

## Step 4 — Add it to Claude
1. In **claude.ai** → **Settings** → **Connectors** → **Add custom connector**.
2. Name: `Kordovan GSC`. URL: your connector URL from Step 3.
3. Save. If it asks about authentication, choose **No authentication** (the secret is
   already baked into the URL).
4. Back in the chat, make sure the connector is **enabled for this conversation**
   (connector toggle), then tell me **"GSC connector added"** and I'll test it live.

---

## What I'll be able to do once it's connected
- `gsc_list_sites` — confirm the property + exact site string
- `gsc_query` — top queries, top pages, clicks/impressions/CTR/position, by date/country/device
- `gsc_list_sitemaps` — sitemap submission + indexing status
- `gsc_inspect_url` — is a page indexed? coverage, last crawl, canonical, rich-results

## Security notes
- The private key lives only as a Cloudflare **Secret** (never in this repo, never in chat).
- The Worker only answers on the secret path (`/mcp/<MCP_SECRET>`) — anyone hitting the
  base URL gets 404. Treat the connector URL like a password.
- The service account is **read-only** (`webmasters.readonly`) — it cannot change
  anything in Search Console.
- To revoke access anytime: delete the Worker, rotate `MCP_SECRET`, or remove the
  service account from Search Console → Settings → Users and permissions.

## Adding Bing / GA4 later
This same Worker can be extended: Bing Webmaster (simple API key) and GA4 (add the
"Google Analytics Data API" in the same Cloud project + add the service account as a
Viewer on the GA4 property). Ping me and I'll hand you an updated `worker.js`.

## If Claude's connector won't accept the URL
Some Claude plans gate custom connectors. Fallback (still free, still live-ish): I can
give you a version that runs on a **Cron trigger** — the Worker pulls your GSC data on a
schedule and commits a JSON snapshot to this repo, which I can always read. Tell me if
you hit a wall and we'll switch to that.
