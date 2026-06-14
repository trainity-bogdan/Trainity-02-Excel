#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c16.py - HTML-Editor-Studiu-Excel-16-Livrare.html.

Companion sincronizat 1:1 cu HTML-Studiu C16:
  - body narativ = EXTRAS VERBATIM din c16/HTML-Studiu (baza stabilizata, gate-clean)
  - + panou #editor-companion-head (LOCKED / editabil / garda C16 / checklist sync)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c14 Editor-Studiu
  - patch title + STORAGE_KEY + NEXT + export filename, C14 -> C16 (regex robust)
"""
import re
SRC_BASE = 'c16/HTML-Studiu-Excel-16-Livrare.html'
SRC_EDITOR = 'c14/HTML-Editor-Studiu-Excel-14-Compunere.html'
OUT = 'c16/HTML-Editor-Studiu-Excel-16-Livrare.html'

PANEL = r'''<div id="editor-companion-head">
  <div class="ech-bar">
    <div class="ech-title">EDITOR-STUDIU · <b>C16 LIVRARE</b> · companion sincronizat cu HTML-Studiu</div>
    <button type="button" class="ech-toggle" onclick="editorTogglePanel()" aria-label="Restrange sau extinde panoul"><span class="ech-tg-txt"></span></button>
  </div>
  <div class="ech-body">
  <div class="ech-sub">Editezi textul direct (click pe text). Zonele cu chenar rosu si lacat sunt LOCKED (nu se ating). Frazele canonice din pasi sunt blocate punctual, restul microcopy-ului ramane editabil. La final apesi EXPORT (bara de jos) ca sa descarci versiunea editata.</div>
  <div class="ech-cols">
    <div class="ech-box ech-lock">
      <div class="ech-h">Zone LOCKED (nu edita)</div>
      <ul>
        <li>Hero: „Cum dau raportului forma care îl face o decizie gata de luat, nu doar informație trimisă?"</li>
        <li>AHA: „Un raport care nu produce o decizie nu e livrat, e doar trimis."</li>
        <li>Mantra: „Nu livrez informație. Livrez o decizie gata de luat."</li>
        <li>Intriga / GREȘEALA / CINE DEVII / WOW / MOTTO</li>
        <li>Pas 3: „mesajul vine gata, tu îi dai forma de decizie."</li>
        <li>Pas 7: „Nu o re-formulezi, o poziționezi."</li>
        <li>Pas 11: „Întrebările de bază sunt vina formei și se elimină."</li>
        <li>Pas 17: „Ești ultimul filtru între un mesaj corect și un decident care trebuie să acționeze."</li>
        <li>Handoff: „C16 face raportul o decizie. Treapta următoare îl face să ruleze singur."</li>
      </ul>
    </div>
    <div class="ech-box ech-edit">
      <div class="ech-h">Zone editabile</div>
      <ul>
        <li>formulări de introducere</li>
        <li>microcopy de pași, explicații pentru learner</li>
        <li>exemple pedagogice (fără cifre finale)</li>
        <li>text de prompt AI (păstrând scopul de a face raportul decision-ready)</li>
        <li>payoff (fără să rupă sloturile LOCKED)</li>
      </ul>
    </div>
    <div class="ech-box ech-guard">
      <div class="ech-h">C16 rămâne la LIVRARE (anti-contaminare)</div>
      <ul>
        <li>doar dă raportului forma de decizie (decision-ready)</li>
        <li>nu sintetizează mesajul esențial (acela vine de la sinteză)</li>
        <li>nu compune pagina / layout vizual (acela vine de la compunere)</li>
        <li>nu sistematizează recurent și nu automatizează (acelea vin la autonomie)</li>
        <li>nu e logistică: nu email, export, share, trimitere</li>
        <li>zero cifre business statice în text; foaie-raport de decizie, nu dashboard</li>
      </ul>
    </div>
  </div>
  <div class="ech-sync">
    <div class="ech-h">Checklist sincronizare cu baza (HTML-Studiu C16 stabilizat)</div>
    <div class="ech-sync-grid">
      <span>title LOCKED</span><span>AHA verbatim</span><span>18 pași</span>
      <span>8 verificări</span><span>6 fenomene</span><span>2 prompturi AI</span>
      <span>hero LIVRARE + obiect de decizie</span><span>lock-by-attribute</span>
    </div>
    <div class="ech-sync-note">Companion generat din baza C16 VERBATIM + strat editor. Continut identic 1:1 cu HTML-Studiu. Lock principal prin atribut „data-locked" (fraza canonica), fallback prin potrivire de fraza. EXPORT scoate stratul de editor si livreaza HTML curat.</div>
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

    # patch identitate editor head + tail C14 -> C16 (regex robust)
    ed_head = re.sub(r'<title>.*?</title>', '<title>C16 · Livrare · Trainity</title>', ed_head, count=1)
    ed_head = re.sub(r'NEXT \(C\d+\)', 'NEXT (C16)', ed_head)
    ed_head = re.sub(r'STRAT EDITOR C\d+', 'STRAT EDITOR C16', ed_head)
    ed_tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c16_study_v1', ed_tail)
    ed_tail = re.sub(r'PAGINA VIE · C\d+', 'PAGINA VIE · C16', ed_tail)
    ed_tail = re.sub(r'HTML-Studiu-Excel-\d+-[\wăâîșțĂÂÎȘȚ]+-Editat\.html',
                     'HTML-Studiu-Excel-16-Livrare-Editat.html', ed_tail)

    assert base_body.startswith('<body>'), 'body neasteptat'
    # FAZA 2 remediere UX: fara panel companion; editorul = pagina vie editabila (model matur c01)
    injected = base_body
    assert '#editor-companion-head' not in injected, 'model matur: panoul companion nu se injecteaza'

    out = ed_head + injected + ed_tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C14|trainity_c14|Date_MASTER-C14|Compunere|COMPUNERE', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  panou companion eliminat (model matur):', '#editor-companion-head' not in out)
    print('  leftover C14:', len(leftover), leftover[:8])


if __name__ == '__main__':
    main()
