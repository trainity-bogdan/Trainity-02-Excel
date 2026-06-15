#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_studiu_c20.py - HTML-Studiu-Excel-20-Delegare.html prin COPY+MODIFY din c19.

Strategie (oglinda build_html_studiu_c19.py): pastrez head+CSS si JS din c19 (generice),
inlocuiesc DOAR <body>..<script> cu narativ C20 DELEGARE. Patch title + mobile-topbar +
STORAGE_KEY. HERO = SVG placeholder inline (imaginile DELEGARE nu exista inca -> DRAFT).

Axa C20: DELEGAREA / predarea proprietatii. T5 AUTONOMIE. Autorul iese din PROPRIETATE.
Artefact central: foaia _DELEGARE (test VIU: AUTOR_ACTIV + ROL_DELEGAT + harta de predare +
V1-V4 + STATUS calculat NEPREDAT/PARTIAL/DELEGAT/AUTONOM). Verb-semnatura: DELEG.
Formula treapta: C18 ruleaza · C19 se tine corect · C20 PREDA proprietatea.
Garda: _DELEGARE este TEST VIU, nu tabel pasiv (anti-RACI). Rol, nu persoana.
Granita vs C19: C19 prinde un INPUT gresit (date); C20 prinde DEPENDENTA de autor (proprietate).
NU management, NU HR, NU fisa de post, NU SOP/documentare. C20 inchide PACK-ul C01-C20.
Zero cifre business (R-V02.15). Zero em-dash / en-dash.
"""
import re, os

SRC = 'c19/HTML-Studiu-Excel-19-Guvernare.html'
OUT = 'c20/HTML-Studiu-Excel-20-Delegare.html'

# HERO placeholder SVG inline (DRAFT: nu exista imagini finale DELEGARE)
HERO_PLACEHOLDER = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
    "</linearGradient></defs><rect width='1200' height='800' fill='url(%23g)'/>"
    "<text x='60' y='410' fill='%23FFD400' font-family='Georgia' font-size='58' "
    "font-weight='bold'>AUTONOMIE</text>"
    "<text x='62' y='462' fill='%23ffffff' font-family='Arial' font-size='24' "
    "opacity='0.7'>C20 · placeholder hero</text></svg>"
)

BODY = r'''<body>

<div class="top-progress"><div class="top-progress-fill" id="topProgressFill"></div></div>

<div class="mobile-topbar" role="banner">
  <div class="mobile-topbar-title">C20 · Delegare</div>
  <div class="mobile-topbar-progress" id="mobileTopProgress">0/18</div>
  <button class="mobile-nav-toggle" id="mobileToggleBtn" onclick="toggleMobileNav()" aria-label="Meniu"></button>
</div>
<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>

<div class="book-app">
  <div class="app-grid">

    <main class="main-content">

      <header class="cover">
        <div class="hero-visual">
          <img class="hero-visual-img" src="__HERO__" alt="Delegare C20: un sistem care merge si se pazeste singur, dar inca al tau, este predat unui rol care il poate detine si continua fara tine; apesi scoate autorul si statusul devine autonom singur">
          <div class="hero-visual-overlay"><span class="hov-kicker">OBIECTUL CONSTRUCȚIEI · C20</span><span class="hov-object">DELEGAREA SISTEMULUI DE LUCRU</span></div>
        </div>
        <div class="hero-question"><span class="hero-question-label">ÎNTREBAREA CONSTRUCȚIEI</span><span class="hero-question-text" data-locked="1">Cum deleg sistemul, ca să meargă fără mine?</span></div>
        <div class="hero-tiernav">
          <div class="system-map" aria-label="harta treptei 5">
            <span class="sm-step">SISTEMATIZARE</span><span class="sm-arrow">·</span><span class="sm-step">AUTOMATIZARE</span><span class="sm-arrow">·</span><span class="sm-step">GUVERNARE</span><span class="sm-arrow">·</span><span class="sm-step active">DELEGARE</span>
          </div>
        </div>
      </header>

      <section class="study-intro-top">
        <h1 class="cover-title">Cum predai proprietatea unui sistem care merge fără tine, ca să nu mai depindă de tine</h1>
        <p class="hero-microbrief">Sistemul tău rulează singur (C18) și se păzește singur (C19). Și totuși e încă al tău, și numai al tău: la orice problemă, tot pe tine te sună. Un sistem care depinde de o singură persoană nu e autonom, e doar bine întreținut de acea persoană. Aici nu mai întrebi „merge?". Predai proprietatea unui rol, și o dovedești în workbook: apeși „scoate autorul" și sistemul confirmă singur că alt rol îl poate continua.</p>
        <div class="cover-miza">C20 nu pornește sistemul și nu îi scrie regulile: ia un sistem guvernat și îi predă proprietatea. Construiești foaia _DELEGARE: rolul care preia, harta de predare și testul viu. Apeși „scoate autorul" și STATUS se reașază singur: NEPREDAT, PARȚIAL, DELEGAT, AUTONOM. Dependența ascunsă pe care doar tu o știai aprinde un FAIL, o muți pe rol, și abia atunci sistemul nu mai e al tău. C20 închide pachetul C01-C20.</div>
      </section>

      <section class="intriga-bomb">
        <p class="cover-subtitle" data-locked="1">Sistemul tău merge fără tine. Dar la orice problemă, tot pe tine te sună.</p>
      </section>

      <!-- ARC TU: recunoastere -> greseala -> aha -> cine devii -->
      <section class="tu-section tu-recunoastere">
        <div class="tu-kicker">SUNĂ CUNOSCUT?</div>
        <p class="tu-lead">Sistemul rulează singur și se păzește singur. Și totuși nu poți pleca. Și totuși:</p>
        <ul class="tu-list">
          <li>la orice problemă, tot pe tine te sună: ești proprietarul informal</li>
          <li>nimeni nu știe sigur ce are voie să atingă cel care ar prelua</li>
          <li>dacă pleci o lună, sistemul rămâne orfan, deși merge perfect</li>
        </ul>
      </section>
      <section class="tu-section tu-greseala">
        <div class="tu-kicker">GREȘEALA CLASICĂ</div>
        <p class="tu-statement" data-locked="1">Crezi că ai delegat când ai explicat.<br><span class="tu-hl">Dar explicația nu mută proprietatea: la prima problemă, tot pe tine te sună.</span></p>
      </section>
      <section class="tu-section tu-aha">
        <div class="tu-kicker">AHA</div>
        <p class="tu-statement" data-locked="1">Un sistem nu e autonom pentru că merge singur. E autonom când îl poate deține altcineva.</p>
      </section>
      <section class="tu-section tu-promise">
        <div class="tu-kicker">CINE DEVII</div>
        <p class="tu-statement" data-locked="1">Nu mai ești proprietarul care ține sistemul în viață. <span class="tu-hl">Ești cel care îl predă unui rol.</span></p>
      </section>

      <section class="study-intro">
        <div class="hero-beforeafter">
          <div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul><li>la orice problemă, tot pe tine te sună</li><li>proprietatea e informală, nescrisă</li><li>nimeni nu știe dacă rolul poate opera singur</li><li>pleci, și sistemul rămâne orfan</li></ul></div>
          <div class="ba-arrow">→</div>
          <div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul><li>proprietatea trece de la o persoană la un rol</li><li>harta de predare alimentează un test viu</li><li>scoți autorul, STATUS se reașază singur</li><li>poți lipsi o lună, rolul continuă</li></ul></div>
        </div>
      </section>
      <section class="study-result">
        <div class="hero-outcomes"><div class="outcomes-label">CE VEI OBȚINE</div><ul class="outcomes-list"><li>foaia _DELEGARE: testul viu al predării proprietății</li><li>rolul care preia, harta de predare, accesul și escaladarea</li><li>comutatorul „scoate autorul" și V1-V4 care se reașază singure</li><li>STATUS calculat: NEPREDAT, PARȚIAL, DELEGAT, AUTONOM</li></ul></div>
      </section>

      <div class="mantra-band">
        <div class="mantra-band-sub">MANTRA · TRAINITY</div>
        <div class="mantra-band-main" data-locked="1"><mark>Nu împart sarcini. Deleg sistemul.</mark></div>
      </div>

      <section>
        <div class="section-marker">SCENA REALĂ · CE PARE DELEGARE DAR TE LASĂ TOT PROPRIETAR</div>
        <div class="anomaly-grid">
<div class="anomaly-card"><span class="anomaly-num">01</span><b class="anomaly-title">EXPLICAȚIA</b><p class="anomaly-desc">I-ai explicat cum merge, deci crezi că ai predat. Dar explicația nu mută proprietatea. Corecția: predarea se dovedește în workbook prin testul viu, nu printr-un discurs.</p></div>
<div class="anomaly-card"><span class="anomaly-num">02</span><b class="anomaly-title">PROPRIETATE INFORMALĂ</b><p class="anomaly-desc">Toți știu că „e al lui", dar nicăieri nu scrie cine îl deține. Corecția: proprietatea trece explicit pe un ROL, cu zonă deținută și backup, nu rămâne o convenție tăcută.</p></div>
<div class="anomaly-card"><span class="anomaly-num">03</span><b class="anomaly-title">PERSOANA, NU ROLUL</b><p class="anomaly-desc">Predai unui om anume. Pleacă omul, pleacă sistemul. Corecția: proprietatea stă pe un rol; persoana se atașează temporar la rol, nu invers.</p></div>
<div class="anomaly-card"><span class="anomaly-num">04</span><b class="anomaly-title">ACCES NECLAR</b><p class="anomaly-desc">Cel care ar prelua nu știe ce vede, ce modifică, unde nu are voie. Corecția: o matrice rol pe zonă spune exact accesul, iar limitele sunt ranges chiar blocate.</p></div>
<div class="anomaly-card"><span class="anomaly-num">05</span><b class="anomaly-title">ESCALADARE VERBALĂ</b><p class="anomaly-desc">„Dacă apare ceva, mă suni." Escaladarea trăiește în vorbe, nu se poate dovedi. Corecția: escaladarea urcă la un ROL, cu un declanșator scris, nu la un semnal C19.</p></div>
<div class="anomaly-card"><span class="anomaly-num">06</span><b class="anomaly-title">SISTEM ORFAN</b><p class="anomaly-desc">Predarea nu poate fi verificată: nimeni nu știe dacă rolul chiar poate opera singur. Corecția: scoți autorul pe viu și sistemul dovedește singur dacă se ține fără tine.</p></div>
</div>
      </section>

      <section class="stage" id="stage-1" data-stage="1" data-stage-ghost="01">
  <header class="stage-header">
    <div class="stage-number">01</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 1 · Sistemul merge, dar e încă al tău</div>
      <h2 class="stage-name">REALITATE</h2>
      <div class="stage-tags"><span class="phase-tag">INPUT</span><span class="type-tag">Manual</span></div>
    </div>
  </header>
  <p class="stage-quote">Sistemul rulează singur și se păzește singur. Înainte de orice hartă, vezi pe viu de ce tot nu poți pleca: la orice problemă, tot pe tine te sună. Ești proprietarul informal.</p>
  <div class="stage-body">
<div class="step" data-step="1">
  <div class="step-head" onclick="toggleStep(1)">
    <div class="step-marker">PAS 01</div>
    <h3 class="step-title">Sistemul rulează și se păzește singur, dar tot pe tine te sună</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(1)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Date_MASTER-C20-Delegare.xlsx. <span data-locked="1">Vine cu sistemul moștenit: motorul rulează (C18) și regulile îl țin corect (C19).</span> Și totuși, la orice problemă, telefonul sună la tine. Ești proprietarul informal: sistemul merge, dar nu are alt deținător decât tine.</p>

  </div>
</div>
<div class="step" data-step="2">
  <div class="step-head" onclick="toggleStep(2)">
    <div class="step-marker">PAS 02</div>
    <h3 class="step-title">„Merge fără efort" nu înseamnă „are alt proprietar"</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(2)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">În sistemul moștenit, C18 a scos efortul și C19 a scos supravegherea. Dar autonomia e încă falsă: <span data-locked="1">sistemul depinde de disponibilitatea ta de a răspunde.</span> Un sistem care rulează perfect, dar pe care îl deține o singură persoană, nu e autonom, e doar bine întreținut de acea persoană.</p>

  </div>
</div>
<div class="step" data-step="3">
  <div class="step-head" onclick="toggleStep(3)">
    <div class="step-marker">PAS 03</div>
    <h3 class="step-title">Deschizi _DELEGARE cu AUTOR_ACTIV=DA: STATUS=NEPREDAT</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(3)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Adaugi o foaie nouă, _DELEGARE, și o fixezi ca foaia predării. <span data-locked="1">Aici nu pornești sistemul și nu îi scrii regulile: îi predai proprietatea.</span> Comutatorul AUTOR_ACTIV e pe DA, harta e goală: STATUS arată NEPREDAT. Pui testul concediului: dacă pleci o lună, sistemul rămâne orfan?</p>

  </div>
</div>
  </div>
</section>

<section class="stage" id="stage-2" data-stage="2" data-stage-ghost="02">
  <header class="stage-header">
    <div class="stage-number">02</div>
    <div class="stage-meta">
      <div class="stage-label">ETAPA 2 · Ce te face indispensabil</div>
      <h2 class="stage-name">DEPENDENȚĂ</h2>
      <div class="stage-tags"><span class="phase-tag">AI</span><span class="type-tag">Copilot · Promptul 1</span></div>
    </div>
  </header>
  <p class="stage-quote">Înainte să predai, vezi ce te face indispensabil: ce inputuri ale sistemului atârnă de tine, ținute în cap sau în foi personale, și care au deja o sursă pe care un rol o poate folosi.</p>
  <div class="stage-body">
<div class="step" data-step="4">
  <div class="step-head" onclick="toggleStep(4)">
    <div class="step-marker">PAS 04</div>
    <h3 class="step-title">Inventariezi din _SISTEM ce inputuri atârnă de tine, le marchezi AUTHOR_ONLY</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(4)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te întrebi nu „ce face sistemul?", ci „ce din el depinde numai de mine?". Treci prin inventarul de inputuri din _SISTEM (C17): parametri ținuți în cap, foi personale, decizii nescrise, o ajustare lunară pe care doar tu o faci. Pe fiecare astfel de input pui un flag AUTHOR_ONLY=DA.</p>

  </div>
</div>
<div class="step" data-step="5">
  <div class="step-head" onclick="toggleStep(5)">
    <div class="step-marker">PAS 05</div>
    <h3 class="step-title">Promptul 1: Copilot separă inputurile author-only de cele cu sursă accesibilă unui rol</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(5)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Deschizi Copilot pe foaia _DELEGARE și lipești Promptul 1. AI parcurge inventarul de inputuri și le împarte: care depind de o singură persoană (author-only) și care au o sursă documentată pe care un rol o poate folosi. Nu desemnează nicio persoană și nu scrie reguli de prag. AI propune, omul decide.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 1 · CE TE FACE INDISPENSABIL</div>
      <div class="prompt-text">Am un sistem care rulează singur pe acest workbook. Din inventarul de inputuri, listează-mi care depind de o singură persoană, ținute în cap sau în foi personale (author-only), și care au deja o sursă documentată pe care un rol operațional ar putea-o folosi fără mine. Pentru fiecare input author-only, propune-mi unde ar putea fi mutat ca să devină accesibil rolului. Nu desemna nicio persoană, nu scrie reguli de prag și nu modifica datele; doar separă ce atârnă de mine de ce nu. Eu decid.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 1)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="6">
  <div class="step-head" onclick="toggleStep(6)">
    <div class="step-marker">PAS 06</div>
    <h3 class="step-title">Definești ROLUL care preia (ROL_DELEGAT), cu zonă deținută și backup</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(6)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Pe _DELEGARE definești ROL_DELEGAT ca validare de listă cu ROLURI, nu cu nume de oameni: de exemplu „Operare Raportare Vânzări", cu o zonă deținută și un backup-rol. <span data-locked="1">Proprietatea stă pe rol; persoana se atașează temporar la rol.</span> Pleacă omul, rolul rămâne, sistemul are cine să-l continue.</p>
    <div class="section-sublabel">CE INTRĂ ÎN DEFINIREA ROLULUI</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">rol</div>
      <div class="inv-item-body">
        <div class="inv-item-label">ROL_DELEGAT · listă de roluri</div>
        <div class="inv-item-desc">Rolul operațional care preia, ales dintr-o listă de roluri, nu un nume de persoană.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">zonă</div>
      <div class="inv-item-body">
        <div class="inv-item-label">ZONA DEȚINUTĂ</div>
        <div class="inv-item-desc">Partea de sistem pe care rolul o deține și o operează cap-coadă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">backup</div>
      <div class="inv-item-body">
        <div class="inv-item-label">BACKUP-ROL</div>
        <div class="inv-item-desc">Rolul care preia când rolul principal lipsește. Continuitatea nu atârnă de un om.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu persoană</div>
      <div class="inv-item-body">
        <div class="inv-item-label">ROL, NU NUME</div>
        <div class="inv-item-desc">Dacă scrii un nume de om în loc de rol, nu ai delegat sistemul, ai împrumutat o persoană.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu HR</div>
      <div class="inv-item-body">
        <div class="inv-item-label">NU E FIȘĂ DE POST</div>
        <div class="inv-item-desc">Rolul exista ca să alimenteze testul viu al predării, nu ca organigramă de citit.</div>
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
      <div class="stage-label">ETAPA 3 · Harta de predare ca input al testului</div>
      <h2 class="stage-name">HARTA</h2>
      <div class="stage-tags"><span class="phase-tag">HARTĂ · ACCES</span><span class="type-tag">Input pentru testul viu</span></div>
    </div>
  </header>
  <p class="stage-quote">Acum transformi predarea într-o hartă care alimentează testul: responsabilitate, acces pe zone, limite blocate și o escaladare către un rol. Nu un tabel de citit, ci intrarea verificărilor V1-V4.</p>
  <div class="stage-body">
<div class="step" data-step="7">
  <div class="step-head" onclick="toggleStep(7)">
    <div class="step-marker">PAS 07</div>
    <h3 class="step-title">Responsabilitatea transferată: ce proces preia rolul, ce decizii poate lua</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(7)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Scrii pe _DELEGARE ce responsabilitate trece la rol: ce proces preia din lanțul lunar de raportare, ce decizii poate lua singur, ce livrare asigură. <span data-locked="1">Nu transferi o sarcină, transferi răspunderea pentru o bucată de sistem.</span> Rolul nu execută la comandă, deține rezultatul.</p>

  </div>
</div>
<div class="step" data-step="8">
  <div class="step-head" onclick="toggleStep(8)">
    <div class="step-marker">PAS 08</div>
    <h3 class="step-title">Acces și drepturi: matrice ROL×ZONĂ; limitele marcate PROTECTED=DA</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(8)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Construiești o matrice ROL pe ZONĂ: ce vede, ce modifică, ce e doar de aprobat. <span data-locked="1">Asta alimentează V2 acces validat.</span> Zonele pe care rolul nu trebuie să le atingă le marchezi PROTECTED=DA, ranges chiar blocate, nu o notă pe margine. Asta alimentează V3 zone interzise.</p>

  </div>
</div>
<div class="step" data-step="9">
  <div class="step-head" onclick="toggleStep(9)">
    <div class="step-marker">PAS 09</div>
    <h3 class="step-title">Escaladare: către ce ROL urcă o problemă peste mandat, cu ce declanșator</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(9)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Stabilești escaladarea: când o problemă depășește mandatul rolului, către ce ROL urcă și cu ce declanșator. <span data-locked="1">Escaladarea C20 urcă la un rol care preia proprietatea, nu la un semnal care schimbă starea (acela e C19).</span> ESCALADARE_ROL și DECLANSATOR alimentează V4.</p>
    <div class="section-sublabel">HARTA DE PREDARE, CA INPUT AL TESTULUI</div>
    <ul class="ba-list">
<li class="ba-item">
      <div class="ba-item-indicator">Proprietatea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">informală, la autor, nescrisă</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">pe un ROL, cu zonă și backup</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Accesul</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">neclar, „întreabă-mă pe mine"</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">matrice ROL×ZONĂ, limite blocate</span></div>
      </div>
    </li>
<li class="ba-item">
      <div class="ba-item-indicator">Escaladarea</div>
      <div class="ba-pair">
        <div class="ba-before"><span class="ba-tag">ÎNAINTE</span><span class="ba-val">verbală, „mă suni pe mine"</span></div>
        <div class="ba-arrow">→</div>
        <div class="ba-after"><span class="ba-tag">DUPĂ</span><span class="ba-val">către un ROL, cu declanșator scris</span></div>
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
      <div class="stage-label">ETAPA 4 · Testul de predare: scoți autorul</div>
      <h2 class="stage-name">TESTUL</h2>
      <div class="stage-tags"><span class="phase-tag">TEST VIU</span><span class="type-tag">Anti-RACI</span></div>
    </div>
  </header>
  <p class="stage-quote">Proba care separă predarea de o promisiune: apeși „scoate autorul" și sistemul recalculează singur. V1-V4 și STATUS se reașază pe viu. Nu bifezi tu o predare; o dovedești.</p>
  <div class="stage-body">
<div class="step" data-step="10">
  <div class="step-head" onclick="toggleStep(10)">
    <div class="step-marker">PAS 10</div>
    <h3 class="step-title">Apeși AUTOR_ACTIV=NU: simulezi autorul scos, sistemul recalculează singur</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(10)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Treci comutatorul AUTOR_ACTIV pe NU: simulezi că autorul a dispărut. <span data-locked="1">Celulele marcate AUTHOR_ONLY se golesc, iar formulele care le citeau întorc eroare.</span> V1-V4 și STATUS se reașază pe viu, fără să atingi tu altceva. Comutatorul e semnătura vizuală a _DELEGARE; foaia moștenită de la C19 nu are acest comutator.</p>

  </div>
</div>
<div class="step" data-step="11">
  <div class="step-head" onclick="toggleStep(11)">
    <div class="step-marker">PAS 11</div>
    <h3 class="step-title">Promptul 2: Copilot arată exact ce input critic încă atârnă de zona autorului</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(11)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cu autorul scos, lipești Promptul 2. AI verifică lanțul critic și arată exact care input încă atârnă de zona autorului, aprinzând V1. <span data-locked="1">AI evidențiază, omul mută.</span> Copilot nu preia proprietatea și nu decide business; doar îți arată unde mai ești tu cheia.</p>
    <div class="prompt-box">
      <div class="prompt-label">PROMPT 2 · CINE MAI E CHEIA</div>
      <div class="prompt-text">Cu autorul scos (AUTOR_ACTIV=NU), verifică lanțul de formule critice și arată-mi exact care input critic încă atârnă de o celulă din zona autorului sau de un input marcat author-only, lăsând o formulă goală sau în eroare. Listează fiecare astfel de dependență și unde ar trebui mutat inputul ca să devină accesibil rolului. Nu prelua proprietatea, nu desemna nicio persoană și nu decide nimic de business; doar evidențiază unde mai sunt eu cheia. Eu mut.</div>
      <button class="copy-btn" onclick="copyPrompt(this, 2)">COPIAZĂ PROMPTUL</button>
    </div>
  </div>
</div>
<div class="step" data-step="12">
  <div class="step-head" onclick="toggleStep(12)">
    <div class="step-marker">PAS 12</div>
    <h3 class="step-title">Testul anti-RACI: STATUS e calculat din V1-V4, nu o bifă pe care o pui tu</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(12)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Întrebarea care separă _DELEGARE de un tabel RACI: STATUS e o bifă pe care o pui tu, sau o stare care se calculează? <span data-locked="1">Aici STATUS iese din V1-V4: se mișcă singur când schimbi harta.</span> Dacă ar fi o casetă bifată manual, ar fi documentare pasivă, nu delegare. Predarea trăiește pentru că testul e viu.</p>
    <div class="section-sublabel">TEST VIU, NU TABEL PASIV</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">se reașază</div>
      <div class="inv-item-body">
        <div class="inv-item-label">STATUS CALCULAT DIN V1-V4</div>
        <div class="inv-item-desc">NEPREDAT, PARȚIAL, DELEGAT, AUTONOM. Starea se mută singură când schimbi harta.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">pe viu</div>
      <div class="inv-item-body">
        <div class="inv-item-label">SCOȚI AUTORUL, SE RECALCULEAZĂ</div>
        <div class="inv-item-desc">AUTOR_ACTIV=NU golește celulele author-only; V1 vede pe loc dependența rămasă.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu bifezi</div>
      <div class="inv-item-body">
        <div class="inv-item-label">NU E RACI, NU E SOP</div>
        <div class="inv-item-desc">Dacă STATUS ar fi o bifă pe care o pui tu, e tabel de citit, nu predare dovedită.</div>
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
      <div class="stage-label">ETAPA 5 · Dependența ascunsă, apoi repararea</div>
      <h2 class="stage-name">REPARARE</h2>
      <div class="stage-tags"><span class="phase-tag">DRAMĂ · V1 FAIL</span><span class="type-tag">Mut pe rol</span></div>
    </div>
  </header>
  <p class="stage-quote">Aici se vede adevărul: cu autorul scos, V1 aprinde FAIL. Un parametru pe care doar tu îl știai lasă o formulă critică goală. Credeai că ai delegat. Tu erai cheia. Apoi îl muți pe rol.</p>
  <div class="stage-body">
<div class="step" data-step="13">
  <div class="step-head" onclick="toggleStep(13)">
    <div class="step-marker">PAS 13</div>
    <h3 class="step-title">V1 aprinde FAIL: un parametru știut doar de tine lasă o formulă goală</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(13)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cu AUTOR_ACTIV=NU, o ajustare manuală lunară pe care doar tu o știai se golește și o formulă critică din lanțul de raportare rămâne goală. <span data-locked="1">V1 trece în FAIL, STATUS cade la PARȚIAL.</span> Credeai că ai delegat. De fapt tu erai cheia: harta arăta complet, dar un input critic atârna tot de tine.</p>

  </div>
</div>
<div class="step" data-step="14">
  <div class="step-head" onclick="toggleStep(14)">
    <div class="step-marker">PAS 14</div>
    <h3 class="step-title">Repari: muți parametrul în blocul documentat PARAM_, accesibil rolului</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(14)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Nu rescrii logica. <span data-locked="1">Muți parametrul din zona ta personală în blocul documentat PARAM_ din _SISTEM, accesibil rolului.</span> Formula citește acum o sursă pe care rolul o poate folosi fără tine. V1 trece din FAIL în OK, fără să fi schimbat ce calculează sistemul, doar de unde citește.</p>

  </div>
</div>
<div class="step" data-step="15">
  <div class="step-head" onclick="toggleStep(15)">
    <div class="step-marker">PAS 15</div>
    <h3 class="step-title">Re-rulezi cu autorul tot scos: nimic nu se mai rupe (granița față de C19)</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(15)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cu AUTOR_ACTIV tot pe NU, nimic nu se mai rupe: lanțul critic e întreg din surse accesibile rolului. <span data-locked="1">Aici e linia față de C19: C19 prinde un INPUT greșit în date; C20 prinde DEPENDENȚA de autor.</span> Alt subiect, altă foaie. C19 te apăra de date proaste; C20 te scoate pe tine din ecuație.</p>
    <div class="section-sublabel">GRANIȚA FAȚĂ DE C19: DATE GREȘITE VS DEPENDENȚĂ DE AUTOR</div>
    <ul class="inv-list">
<li class="inv-item">
      <div class="inv-item-status status-good">prinde</div>
      <div class="inv-item-body">
        <div class="inv-item-label">DEPENDENȚA ASCUNSĂ · SCOASĂ LA LUMINĂ</div>
        <div class="inv-item-desc">Un input pe care doar tu îl știai golește o formulă critică. V1 îl vede pe loc.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-good">repară</div>
      <div class="inv-item-body">
        <div class="inv-item-label">MUTAT PE ROL, NU REScris</div>
        <div class="inv-item-desc">Inputul critic trece în PARAM_ accesibil rolului. Logica rămâne, sursa se mută.</div>
      </div>
    </li>
<li class="inv-item">
      <div class="inv-item-status status-bad">nu C19</div>
      <div class="inv-item-body">
        <div class="inv-item-label">NU E O REGULĂ PE DATE</div>
        <div class="inv-item-desc">Spre deosebire de C19, care prinde un input greșit, C20 prinde că sistemul mai depinde de o persoană.</div>
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
      <div class="stage-label">ETAPA 6 · STATUS AUTONOM și predarea reală</div>
      <h2 class="stage-name">AUTONOM</h2>
      <div class="stage-tags"><span class="phase-tag">PAYOFF</span><span class="type-tag">Pack complet</span></div>
    </div>
  </header>
  <p class="stage-quote">Proba finală: autorul scos, acces validat, zone blocate, escaladare către rol și zero dependență author-only. STATUS devine AUTONOM singur. Predai proprietatea, nu o explici. Pachetul se închide.</p>
  <div class="stage-body">
<div class="step" data-step="16">
  <div class="step-head" onclick="toggleStep(16)">
    <div class="step-marker">PAS 16</div>
    <h3 class="step-title">STATUS devine AUTONOM singur: workbook-ul confirmă că alt rol îl poate continua</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(16)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Cu autorul scos și V1-V4 toate OK, STATUS trece în AUTONOM de la sine. <span data-locked="1">Apeși „scoate autorul" și sistemul nu se rupe: workbook-ul confirmă singur că alt rol îl poate continua.</span> Nu o promisiune, o dovadă vie pe ecran. Asta e WOW-ul predării: STATUS=AUTONOM fără tine în ecuație.</p>

  </div>
</div>
<div class="step" data-step="17">
  <div class="step-head" onclick="toggleStep(17)">
    <div class="step-marker">PAS 17</div>
    <h3 class="step-title">Devii cel care predă proprietatea, nu cel care explică</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(17)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action">Te uiți la ce ai construit: nu un discurs de predare, ci o dovadă în fișier. <span data-locked="1">Dovada că rolul poate continua e în workbook, în testul viu, nu în vorbele tale.</span> Nu mai ești cel care explică „uite cum merge"; ești cel care predă proprietatea și o arată dovedită. Explicația nu mută proprietatea; testul viu o mută.</p>

  </div>
</div>
<div class="step" data-step="18">
  <div class="step-head" onclick="toggleStep(18)">
    <div class="step-marker">PAS 18</div>
    <h3 class="step-title">Poți lipsi o lună: rolul operează, escaladează, continuă; pachetul e închis</h3>
    <div class="step-check" onclick="event.stopPropagation();checkStep(18)" title="Marchează pasul ca verificat"></div>
  </div>
  <div class="step-body">
    <p class="step-action"><span data-locked="1">Acum poți lipsi o lună: rolul operează, escaladează la nevoie, continuă fără tine.</span> Sistemul nu mai e al tău, e al rolului care îl deține. C20 nu mai are treaptă următoare: e construcția-semnătură care închide PACK-ul C01-C20. De la structurarea unui tabel până la predarea unui sistem întreg, arcul e complet.</p>

  </div>
</div>
  </div>
</section>

      <section class="final-section" id="final-section">
        <div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>
        <h2 class="final-title">8 verificări finale canonice</h2>
        <p class="final-intro">Înainte de a preda sistemul ca proprietate a unui rol, confirmi fiecare invariant al delegării. Aceleași verificări, aceeași zonă, la fiecare construcție.</p>
        <div class="final-grid"><div class="final-card" data-final="1"><div class="final-num">1</div><div class="final-body"><div class="final-label">_DELEGARE EXISTĂ</div><div class="final-text">Date_MASTER-C20-Delegare.xlsx are foaia _DELEGARE, ca foaia predării proprietății, distinctă de _GUVERNARE.</div><button class="final-check-btn" onclick="confirmFinal(1)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="2"><div class="final-num">2</div><div class="final-body"><div class="final-label">ROL, NU PERSOANĂ</div><div class="final-text">ROL_DELEGAT e ales dintr-o listă de roluri, cu zonă deținută și backup. Niciun nume de om.</div><button class="final-check-btn" onclick="confirmFinal(2)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="3"><div class="final-num">3</div><div class="final-body"><div class="final-label">AUTOR_ACTIV = COMUTATORUL</div><div class="final-text">Semnătura vizuală a _DELEGARE: apeși „scoate autorul" și sistemul recalculează singur. C19 nu îl are.</div><button class="final-check-btn" onclick="confirmFinal(3)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="4"><div class="final-num">4</div><div class="final-body"><div class="final-label">V1 ZERO DEPENDENȚĂ AUTHOR-ONLY</div><div class="final-text">Cu autorul scos, niciun input critic nu atârnă de zona autorului. Lanțul critic e întreg.</div><button class="final-check-btn" onclick="confirmFinal(4)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="5"><div class="final-num">5</div><div class="final-body"><div class="final-label">V2 ACCES VALIDAT</div><div class="final-text">Rolul vede și modifică zona de operare și are zero acces în zonele protejate.</div><button class="final-check-btn" onclick="confirmFinal(5)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="6"><div class="final-num">6</div><div class="final-body"><div class="final-label">V3 ZONE BLOCATE</div><div class="final-text">Fiecare limită declarată e un range cu PROTECTED=DA, chiar blocat, nu o notă pe margine.</div><button class="final-check-btn" onclick="confirmFinal(6)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="7"><div class="final-num">7</div><div class="final-body"><div class="final-label">V4 ESCALADARE FUNCȚIONALĂ</div><div class="final-text">Escaladarea urcă la un ROL (nu o persoană, nu gol), cu un declanșator scris.</div><button class="final-check-btn" onclick="confirmFinal(7)">VERIFICĂ</button></div></div>
<div class="final-card" data-final="8"><div class="final-num">8</div><div class="final-body"><div class="final-label">STATUS CALCULAT, NU BIFAT</div><div class="final-text">NEPREDAT / PARȚIAL / DELEGAT / AUTONOM, calculat din V1-V4. Se mișcă singur, nu îl bifezi tu.</div><button class="final-check-btn" onclick="confirmFinal(8)">VERIFICĂ</button></div></div></div>
        <div class="completion-badge" id="completion">
          <div class="completion-title">Sistemul nu mai e al tău.</div>
          <div class="completion-subtitle">Predat ca proprietate a unui rol, dovedit în testul viu. Poți lipsi o lună. Pachetul C01-C20 e închis.</div>
        </div>
      </section>

      <section class="next-section">
        <div class="next-label">PACK 02 EXCEL · ULTIMA CONSTRUCȚIE</div>
        <h3 class="next-title">Arcul C01-C20 e complet</h3>
        <p class="next-desc">C20 nu mai are treaptă următoare: e construcția-semnătură care închide pachetul. De la structurarea unui tabel (C01) până la predarea proprietății unui sistem întreg (C20), ai parcurs scanarea, cunoașterea, analiza, raportarea și autonomia. Sistemul nu doar merge fără tine; nu mai e al tău.</p>
      </section>

      <section class="payoff-section">
        <div class="payoff-line dim">Sistemul rula singur și se păzea singur, dar la orice problemă tot pe tine te suna.</div>
        <div class="payoff-line accent">Era încă al tău, și numai al tău: autonomia era falsă cât timp depindea de tine.</div>
        <div class="payoff-line regular">Acum proprietatea a trecut de la o persoană la un rol, dovedit în _DELEGARE: scoți autorul, dependența ascunsă se aprinde, o muți pe rol, și STATUS devine AUTONOM singur.</div>
        <div class="payoff-line payoff-wow" data-locked="1"><span class="wow-tag">WOW:</span><span data-wow="1">Apeși «scoate autorul», și sistemul nu se rupe: workbook-ul confirmă singur că alt rol îl poate continua.</span></div>
        <div class="payoff-motto" data-locked="1">Pleci, și munca nu mai e a ta.</div>
      </section>

      <section class="transformare-section">
        <div class="tu-cert">
          <div class="tu-kicker">✓ DUPĂ C20 POȚI</div>
          <p class="tu-statement-sm">Predai proprietatea unui sistem unui rol și o dovedești în workbook: scoți autorul, dependențele ascunse ies la lumină, le muți pe rol, iar STATUS devine AUTONOM singur.</p>
        </div>
        <div class="ts-block ts-identity"><div class="ts-label">DE ACUM ÎNAINTE</div>
          <div class="ts-pair"><span class="ts-no">Nu mai împarți sarcini.</span><span class="ts-yes">Delegi sistemul.</span></div>
          <div class="ts-pair"><span class="ts-no">Nu mai explici „uite cum merge".</span><span class="ts-yes">Dovedești că rolul îl poate continua.</span></div>
          <div class="ts-pair"><span class="ts-no">Nu mai întrebi „merge fără mine?".</span><span class="ts-yes">Întrebi „e al altcuiva acum?".</span></div>
        </div>
      </section>

      <footer class="footer">
        TRAINITY · C20 DELEGARE · sistemul nu mai e al tău, e al rolului care îl deține
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
<a class="nav-item" data-nav-stage="2" href="#stage-2" onclick="navigateStage(2,event)"><span class="nav-item-num">2</span><span class="nav-item-text"><span class="nav-item-name">DEPENDENȚĂ</span><span class="nav-item-meta">3 pași · Copilot</span></span></a>
<a class="nav-item" data-nav-stage="3" href="#stage-3" onclick="navigateStage(3,event)"><span class="nav-item-num">3</span><span class="nav-item-text"><span class="nav-item-name">HARTA</span><span class="nav-item-meta">3 pași · Hartă</span></span></a>
<a class="nav-item" data-nav-stage="4" href="#stage-4" onclick="navigateStage(4,event)"><span class="nav-item-num">4</span><span class="nav-item-text"><span class="nav-item-name">TESTUL</span><span class="nav-item-meta">3 pași · Test viu</span></span></a>
<a class="nav-item" data-nav-stage="5" href="#stage-5" onclick="navigateStage(5,event)"><span class="nav-item-num">5</span><span class="nav-item-text"><span class="nav-item-name">REPARARE</span><span class="nav-item-meta">3 pași · Dramă</span></span></a>
<a class="nav-item" data-nav-stage="6" href="#stage-6" onclick="navigateStage(6,event)"><span class="nav-item-num">6</span><span class="nav-item-text"><span class="nav-item-name">AUTONOM</span><span class="nav-item-meta">3 pași · Payoff</span></span></a></div>

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

    # patch head: title + NEXT marker (C20 inchide pack-ul -> FINAL)
    head = re.sub(r'<title>.*?</title>', '<title>C20 · Delegare · Trainity</title>', head, count=1)
    head = re.sub(r'NEXT \(C\d+\)', 'NEXT (FINAL)', head)
    # patch script tail: STORAGE_KEY c19 -> c20
    tail = re.sub(r'trainity_c\d+_study_v1', 'trainity_c20_study_v1', tail)

    body = BODY.replace('__HERO__', HERO_PLACEHOLDER)

    out = head + body + tail
    os.makedirs('c20', exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out), 'bytes')

    # ---- self-checks ----
    # garda: tokeni sursa c19 reziduali in CONTINUT (body)
    leftover = re.findall(r'trainity_c19|trainity_c18|Date_MASTER-C19|Date_MASTER-C18|19-Guvernare|18-Automatizare', body)
    print('  leftover c19/c18 storage/file tokens in BODY (trebuie 0):', len(leftover), leftover[:8])
    # garda contaminare C19 ca IDENTITATE: "guvern" doar in granita/callback, nu ca identitate
    guv = re.findall(r'guvern', body, re.IGNORECASE)
    print('  "guvern" in BODY (doar granita C19/callback, verifica context):', len(guv))
    # garda contaminare C18 ca identitate
    autom = re.findall(r'automatiz', body, re.IGNORECASE)
    print('  "automatiz" in BODY (doar callback C18, verifica context):', len(autom))
    # artefact corect
    print('  "_DELEGARE" in BODY:', body.count('_DELEGARE'))
    print('  "_GUVERNARE" in BODY (callback C19, nu identitate):', body.count('_GUVERNARE'))
    print('  "_AUTOMATIZARE" in BODY (trebuie 0):', body.count('_AUTOMATIZARE'))
    # garda RO-EN: "ownership" interzis (R-V03 M2)
    print('  "ownership" in OUT (trebuie 0):', out.lower().count('ownership'))
    # garda anti-em-dash pe TOT out
    for ch, nm in [('—', 'em-dash'), ('–', 'en-dash')]:
        n = out.count(ch)
        print('  ', nm, 'in OUT (trebuie 0):', n)
    # slots locked verbatim
    locked = {
        'HERO': 'Cum deleg sistemul, ca să meargă fără mine?',
        'BOMBA': 'Sistemul tău merge fără tine. Dar la orice problemă, tot pe tine te sună.',
        'MANTRA': 'Nu împart sarcini. Deleg sistemul.',
        'WOW': 'Apeși «scoate autorul», și sistemul nu se rupe: workbook-ul confirmă singur că alt rol îl poate continua.',
        'MOTTO': 'Pleci, și munca nu mai e a ta.',
        'GRESEALA': 'Crezi că ai delegat când ai explicat.',
        'AHA': 'Un sistem nu e autonom pentru că merge singur. E autonom când îl poate deține altcineva.',
        'HOV-OBJECT': 'DELEGAREA SISTEMULUI DE LUCRU',
    }
    for k, v in locked.items():
        print('  LOCK', k, ':', out.count(v))
    # 6 titluri de etapa
    etape = [
        'Sistemul merge, dar e încă al tău',
        'Ce te face indispensabil',
        'Harta de predare ca input al testului',
        'Testul de predare: scoți autorul',
        'Dependența ascunsă, apoi repararea',
        'STATUS AUTONOM și predarea reală',
    ]
    for t in etape:
        print('  ETAPA:', out.count(t), '|', t)
    # arc obligatoriu
    arc = ['AUTOR_ACTIV', 'AUTHOR_ONLY', 'ROL_DELEGAT', 'PARAM_', 'NEPREDAT', 'AUTONOM', 'V1']
    print('  arc prezent:', all(a in out for a in arc))
    print('  steps:', body.count('data-step="'), '| stages:', body.count('id="stage-'),
          '| anomaly:', body.count('anomaly-card'), '| final-card:', body.count('final-card'),
          '| prompturi:', body.count('prompt-box'))
    print('  localStorage in tail:', 'trainity_c20_study_v1' in tail)


if __name__ == '__main__':
    main()
