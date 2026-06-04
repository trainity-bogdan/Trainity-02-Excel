#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c10.py - HTML-Editor-Studiu-Excel-10-Masuri.html.

Companion sincronizat 1:1 cu HTML-Studiu C10 (BRAIN-019):
  - body narativ = EXTRAS VERBATIM din c10/HTML-Studiu (baza stabilizata, gate PASS)
  - + panou #editor-companion-head (LOCKED / editabil / garda C10 / checklist sync)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c09 Editor-Studiu
  - patch title + STORAGE_KEY
"""
SRC_BASE = 'c10/HTML-Studiu-Excel-10-Masuri.html'
SRC_EDITOR = 'c09/HTML-Editor-Studiu-Excel-09-Relatii.html'
OUT = 'c10/HTML-Editor-Studiu-Excel-10-Masuri.html'

PANEL = r'''<div id="editor-companion-head">
  <div class="ech-bar">
    <div class="ech-title">EDITOR-STUDIU · <b>C10 MĂSURI</b> · companion sincronizat cu HTML-Studiu (BRAIN-019)</div>
    <button type="button" class="ech-toggle" onclick="editorTogglePanel()" aria-label="Restrange sau extinde panoul"><span class="ech-tg-txt"></span></button>
  </div>
  <div class="ech-body">
  <div class="ech-sub">Editezi textul direct (click pe text). Zonele cu chenar rosu si lacat sunt LOCKED (nu se ating). Frazele canonice din pasi sunt blocate punctual, restul microcopy-ului ramane editabil. La final apesi EXPORT (bara de jos) ca sa descarci versiunea editata.</div>
  <div class="ech-cols">
    <div class="ech-box ech-lock">
      <div class="ech-h">Zone LOCKED (nu edita)</div>
      <ul>
        <li>Hero: „Cât? Și cum definesc o măsură care răspunde corect de fiecare dată?"</li>
        <li>AHA: „Nu cifra contează. Contează ce întrebare răspunde cifra."</li>
        <li>Mantra: „Măsura corectă răspunde întrebării corecte."</li>
        <li>BOMBĂ / GREȘEALA / CINE DEVII / WOW / MOTTO</li>
        <li>Single source of truth: „Aceasta devine sursa unică de adevăr."</li>
        <li>Reper: „Reperul transformă cifra în sens."</li>
      </ul>
    </div>
    <div class="ech-box ech-edit">
      <div class="ech-h">Zone editabile</div>
      <ul>
        <li>formulări de introducere</li>
        <li>microcopy de pași, explicații pentru learner</li>
        <li>exemple pedagogice (fără cifre finale)</li>
        <li>text de prompt AI (păstrând scopul de definire)</li>
        <li>payoff (fără să rupă sloturile LOCKED)</li>
      </ul>
    </div>
    <div class="ech-box ech-guard">
      <div class="ech-h">C10 rămâne la MĂSURI (anti-contaminare)</div>
      <ul>
        <li>doar definește măsuri (single source of truth, bază, reper, semnal)</li>
        <li>nu compară, nu clasează, nu calculează contribuții (treapta următoare)</li>
        <li>fără interpretarea motivelor (o treaptă mai târziu)</li>
        <li>fără tablou vizual sau acțiuni automate (treptele de raportare/automatizare)</li>
        <li>zero cifre business statice în text</li>
        <li>hero MĂSURI dedicat (fără clonă vizuală din treapta anterioară)</li>
      </ul>
    </div>
  </div>
  <div class="ech-sync">
    <div class="ech-h">Checklist sincronizare cu baza (HTML-Studiu C10 stabilizat)</div>
    <div class="ech-sync-grid">
      <span>title LOCKED</span><span>AHA verbatim</span><span>18 pași</span>
      <span>8 verificări</span><span>6 fenomene</span><span>2 prompturi AI</span>
      <span>măsură: definiție + bază + reper</span><span>lock-by-attribute</span>
    </div>
    <div class="ech-sync-note">Companion generat din baza C10 VERBATIM + strat editor. Continut identic 1:1 cu HTML-Studiu. Lock principal prin atribut „data-locked" (fraza canonica), fallback prin potrivire de fraza. EXPORT scoate stratul de editor si livreaza HTML curat.</div>
  </div>
  </div>
</div>

'''


def split3(path):
    t = open(path, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    return t[:b], t[b:s], t[s:]


def main():
    # baza stabilizata C10: extrag body narativ verbatim
    _, base_body, _ = split3(SRC_BASE)
    # editor c09: head (cu CSS editor) + tail (cu JS editor)
    ed_head, _, ed_tail = split3(SRC_EDITOR)

    # patch identitate editor head + tail
    ed_head = ed_head.replace('<title>C09 · Relații · Trainity</title>',
                              '<title>C10 · Măsuri · Trainity</title>')
    ed_head = ed_head.replace('/* ============ NEXT (C09) ============ */',
                              '/* ============ NEXT (C10) ============ */')
    ed_head = ed_head.replace('STRAT EDITOR C09', 'STRAT EDITOR C10')
    ed_tail = ed_tail.replace('trainity_c09_study_v1', 'trainity_c10_study_v1')
    ed_tail = ed_tail.replace('PAGINA VIE · C09', 'PAGINA VIE · C10')

    # injectez panoul editor imediat dupa <body>\n\n in body-ul bazei
    assert base_body.startswith('<body>'), 'body neasteptat'
    injected = base_body.replace('<body>\n\n', '<body>\n\n' + PANEL, 1)
    assert PANEL in injected, 'panoul nu s-a injectat'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    import re
    leftover = re.findall(r'C09|trainity_c09|Date_MASTER-C09', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  panou editor injectat:', '#editor-companion-head' in out)
    print('  body identic cu baza (post-panou):', base_body.split('\n\n',1)[1][:200] in out)
    print('  leftover C09:', len(leftover), leftover[:4])


if __name__ == '__main__':
    main()
