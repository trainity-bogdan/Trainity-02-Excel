#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transforma cele 4 HTML C02 din identitatea veche MARCARE in identitatea LOCK CONTROL
(CORESPONDENTA CU REALITATEA). Inlocuire pe baza de ancore (a n-a aparitie a fiecarei
clase), aliniata la BLUEPRINT-C02-CONTROL + Date_MASTER real (5 anomalii: orase, TVA,
scadenta, NETWORKDAYS, CNP; AF/CF; status_validare/motiv_anomalie; fara ecouri de suma).
Raporteaza fiecare tinta negasita + leftover-uri MARCARE.
"""
import re, os, sys

FILES = [
    ('HTML-Studiu-Excel-02-Marcare.html', 'HTML-Studiu-Excel-02-Control.html'),
    ('HTML-Editor-Studiu-Excel-02-Marcare.html', 'HTML-Editor-Studiu-Excel-02-Control.html'),
    ('HTML-Video-Excel-02-Marcare.html', 'HTML-Video-Excel-02-Control.html'),
    ('HTML-Editor-Video-Excel-02-Marcare.html', 'HTML-Editor-Video-Excel-02-Control.html'),
]
DIR = 'c02'
report = []

def repl_nth(h, tag, cls, items):
    """Inlocuieste inner-ul fiecarei aparitii (in ordine) a <tag class="cls">...</tag>."""
    pat = re.compile(r'(<' + tag + r' class="' + re.escape(cls) + r'"[^>]*>)(.*?)(</' + tag + r'>)', re.S)
    idx = [0]
    def f(m):
        i = idx[0]; idx[0] += 1
        if i < len(items) and items[i] is not None:
            return m.group(1) + items[i] + m.group(3)
        return m.group(0)
    out = pat.sub(f, h)
    if idx[0] < len(items):
        report.append(f"  ! {cls}: gasit {idx[0]} aparitii, asteptat {len(items)}")
    return out

def repl_one(h, old, new, label):
    if old in h:
        return h.replace(old, new)
    report.append(f"  ! string negasit [{label}]: {old[:50]}")
    return h

# ============================== CONTENT CONTROL ==============================
STEPS = [
 ("Deschide setul predat de construcția precedentă",
  "Dublu-click pe Date_MASTER-C02.xlsx, foaia Vanzari. Setul predat de C01 e structural curat. Acum cauți altceva: valori valide care mint față de realitate."),
 ("Recunoaște că validul poate fi greșit",
  "Un oraș scris în trei feluri. O cotă de TVA care nu respectă categoria. O scadență înaintea facturii. O factură într-o zi nelucrătoare. Un CNP care se contrazice. Excel le acceptă pe toate."),
 ("Deschide foile de referință ale setului",
  "Setul vine cu nomenclatoarele lui: tbl_Localitati, tbl_RegulriTVA, tbl_SarbatoriLegale, tbl_CodJudetCNP. Acestea sunt sursa de adevăr față de care confrunți fiecare valoare."),
 ("Activează Copilot pe foaia Vanzari",
  "Deschide Copilot în panoul lateral Excel, pe foaia Vanzari. Nu ceri nicio modificare. Doar interoghezi."),
 ("Rulează Promptul 1 de interogare",
  "Lipești promptul de mai jos. AI descrie ce valori par valide dar suspecte față de realitate: orașe inconsistente, cote, date, identificatori. Nu modifică nicio celulă."),
 ("Citește harta suspiciunilor",
  "AI întoarce categoriile de suspiciune: unde geografia nu corespunde, unde cota pare greșită, unde datele se contrazic. Acum știi unde să confrunți, nu doar bănuiești."),
 ("Descoperă nomenclatorul real cu Advanced Filter",
  "Pe coloana oras, Advanced Filter cu unique records only scoate toate scrierile existente. Acesta e materialul brut din care iese forma oficială. AF descoperă, nu corectează."),
 ("Rulează Promptul 2 de semnalizare",
  "Lipești promptul de mai jos. AI construiește formulele de confruntare: COUNTIF pe nomenclatorul de localități, XLOOKUP pe regulile de TVA, comparație de date, NETWORKDAYS.INTL pe calendarul de sărbători."),
 ("Construiește coloanele de semnalizare",
  "Fiecare formulă scrie un flag: flag_oras, flag_tva, flag_scadenta, flag_zi. status_validare devine OK sau DE INVESTIGAT, iar motiv_anomalie adună motivele. Valorile sursă rămân neatinse."),
 ("Confruntă semnalările cu setul",
  "Parcurge rândurile DE INVESTIGAT. Fiecare are motivul lui exact alături. Verifici că flag-ul corespunde unei neconcordanțe reale față de realitate, nu unui fals pozitiv."),
 ("Cuantifică anomaliile cu COUNTIF",
  "COUNTIF pe fiecare flag: câte orașe nealiniate, câte cote greșite, câte scadențe imposibile, câte zile nelucrătoare. Foaia _SEMNALIZARE confirmă distribuția numeric."),
 ("Marchează vizual ce necesită decizie",
  "Conditional Formatting colorează rândurile DE INVESTIGAT. Semnalarea marchează pentru ochi, nu corectează. Decizia rămâne a business-ului."),
 ("Ancorează semnalarea într-un tabel structurat",
  "Formulele de flag trăiesc într-un tabel Excel (tbl_Vanzari). Orice rând nou primește automat aceeași confruntare cu realitatea, fără să rescrii o formulă."),
 ("Testează pe un set nou",
  "Adaugi rânduri noi cu aceeași schemă. Flag-urile și status_validare se aplică instant. Aceeași judecată, alt set."),
 ("Fixează regula anti-derivă",
  "Notează cele 5 confruntări și nomenclatoarele lor. Dacă apare un fenomen nou de realitate, adaugi o confruntare explicită, nu o lași să treacă tăcut."),
 ("Verifică sistemul cap-coadă",
  "Setul curat primește status și motiv. Numărul de rânduri rămâne identic. Valorile sursă sunt neatinse. Fiecare neconcordanță are motivul ei."),
 ("Confirmă setul controlat",
  "Setul cu anomaliile semnalate poate intra în decizie cu dovezi: știi ce e valid, ce e de investigat și de ce. Validul nu mai trece automat drept corect."),
 ("Predă către C03",
  "Setul controlat e pregătit pentru C03 Audit: defectele tehnice invizibile, pe care nici ochiul, nici confruntarea cu realitatea nu le văd. Spații, text-vs-număr, caractere ascunse."),
]
STAGE_LABEL = ["ETAPA 1 · TABELUL PARE VALID","ETAPA 2 · INTEROGARE ASISTATĂ DE AI",
 "ETAPA 3 · CONSTRUIREA SEMNALIZĂRII","ETAPA 4 · VERIFICAREA CORESPONDENȚEI",
 "ETAPA 5 · ANCORARE LA SURSĂ","ETAPA 6 · PAYOFF"]
STAGE_NAME = ["REALITATE","INVESTIGAȚIE","TRANSFORMARE","VERIFICARE","STABILIZARE","CONFIRMARE"]
PHASE_TAG = ["INPUT","AI","FORMULE","CONTROL","RECALCUL","PAYOFF"]
TYPE_TAG = ["Manual","Copilot · Promptul 1","Promptul 2","COUNTIF","Tabel structurat","Cap-coadă"]
STAGE_QUOTE = [
 "Deschizi setul predat de construcția precedentă. Structural curat. Dar o valoare validă poate fi greșită față de realitate.",
 "Nu semnalăm încă. Întâi interoghezi AI: ce valori par valide dar suspecte față de realitate. Doar întrebare, nicio modificare.",
 "Cu suspiciunile interogate, construiești aparatul de semnalizare: confrunți fiecare valoare cu nomenclatorul ei, prin formule. Datele nu se modifică.",
 "Nu avem încredere oarbă în semnalare. COUNTIF pe fiecare flag. Confrunți fiecare neconcordanță cu setul și o cuantifici.",
 "Semnalarea nu e o intervenție unică. Formulele stau într-un tabel structurat. Set nou cu aceeași schemă, aceeași judecată.",
 "Construcția e validată operațional. Verifici sistemul cap-coadă și predai setul cu anomaliile de realitate semnalate către C03.",
]
ANOM_TITLE = ["ORAȘE NEALINIATE","TVA GREȘIT","SCADENȚĂ &lt; FACTURĂ","ZI NELUCRĂTOARE","CNP CONTRADICTORIU"]
ANOM_DESC = [
 "Aceeași localitate scrisă în mai multe feluri, sau un oraș plasat într-un județ în care nu există.",
 "O cotă validă ca număr, dar nelegală pentru categoria produsului.",
 "Două date valide, dar scadența cade înaintea facturii.",
 "O factură datată într-o sărbătoare legală sau o duminică.",
 "Un CNP care pare corect, dar se contrazice cu sexul, județul, data nașterii sau cifra de control.",
]
ANOM_LIE = [
 "<b>Greșeala față de realitate:</b> geografia nu corespunde.",
 "<b>Greșeala față de realitate:</b> regula fiscală e încălcată.",
 "<b>Greșeala față de realitate:</b> ordinea în timp e imposibilă.",
 "<b>Greșeala față de realitate:</b> firma nu opera în acea zi.",
 "<b>Greșeala față de realitate:</b> identitatea nu se susține.",
]
FINAL_LABEL = ["CONTROL","NOMENCLATOARE","SEMNALIZARE","VOLUM","ORAȘE / TVA","TIMP","CNP","SURSĂ NEATINSĂ"]
FINAL_TEXT = [
 "Date_MASTER-C02.xlsx există și se deschide pe foaia Vanzari.",
 "Cele 4 foi de referință sunt prezente: localități, TVA, sărbători, cod-județ.",
 "Coloanele de flag, status_validare și motiv_anomalie sunt populate prin formule.",
 "Numărul de rânduri OUTPUT egal cu INPUT. Nimic șters.",
 "COUNTIF confirmă orașele nealiniate și cotele de TVA greșite.",
 "Scadențele imposibile și zilele nelucrătoare sunt semnalate.",
 "Pe CONTACTE, contradicțiile de sex, județ, dată și cifră de control sunt marcate.",
 "Valorile sursă rămân identice. Semnalarea marchează, nu corectează.",
]
TU_STATEMENTS = [
 'Oamenii cred valoarea fiindcă Excel o acceptă.<br><span class="tu-hl">Profesioniștii o confruntă cu realitatea.</span>',
 'Valid nu înseamnă corect.',
 'Nu mai accepți valoarea pe cuvânt. <span class="tu-hl">O confrunți cu realitatea.</span>',
]

def transform(h):
    # identitate + referinte de fisiere/assets in markup si JS
    h = h.replace('02-Marcare', '02-Control')
    h = repl_one(h, 'C02 · Marcare', 'C02 · Control', 'topbar/title')
    # hero singletons
    h = repl_nth(h, 'span', 'hero-question-text', ['Câte valori valide sunt, de fapt, greșite?'])
    h = repl_nth(h, 'h1', 'cover-title', ['Cum pui sub control corespondența datelor cu realitatea'])
    h = repl_nth(h, 'p', 'hero-microbrief', ['O valoare poate fi acceptată de Excel și totuși să fie greșită față de realitate: un oraș care nu există în acel județ, o cotă de TVA nelegală, o scadență înaintea facturii. În această construcție confrunți fiecare valoare cu realitatea, fără să o repari.'])
    h = repl_nth(h, 'div', 'cover-miza', ['Valorile valide pot fi greșite față de realitate. C02 le confruntă cu nomenclatoare, reguli și calendare, semnalează fiecare neconcordanță cu motivul ei și nu modifică nicio valoare sursă.'])
    h = repl_nth(h, 'span', 'ib-1', ['Pare valid.'])
    h = repl_nth(h, 'span', 'ib-2', ['E greșit.'])
    h = repl_nth(h, 'div', 'mantra-band-main', ['Nu credem valorile. Le confruntăm cu <mark>realitatea</mark>.'])
    h = repl_nth(h, 'p', 'tu-lead', ['Lucrezi cu un set care a trecut toate validările. Și totuși:'])
    h = repl_nth(h, 'p', 'tu-statement', TU_STATEMENTS)
    # liste
    h = repl_nth(h, 'ul', 'tu-list', ['<li>un oraș scris în trei feluri diferite</li><li>o cotă de TVA care nu respectă categoria</li><li>o scadență căzută înaintea facturii</li>'])
    # before/after + outcomes: ul-uri fara clasa, le tintim prin context
    h = repl_one(h, '<div class="ba-label">ÎNAINTE</div><ul><li>anomalii ascunse în date</li><li>ștergeri pe loc, fără urmă</li><li>totaluri instabile la filtrare</li><li>nicio dovadă a deciziei</li></ul>',
        '<div class="ba-label">ÎNAINTE</div><ul><li>valori greșite sub aparența validă</li><li>rapoarte construite din date necontrolate</li><li>nicio dovadă pentru ce e suspect</li><li>decizii pe valori nelegate de realitate</li></ul>', 'BA-INAINTE')
    h = repl_one(h, '<div class="ba-label">DUPĂ</div><ul><li>fiecare anomalie marcată</li><li>nimic șters, totul trasabil</li><li>totaluri stabile, verificabile</li><li>motiv clar pentru fiecare rând</li></ul>',
        '<div class="ba-label">DUPĂ</div><ul><li>fiecare neconcordanță semnalată</li><li>nimic modificat, totul trasabil</li><li>motiv clar pentru fiecare rând</li><li>dovezi pentru decizia de business</li></ul>', 'BA-DUPA')
    h = repl_one(h, '<li>set auditat</li><li>anomalii trasabile</li><li>bază pentru audit valoric</li><li>încredere în rapoarte</li>',
        '<li>set cu anomalii semnalate</li><li>aparatul de confruntare cu realitatea</li><li>dovezi pentru fiecare decizie</li><li>încredere că valid = corect</li>', 'OUTCOMES')
    # sm-step
    h = repl_one(h, '<span class="sm-step active">MARCARE</span>', '<span class="sm-step active">CONTROL</span>', 'sm-active')
    h = repl_one(h, '<span class="sm-step">AUDITARE</span>', '<span class="sm-step">AUDIT</span>', 'sm-audit')
    # anomaly cards
    h = repl_nth(h, 'b', 'anomaly-title', ANOM_TITLE)
    h = repl_nth(h, 'p', 'anomaly-desc', ANOM_DESC)
    h = repl_nth(h, 'p', 'anomaly-lie', ANOM_LIE)
    # section-marker (scena)
    h = repl_nth(h, 'div', 'section-marker', ['SCENA REALĂ · CE PARE VALID DAR NU ESTE CORECT'])
    # stages
    h = repl_nth(h, 'div', 'stage-label', STAGE_LABEL)
    h = repl_nth(h, 'h2', 'stage-name', STAGE_NAME)
    h = repl_nth(h, 'span', 'phase-tag', PHASE_TAG)
    h = repl_nth(h, 'span', 'type-tag', TYPE_TAG)
    h = repl_nth(h, 'p', 'stage-quote', STAGE_QUOTE)
    # steps
    h = repl_nth(h, 'h3', 'step-title', [t for t, a in STEPS])
    h = repl_nth(h, 'p', 'step-action', [a for t, a in STEPS])
    # final cards
    h = repl_nth(h, 'div', 'final-label', FINAL_LABEL)
    h = repl_nth(h, 'div', 'final-text', FINAL_TEXT)
    # completion
    h = repl_nth(h, 'div', 'completion-title', ['Set controlat validat.'])
    h = repl_nth(h, 'div', 'completion-subtitle', ['Toate cele 8 verificări finale confirmate. C02 e pregătit pentru C03 Audit.'])
    h = repl_nth(h, 'h3', 'next-title', ['C03 · Audit'])
    h = repl_nth(h, 'p', 'next-desc', ['Valorile sunt acum confruntate cu realitatea, dar pot ascunde defecte tehnice invizibile. Aparența curățeniei nu e dovadă. C03 demonstrează forensic ce e cu adevărat curat, sub spațiile și caracterele ascunse.'])
    h = repl_nth(h, 'div', 'payoff-line dim', ['Nu am modificat nicio valoare.','Nu am șters rânduri.','Nu am reparat nimic.'])
    h = repl_nth(h, 'div', 'payoff-line accent', ['Am semnalat fiecare neconcordanță cu motivul exact.'])
    h = repl_nth(h, 'div', 'payoff-line regular', ['Validul nu mai trece drept corect.','C03 poate începe.'])
    h = repl_nth(h, 'span', 'wow-tag', ['WOW:'])
    h = repl_one(h, '<span data-wow="1">Raportul nu mai înghite minciuna. O marchează.</span>',
        '<span data-wow="1">Excel acceptă orice valoare validă. Acum ai aparatul care întreabă dacă e și corectă.</span>', 'wow')
    h = repl_nth(h, 'div', 'payoff-motto', ['Încrederea începe după confruntarea cu realitatea.'])
    # prompturi (label + text)
    h = repl_one(h, 'PROMPT 1 · INSTRUMENT DE AUDIT', 'PROMPT 1 · INSTRUMENT DE INTEROGARE', 'p1-label')
    h = repl_one(h, 'PROMPT 2 · INSTRUMENT DE MARCARE CONTROLATĂ', 'PROMPT 2 · CONSTRUIREA SEMNALIZĂRII', 'p2-label')
    h = repl_nth(h, 'div', 'prompt-text', [
        'Mă uit la acest set și pare ordonat, dar suspectez că unele valori, deși valide, sunt greșite față de realitate. Verifică pe coloane și spune-mi: există orașe care nu se potrivesc cu județul lor? Există cote de TVA care nu respectă categoria produsului? Există scadențe căzute înaintea facturii? Există facturi în zile nelucrătoare? Există CNP-uri care se contrazic intern? Numără pe fiecare categorie. Nu modifica nimic, doar raportează.',
        'Acum că știi ce valori par greșite față de realitate, ajută-mă să le semnalez fără să le modific. Construiește formulele care confruntă fiecare valoare cu nomenclatorul ei: COUNTIF pe lista de localități, XLOOKUP pe regulile de TVA, comparație între scadență și factură, NETWORKDAYS.INTL pe calendarul de sărbători. Scrie câte un flag pe fiecare regulă, apoi status_validare cu OK sau DE INVESTIGAT și motiv_anomalie cu textul exact. Nu modifica nicio valoare sursă. Vreau să reaplic același aparat pe alt set luna viitoare.'])
    # investigatie (6 inv-items): status -> OK / DE INVESTIGAT
    h = repl_one(h, 'status-bad">DE VERIFICAT</div>', 'status-bad">DE INVESTIGAT</div>', 'inv-dv')
    h = h.replace('status-bad">EXCLUS</div>', 'status-bad">DE INVESTIGAT</div>')
    h = repl_one(h, 'status-good">VALID</div>', 'status-good">OK</div>', 'inv-ok')
    h = repl_nth(h, 'div', 'inv-item-label', ['ORAȘE NEALINIATE','TVA GREȘIT','SCADENȚĂ &lt; FACTURĂ','ZI NELUCRĂTOARE','CNP CONTRADICTORIU','RESTUL VALORILOR'])
    h = repl_nth(h, 'div', 'inv-item-desc', [
        'Aceeași localitate scrisă diferit, sau un oraș care nu există în acel județ.',
        'Cotă validă ca număr, dar nelegală pentru categoria produsului.',
        'data_scadentei cade înaintea lui data_factura. Ordine imposibilă.',
        'data_factura într-o sărbătoare legală sau o duminică. Firma nu opera.',
        'Sexul, județul, data nașterii sau cifra de control nu se susțin reciproc.',
        'Conforme cu realitatea pe toate cele cinci confruntări. Rămân OK.'])
    # ba-val demo (perechi before/after pe etape)
    for old, new in [
        ('amestecate invizibil cu datele bune','amestecate invizibil cu valorile corecte'),
        ('vizibil marcate cu status și motiv','semnalate cu flag, status și motiv'),
        ('implicită, ad-hoc, repetabilă greu','confruntare ad-hoc, greu de repetat'),
        ('explicită pe trei niveluri standardizate','aparat ancorat într-un tabel structurat'),
        ('suma martor pe coloana valoare_neta','valorile sursă în coloana valoare_neta'),
        ('identică, marcarea nu schimbă valori','identice, semnalarea nu le schimbă'),
        ('total contaminat cu anomalii','valori valide dar greșite, necontrolate'),
        ('SUMIF pe status VALID, raportabilă cu încredere','fiecare neconcordanță semnalată, cu motiv'),
    ]:
        h = repl_one(h, old, new, 'baval')
    # nav-meta + footer
    h = repl_one(h, '3 pași · AGGREGATE', '3 pași · COUNTIF', 'nav-aggr')
    h = repl_one(h, '3 pași · Power Query Refresh', '3 pași · Tabel structurat', 'nav-pq')
    h = repl_one(h, 'C02 MARCARE', 'C02 CONTROL', 'footer')
    return h

for src, dst in FILES:
    sp = os.path.join(DIR, src)
    if not os.path.exists(sp):
        report.append(f"LIPSA: {src}"); continue
    report.append(f"\n=== {src} -> {dst} ===")
    h = open(sp, encoding='utf-8').read()
    h = transform(h)
    open(os.path.join(DIR, dst), 'w', encoding='utf-8').write(h)
    # leftover MARCARE-isme
    left = []
    for term in ['Marcare','MARCARE','marchează','week-end','duplicat','Duplicat','dată în viitor',
                 'cod client','câmp obligatoriu','SUMIF','EXCLUS','Power Query','suma martor','suma fizică','adevărat']:
        c = len(re.findall(term, h))
        if c: left.append(f"{term}={c}")
    report.append("  leftover: " + (", ".join(left) if left else "ZERO"))

print("\n".join(report))
