#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_video_c13.py - HTML-Editor-Video-Excel-13-Vizualizare.html.

Editor-Video = head+tail EDITOR (din c12 Editor-Video, strat JS editare/export)
+ BODY identic cu HTML-Video C13 + STAGES/PROMPTS C13. Sincronizat 1:1 cu Video.
Reutilizeaza BODY/STAGES/PROMPTS/exec_placeholder din build_html_video_c13.
"""
import re
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'bvc13', os.path.join(_here, 'build_html_video_c13.py'))
vid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vid)

SRC = 'c12/HTML-Editor-Video-Excel-12-Interpretare.html'
OUT = 'c13/HTML-Editor-Video-Excel-13-Vizualizare.html'


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # title robust C12 -> C13 (oricare forma C12 · X · BROADCAST)
    head = re.sub(r'<title>C12[^<]*</title>',
                  '<title>C13 · VIZUAL · BROADCAST</title>', head)
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
    tail = tail.replace('trainity_c12_video_v1', 'trainity_c13_video_v1')
    tail = tail.replace('PAGINA VIE · C12', 'PAGINA VIE · C13')
    tail = tail.replace('HTML-Video-Excel-12-Interpretare-Editat.html',
                        'HTML-Video-Excel-13-Vizualizare-Editat.html')
    head = head.replace('STRAT EDITOR C12', 'STRAT EDITOR C13')

    out = head + vid.BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    # C12 vizibil (non-base64): tokeni de identitate ramasi
    clean = re.sub(r'url\("data:[^"]*"\)', 'url(IMG)', out)
    vis = [m.group(0) for m in re.finditer(r'.{0,18}C12.{0,28}', clean)
           if 'base64' not in m.group(0) and len(re.sub(r'[A-Za-z0-9+/=]', '', m.group(0))) > 3]
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  exec jpeg base64 ramase:', out.count('data:image/jpeg;base64,'))
    print('  C12 vizibil (non-base64):', len(vis))
    for v in vis[:5]:
        print('   ', repr(v))


if __name__ == '__main__':
    main()
