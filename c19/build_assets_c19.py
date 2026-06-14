#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_assets_c19.py - placeholdere DRAFT pentru C19 GUVERNARE (PIL).

Genereaza 7 JPG, raport 3:2 cinematic (1500x1000), fundal navy gradient
(#1F2A44 -> #0B1020), text auriu (#B8860B / #FFD400). Axa CONTROL.
- hero-poster-excel-19-guvernare.jpg
- exec-stage-1.jpg .. exec-stage-6.jpg (REALITATE / DEVIATII / REGULA / PRAG-SEMNAL / OPRIRE / TEST)
Marcate explicit DRAFT placeholder. NU clone din c01/c18 (text + continut unic).
Zero em-dash / en-dash in text.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUTDIR = 'c19/assets'
W, H = 1500, 1000  # 3:2

NAVY_TOP = (0x1F, 0x2A, 0x44)   # #1F2A44
NAVY_BOT = (0x0B, 0x10, 0x20)   # #0B1020
GOLD = (0xB8, 0x86, 0x0B)       # #B8860B
GOLD_BRIGHT = (0xFF, 0xD4, 0x00)  # #FFD400
MUTED = (0x9A, 0xA6, 0xC0)

FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def font(path, size):
    return ImageFont.truetype(path, size)


def vgradient(w, h, top, bot):
    base = Image.new('RGB', (w, h), top)
    px = base.load()
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return base


def text_w(draw, s, fnt):
    bb = draw.textbbox((0, 0), s, font=fnt)
    return bb[2] - bb[0]


def wrap(draw, s, fnt, maxw):
    words = s.split()
    lines, cur = [], ''
    for wd in words:
        trial = (cur + ' ' + wd).strip()
        if text_w(draw, trial, fnt) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, lines, fnt, y, color, gap=14):
    for ln in lines:
        w = text_w(draw, ln, fnt)
        draw.text(((W - w) / 2, y), ln, font=fnt, fill=color)
        bb = draw.textbbox((0, 0), ln, font=fnt)
        y += (bb[3] - bb[1]) + gap
    return y


def base_canvas():
    img = vgradient(W, H, NAVY_TOP, NAVY_BOT)
    d = ImageDraw.Draw(img)
    # thin gold frame
    margin = 28
    d.rectangle([margin, margin, W - margin, H - margin], outline=GOLD, width=3)
    # subtle inner corner ticks (control vibe)
    return img, d


def make_hero(path):
    img, d = base_canvas()
    f_kicker = font(FONT_BOLD, 34)
    f_title = font(FONT_BOLD, 78)
    f_sub = font(FONT_REG, 40)
    f_draft = font(FONT_BOLD, 30)

    # kicker
    kick = 'TRAINITY · PACK 02 EXCEL · C19'
    w = text_w(d, kick, f_kicker)
    d.text(((W - w) / 2, 150), kick, font=f_kicker, fill=MUTED)

    # title (wrapped)
    title_lines = wrap(d, 'GUVERNAREA SISTEMULUI PRIN REGULI', f_title, W - 240)
    y = 300
    y = draw_centered(d, title_lines, f_title, y, GOLD_BRIGHT, gap=18)

    # subtitle / hero question
    sub_lines = wrap(d, 'Cum se tine corect fara ochiul meu?', f_sub, W - 320)
    y = draw_centered(d, sub_lines, f_sub, y + 30, GOLD)

    # draft stamp bottom
    draft = 'C19 · placeholder DRAFT'
    w = text_w(d, draft, f_draft)
    d.text(((W - w) / 2, H - 120), draft, font=f_draft, fill=MUTED)

    img.save(path, 'JPEG', quality=90)
    return path


def make_stage(path, n, label, descr):
    img, d = base_canvas()
    f_num = font(FONT_BOLD, 120)
    f_label = font(FONT_BOLD, 70)
    f_descr = font(FONT_REG, 34)
    f_draft = font(FONT_BOLD, 28)
    f_kicker = font(FONT_BOLD, 28)

    # kicker
    kick = 'C19 · GUVERNARE · CONTROL'
    w = text_w(d, kick, f_kicker)
    d.text(((W - w) / 2, 120), kick, font=f_kicker, fill=MUTED)

    # big stage number
    numt = '%02d' % n
    w = text_w(d, numt, f_num)
    d.text(((W - w) / 2, 210), numt, font=f_num, fill=GOLD)

    # label
    w = text_w(d, label, f_label)
    d.text(((W - w) / 2, 380), label, font=f_label, fill=GOLD_BRIGHT)

    # description
    descr_lines = wrap(d, descr, f_descr, W - 320)
    draw_centered(d, descr_lines, f_descr, 510, MUTED, gap=12)

    # draft stamp
    draft = 'C19 · exec-stage-%d · placeholder DRAFT' % n
    w = text_w(d, draft, f_draft)
    d.text(((W - w) / 2, H - 110), draft, font=f_draft, fill=MUTED)

    img.save(path, 'JPEG', quality=90)
    return path


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    made = []

    made.append(make_hero(os.path.join(OUTDIR, 'hero-poster-excel-19-guvernare.jpg')))

    stages = [
        (1, 'REALITATE', 'Sistemul care merge doar cat te uiti. Motorul ruleaza, dar pe o intrare gresita produce gunoi in tacere.'),
        (2, 'DEVIATII', 'Ce poate sa devieze previzibil. Plicul asteptat, scris ca praguri vii LIMIT_.'),
        (3, 'REGULA', 'Regula care prinde intrarea gresita. Validare la sursa, STATUS OK / ATENTIE / OPRIT din reguli.'),
        (4, 'PRAG-SEMNAL', 'Pragul si semnalul. STATUS se schimba singur. Semnalul actioneaza, nu se citeste.'),
        (5, 'OPRIRE', 'Exceptia si oprirea controlata. Fail-safe pe STATUS=OPRIT: rezultatul corupt nu mai curge.'),
        (6, 'TEST', 'Testul ochilor inchisi. Plantezi deviatii, pleci: regulile prind, semnaleaza, opresc singure.'),
    ]
    for n, label, descr in stages:
        made.append(make_stage(os.path.join(OUTDIR, 'exec-stage-%d.jpg' % n), n, label, descr))

    for p in made:
        sz = os.path.getsize(p)
        print('SCRIS:', p, '(%d bytes)' % sz)


if __name__ == '__main__':
    main()
