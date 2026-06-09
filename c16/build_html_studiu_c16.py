#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c16.py - HTML-Studiu-Excel-16-Livrare.html prin COPY+MODIFY din c14.

Strategie (ca la C13 din C12): pastrez head+CSS si JS din c14 (generice), inlocuiesc
DOAR blocul <body>..<script> cu narativ C16 LIVRARE. Patch title + STORAGE_KEY + hero.

Axa C16: RAPORT DECISION-READY. C16 = foaie-raport de decizie (raportul devine obiect
de decizie). Pilon T4: T4 consuma raspunsul produs de T3, nu il naste.
Garda: zero sinteza de mesaj ca identitate (=C15), zero layout/dashboard (=C14),
zero sistem recurent/automatizare (=C17), zero logistica (email/export/share),
zero cifre business statice (R-V02.15). 18 step-titles din SPEC_NARATIV_MA_REVIZUIT.
"""
import re, os

SRC = 'c14/HTML-Studiu-Excel-14-Compunere.html'
OUT = 'c16/HTML-Studiu-Excel-16-Livrare.html'

HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>DECIZIA GATA</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C16 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C16 · Livrare</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Livrare C16: un raport complet, cu mesajul sintetizat, capata forma de decizie si devine un obiect din care decidentul poate hotari">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C16</span><span class="hov-object">LIVRARE</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cum dau raportului forma care îl face o decizie gata de luat, nu doar informație trimisă?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 4">
            <span class="sm-step">VIZUALIZARE</span><span class="sm-arrow">·</span><span class="sm-step">COMPUNERE</span><span class="sm-arrow">·</span><span class="sm-step">SINTETIZARE</span><span class="sm-arrow">·</span><span class="sm-step active">LIVRARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <p class="hero-microbrief">Analiza a dat răspunsul, iar treapta dinainte a sintetizat mesajul esențial. Dar raportul, oricât de complet, stă pe loc: decidentul tot nu hotărăște. Înainte să producă o decizie, raportul are nevoie de o formă finală. Și forma nu e neutră: un raport care nu produce o decizie nu e livrat, e doar trimis.</p>
        <div class="cover-miza">C16 nu descoperă răspunsul și nu îl re-sintetizează: îl primește gata și îl face decizie. Aici raportul capătă forma de decizie: concluzia cerută în prima linie, cadrul de decizie explicit, detaliul în anexă, totul predabil fără autor lângă. Nu un document frumos, un obiect de decizie din care decidentul poate hotărî. C16 livrează decizia gata; sistematizarea recurentă a raportului începe la treapta următoare.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">Raportul e gata.</span> <span class="ib-2">Decizia, nu.</span></p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Ai răspunsul, e și sintetizat, și un raport care arată complet. Și totuși:</p>
        <ul class="tu-list">
          <li>raportul conține concluzia, dar decidentul tot cere lămuriri înainte să hotărască</li>
          <li>trimiți raportul și aștepți o decizie care nu vine, sau vine târziu</li>
          <li>fără tine lângă el, raportul nu se înțelege și nu se decide singur</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Oamenii trimit rapoarte.<br><span class="tu-hl">Profesioniștii livrează decizii.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Un raport care nu produce o decizie nu e livrat, e doar trimis.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai predai un teanc de date. <span class="tu-hl">Predai o decizie gata de luat.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>un raport complet, dar care nu mișcă decizia</li><li>concluzia îngropată undeva la pagina paisprezece</li><li>riscul lăsat pe seama decidentului, să-l deducă</li><li>un raport care are nevoie de autor lângă el</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>un raport care produce o decizie de luat</li><li>concluzia cerută stă în prima linie a foii</li><li>cadrul de decizie scris explicit, cu prag</li><li>o foaie care se susține și se decide singură</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>cadrul de decizie: decizie, risc, concluzie, pas următor</li><li>o foaie-raport de decizie care stă în picioare singură</li><li>un raport predabil ca obiect de decizie, nu ca document</li><li>decizia gata de luat, predată treptei următoare</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Nu livrez informație. <mark>Livrez o decizie gata de luat.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CELE ȘASE FELURI ÎN CARE UN RAPORT RĂMÂNE INFORMAȚIE, NU DECIZIE</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">CONCLUZIA ÎNGROPATĂ</b><p class="anomaly-desc">Concluzia relevantă stă undeva în tabel, la pagina paisprezece, nu în capul foii. Corecția: concluzia cerută urcă în prima linie, ca decizie de luat.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">DETALIUL CARE AGLOMEREAZĂ</b><p class="anomaly-desc">Tot detaliul brut, linie cu linie, sufocă decizia în context. Corecția: detaliul coboară în anexă, iar sus rămâne agregatul de decizie.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">LIPSA CADRULUI</b><p class="anomaly-desc">Doar cifre, fără decizie, risc, concluzie și pas următor: e informație, nu decizie. Corecția: se adaugă cadrul de decizie, explicit.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">RISCUL IMPLICIT</b><p class="anomaly-desc">Riscul e lăsat pe seama decidentului, să-l deducă din cifre. Corecția: riscul se scrie, cu pragul lui declarat.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">OPRIT LA CONSTATARE</b><p class="anomaly-desc">Raportul se termină în „asta e situația", fără nicio acțiune propusă. Corecția: se scrie pasul următor, ancorat în date.</p></div>
<div class="anomaly-card"><span class="anomaly-num">06</span><b class="anomaly-title">NEVOIE DE AUTOR</b><p class="anomaly-desc">Fără unitate, perioadă și referință, raportul cere autorul lângă el ca să fie citit. Corecția: fiecare cifră poartă unitate, perioadă și referință.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · RAPORTUL CARE NU MIȘCĂ</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Mesajul e sintetizat, raportul e complet. Înainte de orice formă de decizie, confirmi că pleci de la mesajul primit, nu îl refaci.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Mesajul sintetizat, dar încă nu o decizie</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C16-Livrare.xlsx. <span data-locked="1">Vine cu mesajul esențial, sintetizat în treapta dinainte, și cu rezultatul corect.</span> E adevărat, e clar, dar e încă informație: nu spune ce se decide. Înainte de orice formă, ai un mesaj care nu mișcă.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Raportul plin, iar decidentul tot întreabă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui raportul complet în fața cuiva care trebuie să hotărască. Tot întreabă: „și ce fac cu asta?". Raportul are tot, dar nu are decizia. Lipsa nu e de informație, e de formă de decizie.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Aceeași informație, încă fără cadru de decizie</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Iei mesajul și rezultatul. <span data-locked="1">Nu le re-sintetizezi și nu cauți altă concluzie: mesajul vine gata, tu îi dai forma de decizie.</span> Sarcina nu e să spui altceva, e să faci din ce e deja clar o decizie de luat.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · CE CERE DECIZIA</div>
      <h2 class="stage-name">INVESTIGAȚIE</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să construiești foaia, descoperi ce-i trebuie unui decident concret ca să hotărască și ce din raport e zgomot pentru decizie.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Ce decizie se cere, de fapt, din acest raport</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te întrebi nu „ce conține raportul?", ci „ce hotărâre se ia din el?". Descoperi că o parte din raport servește decizia, iar restul e context. Decizia cerută nu e dată de cifre, e numită de tine.</p>

  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Promptul 1: ce-i trebuie decidentului ca să decidă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 1. Pentru un decident concret, AI-ul propune ce decizie se cere, ce risc o însoțește și ce informație e relevantă față de ce e zgomot. Nu construiești încă; afli ce-i trebuie decidentului. AI propune, tu judeci ce intră în decizie.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · CE-I TREBUIE DECIDENTULUI CA SĂ DECIDĂ</div>
      <div class="prompt-text">Am un raport cu un mesaj esențial deja sintetizat și un rezultat corect. Pentru un decident concret, spune-mi ce decizie se cere de fapt din acest raport, ce risc o însoțește și ce informație e relevantă pentru decizie față de ce e zgomot. Propune o listă, dar nu hotărî tu; eu judec ce intră în decizie. Nu re-sintetiza mesajul și nu căuta concluzii noi; lucrează doar cu încadrarea pentru decizie. Nu compune pagina și nu propune un raport recurent.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Ce e semnal pentru decizie, ce e zgomot</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci raportul prin filtrul deciziei: ce susține hotărârea rămâne sus, ce e doar context coboară. Aici vezi diferența pe viu: aceleași date, dar o parte e semnal pentru decizie, restul e zgomot care aglomerează.</p>
    <div class="section-sublabel">RAPORT AI · CE SUSȚINE DECIZIA</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">semnal</div>
      <div class="inv-item-body">
        <div class="inv-item-label">DECIZIA CERUTĂ · CE SE HOTĂRĂȘTE</div>
        <div class="inv-item-desc">Întrebarea de decizie pe care raportul trebuie să o închidă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">semnal</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CONCLUZIA · CE SUSȚINE DECIZIA</div>
        <div class="inv-item-desc">Mesajul esențial, poziționat ca temei al hotărârii.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">semnal</div>
      <div class="inv-item-body">
        <div class="inv-item-label">RISCUL · CE O POATE STRICA</div>
        <div class="inv-item-desc">Pragul și expunerea care contează pentru hotărâre.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">zgomot</div>
      <div class="inv-item-body">
        <div class="inv-item-label">DETALIUL EXHAUSTIV · CE AGLOMEREAZĂ</div>
        <div class="inv-item-desc">Fiecare rând și fiecare factură: context, nu decizie.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">zgomot</div>
      <div class="inv-item-body">
        <div class="inv-item-label">DRUMUL · CE NU SE HOTĂRĂȘTE</div>
        <div class="inv-item-desc">Cum s-a ajuns la rezultat: anexă, nu cap de foaie.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">zgomot</div>
      <div class="inv-item-body">
        <div class="inv-item-label">ORNAMENTUL · CE NU MIȘCĂ DECIZIA</div>
        <div class="inv-item-desc">Tot ce arată bine, dar nu schimbă hotărârea.</div>
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
      <div class="stage-label">ETAPA 3 · CONSTRUIEȘTI CADRUL DE DECIZIE</div>
      <h2 class="stage-name">TRANSFORMARE</h2>
      <div class="stage-tags"><span class="phase-tag">FORMĂ</span><span class="type-tag">Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Aici raportul capătă forma de decizie: concluzia urcă în cap, cadrul de decizie se scrie, detaliul coboară în anexă.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Concluzia urcă în capul foii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Iei concluzia cerută și o pui în prima linie a foii, ca decizie de luat. <span data-locked="1">Nu o re-formulezi, o poziționezi.</span> Decidentul citește decizia înainte de drumul către ea, nu invers.</p>

  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Promptul 2: construiești cadrul decizie, risc, concluzie, pas următor</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2. AI-ul propune structura foii, tu o corectezi: decizia de luat sus, riscul cu pragul lui, concluzia și pasul următor. AI-ul așază repede; pragul de risc și acțiunea le pui tu. Raportul trece de la „informație completă" la „decizie de luat".</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · CONSTRUIEȘTI CADRUL DE DECIZIE</div>
      <div class="prompt-text">Construiește o foaie-raport de decizie pornind de la mesajul și agregatul date. Pune în capul foii cadrul de decizie: decizia de luat, riscul cu pragul lui, concluzia și pasul următor. Coboară detaliul brut în anexă. Apoi verifică: fiecare cifră are unitate, perioadă și referință, iar foaia se citește fără autor lângă ea. Nu aranja vizual pagina și nu adăuga un dashboard; nu automatiza un flux recurent. Rămâi la o singură foaie-raport de decizie.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Detaliul exhaustiv coboară în anexă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Muți detaliul brut, linie cu linie, jos în anexă. <span data-locked="1">Sus rămâne agregatul care susține decizia; jos stă proba, la nevoie.</span> Ce nu intră în decizie nu dispare, dar nu mai aglomerează capul foii.</p>
    <div class="section-sublabel">DOVADA TRANSFORMĂRII</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Concluzia</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">îngropată în tabel</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">în prima linie, ca decizie</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Detaliul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">tot în capul foii</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">în anexă, agregatul sus</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Cadrul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">doar cifre, fără ramă</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">decizie, risc, concluzie, pas</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Riscul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">lăsat de dedus</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">scris, cu pragul lui</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Raportul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">informație care nu mișcă</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">obiect de decizie</span></div>
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
      <div class="stage-label">ETAPA 4 · FOAIA SE SUSȚINE SINGURĂ</div>
      <h2 class="stage-name">VERIFICARE</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Probă</span></div>
    </div>
  </header>
  <p class="stage-quote">Testezi raportul ca obiect de decizie: poate decidentul hotărî doar din foaie, fără tine lângă?</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Poate decidentul hotărî doar din foaie?</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui foaia în fața decidentului și pleci. Dacă poate hotărî doar din ea, raportul e obiect de decizie. Dacă te cheamă înapoi pentru context de bază, încă e informație, nu decizie.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Testul fără autor: întrebările inevitabile, nu întrebările de bază</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Asculți ce întrebări apar. <span data-locked="1">Întrebările de bază („ce e asta?", „pe ce perioadă?") sunt vina formei și se elimină.</span> Rămân doar întrebările inevitabile de decizie, despre compromisuri și priorități. Acelea sunt sănătoase, nu lipsuri.</p>

  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Riscul și pasul următor, scrise explicit, nu deduse</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Verifici că riscul e scris, cu pragul lui, și că pasul următor e o acțiune, nu o constatare. Nimic lăsat de dedus. Decidentul nu reconstruiește raționamentul, citește decizia.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · REGULA, NU INSPIRAȚIA</div>
      <h2 class="stage-name">STABILIZARE</h2>
      <div class="stage-tags"><span class="phase-tag">ANCORARE</span><span class="type-tag">Reguli</span></div>
    </div>
  </header>
  <p class="stage-quote">Fixezi foaia-raport de decizie în reguli, ca să fie repetabilă, completă și fără surplus.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Cele șase reguli ale foii-raport de decizie</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci raportul prin cele șase reguli: concluzia în cap, cadrul de decizie, detaliul în anexă, riscul scris, pasul următor, fiecare cifră cu referință. Ce trece e decision-ready; ce nu trece, se corectează până trece.</p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Complet pentru decizie, fără surplus</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Tai din capul foii tot ce nu intră în decizie. <span data-locked="1">Complet nu înseamnă tot ce ai, înseamnă cât îi trebuie decidentului.</span> Surplusul coboară în anexă sau dispare. Rămâne exact decizia și ce o susține.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">O foaie-raport de decizie care stă în picioare singură</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Rezultatul etapei e o foaie care se citește și se decide fără autorul lângă ea. Vine alt raport din aceeași natură: aplici aceleași reguli și obții aceeași formă de decizie. Forma e repetabilă, nu o reușită de moment.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-6" data-stage="6" data-stage-ghost="06">
  <header class="stage-header">
    <div class="stage-number">06</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 6 · DECIZIA PREDATĂ</div>
      <h2 class="stage-name">CONFIRMARE</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Handoff T5</span></div>
    </div>
  </header>
  <p class="stage-quote">Forma de decizie scurtează drumul spre hotărâre. Devii cel care predă o decizie, nu un document, și o dai mai departe.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">Forma de decizie scurtează drumul spre hotărâre</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui față în față raportul-informație și raportul-decizie. Cu cadrul de decizie, hotărârea care lua o ședință se ia dintr-o citire. Aceeași informație, dar forma de decizie a scurtat drumul spre hotărâre.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Devii cel care predă o decizie, nu un teanc de date</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Nu mai întrebi „am trimis raportul?", ci „am livrat o decizie?". <span data-locked="1">Ești ultimul filtru între un mesaj corect și un decident care trebuie să acționeze.</span> Nu mai predai date, predai o decizie gata de luat.</p>

  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Raportul-decizie este gata, treapta următoare îl poate sistematiza</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">C16 face raportul o decizie. Treapta următoare îl face să ruleze singur.</span> Predai o foaie-raport de decizie completă, self-standing. Sistematizarea recurentă, automatizarea și guvernarea încep la treapta de autonomie. Tu ai garantat că raportul produce o decizie.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda raportul-decizie treptei următoare, confirmi fiecare invariant al livrării decision-ready. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">CONTROL</div><div class="final-text">Date_MASTER-C16-Livrare.xlsx deschis. Mesajul sintetizat în treapta dinainte este preluat ca atare.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">MESAJ PRELUAT</div><div class="final-text">Forma servește un mesaj venit gata. Zero re-sinteză, zero concluzii noi inventate.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">CONCLUZIA ÎN CAP</div><div class="final-text">Decizia cerută stă în prima linie a foii, nu îngropată la pagina paisprezece.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">CADRU DE DECIZIE</div><div class="final-text">Decizie, risc, concluzie și pas următor: toate explicite, niciunul lăsat de dedus.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">COMPLET FĂRĂ SURPLUS</div><div class="final-text">În capul foii, cât îi trebuie decidentului, nu tot ce ai. Restul în anexă.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">RISC ȘI PAS</div><div class="final-text">Riscul scris, cu pragul lui. Pasul următor e o acțiune, nu o constatare.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">SE SUSȚINE SINGUR</div><div class="final-text">Fiecare cifră poartă unitate, perioadă și referință. Citit fără autor lângă.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">OBIECT DE DECIZIE</div><div class="final-text">Citit o dată, raportul produce o decizie. Gata de predat la treapta de autonomie.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Raport decision-ready.</div>
          <div class="completion-subtitle">Fiecare raport produce o decizie. Gata de sistematizat la treapta următoare.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 5 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C17 · Sistematizarea</h3>
        <p class="next-desc">Ai o foaie-raport de decizie, completă și self-standing. Dar cum o faci să ruleze singură, recurent, fără s-o reconstruiești de fiecare dată? Sistematizarea raportului, automatizarea și autonomia încep la C17, în treapta de autonomie.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Mesajul era corect și sintetizat din treapta dinainte.</div>
        <div class="payoff-line accent">Dar raportul, oricât de complet, rămânea informație: decidentul tot nu hotăra.</div>
        <div class="payoff-line regular">Acum raportul are o formă de decizie, nu de document: concluzia în cap, cadrul de decizie explicit, citit la fel de oricine, fără autor lângă.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Același raport: trimis, stătea pe loc; livrat ca decizie, se hotărăște dintr-o citire.</span></div>
        <div class="payoff-motto" data-locked="1">Raportul care decide.</div>
      </section>

      <footer class="footer">
        TRAINITY · C16 LIVRARE · raportul devine o decizie gata de luat
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

    # patch identitate in head (title) - robust prin regex
    head = re.sub(r'<title>.*?</title>', '<title>C16 · Livrare · Trainity</title>', head, count=1)
    head = re.sub(r'NEXT \(C\d+\)', 'NEXT (C16)', head)
    # patch STORAGE_KEY in tail (orice trainity_cNN_study_v1 -> c16)
    tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c16_study_v1', tail)

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c16', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # garda: tokeni sursa (c14) reziduali in CONTINUT (body)
    leftover = re.findall(r'C14|trainity_c14|Date_MASTER-C14|Compunere|COMPUNERE|COMPOZIȚIE|ordinea privirii', body)
    print('  leftover C14 tokens in BODY (trebuie 0):', len(leftover), leftover[:8])
    # garda contaminare C15/C17 ca IDENTITATE (referintele de granita/handoff sunt ok)
    c15 = re.findall(r'Sintetizare|SINTETIZARE|sintetizez', body)
    print('  C15 identity tokens in BODY (trebuie 0):', len(c15), c15[:6])

    # garda anti-em-dash in BODY
    for ch in ['—', '–']:
        if ch in body:
            print('  ATENTIE em/en-dash in BODY!')

    # verificare structura
    print('  steps:', body.count('data-step="'), '| stages:', body.count('data-stage="') - body.count('data-stage-ghost'))
    print('  fenomene anomaly-card:', body.count('anomaly-card'), '| final-card:', body.count('final-card'))
    print('  prompturi:', body.count('prompt-box'), '| step-title:', body.count('step-title'))


if __name__ == '__main__':
    main()
