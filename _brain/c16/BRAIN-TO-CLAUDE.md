# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV_C16_MA_REVIZIE_MINORA

## CONTEXT
C16 = LIVRAREA
T4 = RAPORTARE
CUVANT LOCKED = LIVRARE
VERB LOCKED = LIVREZ

## STATUS CURENT
C16 = FREEZE_B1_DONE.
M-A autorare executat.
SPEC_NARATIV_PROPUS_MA este aprobat cu revizie minora.

## MANDAT C16-MA-REVIZIE-MINORA

Claude C16, la urmatorul sync:

1. Citeste strict:
   - _brain/c16/CHAT-CONTEXT.md
   - _brain/c16/BRAIN-TO-CLAUDE.md
   - _brain/c16/CLAUDE-TO-BRAIN.md

2. Aplica revizie minora pe SPEC narativ M-A.

3. Modifica Pasul 11:
   din: "Testul fara autor: zero intrebari de follow-up"
   in: "Testul fara autor: intrebarile inevitabile, nu intrebarile de baza"

4. Modifica Pasul 18:
   din: "Predai catre T5 (C17): raportul-decizie gata, urmeaza sa fie sistematizat"
   in: "Raportul-decizie este gata, T5 il poate sistematiza"

5. Pastreaza final-label 1 ca ancora centrala:
   "Un raport care nu produce o decizie nu e livrat, e doar trimis."

6. Nu implementa artefacte.
7. Nu modifica c16/**.
8. Nu modifica fisiere sistem.
9. Nu modifica alte constructii.
10. Daca apare nevoie de SYSTEM, scrie CERERE SYSTEM si opreste executia.

## RAPORT
Scrie raportul in _brain/c16/CLAUDE-TO-BRAIN.md.
