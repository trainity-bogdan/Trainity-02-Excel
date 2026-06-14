#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c17.py - HTML-Editor-Studiu-Excel-17-Sistematizare.html.

Companion sincronizat 1:1 cu HTML-Studiu C17 (model matur, FAZA 2):
  - body narativ = EXTRAS VERBATIM din c17/HTML-Studiu (baza stabilizata)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c16 Editor-Studiu
  - patch title + STORAGE_KEY + NEXT + STRAT EDITOR + export filename, C16 -> C17
  - fara panou companion injectat (editorul = pagina vie editabila)
"""
import re
SRC_BASE = 'c17/HTML-Studiu-Excel-17-Sistematizare.html'
SRC_EDITOR = 'c16/HTML-Editor-Studiu-Excel-16-Livrare.html'
OUT = 'c17/HTML-Editor-Studiu-Excel-17-Sistematizare.html'


def split3(path):
    t = open(path, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    return t[:b], t[b:s], t[s:]


def main():
    _, base_body, _ = split3(SRC_BASE)
    ed_head, _, ed_tail = split3(SRC_EDITOR)

    ed_head = re.sub(r'<title>.*?</title>', '<title>C17 · Sistematizare · Trainity</title>', ed_head, count=1)
    ed_head = re.sub(r'NEXT \(C\d+\)', 'NEXT (C17)', ed_head)
    ed_head = re.sub(r'STRAT EDITOR C\d+', 'STRAT EDITOR C17', ed_head)
    ed_tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c17_study_v1', ed_tail)
    ed_tail = re.sub(r'PAGINA VIE · C\d+', 'PAGINA VIE · C17', ed_tail)
    ed_tail = re.sub(r'HTML-Studiu-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html',
                     'HTML-Studiu-Excel-17-Sistematizare-Editat.html', ed_tail)

    assert base_body.startswith('<body>'), 'body neasteptat'
    injected = base_body
    assert '#editor-companion-head' not in injected, 'model matur: panoul companion nu se injecteaza'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'trainity_c16|Date_MASTER-C16|Livrare|LIVRARE|STRAT EDITOR C16|PAGINA VIE · C16', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  body identic cu HTML-Studiu C17:', base_body == injected)
    print('  leftover C16 tokens (trebuie 0):', len(leftover), leftover[:8])
    for ch in ['—', '–']:
        if ch in out:
            print('  ATENTIE em/en-dash!')


if __name__ == '__main__':
    main()
