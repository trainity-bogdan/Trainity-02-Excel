#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c13.py - HTML-Studiu-Excel-13-Vizualizare.html prin COPY+MODIFY din c12.

Strategie (ca la C12 din C10): pastrez head+CSS si JS din c12 (generice), inlocuiesc
DOAR blocul <body>..<script> cu narativ C13 VIZUALIZARE. Patch title + STORAGE_KEY + hero.

Axa C13: ONESTITATEA FORMEI. C13 = obiect vizual onest, NU dashboard (=C14).
Pilon T4: T4 consuma raspunsul produs de T3, nu il naste.
Garda: zero dashboard/pagina/layout/storytelling ca identitate (=C14/C15/C16),
zero 'de ce'/cauza ca identitate (=C12), zero cifre business statice (R-V02.15).
18 step-titles LOCKED, 6 fenomene LOCKED (perechi deformare->regula).
"""
import re, os

SRC = 'c12/HTML-Studiu-Excel-12-Interpretare.html'
OUT = 'c13/HTML-Studiu-Excel-13-Vizualizare.html'

HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>FORMA ADEVĂRATĂ</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C13 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C13 · VIZUAL</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Vizualizare C13: un rezultat corect produs de analiza capata o forma vizuala onesta, verificata contra cifrei brute">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C13</span><span class="hov-object">FORMA ADEVĂRATĂ</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cum dau unui rezultat forma care îl face adevărat și vizibil dintr-o privire?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 4">
            <span class="sm-step active">VIZUALIZARE</span><span class="sm-arrow">·</span><span class="sm-step">COMPUNERE</span><span class="sm-arrow">·</span><span class="sm-step">SINTETIZARE</span><span class="sm-arrow">·</span><span class="sm-step">LIVRARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title">Cum să dai unui rezultat o formă care nu minte</h1>
        <p class="hero-microbrief">Analiza a dat răspunsul: un rezultat corect, citit din model. Dar răspunsul trăiește în model, mut pentru oricine altcineva. Un decident nu hotărăște privind un Power Pivot. Înainte să fie văzut, rezultatul are nevoie de o formă. Și forma nu e neutră: aceeași cifră, desenată altfel, spune altceva.</p>
        <div class="cover-miza">C13 nu descoperă răspunsul, îl primește de la analiză și îl face vizibil pentru decizie. Aici un rezultat corect capătă forma vizuală care îl arată adevărat dintr-o privire: tipul potrivit, axa onestă, scala declarată, codarea curată. Nu un grafic frumos, un obiect vizual onest, care produce aceeași concluzie ca cifra brută din care vine. C13 construiește obiectul adevărat; așezarea lui în pagină începe la treapta următoare.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">Cifra e corectă.</span> <span class="ib-2">Graficul minte.</span></p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Ai un rezultat corect și un grafic care arată bine. Și totuși:</p>
        <ul class="tu-list">
          <li>același rezultat, desenat de doi oameni, duce la două concluzii diferite</li>
          <li>graficul pare obiectiv, dar cineva a ales axa, scala și culoarea</li>
          <li>ochiul a crezut forma înainte ca cineva să verifice cifra</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Oamenii desenează frumos.<br><span class="tu-hl">Profesioniștii desenează adevărat.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Forma greșită minte cu cifra corectă.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai faci grafice. <span class="tu-hl">Răspunzi de ce vede altcineva.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>un rezultat corect, dar mut în model</li><li>o formă aleasă din reflex sau din default</li><li>o axă care exagerează o diferență minusculă</li><li>un grafic care spune mai mult decât cifra</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>un obiect vizual care arată rezultatul adevărat</li><li>o formă aleasă, nu nimerită</li><li>axă, scală și codare oneste</li><li>un vizual care dă aceeași concluzie ca cifra brută</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>forma vizuală potrivită naturii rezultatului</li><li>cele șase reguli de onestitate a formei</li><li>un vizual verificat contra cifrei brute</li><li>un obiect vizual onest, gata de predat treptei următoare</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Nu desenez frumos. <mark>Desenez adevărat.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CELE ȘASE FELURI ÎN CARE FORMA DEFORMEAZĂ ADEVĂRUL</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">AXA CARE EXAGEREAZĂ</b><p class="anomaly-desc">Axa nu pleacă de la zero și o diferență minusculă pare o prăpastie. Corecția: axa pleacă de la zero, sau abaterea e declarată explicit.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">TIPUL NEPOTRIVIT</b><p class="anomaly-desc">O evoluție pusă în plăcintă, niște categorii puse în linie: forma contrazice natura datelor. Corecția: tipul urmează natura rezultatului.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">SCALA CARE INVENTEAZĂ</b><p class="anomaly-desc">O a doua axă sau o scală nedeclarată creează o corelație care nu există. Corecția: o singură scală liniară, declarată.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">CODAREA CARE SUGEREAZĂ</b><p class="anomaly-desc">3D, gradient sau arie dublă fac ochiul să citească o tendință inexistentă. Corecția: o singură dimensiune codată coerent.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">AGREGAREA CARE ASCUNDE</b><p class="anomaly-desc">Media netezește tot și ascunde variația care era mesajul. Corecția: arăți distribuția, nu doar media.</p></div>
<div class="anomaly-card"><span class="anomaly-num">06</span><b class="anomaly-title">ETICHETA LIPSĂ</b><p class="anomaly-desc">Fără unitate, etichetă sau context, cititorul ghicește ce vede. Corecția: fiecare vizual poartă unitate, etichetă și context.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · RĂSPUNSUL FĂRĂ FORMĂ</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Analiza a dat răspunsul, corect, dar invizibil. Înainte de orice formă, confirmi că rezultatul vine de la analiză și că lui îi dai formă, nu altuia.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Răspunsul corect, dar invizibil</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C13-Vizualizare.xlsx. <span data-locked="1">Vine cu răspunsul produs de analiză: rezultatul corect, citit din model.</span> E adevărat, dar trăiește în model, sub formă de cifre și tabele. Corect nu înseamnă văzut. Înainte de orice grafic, ai un răspuns care nu se vede.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Nimeni nu decide privind un model</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui modelul în fața cuiva care trebuie să hotărască. Nu poate. Un decident nu citește un Power Pivot, nu parcurge un tabel ca să decidă dintr-o privire. Răspunsul e corect și mut în același timp. Lipsa nu e de analiză, e de formă.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Aceeași cifră, încă fără formă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Iei un singur rezultat din răspuns. <span data-locked="1">Nu îl re-analizezi și nu cauți altă cauză: răspunsul vine de la analiză, tu doar îi dai formă.</span> Atât. Sarcina ta nu e să afli ceva nou, e să faci vizibil ce e deja adevărat, fără să strici.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · FORMA E O ALEGERE</div>
      <h2 class="stage-name">INVESTIGAȚIE</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să desenezi, descoperi că aceeași cifră are mai multe forme și că forma greșită schimbă concluzia.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">O cifră, mai multe forme posibile</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Iei rezultatul și încerci să-l arăți. Descoperi imediat că nu există o singură formă: bară, linie, plăcintă, număr mare, tabel. Aceeași cifră intră în multe forme, iar fiecare spune ceva în plus. Forma nu e dată de cifră, e aleasă de tine.</p>

  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Promptul 1: ce formă cere rezultatul</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 1. Pentru tipul de rezultat pe care îl ai, AI-ul propune forma care i se potrivește și te avertizează ce forme l-ar deforma. Nu desenezi încă; afli ce formă cere natura rezultatului. AI propune, tu judeci dacă forma spune adevărul.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · CE FORMĂ CERE REZULTATUL</div>
      <div class="prompt-text">Am un rezultat produs de analiză (o comparație, o evoluție, o parte dintr-un total sau o relație). Spune-mi ce tip de reprezentare i se potrivește naturii lui, ce tipuri l-ar deforma și de ce, și ce reguli de axă și scală țin forma onestă. Nu inventa rezultate noi și nu explica de ce apare rezultatul; lucrează doar cu forma care îl face vizibil corect. Nu compune o pagină și nu propune un dashboard.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Aceeași cifră, două grafice, două concluzii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Desenezi același rezultat în două forme: una cu axa de la zero, una cu axa trunchiată. Aceeași cifră, două imagini, două concluzii opuse. Aici vezi minciuna de formă pe viu: nu cifra s-a schimbat, ci forma. Și ochiul a crezut forma.</p>
    <div class="section-sublabel">RAPORT AI · CE FORMĂ SPUNE ADEVĂRUL</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">onest</div>
      <div class="inv-item-body">
        <div class="inv-item-label">NATURA REZULTATULUI · CE ARATĂ</div>
        <div class="inv-item-desc">Comparație, evoluție, parte din tot sau relație: natura decide forma potrivită.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">onest</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FORMA POTRIVITĂ · CE O ARATĂ ADEVĂRAT</div>
        <div class="inv-item-desc">Tipul de reprezentare pe care AI-ul îl propune fiindcă urmează natura rezultatului.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">onest</div>
      <div class="inv-item-body">
        <div class="inv-item-label">REGULA DE AXĂ · CE ȚINE ONESTITATEA</div>
        <div class="inv-item-desc">Axa de la zero sau abaterea declarată: regula care împiedică exagerarea.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">minte</div>
      <div class="inv-item-body">
        <div class="inv-item-label">AXA TRUNCHIATĂ · CE EXAGEREAZĂ</div>
        <div class="inv-item-desc">Forma care umflă o diferență minusculă: aceeași cifră, altă concluzie.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">minte</div>
      <div class="inv-item-body">
        <div class="inv-item-label">TIPUL NEPOTRIVIT · CE CONTRAZICE NATURA</div>
        <div class="inv-item-desc">Forma care nu urmează natura rezultatului: o evoluție pusă în plăcintă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">minte</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CODAREA CARE SUGEREAZĂ · CE INVENTEAZĂ</div>
        <div class="inv-item-desc">3D, gradient sau scală dublă: efecte care adaugă o tendință inexistentă.</div>
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
      <div class="stage-label">ETAPA 3 · DAI FORMA ONESTĂ</div>
      <h2 class="stage-name">TRANSFORMARE</h2>
      <div class="stage-tags"><span class="phase-tag">FORMĂ</span><span class="type-tag">Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Aici rezultatul capătă forma onestă: tipul urmează natura, axa și scala se corectează, codarea care minte se scoate.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Tipul de grafic urmează natura rezultatului</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Alegi tipul după natura rezultatului, nu după gust. <span data-locked="1">Categorii în bare, evoluție în linie, parte din tot în structură, relație în puncte.</span> Forma nu se nimerește, se alege. Tipul potrivit e cel care arată rezultatul așa cum este, fără să adauge.</p>

  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Promptul 2: generezi vizualul, corectezi axa și scala</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2. AI-ul generează vizualul, tu îl corectezi: axa pleacă de la zero, scala e una singură și liniară, unitatea e pe axă. AI-ul desenează repede; onestitatea o pui tu. Forma trece de la „arată bine" la „arată adevărat".</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · GENEREZI VIZUALUL, CORECTEZI AXA ȘI SCALA</div>
      <div class="prompt-text">Generează vizualul pentru rezultatul ales, în tipul potrivit naturii lui. Apoi verifică și corectează: axa pleacă de la zero sau abaterea e declarată, scala e una singură și liniară, unitatea și eticheta sunt prezente, iar codarea reprezintă o singură dimensiune (fără 3D, gradient sau arie dublă). Nu adăuga un al doilea vizual și nu așeza pagina; rămâi la un singur obiect vizual onest. Nu formula mesajul și nu trece la livrare.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Scoți codarea care sugerează fals</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci peste vizual și scoți tot ce sugerează o tendință care nu există: 3D, gradient care urcă, arie dublă, culoare care insinuează. <span data-locked="1">O formă onestă codează o singură dimensiune coerent.</span> Ce rămâne arată rezultatul, nu o poveste despre el.</p>
    <div class="section-sublabel">DOVADA TRANSFORMĂRII</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Tipul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">ales din reflex</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">urmează natura rezultatului</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Axa</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">trunchiată, exagerează</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">de la zero sau declarată</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Scala</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">dublă, inventează relații</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">una singură, liniară, declarată</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Codarea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">3D și gradient care sugerează</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">o singură dimensiune coerentă</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Rezultatul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">corect, dar invizibil</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">obiect vizual onest</span></div>
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
      <div class="stage-label">ETAPA 4 · VERIFICAREA FORMEI</div>
      <h2 class="stage-name">VERIFICARE</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Față în față cu cifra</span></div>
    </div>
  </header>
  <p class="stage-quote">O formă onestă produce aceeași concluzie ca cifra brută și rezistă unui al doilea ochi. Verifici fiecare.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Vizualul față de cifra brută: aceeași concluzie?</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui vizualul lângă cifra din care vine. Citești concluzia din grafic, apoi din număr. Dacă sunt aceeași, forma e onestă. <span data-locked="1">Dacă graficul spune mai mult sau altceva decât cifra, forma minte.</span> Confrunți, nu construiești nimic nou aici.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Testul celui de-al doilea ochi</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Dai vizualul cuiva care vede doar graficul, fără tine lângă el și fără cifra. Ce concluzie trage? Dacă e aceeași cu a cifrei brute, forma trece. Un grafic onest nu are nevoie de autor lângă el ca să fie citit corect.</p>

  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Marchezi forma care spune mai mult decât cifra</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci fiecare vizual prin cele șase întrebări de onestitate. Cele care adaugă o concluzie pe care cifra nu o susține le marchezi ca neoneste și le corectezi sau le scoți. O formă care spune mai mult decât cifra nu rămâne în set, oricât de bine arată.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · FORMA DEVINE REGULĂ</div>
      <h2 class="stage-name">STABILIZARE</h2>
      <div class="stage-tags"><span class="phase-tag">ANCORARE</span><span class="type-tag">Reguli repetabile</span></div>
    </div>
  </header>
  <p class="stage-quote">Onestitatea nu e un noroc de o dată. O fixezi în reguli, ca orice vizual următor să se nască onest.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Cele șase reguli de onestitate a formei</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Fixezi regulile ca standard: axă de la zero, tip după natură, o singură scală declarată, o singură dimensiune codată, distribuția nu doar media, etichetă și unitate prezente. <span data-locked="1">Cele șase reguli nu sunt o listă de greșeli, sunt felul în care construiești.</span></p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Eticheta, unitatea, contextul: nimic de ghicit</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci peste vizual și elimini orice loc unde cititorul ar trebui să ghicească: pui unitatea, eticheta axelor, perioada, sursa. Un obiect vizual onest se citește singur. Contextul nu e decor, e parte din adevăr: fără el, aceeași formă poate spune lucruri diferite.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">Un obiect vizual onest, repetabil</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Rezultatul etapei e un obiect vizual onest, construit pe reguli, nu pe inspirație. Vine un rezultat nou din aceeași natură: aplici aceleași reguli și obții un vizual la fel de onest. Forma e acum repetabilă, nu o reușită de moment.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-6" data-stage="6" data-stage-ghost="06">
  <header class="stage-header">
    <div class="stage-number">06</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 6 · OBIECTUL ADEVĂRAT</div>
      <h2 class="stage-name">CONFIRMARE</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Handoff C14</span></div>
    </div>
  </header>
  <p class="stage-quote">Forma onestă repară percepția. Devii garantul a ceea ce vede altcineva și predai obiectul mai departe.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">Forma onestă repară percepția</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui față în față forma care mințea și forma onestă a aceluiași rezultat. Concluzia greșită se corectează singură: ochiul care credea prăpastia vede acum diferența reală. Aceeași cifră, dar forma adevărată a reparat percepția.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Devii garantul a ceea ce vede altcineva</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Nu mai întrebi „ce grafic arată mai bine?", ci „ce grafic arată adevărat?". <span data-locked="1">Ești ultimul filtru între un rezultat corect și un ochi care îl va crede pe loc.</span> Nu mai faci grafice ca să ilustrezi: răspunzi de ce vede altcineva.</p>

  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Predai către C14: obiectul, gata de așezat în pagină</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">C13 face obiectul adevărat. C14 îl așază în pagină.</span> Predai un obiect vizual onest, verificat contra cifrei și complet etichetat. Organizarea mai multor astfel de obiecte într-o pagină, ierarhia și ce vede ochiul întâi încep la treapta următoare. Tu ai garantat că obiectul nu minte.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda obiectul vizual treptei următoare, confirmi fiecare invariant al onestității formei. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">CONTROL</div><div class="final-text">Date_MASTER-C13-Vizualizare.xlsx deschis. Răspunsul produs de analiză este corect și preluat ca atare.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">RĂSPUNS PRELUAT</div><div class="final-text">Forma servește un rezultat venit de la analiză. Zero rezultate noi inventate, zero explicații de „de ce".</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">AXĂ</div><div class="final-text">Axa pleacă de la zero, sau abaterea e declarată explicit. Nicio diferență umflată.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">TIP</div><div class="final-text">Tipul de formă urmează natura rezultatului. Nicio evoluție în plăcintă, nicio categorie în linie.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">SCALĂ</div><div class="final-text">O singură scală liniară, declarată. Nicio axă dublă, niciun log ascuns.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">CODARE</div><div class="final-text">O singură dimensiune codată coerent. Fără 3D, gradient sau arie care sugerează fals.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">ETICHETĂ</div><div class="final-text">Unitate, etichetă și context prezente. Nimic lăsat de ghicit cititorului.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">AL DOILEA OCHI</div><div class="final-text">Citit singur, vizualul produce aceeași concluzie ca cifra brută. Obiect onest, gata de predat la C14.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Obiect vizual onest.</div>
          <div class="completion-subtitle">Fiecare formă verificată contra cifrei brute. Gata de așezat în pagină la C14.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 4 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C14 · Compunerea</h3>
        <p class="next-desc">Ai obiecte vizuale oneste, fiecare adevărat singur. Dar cum le așezi într-o pagină pe care decidentul o parcurge dintr-o privire? Organizarea spațială a obiectelor, ierarhia și fluxul încep la C14, în treapta de raportare.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Cifra era corectă de la analiză.</div>
        <div class="payoff-line accent">Dar forma greșită o făcea să mintă, fără să schimbe un singur număr.</div>
        <div class="payoff-line regular">Acum rezultatul are o formă aleasă, nu nimerită: verificată contra cifrei brute, citită la fel de oricine.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Aceeași cifră, două grafice, două concluzii opuse. Apoi forma onestă repară percepția.</span></div>
        <div class="payoff-motto" data-locked="1">Forma nu se nimerește. Se alege.</div>
      </section>

      <footer class="footer">
        TRAINITY · C13 VIZUALIZARE · forma onestă a unui rezultat, verificată contra cifrei
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
<a class="nav-item" data-nav-stage="2" href="#stage-2" onclick="navigateStage(2,event)"><span class="nav-item-num">2</span><span class="nav-item-text"><span class="nav-item-name">INVESTIGAȚIE</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">TRANSFORMARE</span><span class="nav-item-meta">3 pași · Formă</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">VERIFICARE</span><span class="nav-item-meta">3 pași · Control</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">STABILIZARE</span><span class="nav-item-meta">3 pași · Ancorare</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">CONFIRMARE</span><span class="nav-item-meta">3 pași · Handoff</span></span></a></div>

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
    tail = ''.join(lines[script_idx:])  # <script> ... </html>

    # patch identitate in head
    head = head.replace('<title>C12 · Interpretare · Trainity</title>',
                        '<title>C13 · Vizualizare · Trainity</title>')
    head = head.replace('/* ============ NEXT (C12) ============ */',
                        '/* ============ NEXT (C13) ============ */')
    # patch STORAGE_KEY in tail
    tail = tail.replace('trainity_c12_study_v1', 'trainity_c13_study_v1')

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c13', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # garda: tokeni C12 reziduali in CONTINUT (in afara JS/head generic)
    leftover = re.findall(r'C12|trainity_c12|Date_MASTER-C12|Interpretare|INTERPRETARE|de ce-ul', body)
    print('  leftover C12 tokens in BODY (trebuie 0):', len(leftover), leftover[:8])

    # garda anti-em-dash in BODY
    for ch in ['—', '–']:
        if ch in body:
            print('  ATENTIE em/en-dash in BODY!')

    # verificare structura
    print('  steps:', body.count('data-step="'), '| stages:', body.count('data-stage="') - body.count('data-stage-ghost'))
    print('  fenomene anomaly-card:', body.count('anomaly-card'), '| final-card:', body.count('final-card'))
    print('  prompturi:', body.count('prompt-box'))


if __name__ == '__main__':
    main()
