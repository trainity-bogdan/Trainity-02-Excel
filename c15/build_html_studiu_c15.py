#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c15.py - HTML-Studiu-Excel-15-Sintetizare.html prin COPY+MODIFY din c14.

Strategie (ca la C14 din C13): pastrez head+CSS si JS din c14 (generice), inlocuiesc
DOAR blocul <body>..<script> cu narativ C15 SINTETIZARE. Patch title + STORAGE_KEY + NEXT.

Axa C15: SINTEZA, nu rezumat. C15 = formularea mesajului esential (o propozitie), NU layout
(=C14), NU decizie (=C16), NU analiza noua (=T3). SINTEZA != REZUMAT. Pilon T4: T4 consuma
raspunsul produs de T3, nu il naste. 18 step-titles in 6 etape (3x6), 5 fenomene, 8 verificari,
2 prompturi. E5 = REFORMULARE (eticheta C15; intern phase-tag poate fi RECALCUL).
"""
import re, os

SRC = 'c14/HTML-Studiu-Excel-14-Compunere.html'
OUT = 'c15/HTML-Studiu-Excel-15-Sintetizare.html'

HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>MESAJUL ESENTIAL</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C15 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C15 · SINTEZĂ</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Sintetizare C15: o pagina de raport coerenta din care se extrage o singura fraza, mesajul esential pe care pagina il dovedeste">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C15</span><span class="hov-object">MESAJUL ESENȚIAL</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cum transform o pagină într-o singură frază care contează?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 4">
            <span class="sm-step">VIZUALIZARE</span><span class="sm-arrow">·</span><span class="sm-step">COMPUNERE</span><span class="sm-arrow">·</span><span class="sm-step active">SINTETIZARE</span><span class="sm-arrow">·</span><span class="sm-step">LIVRARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title">Cum să sintetizezi o pagină într-o singură frază</h1>
        <p class="hero-microbrief">Primești o pagină coerentă de la treapta de compunere: focar, ierarhie, traseu de citire. Totul e corect și totul se vede. Și decidentul tot întreabă: și ce-i cu asta? O pagină arată; nu spune. Mesajul esențial există în date, dar nu e formulat nicăieri. Aici îl extragi și îl scrii într-o singură frază pe care pagina o dovedește.</p>
        <div class="cover-miza">C15 nu rearanjează pagina și nu calculează nimic. Aici o pagină întreagă capătă o singură afirmație, headline-ul pe care restul paginii îl susține. Nu o cifră nouă, nu o cauză nouă, acelea vin gata din analiză, ci mesajul: ce trebuie să reții dintr-o privire. C15 formulează mesajul; încadrarea lui pentru decizie începe la treapta următoare.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">O pagină impecabilă.</span> <span class="ib-2">Și niciun mesaj.</span></p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Ai o pagină corectă, completă, frumos așezată. Și totuși:</p>
        <ul class="tu-list">
          <li>o trimiți și primești înapoi întrebarea care e ideea?</li>
          <li>fiecare reține altceva din aceeași pagină, sau nimic</li>
          <li>cu cât pui mai mult pe pagină, cu atât spune mai puțin</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Oamenii rezumă tot.<br><span class="tu-hl">Profesioniștii formulează ce contează.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">O pagină arată. O sinteză spune.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai prezinți tot ce ai. <span class="tu-hl">Sintetizezi singura frază care contează.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>pagină corectă pe care nimeni n-o citește până la capăt</li><li>un rezumat care scurtează tot, proporțional</li><li>fiecare prinde altă idee, sau niciuna</li><li>decidentul întreabă și ce-i cu asta?</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>o singură frază care spune ce contează</li><li>headline ancorat în dovada de pe pagină</li><li>același mesaj reținut de toți, dintr-o privire</li><li>decidentul știe în trei secunde ce să rețină</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>o singură afirmație esențială, pe care pagina o dovedește</li><li>distincția fermă între a rezuma tot și a sintetiza ce contează</li><li>un mesaj care trece testul fără asta, decidentul hotărăște la fel?</li><li>o pagină care spune, gata de predat treptei de livrare</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Nu rezumăm. <mark>Sintetizăm.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CELE CINCI FELURI ÎN CARE O PAGINĂ RĂMÂNE MUTĂ</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">REZUMATUL CARE NU SPUNE</b><p class="anomaly-desc">Scurtezi tot proporțional și obții o listă fără ierarhie de sens, nimic nu iese în față. Corecția: sinteza alege singurul mesaj care contează, nu îl scurtează pe tot.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">MESAJUL ÎNGROPAT</b><p class="anomaly-desc">Pagina arată totul, dar afirmația-cheie nu e scrisă nicăieri, cititorul o caută singur. Corecția: o singură frază pe care pagina de dedesubt o dovedește.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">ȘI CE-I CU ASTA?</b><p class="anomaly-desc">Decidentul citește pagina întreagă și tot întreabă care e ideea. Corecția: fraza care trece testul fără ea, decidentul hotărăște la fel?</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">MESAJUL CARE NU SE POTRIVEȘTE</b><p class="anomaly-desc">Aceeași pagină, dar mesajul e scris pentru altă audiență sau altă decizie. Corecția: mesajul pentru ACEASTĂ decizie și ACEASTĂ audiență, nu unul în general.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">AFIRMAȚIA NESUSȚINUTĂ</b><p class="anomaly-desc">Scrii o frază pe care pagina nu o dovedește, mesaj fără acoperire. Corecția: headline ancorat în dovada vizuală deja prezentă pe pagină.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · PAGINA MUTĂ</div>
      <h2 class="stage-name">MUTĂ</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Primești o pagină coerentă, corectă, completă. Înainte de orice frază, vezi de ce o pagină care arată tot poate să nu spună nimic.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Primești pagina coerentă de la compunere</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C15-Sintetizare.xlsx. <span data-locked="1">Vine cu pagina compusă de la treapta de compunere: focar, ierarhie, traseu de citire.</span> Totul e corect și totul se vede. Dar o pagină coerentă nu e încă un mesaj.</p>
  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Testul celor 3 secunde</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O privești trei secunde și te întrebi ce ai reține. De obicei, încă nimic precis. Pagina arată cifre și forme corecte, dar nu îți pune în mână o idee. Acesta e golul pe care urmează să-l umpli cu o frază.</p>
  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">De ce o pagină corectă poate fi mută</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">O pagină arată; nu spune.</span> Corectitudinea și claritatea vizuală nu produc singure un mesaj. Mesajul e o afirmație în cuvinte, nu o sumă de obiecte corecte. De aici începe sinteza.</p>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · REZUMATUL AUTOMAT</div>
      <h2 class="stage-name">REZUMATUL</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Lași AI-ul să scurteze pagina, apoi vezi clar diferența dintre a rezuma tot și a spune ce contează.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">AI propune un rezumat draft al paginii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Ceri AI-ului câteva titluri candidate pornind de la pagină. <span data-locked="1">AI face partea automatizabilă: un rezumat draft. Tu deții alegerea mesajului.</span> Primești materie primă, nu mesajul final.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · TITLURI CANDIDATE (DRAFT)</div>
      <div class="prompt-text">Pe baza acestui raport, propune-mi 3 titluri candidate, fiecare de o singură frază, care spun ce contează pentru decizia și audiența pe care ți le dau. Nu calcula cifre noi și nu explica de ce, formulează doar din ce e deja în raport. Lasă-mă pe mine să aleg și să ascut titlul; tu dă-mi variante de pornire.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Rezumat ≠ sinteză</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui față în față cele două ieșiri. <span data-locked="1">Rezumatul scurtează tot. Sinteza spune ce contează.</span> Rezumatul micșorează proporțional fiecare bucată; sinteza renunță la tot ce nu mută decizia și păstrează o singură afirmație.</p>
  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">De ce rezumatul nu e încă mesajul</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Un rezumat bun e tot o listă: corect, dar fără ierarhie de sens. <span data-locked="1">Mesajul nu e ce conține pagina, e ce trebuie reținut din ea.</span> Alegerea aceea e umană și o faci în etapa următoare.</p>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-3" data-stage="3" data-stage-ghost="03">
  <header class="stage-header">
    <div class="stage-number">03</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 3 · MESAJUL ESENȚIAL</div>
      <h2 class="stage-name">MESAJUL</h2>
      <div class="stage-tags"><span class="phase-tag">SINTEZĂ</span><span class="type-tag">Formulare</span></div>
    </div>
  </header>
  <p class="stage-quote">Alegi singura afirmație pe care pagina o dovedește și o formulezi într-o frază, pentru decizia și audiența de față.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Care e singura afirmație pe care pagina o dovedește?</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te uiți la focarul paginii și întrebi ce afirmație susține el. <span data-locked="1">Mesajul nu se descoperă aici, vine gata din analiză; tu îl formulezi.</span> Cauți afirmația pe care pagina o probează, nu una pe care ți-ai dori-o.</p>
  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Formulezi headline-ul într-o singură frază</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Scrii headline-ul (so-what) într-o singură propoziție și o linie de susținere. <span data-locked="1">O singură afirmație, nu trei.</span> În stratul MESAJ din Excel notezi headline-ul, linia de susținere și legătura la zona din pagină care îl dovedește.</p>
  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Mesajul pentru ACEASTĂ decizie și audiență</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Ajustezi fraza la cine decide și ce are de hotărât. <span data-locked="1">Aceeași pagină poate avea mesaje diferite pentru audiențe diferite; sinteza alege mesajul potrivit, nu unul general.</span> Aici stă judecata umană, partea care nu se automatizează.</p>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-4" data-stage="4" data-stage-ghost="04">
  <header class="stage-header">
    <div class="stage-number">04</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 4 · TESTUL „ȘI CE-I CU ASTA?"</div>
      <h2 class="stage-name">TESTUL</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Pui mesajul la trei probe: contează, e indicativ și nu inventează nimic peste pagină.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Filtrul „fără asta, decidentul hotărăște la fel?"</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Aplici filtrul cheie. <span data-locked="1">Fără această frază, decidentul hotărăște la fel? Dacă da, nu e mesajul.</span> Lași AI-ul să critice candidatul, apoi tu decizi forma finală.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · TESTUL MESAJULUI</div>
      <div class="prompt-text">Pentru titlul ales, verifică: este o singură afirmație? este indicativ, adică spune ce e, nu ce să fac? nu introduce o cifră sau o cauză care nu e deja în raport? trece testul fără asta, decidentul hotărăște la fel? Spune-mi unde cade și de ce; decizia finală asupra formei o iau eu.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Indicativ, nu decizional</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Verifici că mesajul spune ce este, nu ce să faci. <span data-locked="1">C15 enunță; nu numește decizia și nu recomandă, aceea e treaba livrării.</span> Dacă fraza conține de hotărât, recomand sau acțiunea e, ai trecut în C16.</p>
  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Formulat, nu descoperit</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Confirmi că nu ai adăugat nimic peste pagină. <span data-locked="1">Nicio cifră nouă, nicio cauză nouă; acelea vin din analiză.</span> Dacă pentru a scrie mesajul a trebuit să te întorci în model și să calculezi, ai intrat în analiză, nu în sinteză.</p>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · MESAJUL SE ADAPTEAZĂ</div>
      <h2 class="stage-name">REFORMULAREA</h2>
      <div class="stage-tags"><span class="phase-tag">REFORMULARE</span><span class="type-tag">Mesajul la schimbare</span></div>
    </div>
  </header>
  <p class="stage-quote">Când pagina se schimbă, mesajul se reface în cuvinte, nu în cifre.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Pagina se schimbă, mesajul vechi nu mai e exact</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">Datele s-au actualizat în amonte, în model; cifrele s-au schimbat acolo.</span> Pagina reflectă noul rezultat. Headline-ul scris ieri poate să nu mai fie adevărat azi. Îl recitești față de pagina nouă.</p>
  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Reformulezi headline-ul, nu recalculezi</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">Refaci sinteza: rescrii fraza ca să spună ce contează acum.</span> Nu atingi nicio cifră, cifrele rămân ale modelului. Reformularea e un act în cuvinte, nu un recalcul.</p>
  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">Noul mesaj rămâne o singură afirmație susținută</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci mesajul nou prin același criteriu. <span data-locked="1">O singură afirmație, susținută de pagină, pe criteriul ce contează.</span> Sinteza nu e un titlu scris o dată, e o frază care ține pasul cu pagina.</p>
  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-6" data-stage="6" data-stage-ghost="06">
  <header class="stage-header">
    <div class="stage-number">06</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 6 · O PAGINĂ A DEVENIT UN MESAJ</div>
      <h2 class="stage-name">PREDAREA</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Handoff livrare</span></div>
    </div>
  </header>
  <p class="stage-quote">Pagina spune acum o frază, dovedită de tot ce e sub ea, gata de predat pentru încadrarea deciziei.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">O pagină coerentă a devenit un mesaj care contează</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pui mesajul în capul paginii, ca headline. <span data-locked="1">Aceeași pagină care doar arăta, acum spune o frază.</span> Restul paginii nu se schimbă, devine dovada afirmației.</p>
  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Mesajul și pagina-dovadă, împreună</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Verifici că fraza și dovada stau lipite. <span data-locked="1">Headline-ul sus, dovada dedesubt; cine vrea, coboară și verifică.</span> Un mesaj fără pagină e o părere; o pagină fără mesaj e mută. Împreună sunt un raport care spune.</p>
  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Predare către livrare</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Predai pagina cu mesaj treptei de livrare. <span data-locked="1">C15 spune ce contează; încadrarea pentru decizie, ce e de hotărât, vine la C16.</span> Nu tu numești decizia aici, doar formulezi mesajul pe care decizia se va sprijini.</p>
  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda mesajul treptei următoare, confirmi fiecare invariant al sintezei. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">O FRAZĂ</div><div class="final-text">Mesajul e o singură propoziție, nu un paragraf și nu o listă. Dacă are mai multe idei, încă nu e sinteză.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">INDICATIV</div><div class="final-text">Spune ce este, nu ce să faci. Zero de hotărât, recomand sau acțiune; aceea e livrarea, nu sinteza.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">FĂRĂ NIMIC NOU</div><div class="final-text">Nicio cifră nouă, nicio cauză nouă. Mesajul reformulează un răspuns deja produs de analiză, nu îl naște.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">TESTUL SO-WHAT</div><div class="final-text">Trece filtrul fără această frază, decidentul hotărăște la fel? Dacă da, nu e mesajul esențial.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">SINTEZĂ, NU REZUMAT</div><div class="final-text">Alege ce contează, nu scurtează tot. Dacă e o listă proporțională a paginii, e rezumat, nu sinteză.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">PAGINA DOVEDEȘTE</div><div class="final-text">Pagina de dedesubt susține fraza. Un mesaj pe care pagina nu îl probează e o afirmație nesusținută.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">NU REARANJEAZĂ</div><div class="final-text">Sinteza nu mută blocuri pe pagină; aceea e compunerea. Output-ul C15 e o propoziție, nu un layout.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">SINTETIZEZ</div><div class="final-text">Verbul construcției e a sintetiza: formulezi mesajul. Pagină care spune o frază, gata de predat pentru livrare.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Mesaj esențial formulat.</div>
          <div class="completion-subtitle">O singură frază pe care pagina o dovedește. Gata de predat pentru încadrarea deciziei la C16.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 4 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C16 · Livrarea</h3>
        <p class="next-desc">Ai o pagină care spune o frază, dovedită de tot ce e sub ea. Dar ce are decidentul de hotărât, concret, și ce-i trebuie ca să acționeze? Încadrarea deciziei și predarea raportului decision-ready încep la C16, în treapta de raportare.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Pagina era coerentă încă de la treapta de compunere.</div>
        <div class="payoff-line accent">Dar arăta tot și nu spunea nimic, iar decidentul tot întreba care e ideea.</div>
        <div class="payoff-line regular">Acum o singură frază spune ce contează, iar pagina rămâne dovada ei.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">O pagină întreagă pe care trebuia s-o descifrezi. Acum o singură frază îți spune ce contează, iar pagina o dovedește.</span></div>
        <div class="payoff-motto" data-locked="1">Dintr-o privire, mesajul.</div>
      </section>

      <footer class="footer">
        TRAINITY · C15 SINTETIZARE · pagina care spune, într-o frază, ce contează
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
      <div class="nav-items"><a class="nav-item" data-nav-stage="1" href="#stage-1" onclick="navigateStage(1,event)"><span class="nav-item-num">1</span><span class="nav-item-text"><span class="nav-item-name">MUTĂ</span><span class="nav-item-meta">3 pași · Manual</span></span></a>
<a class="nav-item" data-nav-stage="2" href="#stage-2" onclick="navigateStage(2,event)"><span class="nav-item-num">2</span><span class="nav-item-text"><span class="nav-item-name">REZUMATUL</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">MESAJUL</span><span class="nav-item-meta">3 pași · Sinteză</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">TESTUL</span><span class="nav-item-meta">3 pași · Control</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">REFORMULAREA</span><span class="nav-item-meta">3 pași · Reformulare</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">PREDAREA</span><span class="nav-item-meta">3 pași · Handoff</span></span></a></div>

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
    head = head.replace('<title>C14 · Compunere · Trainity</title>',
                        '<title>C15 · Sintetizare · Trainity</title>')
    head = head.replace('/* ============ NEXT (C14) ============ */',
                        '/* ============ NEXT (C15) ============ */')
    # patch STORAGE_KEY in tail
    tail = tail.replace('trainity_c14_study_v1', 'trainity_c15_study_v1')

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c15', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # garda: tokeni C14 reziduali in CONTINUT (in afara JS/head generic)
    leftover = re.findall(r'C14|trainity_c14|Date_MASTER-C14|Compunere|COMPUNERE|Compun\b', body)
    print('  leftover C14 tokens in BODY (trebuie 0):', len(leftover), leftover[:8])

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
