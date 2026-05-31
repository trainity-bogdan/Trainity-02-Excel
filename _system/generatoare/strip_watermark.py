#!/usr/bin/env python3
"""
strip_watermark.py - scoate watermark-ul Gemini / Banana 2 (steluta ✦)
din coltul dreapta-jos al imaginilor generate.

Gemini/Imagen stampileaza AUTOMAT o steluta in coltul dreapta-jos pe ORICE
output. Nu se poate elimina prin prompt (reapare la fiecare generare). Acest
script o DETECTEAZA (pixeli luminosi in sfertul dreapta-jos pe fundal inchis),
ii afla caseta exacta, apoi o acopera cu un petic clonat din STANGA (aceeasi
luminozitate pe randul respectiv), cu feather pe margini. Pe matte-black e
invizibil. Daca nu gaseste nimic luminos, cade pe o caseta fixa in colt.

Uz:
  python3 strip_watermark.py IN [OUT]          # auto-detect
  python3 strip_watermark.py IN OUT --thr 260  # prag luminozitate detectie
Daca OUT lipseste, suprascrie IN pe loc.

Regula R-V49.1: orice imagine Banana/Gemini integrata in proiect trece prin
acest script INAINTE de a ajunge in cNN/assets/. Fara intrebari.
"""
import sys
from PIL import Image, ImageFilter, ImageDraw


def detect_sparkle(im, thr=280):
    """Caseta steluței ALBE din coltul dreapta-jos, sau None.

    Cauta DOAR in coltul extrem (ultimii ~14% latime, ~17% inaltime) ca sa nu
    prinda obiectul. Cere pixeli ALB-cenusii (toate canalele ridicate) ca sa
    excluda reflexiile amber (#FFD400 = albastru scazut)."""
    W, H = im.size
    px = im.load()
    x_from = int(W * 0.86)
    y_from = int(H * 0.83)
    minx = miny = 10**9
    maxx = maxy = -1
    for y in range(y_from, H):
        for x in range(x_from, W):
            r, g, b = px[x, y][:3]
            # alb-cenusiu: luminos SI cu albastru prezent (nu amber)
            if r + g + b > thr and b > 90 and min(r, g, b) > 70:
                minx = min(minx, x); maxx = max(maxx, x)
                miny = min(miny, y); maxy = max(maxy, y)
    if maxx < 0:
        return None
    return (minx, miny, maxx, maxy)


def strip(inp, outp=None, thr=280, pad=10):
    im = Image.open(inp).convert("RGB")
    W, H = im.size
    bb = detect_sparkle(im, thr)
    if bb:
        x0, y0, x1, y1 = bb
        x0 = max(0, x0 - pad); y0 = max(0, y0 - pad)
        x1 = min(W, x1 + pad); y1 = min(H, y1 + pad)
        bw, bh = x1 - x0, y1 - y0
        # sursa = acelasi rand, deplasata la STANGA cu latimea casetei + gap
        gap = bw
        sx0 = max(0, x0 - bw - gap)
        patch = im.crop((sx0, y0, sx0 + bw, y1))
        mode = "auto"
    else:
        # fallback: caseta fixa in colt, clonata de deasupra
        bw, bh = max(8, int(W * 0.10)), max(8, int(H * 0.13))
        x0, y0 = W - bw, H - bh
        patch = im.crop((x0, max(0, y0 - bh), x0 + bw, y0 + bh - bh + bh))
        patch = patch.crop((0, 0, bw, bh))
        mode = "fallback"
    # feather: masca cu colturi moi ca peticul sa nu lase margine
    patch = patch.filter(ImageFilter.GaussianBlur(2))
    mask = Image.new("L", (bw, bh), 0)
    d = ImageDraw.Draw(mask)
    d.rectangle((0, 0, bw, bh), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(6))
    im.paste(patch, (x0, y0), mask)
    outp = outp or inp
    im.save(outp, quality=92)
    print(f"strip_watermark[{mode}]: {inp} -> {outp} | patch {bw}x{bh}px @ ({x0},{y0})")
    return outp


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    inp = sys.argv[1]
    outp = None
    thr = 280
    rest = sys.argv[2:]
    i = 0
    while i < len(rest):
        if rest[i] == "--thr":
            thr = int(rest[i + 1]); i += 2
        else:
            outp = rest[i]; i += 1
    strip(inp, outp, thr)
