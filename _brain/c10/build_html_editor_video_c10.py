#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_video_c10.py - HTML-Editor-Video-Excel-10-Masuri.html.

Editor-Video = head+tail EDITOR (din c09 Editor-Video, cu strat JS de editare/export)
+ BODY identic cu HTML-Video C10 + STAGES/PROMPTS C10. Sincronizat 1:1 cu Video (BRAIN-019).
Reutilizeaza BODY/STAGES/PROMPTS/exec_placeholder din build_html_video_c10.
"""
import re
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'bvc10', os.path.join(_here, 'build_html_video_c10.py'))
vid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vid)

SRC = 'c09/HTML-Editor-Video-Excel-09-Relatii.html'
OUT = 'c10/HTML-Editor-Video-Excel-10-Masuri.html'


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # head: title + exec images placeholder (6 jpeg -> svg)
    head = head.replace('<title>C09 · RELAȚII · BROADCAST</title>',
                        '<title>C10 · MĂSURI · BROADCAST</title>')
    for n in range(1, 7):
        ph = vid.exec_placeholder(n, vid.EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("data:image/jpeg;base64,[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)

    # tail: STAGES + PROMPTS C10 + STORAGE_KEY (pastrez stratul editor JS)
    i_st = tail.index('const STAGES = [')
    i_pr = tail.index('const PROMPTS = {')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + vid.STAGES + vid.PROMPTS + tail[i_fl:]
    tail = tail.replace('trainity_c09_video_v1', 'trainity_c10_video_v1')
    # eventuale label-uri editor cu cod prev (ca la Editor-Studiu: PAGINA VIE · C09)
    tail = tail.replace('PAGINA VIE · C09', 'PAGINA VIE · C10')
    head = head.replace('STRAT EDITOR C09', 'STRAT EDITOR C10')

    out = head + vid.BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    # C09 vizibil (exclud base64): doar handoff legitim din STAGES instr
    clean = re.sub(r'url\("data:[^"]*"\)', 'url(IMG)', out)
    vis = [m.group(0) for m in re.finditer(r'.{0,20}C09.{0,30}', clean)
           if 'base64' not in m.group(0) and len(re.sub(r'[A-Za-z0-9+/=]', '', m.group(0))) > 3]
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  exec jpeg base64 ramase:', out.count('data:image/jpeg;base64,'))
    print('  C09 vizibil (non-base64):')
    for v in vis:
        print('   ', repr(v))


if __name__ == '__main__':
    main()
