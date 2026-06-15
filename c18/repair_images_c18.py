#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repair_images_c18.py - REPARATIE AUDIT T5 (E3): declone imaginile C01 din C18.

C18 a fost COPY+MODIFY din C01 si a pastrat imaginile C01 (hero + 6 exec-stage)
ca base64 in cele 4 HTML + ca fisiere exec-stage-*.jpg clone (imgclone XX).
Per doctrina L202 (clona base64 -> placeholder pana la imaginile reale ARHITECT),
inlocuiesc:
  - hero base64 din Studiu + Editor-Studiu  -> SVG placeholder DRAFT
  - 6 exec base64 din Video + Editor-Video  -> SVG placeholdere DRAFT
  - 6 fisiere assets/exec-stage-N.jpg clone -> JPG DRAFT unice (PIL)
Pastrez hero-automatizare.jpg + infografic (specifice C18). Acelasi tipar ca
build-scriptele C19/C20. Idempotent (se poate re-rula). Zero em-dash.
"""
import re, os, glob, base64, io
from PIL import Image, ImageDraw, ImageFont

EXEC_TITLES = {1: 'REALITATE', 2: 'INVESTIGAȚIE', 3: 'TRANSFORMARE',
               4: 'VERIFICARE', 5: 'STABILIZARE', 6: 'CONFIRMARE'}
EXEC_DESCR = {
    1: 'Sistemul exista (C17), dar fiecare ciclu cere multe atingeri manuale.',
    2: 'Inventariezi pasii stabili care se repeta identic la fiecare ciclu.',
    3: 'Legi pasii intr-un lant pornit dintr-o singura atingere.',
    4: 'Probezi: o atingere, lantul merge pana la capat fara tine.',
    5: 'Ramane doar interventia minima de judecata (granita C19).',
    6: 'Mainile jos: lantul ruleaza, tu pleci din executia repetitiva.',
}

# ---------- SVG placeholders (acelasi format ca build-scriptele) ----------
def hero_svg():
    return ("data:image/svg+xml;utf8,"
            "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
            "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
            "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
            "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
            "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
            "font-weight='bold'>MOTOR</text>"
            "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
            "opacity='0.7'>C18 · placeholder hero</text></svg>")

def exec_svg(n, titlu):
    return ("data:image/svg+xml;utf8,"
            "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
            "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
            "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
            "</linearGradient></defs><rect width='1600' height='900' fill='url(%23g)'/>"
            "<text x='80' y='470' fill='%23FFD400' font-family='Georgia' font-size='90' "
            "font-weight='bold'>" + titlu + "</text>"
            "<text x='84' y='532' fill='%23ffffff' font-family='Arial' font-size='30' "
            "opacity='0.6'>C18 · exec-stage-" + str(n) + " · placeholder DRAFT</text></svg>")


def _real_hero_datauri():
    """hero-automatizare.jpg (foto REALA C18) -> 1200w q82 -> base64. C18 are hero propriu;
    inlocuim clona C01 cu el (nu cu placeholder)."""
    im = Image.open('c18/assets/hero-automatizare.jpg').convert('RGB')
    w = 1200; h = int(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=82)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def declone_studiu(path, hero_uri):
    """Inlocuieste hero <img src='...'> (clona C01 base64 SAU placeholder SVG) cu hero REAL C18."""
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'(hero-visual-img" src=")data:image/jpeg;base64,[A-Za-z0-9+/=]+(")',
               lambda m: m.group(1) + hero_uri + m.group(2), t, count=1)
    t = re.sub(r'(hero-visual-img" src=")data:image/svg\+xml;utf8,[^"]*(")',
               lambda m: m.group(1) + hero_uri + m.group(2), t, count=1)
    open(path, 'w', encoding='utf-8').write(t)
    return t.count('data:image/jpeg;base64,')


def declone_video(path):
    """Inlocuieste cele 6 exec base64 din CSS cu SVG placeholdere DRAFT."""
    t = open(path, encoding='utf-8').read()
    n_before = t.count('data:image/jpeg;base64,')
    for n in range(1, 7):
        ph = exec_svg(n, EXEC_TITLES[n])
        t = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("data:image/jpeg;base64,[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph, t, count=1)
    n_after = t.count('data:image/jpeg;base64,')
    open(path, 'w', encoding='utf-8').write(t)
    return n_before, n_after


# ---------- DRAFT exec-stage JPG (PIL), pastrez hero-automatizare + infografic ----------
W, H = 1500, 1000
NT, NB = (0x1F, 0x2A, 0x44), (0x0B, 0x10, 0x20)
GOLD, GB, MUTED = (0xB8, 0x86, 0x0B), (0xFF, 0xD4, 0x00), (0x9A, 0xA6, 0xC0)
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

def _f(p, s): return ImageFont.truetype(p, s)
def _tw(d, s, f): bb = d.textbbox((0, 0), s, font=f); return bb[2]-bb[0]

def _wrap(d, s, f, mw):
    out, cur = [], ''
    for w in s.split():
        t = (cur+' '+w).strip()
        if _tw(d, t, f) <= mw: cur = t
        else:
            if cur: out.append(cur)
            cur = w
    if cur: out.append(cur)
    return out

def _grad():
    img = Image.new('RGB', (W, H), NT); px = img.load()
    for y in range(H):
        t = y/(H-1)
        px_row = (int(NT[0]+(NB[0]-NT[0])*t), int(NT[1]+(NB[1]-NT[1])*t), int(NT[2]+(NB[2]-NT[2])*t))
        for x in range(W): px[x, y] = px_row
    return img

def make_exec(path, n, label, descr):
    img = _grad(); d = ImageDraw.Draw(img)
    d.rectangle([28, 28, W-28, H-28], outline=GOLD, width=3)
    kick = 'C18 · AUTOMATIZARE · MOTOR'
    w = _tw(d, kick, _f(FB, 28)); d.text(((W-w)/2, 120), kick, font=_f(FB, 28), fill=MUTED)
    nt = '%02d' % n; w = _tw(d, nt, _f(FB, 120)); d.text(((W-w)/2, 210), nt, font=_f(FB, 120), fill=GOLD)
    w = _tw(d, label, _f(FB, 60)); d.text(((W-w)/2, 380), label, font=_f(FB, 60), fill=GB)
    y = 510
    for ln in _wrap(d, descr, _f(FR, 34), W-320):
        w = _tw(d, ln, _f(FR, 34)); d.text(((W-w)/2, y), ln, font=_f(FR, 34), fill=MUTED)
        bb = d.textbbox((0, 0), ln, font=_f(FR, 34)); y += (bb[3]-bb[1])+12
    dr = 'C18 · exec-stage-%d · placeholder DRAFT' % n
    w = _tw(d, dr, _f(FB, 28)); d.text(((W-w)/2, H-110), dr, font=_f(FB, 28), fill=MUTED)
    img.save(path, 'JPEG', quality=90)


def main():
    base = 'c18'
    studii = [glob.glob(f'{base}/HTML-Studiu-Excel-18-*.html')[0],
              glob.glob(f'{base}/HTML-Editor-Studiu-Excel-18-*.html')[0]]
    videos = [glob.glob(f'{base}/HTML-Video-Excel-18-*.html')[0],
              glob.glob(f'{base}/HTML-Editor-Video-Excel-18-*.html')[0]]
    print('=== DECLONE HTML (clona C01 -> hero REAL C18 in Studiu, SVG placeholder in Video) ===')
    hero_uri = _real_hero_datauri()
    for p in studii:
        a = declone_studiu(p, hero_uri); print(f'  {os.path.basename(p)}: hero REAL embed | base64 jpeg={a}')
    for p in videos:
        b, a = declone_video(p); print(f'  {os.path.basename(p)}: exec base64 {b} -> {a}')
    print('=== DRAFT exec-stage JPG (pastrez hero-automatizare + infografic) ===')
    for n in range(1, 7):
        make_exec(f'{base}/assets/exec-stage-{n}.jpg', n, EXEC_TITLES[n], EXEC_DESCR[n])
        print(f'  exec-stage-{n}.jpg DRAFT')
    print('=== assets ramase:', sorted(os.listdir(f'{base}/assets')))


if __name__ == '__main__':
    main()
