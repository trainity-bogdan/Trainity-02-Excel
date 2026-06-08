#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c13.py - HTML-Video-Excel-13-Vizualizare.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c12 Video. Inlocuiesc:
  - BODY scaffolding (hero, exec slides, final, conclusion, topbar) -> C13 VIZUALIZARE
  - const STAGES [...] + const PROMPTS {...} -> C13 (18 step-titles LOCKED)
  - STORAGE_KEY, <title>, exec placeholders -> C13
Garda C13: a da forma onesta. Obiect vizual onest, ZERO dashboard/pagina (C14),
zero mesaj (C15), zero livrare (C16), zero 'de ce' (C12). Cifrele in Excel (R-V02.15).
"""
import re

SRC = 'c12/HTML-Video-Excel-12-Interpretare.html'
OUT = 'c13/HTML-Video-Excel-13-Vizualizare.html'

EXEC_TITLES = {1: 'REALITATE', 2: 'INVESTIGATIE', 3: 'TRANSFORMARE',
               4: 'VERIFICARE', 5: 'STABILIZARE', 6: 'CONFIRMARE'}


def exec_placeholder(n, titlu):
    return (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
        "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
        "</linearGradient></defs><rect width='1600' height='900' fill='url(%23g)'/>"
        "<text x='80' y='480' fill='%23FFD400' font-family='Georgia' font-size='90' "
        "font-weight='bold'>" + titlu + "</text>"
        "<text x='84' y='540' fill='%23ffffff' font-family='Arial' font-size='30' "
        "opacity='0.6'>C13 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )


BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C13 · Vizualizare</div>
  <button class="skipped-btn" id="skipped-btn" onclick="jumpToNextSkipped()" style="display:none">
    <span class="skipped-icon">⚠</span>
    <span class="skipped-text">Mergem la pas sărit</span>
    <span class="skipped-count" id="skipped-count">0</span>
  </button>
</header>

<!-- MAIN STAGE -->
<main class="stage" id="stage">

  <!-- BUTOANE FIXE jos in zona stage -->
  <div class="stage-nav-fixed" id="stage-nav-fixed">
    <button class="nav-btn nav-btn-prev" id="nav-prev" onclick="prevStep()">← Înapoi</button>
    <button class="nav-btn nav-btn-next" id="nav-next" onclick="nextStep()">Înainte →</button>
  </div>

  <!-- HERO INTRO -->
  <section class="screen" data-screen="hero" data-frag-total="2">
    <div class="hero-prelabel">Construcția 13 Excel</div>
    <h1 class="hero-title">FORMA<br>ADEVĂRATĂ</h1>
    <p class="hero-hook frag" data-frag="1">Cifra e corectă.<br><span class="hero-hook-twist">Graficul minte.</span></p>
    <p class="hero-sub frag" data-frag="2">Analiza a dat răspunsul. Acum îi dăm forma care îl face adevărat și vizibil dintr-o privire, verificată contra cifrei brute.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am compus nicio pagină.</p>
      <p class="dim frag" data-frag="2">Nu am formulat niciun mesaj.</p>
      <p class="dim frag" data-frag="3">Nu am livrat niciun raport.</p>
      <p class="accent frag" data-frag="4">Un rezultat corect, acum cu o formă pe care ochiul o crede pentru că e adevărată.</p>
      <p class="frag" data-frag="5">Aceeași cifră, două grafice, două concluzii. Apoi forma onestă a reparat percepția.</p>
      <p class="frag" data-frag="6">Obiectul vizual onest e gata de așezat în pagină.</p>
      <div class="final-motto frag" data-frag="7">Forma nu se nimerește.<br>Se alege.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 13</span>
      </h1>
      <div class="conclusion-divider frag" data-frag="2"></div>
    </div>
  </section>

  <!-- EXECUTIVE SHOW - 7 screens -->
  <section class="screen" data-screen="executive" data-exec-slide="1" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-1"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">01</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 01</div>
      <div class="exec-emotion frag" data-frag="2">Răspuns fără formă</div>
      <h2 class="exec-title frag" data-frag="3">REALITATE</h2>
      <p class="exec-phrase frag" data-frag="4">Te uiți la un rezultat corect. Și la o întrebare fără răspuns: cum îl vede altcineva?</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Forma e o alegere</div>
      <h2 class="exec-title frag" data-frag="3">INVESTIGAȚIE</h2>
      <p class="exec-phrase frag" data-frag="4">Aceeași cifră are mai multe forme. Una spune adevărul, alta minte cu cifra corectă.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Forma devine onestă</div>
      <h2 class="exec-title frag" data-frag="3">TRANSFORMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Tipul urmează natura rezultatului, axa pleacă de la zero, codarea care minte iese.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Forma rezistă</div>
      <h2 class="exec-title frag" data-frag="3">VERIFICARE</h2>
      <p class="exec-phrase frag" data-frag="4">Vizualul citit singur dă aceeași concluzie ca cifra brută. Dacă spune mai mult, iese.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Forma devine regulă</div>
      <h2 class="exec-title frag" data-frag="3">STABILIZARE</h2>
      <p class="exec-phrase frag" data-frag="4">Cele șase reguli fac orice vizual următor onest din naștere, nu din noroc.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">Obiect onest</div>
      <h2 class="exec-title frag" data-frag="3">CONFIRMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Forma adevărată a reparat percepția. Obiectul vizual onest e gata de predat la compunere.</p>
    </div>
  </section>

  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        Forma nu se nimerește.
        <span class="exec-closing-motto-yellow">Se alege.</span>
      </h1>
      <div class="exec-closing-divider frag" data-frag="3"></div>
      <div class="exec-closing-signature frag" data-frag="4">
        <span class="sig-line-1">Trainity · Sistemul 02 Excel</span>
        <span class="sig-line-2">Bogdan Târlă <span class="sig-yellow">(Dr.Excel)</span></span>
      </div>
    </div>
  </section>

</main>

<!-- RIGHT CONTROL PANEL -->
<aside class="panel">
  <div class="panel-section">
    <div class="panel-label">Progres pași</div>
    <div class="progress-big" id="progress-num">00<span class="total">/18</span></div>
    <div class="progress-bar"><div class="progress-bar-fill" id="progress-fill"></div></div>
  </div>

  <div class="panel-section">
    <div class="panel-label">Etape</div>
    <ul class="stage-list" id="stage-list"></ul>
  </div>

  <div class="controls">
    <button class="btn btn-validate" id="btn-action" onclick="validateCurrent()" style="display:none">Validează</button>
    <button class="btn btn-reset" onclick="showResetModal()">Reset progres</button>
    <div class="keyhint">
      <kbd>←</kbd> <kbd>→</kbd> navigare · <kbd>V</kbd> validează
    </div>
  </div>
</aside>

<!-- TOAST -->
<div class="toast" id="toast">Pas validat</div>

<!-- MODAL RESET -->
<div class="modal" id="modal-reset">
  <div class="modal-box">
    <div class="modal-title">Reset progres?</div>
    <div class="modal-text">Toate validările vor fi șterse. Pagina revine la ecranul de introducere.</div>
    <div class="modal-actions">
      <button class="btn btn-secondary" onclick="hideResetModal()">Anulează</button>
      <button class="btn btn-validate" onclick="doReset()">Reset</button>
    </div>
  </div>
</div>

'''

STAGES = r'''const STAGES = [
  {
    id: 1, name: "REALITATE", emotion: "Răspunsul fără formă",
    hook: "Analiza a dat răspunsul corect. Dar în model e mut.",
    next: "Astăzi îi dăm o formă onestă.",
    steps: [
      { num: "01", title: "Răspunsul corect, dar invizibil.",
        instr: "Date_MASTER-C13-Vizualizare.xlsx. Vine cu răspunsul produs de analiză. <strong>Corect nu înseamnă văzut: răspunsul trăiește în model.</strong>",
        excel: true },
      { num: "02", title: "Nimeni nu decide privind un model.",
        instr: "Un decident nu citește un Power Pivot ca să hotărască dintr-o privire. <strong>Lipsa nu e de analiză, e de formă.</strong>",
        excel: true },
      { num: "03", title: "Aceeași cifră, încă fără formă.",
        instr: "Iei un rezultat din răspuns. <strong>Nu îl re-analizezi: răspunsul vine de la analiză, tu doar îi dai formă.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "INVESTIGAȚIE", emotion: "Forma e o alegere",
    hook: "Aceeași cifră are mai multe forme. Forma greșită schimbă concluzia.",
    next: "Copilot propune forma. Tu judeci.",
    steps: [
      { num: "04", title: "O cifră, mai multe forme posibile.",
        instr: "Bară, linie, plăcintă, număr mare. <strong>Forma nu e dată de cifră, e aleasă de tine.</strong>",
        excel: true },
      { num: "05", title: "Ce formă cere rezultatul. Promptul 1.", instr: "", prompt: 1 },
      { num: "06", title: "Aceeași cifră, două grafice, două concluzii.",
        instr: "Una cu axa de la zero, una cu axa trunchiată. <strong>Nu cifra s-a schimbat, ci forma. Și ochiul a crezut forma.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "TRANSFORMARE", emotion: "Forma devine onestă",
    hook: "Rezultatul capătă forma onestă: tip, axă, scală, codare.",
    next: "Și scoatem ce sugerează fals.",
    steps: [
      { num: "07", title: "Tipul de grafic urmează natura rezultatului.",
        instr: "Categorii în bare, evoluție în linie, parte din tot în structură. <strong>Forma nu se nimerește, se alege.</strong>",
        excel: true },
      { num: "08", title: "Generezi vizualul, corectezi axa și scala. Promptul 2.", instr: "", prompt: 2 },
      { num: "09", title: "Scoți codarea care sugerează fals.",
        instr: "3D, gradient, arie dublă, culoare care insinuează. <strong>O formă onestă codează o singură dimensiune coerent.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "VERIFICARE", emotion: "Forma rezistă",
    hook: "O formă onestă produce aceeași concluzie ca cifra brută.",
    next: "Și rezistă unui al doilea ochi.",
    steps: [
      { num: "10", title: "Vizualul față de cifra brută: aceeași concluzie?",
        instr: "Citești concluzia din grafic, apoi din număr. <strong>Dacă graficul spune mai mult sau altceva, forma minte.</strong>",
        excel: true },
      { num: "11", title: "Testul celui de-al doilea ochi.",
        instr: "Dai vizualul cuiva care vede doar graficul. <strong>Un grafic onest nu are nevoie de autor lângă el ca să fie citit corect.</strong>",
        excel: true },
      { num: "12", title: "Marchezi forma care spune mai mult decât cifra.",
        instr: "Treci fiecare vizual prin cele șase întrebări de onestitate. <strong>Ce adaugă o concluzie nesusținută se corectează sau iese.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "STABILIZARE", emotion: "Forma devine regulă",
    hook: "Onestitatea nu e un noroc de o dată. O fixezi în reguli.",
    next: "Ca orice vizual următor să se nască onest.",
    steps: [
      { num: "13", title: "Cele șase reguli de onestitate a formei.",
        instr: "Axă de la zero, tip după natură, o scală declarată, o dimensiune codată, distribuția nu doar media, etichetă prezentă. <strong>Cele șase reguli sunt felul în care construiești.</strong>",
        excel: true },
      { num: "14", title: "Eticheta, unitatea, contextul: nimic de ghicit.",
        instr: "Pui unitatea, eticheta axelor, perioada, sursa. <strong>Un obiect vizual onest se citește singur.</strong>",
        excel: true },
      { num: "15", title: "Un obiect vizual onest, repetabil.",
        instr: "Vine un rezultat nou din aceeași natură: aplici aceleași reguli. <strong>Forma e acum repetabilă, nu o reușită de moment.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "CONFIRMARE", emotion: "Obiectul adevărat",
    hook: "Forma onestă repară percepția. Devii garantul a ce vede altcineva.",
    next: "Și predai obiectul mai departe.",
    steps: [
      { num: "16", title: "Forma onestă repară percepția.",
        instr: "Pui față în față forma care mințea și forma onestă. <strong>Aceeași cifră, dar forma adevărată a reparat percepția.</strong>",
        excel: true },
      { num: "17", title: "Devii garantul a ceea ce vede altcineva.",
        instr: "Nu mai întrebi ce grafic arată mai bine, ci ce grafic arată adevărat. <strong>Ești ultimul filtru între un rezultat corect și un ochi care îl crede pe loc.</strong>",
        excel: true },
      { num: "18", title: "Predai către C14: obiectul, gata de așezat în pagină.",
        instr: "Predai un obiect vizual onest, verificat contra cifrei. <strong>C13 face obiectul adevărat. Treapta de compunere îl așază în pagină.</strong>",
        excel: false }
    ]
  }
];

'''

PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Ce formă cere rezultatul",
    text: "Am un rezultat produs de analiză (o comparație, o evoluție, o parte dintr-un total sau o relație). Spune-mi ce tip de reprezentare i se potrivește naturii lui, ce tipuri l-ar deforma și de ce, și ce reguli de axă și scală țin forma onestă. Nu inventa rezultate noi și nu explica de ce apare rezultatul; lucrează doar cu forma care îl face vizibil corect. Nu compune o pagină și nu propune un dashboard.",
    meta: "Copilot propune forma. Tu judeci."
  },
  2: {
    label: "Prompt 02 · Generezi vizualul, corectezi axa și scala",
    text: "Generează vizualul pentru rezultatul ales, în tipul potrivit naturii lui. Apoi verifică și corectează: axa pleacă de la zero sau abaterea e declarată, scala e una singură și liniară, unitatea și eticheta sunt prezente, iar codarea reprezintă o singură dimensiune (fără 3D, gradient sau arie dublă). Nu adăuga un al doilea vizual și nu așeza pagina; rămâi la un singur obiect vizual onest.",
    meta: "Un singur obiect vizual onest, verificabil."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = head.replace('<title>C12 · CAUZĂ · BROADCAST</title>',
                        '<title>C13 · VIZUAL · BROADCAST</title>')
    # exec placeholders C12 -> C13 (sursa c12 are deja SVG placeholder)
    for n in range(1, 7):
        ph = exec_placeholder(n, EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)

    i_st = tail.index('const STAGES = [')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + STAGES + PROMPTS + tail[i_fl:]
    tail = tail.replace('trainity_c12_video_v1', 'trainity_c13_video_v1')

    out = head + BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C12|trainity_c12|Date_MASTER-C12|INTERPRETARE|de ce-ul', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  exec base64 jpeg ramase:', out.count('data:image/jpeg;base64,'))
    print('  leftover C12:', len(leftover), leftover[:6])
    print('  STAGES steps:', out.count('num: "'))


if __name__ == '__main__':
    main()
