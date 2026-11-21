#!/usr/bin/env python3
"""Blessed Friday 2026: build apply/revert + stock-buffer batches from price_snapshot.json.

Re-run after refreshing `available` in price_snapshot.json from a live read (Nov 26).
Writes: apply_N.graphql, revert_N.graphql, stock_buffer.json,
        stock_buffer_apply.graphql, stock_buffer_revert.graphql
No network calls; it only writes files in this folder.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BATCH = 29            # aliased mutations per call (CLAUDE.md gotcha)
BUFFER_TO = 10        # Founder Nov 9: in-stock clearance variants raised to 10
URI = "kordovan://blessed-friday-2026/stock-buffer"

snap = json.load(open(os.path.join(HERE, "price_snapshot.json")))
loc = snap["location"]
rows = snap["variants"]

# Hard guard: every line must carry a unit cost and a sale price below the regular price.
for r in rows:
    assert r["cost"] and r["cost"] > 0, f"no cost: {r['product']} {r['variant']}"
    assert r["sale"] < float(r["price"]), f"sale >= price: {r['product']} {r['variant']}"

# ---- prices: one productVariantsBulkUpdate per product
products = {}
for r in rows:
    products.setdefault(r["pid"], []).append(r)
pids = list(products)

def cap_literal(v):
    return "null" if v is None else f'"{v}"'

for f in os.listdir(HERE):
    if (f.startswith("apply_") or f.startswith("revert_")) and f.endswith(".graphql"):
        os.remove(os.path.join(HERE, f))

for n, start in enumerate(range(0, len(pids), BATCH), 1):
    chunk = pids[start:start + BATCH]
    ap, rv = [], []
    for i, pid in enumerate(chunk):
        vs = products[pid]
        a = ",".join(f'{{id:"{v["vid"]}",price:"{v["sale"]}",compareAtPrice:"{v["price"]}"}}' for v in vs)
        b = ",".join(f'{{id:"{v["vid"]}",price:"{v["price"]}",compareAtPrice:{cap_literal(v["cap"])}}}' for v in vs)
        ap.append(f'p{i}: productVariantsBulkUpdate(productId:"{pid}", variants:[{a}]){{ userErrors{{field message}} }}')
        rv.append(f'p{i}: productVariantsBulkUpdate(productId:"{pid}", variants:[{b}]){{ userErrors{{field message}} }}')
    open(os.path.join(HERE, f"apply_{n}.graphql"), "w").write("mutation { " + " ".join(ap) + " }")
    open(os.path.join(HERE, f"revert_{n}.graphql"), "w").write("mutation { " + " ".join(rv) + " }")

# ---- stock buffer: only in-stock variants below 10; sold-out (<=0) and >=10 untouched
buf = []
for r in rows:
    q = r["available"]
    if 0 < q < BUFFER_TO:
        buf.append({"product": r["product"], "variant": r["variant"], "vid": r["vid"],
                    "inventoryItemId": r["inventoryItemId"], "real": q, "added": BUFFER_TO - q})
json.dump({"location": loc, "read_at": snap["read_at"], "buffer_to": BUFFER_TO,
           "total_added": sum(b["added"] for b in buf), "variants": buf},
          open(os.path.join(HERE, "stock_buffer.json"), "w"), indent=1, ensure_ascii=False)

def adj(changes, key, ref):
    return ("mutation { inventoryAdjustQuantities(input:{reason:\"correction\", name:\"available\", "
            f"referenceDocumentUri:\"{ref}\", changes:[{changes}]}}) @idempotent(key:\"{key}\") "
            "{ userErrors{field message} inventoryAdjustmentGroup{ changes{ name delta quantityAfterChange item{ id } } } } }")

# apply: changeFromQuantity = recorded real qty -> fails (changes nothing) if stock moved since the read
apply_ch = ",".join(f'{{inventoryItemId:"{b["inventoryItemId"]}",locationId:"{loc}",delta:{b["added"]},changeFromQuantity:{b["real"]}}}' for b in buf)
# revert: subtract exactly `added`; no changeFromQuantity (sales during the sale must stay counted)
revert_ch = ",".join(f'{{inventoryItemId:"{b["inventoryItemId"]}",locationId:"{loc}",delta:{-b["added"]},changeFromQuantity:null}}' for b in buf)
open(os.path.join(HERE, "stock_buffer_apply.graphql"), "w").write(adj(apply_ch, "kdv-bf2026-buffer-apply", URI + "/apply"))
open(os.path.join(HERE, "stock_buffer_revert.graphql"), "w").write(adj(revert_ch, "kdv-bf2026-buffer-revert", URI + "/revert"))

print(f"{len(pids)} products, {len(rows)} variants, {n} price batch(es); "
      f"buffer {len(buf)} variants, +{sum(b['added'] for b in buf)} units")
