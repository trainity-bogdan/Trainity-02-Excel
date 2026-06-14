#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c13.py - HTML-Editor-Studiu-Excel-13-Vizualizare.html.

Companion sincronizat 1:1 cu HTML-Studiu C13:
  - body narativ = EXTRAS VERBATIM din c13/HTML-Studiu (baza stabilizata, gate-clean)
  - + panou #editor-companion-head (LOCKED / editabil / garda C13 / checklist sync)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c12 Editor-Studiu
  - patch title + STORAGE_KEY + NEXT + export filename, C12 -> C13
"""
SRC_BASE = 'c13/HTML-Studiu-Excel-13-Vizualizare.html'
SRC_EDITOR = 'c12/HTML-Editor-Studiu-Excel-12-Interpretare.html'
OUT = 'c13/HTML-Editor-Studiu-Excel-13-Vizualizare.html'

PANEL = r'''<div id="editor-companion-head">
  <div class="ech-bar">
    <div class="ech-title">EDITOR-STUDIU · <b>C13 VIZUALIZARE</b> · companion sincronizat cu HTML-Studiu</div>
    <button type="button" class="ech-toggle" onclick="editorTogglePanel()" aria-label="Restrange sau extinde panoul"><span class="ech-tg-txt"></span></button>
  </div>
  <div class="ech-body">
  <div class="ech-sub">Editezi textul direct (click pe text). Zonele cu chenar rosu si lacat sunt LOCKED (nu se ating). Frazele canonice din pasi sunt blocate punctual, restul microcopy-ului ramane editabil. La final apesi EXPORT (bara de jos) ca sa descarci versiunea editata.</div>
  <div class="ech-cols">
    <div class="ech-box ech-lock">
      <div class="ech-h">Zone LOCKED (nu edita)</div>
      <ul>
        <li>Hero: „Cum dau unui rezultat forma care îl face adevărat și vizibil dintr-o privire?"</li>
        <li>AHA: „Forma greșită minte cu cifra corectă."</li>
        <li>Mantra: „Nu desenez frumos. Desenez adevărat."</li>
        <li>Intriga / GREȘEALA / CINE DEVII / WOW / MOTTO</li>
        <li>Tipul de grafic: „Categorii în bare, evoluție în linie, parte din tot în structură, relație în puncte."</li>
        <li>Codarea: „O formă onestă codează o singură dimensiune coerent."</li>
        <li>Verificare: „Dacă graficul spune mai mult sau altceva decât cifra, forma minte."</li>
        <li>Reguli: „Cele șase reguli nu sunt o listă de greșeli, sunt felul în care construiești."</li>
        <li>Garant: „Ești ultimul filtru între un rezultat corect și un ochi care îl va crede pe loc."</li>
        <li>Handoff: predarea obiectului vizual onest către treapta de compunere</li>
      </ul>
    </div>
    <div class="ech-box ech-edit">
      <div class="ech-h">Zone editabile</div>
      <ul>
        <li>formulări de introducere</li>
        <li>microcopy de pași, explicații pentru learner</li>
        <li>exemple pedagogice (fără cifre finale)</li>
        <li>text de prompt AI (păstrând scopul de a da formă onestă)</li>
        <li>payoff (fără să rupă sloturile LOCKED)</li>
      </ul>
    </div>
    <div class="ech-box ech-guard">
      <div class="ech-h">C13 rămâne la VIZUALIZARE (anti-contaminare)</div>
      <ul>
        <li>doar dă formă onestă unui rezultat deja produs de analiză</li>
        <li>nu compune pagina / dashboard-ul (acela vine la treapta de compunere)</li>
        <li>nu formulează mesajul esențial (vine la sinteză)</li>
        <li>nu livrează raportul (vine la livrare)</li>
        <li>nu explică de ce apare rezultatul (acela vine de la interpretare)</li>
        <li>zero cifre business statice în text; obiect vizual onest, nu dashboard</li>
      </ul>
    </div>
  </div>
  <div class="ech-sync">
    <div class="ech-h">Checklist sincronizare cu baza (HTML-Studiu C13 stabilizat)</div>
    <div class="ech-sync-grid">
      <span>title LOCKED</span><span>AHA verbatim</span><span>18 pași</span>
      <span>8 verificări</span><span>6 fenomene</span><span>2 prompturi AI</span>
      <span>hero VIZUAL + obiect vizual onest</span><span>lock-by-attribute</span>
    </div>
    <div class="ech-sync-note">Companion generat din baza C13 VERBATIM + strat editor. Continut identic 1:1 cu HTML-Studiu. Lock principal prin atribut „data-locked" (fraza canonica), fallback prin potrivire de fraza. EXPORT scoate stratul de editor si livreaza HTML curat.</div>
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

    # patch identitate editor head + tail C12 -> C13
    ed_head = ed_head.replace('<title>C12 · Interpretare · Trainity</title>',
                              '<title>C13 · Vizualizare · Trainity</title>')
    ed_head = ed_head.replace('/* ============ NEXT (C12) ============ */',
                              '/* ============ NEXT (C13) ============ */')
    ed_head = ed_head.replace('STRAT EDITOR C12', 'STRAT EDITOR C13')
    ed_tail = ed_tail.replace('trainity_c12_study_v1', 'trainity_c13_study_v1')
    ed_tail = ed_tail.replace('PAGINA VIE · C12', 'PAGINA VIE · C13')
    ed_tail = ed_tail.replace('HTML-Studiu-Excel-12-Interpretare-Editat.html',
                              'HTML-Studiu-Excel-13-Vizualizare-Editat.html')

    assert base_body.startswith('<body>'), 'body neasteptat'
    # FAZA 2 remediere UX: fara panel companion; editorul = pagina vie editabila (model matur c01)
    injected = base_body
    assert '#editor-companion-head' not in injected, 'model matur: panoul companion nu se injecteaza'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    import re
    leftover = re.findall(r'C12|trainity_c12|Date_MASTER-C12|Interpretare', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  panou companion eliminat (model matur):', '#editor-companion-head' not in out)
    print('  leftover C12:', len(leftover), leftover[:6])


if __name__ == '__main__':
    main()
