#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_assets_c17.py - placeholdere DRAFT pentru C17 SISTEMATIZARE (PIL).

REPARATIE AUDIT T5 (E1/E4): C17 nu avea folder assets/ (V39.assets XX).
Genereaza 7 JPG DRAFT (hero + 6 exec-stage), raport 3:2 (1500x1000), navy gradient,
text auriu. Axa RELUARE / SISTEM. Unice (NU clone C01). Imaginile reale ARHITECT
le inlocuieste ulterior. Text ASCII-safe. Zero em-dash.
Etichete C17 (din Studiu): REALITATE / INVENTAR / SURSA / RELUARE / EXTERNALIZARE / SUBSTITUT.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUTDIR = 'c17/assets'
W, H = 1500, 1000
NAVY_TOP = (0x1F, 0x2A, 0x44); NAVY_BOT = (0x0B, 0x10, 0x20)
GOLD = (0xB8, 0x86, 0x0B); GOLD_BRIGHT = (0xFF, 0xD4, 0x00); MUTED = (0x9A, 0xA6, 0xC0)
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def font(p, s): return ImageFont.truetype(p, s)
def tw(d, s, f): bb = d.textbbox((0, 0), s, font=f); return bb[2]-bb[0]


def wrap(d, s, f, mw):
    words = s.split(); lines = []; cur = ''
    for w in words:
        t = (cur+' '+w).strip()
        if tw(d, t, f) <= mw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


def centered(d, lines, f, y, color, gap=14):
    for ln in lines:
        w = tw(d, ln, f); d.text(((W-w)/2, y), ln, font=f, fill=color)
        bb = d.textbbox((0, 0), ln, font=f); y += (bb[3]-bb[1])+gap
    return y


def vgrad():
    img = Image.new('RGB', (W, H), NAVY_TOP); px = img.load()
    for y in range(H):
        t = y/(H-1)
        r = int(NAVY_TOP[0]+(NAVY_BOT[0]-NAVY_TOP[0])*t)
        g = int(NAVY_TOP[1]+(NAVY_BOT[1]-NAVY_TOP[1])*t)
        b = int(NAVY_TOP[2]+(NAVY_BOT[2]-NAVY_TOP[2])*t)
        for x in range(W): px[x, y] = (r, g, b)
    return img


def canvas():
    img = vgrad(); d = ImageDraw.Draw(img)
    d.rectangle([28, 28, W-28, H-28], outline=GOLD, width=3)
    return img, d


def hero(path):
    img, d = canvas()
    kick = 'TRAINITY · PACK 02 EXCEL · C17'
    w = tw(d, kick, font(FB, 34)); d.text(((W-w)/2, 150), kick, font=font(FB, 34), fill=MUTED)
    y = centered(d, wrap(d, 'SISTEMATIZAREA MUNCII RELUABILE', font(FB, 64), W-240), font(FB, 64), 300, GOLD_BRIGHT, 18)
    y = centered(d, wrap(d, 'Cum transform munca intr-un sistem reluabil?', font(FR, 40), W-320), font(FR, 40), y+30, GOLD)
    dr = 'C17 · placeholder DRAFT'; w = tw(d, dr, font(FB, 30)); d.text(((W-w)/2, H-120), dr, font=font(FB, 30), fill=MUTED)
    img.save(path, 'JPEG', quality=90); return path


def stage(path, n, label, descr):
    img, d = canvas()
    kick = 'C17 · SISTEMATIZARE · RELUARE'
    w = tw(d, kick, font(FB, 28)); d.text(((W-w)/2, 120), kick, font=font(FB, 28), fill=MUTED)
    numt = '%02d' % n; w = tw(d, numt, font(FB, 120)); d.text(((W-w)/2, 210), numt, font=font(FB, 120), fill=GOLD)
    w = tw(d, label, font(FB, 66)); d.text(((W-w)/2, 380), label, font=font(FB, 66), fill=GOLD_BRIGHT)
    centered(d, wrap(d, descr, font(FR, 34), W-320), font(FR, 34), 510, MUTED, 12)
    dr = 'C17 · exec-stage-%d · placeholder DRAFT' % n; w = tw(d, dr, font(FB, 28)); d.text(((W-w)/2, H-110), dr, font=font(FB, 28), fill=MUTED)
    img.save(path, 'JPEG', quality=90); return path


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    made = [hero(os.path.join(OUTDIR, 'hero-poster-excel-17-sistematizare.jpg'))]
    stages = [
        (1, 'REALITATE', 'Munca pe care o stii doar tu. Merge perfect, pana pleci tu.'),
        (2, 'INVENTAR', 'Inventarul componentelor reale ale muncii reluabile.'),
        (3, 'SURSA', 'O singura sursa/intrare, nu copii imprastiate.'),
        (4, 'RELUARE', 'Ordinea de reluare legata de obiecte, nu de memorie.'),
        (5, 'EXTERNALIZARE', 'Cunoasterea scoasa din cap, in structura workbook-ului.'),
        (6, 'SUBSTITUT', 'Testul substitutului: altcineva porneste din START AICI.'),
    ]
    for n, l, dsc in stages:
        made.append(stage(os.path.join(OUTDIR, 'exec-stage-%d.jpg' % n), n, l, dsc))
    for p in made:
        print('SCRIS:', p, '(%d bytes)' % os.path.getsize(p))


if __name__ == '__main__':
    main()
