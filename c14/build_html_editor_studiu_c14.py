#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c14.py - HTML-Editor-Studiu-Excel-14-Compunere.html.

Companion sincronizat 1:1 cu HTML-Studiu C14:
  - body narativ = EXTRAS VERBATIM din c14/HTML-Studiu (baza stabilizata, gate-clean)
  - + panou #editor-companion-head (LOCKED / editabil / garda C14 / checklist sync)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c13 Editor-Studiu
  - patch title + STORAGE_KEY + NEXT + export filename, C13 -> C14
"""
SRC_BASE = 'c14/HTML-Studiu-Excel-14-Compunere.html'
SRC_EDITOR = 'c13/HTML-Editor-Studiu-Excel-13-Vizualizare.html'
OUT = 'c14/HTML-Editor-Studiu-Excel-14-Compunere.html'

PANEL = r'''<div id="editor-companion-head">
  <div class="ech-bar">
    <div class="ech-title">EDITOR-STUDIU · <b>C14 COMPUNERE</b> · companion sincronizat cu HTML-Studiu</div>
    <button type="button" class="ech-toggle" onclick="editorTogglePanel()" aria-label="Restrange sau extinde panoul"><span class="ech-tg-txt"></span></button>
  </div>
  <div class="ech-body">
  <div class="ech-sub">Editezi textul direct (click pe text). Zonele cu chenar rosu si lacat sunt LOCKED (nu se ating). Frazele canonice din pasi sunt blocate punctual, restul microcopy-ului ramane editabil. La final apesi EXPORT (bara de jos) ca sa descarci versiunea editata.</div>
  <div class="ech-cols">
    <div class="ech-box ech-lock">
      <div class="ech-h">Zone LOCKED (nu edita)</div>
      <ul>
        <li>Hero: „Ce vede ochiul întâi?"</li>
        <li>AHA: „Aceleași grafice, altă ordine, altă decizie."</li>
        <li>Mantra: „Compun privirea, nu pagina."</li>
        <li>Intriga / GREȘEALA / CINE DEVII / WOW / MOTTO</li>
        <li>Poziția: „Ce stă sus, mare sau în centru spune important; ce stă jos, mic sau în margine spune secundar."</li>
        <li>Focar: „O pagină are un singur focar, nu cinci."</li>
        <li>Retrogradare: „Fără acest element în prim-plan, decidentul hotărăște la fel?"</li>
        <li>Ierarhie: „Greutate inegală pentru lucruri inegale, prin mărime, poziție, contrast și spațiu."</li>
        <li>Grupare: „Proximitatea spune adevărul despre relații: lângă înseamnă împreună."</li>
        <li>Spațiu: „Spațiul gol nu e lipsă, e instrument: izolează ce contează și separă ce e diferit."</li>
        <li>Handoff: predarea paginii coerente către treapta de sintetizare</li>
      </ul>
    </div>
    <div class="ech-box ech-edit">
      <div class="ech-h">Zone editabile</div>
      <ul>
        <li>formulări de introducere</li>
        <li>microcopy de pași, explicații pentru learner</li>
        <li>exemple pedagogice (fără cifre finale)</li>
        <li>text de prompt AI (păstrând scopul de a așeza spațial, nu de a desena sau a formula mesajul)</li>
        <li>payoff (fără să rupă sloturile LOCKED)</li>
      </ul>
    </div>
    <div class="ech-box ech-guard">
      <div class="ech-h">C14 rămâne la COMPUNERE (anti-contaminare)</div>
      <ul>
        <li>doar așază spațial obiecte vizuale deja produse: focar, ierarhie, traseu, grupare, spațiu</li>
        <li>nu desenează și nu redesenează obiectul vizual (acela vine de la treapta de vizualizare)</li>
        <li>nu formulează mesajul esențial (vine la sinteză)</li>
        <li>nu livrează raportul decision-ready (vine la livrare)</li>
        <li>nu se autorizează ca dashboard: dashboard e substrat tehnic, nu identitate</li>
        <li>zero cifre business statice în text; pagină compusă, nu obiect și nu mesaj</li>
      </ul>
    </div>
  </div>
  <div class="ech-sync">
    <div class="ech-h">Checklist sincronizare cu baza (HTML-Studiu C14 stabilizat)</div>
    <div class="ech-sync-grid">
      <span>title LOCKED</span><span>AHA verbatim</span><span>11 pași</span>
      <span>8 verificări</span><span>6 fenomene</span><span>2 prompturi AI</span>
      <span>hero COMPOZIȚIE + pagină compusă</span><span>lock-by-attribute</span>
    </div>
    <div class="ech-sync-note">Companion generat din baza C14 VERBATIM + strat editor. Continut identic 1:1 cu HTML-Studiu. Lock principal prin atribut „data-locked" (fraza canonica), fallback prin potrivire de fraza. EXPORT scoate stratul de editor si livreaza HTML curat.</div>
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

    # patch identitate editor head + tail C13 -> C14
    ed_head = ed_head.replace('<title>C13 · Vizualizare · Trainity</title>',
                              '<title>C14 · Compunere · Trainity</title>')
    ed_head = ed_head.replace('/* ============ NEXT (C13) ============ */',
                              '/* ============ NEXT (C14) ============ */')
    ed_head = ed_head.replace('STRAT EDITOR C13', 'STRAT EDITOR C14')
    ed_tail = ed_tail.replace('trainity_c13_study_v1', 'trainity_c14_study_v1')
    ed_tail = ed_tail.replace('PAGINA VIE · C13', 'PAGINA VIE · C14')
    ed_tail = ed_tail.replace('HTML-Studiu-Excel-13-Vizualizare-Editat.html',
                              'HTML-Studiu-Excel-14-Compunere-Editat.html')

    assert base_body.startswith('<body>'), 'body neasteptat'
    # FAZA 2 remediere UX: fara panel companion; editorul = pagina vie editabila (model matur c01)
    injected = base_body
    assert '#editor-companion-head' not in injected, 'model matur: panoul companion nu se injecteaza'

    out = ed_head + injected + ed_tail
    import os
    os.makedirs('c14', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)

    import re
    leftover = re.findall(r'C13|trainity_c13|Date_MASTER-C13|Vizualizare', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  panou companion eliminat (model matur):', '#editor-companion-head' not in out)
    print('  leftover C13:', len(leftover), leftover[:6])


if __name__ == '__main__':
    main()
