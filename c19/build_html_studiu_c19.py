#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c19.py - HTML-Studiu-Excel-19-Guvernare.html prin COPY+MODIFY din c18.

Strategie (oglinda build_html_studiu_c17.py): pastrez head+CSS si JS din c18 (generice),
inlocuiesc DOAR <body>..<script> cu narativ C19 GUVERNARE. Patch title + mobile-topbar +
STORAGE_KEY. HERO = SVG placeholder inline (NU base64 clone din c18, imaginile GUVERNARE
nu exista inca -> DRAFT marcat).

Axa C19: GUVERNAREA / controlul prin reguli. T5 AUTONOMIE. Autorul iese din ATENTIE.
Artefact central: foaia _GUVERNARE (reguli/praguri/validari/semnale/exceptii/fail-safe).
Verb-semnatura: GUVERNEZ. Formula treapta: C18 ruleaza · C19 se tine corect · C20 preda.
Garda: E4 = semnal care SCHIMBA STAREA (nu dashboard). E5 = OPRIRE automata fail-safe
(nu interventie umana, fara responsabil). NU babysitting, NU management, NU ownership (C20),
NU motor-ca-identitate (motor = callback la C18). Zero cifre business (R-V02.15).
Zero em-dash / en-dash. Demonstratia tehnica produce STATUS=OPRIT (intentionat).
"""
import re, os

SRC = 'c18/HTML-Studiu-Excel-18-Automatizare.html'
OUT = 'c19/HTML-Studiu-Excel-19-Guvernare.html'

# HERO placeholder SVG inline (DRAFT: nu exista imagini finale GUVERNARE)
HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>CONTROL</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C19 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C19 · Guvernare</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

      <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Guvernare C19: un sistem care rula doar cat stateai cu ochii pe el invata sa se prinda singur cand greseste, sa aprinda semnalul si sa se opreasca fara tine">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C19</span><span class="hov-object">GUVERNAREA SISTEMULUI PRIN REGULI</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cum se ține corect fără ochiul meu?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 5">
            <span class="sm-step">SISTEMATIZARE</span><span class="sm-arrow">·</span><span class="sm-step">AUTOMATIZARE</span><span class="sm-arrow">·</span><span class="sm-step active">GUVERNARE</span><span class="sm-arrow">·</span><span class="sm-step">DELEGARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title">Cum dai sistemului reguli care îl țin corect fără să stai cu ochii pe el</h1>
        <p class="hero-microbrief">Motorul rulează (C18): lanțul se mișcă fără mâna ta. Și totuși, pe o intrare greșită, produce un rezultat greșit în tăcere, iar tu tot verifici „a ieșit bine?" la fiecare ciclu. Aici nu mai supraveghezi munca. O guvernezi prin reguli: deviațiile previzibile sunt prinse, semnalate sau blocate înainte să producă pagubă.</p>
        <div class="cover-miza">C19 nu repară motorul și nu îl pornește: ia un sistem care rulează și îi dă reguli care îl țin corect. Construiești foaia _GUVERNARE: praguri vii, validare la sursă, semnale care schimbă starea, o listă de excepții și un fail-safe care leagă rezultatul de STATUS. Atenția ta nu mai e plafonul. Sistemul se ține corect singur; predarea proprietății începe la treapta următoare.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1">Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.</p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Lanțul se mișcă fără tine și totuși nu poți pleca. Și totuși:</p>
        <ul class="tu-list">
          <li>pe o intrare proastă, motorul produce un rezultat greșit în tăcere</li>
          <li>un caz neprevăzut trece nedetectat și curge în decizii ca și cum ar fi corect</li>
          <li>ai scăpat de efort, dar tot tu verifici „a ieșit bine?" la fiecare ciclu</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Confunzi «merge» cu «merge corect».<br><span class="tu-hl">Un sistem care rulează nu e același lucru cu un sistem în care poți avea încredere.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai ești omul care patrulează sistemul. <span class="tu-hl">Ești omul care îi scrie regulile.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>pe o intrare greșită, rezultat greșit în tăcere</li><li>cazul neprevăzut trece nedetectat</li><li>tot tu verifici la fiecare ciclu</li><li>greșeala se vede târziu, după pagubă</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>intrarea greșită e respinsă la sursă</li><li>excepția cade în listă, nu trece tăcut</li><li>semnalul acționează, STATUS se schimbă singur</li><li>output legat de STATUS=OPRIT, nu mai curge</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>foaia _GUVERNARE: regulile care țin sistemul corect</li><li>praguri vii, validare la sursă, semnale care schimbă starea</li><li>o listă de excepții și un fail-safe legat de STATUS</li><li>un sistem care se prinde singur, fără ochiul tău</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1"><mark>Nu o supraveghez. O guvernez prin reguli.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CE PARE CONTROL DAR ESTE DOAR OCHIUL TĂU</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">BABYSITTING</b><p class="anomaly-desc">Stai cu ochii pe sistem ca să-l prinzi când greșește. Monitorizarea te ține prezent. Corecția: regulile prind în locul ochiului, sistemul se ține fără tine.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">DASHBOARD DE CITIT</b><p class="anomaly-desc">Un panou frumos care afișează stări pentru un om care decide. Asta e T4. Corecția: semnalul C19 acționează, schimbă starea și oprește, nu se citește.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">DOAR REFRESH</b><p class="anomaly-desc">Aduci setul la zi și crezi că l-ai ținut corect. E C04, nu guvernare. Corecția: regulile țin corect un sistem care rulează, nu reîmprospătează un set.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">AUTOMATIZARE</b><p class="anomaly-desc">Motorul rulează singur, dar pe o intrare proastă produce gunoi tăcut. Acela e C18. Corecția: C19 nu pune lanțul în mișcare, îi adaugă regulile care îl țin corect.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">RESPONSABIL</b><p class="anomaly-desc">Numești cine deține și cine răspunde la o abatere. Acela e C20. Corecția: _GUVERNARE marchează și oprește, dar nu desemnează responsabilul.</p></div>
<div class="anomaly-card"><span class="anomaly-num">06</span><b class="anomaly-title">VERIFIC LA FINAL</b><p class="anomaly-desc">Citești rezultatul la capăt și speri că e bun. Greșeala se vede târziu, după pagubă. Corecția: regula prinde abaterea în momentul apariției, la sursă.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · Sistemul care merge doar cât te uiți</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Motorul rulează fără mâna ta. Înainte de orice regulă, vezi pe viu de ce tot nu poți pleca: pe o intrare greșită, produce gunoi în tăcere și tot tu verifici.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Motorul rulează, dar pe o intrare proastă produce gunoi în tăcere</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C19-Guvernare.xlsx. <span data-locked="1">Vine cu motorul moștenit din C18: lanțul se mișcă singur, fără mâna ta.</span> Dar dacă în date intră o valoare imposibilă, motorul o insumă liniștit și scoate un rezultat greșit, fără să clipească. Merge. Nu înseamnă că merge corect.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Tot tu verifici „a ieșit bine?" la fiecare ciclu</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Ai scăpat de efortul execuției, dar nu de grijă. La fiecare ciclu te uiți peste rezultat: „a ieșit bine?". Atenția ta a devenit gâtuirea: sistemul e autonom doar pe hârtie, fiindcă tot un om confirmă de fiecare dată că rezultatul e corect.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">„Merge" nu înseamnă „merge corect"</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Adaugi o foaie nouă, _GUVERNARE, și o fixezi ca foaia controlului. <span data-locked="1">Aici nu repari motorul și nu îl pornești: îi dai regulile care îl țin corect.</span> Declari intenția: nu o mai supraveghez, o guvernez prin reguli. Verificarea iese din mintea ta și intră în sistem.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · Ce poate să devieze previzibil</div>
      <h2 class="stage-name">DEVIAȚII</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să scrii regulile, vezi ce poate strica rezultatul: ce coloane pot primi o valoare imposibilă și care e plicul în care o intrare e încă plauzibilă.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Registrul deviațiilor previzibile: ce poate strica rezultatul</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te întrebi nu „ce a ieșit?", ci „ce poate devia previzibil?". Treci în revistă coloanele de intrare: cantitatea, valoarea netă, data facturii, categoria. Pentru fiecare, ce ar fi o valoare imposibilă, una care nu poate exista, dar pe care motorul ar insuma-o oricum.</p>

  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Promptul 1: Copilot listează valorile și intervalul permis pe fiecare coloană</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Copilot pe foaia _GUVERNARE și lipești Promptul 1. AI parcurge fiecare coloană de intrare și propune valorile întâlnite și intervalul permis, plus o regulă de Data Validation care respinge intrările în afara plicului. Nu corectează automat și nu desemnează pe nimeni. AI propune, omul decide.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · REGISTRUL DEVIAȚIILOR PREVIZIBILE</div>
      <div class="prompt-text">Am un sistem care rulează pe acest workbook. Pentru fiecare coloană de intrare, listează-mi valorile întâlnite și intervalul permis în care o valoare e încă plauzibilă, și propune o regulă de Data Validation care respinge la sursă intrările în afara plicului. Nu corecta automat nicio valoare și nu modifica datele; doar propune regula, eu confirm. Nu configura execuția lanțului și nu desemna cine răspunde. Vreau să văd ce poate devia previzibil.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Definești plicul așteptat ca praguri vii (LIMIT_MIN, LIMIT_MAX)</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pe _GUVERNARE scrii plicul ca praguri vii: named ranges LIMIT_MIN și LIMIT_MAX, cu valoarea în celulă, plus o toleranță pentru închiderea totalurilor. <span data-locked="1">Pragul nu e o opinie din cap, e un parametru vizibil pe care orice regulă îl citește.</span> Schimbi pragul, regula se mută cu el.</p>
    <div class="section-sublabel">CE INTRĂ ÎN PLICUL AȘTEPTAT</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">prag</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CANTITATEA · LIMIT_CANT_MIN / MAX</div>
        <div class="inv-item-desc">Intervalul în care o cantitate e plauzibilă. Sub minim sau peste maxim: în afara plicului.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">prag</div>
      <div class="inv-item-body">
        <div class="inv-item-label">VALOAREA · LIMIT_VAL_MIN</div>
        <div class="inv-item-desc">O valoare netă negativă sau nulă nu poate exista la o vânzare reală.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">prag</div>
      <div class="inv-item-body">
        <div class="inv-item-label">TOLERANȚA · LIMIT_TOL</div>
        <div class="inv-item-desc">Cât poate să difere totalul înregistrat de cel consistent înainte să fie abatere.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu corectează</div>
      <div class="inv-item-body">
        <div class="inv-item-label">PRAGUL MARCHEAZĂ, NU REPARĂ</div>
        <div class="inv-item-desc">Regula spune „în afara plicului", nu schimbă valoarea în locul tău.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">se rupe scos</div>
      <div class="inv-item-body">
        <div class="inv-item-label">PRAG VIU, ÎN CELULĂ</div>
        <div class="inv-item-desc">Pragul trăiește ca named range în workbook, citit de fiecare regulă. Nu e o notă pe margine.</div>
      </div>
    </li>
    </ul>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-3" data-stage="3" data-stage-ghost="03">
  <header class="stage-header">
    <div class="stage-number">03</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 3 · Regula care prinde intrarea greșită</div>
      <h2 class="stage-name">REGULA</h2>
      <div class="stage-tags"><span class="phase-tag">REGULĂ · VALIDARE</span><span class="type-tag">Copilot · Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Acum transformi plicul în reguli care acționează: intrarea greșită e respinsă la sursă, iar din praguri se naște un STATUS care nu se citește, se calculează.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Data Validation la sursă: intrarea greșită e respinsă înainte să intre</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pe zona de intrare pui Data Validation legată de praguri: cantitatea în intervalul LIMIT_, valoarea strict pozitivă, categoria din listă. <span data-locked="1">O valoare imposibilă e respinsă la tastare, nu ajunge niciodată în motor.</span> Regula prinde la sursă, nu la capăt.</p>

  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Promptul 2: Copilot propune pragurile și ce abatere aprinde ATENȚIE / OPRIT</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2. AI propune, peste praguri, ce abatere e doar suspectă (aprinde ATENȚIE) și ce eroare e gravă (trece STATUS în OPRIT și oprește lanțul). Tu corectezi pragurile și decizi unde e linia. AI așază logica semnalului; omul o ratifică.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · PRAGURILE ȘI LOGICA SEMNALULUI</div>
      <div class="prompt-text">Pe baza valorilor și a intervalelor confirmate, propune-mi praguri (min/max) pe valorile interne și o logică de semnal: ce abatere e doar suspectă și aprinde ATENȚIE, și ce eroare e gravă și trece STATUS în OPRIT, oprind lanțul. Spune-mi cum se calculează STATUS din reguli, nu cum se afișează pentru un om. Nu desemna cine răspunde și nu te rezuma la un refresh. Eu corectez pragurile și decid unde e linia.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">STATUS OK / ATENȚIE / OPRIT, calculat din reguli</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În _GUVERNARE construiești STATUS_SISTEM ca formulă peste semnale: dacă o regulă gravă cade, OPRIT; dacă doar o suspiciune, ATENȚIE; altfel OK. <span data-locked="1">STATUS nu e o etichetă pe care o pui tu, e o stare care se recalculează singură la fiecare schimbare în date.</span> Conditional formatting îl colorează verde, galben, roșu.</p>
    <div class="section-sublabel">DOVADA CONTROLULUI</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Intrarea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">orice valoare intra în motor</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">Data Validation respinge la sursă</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Pragul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">știut doar de tine, în cap</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">named range LIMIT_, citit de reguli</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Starea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">o citeai tu, la final</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">STATUS se recalculează singur</span></div>
      </div>
    </li>
    </ul>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-4" data-stage="4" data-stage-ghost="04">
  <header class="stage-header">
    <div class="stage-number">04</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 4 · Pragul și semnalul</div>
      <h2 class="stage-name">PRAG-SEMNAL</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Anti-dashboard</span></div>
    </div>
  </header>
  <p class="stage-quote">Probă pe viu: bagi o intrare greșită și vezi că semnalul nu se mulțumește să afișeze. Acționează. Schimbă STATUS, oprește. Nu e un panou de citit.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Bagi o intrare greșită: e respinsă la sursă, nu ajunge în motor</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Încerci să tastezi o cantitate în afara intervalului sau o valoare negativă. <span data-locked="1">Data Validation o oprește pe loc: nu intră în date, nu ajunge la motor.</span> Greșeala e prinsă în secunda apariției, nu peste trei cicluri, când ar fi produs deja pagubă.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">O valoare derapează intern: pragul aprinde ATENȚIE, STATUS se schimbă singur</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O agregare iese din plicul așteptat, dar nu prin tastare, ci din combinația datelor. <span data-locked="1">Pragul o vede: STATUS trece din OK în ATENȚIE, fără să atingi tu nimic.</span> Nu tu observi abaterea și schimbi eticheta; regula o observă și starea se mută singură.</p>

  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Testul anti-dashboard: semnalul acționează (schimbă starea), nu doar afișează</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Întrebarea care separă C19 de un panou T4: semnalul doar arată o culoare, sau face ceva? <span data-locked="1">Aici semnalul schimbă STATUS și, prin el, leagă mai departe oprirea lanțului.</span> Dacă ar fi doar un dashboard de citit pentru un om care decide, n-ar fi guvernare. Semnalul acționează.</p>
    <div class="section-sublabel">ANTI-DASHBOARD, PE VIU</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">acționează</div>
      <div class="inv-item-body">
        <div class="inv-item-label">SCHIMBĂ STAREA</div>
        <div class="inv-item-desc">Semnalul mută STATUS între OK, ATENȚIE și OPRIT. Starea se schimbă, nu doar culoarea.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">la sursă</div>
      <div class="inv-item-body">
        <div class="inv-item-label">PRINDE LA INTRARE</div>
        <div class="inv-item-desc">Intrarea greșită e respinsă unde apare, nu citită la capăt după ce a curs.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu citește</div>
      <div class="inv-item-body">
        <div class="inv-item-label">NU E DASHBOARD (T4)</div>
        <div class="inv-item-desc">Nu e un panou frumos pentru un om care decide. Acționează singur, nu așteaptă o privire.</div>
      </div>
    </li>
    </ul>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · Excepția și oprirea controlată</div>
      <h2 class="stage-name">OPRIRE</h2>
      <div class="stage-tags"><span class="phase-tag">STARE · SEMNAL</span><span class="type-tag">Fail-safe</span></div>
    </div>
  </header>
  <p class="stage-quote">Cazul neprevăzut nu mai trece tăcut: cade în lista de excepții, iar pe STATUS=OPRIT, un fail-safe leagă output-ul și rezultatul corupt nu mai curge. Fără mâna ta.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Excepția: cazul neprevăzut cade în lista de excepții, nu trece tăcut</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O categorie necunoscută, un caz pe care nicio regulă nu îl prevedea, apare în date. <span data-locked="1">În loc să treacă tăcut, cade în lista de excepții din _GUVERNARE, marcat ca „de privit".</span> Excepția nu se ascunde și nu se autocorectează: e scoasă la lumină ca să nu curgă nedetectată.</p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Fail-safe: output legat de STATUS=OPRIT, rezultatul corupt nu mai curge</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Construiești OUTPUT_GUVERNAT: dacă STATUS e OPRIT, rezultatul e reținut; altfel, trece totalul validat. <span data-locked="1">Output-ul nu mai e legat de motor, ci de stare: pe OPRIT, sistemul se oprește singur, nu produce un rezultat corupt în aval.</span> Oprirea e automată, nu o apeși tu.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">_GUVERNARE marchează excepția și oprește, dar nu desemnează responsabilul (granița C20)</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">Aici e linia care separă guvernarea de predarea proprietății.</span> _GUVERNARE prinde abaterea, aprinde semnalul și oprește lanțul, dar nu scrie un nume lângă excepție și nu escaladează la cineva. Spune „aici e o abatere și sistemul s-a oprit", nu „tu răspunzi de ea". Cine deține și cine preia e treaba treptei următoare.</p>
    <div class="section-sublabel">CE FACE ȘI CE NU FACE _GUVERNARE</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">marchează</div>
      <div class="inv-item-body">
        <div class="inv-item-label">EXCEPȚIA · SCOASĂ LA LUMINĂ</div>
        <div class="inv-item-desc">Cazul neprevăzut cade în listă, nu trece tăcut. Sistemul îl arată.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">oprește</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FAIL-SAFE · STATUS=OPRIT</div>
        <div class="inv-item-desc">Output legat de stare. Rezultatul corupt nu mai curge, fără intervenția ta.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu desemnează</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FĂRĂ RESPONSABIL, FĂRĂ ESCALADARE</div>
        <div class="inv-item-desc">Nu scrie cine răspunde, nu predă proprietatea. Asta începe la C20.</div>
      </div>
    </li>
    </ul>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-6" data-stage="6" data-stage-ghost="06">
  <header class="stage-header">
    <div class="stage-number">06</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 6 · Testul ochilor închiși</div>
      <h2 class="stage-name">TEST</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Predare T5</span></div>
    </div>
  </header>
  <p class="stage-quote">Proba finală: plantezi deviații, pleci, închizi ochii. Regulile prind, semnalează, opresc singure. Apoi marchezi unde se termină C19 și începe predarea proprietății.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">Plantezi deviații, pleci: regulile prind, semnalează, opresc singure</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Strecori în date câteva valori imposibile și un caz neprevăzut, apoi pleci din fața ecranului. <span data-locked="1">Fără tine, regulile prind anomaliile, semnalul trece STATUS în OPRIT, iar fail-safe-ul reține rezultatul.</span> În demonstrația tehnică, datele vin cu deviații deja plantate: STATUS=OPRIT este intenționat, dovada că sistemul s-a prins singur, nu un defect.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Devii cel care scrie constituția sistemului, nu cel care patrulează</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te uiți la ce ai construit: nu mai stai cu ochii pe sistem ca să-l prinzi când greșește. <span data-locked="1">I-ai scris regulile, pragurile, semnalele și oprirea. El se prinde singur.</span> Nu mai ești paznicul care patrulează; ești cel care a scris constituția după care sistemul se guvernează.</p>
    <div class="section-sublabel">TESTUL OCHILOR ÎNCHIȘI, PE VIU</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">trece</div>
      <div class="inv-item-body">
        <div class="inv-item-label">SE PRINDE FĂRĂ TINE</div>
        <div class="inv-item-desc">Deviațiile plantate sunt prinse, semnalate, oprite. Fără ochiul tău pe ecran.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">trece</div>
      <div class="inv-item-body">
        <div class="inv-item-label">OPRIREA E AUTOMATĂ</div>
        <div class="inv-item-desc">Pe STATUS=OPRIT, fail-safe-ul reține rezultatul singur. Nu apeși tu nimic.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">pică</div>
      <div class="inv-item-body">
        <div class="inv-item-label">O ABATERE NEPRINSĂ</div>
        <div class="inv-item-desc">Dacă o deviație trece tăcut, mai e o regulă de scris. Sistemul nu se ține încă singur.</div>
      </div>
    </li>
    </ul>
  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Sistemul se ține corect singur; C20 îi poate prelua proprietatea</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">C19 face sistemul să se țină corect singur, încă deținut de autor. Treapta următoare predă proprietatea.</span> Predai un sistem guvernat: reguli, praguri, semnale și oprire, toate vii în _GUVERNARE. Cine deține, cine răspunde și cine preia controlul încep la C20. Tu ai garantat că sistemul se ține corect fără ochiul tău.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda sistemul guvernat treptei următoare, confirmi fiecare invariant al guvernării. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">_GUVERNARE EXISTĂ</div><div class="final-text">Date_MASTER-C19-Guvernare.xlsx are foaia _GUVERNARE, ca foaia controlului prin reguli.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">PRAGURI VII</div><div class="final-text">Plicul așteptat ca named ranges LIMIT_, în celulă, citite de fiecare regulă.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">VALIDARE LA SURSĂ</div><div class="final-text">Data Validation respinge intrarea greșită la tastare, nu intră în motor.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">STATUS CALCULAT</div><div class="final-text">OK / ATENȚIE / OPRIT, recalculat singur din reguli, nu o etichetă pusă de tine.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">SEMNAL CARE ACȚIONEAZĂ</div><div class="final-text">Semnalul schimbă starea și leagă oprirea. Nu e un dashboard de citit (T4).</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">EXCEPȚIA NU TRECE TĂCUT</div><div class="final-text">Cazul neprevăzut cade în lista de excepții, scos la lumină, nu ascuns.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">FAIL-SAFE LEGAT DE STATUS</div><div class="final-text">Pe STATUS=OPRIT, output-ul e reținut singur. Rezultatul corupt nu mai curge.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">SE ȚINE FĂRĂ AUTOR</div><div class="final-text">Cu deviații plantate și autorul absent, regulile prind, semnalează, opresc. Gata de predat la C20.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Sistemul se ține corect singur.</div>
          <div class="completion-subtitle">Guvernat prin reguli, fără ochiul autorului. Gata de predat proprietatea la treapta următoare.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 5 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C20 · Delegarea</h3>
        <p class="next-desc">Sistemul se ține corect singur, dar e încă deținut de tine: tu i-ai scris regulile, tot tu ești titularul. Cum predai proprietatea, ca altcineva să dețină și să răspundă de sistemul guvernat? Delegarea începe la C20.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Motorul rula fără mâna ta, dar pe o intrare greșită producea gunoi în tăcere.</div>
        <div class="payoff-line accent">Și tot tu verificai „a ieșit bine?" la fiecare ciclu: atenția ta era plafonul.</div>
        <div class="payoff-line regular">Acum sistemul se ține corect prin reguli: intrarea greșită e respinsă, excepția nu trece tăcut, iar pe o eroare gravă se oprește singur, din _GUVERNARE.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.</span></div>
        <div class="payoff-motto" data-locked="1">Pleci, și munca se ține singură.</div>
      </section>

      <section class="transformare-section">
        <div class="tu-cert">
          <div class="tu-kicker">✓ DUPĂ C19 POȚI</div>
          <p class="tu-statement-sm">Dai sistemului reguli care îl țin corect fără ochiul tău: intrarea greșită respinsă, excepția marcată, oprirea automată pe eroare gravă.</p>
        </div>
        <div class="ts-block ts-identity"><div class="ts-label">DE ACUM ÎNAINTE</div>
          <div class="ts-pair"><span class="ts-no">Nu mai supraveghezi.</span><span class="ts-yes">Guvernezi prin reguli.</span></div>
          <div class="ts-pair"><span class="ts-no">Nu mai verifici „a ieșit bine?".</span><span class="ts-yes">Lași regulile să prindă.</span></div>
          <div class="ts-pair"><span class="ts-no">Nu mai întrebi „merge?".</span><span class="ts-yes">Întrebi „se ține corect fără mine?".</span></div>
        </div>
      </section>

      <footer class="footer">
        TRAINITY · C19 GUVERNARE · sistemul se ține corect singur, prin reguli
      </footer>

    </main>

    <nav class="side-nav" id="sideNav">

      <div class="nav-progress">
        <div class="nav-progress-row">
          <span class="nav-progress-num" id="navProgressNum">0/18</span>
          <span class="nav-progress-total">PAȘI</span>
        </div>
        <div class="nav-progress-track"><div class="nav-progress-fill" id="navProgressFill"></div></div>
      </div>

      <div class="nav-section-label">6 ETAPE</div>
      <div class="nav-items"><a class="nav-item" data-nav-stage="1" href="#stage-1" onclick="navigateStage(1,event)"><span class="nav-item-num">1</span><span class="nav-item-text"><span class="nav-item-name">REALITATE</span><span class="nav-item-meta">3 pași · Manual</span></span></a>
<a class="nav-item" data-nav-stage="2" href="#stage-2" onclick="navigateStage(2,event)"><span class="nav-item-num">2</span><span class="nav-item-text"><span class="nav-item-name">DEVIAȚII</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">REGULA</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">PRAG-SEMNAL</span><span class="nav-item-meta">3 pași · Control</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">OPRIRE</span><span class="nav-item-meta">3 pași · Fail-safe</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">TEST</span><span class="nav-item-meta">3 pași · Payoff</span></span></a></div>

      <div class="nav-section-label">8 VERIFICĂRI FINALE</div>
      <div class="nav-finals">
        <div class="nav-finals-grid"><a class="nav-final-dot" data-nav-final="1" href="#final-1" onclick="navigateFinal(1,event)">1</a>
<a class="nav-final-dot" data-nav-final="2" href="#final-2" onclick="navigateFinal(2,event)">2</a>
<a class="nav-final-dot" data-nav-final="3" href="#final-3" onclick="navigateFinal(3,event)">3</a>
<a class="nav-final-dot" data-nav-final="4" href="#final-4" onclick="navigateFinal(4,event)">4</a>
<a class="nav-final-dot" data-nav-final="5" href="#final-5" onclick="navigateFinal(5,event)">5</a>
<a class="nav-final-dot" data-nav-final="6" href="#final-6" onclick="navigateFinal(6,event)">6</a>
<a class="nav-final-dot" data-nav-final="7" href="#final-7" onclick="navigateFinal(7,event)">7</a>
<a class="nav-final-dot" data-nav-final="8" href="#final-8" onclick="navigateFinal(8,event)">8</a></div>
      </div>

      <div class="nav-controls">
        <button class="nav-ctrl-btn" onclick="resetProgress()">RESETEAZĂ PROGRES</button>
      </div>
    </nav>

  </div>
</div>

<button class="scroll-top" id="scrollTop" onclick="scrollToTop()" aria-label="Sus">↑</button>

<div class="stage-toast" id="stageToast" role="status" aria-live="polite"></div>

<button class="continue-btn" id="continueBtn" onclick="continueToCurrentStep()" aria-label="Continuă cu pasul curent">
  <span class="continue-btn-text">Continuă</span>
  <span class="continue-btn-counter" id="continueBtnCounter">pasul 1/18</span>
  <span class="continue-btn-arrow">↓</span>
</button>

'''


def main():
    src = open(SRC, encoding='utf-8').read()
    lines = src.splitlines(keepends=True)
    body_idx = next(i for i, l in enumerate(lines) if l.startswith('<body>'))
    script_idx = next(i for i, l in enumerate(lines) if l.startswith('<script>'))
    head = ''.join(lines[:body_idx])
    tail = ''.join(lines[script_idx:])

    # patch head: title + mobile-topbar (NEXT(...) marker e in CSS comment, il aliniem)
    head = re.sub(r'<title>.*?</title>', '<title>C19 · Guvernare · Trainity</title>', head, count=1)
    head = re.sub(r'NEXT \(C\d+\)', 'NEXT (C20)', head)
    # patch script tail: STORAGE_KEY c18 -> c19
    tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c19_study_v1', tail)

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c19', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # ---- self-checks ----
    # garda: tokeni sursa c18 reziduali in CONTINUT (body)
    leftover = re.findall(r'trainity_c18|trainity_c17|Date_MASTER-C18|Date_MASTER-C17', body)
    print('  leftover c18/c17 storage/file tokens in BODY (trebuie 0):', len(leftover), leftover[:8])
    # garda contaminare C18 ca IDENTITATE: "automatiz" doar in anomaly-card granita + ba-after (callback), nu ca identitate
    autom = re.findall(r'automatiz', body, re.IGNORECASE)
    print('  "automatiz" in BODY (doar granita C18/callback, verifica context):', len(autom))
    # garda contaminare C17 ca identitate
    sist = re.findall(r'sistematiz|_SISTEM\b', body, re.IGNORECASE)
    print('  "sistematiz/_SISTEM" in BODY (doar system-map eticheta vecina):', len(sist))
    # artefact corect
    print('  "_GUVERNARE" in BODY:', body.count('_GUVERNARE'))
    print('  "_AUTOMATIZARE" in BODY (trebuie 0):', body.count('_AUTOMATIZARE'))
    # garda anti-em-dash pe TOT out
    for ch, nm in [('—', 'em-dash'), ('–', 'en-dash')]:
        n = out.count(ch)
        print('  ', nm, 'in OUT (trebuie 0):', n)
    # slots locked verbatim
    locked = {
        'HERO': 'Cum se ține corect fără ochiul meu?',
        'BOMBA': 'Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.',
        'MANTRA': 'Nu o supraveghez. O guvernez prin reguli.',
        'WOW': 'Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.',
        'MOTTO': 'Pleci, și munca se ține singură.',
        'GRESEALA': 'Confunzi «merge» cu «merge corect».',
        'AHA': 'Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.',
        'HOV-OBJECT': 'GUVERNAREA SISTEMULUI PRIN REGULI',
    }
    for k, v in locked.items():
        print('  LOCK', k, ':', out.count(v))
    # 6 titluri de etapa
    etape = [
        'Sistemul care merge doar cât te uiți',
        'Ce poate să devieze previzibil',
        'Regula care prinde intrarea greșită',
        'Pragul și semnalul',
        'Excepția și oprirea controlată',
        'Testul ochilor închiși',
    ]
    for t in etape:
        print('  ETAPA:', out.count(t), '|', t)
    # arc obligatoriu
    arc = ['respinsă la sursă', 'aprinde ATENȚIE', 'STATUS', 'listă de excepții', 'opr', 'ochilor închiși']
    print('  arc prezent:', all(a.lower() in out.lower() for a in arc))
    print('  steps:', body.count('data-step="'), '| stages:', body.count('id="stage-'),
          '| anomaly:', body.count('anomaly-card'), '| final-card:', body.count('final-card'),
          '| prompturi:', body.count('prompt-box'))
    print('  localStorage in tail:', 'trainity_c19_study_v1' in tail)


if __name__ == '__main__':
    main()
