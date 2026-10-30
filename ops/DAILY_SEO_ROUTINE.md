# Daily SEO routine (scheduled task)

Set up in claude.ai → Code → Routines (or Scheduled tasks) → New:
- **Schedule:** every day 08:38, time zone Asia/Karachi (runs in the cloud, no laptop needed)
- **Repository:** kordovanofficial-afk/KDV
- **Connectors:** Shopify, Kordovan GSC
- **Notifications:** push on
- **Prompt:** paste the block below.

✅ Set up by the owner in the Claude app (Oct 30 2026). The connector-less copy made from a session was deleted.

```
Daily SEO routine for Kordovan (kordovanleather.com, Shopify store, Pakistani leather brand). Read CLAUDE.md in the repo first. Its hard rules override anything in this prompt (FREE options only, never mention the workshop city in new content, Humanizer rules on all customer-facing text, never invent reviews, ask before any push to the `kordovan` branch).

GOAL: find and fix SEO problems and move forward SEO work that leads to SALES, not vanity traffic.

1. Search Console (Kordovan GSC connector, always pass siteUrl "https://kordovanleather.com/"; its dimension filters are ignored, so pull unfiltered and filter yourself). Compare the last 7 days with the 7 before (data lags 2-3 days). Flag: real drops in clicks or position on money pages (collections and products), and page-2 chances (position 6-20 with real impressions) on buying-intent queries.
2. Shopify catalogue health on ACTIVE products: images missing alt text, missing SEO title or description, empty or stub descriptions, products with no images, sold-out bestsellers, jackets or footwear missing custom.made_to_order = true, and stale or false wording anywhere (the workshop city name, "4-7 days", "50%" deposit, unqualified "free shipping"; free delivery is only over Rs 5,500).
3. URL redirects that point at a product or page that is deleted or not active, and redirect chains.
4. Look at the open SEO items in CLAUDE.md and note whether any can move forward.

YOU MAY APPLY THESE WITHOUT ASKING (max 50 writes per run, read every write back to verify):
 a. Alt text on images that have none, using the filename-based method in CLAUDE.md ("ALT TEXT - the method that worked"). Never overwrite an existing alt. Vegan products must never be called leather.
 b. Point broken redirects (target deleted or draft) at the nearest equivalent active product, or failing that the category collection. Never the homepage. Re-verify afterwards.

NEVER DO AUTOMATICALLY: theme edits or any git push that deploys, product/collection/blog copy, SEO titles or descriptions, prices, inventory, discounts, Meta ads, reviews, anything paid. For these, DRAFT the fix in the report (copy written to Humanizer rules) so the owner can approve it.

If the Shopify or Kordovan GSC connector is not available in this session, say so at the top of the report and do what you can with the rest.

REPORT (the final message of the session): short and plain. (1) What you changed, with handles/IDs. (2) Problems found. (3) Top 3 proposed actions ranked by likely sales impact, each with the drafted copy or exact change ready to approve. If nothing notable happened, say so in two lines. Do not commit files to the repo.
```
