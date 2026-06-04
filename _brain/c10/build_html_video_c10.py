#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c10.py - HTML-Video-Excel-10-Masuri.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c09 Video. Inlocuiesc:
  - BODY scaffolding (hero, final, conclusion, 7 exec slides, topbar) -> C10 MASURI
  - const STAGES [...] + const PROMPTS {...} (continutul pasilor) -> C10
  - STORAGE_KEY, <title>
  - 6 imagini exec base64 din head CSS -> placeholder SVG (dependenta ARHITECT)

Garda C10: a defini (Cat?). Zero ranking/contributie (C11), cauza (C12), dashboard (T4).
"""
import re

SRC = 'c09/HTML-Video-Excel-09-Relatii.html'
OUT = 'c10/HTML-Video-Excel-10-Masuri.html'


def exec_placeholder(n, titlu):
    svg = (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
        "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
        "</linearGradient></defs><rect width='1600' height='900' fill='url(%23g)'/>"
        "<text x='80' y='480' fill='%23FFD400' font-family='Georgia' font-size='90' "
        "font-weight='bold'>" + titlu + "</text>"
        "<text x='84' y='540' fill='%23ffffff' font-family='Arial' font-size='30' "
        "opacity='0.6'>C10 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )
    return svg


EXEC_TITLES = {1: 'REALITATE', 2: 'INVESTIGATIE', 3: 'TRANSFORMARE',
               4: 'VERIFICARE', 5: 'STABILIZARE', 6: 'CONFIRMARE'}

BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C10 · Măsuri</div>
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
    <div class="hero-prelabel">Construcția 10 Excel</div>
    <h1 class="hero-title">MĂSURA<br>POTRIVITĂ</h1>
    <p class="hero-hook frag" data-frag="1">Ai toate cifrele.<br><span class="hero-hook-twist">Și nicio decizie.</span></p>
    <p class="hero-sub frag" data-frag="2">Înainte de orice clasament, definim măsura: o singură dată, cu bază și reper.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am comparat nimic.</p>
      <p class="dim frag" data-frag="2">Nu am clasat nicio felie.</p>
      <p class="dim frag" data-frag="3">Nu am interpretat niciun motiv.</p>
      <p class="accent frag" data-frag="4">Cifre care veneau brute, fără definiție. Acum sunt măsuri cu bază și reper.</p>
      <p class="frag" data-frag="5">O ceri pe orice felie și rămâne aceeași.</p>
      <p class="frag" data-frag="6">C11 poate începe.</p>
      <div class="final-motto frag" data-frag="7">O măsură definită o dată.<br>Apoi clasamentul.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 10</span>
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
      <div class="exec-emotion frag" data-frag="2">Cifre fără măsură</div>
      <h2 class="exec-title frag" data-frag="3">REALITATE</h2>
      <p class="exec-phrase frag" data-frag="4">Te uiți la un model care răspunde. Și la cifre care încă nu sunt măsuri.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Întrebarea înaintea cifrei</div>
      <h2 class="exec-title frag" data-frag="3">INVESTIGAȚIE</h2>
      <p class="exec-phrase frag" data-frag="4">Nu calculăm tot ce se poate. Întrebăm întâi ce măsură răspunde.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Măsura definită</div>
      <h2 class="exec-title frag" data-frag="3">TRANSFORMARE</h2>
      <p class="exec-phrase frag" data-frag="4">O definim o dată. Cu o bază declarată și un reper.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Aceeași pe orice felie</div>
      <h2 class="exec-title frag" data-frag="3">VERIFICARE</h2>
      <p class="exec-phrase frag" data-frag="4">O măsură care se rupe la filtru nu e măsură. A noastră ține.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Definiție ancorată</div>
      <h2 class="exec-title frag" data-frag="3">STABILIZARE</h2>
      <p class="exec-phrase frag" data-frag="4">O măsură bună se definește o dată la sursă și rămâne.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">Măsuri controlabile</div>
      <h2 class="exec-title frag" data-frag="3">CONFIRMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Erau cifre brute. Acum sunt măsuri cu bază și reper, predate mai departe.</p>
    </div>
  </section>

  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        O măsură definită o dată.
        <span class="exec-closing-motto-yellow">Apoi clasamentul.</span>
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
    id: 1, name: "REALITATE", emotion: "Deschidere cantitativă",
    hook: "Ai un model care răspunde. Dar răspunsul vine ca o cifră brută.",
    next: "Astăzi o transformăm în măsură.",
    steps: [
      { num: "01", title: "Confirmăm că datele sunt legate corect.",
        instr: "Date_MASTER-C10.xlsx. Modelul vine de la C09: un fact și dimensiuni legate prin chei. <strong>O măsură peste un model rupt e o cifră falsă.</strong>",
        excel: true },
      { num: "02", title: "Formulăm întrebarea de business: cât?",
        instr: "Cât în total, cât în medie, cât pe o felie. <strong>Întrebarea decide măsura, nu invers.</strong>",
        excel: true },
      { num: "03", title: "Vedem că o cifră brută nu e încă o măsură.",
        instr: "Aduni o coloană în trei secunde. Dar fără bază, reper sau definiție stabilă, <strong>e o cifră de moment, nu o măsură.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "INVESTIGAȚIE", emotion: "Interogare asistată",
    hook: "Nu calculăm la întâmplare. Întrebăm întâi ce măsură răspunde.",
    next: "Copilot propune măsura. Apoi alegem.",
    steps: [
      { num: "04", title: "Cerem AI-ului ce măsură răspunde. Promptul 1.", instr: "", prompt: 1 },
      { num: "05", title: "Distingem cifra utilă de cifra decorativă.",
        instr: "Suma valorii răspunde la o întrebare. Suma numerelor de factură, la niciuna. <strong>Dacă nu răspunde la o decizie, rămâne decorativă.</strong>",
        excel: true },
      { num: "06", title: "Alegem măsura potrivită întrebării.",
        instr: "Aceeași felie susține măsuri diferite. <strong>Alegem una, conștient, și îi reținem baza de raportare.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "TRANSFORMARE", emotion: "Definirea măsurii",
    hook: "Cifra brută devine măsură: o definim o singură dată.",
    next: "Cu o bază declarată și un reper.",
    steps: [
      { num: "07", title: "Definim măsura o singură dată.",
        instr: "O scriem în foaia Masuri: ce agregăm, pe ce model. <strong>Aceasta devine sursa unică de adevăr.</strong>",
        excel: true },
      { num: "08", title: "Declarăm baza de raportare. Promptul 2.", instr: "", prompt: 2 },
      { num: "09", title: "Ancorăm măsura într-un reper.",
        instr: "O țintă sau un prag. Față de reper, măsura dă un semnal: peste sau sub. <strong>Reperul transformă cifra în sens.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "VERIFICARE", emotion: "Robustețea măsurii",
    hook: "O măsură de încredere dă același rezultat pe orice felie.",
    next: "Și un semnal clar față de reper.",
    steps: [
      { num: "10", title: "Verificăm că măsura e context-aware.",
        instr: "Aceeași definiție pe tot setul, pe o categorie, pe un client, pe o perioadă. <strong>Valorile diferă fiindcă felia diferă, nu fiindcă măsura e alta.</strong>",
        excel: true },
      { num: "11", title: "Verificăm baza și reperul.",
        instr: "Fiecare măsură își declară numitorul și are un reper. <strong>O cifră de care nu poți răspunde nu susține o decizie.</strong>",
        excel: true },
      { num: "12", title: "Confirmăm semnalul controlabil.",
        instr: "Știi ce măsură a aprins semnalul și față de ce reper. <strong>Un semnal pe care îl poți explica e un semnal controlabil.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "STABILIZARE", emotion: "Ancorare la sursă",
    hook: "O măsură bună nu se redefinește la fiecare felie sau sursă nouă.",
    next: "Se definește o dată și rămâne.",
    steps: [
      { num: "13", title: "Ancorăm definiția măsurii.",
        instr: "Trăiește într-un singur loc, peste model, nu copiată în zeci de celule. <strong>O sursă de adevăr, o singură definiție de întreținut.</strong>",
        excel: true },
      { num: "14", title: "Un rând nou se include singur în măsură.",
        instr: "Adăugăm o tranzacție nouă. Măsura se recalculează singură. <strong>Nu rescriem nimic. Definiția agregă peste model.</strong>",
        excel: true },
      { num: "15", title: "Aplicăm regula anti-derivă.",
        instr: "Vine exportul de luna viitoare: definiția, baza și reperul rămân valabile. <strong>Măsura nu derivează. E ancorată la o definiție, nu la o stare de moment.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "CONFIRMARE", emotion: "Predarea măsurilor",
    hook: "Măsurile sunt definite. Fiecare cu bază și reper.",
    next: "C11 compară măsurile deasupra.",
    steps: [
      { num: "16", title: "Facem prima citire a măsurii.",
        instr: "Cerem măsura definită și primim o valoare, baza ei și semnalul. <strong>Aceeași întrebare dă același răspuns, indiferent cine o pune.</strong>",
        excel: true },
      { num: "17", title: "Confirmăm setul de măsuri controlabile.",
        instr: "Fiecare măsură are întrebare, definiție unică, bază și reper. <strong>Nicio cifră orfană. Un set de măsuri controlabile.</strong>",
        excel: true },
      { num: "18", title: "Predăm măsurile către C11.",
        instr: "C10 definește măsuri. Atât. <strong>Care e mai mare, care contribuie, ce loc ocupă fiecare felie, începe la C11.</strong>",
        excel: false }
    ]
  }
];

'''

PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Identificarea măsurii",
    text: "Am un model cu un fact (Vanzari) legat de dimensiuni. Pentru întrebarea de business pe care o pun, spune-mi ce măsură răspunde corect (total, medie sau rată), ce coloană se agregă, care este baza de raportare (numitorul) și ce cifre din set nu merită transformate în măsuri. Nu modifica datele.",
    meta: "Copilot propune măsura. Nu o definește. O descrie."
  },
  2: {
    label: "Prompt 02 · Definirea măsurii",
    text: "Vreau să definesc măsura o singură dată, ca sursă unică de adevăr. Spune-mi definiția clară (ce agreg și pe ce bază), cum o ancorez într-un reper sau prag, ce semnal produce față de reper și cum mă asigur că aceeași definiție dă rezultat corect pe orice tăietură. Nu interpreta diferențele dintre felii; verific doar definiția, baza, reperul și robustețea.",
    meta: "Definiție, bază, reper, semnal."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # head: title + exec images placeholder
    head = head.replace('<title>C09 · RELAȚII · BROADCAST</title>',
                        '<title>C10 · MĂSURI · BROADCAST</title>')
    for n in range(1, 7):
        ph = exec_placeholder(n, EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("data:image/jpeg;base64,[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)

    # tail: inlocuiesc STAGES + PROMPTS + STORAGE_KEY
    i_st = tail.index('const STAGES = [')
    i_pr = tail.index('const PROMPTS = {')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + STAGES + PROMPTS + tail[i_fl:]
    tail = tail.replace('trainity_c09_video_v1', 'trainity_c10_video_v1')

    out = head + BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C09|trainity_c09|Date_MASTER-C09|RELAȚIILE DINTRE', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  exec base64 ramase:', out.count('data:image/jpeg;base64,'))
    print('  exec placeholder svg:', out.count('exec-stage-') )
    print('  leftover C09:', len(leftover), leftover[:5])


if __name__ == '__main__':
    main()
