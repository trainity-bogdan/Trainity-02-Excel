#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c16.py - HTML-Video-Excel-16-Livrare.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c14 Video. Inlocuiesc:
  - BODY scaffolding (hero, exec slides, final, conclusion, topbar) -> C16 LIVRARE
  - const STAGES [...] + const PROMPTS {...} -> C16 (18 step-titles din SPEC narativ)
  - STORAGE_KEY, <title>, exec placeholders -> C16
Garda C16: a livra raportul ca obiect de decizie. ZERO sinteza mesaj (C15),
ZERO layout/pagina (C14), ZERO sistem recurent (C17), ZERO logistica.
Cifrele in Excel (R-V02.15). exec-stage = placeholdere (C16 nu are assets reale).
"""
import re

SRC = 'c14/HTML-Video-Excel-14-Compunere.html'
OUT = 'c16/HTML-Video-Excel-16-Livrare.html'

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
        "opacity='0.6'>C16 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )


BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C16 · Livrare</div>
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
    <div class="hero-prelabel">Construcția 16 Excel</div>
    <h1 class="hero-title">DECIZIA<br>GATA</h1>
    <p class="hero-hook frag" data-frag="1">Raportul e gata.<br><span class="hero-hook-twist">Decizia, nu.</span></p>
    <p class="hero-sub frag" data-frag="2">Analiza a dat răspunsul, sinteza a dat mesajul. Acum îi dăm forma care îl face o decizie gata de luat, nu doar informație trimisă.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am sintetizat niciun mesaj.</p>
      <p class="dim frag" data-frag="2">Nu am compus nicio pagină.</p>
      <p class="dim frag" data-frag="3">Nu am sistematizat niciun raport recurent.</p>
      <p class="accent frag" data-frag="4">Un mesaj corect, acum cu o formă din care decidentul poate hotărî.</p>
      <p class="frag" data-frag="5">Același raport: trimis, stătea pe loc; livrat ca decizie, se hotărăște dintr-o citire.</p>
      <p class="frag" data-frag="6">Raportul-decizie e gata de sistematizat la treapta de autonomie.</p>
      <div class="final-motto frag" data-frag="7">Nu livrez informație.<br>Livrez o decizie gata de luat.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 16</span>
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
      <div class="exec-emotion frag" data-frag="2">Raportul care nu mișcă</div>
      <h2 class="exec-title frag" data-frag="3">REALITATE</h2>
      <p class="exec-phrase frag" data-frag="4">Te uiți la un raport complet. Și la o întrebare fără răspuns: de ce nu se decide din el?</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Ce cere decizia</div>
      <h2 class="exec-title frag" data-frag="3">INVESTIGAȚIE</h2>
      <p class="exec-phrase frag" data-frag="4">Nu tot raportul susține decizia. O parte e semnal, restul e zgomot care aglomerează.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Forma de decizie</div>
      <h2 class="exec-title frag" data-frag="3">TRANSFORMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Concluzia urcă în cap, cadrul decizie, risc, concluzie, pas se scrie, detaliul coboară în anexă.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Foaia se susține singură</div>
      <h2 class="exec-title frag" data-frag="3">VERIFICARE</h2>
      <p class="exec-phrase frag" data-frag="4">Decidentul hotărăște doar din foaie. Dacă te cheamă pentru context de bază, încă e informație.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Regula, nu inspirația</div>
      <h2 class="exec-title frag" data-frag="3">STABILIZARE</h2>
      <p class="exec-phrase frag" data-frag="4">Cele șase reguli fac orice raport următor decision-ready, complet și fără surplus.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">Decizia predată</div>
      <h2 class="exec-title frag" data-frag="3">CONFIRMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Forma de decizie scurtează drumul spre hotărâre. Predai o decizie, nu un teanc de date.</p>
    </div>
  </section>

  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        Raportul
        <span class="exec-closing-motto-yellow">care decide.</span>
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
'''

STAGES = r'''const STAGES = [
  {
    id: 1, name: "REALITATE", emotion: "Raportul care nu mișcă",
    hook: "Mesajul e sintetizat, raportul e complet. Și totuși decidentul nu hotărăște.",
    next: "Pentru că lipsește forma de decizie.",
    steps: [
      { num: "01", title: "Mesajul sintetizat, dar încă nu o decizie.",
        instr: "Deschizi raportul cu mesajul esențial și rezultatul corect. <strong>E adevărat, e clar, dar e încă informație: nu spune ce se decide.</strong>",
        excel: true },
      { num: "02", title: "Raportul plin, iar decidentul tot întreabă.",
        instr: "Pui raportul complet în fața cuiva care trebuie să hotărască. Tot întreabă: și ce fac cu asta? <strong>Lipsa nu e de informație, e de formă de decizie.</strong>",
        excel: true },
      { num: "03", title: "Aceeași informație, încă fără cadru de decizie.",
        instr: "Iei mesajul și rezultatul. <strong>Nu le re-sintetizezi: mesajul vine gata, tu îi dai forma de decizie.</strong>",
        excel: false }
    ]
  },
  {
    id: 2, name: "INVESTIGAȚIE", emotion: "Ce cere decizia",
    hook: "Înainte să construiești foaia, descoperi ce-i trebuie decidentului ca să hotărască.",
    next: "Și ce din raport e doar zgomot.",
    steps: [
      { num: "04", title: "Ce decizie se cere, de fapt, din acest raport.",
        instr: "Nu ce conține raportul, ci ce hotărâre se ia din el. <strong>Decizia cerută nu e dată de cifre, e numită de tine.</strong>",
        excel: true },
      { num: "05", title: "Ce-i trebuie decidentului ca să decidă. Promptul 1.", instr: "", prompt: 1 },
      { num: "06", title: "Ce e semnal pentru decizie, ce e zgomot.",
        instr: "Ce susține hotărârea rămâne sus, ce e doar context coboară. <strong>Aceleași date, dar o parte e semnal, restul aglomerează.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "TRANSFORMARE", emotion: "Forma de decizie",
    hook: "Aici raportul capătă forma de decizie: concluzia urcă, cadrul se scrie.",
    next: "Și detaliul coboară în anexă.",
    steps: [
      { num: "07", title: "Concluzia urcă în capul foii.",
        instr: "Pui concluzia cerută în prima linie, ca decizie de luat. <strong>Nu o re-formulezi, o poziționezi.</strong>",
        excel: true },
      { num: "08", title: "Construiești cadrul de decizie. Promptul 2.", instr: "", prompt: 2 },
      { num: "09", title: "Detaliul exhaustiv coboară în anexă.",
        instr: "Muți detaliul brut jos; sus rămâne agregatul care susține decizia. <strong>Ce nu intră în decizie nu dispare, dar nu mai aglomerează.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "VERIFICARE", emotion: "Foaia se susține singură",
    hook: "O foaie decision-ready se decide fără autorul lângă ea.",
    next: "Și rezistă fără tine.",
    steps: [
      { num: "10", title: "Poate decidentul hotărî doar din foaie?",
        instr: "Pui foaia în fața decidentului și pleci. <strong>Dacă te cheamă pentru context de bază, încă e informație, nu decizie.</strong>",
        excel: true },
      { num: "11", title: "Testul fără autor: întrebările inevitabile, nu cele de bază.",
        instr: "Întrebările de bază sunt vina formei și se elimină. <strong>Rămân doar întrebările inevitabile de decizie, despre compromisuri.</strong>",
        excel: true },
      { num: "12", title: "Riscul și pasul următor, scrise explicit, nu deduse.",
        instr: "Riscul cu pragul lui, pasul următor ca acțiune. <strong>Decidentul nu reconstruiește raționamentul, citește decizia.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "STABILIZARE", emotion: "Regula, nu inspirația",
    hook: "Onestitatea livrării nu e noroc. O fixezi în reguli.",
    next: "Ca orice raport următor să fie decision-ready.",
    steps: [
      { num: "13", title: "Cele șase reguli ale foii-raport de decizie.",
        instr: "Concluzia în cap, cadrul de decizie, anexa, riscul scris, pasul următor, fiecare cifră cu referință. <strong>Cele șase reguli sunt felul în care construiești.</strong>",
        excel: true },
      { num: "14", title: "Complet pentru decizie, fără surplus.",
        instr: "Tai din cap tot ce nu intră în decizie. <strong>Complet nu înseamnă tot ce ai, înseamnă cât îi trebuie decidentului.</strong>",
        excel: true },
      { num: "15", title: "O foaie-raport de decizie care stă în picioare singură.",
        instr: "Vine alt raport din aceeași natură: aceleași reguli, aceeași formă de decizie. <strong>Repetabil, nu o reușită de moment.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "CONFIRMARE", emotion: "Decizia predată",
    hook: "Forma de decizie scurtează drumul spre hotărâre.",
    next: "Și predai decizia mai departe.",
    steps: [
      { num: "16", title: "Forma de decizie scurtează drumul spre hotărâre.",
        instr: "Hotărârea care lua o ședință se ia dintr-o citire. <strong>Aceeași informație, dar forma de decizie a scurtat drumul.</strong>",
        excel: true },
      { num: "17", title: "Devii cel care predă o decizie, nu un teanc de date.",
        instr: "Nu am trimis raportul, ci am livrat o decizie. <strong>Ești ultimul filtru între un mesaj corect și un decident care trebuie să acționeze.</strong>",
        excel: true },
      { num: "18", title: "Predai către treapta de autonomie: raportul-decizie gata.",
        instr: "Predai o foaie-raport de decizie completă, self-standing. <strong>C16 face raportul o decizie. Treapta de autonomie îl face să ruleze singur.</strong>",
        excel: false }
    ]
  }
];

'''

PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Ce-i trebuie decidentului ca să decidă",
    text: "Am un raport cu un mesaj esențial deja sintetizat și un rezultat corect. Pentru un decident concret, spune-mi ce decizie se cere de fapt din acest raport, ce risc o însoțește și ce informație e relevantă pentru decizie față de ce e zgomot. Propune o listă, dar nu hotărî tu; eu judec ce intră în decizie. Nu re-sintetiza mesajul și nu căuta concluzii noi; lucrează doar cu încadrarea pentru decizie. Nu compune pagina și nu propune un raport recurent.",
    meta: "Copilot propune. Tu judeci ce intră în decizie."
  },
  2: {
    label: "Prompt 02 · Construiești cadrul de decizie",
    text: "Construiește o foaie-raport de decizie pornind de la mesajul și agregatul date. Pune în capul foii cadrul de decizie: decizia de luat, riscul cu pragul lui, concluzia și pasul următor. Coboară detaliul brut în anexă. Apoi verifică: fiecare cifră are unitate, perioadă și referință, iar foaia se citește fără autor lângă ea. Nu aranja vizual pagina și nu adăuga un dashboard; nu automatiza un flux recurent.",
    meta: "O singură foaie-raport de decizie, self-standing."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = re.sub(r'<title>C\d+[^<]*</title>', '<title>C16 · LIVRARE · BROADCAST</title>', head, count=1)
    # exec placeholders C14 -> C16 placeholder SVG
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
    tail = re.sub(r'trainity_c\d+_video_v1', 'trainity_c16_video_v1', tail)

    out = head + BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C14|trainity_c14|Date_MASTER-C14|Compunere|COMPUNERE|ordinea privirii', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  exec base64 jpeg ramase (trebuie 0, placeholdere):', out.count('data:image/jpeg;base64,'))
    print('  leftover C14:', len(leftover), leftover[:6])
    print('  STAGES steps:', out.count('num: "'))


if __name__ == '__main__':
    main()
