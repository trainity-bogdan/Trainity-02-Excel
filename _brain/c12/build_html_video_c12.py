#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c12.py - HTML-Video-Excel-12-Interpretare.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c09 Video. Inlocuiesc:
  - BODY scaffolding (hero, final, conclusion, 7 exec slides, topbar) -> C12 INTERPRETARE
  - const STAGES [...] + const PROMPTS {...} (continutul pasilor) -> C12
  - STORAGE_KEY, <title>
  - 6 imagini exec base64 din head CSS -> placeholder SVG (dependenta ARHITECT)

Garda C12: a explica (De ce?). Clasamentul = INPUT citit (C11), zero dashboard (T4),
zero what-if/scenariu/predictie/recomandare (T5), zero re-ierarhizare. Inchide T3.
"""
import re

SRC = 'c09/HTML-Video-Excel-09-Relatii.html'
OUT = 'c12/HTML-Video-Excel-12-Interpretare.html'


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
        "opacity='0.6'>C12 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )
    return svg


EXEC_TITLES = {1: 'REALITATE', 2: 'INVESTIGATIE', 3: 'TRANSFORMARE',
               4: 'VERIFICARE', 5: 'STABILIZARE', 6: 'CONFIRMARE'}

BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C12 · Interpretare</div>
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
    <div class="hero-prelabel">Construcția 12 Excel</div>
    <h1 class="hero-title">DE CE-UL<br>DIN DATE</h1>
    <p class="hero-hook frag" data-frag="1">Știi care a crescut.<br><span class="hero-hook-twist">Nu știi de ce.</span></p>
    <p class="hero-sub frag" data-frag="2">Înainte de a raporta ceva, explicăm: de ce arată rezultatul așa, citit din model, nu ghicit.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am reordonat nimic.</p>
      <p class="dim frag" data-frag="2">Nu am desenat niciun tablou.</p>
      <p class="dim frag" data-frag="3">Nu am propus nicio acțiune.</p>
      <p class="accent frag" data-frag="4">Un clasament care arăta doar CARE. Acum și DE CE, citit din model.</p>
      <p class="frag" data-frag="5">Întrebi de ce. Modelul explică.</p>
      <p class="frag" data-frag="6">Analiza setului e completă: treapta T3 finalizată.</p>
      <div class="final-motto frag" data-frag="7">Nu citi rezultatul.<br>Explică-l.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 12</span>
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
      <div class="exec-emotion frag" data-frag="2">Rezultat fără cauză</div>
      <h2 class="exec-title frag" data-frag="3">REALITATE</h2>
      <p class="exec-phrase frag" data-frag="4">Te uiți la un clasament corect. Și la o întrebare fără răspuns: de ce?</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Cauza, citită nu ghicită</div>
      <h2 class="exec-title frag" data-frag="3">INVESTIGAȚIE</h2>
      <p class="exec-phrase frag" data-frag="4">Nu ghicim de ce. Citim cauza din model și separăm coincidența de cauză.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Rezultatul devine explicație</div>
      <h2 class="exec-title frag" data-frag="3">TRANSFORMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Coborâm sub total, găsim cauza și o scriem ca frază verificabilă.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Explicația rezistă</div>
      <h2 class="exec-title frag" data-frag="3">VERIFICARE</h2>
      <p class="exec-phrase frag" data-frag="4">O explicație pe care nu o poți arăta în date nu trece. A noastră se arată.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Explicație ancorată</div>
      <h2 class="exec-title frag" data-frag="3">STABILIZARE</h2>
      <p class="exec-phrase frag" data-frag="4">Cauza reală rămâne și pe datele de luna viitoare. Nu se agață de o poveste.</p>
    </div>
  </section>

  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-overlay"></div><div class="exec-accent-bar"></div><div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">Analiză închisă</div>
      <h2 class="exec-title frag" data-frag="3">CONFIRMARE</h2>
      <p class="exec-phrase frag" data-frag="4">Erau cifre. Acum sunt explicate, citit din model. Treapta T3 e finalizată.</p>
    </div>
  </section>

  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        Nu citi rezultatul.
        <span class="exec-closing-motto-yellow">Explică-l.</span>
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
    id: 1, name: "REALITATE", emotion: "Deschidere interpretativă",
    hook: "Ai un clasament corect. Arată CARE conduce, nu DE CE.",
    next: "Astăzi îl transformăm în explicație.",
    steps: [
      { num: "01", title: "Confirmăm că avem model, măsuri și clasament.",
        instr: "Date_MASTER-C12.xlsx. Vine cu modelul, măsurile și clasamentul predate de treaptă. <strong>O explicație peste un clasament greșit lămurește un lucru care nu există.</strong>",
        excel: true },
      { num: "02", title: "Formulăm întrebarea de business: de ce?",
        instr: "De ce conduce acela, de ce a apărut diferența. <strong>Întrebarea decide ce cauză cauți, nu invers.</strong>",
        excel: true },
      { num: "03", title: "Vedem că un clasament arată CARE, nu DE CE.",
        instr: "Clasamentul spune cine conduce și cu cât. Atât. <strong>O constatare numerică nu e încă o explicație: lipsește cauza.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "INVESTIGAȚIE", emotion: "Citire asistată",
    hook: "Nu ghicim de ce. Întrebăm modelul ce cauze susțin datele.",
    next: "Copilot citește cauza. Apoi o cernem.",
    steps: [
      { num: "04", title: "Citim cauza din model, nu din presupunere. Promptul 1.", instr: "", prompt: 1 },
      { num: "05", title: "Separăm ce apare împreună de ce produce rezultatul.",
        instr: "Două lucruri care cresc împreună par legate, dar coincidența nu e cauză. <strong>Dacă elimini factorul și rezultatul rămâne, nu era cauza.</strong>",
        excel: true },
      { num: "06", title: "Identificăm factorii principali, nu o cauză unică.",
        instr: "Un rezultat de business rar are o singură cauză. <strong>Reținem factorii principali și ordinea lor, fără să forțăm o explicație unică.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "TRANSFORMARE", emotion: "De la rezultat la explicație",
    hook: "Rezultatul numeric devine explicație: coborâm sub total.",
    next: "Și scriem insight-ul ca frază verificabilă.",
    steps: [
      { num: "07", title: "Coborâm sub total ca să găsim cauza ascunsă. Promptul 2.", instr: "", prompt: 2 },
      { num: "08", title: "Scriem insight-ul într-o frază verificabilă.",
        instr: "Ce rezultat, din ce cauză, vizibilă pe ce felie. <strong>O frază pe care un decident o înțelege și o poți arăta înapoi în model.</strong>",
        excel: true },
      { num: "09", title: "Ancorăm explicația în model.",
        instr: "Fiecare frază trimite la felia, măsura sau comparația care o susține. <strong>Cauza trăiește în model, nu în intuiție.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "VERIFICARE", emotion: "Explicația rezistă",
    hook: "O explicație de încredere se arată înapoi în date.",
    next: "Și rezistă întrebării: de unde știi?",
    steps: [
      { num: "10", title: "Verificăm că explicația se arată înapoi în model.",
        instr: "Pentru fiecare insight, arătăm felia care îl susține. <strong>Un de ce pe care nu îl poți dovedi rămâne o presupunere.</strong>",
        excel: true },
      { num: "11", title: "Respingem narativul pe care datele nu îl susțin.",
        instr: "O poveste poate fi plauzibilă și falsă. <strong>Cele pe care datele nu le confirmă se resping, oricât de bine sună.</strong>",
        excel: true },
      { num: "12", title: "Confirmăm că nu am forțat o cauză unică.",
        instr: "Numește un singur vinovat unde lucrează mai mulți factori? <strong>O explicație onestă arată factorii principali și greutatea lor.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "STABILIZARE", emotion: "Explicație ancorată",
    hook: "O explicație bună nu se schimbă la fiecare recitire.",
    next: "E ancorată în model și rezistă datelor noi.",
    steps: [
      { num: "13", title: "Ancorăm explicația la model, nu la o stare de moment.",
        instr: "Insight-ul trăiește lângă felia care îl susține. <strong>Când cineva întreabă de unde știi, trimiți la aceeași felie.</strong>",
        excel: true },
      { num: "14", title: "Un rând nou nu schimbă cauza dacă explicația e reală.",
        instr: "Adăugăm date noi. <strong>Dacă o singură tranzacție răstoarnă explicația, n-a fost cauză, a fost coincidență.</strong>",
        excel: true },
      { num: "15", title: "Aplicăm regula anti-poveste.",
        instr: "Vine exportul de luna viitoare: cauza citită din model se confirmă sau se ajustează cinstit. <strong>Explicația nu se agață de o concluzie comodă.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "CONFIRMARE", emotion: "Închiderea analizei",
    hook: "Întrebi de ce. Modelul explică. Apoi închizi analiza.",
    next: "Treapta de raportare poate începe.",
    steps: [
      { num: "16", title: "Facem prima citire a insight-ului.",
        instr: "Rezultatul, cauza și felia care o susține. <strong>Aceeași întrebare de ce dă aceeași explicație, indiferent cine o spune.</strong>",
        excel: true },
      { num: "17", title: "Confirmăm setul de explicații ancorate.",
        instr: "Fiecare insight are întrebare, cauză citită din model și o felie care îl dovedește. <strong>Niciunul nu e o poveste orfană.</strong>",
        excel: true },
      { num: "18", title: "Închidem analiza: treapta T3 finalizată.",
        instr: "Setul a fost legat, măsurat, comparat și acum interpretat. <strong>Cum se vede dintr-o privire începe la treapta următoare.</strong>",
        excel: false }
    ]
  }
];

'''

PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Citirea cauzei din model",
    text: "Am un model cu un clasament și măsuri definite. Pentru rezultatul pe care îl indic, citește din date și spune-mi: ce cauze posibile susține modelul (ce felie, client, produs sau perioadă pare să tragă rezultatul), care dintre ele apar doar împreună fără să fie cauză, și pe ce tăietură ar trebui să cobor ca să văd cauza ascunsă de total. Rămâi la ce s-a întâmplat și de ce; nu trece la ce ar urma sau la pași de făcut. Nu modifica datele.",
    meta: "Copilot citește cauza. Nu o ghicește."
  },
  2: {
    label: "Prompt 02 · De la rezultat la explicație verificabilă",
    text: "Vreau să transform rezultatul în explicație. Pe baza cauzelor citite din model, spune-mi pe ce tăietură cobor ca să văd cauza ascunsă de total, cum verific că factorul chiar produce rezultatul (nu doar apare cu el) și formulează o frază de insight care numește factorii principali și poate fi arătată înapoi în date. Distinge explicația de clasament: ordinea e deja dată, eu caut cauza.",
    meta: "Cauză citită, factori principali, verificabil."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = head.replace('<title>C09 · RELAȚII · BROADCAST</title>',
                        '<title>C12 · INTERPRETARE · BROADCAST</title>')
    for n in range(1, 7):
        ph = exec_placeholder(n, EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("data:image/jpeg;base64,[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)

    i_st = tail.index('const STAGES = [')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + STAGES + PROMPTS + tail[i_fl:]
    tail = tail.replace('trainity_c09_video_v1', 'trainity_c12_video_v1')

    out = head + BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'C09|trainity_c09|Date_MASTER-C09|RELAȚIILE DINTRE', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  exec base64 ramase:', out.count('data:image/jpeg;base64,'))
    print('  leftover C09:', len(leftover), leftover[:5])
    for term in ['dashboard', 'what-if', 'scenari', 'predicți', 'recomand']:
        n = out.lower().count(term)
        if n:
            print('  ATENTIE T4/T5 (%dx): %s' % (n, term))


if __name__ == '__main__':
    main()
