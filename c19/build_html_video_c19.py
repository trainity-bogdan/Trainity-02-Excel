#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c19.py - HTML-Video-Excel-19-Guvernare.html (broadcast, JS-driven).

Mostenesc head+CSS si JS generic din c18 Video (sibling T5, acelasi tier).
Inlocuiesc:
  - BODY scaffolding (hero, exec slides, topbar, panel, toast, modal) -> C19 GUVERNARE
  - const STAGES [...] + const PROMPTS {...} -> C19 (6 etape / 18 pasi)
  - STORAGE_KEY, <title>, exec placeholders -> C19
ATENTIE: c18 Video are 6 imagini base64 CLONA (din c01). NU le copiez.
exec-stage + hero = SVG placeholder DRAFT (asset real ulterior).

Garda C19 (verb GUVERNEZ, artefact _GUVERNARE):
  C18 ruleaza (motorul) · C19 se tine corect prin reguli · C20 preda proprietatea.
  Etapa 4 = SEMNAL care SCHIMBA STAREA. Etapa 5 = OPRIRE automata fail-safe.
  ZERO identitate: management, responsabil, escaladare, dashboard decorativ,
  monitorizare, QA generic, ownership, delegare, AUTOMATIZARE ca identitate C19.
  ("motor" doar callback la C18.) Cifrele in Excel (R-V02.15).
