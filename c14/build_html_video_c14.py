#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c14.py - HTML-Video-Excel-14-Compunere.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c13 Video. Inlocuiesc:
  - BODY scaffolding (hero, exec slides, final, conclusion, topbar) -> C14 COMPUNERE
  - const STAGES [...] + const PROMPTS {...} -> C14 (11 step-titles in 6 etape 2+2+2+2+2+1)
  - STORAGE_KEY, <title>, exec placeholders -> C14
Garda C14: a asaza spatial. Pagina cu focar/ierarhie, ZERO obiect singular (C13),
zero mesaj (C15), zero livrare (C16). Cifrele in Excel (R-V02.15).
"""
import re

SRC = 'c13/HTML-Video-Excel-13-Vizualizare.html'
OUT = 'c14/HTML-Video-Excel-14-Compunere.html'

EXEC_TITLES = {1: 'ZIDUL', 2: 'POZITIA', 3: 'TRASEUL',
               4: 'IERARHIA', 5: 'SPATIUL', 6: 'PROBA'}


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
        "opacity='0.6'>C14 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )


BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C14 · Compunere</div>
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
    <div class="hero-prelabel">Construcția 14 Excel</div>
    <h1 class="hero-title">ORDINEA<br>PRIVIRII</h1>
    <p class="hero-hook frag" data-frag="1">Graficele sunt corecte.<br><span class="hero-hook-twist">Pagina te încurcă.</span></p>
    <p class="hero-sub frag" data-frag="2">Avem obiecte vizuale oneste. Acum le așezăm pe pagină astfel încât ochiul să prindă întâi ce contează pentru decizie.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am desenat niciun grafic.</p>
      <p class="dim frag" data-frag="2">Nu am formulat niciun mesaj.</p>
      <p class="dim frag" data-frag="3">Nu am livrat niciun raport.</p>
      <p class="accent frag" data-frag="4">Aceleași obiecte, acum așezate ca ochiul să prindă întâi ce contează.</p>
      <p class="frag" data-frag="5">Aceleași grafice, aceleași cifre, altă ordine, altă decizie.</p>
      <p class="frag" data-frag="6">Pagina coerentă e gata de predat pentru extragerea mesajului.</p>
      <div class="final-motto frag" data-frag="7">Ce vede ochiul întâi<br>schimbă decizia.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 14</span>
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
      <div class="exec-emotion frag" data-frag="2">Pagina fără ordine</div>
      <h2 class="exec-title frag" data-frag="3">ZIDUL</h2>
      <p class="exec-phrase frag" data-frag="4">Ai obiecte corecte și o pagină fără un întâi. Ochiul aterizează la întâmplare și rătăcește.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Poziția e importanță</div>
      <h2 class="exec-title frag" data-frag="3">POZIȚIA</h2>
      <p class="exec-phrase frag" data-frag="4">Unde așezi un obiect spune cât contează. Poziția nu e neutră, e un argument despre importanță.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Ordinea de citire</div>
      <h2 class="exec-title frag" data-frag="3">TRASEUL</h2>
      <p class="exec-phrase frag" data-frag="4">Un focar atins primul, apoi un traseu: ce vede ochiul după și ce coboară din prim-plan.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Greutate inegală</div>
      <h2 class="exec-title frag" data-frag="3">IERARHIA</h2>
      <p class="exec-phrase frag" data-frag="4">Mărime, poziție, contrast, spațiu: importanța se vede instant, nu se caută.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Compoziția guvernată</div>
      <h2 class="exec-title frag" data-frag="3">SPAȚIUL</h2>
      <p class="exec-phrase frag" data-frag="4">Spațiul gol izolează focarul. Toată pagina se aliniază la răspunsul venit din analiză.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">Al doilea ochi</div>
      <h2 class="exec-title frag" data-frag="3">PROBA</h2>
      <p class="exec-phrase frag" data-frag="4">Un cititor de trei secunde prinde aceeași prioritate. Pagina e gata de predat pentru mesaj.</p>
    </div>
  </section>

  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        Ce vede ochiul întâi
        <span class="exec-closing-motto-yellow">schimbă decizia.</span>
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
    <div class="progress-big" id="progress-num">00<span class="total">/11</span></div>
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
    id: 1, name: "ZIDUL", emotion: "Pagina fără ordine",
    hook: "Obiecte corecte, o pagină fără un întâi. Ochiul rătăcește.",
    next: "Astăzi îi dăm o ordine.",
    steps: [
      { num: "01", title: "Pagina fără întâi.",
        instr: "Date_MASTER-C14-Compunere.xlsx. Obiectele vizuale oneste vin în ordinea producției. <strong>Toate la fel, niciun focar: ochiul nu știe unde să înceapă.</strong>",
        excel: true },
      { num: "02", title: "Primul punct de contact al ochiului.",
        instr: "Privirea cade undeva întâi: sus-stânga, cel mai mare, cel mai contrastant. <strong>Pagina are deja un traseu, doar că nu l-am ales noi.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "POZIȚIA", emotion: "Poziția e importanță",
    hook: "Unde așezi un obiect spune cât contează.",
    next: "Copilot propune ierarhia. Noi judecăm.",
    steps: [
      { num: "03", title: "Poziția ca semnal de importanță.",
        instr: "Sus, mare sau central spune important; jos, mic sau în margine spune secundar. <strong>Poziția nu e neutră, e un argument.</strong>",
        excel: true },
      { num: "04", title: "Ierarhia și ordinea de citire. Promptul 1.", instr: "", prompt: 1 }
    ]
  },
  {
    id: 3, name: "TRASEUL", emotion: "Ordinea de citire",
    hook: "Un focar atins primul, apoi un traseu deliberat.",
    next: "Și coborâm ce nu mută decizia.",
    steps: [
      { num: "05", title: "Focarul vizual.",
        instr: "Focarul e obiectul care poartă răspunsul venit din analiză, plasat unde cade ochiul primul. <strong>O pagină are un singur focar, nu cinci.</strong>",
        excel: true },
      { num: "06", title: "Traseul de citire.",
        instr: "După focar, ordonăm ce vede ochiul al doilea și al treilea, apoi retrogradăm ce nu mută decizia. <strong>Coboară din prim-plan, fără să-l ștergem.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "IERARHIA", emotion: "Greutate inegală",
    hook: "Importanța se vede instant, nu se caută.",
    next: "Și grupăm ce ține împreună.",
    steps: [
      { num: "07", title: "Ierarhia vizuală pentru decizie.",
        instr: "Două sau trei niveluri: focar peste suport peste detaliu, prin mărime, poziție, contrast, spațiu. <strong>Greutate inegală pentru lucruri inegale.</strong>",
        excel: true },
      { num: "08", title: "Gruparea elementelor legate.",
        instr: "Punem împreună ce ține de aceeași întrebare, separăm ce nu e legat. <strong>Proximitatea spune adevărul despre relații: lângă înseamnă împreună.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "SPAȚIUL", emotion: "Compoziția guvernată",
    hook: "Spațiul gol e instrument, nu lipsă.",
    next: "Și aliniem totul la răspuns.",
    steps: [
      { num: "09", title: "Spațiul gol ca instrument de ierarhie.",
        instr: "Lăsăm gol în jurul focarului și între grupuri. <strong>Spațiul gol izolează ce contează; reflexul de a-l umple strică ierarhia.</strong>",
        excel: true },
      { num: "10", title: "Compunerea guvernată de răspuns. Promptul 2.", instr: "", prompt: 2 }
    ]
  },
  {
    id: 6, name: "PROBA", emotion: "Al doilea ochi",
    hook: "O pagină compusă trece proba unui ochi proaspăt.",
    next: "Și o predăm pentru mesaj.",
    steps: [
      { num: "11", title: "Testul celui de-al doilea ochi.",
        instr: "Dăm pagina cuiva trei secunde, fără noi lângă el. <strong>Dacă focarul și ordinea citită coincid cu intenția, pagina trece și e gata de predat pentru mesaj.</strong>",
        excel: false }
    ]
  }
];

'''

PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Ierarhia și ordinea de citire",
    text: "Am mai multe obiecte vizuale deja produse și verificate, plus răspunsul venit din analiză pe care pagina trebuie să-l facă vizibil. Propune-mi ce ar trebui să vadă ochiul întâi, ce după și ce să retrogradez, ca decidentul să prindă dintr-o privire ce contează. Nu redesena obiectele și nu schimba tipul lor, nu formula mesajul în cuvinte și nu pregăti livrarea. Lucrează doar cu ordinea și ierarhia spațială.",
    meta: "Copilot propune ordinea. Noi judecăm."
  },
  2: {
    label: "Prompt 02 · Varianta de compoziție",
    text: "Pe baza ierarhiei stabilite și a răspunsului venit din analiză, propune-mi o variantă de așezare a obiectelor pe pagina de raport: poziționare, grupare, spațiu gol și focar, astfel încât ochiul să prindă întâi ce contează pentru decizie. Nu schimba tipul graficelor și nu inventa date, nu scrie concluzia în cuvinte și nu pregăti pachetul de livrare. Dă-mi doar compoziția spațială, pe care o corectez după criteriul se vede întâi ce decide.",
    meta: "O singură pagină, ochiul prinde decizia."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = head.replace('<title>C13 · VIZUAL · BROADCAST</title>',
                        '<title>C14 · COMPOZIȚIE · BROADCAST</title>')
    # exec placeholders C13 -> C14 (sursa c13 are deja SVG placeholder)
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
    tail = tail.replace('trainity_c13_video_v1', 'trainity_c14_video_v1')

    out = head + BODY + tail
    import os
    os.makedirs('c14', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C13|trainity_c13|Date_MASTER-C13|VIZUALIZARE|de ce-ul', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  exec base64 jpeg ramase:', out.count('data:image/jpeg;base64,'))
    print('  leftover C13:', len(leftover), leftover[:6])
    print('  STAGES steps:', out.count('num: "'))


if __name__ == '__main__':
    main()
