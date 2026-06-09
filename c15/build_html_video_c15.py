#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c15.py - HTML-Video-Excel-15-Sintetizare.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c14 Video. Inlocuiesc:
  - BODY scaffolding (hero, exec slides, final, conclusion, topbar) -> C15 SINTETIZARE
  - const STAGES [...] + const PROMPTS {...} -> C15 (18 step-titles in 6 etape, 3x6)
  - STORAGE_KEY, <title>, exec placeholders, progres /18 -> C15
Garda C15: a formula mesajul esential (o propozitie). SINTEZA != REZUMAT. Zero calcul (T3),
zero rearanjare pagina (C14), zero livrare/decizie (C16). Cifrele in Excel (R-V02.15).
E5 = REFORMULARE (eticheta C15).
"""
import re

SRC = 'c14/HTML-Video-Excel-14-Compunere.html'
OUT = 'c15/HTML-Video-Excel-15-Sintetizare.html'

EXEC_TITLES = {1: 'MUTĂ', 2: 'REZUMATUL', 3: 'MESAJUL',
               4: 'TESTUL', 5: 'REFORMULAREA', 6: 'PREDAREA'}


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
        "opacity='0.6'>C15 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )


BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C15 · Sintetizare</div>
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
    <div class="hero-prelabel">Construcția 15 Excel</div>
    <h1 class="hero-title">MESAJUL<br>ESENȚIAL</h1>
    <p class="hero-hook frag" data-frag="1">O pagină impecabilă.<br><span class="hero-hook-twist">Și niciun mesaj.</span></p>
    <p class="hero-sub frag" data-frag="2">Avem o pagină coerentă. Acum extragem din ea o singură frază, mesajul pe care pagina îl dovedește.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am calculat nicio cifră nouă.</p>
      <p class="dim frag" data-frag="2">Nu am rearanjat pagina.</p>
      <p class="dim frag" data-frag="3">Nu am numit nicio decizie.</p>
      <p class="accent frag" data-frag="4">Aceeași pagină, acum spune o singură frază care contează.</p>
      <p class="frag" data-frag="5">O pagină arăta tot și nu spunea nimic. Acum are un mesaj, iar pagina îl dovedește.</p>
      <p class="frag" data-frag="6">Pagina cu mesaj e gata de predat pentru încadrarea deciziei.</p>
      <div class="final-motto frag" data-frag="7">Dintr-o privire,<br>mesajul.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 15</span>
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
      <div class="exec-emotion frag" data-frag="2">Pagina mută</div>
      <h2 class="exec-title frag" data-frag="3">MUTĂ</h2>
      <p class="exec-phrase frag" data-frag="4">O pagină coerentă, corectă, completă. O privești trei secunde și tot nu știi ce să reții.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Rezumatul automat</div>
      <h2 class="exec-title frag" data-frag="3">REZUMATUL</h2>
      <p class="exec-phrase frag" data-frag="4">AI scurtează pagina. Rezumatul scurtează tot; sinteza spune ce contează. Nu sunt același lucru.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Mesajul esențial</div>
      <h2 class="exec-title frag" data-frag="3">MESAJUL</h2>
      <p class="exec-phrase frag" data-frag="4">Alegi singura afirmație pe care pagina o dovedește și o formulezi într-o frază, pentru decizia de față.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Testul și ce-i cu asta?</div>
      <h2 class="exec-title frag" data-frag="3">TESTUL</h2>
      <p class="exec-phrase frag" data-frag="4">Fără această frază, decidentul hotărăște la fel? Indicativ, nu decizional. Nimic nou peste pagină.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Mesajul se adaptează</div>
      <h2 class="exec-title frag" data-frag="3">REFORMULAREA</h2>
      <p class="exec-phrase frag" data-frag="4">Datele s-au schimbat în amonte. Reformulezi headline-ul, refaci sinteza, nu recalculezi nimic.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">O pagină a devenit un mesaj</div>
      <h2 class="exec-title frag" data-frag="3">PREDAREA</h2>
      <p class="exec-phrase frag" data-frag="4">Headline-ul sus, pagina-dovadă dedesubt. Gata de predat pentru încadrarea deciziei la livrare.</p>
    </div>
  </section>

  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        Dintr-o privire,
        <span class="exec-closing-motto-yellow">mesajul.</span>
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
    id: 1, name: "MUTĂ", emotion: "Pagina mută",
    hook: "O pagină coerentă, corectă. O privești și tot nu știi ce să reții.",
    next: "Astăzi îi dăm o frază.",
    steps: [
      { num: "01", title: "Primești pagina coerentă de la compunere.",
        instr: "Date_MASTER-C15-Sintetizare.xlsx. Vine cu pagina compusă: focar, ierarhie, traseu. <strong>Totul e corect și totul se vede, dar o pagină coerentă nu e încă un mesaj.</strong>",
        excel: true },
      { num: "02", title: "Testul celor 3 secunde.",
        instr: "O privești trei secunde și te întrebi ce ai reține. <strong>De obicei, încă nimic precis: pagina arată, nu spune.</strong>",
        excel: true },
      { num: "03", title: "De ce o pagină corectă poate fi mută.",
        instr: "Corectitudinea și claritatea vizuală nu produc singure un mesaj. <strong>Mesajul e o afirmație în cuvinte, nu o sumă de obiecte corecte.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "REZUMATUL", emotion: "Rezumatul automat",
    hook: "Lași AI-ul să scurteze pagina.",
    next: "Apoi vezi diferența de sinteză.",
    steps: [
      { num: "04", title: "AI propune un rezumat draft.", instr: "", prompt: 1 },
      { num: "05", title: "Rezumat nu e sinteză.",
        instr: "Pui față în față cele două ieșiri. <strong>Rezumatul scurtează tot. Sinteza spune ce contează.</strong> Rezumatul micșorează proporțional; sinteza păstrează o singură afirmație.",
        excel: true },
      { num: "06", title: "De ce rezumatul nu e încă mesajul.",
        instr: "Un rezumat bun e tot o listă: corect, fără ierarhie de sens. <strong>Mesajul nu e ce conține pagina, e ce trebuie reținut din ea.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "MESAJUL", emotion: "Mesajul esențial",
    hook: "Alegi singura afirmație pe care pagina o dovedește.",
    next: "Și o formulezi într-o frază.",
    steps: [
      { num: "07", title: "Care e singura afirmație pe care pagina o dovedește?",
        instr: "Te uiți la focarul paginii și întrebi ce afirmație susține el. <strong>Mesajul nu se descoperă aici, vine gata din analiză; tu îl formulezi.</strong>",
        excel: true },
      { num: "08", title: "Formulezi headline-ul într-o singură frază.",
        instr: "Scrii headline-ul și o linie de susținere, plus legătura la zona din pagină care îl dovedește. <strong>O singură afirmație, nu trei.</strong>",
        excel: true },
      { num: "09", title: "Mesajul pentru această decizie și audiență.",
        instr: "Ajustezi fraza la cine decide și ce are de hotărât. <strong>Aceeași pagină poate avea mesaje diferite; sinteza alege mesajul potrivit, nu unul general.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "TESTUL", emotion: "Și ce-i cu asta?",
    hook: "Pui mesajul la trei probe.",
    next: "Contează, e indicativ, nu inventează.",
    steps: [
      { num: "10", title: "Filtrul fără asta, decidentul hotărăște la fel?", instr: "", prompt: 2 },
      { num: "11", title: "Indicativ, nu decizional.",
        instr: "Verifici că mesajul spune ce este, nu ce să faci. <strong>C15 enunță; nu numește decizia și nu recomandă, aceea e treaba livrării.</strong>",
        excel: true },
      { num: "12", title: "Formulat, nu descoperit.",
        instr: "Confirmi că nu ai adăugat nimic peste pagină. <strong>Nicio cifră nouă, nicio cauză nouă; acelea vin din analiză.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "REFORMULAREA", emotion: "Mesajul se adaptează",
    hook: "Pagina se schimbă, mesajul se reface.",
    next: "În cuvinte, nu în cifre.",
    steps: [
      { num: "13", title: "Pagina se schimbă, mesajul vechi nu mai e exact.",
        instr: "Datele s-au actualizat în amonte, în model; cifrele s-au schimbat acolo. <strong>Headline-ul scris ieri poate să nu mai fie adevărat azi.</strong>",
        excel: true },
      { num: "14", title: "Reformulezi headline-ul, nu recalculezi.",
        instr: "Rescrii fraza ca să spună ce contează acum. <strong>Nu atingi nicio cifră; reformularea e un act în cuvinte, nu un recalcul.</strong>",
        excel: true },
      { num: "15", title: "Noul mesaj rămâne o singură afirmație susținută.",
        instr: "Treci mesajul nou prin același criteriu. <strong>O singură afirmație, susținută de pagină, pe criteriul ce contează.</strong>",
        excel: true }
    ]
  },
  {
    id: 6, name: "PREDAREA", emotion: "O pagină a devenit un mesaj",
    hook: "Pagina spune acum o frază, dovedită de tot ce e sub ea.",
    next: "Și o predăm pentru livrare.",
    steps: [
      { num: "16", title: "O pagină coerentă a devenit un mesaj care contează.",
        instr: "Pui mesajul în capul paginii, ca headline. <strong>Aceeași pagină care doar arăta, acum spune o frază; restul devine dovada.</strong>",
        excel: true },
      { num: "17", title: "Mesajul și pagina-dovadă, împreună.",
        instr: "Verifici că fraza și dovada stau lipite. <strong>Un mesaj fără pagină e o părere; o pagină fără mesaj e mută. Împreună sunt un raport care spune.</strong>",
        excel: true },
      { num: "18", title: "Predare către livrare.",
        instr: "Predai pagina cu mesaj treptei de livrare. <strong>C15 spune ce contează; încadrarea pentru decizie vine la treapta următoare.</strong>",
        excel: false }
    ]
  }
];

'''

PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Titluri candidate (draft)",
    text: "Pe baza acestui raport, propune-mi 3 titluri candidate, fiecare de o singură frază, care spun ce contează pentru decizia și audiența pe care ți le dau. Nu calcula cifre noi și nu explica de ce, formulează doar din ce e deja în raport. Lasă-mă pe mine să aleg și să ascut titlul; tu dă-mi variante de pornire.",
    meta: "AI draftuiește. Noi alegem mesajul."
  },
  2: {
    label: "Prompt 02 · Testul mesajului",
    text: "Pentru titlul ales, verifică: este o singură afirmație? este indicativ, adică spune ce e, nu ce să fac? nu introduce o cifră sau o cauză care nu e deja în raport? trece testul fără asta, decidentul hotărăște la fel? Spune-mi unde cade și de ce; decizia finală asupra formei o iau eu.",
    meta: "AI critică. Noi decidem forma."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = head.replace('<title>C14 · COMPOZIȚIE · BROADCAST</title>',
                        '<title>C15 · SINTEZĂ · BROADCAST</title>')
    # exec placeholders C14 -> C15
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
    tail = tail.replace('trainity_c14_video_v1', 'trainity_c15_video_v1')

    out = head + BODY + tail
    import os
    os.makedirs('c15', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C14|trainity_c14|Date_MASTER-C14|COMPUNERE|Compun\b', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  exec base64 jpeg ramase:', out.count('data:image/jpeg;base64,'))
    print('  leftover C14:', len(leftover), leftover[:6])
    print('  STAGES steps:', out.count('num: "'))
    for ch in ['—', '–']:
        if ch in BODY + STAGES + PROMPTS:
            print('  ATENTIE em/en-dash in continut C15!')


if __name__ == '__main__':
    main()
