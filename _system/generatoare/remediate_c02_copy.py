#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remedieri de COPY C02 (decizie ARHITECT). Doar text, zero structura/arhitectura."""
import re, os, docx

HTML = ['HTML-Studiu-Excel-02-Control.html','HTML-Editor-Studiu-Excel-02-Control.html',
        'HTML-Video-Excel-02-Control.html','HTML-Editor-Video-Excel-02-Control.html']
DIR = 'c02'
rep = []

# (old, new, eticheta) - aplicate global pe fiecare fisier daca exista
COMMON = [
    # H1 (cover-title) - Studiu/Editor-Studiu
    ('Cum pui sub control corespondența datelor cu realitatea',
     'Valid pentru Excel. Greșit pentru realitate.', 'H1'),
    # Mantra (cu <mark>)
    ('Nu credem valorile. Le confruntăm cu <mark>realitatea</mark>.',
     'Nu luăm valorile de bune. Le confruntăm cu <mark>realitatea</mark>.', 'MANTRA'),
    # Competenta (tu-statement-sm)
    ('Identifici și marchezi în câteva minute fiecare rând care denaturează un raport, fără să distrugi datele originale.',
     'Separi ce e valid de ce e corect, în câteva minute.', 'COMPETENTA'),
    # WOW (data-wow) - toate 4
    ('Excel acceptă orice valoare validă. Acum ai aparatul care întreabă dacă e și corectă.',
     'Excel acceptă orice. De acum, tu nu.', 'WOW'),
    # Regula oficiala introdusa explicit, in slotul existent cover-miza (fara element nou)
    ('Valorile valide pot fi greșite față de realitate. C02 le confruntă cu nomenclatoare, reguli și calendare, semnalează fiecare neconcordanță cu motivul ei și nu modifică nicio valoare sursă.',
     'Excel acceptă valoarea. Business-ul o investighează. Valorile valide pot fi greșite față de realitate: C02 le confruntă cu nomenclatoare, reguli și calendare, semnalează fiecare neconcordanță cu motivul ei și nu modifică nicio valoare sursă.', 'REGULA'),
]

for f in HTML:
    p = os.path.join(DIR, f)
    h = open(p, encoding='utf-8').read()
    hits = []
    for old, new, lbl in COMMON:
        c = h.count(old)
        if c:
            h = h.replace(old, new); hits.append(f"{lbl}x{c}")
    open(p, 'w', encoding='utf-8').write(h)
    rep.append(f"{f}: " + (", ".join(hits) if hits else "—"))

# FILM: mantra (para 9) + WOW (para 11)
fp = os.path.join(DIR, 'FILM-Excel-02-Control.docx')
d = docx.Document(fp)
def setp(p, t):
    if p.runs:
        p.runs[0].text = t
        for r in p.runs[1:]: r.text = ''
    else: p.add_run(t)
fhits = []
for p in d.paragraphs:
    if p.text.strip() == 'Nu credem valorile. Le confruntăm cu realitatea.' or p.text.strip() == 'Nu luăm valorile de bune. Le confruntăm cu realitatea.':
        setp(p, 'Nu luăm valorile de bune. Le confruntăm cu realitatea.'); fhits.append('MANTRA')
    elif 'aparatul care întreabă' in p.text:
        setp(p, 'Excel acceptă orice. De acum, tu nu.'); fhits.append('WOW')
d.save(fp)
rep.append("FILM: " + (", ".join(fhits) if fhits else "—"))

print("\n".join(rep))
