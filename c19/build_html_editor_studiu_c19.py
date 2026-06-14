#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c19.py - HTML-Editor-Studiu-Excel-19-Guvernare.html.

Companion sincronizat 1:1 cu HTML-Studiu C19 (model matur):
  - body narativ = EXTRAS VERBATIM din c19/HTML-Studiu (baza stabilizata)
  - head+CSS editor + JS editor (contenteditable, toolbar, export) = din c18 Editor-Studiu
  - patch: title + mobile-topbar + STORAGE_KEY + export filename + NEXT, C18 -> C19
  - editorul = pagina vie editabila (fara panou companion injectat)

Zero leftover tokens C18 (Automatizare/MOTOR-ca-identitate/trainity_c18/01-Structurare).
Zero em-dash / en-dash.
"""
import re

SRC_BASE = 'c19/HTML-Studiu-Excel-19-Guvernare.html'
SRC_EDITOR = 'c18/HTML-Editor-Studiu-Excel-18-Automatizare.html'
OUT = 'c19/HTML-Editor-Studiu-Excel-19-Guvernare.html'


def split3(path):
    t = open(path, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    return t[:b], t[b:s], t[s:]


def main():
    _, base_body, _ = split3(SRC_BASE)
    ed_head, _, ed_tail = split3(SRC_EDITOR)

    # patch editor head (din c18): title + mobile-topbar + NEXT marker
    ed_head = re.sub(r'<title>.*?</title>', '<title>C19 · Guvernare · Trainity</title>', ed_head, count=1)
    ed_head = re.sub(r'NEXT \(C\d+\)', 'NEXT (C20)', ed_head)

    # patch editor tail (din c18): STORAGE_KEY + export filename + marker pagina vie
    ed_tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c19_study_v1', ed_tail)
    ed_tail = re.sub(r'HTML-Studiu-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html',
                     'HTML-Studiu-Excel-19-Guvernare-Editat.html', ed_tail)
    # marker traceabilitate: eticheta toolbar editor primeste · C19
    ed_tail = re.sub(r'(PAGINĂ VIE)(?!\s*·\s*C\d+)', r'\1 · C19', ed_tail)
    # daca C18 folosea conventia veche STRAT EDITOR / PAGINA VIE (nu e cazul), aliniaza
    ed_head = re.sub(r'STRAT EDITOR C\d+', 'STRAT EDITOR C19', ed_head)
    ed_tail = re.sub(r'PAGINA VIE · C\d+', 'PAGINA VIE · C19', ed_tail)

    assert base_body.startswith('<body>'), 'body neasteptat'
    injected = base_body
    assert '#editor-companion-head' not in injected, 'model matur: panoul companion nu se injecteaza'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    # ---- self-checks ----
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')
    print('  body identic cu HTML-Studiu C19:', base_body == injected)
    leftover = re.findall(
        r'trainity_c18|trainity_c17|Date_MASTER-C18|01-Structurare|18-Automatizare|17-Sistematizare|'
        r'STRAT EDITOR C18|PAGINA VIE · C18|C18 · MOTOR',
        out)
    print('  leftover C18/C17 editor tokens (trebuie 0):', len(leftover), leftover[:8])
    for ch, nm in [('—', 'em-dash'), ('–', 'en-dash')]:
        print('  ', nm, 'in OUT (trebuie 0):', out.count(ch))
    print('  STORAGE_KEY:', 'trainity_c19_study_v1' in out)
    print('  export filename:', 'HTML-Studiu-Excel-19-Guvernare-Editat.html' in out)
    print('  contenteditable editor prezent:', out.count('contenteditable') > 0,
          '| editorExport:', 'editorExport' in out)
    print('  title:', '<title>C19 · Guvernare · Trainity</title>' in out)
    print('  mobile-topbar C19:', 'C19 · Guvernare</div>' in out or '>C19 · Guvernare<' in out)
    # locked slots inca prezente (mostenite din body)
    for lbl, v in [
        ('HERO', 'Cum se ține corect fără ochiul meu?'),
        ('BOMBA', 'Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.'),
        ('MANTRA', 'Nu o supraveghez. O guvernez prin reguli.'),
        ('WOW', 'Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.'),
        ('AHA', 'Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.'),
    ]:
        print('  LOCK', lbl, ':', out.count(v))


if __name__ == '__main__':
    main()
