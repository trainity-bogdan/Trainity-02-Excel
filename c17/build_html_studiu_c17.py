#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c17.py - HTML-Studiu-Excel-17-Sistematizare.html prin COPY+MODIFY din c16.

Strategie: pastrez head+CSS si JS din c16 (generice), inlocuiesc DOAR <body>..<script>
cu narativ C17 SISTEMATIZARE. Patch title + STORAGE_KEY + NEXT.

Axa C17: RELUABILITATEA / forma reluabila. T5 AUTONOMIE. Autorul iese din OCAZIE.
Artefact central: foaia _SISTEM (harta functionala nativ-Excel).
Garda OGLINDA: _SISTEM oglindeste, leaga, navigheaza. NU executa (C18), NU judeca
praguri/validari (C19), NU muta ownership (C20). Anti-SOP: se rupe scoasa din workbook.
Zero cifre business in pagina (R-V02.15). Zero em-dash.
"""
import re, os

SRC = 'c16/HTML-Studiu-Excel-16-Livrare.html'
OUT = 'c17/HTML-Studiu-Excel-17-Sistematizare.html'

HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>SISTEM RELUABIL</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C17 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C17 · SISTEM</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

            <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Sistematizare C17: o munca pe care o stiai doar tu devine o harta vie in workbook, pe care altcineva o porneste si o reia fara tine">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C17</span><span class="hov-object">SISTEMATIZAREA MUNCII RELUABILE</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cum transform munca pe care doar eu o știu într-un sistem pe care altcineva îl pornește?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 5">
            <span class="sm-step active">SISTEMATIZARE</span><span class="sm-arrow">·</span><span class="sm-step">AUTOMATIZARE</span><span class="sm-arrow">·</span><span class="sm-step">GUVERNARE</span><span class="sm-arrow">·</span><span class="sm-step">DELEGARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title">Cum să transformi o muncă pe care o repeți într-un sistem pe care altcineva îl poate relua</h1>
        <p class="hero-microbrief">Raportul e gata, predat o dată. Dar l-ai făcut tu. În concediu, munca se oprește: tu ești ocazia, fără tine nu pornește. Aici nu mai faci raportul, faci munca reluabilă. O scrii ca hartă vie în workbook, legată de foile reale, pe care un om instruit o pornește fără tine.</p>
        <div class="cover-miza">C17 nu refece raportul și nu îl automatizează: ia munca pe care ai făcut-o și o face sistem. Construiești foaia _SISTEM, o hartă funcțională a workbook-ului: componentele reale, sursele, ordinea de reluare, totul prin legături vii care se rup dacă scoți foaia din fișier. Nu o procedură de citit, un sistem care trăiește în Excel. C17 face munca reluabilă de altcineva; să ruleze singură începe la treapta următoare.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1"><span class="ib-1">Munca ta merge perfect.</span> <span class="ib-2">Până pleci tu.</span></p>
      </section>

      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Munca merge, raportul iese, totul e în regulă. Și totuși:</p>
        <ul class="tu-list">
          <li>de fiecare dată o reiei din memorie, cu mici variații, fără un loc unde scrie cum</li>
          <li>nimeni altcineva nu poate porni procesul fără să te întrebe pe tine de unde începe</li>
          <li>pleci o săptămână și munca se oprește, fiindcă trăiește doar în capul tău</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Nu ai un proces.<br><span class="tu-hl">Ai o memorie personală care ține un Excel în viață.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">O muncă făcută de două ori nu mai e o livrare. E un sistem ascuns în workbook.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai ești omul care ține munca. <span class="tu-hl">Ești omul care o face sistem.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>munca trăiește doar în capul tău, nescrisă</li><li>fiecare reluare începe cu „de unde plecam?"</li><li>doar tu poți porni procesul, ești ocazia</li><li>în concediu, munca se oprește</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>munca e o hartă vie în workbook, legată de foile reale</li><li>componente, surse și ordine de reluare, scrise o dată</li><li>un om instruit pornește din foaie, fără tine</li><li>poți lipsi, munca are cine s-o reia</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>foaia _SISTEM: harta funcțională reluabilă a muncii</li><li>componente, surse și pași legați de obiectele reale din workbook</li><li>convențiile scoase din cap în parametri vii</li><li>un sistem pe care altcineva îl pornește fără tine</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1">Nu o fac din nou. <mark>O fac sistem.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CELE ȘASE FELURI ÎN CARE MUNCA RĂMÂNE LEGATĂ DE TINE</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">CUNOAȘTERE TRIBALĂ</b><p class="anomaly-desc">Procesul trăiește doar în capul tău, nescris nicăieri. Corecția: îl scrii ca hartă vie în foaia _SISTEM, legată de componentele reale.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">RELUARE DIN MEMORIE</b><p class="anomaly-desc">De fiecare dată reconstruiești pașii din minte, cu mici variații. Corecția: ordinea de reluare se scrie o dată, ca lanț de pași legați de obiecte.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">SURSĂ AMBIGUĂ</b><p class="anomaly-desc">Aceeași intrare vine din două locuri, nu se știe care e cea bună. Corecția: o singură sursă de adevăr per intrare, fixată ca named range SRC_.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">CONVENȚII NESCRISE</b><p class="anomaly-desc">Alegerile tale („așa fac eu") nu sunt nicăieri, doar tu le știi. Corecția: convențiile devin parametri vii în workbook, named ranges PARAM_.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">DOAR TU POȚI PORNI</b><p class="anomaly-desc">Nimeni nu reia procesul fără să te întrebe de unde începe. Corecția: scrii profilul de competență care poate relua, nu numele tău.</p></div>
<div class="anomaly-card"><span class="anomaly-num">06</span><b class="anomaly-title">GÂTUIREA PE AUTOR</b><p class="anomaly-desc">Pleci, munca se oprește, fiindcă ești singurul punct prin care trece. Corecția: harta reluabilă scoate munca din tine, fără să o automatizeze încă.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · MUNCA PE CARE O ȘTII DOAR TU</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Munca e validată și raportul iese. Înainte de orice hartă, vezi pe viu că reluarea trăiește doar în capul tău: tu ești ocazia.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Workbook-ul merge, dar numai cu tine la cârmă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C17-Sistematizare.xlsx. <span data-locked="1">Vine cu tot procesul care a produs raportul: surse, foi de lucru, raportul de decizie.</span> Funcționează. Dar ca să-l reiei, trebuie să știi din cap de unde pleci și în ce ordine. E muncă, nu sistem.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">Dai workbook-ul altcuiva și se blochează</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Rogi un coleg instruit să reia munca fără tine. Se uită la foile împrăștiate și întreabă: „de unde încep, care e sursa, în ce ordine?". Lipsa nu e de date, e de hartă. Munca e prizonieră în memoria ta.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Creezi foaia _SISTEM și declari harta reluabilă</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Adaugi o foaie nouă, _SISTEM, și o fixezi prima. <span data-locked="1">Aici nu copiezi date și nu scrii o procedură de citit: construiești o hartă vie, legată de foile reale.</span> Declari intenția: munca asta devine un sistem pe care altcineva îl pornește.</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · INVENTARUL COMPONENTELOR REALE</div>
      <h2 class="stage-name">INVENTAR</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să scrii pașii, vezi din ce e făcută munca: ce foi, ce tabele, ce surse reale există în workbook.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Ce componente are de fapt munca</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te întrebi nu „ce raport iese?", ci „din ce e făcut procesul?". Descoperi părțile reale: foile-sursă, foile de lucru, foaia-raport. Componentele există deja în workbook; tu doar le faci vizibile și navigabile.</p>

  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Promptul 1: AI inventariază componentele reale</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 1. AI-ul parcurge workbook-ul și propune lista componentelor: ce foi sunt surse, ce e lucru, ce e ieșire. Nu construiește harta și nu automatizează nimic; doar îți arată din ce e făcut procesul. AI propune inventarul, tu confirmi rolurile.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · INVENTARUL COMPONENTELOR REALE</div>
      <div class="prompt-text">Am un workbook care a produs un raport. Parcurge foile lui și fă-mi un inventar al componentelor reale: pentru fiecare foaie, spune dacă e sursă, foaie de lucru sau ieșire, și ce rol are în proces. Propune o listă, dar nu construi nicio hartă și nu hotărî tu rolurile finale; eu confirm. Nu automatiza nimic, nu adăuga reguli sau praguri, nu desemna responsabili. Vreau doar să văd din ce e făcută munca.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Blocul A: componentele reale, prin legături vii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În _SISTEM construiești blocul A: fiecare componentă e un HYPERLINK către foaia reală, lângă o oglindă cu cât conține, prin COUNTA. Componenta se numără singură. Click pe link și ești în foaia reală. Harta nu descrie munca, o arată vie.</p>
    <div class="section-sublabel">BLOCUL A · COMPONENTE (OGLINDĂ + NAVIGARE)</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">sursă</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FOILE-SURSĂ · HYPERLINK + COUNTA</div>
        <div class="inv-item-desc">Tabelul fact și dimensiunile, fiecare cu un link viu și câte rânduri are acum.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">lucru</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FOILE DE LUCRU · NAVIGABILE</div>
        <div class="inv-item-desc">Pașii intermediari care duc la raport, legați prin link la zona reală.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">ieșire</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FOAIA-RAPORT · CAPĂTUL LANȚULUI</div>
        <div class="inv-item-desc">Unde stă rezultatul livrabil, ca destinație a reluării.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu execută</div>
      <div class="inv-item-body">
        <div class="inv-item-label">OGLINDĂ, NU MOTOR</div>
        <div class="inv-item-desc">COUNTA arată starea, nu o schimbă. Harta nu rulează munca, doar o reflectă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu judecă</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FĂRĂ PRAG, FĂRĂ ALERTĂ</div>
        <div class="inv-item-desc">Oglinda nu spune „prea puțin" sau „greșit". Doar afișează ce există.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">se rupe scoasă</div>
      <div class="inv-item-body">
        <div class="inv-item-label">LEGATĂ DE FOILE REALE</div>
        <div class="inv-item-desc">Ștergi foaia, link-ul moare și COUNTA dă eroare. Harta trăiește doar în workbook.</div>
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
      <div class="stage-label">ETAPA 3 · O SINGURĂ SURSĂ PENTRU FIECARE INTRARE</div>
      <h2 class="stage-name">SURSĂ</h2>
      <div class="stage-tags"><span class="phase-tag">FORMĂ</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">O hartă reluabilă cere un singur adevăr per intrare. Fixezi sursa canonică, ca nimeni să nu mai întrebe „care fișier?".</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Fiecare intrare, o singură sursă de adevăr</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pentru fiecare intrare a muncii, alegi sursa canonică și o fixezi ca named range SRC_. <span data-locked="1">Nu copiezi datele, le legi: SRC_ pointează zona reală.</span> Reluarea nu mai întreabă „de unde?"; numele spune singur.</p>

  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Elimini dublura sursei</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Dacă o intrare venea din două locuri, declari unul singur canonic. Ambiguitatea dispare: o intrare, o sursă, un nume. Cine reia nu mai alege între variante, urmează harta.</p>

  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Blocul B: SRC_ cu oglinda lui vie</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În blocul B, lângă fiecare SRC_ pui o oglindă: ROWS(SRC_), câte rânduri are sursa acum. <span data-locked="1">Oglinda doar arată, nu verifică un prag și nu blochează nimic.</span> Sursa e legată de zona reală: scoți zona, oglinda dă eroare.</p>
    <div class="section-sublabel">DOVADA RELUABILITĂȚII</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Sursa</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">știută doar de tine</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">named range SRC_, vizibil</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Intrarea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">din două locuri, ambiguă</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">o singură sursă canonică</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Verificarea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">deschideai și numărai manual</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">ROWS(SRC_) oglindește live</span></div>
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
      <div class="stage-label">ETAPA 4 · ORDINEA DE RELUARE, LEGATĂ DE OBIECTE</div>
      <h2 class="stage-name">RELUARE</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 2</span></div>
    </div>
  </header>
  <p class="stage-quote">Acum scrii pașii de reluare ca lanț navigabil: fiecare pas duce la obiectul real și arată ce iese, fără să automatizezi.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Ordinea de reluare, pas cu pas</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Scrii secvența reală: deschizi sursa, recalculezi măsurile, citești clasamentul, iei mesajul, predai raportul. Fiecare pas e o acțiune de om, în ordine. Harta spune ce se face și unde, nu o face în locul tău.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Promptul 2: lanțul de pași legați de obiecte</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Lansezi Promptul 2. AI-ul propune ordinea pașilor și, pentru fiecare, obiectul real atins și ce rezultat apare. Marchează și care pași s-ar putea automatiza mai târziu, fără să-i automatizeze acum. AI așază lanțul; tu confirmi ordinea și legăturile.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · LANȚUL DE RELUARE LEGAT DE OBIECTE</div>
      <div class="prompt-text">Pe baza componentelor și surselor confirmate, propune-mi ordinea de reluare a muncii ca lanț de pași. Pentru fiecare pas spune ce obiect real din workbook se atinge și ce rezultat devine vizibil. Marchează care pași sunt repetitivi și ar fi candidați de automatizare mai târziu, dar nu îi automatiza și nu scrie niciun macro. Nu adăuga reguli, praguri sau validări, nu stabili cine răspunde. Pașii rămân acțiuni de om, în ordine.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Blocul C: pași, obiect atins, rezultat oglindit</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În blocul C, fiecare pas e un HYPERLINK la zona lui, cu obiectul atins ca named range OBJ_ și rezultatul oglindit live. <span data-locked="1">Pașii repetitivi îi etichetezi „candidat C18", dar îi lași manuali.</span> Harta arată ce iese, nu produce ea rezultatul.</p>
    <div class="section-sublabel">BLOCUL C · LANȚUL DE RELUARE</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Pasul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">în memoria ta</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">HYPERLINK la obiectul real</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Rezultatul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">îl verificai din cap</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">oglindit live, ca reper</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Automatizarea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">tentația de a o face acum</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">etichetă „candidat C18", amânată</span></div>
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
      <div class="stage-label">ETAPA 5 · CUNOAȘTEREA SCOASĂ DIN CAP</div>
      <h2 class="stage-name">EXTERNALIZARE</h2>
      <div class="stage-tags"><span class="phase-tag">FORMĂ</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Ce știai doar tu devine vizibil: convențiile ca parametri vii, iar cine poate relua ca profil de competență, nu ca nume.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">Convențiile din capul tău devin parametri vii</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Alegerile pe care le făceai „așa, că știu eu" le scrii ca named ranges PARAM_, cu valoarea în celulă. <span data-locked="1">Sursa canonică, categoria pe care se concentrează raportul, foaia finală: toate devin parametri vizibili.</span> Reluarea le citește din workbook, nu din tine.</p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Cine poate relua: profil de competență, nu nume</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În blocul D scrii ce fel de om poate porni harta: ce competență minimă îi trebuie, nu cine anume. <span data-locked="1">Nu numești un titular și nu predai răspunderea, doar descrii profilul care poate relua.</span> Sistemul rămâne deschis oricui instruit.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">Blocul D și E: profil plus parametri</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Harta are acum tot ce trăia în capul tău: profilul care poate relua și parametrii care ghidează pașii. <span data-locked="1">Nimic „cum știu eu" nesemnat: dacă un pas cerea o alegere, alegerea e scrisă ca PARAM_.</span> Cunoașterea tribală a ieșit din tine în workbook.</p>
    <div class="section-sublabel">CE A IEȘIT DIN CAP</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">scris</div>
      <div class="inv-item-body">
        <div class="inv-item-label">CONVENȚIILE · PARAM_</div>
        <div class="inv-item-desc">Alegerile de proces, ca valori vii în workbook, nu în memoria ta.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">scris</div>
      <div class="inv-item-body">
        <div class="inv-item-label">PROFILUL · CINE POATE RELUA</div>
        <div class="inv-item-desc">Competența minimă, nu un nume. Reluabil de oricine instruit.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu predat</div>
      <div class="inv-item-body">
        <div class="inv-item-label">FĂRĂ TITULAR, FĂRĂ ESCALADARE</div>
        <div class="inv-item-desc">C17 spune cine poate, nu cine deține. Predarea proprietății e altă treaptă.</div>
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
      <div class="stage-label">ETAPA 6 · TESTUL SUBSTITUTULUI</div>
      <h2 class="stage-name">SUBSTITUT</h2>
      <div class="stage-tags"><span class="phase-tag">HANDOFF</span><span class="type-tag">Predare C18</span></div>
    </div>
  </header>
  <p class="stage-quote">Proba finală: altcineva pornește din _SISTEM și reia munca fără tine. Apoi marchezi unde se oprește C17 și începe automatizarea.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">START AICI și punctul de reluare</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În blocul F pui un START AICI, un HYPERLINK către primul pas, și un punct de reluare, unde reintri dacă te-ai oprit. <span data-locked="1">Oricine deschide harta știe de unde începe, fără să te întrebe.</span> Intrarea în sistem e una singură, scrisă.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Testul substitutului: altcineva reia, fără tine</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Dai workbook-ul colegului instruit și pleci din cameră. <span data-locked="1">Pornește din START AICI, urmează linkurile, atinge obiectele, vede rezultatele, reia munca cap la cap doar din foaie.</span> Dacă trebuie să te întrebe ceva nescris, mai ai de scris. Dacă nu, munca e reluabilă fără tine.</p>
    <div class="section-sublabel">TESTUL ANTI-SOP, PE VIU</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">trece</div>
      <div class="inv-item-body">
        <div class="inv-item-label">PORNEȘTE DOAR DIN FOAIE</div>
        <div class="inv-item-desc">Substitutul reia munca fără să te întrebe. Harta se susține singură.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">trece</div>
      <div class="inv-item-body">
        <div class="inv-item-label">SE RUPE SCOASĂ DIN WORKBOOK</div>
        <div class="inv-item-desc">Copiezi _SISTEM în Word: link-uri moarte, oglinzi în eroare. Nu e o procedură, e o hartă vie.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">pică</div>
      <div class="inv-item-body">
        <div class="inv-item-label">UN PAS „CUM ȘTIU EU"</div>
        <div class="inv-item-desc">Dacă substitutul se blochează pe o alegere nescrisă, mai e cunoaștere în capul tău.</div>
      </div>
    </li>
    </ul>
  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Granița C17 spre C18: harta e gata, treapta următoare o pune să ruleze</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">C17 face munca reluabilă de un om. Treapta următoare scoate omul din pașii repetitivi.</span> Predai o hartă cu pașii „candidat C18" marcați, gata de automatizat. Automatizarea, guvernarea prin reguli și predarea proprietății încep mai sus. Tu ai garantat că munca se reia fără tine.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda harta reluabilă treptei următoare, confirmi fiecare invariant al sistematizării. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">_SISTEM EXISTĂ</div><div class="final-text">Date_MASTER-C17-Sistematizare.xlsx are foaia _SISTEM, prima, ca hartă a muncii.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">COMPONENTE VII</div><div class="final-text">Foile reale, prin HYPERLINK și COUNTA. Click duce la foaie, oglinda arată starea.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">O SINGURĂ SURSĂ</div><div class="final-text">Fiecare intrare are un singur SRC_, sursă canonică, fără ambiguitate.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">ORDINE NAVIGABILĂ</div><div class="final-text">Pașii, ca lanț de linkuri spre obiectele reale, cu rezultatul oglindit.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">CONVENȚII SCRISE</div><div class="final-text">Alegerile din cap, ca named ranges PARAM_, vii în workbook. Nimic „cum știu eu".</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">PROFIL, NU NUME</div><div class="final-text">Cine poate relua e o competență, nu o persoană. Fără titular, fără escaladare.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">ANTI-SOP</div><div class="final-text">Scoasă din workbook, harta se rupe: linkuri moarte, oglinzi în eroare. Trăiește legată de foi.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">RELUABIL FĂRĂ AUTOR</div><div class="final-text">Substitutul pornește din foaie și reia munca fără tine. Gata de predat la automatizare.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Munca a devenit sistem.</div>
          <div class="completion-subtitle">Reluabilă fără autor. Gata de pus să ruleze la treapta următoare.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">TREAPTA 5 · CONSTRUCȚIA URMĂTOARE</div>
        <h3 class="next-title">C18 · Automatizarea</h3>
        <p class="next-desc">Ai un sistem reluabil de un om, cu pașii „candidat C18" marcați. Dar cum scoți omul din pașii repetitivi, ca munca să ruleze fără să o pornească cineva de fiecare dată? Automatizarea începe la C18.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Munca era validată și raportul ieșea de fiecare dată.</div>
        <div class="payoff-line accent">Dar o făceai tu: în concediu se oprea, fiindcă trăia doar în capul tău.</div>
        <div class="payoff-line regular">Acum munca e o hartă vie în workbook, legată de foile reale, pe care un om instruit o pornește fără tine, din _SISTEM.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Un proces care trăia doar în capul tău. Acum o hartă vie în workbook, pe care altcineva o pornește fără tine.</span></div>
        <div class="payoff-motto" data-locked="1">Pleci, și munca o reia altcineva.</div>
      </section>

      <footer class="footer">
        TRAINITY · C17 SISTEMATIZARE · munca devine un sistem reluabil fără autor
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
<a class="nav-item" data-nav-stage="2" href="#stage-2" onclick="navigateStage(2,event)"><span class="nav-item-num">2</span><span class="nav-item-text"><span class="nav-item-name">INVENTAR</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">SURSĂ</span><span class="nav-item-meta">3 pași · Manual</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">RELUARE</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">EXTERNALIZARE</span><span class="nav-item-meta">3 pași · Manual</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">SUBSTITUT</span><span class="nav-item-meta">3 pași · Handoff</span></span></a></div>

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

    head = re.sub(r'<title>.*?</title>', '<title>C17 · Sistematizare · Trainity</title>', head, count=1)
    head = re.sub(r'NEXT \(C\d+\)', 'NEXT (C17)', head)
    tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c17_study_v1', tail)

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c17', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # garda: tokeni sursa c16 reziduali in CONTINUT (body)
    leftover = re.findall(r'trainity_c16|Date_MASTER-C16|Livrare|LIVRARE|decizie de luat|raport-decizie|decision-ready', body)
    print('  leftover C16 tokens in BODY (trebuie 0):', len(leftover), leftover[:8])
    # garda contaminare C18/C19/C20 ca IDENTITATE (granita/handoff sunt ok)
    c18 = re.findall(r'automatiz', body, re.IGNORECASE)
    print('  "automatiz" in BODY (doar candidat C18/handoff, verifica context):', len(c18))
    c19 = re.findall(r'\bvalidare\b|\bprag\b|\bvalideaz', body, re.IGNORECASE)
    print('  C19 (validare/prag) in BODY (trebuie ~0, doar negatii):', len(c19), c19[:6])
    # garda anti-em-dash
    for ch in ['—', '–']:
        if ch in body:
            print('  ATENTIE em/en-dash in BODY!')
    print('  steps:', body.count('data-step="'), '| stages:', body.count('data-stage="') - body.count('data-stage-ghost'))
    print('  anomaly-card:', body.count('anomaly-card'), '| final-card:', body.count('final-card'), '| prompturi:', body.count('prompt-box'))


if __name__ == '__main__':
    main()
