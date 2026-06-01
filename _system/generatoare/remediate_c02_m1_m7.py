#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remedieri C02 M1-M7 (decizie ARHITECT). Doar copy/terminologie/alt-text. Zero structura."""
import os, re

FILES = ['HTML-Studiu-Excel-02-Control.html', 'HTML-Editor-Studiu-Excel-02-Control.html']
DIR = 'c02'

REPL = [
    # M1 CRITIC - ts-pair 1 + ts-pair 3 (pair 2 ramane)
    ('<span class="ts-no">Nu mai ștergi ce te încurcă.</span><span class="ts-yes">Marchezi.</span>',
     '<span class="ts-no">Nu mai ștergi ce pare greșit.</span><span class="ts-yes">Semnalizezi cu dovada.</span>', 'M1a'),
    ('<span class="ts-no">Nu mai întrebi „sunt corecte?".</span><span class="ts-yes">Întrebi „ce trebuie verificat?".</span>',
     '<span class="ts-no">Nu mai întrebi „e valid?".</span><span class="ts-yes">Întrebi „e și corect?".</span>', 'M1c'),
    # M2 / M3 - etichete ba-item-indicator
    ('>Sumă fizică<', '>Valori sursă<', 'M2'),
    ('>Suma raport oficial<', '>Neconcordanțe semnalate<', 'M3'),
    # M4 - alt-text
    ('Pagina de raport cu o stampila galbena DE VERIFICAT apasata pe un rand anomal',
     'Pagina cu un rand semnalat DE INVESTIGAT, confruntat cu realitatea', 'M4'),
    # M5 - next-desc
    ('ce e cu adevărat curat', 'ce este tehnic curat', 'M5'),
    # M6 - lista ÎNAINTE
    ('rapoarte construite din date necontrolate', 'decizii construite pe valori neverificate', 'M6'),
    # M7 - outcomes
    ('încredere că valid = corect', 'încredere că validul a fost confruntat cu realitatea', 'M7'),
]

FORBIDDEN = ['valid = corect', 'Marchezi', 'sunt corecte?', 'Sumă fizică', 'Suma raport oficial',
             'DE VERIFICAT', 'rapoarte construite din date necontrolate', 'ce e cu adevărat curat']

print("=== APLICARE ===")
for f in FILES:
    p = os.path.join(DIR, f)
    h = open(p, encoding='utf-8').read()
    hits = []
    for old, new, lbl in REPL:
        c = h.count(old)
        if c:
            h = h.replace(old, new); hits.append(f"{lbl}x{c}")
        else:
            hits.append(f"{lbl}:LIPSA")
    open(p, 'w', encoding='utf-8').write(h)
    print(f"  {f}: {', '.join(hits)}")

print("\n=== AUDIT FINAL (fraze interzise) ===")
overall_ok = True
for f in FILES:
    h = open(os.path.join(DIR, f), encoding='utf-8').read()
    found = [t for t in FORBIDDEN if t in h]
    status = 'PASS - zero fraze interzise' if not found else 'FAIL: ' + ', '.join(found)
    if found: overall_ok = False
    print(f"  {f}: {status}")
print("\nREZULTAT:", "PASS" if overall_ok else "FAIL")
