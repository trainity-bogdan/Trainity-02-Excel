#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_assets_c10.py - placeholdere assets C10 (hero + 6 exec-stage).

Imaginile reale le face ARHITECT extern (Banana/Gemini) si le base64-ez la primire.
Pana atunci: placeholdere JPEG DISTINCTE (gradient + text per etapa), ca audit_sync
R-V39.assets sa gaseasca cele 6 exec-stage-*.jpg, iar 9.imgclone sa nu le confunde
byte-identic cu C01.
"""
import os
from PIL import Image, ImageDraw

os.makedirs('c10/assets', exist_ok=True)

STAGES = {
    1: ('REALITATE', 'Cifre fără măsură', (31, 42, 68)),
    2: ('INVESTIGAȚIE', 'Întrebarea înaintea cifrei', (38, 50, 80)),
    3: ('TRANSFORMARE', 'Măsura definită', (46, 40, 78)),
    4: ('VERIFICARE', 'Aceeași pe orice felie', (28, 56, 70)),
    5: ('STABILIZARE', 'Definiție ancorată', (34, 48, 62)),
    6: ('CONFIRMARE', 'Măsuri controlabile', (52, 44, 36)),
}


def grad(w, h, c0, c1):
    img = Image.new('RGB', (w, h), c0)
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        col = tuple(int(c0[i] + (c1[i] - c0[i]) * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=col)
    return img, d


def exec_img(n):
    name, emotion, base = STAGES[n]
    w, h = 1600, 1067  # 3:2
    img, d = grad(w, h, base, (8, 12, 22))
    d.rectangle([60, 60, 60 + 14, h - 60], fill=(255, 212, 0))
    d.text((110, h - 230), f'Etapa 0{n}', fill=(255, 212, 0))
    d.text((110, h - 190), name, fill=(255, 255, 255))
    d.text((110, h - 150), emotion, fill=(200, 200, 200))
    d.text((110, 80), 'C10 · MASURI · placeholder (imagine reala: ARHITECT)', fill=(150, 160, 180))
    # marcaj unic per etapa (evita byte-identic intre ele si cu C01)
    d.ellipse([w - 320 - n * 30, 120, w - 120, 320 + n * 30], outline=(255, 212, 0), width=3)
    img.save(f'c10/assets/exec-stage-{n}.jpg', quality=85)


def hero():
    w, h = 1600, 1067
    img, d = grad(w, h, (31, 42, 68), (11, 16, 32))
    d.text((100, 440), 'MASURA POTRIVITA', fill=(255, 212, 0))
    d.text((104, 510), 'C10 · MASURI · hero placeholder (imagine reala: ARHITECT)', fill=(180, 190, 210))
    img.save('c10/assets/hero-poster-excel-10-masuri.jpg', quality=85)


def main():
    for n in range(1, 7):
        exec_img(n)
    hero()
    import glob
    jpgs = sorted(glob.glob('c10/assets/*.jpg'))
    print('SCRIS c10/assets/:', len(jpgs), 'fisiere')
    for j in jpgs:
        print('  ', os.path.basename(j), os.path.getsize(j), 'bytes')


if __name__ == '__main__':
    main()
