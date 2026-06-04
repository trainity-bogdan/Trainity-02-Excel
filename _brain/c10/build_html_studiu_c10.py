#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c10.py - HTML-Studiu-Excel-10-Masuri.html prin COPY+MODIFY din c09.

Strategie sigura: pastrez head+CSS (linii 1..1476) si JS (de la <script>) din c09,
care sunt generice. Inlocuiesc DOAR blocul narativ <body>..<script> cu narativ C10
MASURI. Patch title + STORAGE_KEY + hero placeholder.

Garda C10: pur 'a defini' (Cat?). Zero ranking/contributie/comparatie intre entitati
(=C11), zero cauza (=C12), zero dashboard (=T4). Zero cifre business (R-V02.15).
"""
import re

SRC = 'c09/HTML-Studiu-Excel-09-Relatii.html'
OUT = 'c10/HTML-Studiu-Excel-10-Masuri.html'

# placeholder hero (gradient SVG inline) - ARHITECT inlocuieste cu imaginea reala
HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='420' fill='%23FFD400' font-family='Georgia' font-size='64' "
    "font-weight='bold'>MASURA POTRIVITA</text>"
    "<text x='62' y='470' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C10 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C10 · Măsuri</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Masura C10: o cifra bruta din model devine o masura definita, cu baza de raportare si reper">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C10</span><span class="hov-object">MĂSURI</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cât? Și cum definesc o măsură care răspunde corect de fiecare dată?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 3">
            <span class="sm-step">RELAȚII</span><span class="sm-arrow">·</span><span class="sm-step active">MĂSURI</span><span class="sm-arrow">·</span><span class="sm-step">COMPARAȚII</span><span class="sm-arrow">·</span><span class="sm-step">INTERPRETARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title" data-locked="1">Cât? Și cum definesc o măsură care răspunde corect de fiecare dată?</h1>
        <p class="hero-microbrief">Ai un model care răspunde la întrebări. Dar răspunsul vine ca o cifră brută: un total, o medie, un procent. Un director nu vrea o cifră, vrea o măsură în care poate avea încredere de fiecare dată, pe orice felie. O cifră calculată o dată nu este încă o măsură.</p>
        <div class="cover-miza">Aceeași întrebare poate primi trei cifre diferite, calculate în trei locuri. C10 este momentul în care cifrele brute devin măsuri definite o singură dată: cu o bază de raportare clară, ancorate într-un reper, robuste la orice tăietură. O măsură bună reduce haosul, nu îl amplifică.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">Ai toate cifrele.</span> <span class="ib-2">Și nicio decizie.</span></p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Ai un model legat corect și ceri o cifră simplă: "cât?". Și totuși:</p>
        <ul class="tu-list">
          <li>apar totaluri, medii și procente, dar fiecare loc dă altă valoare</li>
          <li>nu știi care e numitorul unui procent sau față de ce se raportează</li>
          <li>nicio cifră nu are un reper care să-i dea sens</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Oamenii calculează tot ce se poate calcula.<br><span class="tu-hl">Profesioniștii definesc măsura o singură dată.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Nu cifra contează. Contează ce întrebare răspunde cifra.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai aduni cifre. <span class="tu-hl">Definești măsuri.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>cifre brute fără o întrebare clară</li><li>aceeași cifră calculată diferit în locuri diferite</li><li>procente fără bază de raportare</li><li>niciun reper care să dea sens cifrei</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>măsuri definite o singură dată</li><li>o singură sursă de adevăr per măsură</li><li>bază de raportare declarată</li><li>reper și semnal controlabil</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>măsuri definite ca sursă unică de adevăr</li><li>bază de raportare clară pentru fiecare rată</li><li>reper definit și semnal explicabil</li><li>măsură robustă: aceeași definiție pe orice tăietură</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Măsura corectă răspunde <mark>întrebării corecte</mark>.</div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CE SE ÎNTÂMPLĂ CÂND CIFRELE NU SUNT MĂSURI</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">TOTAL FĂRĂ ÎNTREBARE</b><p class="anomaly-desc">Se adună o coloană pentru că se poate aduna. Dar fără o întrebare clară în spate, totalul nu răspunde la nimic: e o cifră, nu o măsură.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">MEDIA CARE ASCUNDE</b><p class="anomaly-desc">O medie pe tot setul pare obiectivă. Dar amestecă lucruri diferite și ascunde realitatea: aceeași medie poate descrie situații complet opuse.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">PROCENT FĂRĂ BAZĂ</b><p class="anomaly-desc">Un procent fără numitor declarat poate spune orice. "Procent din ce?" Fără baza de raportare clară, cifra pare precisă și este goală.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">TREI CIFRE PENTRU O ÎNTREBARE</b><p class="anomaly-desc">Aceeași măsură e recalculată în trei locuri și dă trei valori. Lipsește sursa unică de adevăr: nimeni nu știe care cifră e cea oficială.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">MĂSURA FRAGILĂ</b><p class="anomaly-desc">Pui un filtru sau schimbi tăietura și măsura se rupe sau dă un rezultat absurd. O măsură care nu rezistă la context nu e o măsură, e o coincidență.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · DESCHIDERE CANTITATIVĂ</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Modelul predat de C09 răspunde deja la întrebări. Acum nu mai întrebi dacă poate răspunde, ci cât: și transformi răspunsul într-o măsură.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Confirmi că datele sunt legate corect</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C10.xlsx. <span data-locked="1">Modelul vine de la C09: un fact (Vanzari) legat prin chei de dimensiuni.</span> Înainte de orice măsură, confirmi că relațiile țin. O măsură construită peste un model rupt este o cifră falsă, oricât de elegantă.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Formulezi întrebarea de business: "Cât?"</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O măsură fără întrebare e o cifră decorativă. Pornești de la întrebarea reală: "cât?". Cât în total, cât în medie, cât pe o felie. Întrebarea decide măsura, nu invers. Mai întâi întrebarea, abia apoi calculul.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Vezi că o cifră brută nu e încă o măsură</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Poți aduna o coloană în trei secunde. Dar o cifră calculată ad-hoc nu are bază declarată, nici reper, nici garanția că dă același rezultat data viitoare. O măsură este o definiție, nu un calcul de moment.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · INTEROGARE ASISTATĂ DE AI</div>
      <h2 class="stage-name">INVESTIGAȚIE</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să definești măsura, întrebi modelul ce măsură răspunde corect la întrebare și ce cifre nu merită promovate.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Ceri AI-ului ce măsură răspunde întrebării</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 1. Pentru întrebarea ta de business, AI-ul propune măsura potrivită (total, medie sau rată), ce coloană agreg și care ar fi baza de raportare. Nu definești încă; afli ce măsură răspunde corect.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · IDENTIFICAREA MĂSURII</div>
      <div class="prompt-text">Am un model cu un fact (Vanzari) legat de dimensiuni. Pentru întrebarea de business pe care o pun, spune-mi ce măsură răspunde corect (total, medie sau rată), ce coloană se agregă, care este baza de raportare (numitorul) și ce cifre din set nu merită transformate în măsuri pentru că nu răspund la nicio întrebare reală. Nu modifica datele.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Distingi cifra utilă de cifra decorativă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Nu orice cifră merită rang de măsură. Suma valorii răspunde la o întrebare; suma numerelor de factură nu răspunde la nimic. Criteriul e simplu: dacă cifra nu răspunde la o întrebare de decizie, rămâne decorativă.</p>

  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Alegi măsura potrivită întrebării</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cu raportul AI în față, alegi măsura care răspunde la întrebarea ta și îi reții baza de raportare. Aceeași felie de date poate susține măsuri diferite: alegi una, conștient, nu pe toate la grămadă.</p>
    <div class="section-sublabel">RAPORT AI · MĂSURĂ IDENTIFICATĂ</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">date</div>
      <div class="inv-item-body">
        <div class="inv-item-label">ÎNTREBAREA · "CÂT?"</div>
        <div class="inv-item-desc">Întrebarea de business e ancora măsurii: fără ea, cifra nu are sens.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">date</div>
      <div class="inv-item-body">
        <div class="inv-item-label">MĂSURĂ CANDIDAT · TOTAL / MEDIE / RATĂ</div>
        <div class="inv-item-desc">Tipul măsurii decurge din întrebare: cât în total, cât în medie, cât raportat la o bază.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">date</div>
      <div class="inv-item-body">
        <div class="inv-item-label">BAZA DE RAPORTARE · NUMITORUL</div>
        <div class="inv-item-desc">Orice rată își declară numitorul: per tranzacție, per client, per zi activă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-neutral">reper</div>
      <div class="inv-item-body">
        <div class="inv-item-label">REPER · ȚINTĂ SAU PRAG</div>
        <div class="inv-item-desc">Măsura capătă sens raportată la un reper definit, nu citită în gol.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-neutral">reper</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CONTEXT · ACEEAȘI DEFINIȚIE PE ORICE TĂIETURĂ</div>
        <div class="inv-item-desc">O măsură bună dă rezultat corect pe categorie, client sau perioadă, fără să se rescrie.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-neutral">reper</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CIFRĂ DECORATIVĂ · CE NU DEVINE MĂSURĂ</div>
        <div class="inv-item-desc">Suma numerelor de factură sau media unei constante fiscale: cifre care nu răspund la nicio întrebare.</div>
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
      <div class="stage-label">ETAPA 3 · DEFINIREA MĂSURII</div>
      <h2 class="stage-name">TRANSFORMARE</h2>
      <div class="stage-tags"><span class="phase-tag">DEFINIRE</span><span class="type-tag">Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Aici cifra brută devine măsură: o definești o singură dată, îi declari baza și o ancorezi într-un reper.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Definești măsura o singură dată</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2. Scrii definiția măsurii o singură dată, în foaia Masuri: ce agreg și pe ce model. <span data-locked="1">Aceasta devine sursa unică de adevăr.</span> Oriunde apare măsura, trimite la aceeași definiție, nu la un calcul refăcut de mână.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · DEFINIREA MĂSURII</div>
      <div class="prompt-text">Vreau să definesc măsura o singură dată, ca sursă unică de adevăr. Spune-mi definiția clară (ce agreg și pe ce bază), cum o ancorez într-un reper sau prag, ce semnal produce față de reper și cum mă asigur că aceeași definiție dă rezultat corect pe orice tăietură (categorie, client, perioadă). Distinge clar definirea măsurii de compararea ei: clasamentul și diferențele între felii vin separat, nu acum.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Declari baza de raportare</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Orice măsură relativă își declară numitorul. O medie e total împărțit la ceva: per tranzacție, per client, per zi activă. Baza de raportare nu e un detaliu, e jumătate din măsură. Schimbi baza, schimbi măsura, chiar dacă numărătorul rămâne.</p>

  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Ancorezi măsura într-un reper</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O măsură citită în gol nu spune nimic. O ancorezi într-un reper definit: o țintă sau un prag. Față de reper, măsura produce un semnal clar, peste sau sub. <span data-locked="1">Reperul transformă cifra în sens.</span></p>
    <div class="section-sublabel">DOVADA TRANSFORMĂRII</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Cifra</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">cifră brută calculată ad-hoc</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">măsură definită explicit</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Definiția</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">recalculată în mai multe locuri</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">o singură sursă de adevăr</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Baza</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">numitor neclar</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">bază de raportare declarată</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Reperul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">nicio țintă, citire în gol</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">reper definit + semnal</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Contextul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">se rupe la primul filtru</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">aceeași definiție pe orice tăietură</span></div>
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
      <div class="stage-label">ETAPA 4 · VERIFICAREA MĂSURII</div>
      <h2 class="stage-name">VERIFICARE</h2>
      <div class="stage-tags"><span class="phase-tag">CONTROL</span><span class="type-tag">Funcții de validare</span></div>
    </div>
  </header>
  <p class="stage-quote">O măsură de încredere dă același rezultat pe orice felie și un semnal clar față de reper. Verifici fiecare.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Verifici că măsura e context-aware</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În foaia Masuri_Context recalculezi aceeași măsură pe tăieturi diferite: tot setul, o categorie, un client, o perioadă. Valorile diferă pentru că tăietura diferă, nu pentru că măsura e alta. Definiția rămâne identică. Asta e o măsură robustă.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Verifici baza și reperul în foaia Masuri</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pentru fiecare măsură confirmi că baza de raportare e declarată explicit și că reperul e definit. O rată fără numitor vizibil sau o măsură fără reper nu trece verificarea: o cifră de care nu poți răspunde nu poate susține o decizie.</p>

  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Confirmi semnalul controlabil</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Măsura raportată la reper produce un semnal: peste sau sub. Semnalul e explicabil, nu o alarmă oarbă: știi exact ce măsură l-a aprins și față de ce reper. Un semnal pe care îl poți explica e un semnal controlabil.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-5" data-stage="5" data-stage-ghost="05">
  <header class="stage-header">
    <div class="stage-number">05</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 5 · ANCORARE LA SURSĂ</div>
      <h2 class="stage-name">STABILIZARE</h2>
      <div class="stage-tags"><span class="phase-tag">RECALCUL</span><span class="type-tag">Tabel structurat</span></div>
    </div>
  </header>
  <p class="stage-quote">O măsură bună nu se redefinește la fiecare felie sau sursă nouă. Se definește o dată și rămâne.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Ancorezi definiția măsurii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Definiția trăiește într-un singur loc, peste model, nu copiată în zeci de celule. Când o ceri pe altă felie, trimiți la aceeași definiție. O singură sursă de adevăr înseamnă o singură definiție de întreținut.</p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Un rând nou se include singur în măsură</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Adaugi o tranzacție nouă în fact. Măsura se recalculează singură: definiția agregă peste model, nu peste un interval fix. Nu rescrii nimic, măsura absoarbe rândul nou exact ca pe celelalte.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">Aplici regula anti-derivă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">O măsură bună supraviețuiește sursei noi. Vine exportul de luna viitoare: definiția, baza și reperul rămân valabile, iar măsura dă un rezultat comparabil. Măsura nu derivează: e ancorată la o definiție, nu la o stare de moment.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-6" data-stage="6" data-stage-ghost="06">
  <header class="stage-header">
    <div class="stage-number">06</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 6 · PREDAREA MĂSURILOR</div>
      <h2 class="stage-name">CONFIRMARE</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Cap-coadă</span></div>
    </div>
  </header>
  <p class="stage-quote">Pui întrebarea "cât?". Măsura definită răspunde la fel de fiecare dată. Apoi o predai mai departe.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">Faci prima citire a măsurii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Ceri măsura definită și primești un răspuns: o valoare, baza ei și semnalul față de reper. Aceeași întrebare pusă din nou dă același răspuns. Cifra nu mai depinde de cine o calculează sau unde.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Confirmi setul de măsuri controlabile</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci în revistă măsurile: fiecare are o întrebare, o definiție unică, o bază declarată și un reper. Niciuna nu e o cifră orfană. Ai un set de măsuri controlabile, nu o grămadă de calcule.</p>

  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Predai măsurile către C11</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">C10 definește măsuri. Atât. Care măsură e mai mare, care contribuie mai mult, ce loc ocupă fiecare felie, începe la C11. Predai un set de măsuri definite, cu valorile sursă neatinse și suma conservată.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda măsurile către C11, confirmi fiecare invariant al măsurii. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">CONTROL</div><div class="final-text">Date_MASTER-C10.xlsx deschis. Modelul legat corect, suma de control fixată la intrare.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">ÎNTREBARE</div><div class="final-text">Fiecare măsură răspunde la o întrebare clară de tip "cât?". Nicio cifră fără întrebare.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">SURSĂ UNICĂ</div><div class="final-text">Fiecare măsură e definită o singură dată, reutilizabilă. Zero cifre recalculate diferit.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">BAZĂ DE RAPORTARE</div><div class="final-text">Fiecare rată sau procent își declară numitorul: per tranzacție, per client, per zi activă.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">REPER</div><div class="final-text">Fiecare măsură de decizie e ancorată într-un reper definit: o țintă sau un prag.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">SEMNAL</div><div class="final-text">Măsura produce un semnal explicabil față de reper: știi ce măsură și față de ce prag.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">CONTEXT</div><div class="final-text">Aceeași definiție dă rezultat corect pe orice tăietură: categorie, client, perioadă.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">PREDARE</div><div class="final-text">Set de măsuri controlabile predat către C11. Valori sursă neatinse, suma conservată cap-coadă.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Set de măsuri validat.</div>
          <div class="completion-subtitle">Fiecare măsură definită, cu bază și reper. Predat către C11.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 3 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C11 · Comparații</h3>
        <p class="next-desc">Ai măsuri definite, fiecare cu bază și reper. Dar care e mai mare, care contribuie mai mult, ce loc ocupă fiecare felie? Compararea măsurilor, clasamentul și diferențele încep la C11.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Modelul răspundea deja la întrebări.</div>
        <div class="payoff-line accent">Dar fiecare cifră venea brută: fără definiție, fără bază, fără reper.</div>
        <div class="payoff-line regular">Acum fiecare măsură e definită o dată, are o bază și un reper. O ceri pe orice felie și rămâne aceeași.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Același set de date putea susține concluzii opuse. Acum cifra care primește autoritate este o măsură definită, și nu mai minte.</span></div>
        <div class="payoff-motto" data-locked="1">Nu calcula mai mult. Măsoară mai corect.</div>
      </section>

      <footer class="footer">
        TRAINITY · C10 MĂSURI · măsuri definite, controlabile
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
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">TRANSFORMARE</span><span class="nav-item-meta">3 pași · Definire</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">VERIFICARE</span><span class="nav-item-meta">3 pași · Control</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">STABILIZARE</span><span class="nav-item-meta">3 pași · Recalcul</span></span></a>
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
    # head = pana la <body> exclusiv (linii 1..1476), <body> e linia 1477 (index 1476)
    body_idx = next(i for i, l in enumerate(lines) if l.startswith('<body>'))
    script_idx = next(i for i, l in enumerate(lines) if l.startswith('<script>'))
    head = ''.join(lines[:body_idx])
    tail = ''.join(lines[script_idx:])  # <script> ... </html>

    # patch identitate in head
    head = head.replace('<title>C09 · Relații · Trainity</title>',
                        '<title>C10 · Măsuri · Trainity</title>')
    head = head.replace('/* ============ NEXT (C09) ============ */',
                        '/* ============ NEXT (C10) ============ */')
    # patch STORAGE_KEY in tail
    tail = tail.replace('trainity_c09_study_v1', 'trainity_c10_study_v1')

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    # garda: nu trebuie sa ramana tokeni C09 reziduali in continut
    leftover = re.findall(r'C09|trainity_c09|Date_MASTER-C09|Relatii_Model', out)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  leftover C09 tokens:', len(leftover), leftover[:5])
    # garda anti-drift C11/C12: termeni interzisi in C10 (in afara de mentiunile explicite de predare/distinctie)
    for term in ['clasament', 'ranking', 'Pareto', 'contribuie mai mult']:
        n = out.count(term)
        if n:
            print('  NOTA termen C11 prezent (%dx): %s (verifica sa fie doar in predare/distinctie)' % (n, term))


if __name__ == '__main__':
    main()
