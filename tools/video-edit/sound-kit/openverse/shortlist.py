"""Build a CC0-only Openverse shortlist for the Kordovan foley cues (book §17).

  python3 shortlist.py            # search -> shortlist.json + SHORTLIST.md
  python3 shortlist.py --download # fetch the picks into ./files/ (needs cdn.freesound.org
                                  # and upload.wikimedia.org allowed in the network policy)

CC0 only, so every file is safe for paid ads with no credit line. Creator and source are
still recorded for our own audit trail.
"""
import json, re, sys, time, urllib.parse, urllib.request, pathlib

API = "https://api.openverse.org/v1/audio/"
HERE = pathlib.Path(__file__).parent
PICKS = 4          # keep the best few per cue
MAX_S = 20         # foley, not ambience beds
# Off-brand or wrong-object matches seen in the first run: Lingua Libre word recordings ("LL-…"),
# electrical switches, horror, digital/synth, plastic, vehicle.
BLOCK = re.compile(r"^LL-|amplifier|heater|fan|flesh|horror|digital|synth|plastic|seat ?belt|vehmech|car\b|metallicscratch", re.I)
CUES = {
    "leather_creak":   ["leather creak", "leather stretch", "leather rubbing"],
    "snap_button":     ["press stud", "snap fastener", "popper button", "wallet snap"],
    "zip":             ["zipper jacket", "zip up"],
    "card_slide":      ["card slide", "plastic card"],
    "cash_paper":      ["counting money", "paper money", "money bills"],
    "buckle":          ["belt buckle", "metal buckle"],
    "drop_on_wood":    ["wallet drop table", "object drop wood table"],
    "fabric_cloth":    ["jacket cloth movement", "clothing rustle"],
    "keys":            ["keys jingle"],
    "sewing":          ["hand sewing", "sewing fabric", "thread pull"],
    "workshop_tone":   ["workshop room tone", "room tone"],
    "soft_whoosh":     ["soft whoosh", "cloth whoosh"],
}

def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "kordovan-video/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def search(q):
    qs = urllib.parse.urlencode({"q": q, "license": "cc0", "page_size": 20})
    return json.loads(get(f"{API}?{qs}"))["results"]

def build():
    out = {}
    for cue, queries in CUES.items():
        seen, rows = set(), []
        for q in queries:
            try:
                res = search(q)
            except Exception as e:
                print(f"  {q}: {e}"); continue
            for r in res:
                d = (r.get("duration") or 0) / 1000
                if r["id"] in seen or r.get("license") != "cc0" or not (0.2 <= d <= MAX_S):
                    continue
                if r.get("mature") or BLOCK.search(r["title"] or ""):
                    continue
                seen.add(r["id"])
                rows.append({"id": r["id"], "title": r["title"], "creator": r.get("creator"),
                             "source": r.get("source"), "duration_s": round(d, 2),
                             "filetype": r.get("filetype"), "url": r["url"],
                             "landing": r.get("foreign_landing_url"), "license": "cc0",
                             "query": q})
            time.sleep(3.2)   # anonymous limit: 20 searches/min
        out[cue] = rows[:PICKS]
        print(f"{cue}: {len(rows)} CC0 candidates, kept {len(out[cue])}")
    (HERE / "shortlist.json").write_text(json.dumps(out, indent=1))
    lines = ["# Openverse CC0 shortlist (auto-built, book §17)", "",
             "Every sound here is **CC0**: safe for paid ads, no credit needed. Audition before use; "
             "our own recorded foley (`../README.md`) always beats these.", ""]
    for cue, rows in out.items():
        lines += [f"## {cue}", "| # | Title | Creator | Source | Length |", "|---|---|---|---|---|"]
        for i, r in enumerate(rows, 1):
            lines.append(f"| {i} | [{r['title'][:60]}]({r['landing']}) | {r['creator']} | {r['source']} | {r['duration_s']} s |")
        lines.append("")
    (HERE / "SHORTLIST.md").write_text("\n".join(lines))

def download():
    out = json.loads((HERE / "shortlist.json").read_text())
    dest = HERE / "files"; dest.mkdir(exist_ok=True)
    credits = ["# CREDITS (all CC0, kept for audit)", ""]
    for cue, rows in out.items():
        for i, r in enumerate(rows, 1):
            ext = (r.get("filetype") or r["url"].rsplit(".", 1)[-1]).lower()
            f = dest / f"{cue}_{i:02d}.{ext}"
            try:
                f.write_bytes(get(r["url"])); ok = "ok"
            except Exception as e:
                ok = f"FAILED ({e})"
            print(f.name, ok)
            credits.append(f"- `{f.name}` · \"{r['title']}\" by {r['creator']} · CC0 · {r['landing']}")
    (dest / "CREDITS.md").write_text("\n".join(credits) + "\n")

if __name__ == "__main__":
    download() if "--download" in sys.argv else build()
