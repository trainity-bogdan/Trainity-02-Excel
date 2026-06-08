# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV_C16_002

## CONTEXT
C16 LIVRAREA. T4 RAPORTARE. CUVÂNT LIVRARE. VERB LIVREZ.

Identitate blocată:
- C16 = LIVRAREA
- T4 = RAPORTARE
- CUVÂNT LOCKED = LIVRARE
- VERB LOCKED = LIVREZ
- Rol în T4: transformarea raportului într-un material decision-ready, predabil decidentului
- Graniță în jos: C15 = mesajul esențial sintetizat
- Graniță în sus: C17 = sistematizarea raportului în T5 AUTONOMIE

## FEEDBACK BRAIN PE RAPORTUL ANTERIOR

SEED C16 este aprobat cu ajustări.
SPEC C16 încă nu este aprobat. Necesită rafinare în structura 11-slot confirmată.

Aprobări:
- definiția LIVRĂRII ca transformarea raportului într-un obiect de decizie
- anti-definiția logistică: LIVRAREA nu este email, export, PDF ca simplă formă tehnică, share, trimitere sau predare administrativă
- granițele C15/C16/C17
- miza: valoarea lanțului T1-T4 se realizează sau se pierde în momentul livrării
- mantra: "Nu livrez informație. Livrez o decizie gata de luat."
- motto: "Raportul care decide."
- slug: livrarea

Corecții obligatorii:
- C16 nu sintetizează concluzia, ci livrează mesajul sintetizat anterior de C15
- C16 nu face compunere vizuală generală, aceasta este granița C14
- C16 nu creează sistem recurent, dashboard viu, procedură autonomă sau automatizare, acestea aparțin C17/T5
- WOW-ul poate rămâne aspirațional, dar nu trebuie să pară promisiune operațională rigidă

## MANDAT C16-002

Claude C16, la următorul sync:

1. Citește strict:
   - _brain/c16/CHAT-CONTEXT.md
   - _brain/c16/BRAIN-TO-CLAUDE.md
   - _brain/c16/CLAUDE-TO-BRAIN.md

2. Rafinează SEED-ul C16 pe baza aprobărilor BRAIN.

3. Rescrie SPEC 11-slot C16 în ordinea confirmată:
   1. IDENTITATE
   2. SLUG
   3. INTRIGA
   4. PROBLEMELE
   5. MIZA
   6. MANTRA
   7. WOW
   8. MOTTO
   9. FENOMENE
   10. GRANIȚE
   11. STEP-TITLES

4. Fixează artefactul conceptual C16 ca:
   "foaie-raport de decizie", adică o pagină executivă decision-ready în Excel.

5. Ajustează STEP-TITLES astfel încât să nu pară C15 și nici C14:
   - nu "sintetizează concluzia"
   - nu "aranjează vizual"
   - ci "livrează cadrul final pentru decizie"

6. Propune o versiune finală de SPEC C16, gata pentru aprobare BRAIN.

7. Nu implementa artefacte.
8. Nu modifica c16/**.
9. Nu modifica fișiere sistem.
10. Nu modifica alte cNN/** sau alte _brain/cYY/**.

11. Scrie raportul exclusiv în:
   - _brain/c16/CLAUDE-TO-BRAIN.md

12. Dacă apare nevoie de sistem, scrie doar CERERE SYSTEM în _brain/c16/CLAUDE-TO-BRAIN.md și oprește execuția.

## RAPORT
Scrie raportul în _brain/c16/CLAUDE-TO-BRAIN.md.
