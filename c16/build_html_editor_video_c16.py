#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_video_c16.py - HTML-Editor-Video-Excel-16-Livrare.html.

Editor-Video = head+tail EDITOR (din c14 Editor-Video, strat JS editare/export)
+ BODY identic cu HTML-Video C16 + STAGES/PROMPTS C16. Sincronizat 1:1 cu Video.
Reutilizeaza BODY/STAGES/PROMPTS/exec_placeholder din build_html_video_c16.
"""
import re
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'bvc16', os.path.join(_here, 'build_html_video_c16.py'))
vid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vid)

SRC = 'c14/HTML-Editor-Video-Excel-14-Compunere.html'
OUT = 'c16/HTML-Editor-Video-Excel-16-Livrare.html'


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # title robust C14 -> C16
    head = re.sub(r'<title>C\d+[^<]*</title>', '<title>C16 · LIVRARE · BROADCAST</title>', head)
    head = re.sub(r'STRAT EDITOR C\d+', 'STRAT EDITOR C16', head)
    for n in range(1, 7):
        ph = vid.exec_placeholder(n, vid.EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)

    i_st = tail.index('const STAGES = [')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + vid.STAGES + vid.PROMPTS + tail[i_fl:]
    tail = re.sub(r'trainity_c\d+_video_v1', 'trainity_c16_video_v1', tail)
    tail = re.sub(r'PAGINA VIE · C\d+', 'PAGINA VIE · C16', tail)
    tail = re.sub(r'HTML-Video-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html',
                  'HTML-Video-Excel-16-Livrare-Editat.html', tail)

    out = head + vid.BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    clean = re.sub(r'url\("data:[^"]*"\)', 'url(IMG)', out)
    vis = [m.group(0) for m in re.finditer(r'.{0,12}C14.{0,20}', clean)
           if 'base64' not in m.group(0) and len(re.sub(r'[A-Za-z0-9+/=]', '', m.group(0))) > 3]
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  exec base64 jpeg ramase:', out.count('data:image/jpeg;base64,'))
    print('  STAGES steps:', out.count('num: "'))
    print('  C14 vizibil (non-base64):', len(vis), vis[:4])


if __name__ == '__main__':
    main()
