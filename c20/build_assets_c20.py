#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_assets_c20.py - placeholdere DRAFT pentru C20 DELEGARE (PIL).

Genereaza 7 JPG, raport 3:2 cinematic (1500x1000), fundal navy gradient
(#1F2A44 -> #0B1020), text auriu (#B8860B / #FFD400). Axa PREDARE / PROPRIETATE.
- hero-poster-excel-20-delegare.jpg
- exec-stage-1.jpg .. exec-stage-6.jpg (REALITATE / DEPENDENTA / HARTA / TESTUL / REPARARE / AUTONOM)
Marcate explicit DRAFT placeholder. NU clone din c01/c19 (text + continut unic).
Imaginile reale DELEGARE le produce ARHITECT extern si le inlocuieste ulterior.
Text ASCII-safe (fara diacritice / ghilimele), ca in c19. Zero em-dash / en-dash.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUTDIR = 'c20/assets'
W, H = 1500, 1000  # 3:2

NAVY_TOP = (0x1F, 0x2A, 0x44)
NAVY_BOT = (0x0B, 0x10, 0x20)
GOLD = (0xB8, 0x86, 0x0B)
GOLD_BRIGHT = (0xFF, 0xD4, 0x00)
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
    margin = 28
    d.rectangle([margin, margin, W - margin, H - margin], outline=GOLD, width=3)
    return img, d


def make_hero(path):
    img, d = base_canvas()
    f_kicker = font(FONT_BOLD, 34)
    f_title = font(FONT_BOLD, 72)
    f_sub = font(FONT_REG, 40)
    f_draft = font(FONT_BOLD, 30)

    kick = 'TRAINITY · PACK 02 EXCEL · C20'
    w = text_w(d, kick, f_kicker)
    d.text(((W - w) / 2, 150), kick, font=f_kicker, fill=MUTED)

    title_lines = wrap(d, 'DELEGAREA SISTEMULUI DE LUCRU', f_title, W - 240)
    y = 300
    y = draw_centered(d, title_lines, f_title, y, GOLD_BRIGHT, gap=18)

    sub_lines = wrap(d, 'Cum deleg sistemul, ca sa mearga fara mine?', f_sub, W - 320)
    y = draw_centered(d, sub_lines, f_sub, y + 30, GOLD)

    draft = 'C20 · placeholder DRAFT'
    w = text_w(d, draft, f_draft)
    d.text(((W - w) / 2, H - 120), draft, font=f_draft, fill=MUTED)

    img.save(path, 'JPEG', quality=90)
    return path


def make_stage(path, n, label, descr):
    img, d = base_canvas()
    f_num = font(FONT_BOLD, 120)
    f_label = font(FONT_BOLD, 66)
    f_descr = font(FONT_REG, 34)
    f_draft = font(FONT_BOLD, 28)
    f_kicker = font(FONT_BOLD, 28)

    kick = 'C20 · DELEGARE · PROPRIETATE'
    w = text_w(d, kick, f_kicker)
    d.text(((W - w) / 2, 120), kick, font=f_kicker, fill=MUTED)

    numt = '%02d' % n
    w = text_w(d, numt, f_num)
    d.text(((W - w) / 2, 210), numt, font=f_num, fill=GOLD)

    w = text_w(d, label, f_label)
    d.text(((W - w) / 2, 380), label, font=f_label, fill=GOLD_BRIGHT)

    descr_lines = wrap(d, descr, f_descr, W - 320)
    draw_centered(d, descr_lines, f_descr, 510, MUTED, gap=12)

    draft = 'C20 · exec-stage-%d · placeholder DRAFT' % n
    w = text_w(d, draft, f_draft)
    d.text(((W - w) / 2, H - 110), draft, font=f_draft, fill=MUTED)

    img.save(path, 'JPEG', quality=90)
    return path


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    made = []

    made.append(make_hero(os.path.join(OUTDIR, 'hero-poster-excel-20-delegare.jpg')))

    stages = [
        (1, 'REALITATE', 'Sistemul merge, dar e inca al tau. Ruleaza si se pazeste singur, dar la orice problema tot pe tine te suna.'),
        (2, 'DEPENDENTA', 'Ce te face indispensabil. Inputurile care atarna numai de tine, marcate author-only.'),
        (3, 'HARTA', 'Harta de predare ca input al testului. Rol, acces pe zone, limite blocate, escaladare catre un rol.'),
        (4, 'TESTUL', 'Scoti autorul. Apesi AUTOR_ACTIV=NU; V1-V4 si STATUS se reaseaza singure. Nu bifezi, dovedesti.'),
        (5, 'REPARARE', 'Dependenta ascunsa, apoi repararea. V1 aprinde FAIL: tu erai cheia. Muti parametrul pe rol.'),
        (6, 'AUTONOM', 'STATUS autonom si predarea reala. Autorul scos, zero dependenta: AUTONOM singur. Pachetul se inchide.'),
    ]
    for n, label, descr in stages:
        made.append(make_stage(os.path.join(OUTDIR, 'exec-stage-%d.jpg' % n), n, label, descr))

    for p in made:
        sz = os.path.getsize(p)
        print('SCRIS:', p, '(%d bytes)' % sz)


if __name__ == '__main__':
    main()
