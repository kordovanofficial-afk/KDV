import sys, numpy as np, potrace
from PIL import Image
im = Image.open(sys.argv[1]).convert("L")
a = np.array(im) < 128
bm = potrace.Bitmap(a)
plist = bm.trace(turdsize=20, alphamax=1.0, opticurve=True, opttolerance=0.2)
parts=[]
for c in plist:
    if len(c.segments)<=4: continue
    s=c.start_point; d=[f"M{s.x:.1f},{s.y:.1f}"]
    for seg in c.segments:
        if seg.is_corner: d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        else: d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
    d.append("Z"); parts.append("".join(d))
w,h=im.size
open(sys.argv[2],"w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path fill-rule="evenodd" d="{" ".join(parts)}"/></svg>')
print(len(parts),"subpaths",w,h)
