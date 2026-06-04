#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c12.py - HTML-Studiu-Excel-12-Interpretare.html prin COPY+MODIFY din c10.

Strategie sigura (ca la C10): pastrez head+CSS si JS din c10 (generice), inlocuiesc
DOAR blocul <body>..<script> cu narativ C12 INTERPRETARE. Patch title + STORAGE_KEY +
hero placeholder + comentariu NEXT.

Garda C12: pur 'a explica' (De ce?). Clasamentul vine ca INPUT (citit, nu produs = C11).
Zero dashboard/grafic (=T4), zero what-if/scenarii/predictie/recomandare actiune (=T5),
zero re-ierarhizare (=C11). Zero cifre business (R-V02.15). C12 INCHIDE treapta T3.
"""
import re

SRC = 'c10/HTML-Studiu-Excel-10-Masuri.html'
OUT = 'c12/HTML-Studiu-Excel-12-Interpretare.html'

HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='60' "
    "font-weight='bold'>DE CE-UL DIN DATE</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C12 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C12 · Interpretare</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Interpretare C12: un clasament corect devine o explicatie verbala, cu cauza citita din model si verificabila">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C12</span><span class="hov-object">INTERPRETARE</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">De ce? Și cum transform un rezultat numeric într-o explicație pe care o pot apăra?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 3">
            <span class="sm-step">RELAȚII</span><span class="sm-arrow">·</span><span class="sm-step">MĂSURI</span><span class="sm-arrow">·</span><span class="sm-step">COMPARAȚII</span><span class="sm-arrow">·</span><span class="sm-step active">INTERPRETARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title" data-locked="1">Cum citești cauza din spatele rezultatului</h1>
        <p class="hero-microbrief">Ai un model care răspunde, măsuri definite și un clasament clar. Știi cine conduce și cu cât diferă. Și totuși un clasament arată CARE, nu DE CE. Un director nu se oprește la „care a scăzut", întreabă imediat „de ce". O cifră adevărată fără explicație rămâne o constatare, nu o decizie.</p>
        <div class="cover-miza">Același rezultat poate avea două explicații opuse, și doar una se verifică în date. C12 este momentul în care rezultatul numeric devine explicație verbală: cauza citită din model, nu ghicită, ancorată în relații, măsuri și comparații, scrisă într-o frază pe care un om o poate înțelege, contesta și verifica. Cu C12, setul a parcurs tot drumul: corect, înțeles, interpretat.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">Știi care a crescut.</span> <span class="ib-2">Nu știi de ce.</span></p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Ai un clasament corect și un total clar. Și totuși:</p>
        <ul class="tu-list">
          <li>vezi care conduce, dar nu poți spune ce anume îl duce acolo</li>
          <li>fiecare om din ședință dă altă explicație pentru aceeași cifră</li>
          <li>explicația sună plauzibil, dar nimeni nu o poate arăta în date</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Oamenii ghicesc de ce.<br><span class="tu-hl">Profesioniștii citesc de ce, în date.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Nu rezultatul contează. Contează de ce apare rezultatul.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai citești un clasament. <span class="tu-hl">Înțelegi de ce arată așa.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>un clasament care arată CARE, fără DE CE</li><li>explicații diferite de la oameni diferiți</li><li>povești plauzibile pe care datele nu le susțin</li><li>o singură cauză forțată acolo unde lucrează mai mulți factori</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>cauza citită din model, nu ghicită</li><li>insight verbal scris într-o frază clară</li><li>explicație verificabilă înapoi în date</li><li>factorii principali identificați, fără explicație unică forțată</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>explicația rezultatului, citită din model</li><li>distincția între ce apare împreună și ce produce rezultatul</li><li>insight verbal ancorat, scris ca frază verificabilă</li><li>analiza setului închisă: treapta T3 finalizată</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Cifra spune cât. <mark>Explicația spune de ce.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CE SE ÎNTÂMPLĂ CÂND REZULTATUL NU E EXPLICAT</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">CLASAMENT FĂRĂ CAUZĂ</b><p class="anomaly-desc">Vezi care conduce și cu cât. Dar fără cauza din spate, clasamentul rămâne o constatare: arată CARE, nu spune DE CE, și nu susține o decizie.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">ÎMPREUNĂ NU ÎNSEAMNĂ DIN CAUZA</b><p class="anomaly-desc">Două lucruri cresc în același timp și pari că ai găsit cauza. Dar ce apare împreună nu explică automat ce produce rezultatul: coincidența nu e cauză.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">POVESTEA PLAUZIBILĂ</b><p class="anomaly-desc">O explicație sună perfect și toată lumea o acceptă. Dar nimeni nu o poate arăta în date: o poveste care nu se verifică în model nu e o explicație, e o presupunere.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">CAUZA UNICĂ FORȚATĂ</b><p class="anomaly-desc">Se caută un singur vinovat pentru un rezultat la care lucrează mai mulți factori. O explicație unică forțată e comodă și greșită: pierde factorii principali reali.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">CAUZA ASCUNSĂ DE TOTAL</b><p class="anomaly-desc">Totalul arată o direcție, dar cauza reală apare doar când cobori sub el, pe tăietura potrivită. Citit doar la nivel de total, rezultatul ascunde de ce s-a întâmplat.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · DESCHIDERE INTERPRETATIVĂ</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Comparațiile predate de C11 arată deja care conduce și cu cât diferă. Acum nu mai întrebi care, ci de ce: și transformi rezultatul în explicație.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Confirmi că ai model, măsuri și clasament</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C12.xlsx. <span data-locked="1">Vine cu tot lanțul treptei: modelul legat, măsurile definite și clasamentul predat de comparații.</span> Înainte de orice explicație, confirmi că rezultatul pe care vrei să-l explici este corect. O explicație construită peste un clasament greșit lămurește un lucru care nu există.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Formulezi întrebarea de business: „De ce?"</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O explicație fără întrebare e o părere. Pornești de la întrebarea reală: „de ce?". De ce conduce acela, de ce a apărut diferența, de ce arată rezultatul așa. Întrebarea decide ce cauză cauți, nu invers. Mai întâi „de ce", abia apoi căutarea în model.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Vezi că un clasament arată CARE, nu DE CE</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Clasamentul îți spune cine conduce și cu cât. Atât. Nu îți spune ce anume îl duce acolo. O constatare numerică nu este încă o explicație: lipsește cauza, citită din model, care transformă „care" în „de ce".</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · CITIRE ASISTATĂ DE AI</div>
      <h2 class="stage-name">INVESTIGAȚIE</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să dai o explicație, întrebi modelul ce cauze posibile arată datele și ce coincidențe nu sunt cauze.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Citești cauza din model, nu din presupunere</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 1. Pentru rezultatul pe care vrei să-l explici, AI-ul citește modelul și propune cauzele posibile pe care datele le susțin: ce felie, ce factor, ce tipar. Nu explici încă; afli ce cauze sunt vizibile în model, nu în intuiție.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · CITIREA CAUZEI DIN MODEL</div>
      <div class="prompt-text">Am un model cu un clasament și măsuri definite. Pentru rezultatul pe care îl indic, citește din date și spune-mi: ce cauze posibile susține modelul (ce felie, client, produs sau perioadă pare să tragă rezultatul), care dintre ele apar doar împreună fără să fie cauză, și pe ce tăietură ar trebui să cobor ca să văd cauza ascunsă de total. Rămâi la ce s-a întâmplat și de ce; nu trece la ce ar urma sau ce e de făcut. Nu modifica datele.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Separi ce apare împreună de ce produce rezultatul</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Două lucruri care cresc împreună par legate, dar coincidența nu e cauză. Testezi fiecare candidat: dacă elimini factorul, dispare rezultatul? Dacă apare și fără el? Ce apare împreună intră pe lista de verificat, nu pe lista de explicații.</p>

  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Identifici factorii principali, nu o cauză unică</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cu raportul AI în față, reții factorii pe care datele îi susțin. Un rezultat de business rar are o singură cauză: identifici factorii principali și ordinea lor, fără să forțezi o explicație unică doar pentru că e comodă.</p>
    <div class="section-sublabel">RAPORT AI · CAUZE CITITE DIN MODEL</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">cauză</div>
      <div class="inv-item-body">
        <div class="inv-item-label">ÎNTREBAREA · „DE CE?"</div>
        <div class="inv-item-desc">Întrebarea e ancora explicației: fără ea, cauza nu are direcție.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">cauză</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FACTOR PRINCIPAL · CE TRAGE REZULTATUL</div>
        <div class="inv-item-desc">Felia sau factorul pe care modelul îl arată ca motor real al rezultatului.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">cauză</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FACTOR SECUNDAR · CE CONTRIBUIE</div>
        <div class="inv-item-desc">Rezultatul rar are o singură cauză: și factorii secundari intră în explicație.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-neutral">verifică</div>
      <div class="inv-item-body">
        <div class="inv-item-label">COINCIDENȚĂ · ÎMPREUNĂ, DAR NU CAUZĂ</div>
        <div class="inv-item-desc">Ce apare împreună cu rezultatul fără să-l producă: se verifică, nu se promovează la cauză.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-neutral">verifică</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CAUZĂ ASCUNSĂ · SUB TOTAL</div>
        <div class="inv-item-desc">Tăietura pe care cauza reală devine vizibilă, deși totalul o acoperă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-neutral">verifică</div>
      <div class="inv-item-body">
        <div class="inv-item-label">NARATIV NESUSȚINUT · CE SE RESPINGE</div>
        <div class="inv-item-desc">Explicația plauzibilă pe care modelul nu o confirmă: rămâne în afara interpretării.</div>
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
      <div class="stage-label">ETAPA 3 · DE LA REZULTAT LA EXPLICAȚIE</div>
      <h2 class="stage-name">TRANSFORMARE</h2>
      <div class="stage-tags"><span class="phase-tag">INSIGHT</span><span class="type-tag">Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Aici rezultatul numeric devine explicație: cobori sub total, găsești cauza și o scrii într-o frază verificabilă.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Cobori sub total ca să găsești cauza ascunsă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2. Totalul arată direcția, dar nu cauza. Cobori pe tăietura potrivită, în foaia Interpretare: pe felie, pe perioadă, pe segment. <span data-locked="1">Cauza reală apare adesea doar sub total.</span> Citești de jos cauza pe care agregarea o ascundea.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · DE LA REZULTAT LA EXPLICAȚIE VERIFICABILĂ</div>
      <div class="prompt-text">Vreau să transform rezultatul în explicație. Pe baza cauzelor citite din model, spune-mi pe ce tăietură cobor ca să văd cauza ascunsă de total, cum verific că factorul chiar produce rezultatul (nu doar apare cu el) și formulează o frază de insight care numește factorii principali și poate fi arătată înapoi în date. Explică doar ce s-a întâmplat și de ce; nu trece la ce ar urma sau la pași de făcut. Distinge clar explicația de clasament: ordinea și diferențele sunt deja date, eu caut cauza.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Scrii insight-ul într-o frază verificabilă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Insight-ul care rămâne în cap nu e o explicație. Îl scrii într-o frază clară: ce rezultat, din ce cauză, vizibilă pe ce felie. O frază pe care un decident o înțelege și pe care o poți arăta înapoi în model. Insight verbal, nu jargon.</p>

  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Ancorezi explicația în model</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O explicație care nu se arată în date e o părere. O ancorezi: fiecare frază de insight trimite la felia, măsura sau comparația care o susține. <span data-locked="1">Cauza trăiește în model, nu în intuiție.</span> Așa explicația poate fi verificată de oricine.</p>
    <div class="section-sublabel">DOVADA TRANSFORMĂRII</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Rezultatul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">clasament care arată CARE</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">explicație care spune DE CE</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Cauza</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">ghicită, din intuiție</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">citită din model</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Coincidența</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">„împreună" luat drept cauză</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">separată de cauza reală</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Insight-ul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">rămas în capul analistului</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">frază verificabilă scrisă</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Factorii</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">o cauză unică forțată</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">factorii principali numiți</span></div>
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
      <div class="stage-label">ETAPA 4 · VERIFICAREA EXPLICAȚIEI</div>
      <h2 class="stage-name">VERIFICARE</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Citire din model</span></div>
    </div>
  </header>
  <p class="stage-quote">O explicație de încredere se arată înapoi în date și rezistă întrebării „de unde știi?". Verifici fiecare.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Verifici că explicația se arată înapoi în model</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pentru fiecare frază de insight, arăți felia, măsura sau comparația care o susține. Dacă nu poți arăta cauza în model, explicația nu trece: un „de ce" pe care nu îl poți dovedi în date rămâne o presupunere, nu un insight.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Respingi narativul pe care datele nu îl susțin</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O poveste poate fi plauzibilă și falsă în același timp. Treci fiecare explicație prin model: cele pe care datele nu le confirmă se resping, oricât de bine sună. Interpretarea bună elimină narativele convenabile, nu le colecționează.</p>

  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Confirmi că nu ai forțat o cauză unică</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Recitești explicația: numește un singur vinovat acolo unde lucrează mai mulți factori? Dacă da, o corectezi. O explicație onestă arată factorii principali și greutatea lor, nu o cauză unică aleasă pentru că e mai ușor de spus.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · STABILIZAREA EXPLICAȚIEI</div>
      <h2 class="stage-name">STABILIZARE</h2>
      <div class="stage-tags"><span class="phase-tag">ANCORARE</span><span class="type-tag">Citire repetabilă</span></div>
    </div>
  </header>
  <p class="stage-quote">O explicație bună nu se schimbă la fiecare recitire. E ancorată în model și rezistă datelor noi.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Ancorezi explicația la model, nu la o stare de moment</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Insight-ul trăiește lângă felia care îl susține, nu într-o notă ruptă de date. Când cineva întreabă „de unde știi?", trimiți la aceeași felie din model. O explicație ancorată e o explicație care poate fi recitită, nu reținută din memorie.</p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Un rând nou nu schimbă cauza dacă explicația e reală</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Adaugi date noi în model. O explicație reală rămâne valabilă: factorul principal e tot acolo. Dacă o singură tranzacție nouă răstoarnă explicația, n-a fost o cauză, a fost o coincidență prinsă la un moment dat.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">Aplici regula anti-poveste</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O explicație bună supraviețuiește sursei noi. Vine exportul de luna viitoare: cauza citită din model se confirmă pe datele noi sau se ajustează cinstit. Explicația nu se agață de o poveste: e ancorată în date, nu într-o concluzie comodă.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-6" data-stage="6" data-stage-ghost="06">
  <header class="stage-header">
    <div class="stage-number">06</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 6 · ÎNCHIDEREA ANALIZEI</div>
      <h2 class="stage-name">CONFIRMARE</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Cap-coadă</span></div>
    </div>
  </header>
  <p class="stage-quote">Pui întrebarea „de ce?". Modelul explică. Apoi închizi analiza setului și o predai mai departe.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">Faci prima citire a insight-ului</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Citești fraza de insight: rezultatul, cauza și felia care o susține. Pusă din nou, aceeași întrebare „de ce?" dă aceeași explicație, pentru că e ancorată în model. Explicația nu mai depinde de cine o spune.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Confirmi setul de explicații ancorate</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci în revistă insight-urile: fiecare are o întrebare, o cauză citită din model, factorii principali și o felie care îl dovedește. Niciunul nu e o poveste orfană. Ai un set de explicații verificabile, nu un set de păreri.</p>

  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Închizi analiza: treapta T3 finalizată</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">Am completat analiza setului: treapta T3 este finalizată.</span> Setul a fost legat, măsurat, comparat și acum interpretat: de la „ce există" la „de ce arată așa". C12 explică ce s-a întâmplat și de ce. Cum se vede dintr-o privire și cum se pune în pagină începe la treapta următoare. Predai un set de explicații ancorate, cu valorile sursă neatinse și suma conservată.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a închide analiza și a o preda treptei următoare, confirmi fiecare invariant al interpretării. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">CONTROL</div><div class="final-text">Date_MASTER-C12.xlsx deschis. Model, măsuri și clasament corecte, suma de control fixată la intrare.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">ÎNTREBARE</div><div class="final-text">Fiecare insight răspunde la o întrebare clară de tip „de ce?". Nicio explicație fără întrebare.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">CAUZĂ CITITĂ</div><div class="final-text">Fiecare cauză e citită din model, nu ghicită. Zero explicații din intuiție.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">COINCIDENȚĂ</div><div class="final-text">Ce apare împreună e separat de ce produce rezultatul. Nicio coincidență promovată la cauză.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">FACTORI</div><div class="final-text">Factorii principali numiți, fără o cauză unică forțată acolo unde lucrează mai mulți.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">VERIFICABIL</div><div class="final-text">Fiecare insight se arată înapoi în model. Narativul nesusținut de date e respins.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">FRAZĂ</div><div class="final-text">Insight-ul e scris ca frază clară, înțeleasă de un decident, nu lăsat în capul analistului.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">ÎNCHIDERE T3</div><div class="final-text">Analiza setului închisă, treapta T3 finalizată. Valori sursă neatinse, suma conservată cap-coadă.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Analiză închisă.</div>
          <div class="completion-subtitle">Fiecare rezultat explicat, cu cauza citită din model. Treapta T3 finalizată.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 4 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C13 · Vizualizare executivă</h3>
        <p class="next-desc">Ai explicații ancorate: rezultatul și cauza lui, citite din model. Dar cum vede altcineva, dintr-o privire, ce ai înțeles? Punerea răspunsului în pagină, vizibil pentru o audiență, începe la C13, în treapta de raportare.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Clasamentul arăta deja care conduce și cu cât.</div>
        <div class="payoff-line accent">Dar nimeni nu putea spune de ce, fără să ghicească.</div>
        <div class="payoff-line regular">Acum fiecare rezultat are o cauză citită din model, scrisă ca frază verificabilă. Pui întrebarea „de ce?" și modelul explică.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Același clasament putea avea două explicații opuse. Acum doar una se verifică în date, și o poți arăta oricui.</span></div>
        <div class="payoff-motto" data-locked="1">Nu citi rezultatul. Explică-l.</div>
      </section>

      <footer class="footer">
        TRAINITY · C12 INTERPRETARE · de ce-ul din date, explicat și verificabil
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
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">TRANSFORMARE</span><span class="nav-item-meta">3 pași · Insight</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">VERIFICARE</span><span class="nav-item-meta">3 pași · Control</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">STABILIZARE</span><span class="nav-item-meta">3 pași · Ancorare</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">CONFIRMARE</span><span class="nav-item-meta">3 pași · Cap-coadă</span></span></a></div>

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
    head = head.replace('<title>C10 · Măsuri · Trainity</title>',
                        '<title>C12 · Interpretare · Trainity</title>')
    head = head.replace('/* ============ NEXT (C10) ============ */',
                        '/* ============ NEXT (C12) ============ */')
    # patch STORAGE_KEY in tail
    tail = tail.replace('trainity_c10_study_v1', 'trainity_c12_study_v1')

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    import os
    os.makedirs('c12', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')

    # garda: nu trebuie sa ramana tokeni C10 reziduali in CONTINUT
    leftover = re.findall(r'C10|trainity_c10|Date_MASTER-C10|Măsuri|MĂSURI|măsură potrivită', out)
    # filtram aparitiile LEGITIME (system-map, lant T3, predare/distinctie)
    print('  leftover C10/Masuri tokens (verifica context legitim):', len(leftover))

    # garda anti-drift T4/T5: termeni interzisi ca identitate in C12
    for term in ['dashboard', 'what-if', 'scenariu', 'predicți', 'recomand', 'cockpit']:
        n = out.lower().count(term)
        if n:
            print('  ATENTIE termen T4/T5 prezent (%dx): %s' % (n, term))


if __name__ == '__main__':
    main()
