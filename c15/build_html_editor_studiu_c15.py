#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_editor_studiu_c15.py - HTML-Editor-Studiu-Excel-15-Sintetizare.html.

Companion sincronizat 1:1 cu HTML-Studiu C15:
  - body narativ = EXTRAS VERBATIM din c15/HTML-Studiu (baza stabilizata, gate-clean)
  - + panou #editor-companion-head (LOCKED / editabil / garda C15 / checklist sync)
  - head+CSS editor + JS editor (export, lock-by-attribute) = din c14 Editor-Studiu
  - patch title + STORAGE_KEY + NEXT + export filename, C14 -> C15
"""
SRC_BASE = 'c15/HTML-Studiu-Excel-15-Sintetizare.html'
SRC_EDITOR = 'c14/HTML-Editor-Studiu-Excel-14-Compunere.html'
OUT = 'c15/HTML-Editor-Studiu-Excel-15-Sintetizare.html'

PANEL = r'''<div id="editor-companion-head">
  <div class="ech-bar">
    <div class="ech-title">EDITOR-STUDIU · <b>C15 SINTETIZARE</b> · companion sincronizat cu HTML-Studiu</div>
    <button type="button" class="ech-toggle" onclick="editorTogglePanel()" aria-label="Restrange sau extinde panoul"><span class="ech-tg-txt"></span></button>
  </div>
  <div class="ech-body">
  <div class="ech-sub">Editezi textul direct (click pe text). Zonele cu chenar rosu si lacat sunt LOCKED (nu se ating). Frazele canonice din pasi sunt blocate punctual, restul microcopy-ului ramane editabil. La final apesi EXPORT (bara de jos) ca sa descarci versiunea editata.</div>
  <div class="ech-cols">
    <div class="ech-box ech-lock">
      <div class="ech-h">Zone LOCKED (nu edita)</div>
      <ul>
        <li>Hero: „Cum transform o pagină într-o singură frază care contează?"</li>
        <li>AHA: „O pagină arată. O sinteză spune."</li>
        <li>Mantra: „Nu rezumăm. Sintetizăm."</li>
        <li>Intriga / GREȘEALA / CINE DEVII / WOW / MOTTO</li>
        <li>Formula: „Rezumatul scurtează tot. Sinteza spune ce contează."</li>
        <li>Pagina mută: „O pagină arată; nu spune."</li>
        <li>Mesajul: „Mesajul nu se descoperă aici, vine gata din analiză; tu îl formulezi."</li>
        <li>Filtru: „Fără această frază, decidentul hotărăște la fel? Dacă da, nu e mesajul."</li>
        <li>Reformulare: „Refaci sinteza; nu atingi nicio cifră, cifrele rămân ale modelului."</li>
        <li>Handoff: predarea mesajului și a paginii-dovadă către treapta de livrare</li>
      </ul>
    </div>
    <div class="ech-box ech-edit">
      <div class="ech-h">Zone editabile</div>
      <ul>
        <li>formulări de introducere</li>
        <li>microcopy de pași, explicații pentru learner</li>
        <li>exemple pedagogice (fără cifre finale)</li>
        <li>text de prompt AI (păstrând scopul de a formula mesajul, nu de a calcula sau a livra)</li>
        <li>payoff (fără să rupă sloturile LOCKED)</li>
      </ul>
    </div>
    <div class="ech-box ech-guard">
      <div class="ech-h">C15 rămâne la SINTEZĂ (anti-contaminare)</div>
      <ul>
        <li>doar formulează mesajul esențial: o singură frază pe care pagina o dovedește</li>
        <li>SINTEZĂ != REZUMAT: alege ce contează, nu scurtează tot proporțional</li>
        <li>nu calculează insight și nu descoperă cauză (acelea vin din analiză)</li>
        <li>nu rearanjează pagina (aceea e compunerea)</li>
        <li>nu numește decizia și nu livrează raportul (acelea vin la livrare)</li>
        <li>zero cifre business statice în text; mesaj formulat, nu calculat</li>
      </ul>
    </div>
  </div>
  <div class="ech-sync">
    <div class="ech-h">Checklist sincronizare cu baza (HTML-Studiu C15 stabilizat)</div>
    <div class="ech-sync-grid">
      <span>title LOCKED</span><span>AHA verbatim</span><span>18 pași</span>
      <span>8 verificări</span><span>5 fenomene</span><span>2 prompturi AI</span>
      <span>hero SINTEZĂ + mesaj esențial</span><span>lock-by-attribute</span>
    </div>
    <div class="ech-sync-note">Companion generat din baza C15 VERBATIM + strat editor. Continut identic 1:1 cu HTML-Studiu. Lock principal prin atribut „data-locked" (fraza canonica), fallback prin potrivire de fraza. EXPORT scoate stratul de editor si livreaza HTML curat.</div>
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

    # patch identitate editor head + tail C14 -> C15
    ed_head = ed_head.replace('<title>C14 · Compunere · Trainity</title>',
                              '<title>C15 · Sintetizare · Trainity</title>')
    ed_head = ed_head.replace('/* ============ NEXT (C14) ============ */',
                              '/* ============ NEXT (C15) ============ */')
    ed_head = ed_head.replace('STRAT EDITOR C14', 'STRAT EDITOR C15')
    ed_tail = ed_tail.replace('trainity_c14_study_v1', 'trainity_c15_study_v1')
    ed_tail = ed_tail.replace('PAGINA VIE · C14', 'PAGINA VIE · C15')
    ed_tail = ed_tail.replace('HTML-Studiu-Excel-14-Compunere-Editat.html',
                              'HTML-Studiu-Excel-15-Sintetizare-Editat.html')

    assert base_body.startswith('<body>'), 'body neasteptat'
    injected = base_body.replace('<body>\n\n', '<body>\n\n' + PANEL, 1)
    assert PANEL in injected, 'panoul nu s-a injectat'

    out = ed_head + injected + ed_tail
    import os
    os.makedirs('c15', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)

    import re
    leftover = re.findall(r'C14|trainity_c14|Date_MASTER-C14|Compunere', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  panou editor injectat:', '#editor-companion-head' in out)
    print('  leftover C14:', len(leftover), leftover[:6])


if __name__ == '__main__':
    main()
