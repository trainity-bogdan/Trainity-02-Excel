#!/usr/bin/env python3
"""
strip_watermark.py - scoate watermark-ul Gemini / Banana 2 (steluta ✦)
din coltul dreapta-jos al imaginilor generate.

Gemini/Imagen stampileaza AUTOMAT o steluta in coltul dreapta-jos pe ORICE
output. Nu se poate elimina prin prompt (reapare la fiecare generare). Acest
script o curata prin clonare verticala: acopera caseta din coltul dreapta-jos
cu o felie identica luata imediat DEASUPRA ei, continuand gradientul/textura
suprafetei. Pe fundalul matte-black al seriei e invizibil.

Uz:
  python3 strip_watermark.py IN.jpg [OUT.jpg]
  python3 strip_watermark.py IN.jpg OUT.jpg --w 0.11 --h 0.14
Daca OUT lipseste, suprascrie IN pe loc.

Regula R-V49.1: orice imagine Banana/Gemini integrata in proiect trece prin
acest script INAINTE de a ajunge in cNN/assets/. Fara intrebari.
"""
import sys
from PIL import Image, ImageFilter


def strip(inp, outp=None, wfrac=0.11, hfrac=0.14, feather=6):
    im = Image.open(inp).convert("RGB")
    W, H = im.size
    # caseta watermark = coltul dreapta-jos
    bw = max(8, int(W * wfrac))
    bh = max(8, int(H * hfrac))
    x0, y0 = W - bw, H - bh
    # sursa = aceeasi coloana, deplasata in sus cu inaltimea casetei
    sy0 = y0 - bh
    if sy0 < 0:
        sy0 = 0
    patch = im.crop((x0, sy0, W, sy0 + bh))
    # blur usor doar pe petic, sa nu ramana margine vizibila
    patch = patch.filter(ImageFilter.GaussianBlur(feather))
    im.paste(patch, (x0, y0))
    outp = outp or inp
    im.save(outp, quality=92)
    print(f"strip_watermark: {inp} -> {outp} | caseta {bw}x{bh}px @ ({x0},{y0})")
    return outp


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    inp = sys.argv[1]
    outp = None
    wf, hf = 0.11, 0.14
    rest = sys.argv[2:]
    i = 0
    while i < len(rest):
        a = rest[i]
        if a == "--w":
            wf = float(rest[i + 1]); i += 2
        elif a == "--h":
            hf = float(rest[i + 1]); i += 2
        else:
            outp = a; i += 1
    strip(inp, outp, wf, hf)
