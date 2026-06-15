#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c20.py - HTML-Video-Excel-20-Delegare.html (broadcast, JS-driven).

Mostenesc head+CSS si JS generic din c19 Video (sibling T5, acelasi tier).
Inlocuiesc:
  - BODY scaffolding (hero, exec slides, topbar, panel, toast, modal) -> C20 DELEGARE
  - const STAGES [...] + const PROMPTS {...} -> C20 (6 etape / 18 pasi)
  - STORAGE_KEY, <title>, exec placeholders -> C20
exec-stage + hero = SVG placeholder DRAFT (asset real ARHITECT ulterior).

Garda C20 (verb DELEG, artefact _DELEGARE):
  C18 ruleaza (motorul) · C19 se tine corect prin reguli · C20 PREDA proprietatea.
  Etapa 4 = testul VIU (scoti autorul). Etapa 5 = drama V1 FAIL -> reparare.
  Granita vs C19: C19 prinde un INPUT gresit (date); C20 prinde DEPENDENTA de autor.
  ZERO identitate: management, HR, fisa de post, RACI, SOP, documentare verbala,
  ownership ca termen, GUVERNARE/CONTROL ca identitate C20.
  ("_GUVERNARE"/"reguli" doar callback la C19.) Cifrele in Excel (R-V02.15).
