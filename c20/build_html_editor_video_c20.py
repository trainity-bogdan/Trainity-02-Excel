#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_video_c20.py - HTML-Editor-Video-Excel-20-Delegare.html.

Editor-Video = head+tail EDITOR (din c19 Editor-Video, strat JS editare/export)
+ BODY identic cu HTML-Video C20 + STAGES/PROMPTS C20. Sincronizat 1:1 cu Video.
Reutilizeaza BODY/STAGES/PROMPTS/exec_placeholder/hero_placeholder din
build_html_video_c20. exec-stage + hero = SVG placeholder DRAFT (NU base64 clona).
Tokens C19 -> C20: title, localStorage, export filename. Zero leftover c18/c19.
"""
import re
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'bvc20', os.path.join(_here, 'build_html_video_c20.py'))
vid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vid)

SRC = 'c19/HTML-Editor-Video-Excel-19-Guvernare.html'
OUT = 'c20/HTML-Editor-Video-Excel-20-Delegare.html'

TITLE = 'C20 · DELEGARE · BROADCAST · EDITOR'
STORAGE = 'trainity_c20_video_v1'
EXPORT = 'HTML-Video-Excel-20-Delegare-Editat.html'


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # --- HEAD: title editor + exec-stage placeholders DRAFT ---
    head = re.sub(r'<title>C\d+[^<]*</title>', '<title>%s</title>' % TITLE, head, count=1)
    for n in range(1, 7):
        ph = vid.exec_placeholder(n, vid.EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)
    hero = vid.hero_placeholder()
    head = re.sub(r'(\.hero[\w-]*\s*\{[^}]*background-image:\s*)url\("data:image/jpeg;base64,[^"]*"\)',
                  lambda m: m.group(1) + 'url("%s")' % hero, head)

    # --- TAIL: STAGES + PROMPTS + tokens C19 -> C20 ---
    i_st = tail.index('const STAGES = [')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + vid.STAGES + vid.PROMPTS + tail[i_fl:]
    tail = re.sub(r'trainity_c\d+_video_v1', STORAGE, tail)
    tail = re.sub(r'HTML-Video-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html', EXPORT, tail)

    # BODY = identic cu Video C20 (curat, fara leftover c01/c19)
    out = head + vid.BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    # --- SELF-VERIFY ---
    import unicodedata
    outn = unicodedata.normalize('NFC', out)
    def has(s):
        return unicodedata.normalize('NFC', s) in outn
    jpeg = out.count('data:image/jpeg;base64,')
    leftover = re.findall(
        r'trainity_c19|trainity_c18|19-Guvernare|18-Automatizare|01-Structurare|'
        r'STRAT EDITOR C19|STRAT EDITOR C18|Construcția 01|Construcția 19|GUVERNAREA|'
        r'_GUVERNARE|_AUTOMATIZARE|CONTROL · BROADCAST', out)
    dashes = [c for c in ('—', '–') if c in out]
    own = out.lower().count('ownership')
    locked = {
        'HERO': 'Cum deleg sistemul, ca să meargă fără mine?',
        'BOMBA': 'Sistemul tău merge fără tine. Dar la orice problemă, tot pe tine te sună.',
        'MANTRA': 'Nu împart sarcini. Deleg sistemul.',
        'WOW': 'Apeși «scoate autorul», și sistemul nu se rupe',
        'MOTTO': 'Pleci, și munca nu mai e a ta.',
        'GRESEALA': 'Crezi că ai delegat când ai explicat.',
        'AHA': 'Un sistem nu e autonom pentru că merge singur. E autonom când îl poate deține altcineva.',
        'hov-object': 'DELEGAREA SISTEMULUI DE LUCRU',
    }
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out.encode('utf-8')), 'bytes')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  STORAGE_KEY:', re.search(r'const STORAGE_KEY = "[^"]*"', out).group(0))
    print('  export filename:', re.search(r'a\.download = "([^"]*)"', out).group(1))
    print('  exec base64 jpeg ramase (trebuie 0):', jpeg)
    print('  exec-stage SVG placeholder DRAFT (trebuie 6):', out.count('placeholder DRAFT') - 1)
    print('  STAGES steps (num:):', out.count('num: "'), '| prompturi:', out.count('label: "Prompt'))
    print('  leftover c18/c19/clona (trebuie 0):', len(leftover), leftover[:6])
    print('  "ownership" (trebuie 0):', own)
    print('  em/en-dash (trebuie []):', dashes)
    miss = [k for k, v in locked.items() if not has(v)]
    print('  LOCKED 8 sloturi:', 'TOATE OK' if not miss else ('LIPSA -> ' + ', '.join(miss)))
    print('  pack inchis (C01-C20):', 'OK' if 'C01-C20' in out else 'LIPSA')
    print('  EDITOR layer (editorExport):', 'OK' if 'editorExport' in out else 'LIPSA')
    print('  closing </html>:', 'OK' if out.rstrip().endswith('</html>') else 'LIPSA')


if __name__ == '__main__':
    main()