"""
import re

SRC = 'c18/HTML-Video-Excel-18-Automatizare.html'
OUT = 'c19/HTML-Video-Excel-19-Guvernare.html'

TITLE = 'C19 · GUVERNARE · BROADCAST'
STORAGE = 'trainity_c19_video_v1'

# Axa CONTROL: eticheta scurta pe placeholderul exec-stage (DRAFT)
EXEC_TITLES = {1: 'REALITATE', 2: 'DEVIATII', 3: 'REGULA',
               4: 'PRAG-SEMNAL', 5: 'OPRIRE', 6: 'TEST'}


def exec_placeholder(n, titlu):
    """SVG inline 1600x900 DRAFT (NU base64 de poza clonata)."""
    return (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
        "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
        "</linearGradient></defs><rect width='1600' height='900' fill='url(%23g)'/>"
        "<text x='80' y='470' fill='%23FFD400' font-family='Georgia' font-size='90' "
        "font-weight='bold'>" + titlu + "</text>"
        "<text x='84' y='532' fill='%23ffffff' font-family='Arial' font-size='30' "
        "opacity='0.6'>C19 · exec-stage-" + str(n) + " · placeholder DRAFT</text></svg>"
    )


def hero_placeholder():
    """Hero broadcast = SVG placeholder DRAFT, text CONTROL (NU poza clonata)."""
    return (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
        "<defs><linearGradient id='hg' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
        "</linearGradient></defs><rect width='1600' height='900' fill='url(%23hg)'/>"
        "<text x='80' y='470' fill='%23FFD400' font-family='Georgia' font-size='96' "
        "font-weight='bold'>CONTROL</text>"
        "<text x='84' y='534' fill='%23ffffff' font-family='Arial' font-size='30' "
        "opacity='0.6'>C19 · hero · placeholder DRAFT</text></svg>"
    )


# ============ BODY C19 (curat, fara contaminare clona c01/c18) ============
BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C19 · Guvernare</div>
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
  <section class="screen" data-screen="hero" data-frag-total="3">
    <div class="hero-prelabel">Construcția 19 Excel</div>
    <h1 class="hero-title" data-locked="1">GUVERNAREA SISTEMULUI PRIN REGULI</h1>
    <p class="hero-hook frag" data-frag="1"><span data-locked="1">Cum se ține corect fără ochiul meu?</span></p>
    <p class="hero-sub frag" data-frag="2"><span data-locked="1">Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.</span></p>
    <p class="hero-sub frag" data-frag="3">Înainte să avem încredere, dăm sistemului reguli care îl țin corect fără ochiul nostru.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="11">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am pus motorul în mișcare, rula deja.</p>
      <p class="dim frag" data-frag="2">Nu am stat cu ochii pe el ca să-l prind.</p>
      <p class="dim frag" data-frag="3">Nu am desemnat cine răspunde de o abatere.</p>
      <p class="dim frag" data-frag="4">Greșeala clasică: <span data-locked="1">Confunzi «merge» cu «merge corect».</span></p>
      <p class="accent frag" data-frag="5">Am mutat verificarea din mintea mea în reguli.</p>
      <p class="frag" data-frag="6">Intrarea greșită e respinsă, excepția nu trece tăcut, eroarea gravă oprește singură.</p>
      <p class="frag" data-frag="7"><span data-locked="1">Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.</span></p>
      <p class="frag" data-frag="8">C20 poate prelua proprietatea sistemului guvernat.</p>
      <p class="payoff-wow frag" data-frag="9"><span class="wow-tag">WOW:</span><span data-wow="1">Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.</span></p>
      <p class="accent frag" data-frag="10"><span data-locked="1">Nu o supraveghez. O guvernez prin reguli.</span></p>
      <div class="final-motto frag" data-frag="11">Pleci, și munca se ține singură.</div>
    </div>
  </section>

  <!-- ============================================================ -->
  <!-- CONCLUZII - slide tranzitie intre final si executive          -->
  <!-- ============================================================ -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 19</span>
      </h1>
      <div class="conclusion-divider frag" data-frag="2"></div>
    </div>
  </section>

  <!-- ============================================================ -->
  <!-- EXECUTIVE SHOW - 7 screens (6 etape + 1 closing)              -->
  <!-- exec-stage = SVG placeholder DRAFT (axa CONTROL)              -->
  <!-- ============================================================ -->

  <!-- EXEC SLIDE 1: REALITATE -->
  <section class="screen" data-screen="executive" data-exec-slide="1" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-1"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">01</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 01</div>
      <div class="exec-emotion frag" data-frag="2">Sistemul care merge doar cât te uiți</div>
      <h2 class="exec-title frag" data-frag="3">REALITATE</h2>
      <p class="exec-phrase frag" data-frag="4">Motorul rulează fără mâna mea. Și totuși, pe o intrare proastă produce gunoi în tăcere.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 2: DEVIAȚII -->
  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-2"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Ce poate să devieze previzibil</div>
      <h2 class="exec-title frag" data-frag="3">DEVIAȚII</h2>
      <p class="exec-phrase frag" data-frag="4">Înainte de orice regulă, văd ce poate strica rezultatul. Plicul așteptat, scris ca praguri vii.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 3: REGULA -->
  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-3"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Regula care prinde intrarea greșită</div>
      <h2 class="exec-title frag" data-frag="3">REGULA</h2>
      <p class="exec-phrase frag" data-frag="4">Data Validation la sursă respinge intrarea greșită. STATUS OK / ATENȚIE / OPRIT iese din reguli.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 4: PRAG-SEMNAL -->
  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-4"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Pragul și semnalul</div>
      <h2 class="exec-title frag" data-frag="3">PRAG-SEMNAL</h2>
      <p class="exec-phrase frag" data-frag="4">O valoare derapează, pragul aprinde ATENȚIE, STATUS se schimbă singur. Semnalul acționează, nu se citește.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 5: OPRIRE -->
  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-5"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Excepția și oprirea controlată</div>
      <h2 class="exec-title frag" data-frag="3">OPRIRE</h2>
      <p class="exec-phrase frag" data-frag="4">Cazul neprevăzut cade în lista de excepții. Pe STATUS=OPRIT, fail-safe-ul reține rezultatul corupt.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 6: TEST -->
  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-6"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">Testul ochilor închiși</div>
      <h2 class="exec-title frag" data-frag="3">TEST</h2>
      <p class="exec-phrase frag" data-frag="4">Plantez deviații, plec din fața ecranului. Regulile prind, semnalează și opresc singure. C20 preia proprietatea.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 7: CLOSING APOTEOTIC -->
  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">Pleci, și munca <span class="exec-closing-motto-yellow">se ține singură.</span></h1>
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


# ============ STAGES C19 (6 etape x 3 pasi = 18, din SPEC C19 sectiunea 6) ============
STAGES = r'''const STAGES = [
  {
    id: 1, name: "REALITATE", emotion: "Sistemul care merge doar cât te uiți",
    hook: "Motorul rulează fără mâna ta.",
    next: "Și totuși, pe o intrare proastă produce gunoi în tăcere.",
    steps: [
      { num: "01", title: "Motorul rulează, dar pe o intrare proastă produce gunoi în tăcere.",
        instr: "Pornești motorul C18 dintr-o atingere. Lanțul se mișcă singur. <strong>Dar o intrare proastă curge prin el și iese un rezultat greșit, fără ca nimic să te avertizeze.</strong>",
        excel: true },
      { num: "02", title: "Tot tu verifici „a ieșit bine?\" la fiecare ciclu.",
        instr: "Ai scăpat de efortul pașilor, dar nu poți pleca. <strong>La fiecare ciclu te uiți încă o dată să confirmi că rezultatul e corect. Atenția ta a devenit gâtuirea.</strong>",
        excel: true },
      { num: "03", title: "„Merge\" nu înseamnă „merge corect\".",
        instr: "Sistemul rulează, deci pare gata. <strong>Confunzi «merge» cu «merge corect»: un sistem care se mișcă nu e același lucru cu unul în care poți avea încredere.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "DEVIAȚII", emotion: "Ce poate să devieze previzibil",
    hook: "Înainte de orice regulă, vezi ce poate strica rezultatul.",
    next: "Plicul așteptat, scris ca praguri vii.",
    steps: [
      { num: "04", title: "Registrul deviațiilor previzibile: ce poate strica rezultatul.",
        instr: "Deschizi foaia _GUVERNARE și treci în revistă coloanele de intrare. <strong>Nu cauți greșeala de azi, ci ce poate devia previzibil mâine: o cantitate aberantă, o categorie necunoscută, un total care nu se închide.</strong>",
        excel: true },
      { num: "05", title: "Promptul 1: Copilot listează valorile și intervalul permis pe fiecare coloană.", instr: "", prompt: 1 },
      { num: "06", title: "Definești plicul așteptat ca praguri vii (LIMIT_MIN, LIMIT_MAX).",
        instr: "Scrii plicul ca named ranges LIMIT_MIN și LIMIT_MAX, cu valoarea în celulă, plus o toleranță de închidere. <strong>Pragul nu e o opinie din capul tău, e un parametru viu pe care orice regulă îl citește.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "REGULA", emotion: "Regula care prinde intrarea greșită",
    hook: "Regula prinde la sursă, nu la capăt.",
    next: "Validarea respinge, STATUS iese din reguli.",
    steps: [
      { num: "07", title: "Data Validation la sursă: intrarea greșită e respinsă înainte să intre.",
        instr: "Pui Data Validation legată de praguri pe zona de intrare: cantitatea în interval, valoarea strict pozitivă, categoria din listă. <strong>O valoare imposibilă e respinsă la tastare, nu ajunge niciodată în motor.</strong>",
        excel: true },
      { num: "08", title: "Promptul 2: Copilot propune pragurile și ce abatere aprinde ATENȚIE / OPRIT.", instr: "", prompt: 2 },
      { num: "09", title: "STATUS OK / ATENȚIE / OPRIT, calculat din reguli.",
        instr: "Construiești STATUS ca formulă peste praguri, nu ca etichetă pusă de tine. <strong>OK cât totul e în plic, ATENȚIE pe o abatere suspectă, OPRIT pe o eroare gravă. Starea se recalculează singură.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "PRAG-SEMNAL", emotion: "Pragul și semnalul",
    hook: "Semnalul acționează, nu se citește.",
    next: "Starea se schimbă singură, nu o citești tu.",
    steps: [
      { num: "10", title: "Bagi o intrare greșită: e respinsă la sursă, nu ajunge în motor.",
        instr: "Încerci să tastezi o cantitate în afara intervalului sau o valoare negativă. <strong>Data Validation o oprește pe loc: greșeala e prinsă în secunda apariției, nu peste trei cicluri, când ar fi produs deja pagubă.</strong>",
        excel: true },
      { num: "11", title: "O valoare derapează intern: pragul aprinde ATENȚIE, STATUS se schimbă singur.",
        instr: "O valoare internă iese din plicul așteptat. <strong>Pragul o prinde, STATUS trece din OK în ATENȚIE de la sine. Nu ai apăsat nimic, regula a văzut prima.</strong>",
        excel: true },
      { num: "12", title: "Testul anti-dashboard: semnalul acționează (schimbă starea), nu doar afișează.",
        instr: "Întrebarea care separă C19 de un panou T4: semnalul tău schimbă ceva sau doar arată? <strong>Aici STATUS schimbă starea sistemului și pregătește oprirea. Dacă doar colorezi o celulă de citit, e dashboard, nu guvernare.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "OPRIRE", emotion: "Excepția și oprirea controlată",
    hook: "Cazul neprevăzut nu mai trece tăcut.",
    next: "Fail-safe leagă output-ul de STATUS=OPRIT.",
    steps: [
      { num: "13", title: "Excepția: cazul neprevăzut cade în lista de excepții, nu trece tăcut.",
        instr: "O categorie necunoscută, un caz pe care nicio regulă nu îl prevedea. <strong>În loc să curgă tăcut în decizii, cade într-o listă de excepții, scos la lumină ca să fie văzut.</strong>",
        excel: true },
      { num: "14", title: "Fail-safe: output legat de STATUS=OPRIT, rezultatul corupt nu mai curge.",
        instr: "Legi output-ul de STATUS: pe OPRIT, rezultatul e reținut singur. <strong>Eroarea gravă oprește lanțul, fail-safe-ul blochează rezultatul corupt înainte să ajungă în aval. Fără mâna ta.</strong>",
        excel: true },
      { num: "15", title: "_GUVERNARE marchează excepția și oprește, dar nu desemnează responsabilul (granița C20).",
        instr: "Pe _GUVERNARE: praguri, validare, STATUS, listă de excepții, fail-safe. <strong>Sistemul marchează abaterea și se oprește singur. Cine deține și cine răspunde de oprire începe la C20, nu aici.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "TEST", emotion: "Testul ochilor închiși",
    hook: "Proba finală: pleci, și regulile țin singure.",
    next: "Sistemul guvernat e gata de predat la C20.",
    steps: [
      { num: "16", title: "Plantezi deviații, pleci: regulile prind, semnalează, opresc singure.",
        instr: "Strecori în date câteva valori imposibile și un caz neprevăzut, apoi pleci din fața ecranului. <strong>Fără tine, regulile prind anomaliile, semnalul trece STATUS în OPRIT, fail-safe-ul reține rezultatul. STATUS=OPRIT e intenționat: dovada că sistemul s-a prins singur.</strong>",
        excel: true },
      { num: "17", title: "Devii cel care scrie constituția sistemului, nu cel care patrulează.",
        instr: "Nu mai ești omul care stă cu ochii pe sistem ca să-l prindă. <strong>Ești cel care îi scrie regulile. Verificarea a ieșit din mintea ta și trăiește în _GUVERNARE.</strong>",
        excel: true },
      { num: "18", title: "Sistemul se ține corect singur; C20 îi poate prelua proprietatea.",
        instr: "Marchezi construcția finalizată. <strong>C19 face sistemul să se țină corect singur, încă deținut de tine. Predarea proprietății, a răspunderii și a controlului începe la C20 Delegarea.</strong>",
        excel: false }
    ]
  }
];

'''


# ============ PROMPTS C19 (2 Copilot, texte din SPEC / consistente cu Studiu) ============
PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Registrul deviațiilor previzibile",
    text: "Am un sistem care rulează pe acest workbook. Pentru fiecare coloană de intrare, listează-mi valorile întâlnite și intervalul permis în care o valoare e încă plauzibilă, și propune o regulă de Data Validation care respinge la sursă intrările în afara plicului. Nu corecta automat nicio valoare și nu modifica datele; doar propune regula, eu confirm. Nu configura execuția lanțului și nu desemna cine răspunde. Vreau să văd ce poate devia previzibil.",
    meta: "AI propune plicul și validarea. Omul confirm regula."
  },
  2: {
    label: "Prompt 02 · Pragurile și logica semnalului",
    text: "Pe baza valorilor și a intervalelor confirmate, propune-mi praguri (min/max) pe valorile interne și o logică de semnal: ce abatere e doar suspectă și aprinde ATENȚIE, și ce eroare e gravă și trece STATUS în OPRIT, oprind lanțul. Spune-mi cum se calculează STATUS din reguli, nu cum se afișează pentru un om. Nu desemna cine răspunde și nu te rezuma la un refresh. Eu corectez pragurile și decid unde e linia.",
    meta: "AI așază logica semnalului. Omul ratifică pragurile."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # --- HEAD: title + exec-stage placeholders DRAFT (inlocuiesc base64 clona c01) ---
    head = re.sub(r'<title>C\d+[^<]*</title>', '<title>%s</title>' % TITLE, head, count=1)
    for n in range(1, 7):
        ph = exec_placeholder(n, EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)
    # daca exista vreun hero base64 in head (background hero), il inlocuiesc cu placeholder
    hero = hero_placeholder()
    head = re.sub(r'(\.hero[\w-]*\s*\{[^}]*background-image:\s*)url\("data:image/jpeg;base64,[^"]*"\)',
                  lambda m: m.group(1) + 'url("%s")' % hero, head)

    # --- TAIL: STAGES + PROMPTS + STORAGE_KEY ---
    i_st = tail.index('const STAGES = [')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + STAGES + PROMPTS + tail[i_fl:]
    tail = re.sub(r'trainity_c\d+_video_v1', STORAGE, tail)

    out = head + BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    # --- SELF-VERIFY ---
    import unicodedata
    outn = unicodedata.normalize('NFC', out)
    def has(s):
        return unicodedata.normalize('NFC', s) in outn
    jpeg = out.count('data:image/jpeg;base64,')
    contam = re.findall(r'_AUTOMATIZARE|AUTOMATIZEZ|_SISTEM\b|SISTEMATIZARE|trainity_c18|trainity_c17|18-Automatizare|17-Sistematizare', out)
    dashes = [c for c in ('—', '–') if c in out]
    locked = {
        'HERO': 'Cum se ține corect fără ochiul meu?',
        'BOMBA': 'Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.',
        'MANTRA': 'Nu o supraveghez. O guvernez prin reguli.',
        'WOW': 'Un sistem care mergea doar cât stăteai cu ochii pe el.',
        'MOTTO': 'Pleci, și munca se ține singură.',
        'GRESEALA': 'confunzi «merge» cu «merge corect»',
        'AHA': 'Un sistem în care ai încredere nu e cel pe care îl urmărești.',
        'hov-object': 'GUVERNAREA SISTEMULUI PRIN REGULI',
    }
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out.encode('utf-8')), 'bytes')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  STORAGE_KEY:', re.search(r'const STORAGE_KEY = "[^"]*"', out).group(0))
    print('  exec base64 jpeg ramase (trebuie 0):', jpeg)
    print('  exec-stage SVG placeholder DRAFT (trebuie 6):', out.count('placeholder DRAFT') - 1)
    print('  STAGES steps (num:):', out.count('num: "'), '| prompturi:', out.count('label: "Prompt'))
    print('  contaminare C17/C18/AUTOMATIZARE (trebuie 0):', len(contam), contam[:6])
    print('  em/en-dash (trebuie []):', dashes)
    miss = [k for k, v in locked.items() if not has(v)]
    print('  LOCKED 8 sloturi:', 'TOATE OK' if not miss else ('LIPSA -> ' + ', '.join(miss)))
    print('  6 etape verbatim:', sum(has(e) for e in [
        'Sistemul care merge doar cât te uiți', 'Ce poate să devieze previzibil',
        'Regula care prinde intrarea greșită', 'Pragul și semnalul',
        'Excepția și oprirea controlată', 'Testul ochilor închiși']), '/6')
    print('  NEXT C20:', 'OK' if 'C20' in out else 'LIPSA')
    print('  closing </html>:', 'OK' if out.rstrip().endswith('</html>') else 'LIPSA')


if __name__ == '__main__':
    main()
