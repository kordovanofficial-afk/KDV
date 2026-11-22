# Product URL cleanup — APPROVED by Founder Nov 22 2026, RUN on Wed Dec 2 (after the Blessed Friday revert)
30 products (kodo-vertical-2-0 dropped from the Nov 21 list: it is already clean). Map: `handle_map.json` (old → new).
Method: `productUpdate(product:{id, handle:NEW, redirectNewHandle:true})` → Shopify creates a 301 from the old URL
(query strings / utm kept). ≤29 aliases per call.
Pre-checks on the day: (1) each NEW handle is free (`productByHandle`), (2) theme has no hard-coded old handles
(checked Nov 22 on origin/kordovan: none), (3) BF revert finished.
After: read back handles + `urlRedirects(query:"path:/products/OLD")` for each; Merchant Center + Meta catalogue
pick up the new URLs on the next feed sync. Revert = productUpdate back to OLD handle (redirect auto-handled).