"""
import re

SRC = 'c19/HTML-Video-Excel-19-Guvernare.html'
OUT = 'c20/HTML-Video-Excel-20-Delegare.html'

TITLE = 'C20 · DELEGARE · BROADCAST'
STORAGE = 'trainity_c20_video_v1'

# Axa DELEGARE: eticheta scurta pe placeholderul exec-stage (DRAFT)
EXEC_TITLES = {1: 'REALITATE', 2: 'DEPENDENȚĂ', 3: 'HARTA',
               4: 'TESTUL', 5: 'REPARARE', 6: 'AUTONOM'}


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
        "opacity='0.6'>C20 · exec-stage-" + str(n) + " · placeholder DRAFT</text></svg>"
    )


def hero_placeholder():
    """Hero broadcast = SVG placeholder DRAFT, text AUTONOMIE (NU poza clonata)."""
    return (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
        "<defs><linearGradient id='hg' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
        "</linearGradient></defs><rect width='1600' height='900' fill='url(%23hg)'/>"
        "<text x='80' y='470' fill='%23FFD400' font-family='Georgia' font-size='96' "
        "font-weight='bold'>AUTONOMIE</text>"
        "<text x='84' y='534' fill='%23ffffff' font-family='Arial' font-size='30' "
        "opacity='0.6'>C20 · hero · placeholder DRAFT</text></svg>"
    )


# ============ BODY C20 (curat, fara contaminare clona c01/c19) ============
BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C20 · Delegare</div>
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
    <div class="hero-prelabel">Construcția 20 Excel</div>
    <h1 class="hero-title" data-locked="1">DELEGAREA SISTEMULUI DE LUCRU</h1>
    <p class="hero-hook frag" data-frag="1"><span data-locked="1">Cum deleg sistemul, ca să meargă fără mine?</span></p>
    <p class="hero-sub frag" data-frag="2"><span data-locked="1">Sistemul tău merge fără tine. Dar la orice problemă, tot pe tine te sună.</span></p>
    <p class="hero-sub frag" data-frag="3">Înainte să spunem că e autonom, îi predăm proprietatea unui rol, dovedit în workbook.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="11">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am pornit sistemul, rula deja.</p>
      <p class="dim frag" data-frag="2">Nu am stat să-l păzesc, se păzea singur.</p>
      <p class="dim frag" data-frag="3">Nu am explicat cum merge: explicația nu mută proprietatea.</p>
      <p class="dim frag" data-frag="4">Greșeala clasică: <span data-locked="1">Crezi că ai delegat când ai explicat.</span></p>
      <p class="accent frag" data-frag="5">Am mutat proprietatea de la o persoană la un rol.</p>
      <p class="frag" data-frag="6">Am scos autorul pe viu, dependența ascunsă s-a aprins, am mutat-o pe rol.</p>
      <p class="frag" data-frag="7"><span data-locked="1">Un sistem nu e autonom pentru că merge singur. E autonom când îl poate deține altcineva.</span></p>
      <p class="frag" data-frag="8">C20 închide pachetul Excel. Nu mai e treaptă următoare.</p>
      <p class="payoff-wow frag" data-frag="9"><span class="wow-tag">WOW:</span><span data-wow="1">Apeși «scoate autorul», și sistemul nu se rupe: workbook-ul confirmă singur că alt rol îl poate continua.</span></p>
      <p class="accent frag" data-frag="10"><span data-locked="1">Nu împart sarcini. Deleg sistemul.</span></p>
      <div class="final-motto frag" data-frag="11">Pleci, și munca nu mai e a ta.</div>
    </div>
  </section>

  <!-- ============================================================ -->
  <!-- CONCLUZII - slide tranzitie intre final si executive          -->
  <!-- ============================================================ -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 20</span>
      </h1>
      <div class="conclusion-divider frag" data-frag="2"></div>
    </div>
  </section>

  <!-- ============================================================ -->
  <!-- EXECUTIVE SHOW - 7 screens (6 etape + 1 closing)              -->
  <!-- exec-stage = SVG placeholder DRAFT (axa DELEGARE)             -->
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
      <div class="exec-emotion frag" data-frag="2">Sistemul merge, dar e încă al tău</div>
      <h2 class="exec-title frag" data-frag="3">REALITATE</h2>
      <p class="exec-phrase frag" data-frag="4">Sistemul rulează și se păzește singur. Și totuși, la orice problemă, tot pe mine mă sună. Sunt proprietarul informal.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 2: DEPENDENȚĂ -->
  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-2"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">02</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 02</div>
      <div class="exec-emotion frag" data-frag="2">Ce mă face indispensabil</div>
      <h2 class="exec-title frag" data-frag="3">DEPENDENȚĂ</h2>
      <p class="exec-phrase frag" data-frag="4">Inventariez ce inputuri atârnă numai de mine, ținute în cap sau în foi personale. Le marchez author-only.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 3: HARTA -->
  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-3"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">03</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 03</div>
      <div class="exec-emotion frag" data-frag="2">Harta de predare ca input al testului</div>
      <h2 class="exec-title frag" data-frag="3">HARTA</h2>
      <p class="exec-phrase frag" data-frag="4">Rol, responsabilitate, acces pe zone, limite blocate, escaladare către un rol. Nu un tabel de citit, ci intrarea testului.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 4: TESTUL -->
  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-4"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">04</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 04</div>
      <div class="exec-emotion frag" data-frag="2">Scoți autorul</div>
      <h2 class="exec-title frag" data-frag="3">TESTUL</h2>
      <p class="exec-phrase frag" data-frag="4">Apăs «scoate autorul». V1-V4 și STATUS se reașază singure. Nu bifez o predare, o dovedesc pe viu.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 5: REPARARE -->
  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-5"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">05</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 05</div>
      <div class="exec-emotion frag" data-frag="2">Dependența ascunsă, apoi repararea</div>
      <h2 class="exec-title frag" data-frag="3">REPARARE</h2>
      <p class="exec-phrase frag" data-frag="4">V1 aprinde FAIL: tu erai cheia. Mut parametrul pe rol, V1 trece OK, fără să rescriu logica.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 6: AUTONOM -->
  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap">
      <div class="exec-image" data-exec-img="exec-stage-6"></div>
    </div>
    <div class="exec-overlay"></div>
    <div class="exec-accent-bar"></div>
    <div class="exec-ghost-num">06</div>
    <div class="exec-content">
      <div class="exec-label frag" data-frag="1">Etapa 06</div>
      <div class="exec-emotion frag" data-frag="2">STATUS autonom și predarea reală</div>
      <h2 class="exec-title frag" data-frag="3">AUTONOM</h2>
      <p class="exec-phrase frag" data-frag="4">Autorul scos, zero dependență author-only: STATUS devine AUTONOM singur. Pot lipsi o lună. Pachetul se închide.</p>
    </div>
  </section>

  <!-- EXEC SLIDE 7: CLOSING APOTEOTIC -->
  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">Pleci, și munca <span class="exec-closing-motto-yellow">nu mai e a ta.</span></h1>
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


# ============ STAGES C20 (6 etape x 3 pasi = 18, din BLUEPRINT C20) ============
STAGES = r'''const STAGES = [
  {
    id: 1, name: "REALITATE", emotion: "Sistemul merge, dar e încă al tău",
    hook: "Sistemul rulează și se păzește singur.",
    next: "Și totuși, la orice problemă, tot pe tine te sună.",
    steps: [
      { num: "01", title: "Sistemul rulează și se păzește singur, dar tot pe tine te sună.",
        instr: "Deschizi sistemul moștenit: motorul rulează (C18), regulile îl țin corect (C19). <strong>Și totuși, la orice problemă, telefonul sună la tine. Ești proprietarul informal: sistemul merge, dar nu are alt deținător.</strong>",
        excel: true },
      { num: "02", title: "„Merge fără efort\" nu înseamnă „are alt proprietar\".",
        instr: "În sistemul moștenit, C18 a scos efortul și C19 a scos supravegherea. <strong>Dar autonomia e încă falsă: sistemul depinde de disponibilitatea ta. Un sistem deținut de o singură persoană nu e autonom, e doar bine întreținut de ea.</strong>",
        excel: true },
      { num: "03", title: "Deschizi _DELEGARE cu AUTOR_ACTIV=DA: STATUS=NEPREDAT.",
        instr: "Adaugi foaia _DELEGARE și o fixezi ca foaia predării. <strong>Comutatorul AUTOR_ACTIV e pe DA, harta e goală: STATUS arată NEPREDAT. Testul concediului: dacă pleci o lună, sistemul rămâne orfan?</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "DEPENDENȚĂ", emotion: "Ce te face indispensabil",
    hook: "Înainte să predai, vezi ce te face indispensabil.",
    next: "Inputurile care atârnă numai de tine, marcate author-only.",
    steps: [
      { num: "04", title: "Inventariezi din _SISTEM ce inputuri atârnă de tine, le marchezi AUTHOR_ONLY.",
        instr: "Te întrebi nu „ce face sistemul?\", ci „ce din el depinde numai de mine?\". <strong>Parametri ținuți în cap, foi personale, o ajustare lunară pe care doar tu o faci. Pe fiecare pui un flag AUTHOR_ONLY=DA.</strong>",
        excel: true },
      { num: "05", title: "Promptul 1: Copilot separă inputurile author-only de cele cu sursă accesibilă unui rol.", instr: "", prompt: 1 },
      { num: "06", title: "Definești ROLUL care preia (ROL_DELEGAT), cu zonă deținută și backup.",
        instr: "Definești ROL_DELEGAT ca listă de roluri, nu de oameni: de exemplu „Operare Raportare Vânzări\", cu zonă deținută și backup-rol. <strong>Proprietatea stă pe rol; persoana se atașează temporar. Pleacă omul, rolul rămâne.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "HARTA", emotion: "Harta de predare ca input al testului",
    hook: "Harta nu e un tabel de citit.",
    next: "E intrarea verificărilor V1-V4.",
    steps: [
      { num: "07", title: "Responsabilitatea transferată: ce proces preia rolul, ce decizii poate lua.",
        instr: "Scrii ce responsabilitate trece la rol: ce proces preia din lanțul lunar de raportare, ce decizii ia singur, ce livrare asigură. <strong>Nu transferi o sarcină, transferi răspunderea pentru o bucată de sistem.</strong>",
        excel: true },
      { num: "08", title: "Acces și drepturi: matrice ROL×ZONĂ; limitele marcate PROTECTED=DA.",
        instr: "Construiești o matrice ROL pe ZONĂ: ce vede, ce modifică, ce e doar de aprobat (alimentează V2). <strong>Zonele pe care rolul nu trebuie să le atingă le marchezi PROTECTED=DA, ranges chiar blocate (alimentează V3).</strong>",
        excel: true },
      { num: "09", title: "Escaladare: către ce ROL urcă o problemă peste mandat, cu ce declanșator.",
        instr: "Stabilești escaladarea: când o problemă depășește mandatul, către ce ROL urcă și cu ce declanșator (alimentează V4). <strong>Escaladarea C20 urcă la un rol care preia proprietatea, nu la un semnal care schimbă starea, acela e C19.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "TESTUL", emotion: "Testul de predare: scoți autorul",
    hook: "Apeși „scoate autorul\" și sistemul recalculează singur.",
    next: "Nu bifezi o predare, o dovedești.",
    steps: [
      { num: "10", title: "Apeși AUTOR_ACTIV=NU: simulezi autorul scos, sistemul recalculează singur.",
        instr: "Treci comutatorul AUTOR_ACTIV pe NU: simulezi că autorul a dispărut. <strong>Celulele author-only se golesc, formulele care le citeau întorc eroare. V1-V4 și STATUS se reașază pe viu. Comutatorul e semnătura _DELEGARE; C19 nu îl are.</strong>",
        excel: true },
      { num: "11", title: "Promptul 2: Copilot arată exact ce input critic încă atârnă de zona autorului.", instr: "", prompt: 2 },
      { num: "12", title: "Testul anti-RACI: STATUS e calculat din V1-V4, nu o bifă pe care o pui tu.",
        instr: "Întrebarea care separă _DELEGARE de un tabel RACI: STATUS e o bifă sau o stare calculată? <strong>Aici STATUS iese din V1-V4, se mișcă singur când schimbi harta. O casetă bifată manual ar fi documentare pasivă, nu delegare.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "REPARARE", emotion: "Dependența ascunsă, apoi repararea",
    hook: "Cu autorul scos, V1 aprinde FAIL.",
    next: "Credeai că ai delegat. Tu erai cheia.",
    steps: [
      { num: "13", title: "V1 aprinde FAIL: un parametru știut doar de tine lasă o formulă goală.",
        instr: "Cu AUTOR_ACTIV=NU, o ajustare manuală lunară pe care doar tu o știai se golește, o formulă critică rămâne goală. <strong>V1 trece în FAIL, STATUS cade la PARȚIAL. Credeai că ai delegat. De fapt tu erai cheia.</strong>",
        excel: true },
      { num: "14", title: "Repari: muți parametrul în blocul documentat PARAM_, accesibil rolului.",
        instr: "Nu rescrii logica. <strong>Muți parametrul din zona ta personală în blocul documentat PARAM_, accesibil rolului. Formula citește acum o sursă pe care rolul o poate folosi. V1 trece din FAIL în OK.</strong>",
        excel: true },
      { num: "15", title: "Re-rulezi cu autorul tot scos: nimic nu se mai rupe (granița vs C19).",
        instr: "Cu AUTOR_ACTIV tot pe NU, nimic nu se mai rupe. <strong>Aici e linia față de C19: C19 prinde un INPUT greșit în date; C20 prinde DEPENDENȚA de autor. Alt subiect, altă foaie.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "AUTONOM", emotion: "STATUS autonom și predarea reală",
    hook: "Proba finală: autorul scos, zero dependență.",
    next: "Pachetul se închide.",
    steps: [
      { num: "16", title: "STATUS devine AUTONOM singur: workbook-ul confirmă că alt rol îl poate continua.",
        instr: "Cu autorul scos și V1-V4 toate OK, STATUS trece în AUTONOM de la sine. <strong>Apeși «scoate autorul» și sistemul nu se rupe: workbook-ul confirmă singur că alt rol îl poate continua. O dovadă vie, nu o promisiune.</strong>",
        excel: true },
      { num: "17", title: "Devii cel care predă proprietatea, nu cel care explică.",
        instr: "Nu un discurs de predare, ci o dovadă în fișier. <strong>Dovada că rolul poate continua e în testul viu, nu în vorbele tale. Explicația nu mută proprietatea; testul viu o mută.</strong>",
        excel: true },
      { num: "18", title: "Poți lipsi o lună: rolul operează, escaladează, continuă; pachetul e închis.",
        instr: "Marchezi construcția finalizată. <strong>Acum poți lipsi o lună: rolul operează, escaladează, continuă fără tine. Sistemul nu mai e al tău, e al rolului. C20 închide întregul PACK Excel.</strong>",
        excel: false }
    ]
  }
];

'''


# ============ PROMPTS C20 (2 Copilot, texte din BLUEPRINT / consistente cu Studiu) ============
PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Ce te face indispensabil",
    text: "Am un sistem care rulează singur pe acest workbook. Din inventarul de inputuri, listează-mi care depind de o singură persoană, ținute în cap sau în foi personale (author-only), și care au deja o sursă documentată pe care un rol operațional ar putea-o folosi fără mine. Pentru fiecare input author-only, propune-mi unde ar putea fi mutat ca să devină accesibil rolului. Nu desemna nicio persoană, nu scrie reguli de prag și nu modifica datele; doar separă ce atârnă de mine de ce nu. Eu decid.",
    meta: "AI separă author-only de accesibil rolului. Omul decide."
  },
  2: {
    label: "Prompt 02 · Cine mai e cheia",
    text: "Cu autorul scos (AUTOR_ACTIV=NU), verifică lanțul de formule critice și arată-mi exact care input critic încă atârnă de o celulă din zona autorului sau de un input marcat author-only, lăsând o formulă goală sau în eroare. Listează fiecare astfel de dependență și unde ar trebui mutat inputul ca să devină accesibil rolului. Nu prelua proprietatea, nu desemna nicio persoană și nu decide nimic de business; doar evidențiază unde mai sunt eu cheia. Eu mut.",
    meta: "AI evidențiază dependența rămasă. Omul mută."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    # --- HEAD: title + exec-stage placeholders DRAFT ---
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
    contam = re.findall(r'_GUVERNARE|GUVERNEZ|GUVERNAREA SISTEMULUI|_AUTOMATIZARE|AUTOMATIZEZ|trainity_c19|trainity_c18|19-Guvernare|18-Automatizare', out)
    dashes = [c for c in ('—', '–') if c in out]
    own = out.lower().count('ownership')
    locked = {
        'HERO': 'Cum deleg sistemul, ca să meargă fără mine?',
        'BOMBA': 'Sistemul tău merge fără tine. Dar la orice problemă, tot pe tine te sună.',
        'MANTRA': 'Nu împart sarcini. Deleg sistemul.',
        'WOW': 'Apeși «scoate autorul», și sistemul nu se rupe',
        'MOTTO': 'Pleci, și munca nu mai e a ta.',
        'GRESEALA': 'Crezi că ai delegat când ai explicat.',
        'AHA': 'Un sistem nu e autonom pentru că merge singur. E autonom când îl poate deține altcineva.',
        'hov-object': 'DELEGAREA SISTEMULUI DE LUCRU',
    }
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii,', len(out.encode('utf-8')), 'bytes')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  STORAGE_KEY:', re.search(r'const STORAGE_KEY = "[^"]*"', out).group(0))
    print('  exec base64 jpeg ramase (trebuie 0):', jpeg)
    print('  exec-stage SVG placeholder DRAFT (trebuie 6):', out.count('placeholder DRAFT') - 1)
    print('  STAGES steps (num:):', out.count('num: "'), '| prompturi:', out.count('label: "Prompt'))
    print('  contaminare C19/C18 ca identitate (trebuie 0):', len(contam), contam[:6])
    print('  "ownership" (trebuie 0):', own)
    print('  em/en-dash (trebuie []):', dashes)
    miss = [k for k, v in locked.items() if not has(v)]
    print('  LOCKED 8 sloturi:', 'TOATE OK' if not miss else ('LIPSA -> ' + ', '.join(miss)))
    print('  6 etape verbatim:', sum(has(e) for e in [
        'Sistemul merge, dar e încă al tău', 'Ce te face indispensabil',
        'Harta de predare ca input al testului', 'Scoți autorul',
        'Dependența ascunsă, apoi repararea', 'STATUS autonom și predarea reală']), '/6')
    print('  pack inchis (C01-C20):', 'OK' if 'C01-C20' in out else 'LIPSA')
    print('  closing </html>:', 'OK' if out.rstrip().endswith('</html>') else 'LIPSA')


if __name__ == '__main__':
    main()
