# BRAIN -> CLAUDE C18

## STATUS
C18_GATE_DIAGNOSTIC_CERUT

## CONTEXT
C18 AUTOMATIZAREA. T5 AUTONOMIE. CUVANT MOTOR. VERB AUTOMATIZEZ.

C18 este conceptual inchis, P2 reparat si CONTROL_FINAL reparat.

RELEASE ramane NU.

P0 ramas pentru acest mandat:
- B2 gate este neverificabil, deoarece gate_v20.py pare hardcodat C01-C17 si nu cunoaste C18.

## OBIECTIV
Fa diagnostic complet pentru problema B2 gate C18 si propune solutia corecta de sistem.

## LIMITA STRICTA
Nu modifica gate_v20.py.
Nu modifica fisiere _system.
Nu modifica artefacte C18.
Nu declara B2 PASS daca nu ruleaza real.
Nu declara release.

Acest mandat este doar diagnostic + propunere SYSTEM.

## VERIFICARI OBLIGATORII
Verifica explicit:
1. de ce gate_v20.py nu poate valida C18;
2. daca problema este doar lipsa C18 din dict hardcodat;
3. ce identitati cunoaste gate_v20.py acum;
4. ce date C18 ar trebui introduse ca gate-ul sa poata valida C18;
5. daca exista intrari C18 in _system/SISTEM_TRAINITY-versiuni.md;
6. daca exista intrari C18 in _system/referinte/IDENTITATE-TEHNICA.md;
7. daca pre_generation_check 18 ramane PASS;
8. daca audit_sync ramane PASS mai putin imgclone;
9. daca adaugarea C18 in gate ar afecta C01-C17;
10. daca exista risc de contaminare sistem printr-un patch rapid;
11. daca solutia corecta este patch punctual C18 sau parser de productie;
12. ce mandat trebuie dat chatului SYSTEM pentru reparatia reala.

## FORMAT RAPORT
Scrie raport in _brain/c18/CLAUDE-TO-BRAIN.md cu:
1. verdict scurt;
2. cauza exacta pentru B2 neverificabil;
3. fisiere citite;
4. status intrari C18 in sistem;
5. solutia minima sigura;
6. solutia structurala recomandata;
7. riscuri;
8. prompt complet pentru CHAT SYSTEM, daca este nevoie;
9. verdict: RELEASE = NU pana cand B2 ruleaza real si trece.

## IMPORTANT
Daca este necesara modificare in gate_v20.py sau _system, formuleaza doar CERERE SYSTEM.
Nu executa tu modificarea.

## RAPORT
Scrie diagnosticul complet in _brain/c18/CLAUDE-TO-BRAIN.md.
