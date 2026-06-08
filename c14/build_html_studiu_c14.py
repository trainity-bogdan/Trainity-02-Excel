#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c14.py - HTML-Studiu-Excel-14-Compunere.html prin COPY+MODIFY din c13.

Strategie (ca la C13 din C12): pastrez head+CSS si JS din c13 (generice), inlocuiesc
DOAR blocul <body>..<script> cu narativ C14 COMPUNERE. Patch title + STORAGE_KEY + NEXT.

Axa C14: ORGANIZAREA SPATIALA A ELEMENTELOR VIZUALE. C14 = pagina cu ierarhie, NU obiectul
singular (=C13), NU mesajul (=C15), NU livrarea (=C16). Dashboard = substrat, nu identitate.
Pilon T4: T4 consuma raspunsul produs de T3, nu il naste.
11 step-titles LOCKED in 6 etape (2+2+2+2+2+1), 6 fenomene, 8 verificari, 2 prompturi.
"""
import re, os

SRC = 'c13/HTML-Studiu-Excel-13-Vizualizare.html'
OUT = 'c14/HTML-Studiu-Excel-14-Compunere.html'

HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>ORDINEA PRIVIRII</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C14 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C14 · Compunere</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/11</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Compunere C14: mai multe obiecte vizuale oneste asezate spatial intr-o pagina de raport cu focar, ierarhie si traseu de citire">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C14</span><span class="hov-object">COMPOZIȚIE</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Ce vede ochiul întâi?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 4">
            <span class="sm-step">VIZUALIZARE</span><span class="sm-arrow">·</span><span class="sm-step active">COMPUNERE</span><span class="sm-arrow">·</span><span class="sm-step">SINTETIZARE</span><span class="sm-arrow">·</span><span class="sm-step">LIVRARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <p class="hero-microbrief">Ai obiecte vizuale oneste, fiecare adevărat singur, primite de la treapta de vizualizare. Le pui pe o pagină. Și decidentul tot nu vede ce contează. Nimic nu e fals, dar pagina induce în eroare: aceleași obiecte, altă așezare, altă decizie. O pagină nu e un container, e un traseu al privirii.</p>
        <div class="cover-miza">C14 nu desenează obiectul și nu formulează mesajul. Aici mai multe obiecte vizuale oneste se așază spațial într-o pagină de raport: un focar atins primul, o ierarhie care spune ce e principal, un traseu de citire pentru decizie. Nu o pagină frumoasă, o pagină în care ochiul prinde întâi ce contează. C14 organizează ordinea privirii; extragerea mesajului începe la treapta următoare.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">Graficele sunt corecte.</span> <span class="ib-2">Pagina te încurcă.</span></p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Ai toate graficele corecte și o pagină care pare profesională. Și totuși:</p>
        <ul class="tu-list">
          <li>decidentul caută cu privirea unde să se uite întâi și ezită</li>
          <li>cel mai important rezultat stă jos, la fel de mare ca un detaliu minor</li>
          <li>pagina pare completă, dar decizia întârzie sau iese greșită</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Oamenii umplu pagina.<br><span class="tu-hl">Profesioniștii o ordonează.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Aceleași grafice, altă ordine, altă decizie.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai aranjezi pagina. <span class="tu-hl">Conduci privirea decidentului.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>obiecte corecte, împrăștiate, fără un focar</li><li>toate la fel de mari, nicio ierarhie</li><li>ochiul aterizează la întâmplare și rătăcește</li><li>pagina pare completă, decizia întârzie</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>un singur focar, atins primul de ochi</li><li>ierarhie clară: principal, suport, detaliu</li><li>un traseu de citire pentru decizie</li><li>răspunsul se prinde în câteva secunde</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>un focar care duce ochiul la ce contează întâi</li><li>o ierarhie vizuală făcută pentru decizie, nu pentru estetică</li><li>o pagină testată cu al doilea ochi în trei secunde</li><li>o pagină de raport coerentă, gata de predat treptei următoare</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Compun privirea, <mark>nu pagina.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CELE ȘASE FELURI ÎN CARE AȘEZAREA STRICĂ DECIZIA</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">PAGINA-ZID</b><p class="anomaly-desc">Zeci de obiecte de aceeași mărime, niciunul mai important, ochiul nu știe unde să meargă. Corecția: stabilești un singur focar, atins primul.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">ESENȚIALUL ÎNGROPAT</b><p class="anomaly-desc">Cel mai important rezultat stă jos, în colț, la fel de mare ca un detaliu. Corecția: esențialul urcă în primul punct de contact al ochiului.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">ORDINEA DE PRODUCȚIE</b><p class="anomaly-desc">Pui obiectele în ordinea în care le-ai făcut, nu în care trebuie văzute. Corecția: ordinea de citire e guvernată de răspuns, nu de cronologie.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">GREUTATE EGALĂ</b><p class="anomaly-desc">Titlu, total, detaliu, notă, toate la fel de mari: nicio ierarhie. Corecția: greutate inegală prin mărime, poziție, contrast și spațiu.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">PROXIMITATEA CARE MINTE</b><p class="anomaly-desc">Lucruri legate stau departe, lucruri nelegate stau lipite. Corecția: grupezi spațial ce ține împreună, separi ce nu e legat.</p></div>
<div class="anomaly-card"><span class="anomaly-num">06</span><b class="anomaly-title">HORROR VACUI</b><p class="anomaly-desc">Umpli orice spațiu gol cu încă un obiect. Corecția: spațiul gol e instrument de ierarhie, izolează focarul și separă grupurile.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · PAGINA FĂRĂ ORDINE</div>
      <h2 class="stage-name">ZIDUL</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Primești obiecte oneste și o pagină fără un întâi. Înainte de orice așezare, vezi cum citește ochiul pagina pe care nu ai compus-o încă.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Pagina fără "întâi"</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C14-Compunere.xlsx. <span data-locked="1">Vine cu obiectele vizuale oneste preluate de la treapta de vizualizare, așezate în ordinea producției.</span> Toate la fel de mari, niciunul mai important. Ochiul nu știe unde să înceapă. Obiecte corecte nu fac o pagină care decide.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Primul punct de contact al ochiului</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te uiți unde cade ochiul primul: sus-stânga, cel mai mare, cel mai contrastant. Pagina are deja un traseu al privirii, doar că nu l-ai ales tu. Nu citim totul deodată; întâlnim ceva întâi. Asta e pârghia pe care urmează s-o controlezi.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · POZIȚIA ȘI FOCARUL</div>
      <h2 class="stage-name">POZIȚIA</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Descoperi că poziția nu e neutră: unde așezi un obiect spune cât contează. Apoi alegi ce întâlnește ochiul primul.</p>
  <div class="stage-body">
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Poziția ca semnal de importanță</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Muți același obiect sus, apoi jos, apoi în colț. <span data-locked="1">Ce stă sus, mare sau în centru spune "important"; ce stă jos, mic sau în margine spune "secundar".</span> Poziția e un argument, vrând-nevrând. De acum o folosești intenționat, nu din reflex.</p>

  </div>
</div>
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Focarul vizual</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Alegi focarul: obiectul care poartă răspunsul venit din analiză, și-l plasezi unde cade ochiul primul. <span data-locked="1">O pagină are un singur focar, nu cinci.</span> Nu inventezi importanța aici, o primești din răspuns și o așezi în prim-plan. Apoi ceri AI-ului o ierarhie de pornire: ce vede ochiul întâi, ce după, ce se retrogradează; tu judeci dacă servește decizia.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · IERARHIA ȘI ORDINEA DE CITIRE</div>
      <div class="prompt-text">Am mai multe obiecte vizuale deja produse și verificate, plus răspunsul venit din analiză pe care pagina trebuie să-l facă vizibil. Propune-mi ce ar trebui să vadă ochiul întâi, ce după și ce să retrogradez, ca decidentul să prindă dintr-o privire ce contează. Nu redesena obiectele și nu schimba tipul lor, nu formula mesajul în cuvinte și nu pregăti livrarea. Lucrează doar cu ordinea și ierarhia spațială.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-3" data-stage="3" data-stage-ghost="03">
  <header class="stage-header">
    <div class="stage-number">03</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 3 · ORDINEA DE CITIRE</div>
      <h2 class="stage-name">TRASEUL</h2>
      <div class="stage-tags"><span class="phase-tag">COMPUNERE</span><span class="type-tag">Traseu și retrogradare</span></div>
    </div>
  </header>
  <p class="stage-quote">Ordonezi ce vede ochiul după focar, apoi cobori din prim-plan ce nu mută decizia.</p>
  <div class="stage-body">
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Traseul de citire</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">După focar, ordonezi ce vede ochiul al doilea și al treilea. <span data-locked="1">Construiești fluxul focar, susținere, detaliu, folosind poziția și alinierea ca să ghidezi privirea.</span> Traseul nu e decorativ, e drumul pe care îl parcurge decizia.</p>

  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Retrogradarea elementelor secundare</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cobori din prim-plan ce nu mută decizia, fără să ștergi. Aplici filtrul: <span data-locked="1">fără acest element în prim-plan, decidentul hotărăște la fel?</span> Dacă da, îl micșorezi, îl muți în periferie sau îl lași ca detaliu la cerere. Ierarhie prin de-emfază, nu doar prin emfază.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-4" data-stage="4" data-stage-ghost="04">
  <header class="stage-header">
    <div class="stage-number">04</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 4 · GREUTATE INEGALĂ</div>
      <h2 class="stage-name">IERARHIA</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Ierarhie și grupare</span></div>
    </div>
  </header>
  <p class="stage-quote">Faci ierarhia vizibilă instant cu mărime, poziție, contrast și spațiu, apoi grupezi ce ține împreună.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Ierarhia vizuală pentru decizie</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Construiești două sau trei niveluri clare: focar peste suport peste detaliu. <span data-locked="1">Greutate inegală pentru lucruri inegale, prin mărime, poziție, contrast și spațiu.</span> Criteriul nu e "arată plăcut", e "se vede întâi ce decide". Importanța trebuie citită instant, nu căutată.</p>

  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Gruparea elementelor legate</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui spațial împreună obiectele care țin de aceeași întrebare și separi ce nu e legat. <span data-locked="1">Proximitatea spune adevărul despre relații: lângă înseamnă împreună.</span> Gruparea reduce efortul de citire, fără să creezi relații noi în date.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · COMPOZIȚIA GUVERNATĂ</div>
      <h2 class="stage-name">SPAȚIUL</h2>
      <div class="stage-tags"><span class="phase-tag">ANCORARE</span><span class="type-tag">Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Folosești spațiul gol ca instrument, apoi aliniezi toată pagina la răspunsul venit din analiză.</p>
  <div class="stage-body">
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Spațiul gol ca instrument de ierarhie</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lași spațiu gol în jurul focarului și între grupuri. <span data-locked="1">Spațiul gol nu e lipsă, e instrument: izolează ce contează și separă ce e diferit.</span> Reflexul de a-l umple cu încă un obiect strică ierarhia. Golul deliberat dă respiro și ordine.</p>

  </div>
</div>
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Compunerea guvernată de răspunsul venit din T3</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2 și aliniezi toată pagina la răspunsul deja produs de analiză. <span data-locked="1">Răspunsul decide ce e focar și ce e suport; compoziția îl servește, nu îl naște.</span> Build-up guvernat de răspuns, nu orb. Corectezi varianta AI după "se vede întâi ce decide".</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · VARIANTA DE COMPOZIȚIE</div>
      <div class="prompt-text">Pe baza ierarhiei stabilite și a răspunsului venit din analiză, propune-mi o variantă de așezare a obiectelor pe pagina de raport: poziționare, grupare, spațiu gol și focar, astfel încât ochiul să prindă întâi ce contează pentru decizie. Nu schimba tipul graficelor și nu inventa date, nu scrie concluzia în cuvinte și nu pregăti pachetul de livrare. Dă-mi doar compoziția spațială, pe care o corectez după criteriul "se vede întâi ce decide".</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
    <div class="section-sublabel">DOVADA COMPUNERII · ACELEAȘI OBIECTE, ALTĂ AȘEZARE</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Focarul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">niciunul, totul egal</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">unul singur, atins primul</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Ordinea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">ordinea producției</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">traseu guvernat de răspuns</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Greutatea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">egală la lucruri inegale</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">ierarhie pe trei niveluri</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Spațiul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">umplut, horror vacui</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">gol deliberat, izolează focarul</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Decizia</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">întârzie, ochiul rătăcește</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">se prinde în câteva secunde</span></div>
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
      <div class="stage-label">ETAPA 6 · AL DOILEA OCHI</div>
      <h2 class="stage-name">PROBA</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Handoff sinteză</span></div>
    </div>
  </header>
  <p class="stage-quote">O pagină compusă trece proba unui ochi proaspăt în trei secunde, apoi e gata de predat pentru extragerea mesajului.</p>
  <div class="stage-body">
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Testul celui de-al doilea ochi</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Dai pagina cuiva care o vede trei secunde, fără tine lângă el. Ce a întâlnit ochiul întâi? Ce a prins ca prioritate? <span data-locked="1">Dacă focarul și ordinea citită coincid cu intenția, pagina trece; dacă nu, reașezi.</span> Apoi predai pagina coerentă către treapta de sintetizare, gata să i se extragă mesajul. C14 așază pagina; mesajul îl formulează C15.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda pagina treptei următoare, confirmi fiecare invariant al compunerii. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">CONTROL</div><div class="final-text">Date_MASTER-C14-Compunere.xlsx deschis. Obiectele vizuale preluate de la treapta de vizualizare sunt corecte și luate ca atare.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">OBIECTE PRELUATE</div><div class="final-text">Aceleași grafice, tip neschimbat. Zero obiecte redesenate, zero date inventate, zero concluzie formulată.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">FOCAR</div><div class="final-text">Un singur focar, atins primul de ochi. Poartă răspunsul venit din analiză, nu un detaliu nimerit acolo.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">TRASEU</div><div class="final-text">Ordine de citire deliberată: focar, susținere, detaliu. Ce nu mută decizia e retrogradat din prim-plan.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">IERARHIE</div><div class="final-text">Greutate inegală pentru lucruri inegale, prin mărime, poziție, contrast și spațiu. Importanța se vede instant.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">GRUPARE</div><div class="final-text">Proximitatea reflectă relațiile reale. Lucrurile legate stau împreună, cele nelegate sunt separate.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">SPAȚIU</div><div class="final-text">Spațiul gol folosit ca instrument, nu umplut. Izolează focarul și separă grupurile.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">AL DOILEA OCHI</div><div class="final-text">Un cititor de trei secunde prinde aceeași prioritate. Pagină coerentă, gata de predat pentru extragerea mesajului.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Pagină de raport compusă.</div>
          <div class="completion-subtitle">Focar, ierarhie și traseu de citire pentru decizie. Gata de predat pentru extragerea mesajului la C15.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 4 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C15 · Sintetizarea</h3>
        <p class="next-desc">Ai o pagină în care ochiul prinde întâi ce contează. Dar care e propoziția pe care pagina o dovedește, mesajul de o frază pentru decident? Extragerea și formularea mesajului esențial încep la C15, în treapta de raportare.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Obiectele erau corecte de la treapta de vizualizare.</div>
        <div class="payoff-line accent">Dar așezarea greșită ascundea ce contează, fără să schimbe un singur grafic.</div>
        <div class="payoff-line regular">Acum pagina are un focar, o ierarhie și un traseu: ochiul prinde decizia dintr-o privire.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Aceleași grafice, aceleași cifre, altă așezare. Decizia se schimbă mutând blocurile, nu conținutul.</span></div>
        <div class="payoff-motto" data-locked="1">Ce vede ochiul întâi schimbă decizia.</div>
      </section>

      <footer class="footer">
        TRAINITY · C14 COMPUNERE · pagina compusă în care ochiul prinde decizia dintr-o privire
      </footer>

    </main>

    <nav class="side-nav" id="sideNav">

      <div class="nav-progress">
        <div class="nav-progress-row">
          <span class="nav-progress-num" id="navProgressNum">0/11</span>
          <span class="nav-progress-total">PAȘI</span>
        </div>
        <div class="nav-progress-track"><div class="nav-progress-fill" id="navProgressFill"></div></div>
      </div>

      <div class="nav-section-label">6 ETAPE</div>
      <div class="nav-items"><a class="nav-item" data-nav-stage="1" href="#stage-1" onclick="navigateStage(1,event)"><span class="nav-item-num">1</span><span class="nav-item-text"><span class="nav-item-name">ZIDUL</span><span class="nav-item-meta">2 pași · Manual</span></span></a>
<a class="nav-item" data-nav-stage="2" href="#stage-2" onclick="navigateStage(2,event)"><span class="nav-item-num">2</span><span class="nav-item-text"><span class="nav-item-name">POZIȚIA</span><span class="nav-item-meta">2 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">TRASEUL</span><span class="nav-item-meta">2 pași · Compunere</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">IERARHIA</span><span class="nav-item-meta">2 pași · Control</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">SPAȚIUL</span><span class="nav-item-meta">2 pași · Ancorare</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">PROBA</span><span class="nav-item-meta">1 pas · Handoff</span></span></a></div>

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
  <span class="continue-btn-counter" id="continueBtnCounter">pasul 1/11</span>
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
    head = head.replace('<title>C13 · Vizualizare · Trainity</title>',
                        '<title>C14 · Compunere · Trainity</title>')
    head = head.replace('/* ============ NEXT (C13) ============ */',
                        '/* ============ NEXT (C14) ============ */')
    # patch STORAGE_KEY in tail
    tail = tail.replace('trainity_c13_study_v1', 'trainity_c14_study_v1')

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c14', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # garda: tokeni C13 reziduali in CONTINUT (in afara JS/head generic)
    leftover = re.findall(r'C13|trainity_c13|Date_MASTER-C13|Vizualizare|VIZUALIZARE', body)
    print('  leftover C13 tokens in BODY (trebuie 0):', len(leftover), leftover[:8])

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
