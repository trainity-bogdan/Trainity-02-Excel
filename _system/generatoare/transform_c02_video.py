#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transforma HTML-Video + HTML-Editor-Video C02 din MARCARE in CONTROL.
Inlocuieste blocurile JS STAGES si PROMPTS integral + frag-urile exec/hook/wow/motto."""
import re, os

FILES = [
    ('HTML-Video-Excel-02-Marcare.html', 'HTML-Video-Excel-02-Control.html'),
    ('HTML-Editor-Video-Excel-02-Marcare.html', 'HTML-Editor-Video-Excel-02-Control.html'),
]
DIR = 'c02'
report = []

NEW_STAGES = '''const STAGES = [
  {
    id: 1, name: "REALITATE", emotion: "Tabelul pare valid",
    hook: "Te uiți la un set care a trecut toate validările.",
    next: "Astăzi descoperim de ce validul poate fi greșit.",
    steps: [
      { num: "01", title: "Deschidem setul predat de construcția precedentă.",
        instr: "Setul predat este curat structural. <strong>Aici începe altă căutare: ce trece validarea tehnică, dar e greșit față de realitate.</strong>",
        excel: true },
      { num: "02", title: "Privim valorile, nu structura.",
        instr: "Un oraș care nu există în acel județ. O cotă de TVA nelegală pentru categorie. O scadență înaintea facturii. O factură într-o zi nelucrătoare. Un CNP care se contrazice. <strong>Toate trec validarea. Niciuna nu e corectă.</strong>",
        excel: true },
      { num: "03", title: "Deschidem foile de referință.",
        instr: "Setul vine cu nomenclatoarele lui: localități, reguli de TVA, sărbători legale, coduri de județ. <strong>Acestea sunt realitatea față de care confruntăm fiecare valoare.</strong>",
        excel: true }
    ]
  },
  {
    id: 2, name: "INVESTIGAȚIE", emotion: "Suspiciune metodică",
    hook: "AI-ul nu semnalează încă.",
    next: "Înainte să semnalăm, lăsăm AI-ul să interogheze pe categorii.",
    steps: [
      { num: "04", title: "Activăm Copilot. Fără să-i cerem acțiune.",
        instr: "Deschidem Copilot pe foaia Vanzari. <strong>Nu îi cerem să modifice. Îi cerem să interogheze pe categorii.</strong> AI-ul care decide fără diagnostic decide greșit.",
        excel: true },
      { num: "05", title: "Punem AI-ul să interogheze. Promptul 1.", instr: "", prompt: 1 },
      { num: "06", title: "Citim raportul. Pe cele cinci categorii.",
        instr: "Confirmăm fiecare categorie de suspiciune. <strong>Dacă Copilot vede mai puține neconcordanțe decât realitatea, întrebăm din nou.</strong> Investigația nu se închide cu îndoieli.",
        excel: true }
    ]
  },
  {
    id: 3, name: "TRANSFORMARE", emotion: "Construirea semnalizării",
    hook: "Nu modificăm valori. Le confruntăm cu realitatea.",
    next: "Formulele construiesc coloanele de semnalizare: flag, status și motiv.",
    steps: [
      { num: "07", title: "Descoperim nomenclatorul real cu Advanced Filter.",
        instr: "Pe coloana oras, Advanced Filter cu unique records scoate toate scrierile existente. <strong>Materialul brut din care iese forma oficială. AF descoperă, nu corectează.</strong>",
        excel: true },
      { num: "08", title: "Construim formulele de confruntare. Promptul 2.", instr: "", prompt: 2 },
      { num: "09", title: "Aplicăm și obținem setul semnalizat.",
        instr: "COUNTIF pe localități, XLOOKUP pe TVA, comparație de date, NETWORKDAYS.INTL pe calendar. <strong>Fiecare regulă scrie un flag. status_validare devine OK sau DE INVESTIGAT, motiv_anomalie adună motivele. Valorile sursă rămân neatinse.</strong>",
        excel: true }
    ]
  },
  {
    id: 4, name: "VERIFICARE", emotion: "Verificarea corespondenței",
    hook: "O semnalare scrisă nu e o semnalare confirmată.",
    next: "Cifrele decid. COUNTIF aduce dovada numerică.",
    steps: [
      { num: "10", title: "Confruntăm semnalările cu setul.",
        instr: "Parcurgem rândurile DE INVESTIGAT. <strong>Fiecare flag trebuie să corespundă unei neconcordanțe reale față de realitate, nu unui fals pozitiv.</strong>",
        excel: true },
      { num: "11", title: "Cuantificăm anomaliile cu COUNTIF.",
        instr: "COUNTIF pe fiecare flag: câte orașe nealiniate, câte cote greșite, câte scadențe imposibile, câte zile nelucrătoare. <strong>Foaia _SEMNALIZARE confirmă distribuția numeric.</strong>",
        excel: true },
      { num: "12", title: "Marcăm vizual ce necesită decizie.",
        instr: "Conditional Formatting colorează rândurile DE INVESTIGAT. <strong>Semnalarea marchează pentru ochi, nu corectează. Decizia rămâne a business-ului.</strong>",
        excel: true }
    ]
  },
  {
    id: 5, name: "STABILIZARE", emotion: "Ancorare la sursă",
    hook: "Un set confruntat azi nu se confruntă singur luna viitoare.",
    next: "Decât dacă formulele rămân ancorate într-un tabel structurat.",
    steps: [
      { num: "13", title: "Ancorăm semnalarea într-un tabel structurat.",
        instr: "Formulele de flag trăiesc în tabelul Excel. <strong>Orice rând nou primește automat aceeași confruntare cu realitatea.</strong>",
        excel: true },
      { num: "14", title: "Testăm cu un set nou.",
        instr: "Adăugăm rânduri noi de aceeași schemă. <strong>Dacă flag-urile și status_validare se aplică singure, mecanismul e viu. Dacă nu, nu am construit nimic.</strong>",
        excel: true },
      { num: "15", title: "Fixăm regula anti-derivă.",
        instr: "Notăm cele cinci confruntări și nomenclatoarele lor. <strong>Dacă apare un fenomen nou de realitate, adăugăm o confruntare explicită, nu o lăsăm să treacă tăcut.</strong>",
        excel: false }
    ]
  },
  {
    id: 6, name: "CONFIRMARE", emotion: "Predarea către C03",
    hook: "Valorile păreau valide.",
    next: "De data asta, fiecare neconcordanță are motivul ei explicit.",
    steps: [
      { num: "16", title: "Verificăm sistemul cap-coadă.",
        instr: "Reluăm setul, citim _SEMNALIZARE. <strong>Numărul de rânduri rămâne identic. Valorile sursă sunt neatinse. Fiecare neconcordanță are motivul ei.</strong>",
        excel: true },
      { num: "17", title: "Confirmăm setul controlat.",
        instr: "Flag, status și motiv pe fiecare rând. <strong>Acest set poate intra în decizie cu dovezi: știm ce e valid, ce e de investigat și de ce.</strong>",
        excel: true },
      { num: "18", title: "Predăm către C03.",
        instr: "Confirmăm construcția finalizată. <strong>C03 nu va începe de la încredere oarbă. Va începe de la un set unde anomaliile de realitate sunt semnalate, dar contaminarea tehnică invizibilă încă urmează să fie demonstrată.</strong>",
        excel: false }
    ]
  }
];'''

NEW_PROMPTS = '''PROMPTS = {
  1: {
    label: "Prompt 01 · Interogare",
    text: "Interoghează acest set de vânzări fără să modifici nimic. Pe categorii: câte rânduri au un oraș care nu există în județul declarat, câte au o cotă de TVA care nu respectă categoria produsului, câte au scadența înaintea facturii, câte au data facturii într-o sărbătoare legală sau o duminică, câte CNP-uri de pe contacte se contrazic intern. Raportează numeric, pe fiecare categorie.",
    meta: "AI interoghează. Nu modifică. Nu decide. Numără pe categorii."
  },
  2: {
    label: "Prompt 02 · Semnalizare",
    text: "Construiește formulele care confruntă fiecare valoare cu nomenclatorul ei: COUNTIF pe lista de localități, XLOOKUP pe regulile de TVA, comparație între scadență și factură, NETWORKDAYS.INTL pe calendarul de sărbători. Scrie câte un flag pe fiecare regulă, apoi status_validare cu OK sau DE INVESTIGAT și motiv_anomalie cu textul exact. Nu modifica nicio valoare sursă. Vreau să reaplic același aparat pe alt set luna viitoare.",
    meta: "Formulele construiesc semnalizarea. Flag, status și motiv pe fiecare rând. Reaplicabil."
  }
};'''

FRAGS = [
    ('Aparența curățeniei. Astăzi am descoperit de ce era doar aparență.',
     'Aparența validității. Astăzi am descoperit de ce era doar aparență.'),
    ('Nu am șters anomalii. Le-am marcat cu motivul exact.',
     'Nu am modificat valori. Le-am confruntat cu realitatea.'),
    ('O marcare aplicată nu este o marcare confirmată. COUNTIF și SUMIF decid.',
     'O semnalare scrisă nu e o semnalare confirmată. COUNTIF decide.'),
    ('Un set marcat azi nu marchează singur setul de luna viitoare. Decât dacă regulile rămân conectate.',
     'Un set confruntat azi nu se confruntă singur luna viitoare. Decât dacă formulele rămân ancorate.'),
    ('Datele păreau curate. De data asta, le-am dovedit pe fiecare cu motivul ei.',
     'Valorile păreau valide. De data asta, le-am confruntat pe fiecare cu realitatea.'),
    ('Tabelul pare curat', 'Tabelul pare valid'),
    ('Marcare controlată', 'Construirea semnalizării'),
    ('Cross-check numeric', 'Verificarea corespondenței'),
    ('Reguli reaplicabile', 'Ancorare la sursă'),
    ('Tabelul cu date pare curat.', 'Setul de date pare valid.'),
    ('Datele însă mint.', 'Dar valid nu înseamnă corect.'),
    ('Raportul nu mai înghite minciuna. O marchează.',
     'Excel acceptă orice valoare validă. Acum ai aparatul care întreabă dacă e și corectă.'),
    ('Am marcat ce e neconform cu motivul exact.',
     'Am semnalat fiecare neconcordanță cu motivul exact.'),
    ('după verificare.', 'după confruntarea cu realitatea.'),
    ('C02 · MARCARE · BROADCAST', 'C02 · CONTROL · BROADCAST'),
    ('C02 · Marcare', 'C02 · Control'),
]

for src, dst in FILES:
    sp = os.path.join(DIR, src)
    if not os.path.exists(sp):
        report.append(f"LIPSA: {src}"); continue
    report.append(f"\n=== {src} -> {dst} ===")
    h = open(sp, encoding='utf-8').read()
    h = h.replace('02-Marcare', '02-Control')
    # STAGES block
    m = re.search(r'const STAGES = \[.*?\n\];', h, re.S)
    if m: h = h[:m.start()] + NEW_STAGES + h[m.end():]
    else: report.append("  ! STAGES negasit")
    # PROMPTS block
    m = re.search(r'PROMPTS = \{.*?\n\};', h, re.S)
    if m: h = h[:m.start()] + NEW_PROMPTS + h[m.end():]
    else: report.append("  ! PROMPTS negasit")
    # frags
    for old, new in FRAGS:
        if old in h: h = h.replace(old, new)
        else: report.append(f"  ! frag negasit: {old[:45]}")
    open(os.path.join(DIR, dst), 'w', encoding='utf-8').write(h)
    left = []
    for t in ['Marcare','MARCARE','marchează','week-end','duplicat','cod client','SUMIF','EXCLUS','Power Query','suma fizică','suma martor','câmp obligatoriu','în viitor']:
        c = len(re.findall(t, h))
        if c: left.append(f"{t}={c}")
    report.append("  leftover: " + (", ".join(left) if left else "ZERO"))

print("\n".join(report))
