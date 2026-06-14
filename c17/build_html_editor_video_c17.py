#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_video_c17.py - HTML-Editor-Video-Excel-17-Sistematizare.html.

Editor-Video = head+tail EDITOR (din c16 Editor-Video, strat JS editare/export)
+ BODY identic cu HTML-Video C17 + STAGES/PROMPTS C17. Sincronizat 1:1 cu Video.
Reutilizeaza BODY/STAGES/PROMPTS/exec_placeholder din build_html_video_c17.
"""
import re
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'bvc17', os.path.join(_here, 'build_html_video_c17.py'))
vid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vid)

SRC = 'c16/HTML-Editor-Video-Excel-16-Livrare.html'
OUT = 'c17/HTML-Editor-Video-Excel-17-Sistematizare.html'


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = re.sub(r'<title>C\d+[^<]*</title>', '<title>C17 · SISTEMATIZARE · BROADCAST</title>', head)
    head = re.sub(r'STRAT EDITOR C\d+', 'STRAT EDITOR C17', head)
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
    tail = re.sub(r'trainity_c\d+_video_v1', 'trainity_c17_video_v1', tail)
    tail = re.sub(r'PAGINA VIE · C\d+', 'PAGINA VIE · C17', tail)
    tail = re.sub(r'HTML-Video-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html',
                  'HTML-Video-Excel-17-Sistematizare-Editat.html', tail)

    out = head + vid.BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'trainity_c16|Date_MASTER-C16|PAGINA VIE · C16|STRAT EDITOR C16', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  exec base64 jpeg ramase:', out.count('data:image/jpeg;base64,'))
    print('  STAGES steps:', out.count('num: "'))
    print('  leftover C16 (trebuie 0):', len(leftover), leftover[:6])
    for ch in ['—', '–']:
        if ch in out:
            print('  ATENTIE em/en-dash!')


if __name__ == '__main__':
    main()
