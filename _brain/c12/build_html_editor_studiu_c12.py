#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c12.py - HTML-Editor-Studiu-Excel-12-Interpretare.html.

Companion sincronizat 1:1 cu HTML-Studiu C12 (BRAIN-016/019):
  - body narativ = EXTRAS VERBATIM din c12/HTML-Studiu (baza stabilizata, content gate-clean)
  - + panou #editor-companion-head (LOCKED / editabil / garda C12 / checklist sync)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c09 Editor-Studiu
  - patch title + STORAGE_KEY
"""
SRC_BASE = 'c12/HTML-Studiu-Excel-12-Interpretare.html'
SRC_EDITOR = 'c09/HTML-Editor-Studiu-Excel-09-Relatii.html'
OUT = 'c12/HTML-Editor-Studiu-Excel-12-Interpretare.html'

PANEL = r'''<div id="editor-companion-head">
  <div class="ech-bar">
    <div class="ech-title">EDITOR-STUDIU · <b>C12 INTERPRETARE</b> · companion sincronizat cu HTML-Studiu (BRAIN-019)</div>
    <button type="button" class="ech-toggle" onclick="editorTogglePanel()" aria-label="Restrange sau extinde panoul"><span class="ech-tg-txt"></span></button>
  </div>
  <div class="ech-body">
  <div class="ech-sub">Editezi textul direct (click pe text). Zonele cu chenar rosu si lacat sunt LOCKED (nu se ating). Frazele canonice din pasi sunt blocate punctual, restul microcopy-ului ramane editabil. La final apesi EXPORT (bara de jos) ca sa descarci versiunea editata.</div>
  <div class="ech-cols">
    <div class="ech-box ech-lock">
      <div class="ech-h">Zone LOCKED (nu edita)</div>
      <ul>
        <li>Hero: „De ce? Și cum transform un rezultat numeric într-o explicație pe care o pot apăra?"</li>
        <li>AHA: „Nu rezultatul contează. Contează de ce apare rezultatul."</li>
        <li>Mantra: „Cifra spune cât. Explicația spune de ce."</li>
        <li>BOMBĂ / GREȘEALA / CINE DEVII / WOW / MOTTO</li>
        <li>Cauza în model: „Cauza reală apare adesea doar sub total."</li>
        <li>Ancorare: „Cauza trăiește în model, nu în intuiție."</li>
        <li>Închidere T3: „Am completat analiza setului: treapta T3 este finalizată."</li>
      </ul>
    </div>
    <div class="ech-box ech-edit">
      <div class="ech-h">Zone editabile</div>
      <ul>
        <li>formulări de introducere</li>
        <li>microcopy de pași, explicații pentru learner</li>
        <li>exemple pedagogice (fără cifre finale)</li>
        <li>text de prompt AI (păstrând scopul de a explica)</li>
        <li>payoff (fără să rupă sloturile LOCKED)</li>
      </ul>
    </div>
    <div class="ech-box ech-guard">
      <div class="ech-h">C12 rămâne la INTERPRETARE (anti-contaminare)</div>
      <ul>
        <li>doar explică: cauza citită din model, insight verbal, verificabil</li>
        <li>nu re-clasează, nu reordonează (clasamentul vine de la treapta comparațiilor)</li>
        <li>fără tablou vizual de raportare (acela vine la treapta de raportare)</li>
        <li>fără simulări, prognoze sau acțiuni declanșate (treapta de automatizare)</li>
        <li>zero cifre business statice în text</li>
        <li>hero INTERPRETARE dedicat (fără clonă vizuală din treapta anterioară)</li>
      </ul>
    </div>
  </div>
  <div class="ech-sync">
    <div class="ech-h">Checklist sincronizare cu baza (HTML-Studiu C12 stabilizat)</div>
    <div class="ech-sync-grid">
      <span>title LOCKED</span><span>AHA verbatim</span><span>18 pași</span>
      <span>8 verificări</span><span>6 fenomene</span><span>2 prompturi AI</span>
      <span>cauză citită din model + verificabil</span><span>lock-by-attribute</span>
    </div>
    <div class="ech-sync-note">Companion generat din baza C12 VERBATIM + strat editor. Continut identic 1:1 cu HTML-Studiu. Lock principal prin atribut „data-locked" (fraza canonica), fallback prin potrivire de fraza. EXPORT scoate stratul de editor si livreaza HTML curat.</div>
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
    _, base_body, _ = split3(SRC_BASE)
    ed_head, _, ed_tail = split3(SRC_EDITOR)

    # patch identitate editor head + tail C09 -> C12
    ed_head = ed_head.replace('<title>C09 · Relații · Trainity</title>',
                              '<title>C12 · Interpretare · Trainity</title>')
    ed_head = ed_head.replace('/* ============ NEXT (C09) ============ */',
                              '/* ============ NEXT (C12) ============ */')
    ed_head = ed_head.replace('STRAT EDITOR C09', 'STRAT EDITOR C12')
    ed_tail = ed_tail.replace('trainity_c09_study_v1', 'trainity_c12_study_v1')
    ed_tail = ed_tail.replace('PAGINA VIE · C09', 'PAGINA VIE · C12')
    ed_tail = ed_tail.replace('HTML-Studiu-Excel-09-Relatii-Editat.html',
                              'HTML-Studiu-Excel-12-Interpretare-Editat.html')

    assert base_body.startswith('<body>'), 'body neasteptat'
    injected = base_body.replace('<body>\n\n', '<body>\n\n' + PANEL, 1)
    assert PANEL in injected, 'panoul nu s-a injectat'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    import re
    leftover = re.findall(r'C09|trainity_c09|Date_MASTER-C09|Relatii', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  panou editor injectat:', '#editor-companion-head' in out)
    print('  leftover C09:', len(leftover), leftover[:4])


if __name__ == '__main__':
    main()
