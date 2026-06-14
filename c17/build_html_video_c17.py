#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html_video_c17.py - HTML-Video-Excel-17-Sistematizare.html (broadcast, JS-driven).

Pastrez head+CSS si JS generic din c16 Video. Inlocuiesc:
  - BODY scaffolding (hero, final, conclusion, exec-closing, topbar) -> C17 SISTEMATIZARE
  - const STAGES [...] + const PROMPTS {...} -> C17 (6 etape / 18 pasi)
  - STORAGE_KEY, <title>, exec placeholders -> C17
Garda C17: a face munca reluabila. ZERO automatizare ca identitate (=C18),
ZERO reguli/praguri (=C19), ZERO ownership (=C20). Garda OGLINDA. Anti-SOP.
Cifrele in Excel (R-V02.15). exec-stage = placeholdere SVG (asset real ulterior).
"""
import re

SRC = 'c16/HTML-Video-Excel-16-Livrare.html'
OUT = 'c17/HTML-Video-Excel-17-Sistematizare.html'

EXEC_TITLES = {1: 'REALITATE', 2: 'INVENTAR', 3: 'SURSA',
               4: 'RELUARE', 5: 'EXTERNALIZARE', 6: 'SUBSTITUT'}


def exec_placeholder(n, titlu):
    return (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='900'>"
        "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='%231F2A44'/><stop offset='1' stop-color='%230B1020'/>"
        "</linearGradient></defs><rect width='1600' height='900' fill='url(%23g)'/>"
        "<text x='80' y='480' fill='%23FFD400' font-family='Georgia' font-size='90' "
        "font-weight='bold'>" + titlu + "</text>"
        "<text x='84' y='540' fill='%23ffffff' font-family='Arial' font-size='30' "
        "opacity='0.6'>C17 · exec-stage-" + str(n) + " · placeholder</text></svg>"
    )


BODY = r'''<body>
<!-- TOP STATUS BAR -->
<header class="topbar">
  <div class="topbar-brand">Sistemul 02 - Excel · C17 · Sistematizare</div>
  <button class="skipped-btn" id="skipped-btn" onclick="jumpToNextSkipped()" style="display:none">
    <span class="skipped-icon">⚠</span>
    <span class="skipped-text">Mergem la pas sărit</span>
    <span class="skipped-count" id="skipped-count">0</span>
  </button>
</header>

<!-- MAIN STAGE -->
<main class="stage" id="stage">

  <div class="stage-nav-fixed" id="stage-nav-fixed">
    <button class="nav-btn nav-btn-prev" id="nav-prev" onclick="prevStep()">← Înapoi</button>
    <button class="nav-btn nav-btn-next" id="nav-next" onclick="nextStep()">Înainte →</button>
  </div>

  <!-- HERO INTRO -->
  <section class="screen" data-screen="hero" data-frag-total="2">
    <div class="hero-prelabel">Construcția 17 Excel</div>
    <h1 class="hero-title">SISTEM<br>RELUABIL</h1>
    <p class="hero-hook frag" data-frag="1">Munca ta merge perfect.<br><span class="hero-hook-twist">Până pleci tu.</span></p>
    <p class="hero-sub frag" data-frag="2">Raportul e gata, dar l-ai făcut tu. Aici nu mai faci raportul, faci munca reluabilă: o hartă vie în workbook, pe care altcineva o pornește fără tine.</p>
  </section>

  <!-- DINAMIC SCREENS injected here -->
  <section class="screen" data-screen="explain"></section>
  <section class="screen" data-screen="step"></section>
  <section class="screen" data-screen="prompt"></section>
  <section class="screen" data-screen="switch"></section>
  <section class="screen" data-screen="verify"></section>
  <section class="screen" data-screen="final" data-frag-total="7">
    <div class="final-block">
      <p class="dim frag" data-frag="1">Nu am automatizat niciun pas.</p>
      <p class="dim frag" data-frag="2">Nu am adăugat nicio regulă sau prag.</p>
      <p class="dim frag" data-frag="3">Nu am predat proprietatea nimănui.</p>
      <p class="accent frag" data-frag="4">O muncă pe care o știai doar tu, acum o hartă vie în workbook.</p>
      <p class="frag" data-frag="5">Un proces care trăia în capul tău; acum altcineva îl pornește fără tine.</p>
      <p class="frag" data-frag="6">Harta reluabilă e gata de pus să ruleze la treapta de autonomie.</p>
      <div class="final-motto frag" data-frag="7">Nu o fac din nou.<br>O fac sistem.</div>
    </div>
  </section>

  <!-- CONCLUZII -->
  <section class="screen" data-screen="conclusion" data-frag-total="2">
    <div class="conclusion-block">
      <h1 class="conclusion-title frag" data-frag="1">
        Concluzii
        <span class="conclusion-title-yellow">Construcția 17</span>
      </h1>
      <div class="conclusion-divider frag" data-frag="2"></div>
    </div>
  </section>

  <!-- EXECUTIVE SHOW - 7 screens -->
  <section class="screen" data-screen="executive" data-exec-slide="1" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-1"></div></div>
    <div class="exec-content"><div class="exec-prelabel frag" data-frag="1">Etapa 1</div><h2 class="exec-title frag" data-frag="2">REALITATE</h2><p class="exec-desc frag" data-frag="3">Munca merge, dar numai cu tine. Fără tine, nu pornește: tu ești ocazia.</p><div class="exec-line frag" data-frag="4"></div></div>
  </section>
  <section class="screen" data-screen="executive" data-exec-slide="2" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-2"></div></div>
    <div class="exec-content"><div class="exec-prelabel frag" data-frag="1">Etapa 2</div><h2 class="exec-title frag" data-frag="2">INVENTAR</h2><p class="exec-desc frag" data-frag="3">Componentele reale, prin HYPERLINK și COUNTA. Harta nu descrie munca, o arată vie.</p><div class="exec-line frag" data-frag="4"></div></div>
  </section>
  <section class="screen" data-screen="executive" data-exec-slide="3" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-3"></div></div>
    <div class="exec-content"><div class="exec-prelabel frag" data-frag="1">Etapa 3</div><h2 class="exec-title frag" data-frag="2">SURSĂ</h2><p class="exec-desc frag" data-frag="3">O singură sursă de adevăr per intrare, fixată ca SRC_, cu oglinda ei vie.</p><div class="exec-line frag" data-frag="4"></div></div>
  </section>
  <section class="screen" data-screen="executive" data-exec-slide="4" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-4"></div></div>
    <div class="exec-content"><div class="exec-prelabel frag" data-frag="1">Etapa 4</div><h2 class="exec-title frag" data-frag="2">RELUARE</h2><p class="exec-desc frag" data-frag="3">Pașii ca lanț navigabil, legat de obiecte. Repetitivii, marcați candidat de automatizare, nu automatizați.</p><div class="exec-line frag" data-frag="4"></div></div>
  </section>
  <section class="screen" data-screen="executive" data-exec-slide="5" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-5"></div></div>
    <div class="exec-content"><div class="exec-prelabel frag" data-frag="1">Etapa 5</div><h2 class="exec-title frag" data-frag="2">EXTERNALIZARE</h2><p class="exec-desc frag" data-frag="3">Convențiile din cap devin PARAM_; cine reia e un profil de competență, nu un nume.</p><div class="exec-line frag" data-frag="4"></div></div>
  </section>
  <section class="screen" data-screen="executive" data-exec-slide="6" data-frag-total="4">
    <div class="exec-image-wrap"><div class="exec-image" data-exec-img="exec-stage-6"></div></div>
    <div class="exec-content"><div class="exec-prelabel frag" data-frag="1">Etapa 6</div><h2 class="exec-title frag" data-frag="2">SUBSTITUT</h2><p class="exec-desc frag" data-frag="3">Altcineva pornește din _SISTEM și reia munca fără tine. Apoi handoff spre C18.</p><div class="exec-line frag" data-frag="4"></div></div>
  </section>
  <section class="screen exec-closing" data-screen="executive" data-exec-slide="7" data-frag-total="4">
    <div class="exec-content">
      <div class="exec-closing-prelabel frag" data-frag="1">Motto:</div>
      <h1 class="exec-closing-motto frag" data-frag="2">
        Pleci, și munca
        <span class="exec-closing-motto-yellow">o reia altcineva.</span>
      </h1>
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
'''


STAGES = r'''const STAGES = [
  {
    id: 1, name: "REALITATE", emotion: "Munca pe care o știi doar tu",
    hook: "Munca e validată, raportul iese. Și totuși, fără tine, nu pornește.",
    next: "Pentru că trăiește doar în capul tău.",
    steps: [
      { num: "01", title: "Workbook-ul merge, dar numai cu tine la cârmă.",
        instr: "Deschizi workbook-ul cu tot procesul care a produs raportul. <strong>Funcționează, dar ca să-l reiei trebuie să știi din cap de unde pleci.</strong>",
        excel: true },
      { num: "02", title: "Dai workbook-ul altcuiva și se blochează.",
        instr: "Un coleg instruit se uită la foile împrăștiate și întreabă de unde începe. <strong>Lipsa nu e de date, e de hartă.</strong>",
        excel: true },
      { num: "03", title: "Creezi foaia _SISTEM și declari harta reluabilă.",
        instr: "Adaugi o foaie nouă, prima. <strong>Nu o procedură de citit: o hartă vie, legată de foile reale.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "INVENTAR", emotion: "Componentele reale",
    hook: "Înainte să scrii pașii, vezi din ce e făcută munca.",
    next: "Ce e sursă, ce e lucru, ce e ieșire.",
    steps: [
      { num: "04", title: "Ce componente are de fapt munca.",
        instr: "Nu ce raport iese, ci din ce e făcut procesul. <strong>Componentele există deja; tu le faci vizibile și navigabile.</strong>",
        excel: true },
      { num: "05", title: "Inventarul componentelor reale. Promptul 1.", instr: "", prompt: 1 },
      { num: "06", title: "Blocul A: componente prin HYPERLINK și COUNTA.",
        instr: "Fiecare componentă, un link viu către foaia reală, cu cât conține. <strong>Harta nu descrie munca, o arată vie. Oglindă, nu motor.</strong>",
        excel: true }
    ]
  },
  {
    id: 3, name: "SURSĂ", emotion: "O singură sursă pentru fiecare intrare",
    hook: "O hartă reluabilă cere un singur adevăr per intrare.",
    next: "Sursa canonică, fixată ca SRC_.",
    steps: [
      { num: "07", title: "Fiecare intrare, o singură sursă de adevăr.",
        instr: "Alegi sursa canonică și o fixezi ca named range SRC_. <strong>Nu copiezi datele, le legi. Numele spune singur de unde.</strong>",
        excel: true },
      { num: "08", title: "Elimini dublura sursei.",
        instr: "Dacă o intrare venea din două locuri, declari unul singur canonic. <strong>O intrare, o sursă, un nume.</strong>",
        excel: true },
      { num: "09", title: "Blocul B: SRC_ cu oglinda lui vie.",
        instr: "Lângă SRC_ pui ROWS(SRC_), câte rânduri are acum. <strong>Oglinda doar arată, nu verifică un prag și nu blochează.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "RELUARE", emotion: "Ordinea legată de obiecte",
    hook: "Scrii pașii ca lanț navigabil, fără să automatizezi.",
    next: "Fiecare pas duce la obiectul real.",
    steps: [
      { num: "10", title: "Ordinea de reluare, pas cu pas.",
        instr: "Scrii secvența reală, fiecare pas o acțiune de om, în ordine. <strong>Harta spune ce se face și unde, nu o face în locul tău.</strong>",
        excel: true },
      { num: "11", title: "Lanțul de pași legați de obiecte. Promptul 2.", instr: "", prompt: 2 },
      { num: "12", title: "Blocul C: pași, obiect atins, rezultat oglindit.",
        instr: "Fiecare pas, un link la zona lui, cu obiectul OBJ_ și rezultatul oglindit. <strong>Repetitivii, etichetați candidat de automatizare, dar lăsați manuali.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "EXTERNALIZARE", emotion: "Cunoașterea scoasă din cap",
    hook: "Ce știai doar tu devine vizibil.",
    next: "Convenții ca PARAM_, profil de competență.",
    steps: [
      { num: "13", title: "Convențiile din capul tău devin parametri vii.",
        instr: "Alegerile de proces le scrii ca named ranges PARAM_, cu valoarea în celulă. <strong>Reluarea le citește din workbook, nu din tine.</strong>",
        excel: true },
      { num: "14", title: "Cine poate relua: profil de competență, nu nume.",
        instr: "Scrii ce competență îi trebuie, nu cine anume. <strong>Nu numești un titular și nu predai răspunderea.</strong>",
        excel: true },
      { num: "15", title: "Blocul D și E: profil plus parametri.",
        instr: "Harta are tot ce trăia în capul tău. <strong>Nimic cum-știu-eu nesemnat: orice alegere e scrisă ca PARAM_.</strong>",
        excel: true }
    ]
  },
  {
    id: 6, name: "SUBSTITUT", emotion: "Testul substitutului",
    hook: "Proba finală: altcineva pornește din _SISTEM, fără tine.",
    next: "Apoi marchezi granița spre automatizare.",
    steps: [
      { num: "16", title: "START AICI și punctul de reluare.",
        instr: "În blocul F pui un START AICI și un punct de reluare. <strong>Oricine deschide harta știe de unde începe, fără să te întrebe.</strong>",
        excel: true },
      { num: "17", title: "Testul substitutului: altcineva reia, fără tine.",
        instr: "Dai workbook-ul și pleci din cameră. <strong>Pornește din START AICI și reia munca doar din foaie. Dacă te întreabă ceva nescris, mai ai de scris.</strong>",
        excel: true },
      { num: "18", title: "Granița spre automatizare: harta e gata, treapta următoare o pune să ruleze.",
        instr: "C17 face munca reluabilă de un om. <strong>Predai pașii candidat de automatizare; automatizarea, guvernarea și predarea încep mai sus.</strong>",
        excel: false }
    ]
  }
];

'''


PROMPTS = r'''const PROMPTS = {
  1: {
    label: "Prompt 01 · Inventarul componentelor reale",
    text: "Am un workbook care a produs un raport. Parcurge foile lui și fă-mi un inventar al componentelor reale: pentru fiecare foaie, spune dacă e sursă, foaie de lucru sau ieșire, și ce rol are în proces. Propune o listă, dar nu construi nicio hartă și nu hotărî tu rolurile finale; eu confirm. Nu automatiza nimic, nu adăuga reguli sau praguri, nu desemna responsabili. Vreau doar să văd din ce e făcută munca.",
    meta: "Copilot inventariază. Tu confirmi rolurile."
  },
  2: {
    label: "Prompt 02 · Lanțul de reluare legat de obiecte",
    text: "Pe baza componentelor și surselor confirmate, propune-mi ordinea de reluare a muncii ca lanț de pași. Pentru fiecare pas spune ce obiect real din workbook se atinge și ce rezultat devine vizibil. Marchează care pași sunt repetitivi și ar fi candidați de automatizare mai târziu, dar nu îi automatiza și nu scrie niciun macro. Nu adăuga reguli, praguri sau validări, nu stabili cine răspunde. Pașii rămân acțiuni de om, în ordine.",
    meta: "Pașii rămân acțiuni de om, în ordine."
  }
};

'''


def main():
    t = open(SRC, encoding='utf-8').read()
    b = t.index('<body>')
    s = t.index('<script>')
    head, _, tail = t[:b], t[b:s], t[s:]

    head = re.sub(r'<title>C\d+[^<]*</title>', '<title>C17 · SISTEMATIZARE · BROADCAST</title>', head, count=1)
    for n in range(1, 7):
        ph = exec_placeholder(n, EXEC_TITLES[n])
        head = re.sub(
            r'(\.exec-image\[data-exec-img="exec-stage-%d"\]\s*\{\s*background-image:\s*)'
            r'url\("[^"]*"\)' % n,
            lambda m, ph=ph: m.group(1) + 'url("%s")' % ph,
            head, count=1)

    i_st = tail.index('const STAGES = [')
    i_fl = tail.index('// FLOW')
    tail = tail[:i_st] + STAGES + PROMPTS + tail[i_fl:]
    tail = re.sub(r'trainity_c\d+_video_v1', 'trainity_c17_video_v1', tail)

    out = head + BODY + tail
    open(OUT, 'w', encoding='utf-8').write(out)

    leftover = re.findall(r'trainity_c16|Date_MASTER-C16|Livrare|LIVRARE|DECIZIA|decizie de luat', out)
    print('SCRIS:', OUT, '-', len(out.splitlines()), 'linii')
    print('  title:', re.search(r'<title>[^<]*</title>', out).group(0))
    print('  exec base64 jpeg ramase (trebuie 0, placeholdere):', out.count('data:image/jpeg;base64,'))
    print('  leftover C16:', len(leftover), leftover[:6])
    print('  STAGES steps:', out.count('num: "'), '| prompturi:', out.count('label: "Prompt'))
    for ch in ['—', '–']:
        if ch in out:
            print('  ATENTIE em/en-dash!')


if __name__ == '__main__':
    main()
