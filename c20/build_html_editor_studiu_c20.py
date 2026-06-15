#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c20.py - HTML-Editor-Studiu-Excel-20-Delegare.html.

Companion sincronizat 1:1 cu HTML-Studiu C20 (model matur):
  - body narativ = EXTRAS VERBATIM din c20/HTML-Studiu (baza stabilizata)
  - head+CSS editor + JS editor (contenteditable, toolbar, export) = din c19 Editor-Studiu
  - patch: title + mobile-topbar + STORAGE_KEY + export filename + NEXT, C19 -> C20
  - editorul = pagina vie editabila (fara panou companion injectat)

Zero leftover tokens C19 (Guvernare/CONTROL-ca-identitate/trainity_c19/19-Guvernare).
Zero em-dash / en-dash.
"""
import re

SRC_BASE = 'c20/HTML-Studiu-Excel-20-Delegare.html'
SRC_EDITOR = 'c19/HTML-Editor-Studiu-Excel-19-Guvernare.html'
OUT = 'c20/HTML-Editor-Studiu-Excel-20-Delegare.html'


def split3(path):
    t = open(path, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    return t[:b], t[b:s], t[s:]


def main():
    _, base_body, _ = split3(SRC_BASE)
    ed_head, _, ed_tail = split3(SRC_EDITOR)

    # patch editor head (din c19): title + mobile-topbar + NEXT marker
    ed_head = re.sub(r'<title>.*?</title>', '<title>C20 · Delegare · Trainity</title>', ed_head, count=1)
    ed_head = re.sub(r'NEXT \(C\d+\)', 'NEXT (FINAL)', ed_head)

    # patch editor tail (din c19): STORAGE_KEY + export filename + marker pagina vie
    ed_tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c20_study_v1', ed_tail)
    ed_tail = re.sub(r'HTML-Studiu-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html',
                     'HTML-Studiu-Excel-20-Delegare-Editat.html', ed_tail)
    # marker traceabilitate: eticheta toolbar editor primeste · C20
    ed_tail = re.sub(r'(PAGINĂ VIE)(?!\s*·\s*C\d+)', r'\1 · C20', ed_tail)
    # aliniere conventii vechi STRAT EDITOR / PAGINA VIE daca exista
    ed_head = re.sub(r'STRAT EDITOR C\d+', 'STRAT EDITOR C20', ed_head)
    ed_tail = re.sub(r'PAGINA VIE · C\d+', 'PAGINA VIE · C20', ed_tail)
    ed_tail = re.sub(r'PAGINĂ VIE · C19', 'PAGINĂ VIE · C20', ed_tail)

    assert base_body.startswith('<body>'), 'body neasteptat'
    injected = base_body
    assert '#editor-companion-head' not in injected, 'model matur: panoul companion nu se injecteaza'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    # ---- self-checks ----
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')
    print('  body identic cu HTML-Studiu C20:', base_body == injected)
    leftover = re.findall(
        r'trainity_c19|trainity_c18|Date_MASTER-C19|19-Guvernare|18-Automatizare|'
        r'STRAT EDITOR C19|PAGINA VIE · C19|PAGINĂ VIE · C19|C19 · GUVERNARE',
        out)
    print('  leftover C19/C18 editor tokens (trebuie 0):', len(leftover), leftover[:8])
    for ch, nm in [('—', 'em-dash'), ('–', 'en-dash')]:
        print('  ', nm, 'in OUT (trebuie 0):', out.count(ch))
    print('  "ownership" in OUT (trebuie 0):', out.lower().count('ownership'))
    print('  STORAGE_KEY:', 'trainity_c20_study_v1' in out)
    print('  export filename:', 'HTML-Studiu-Excel-20-Delegare-Editat.html' in out)
    print('  contenteditable editor prezent:', out.count('contenteditable') > 0,
          '| editorExport:', 'editorExport' in out)
    print('  title:', '<title>C20 · Delegare · Trainity</title>' in out)
    print('  mobile-topbar C20:', 'C20 · Delegare</div>' in out or '>C20 · Delegare<' in out)
    # locked slots inca prezente (mostenite din body)
    for lbl, v in [
        ('HERO', 'Cum deleg sistemul, ca să meargă fără mine?'),
        ('BOMBA', 'Sistemul tău merge fără tine. Dar la orice problemă, tot pe tine te sună.'),
        ('MANTRA', 'Nu împart sarcini. Deleg sistemul.'),
        ('WOW', 'Apeși «scoate autorul», și sistemul nu se rupe: workbook-ul confirmă singur că alt rol îl poate continua.'),
        ('AHA', 'Un sistem nu e autonom pentru că merge singur. E autonom când îl poate deține altcineva.'),
    ]:
        print('  LOCK', lbl, ':', out.count(v))


if __name__ == '__main__':
    main()
