# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV_C16_MA_AUTORARE

## CONTEXT
C16 = LIVRAREA
T4 = RAPORTARE
CUVANT LOCKED = LIVRARE
VERB LOCKED = LIVREZ

## STATUS CURENT
C16 = FREEZE_B1_DONE.
B2_PREP_RAPORTAT executat.
Blocaj principal spre generare = M-A autorare SPEC narativ.

## MANDAT C16-MA-AUTORARE

Claude C16, la urmatorul sync:

1. Citeste strict:
   - _brain/c16/CHAT-CONTEXT.md
   - _brain/c16/BRAIN-TO-CLAUDE.md
   - _brain/c16/CLAUDE-TO-BRAIN.md

2. Autorare M-A pentru C16, fara implementare de artefacte.

3. Construieste SPEC narativ complet pentru C16 pe baza SEED-ului 11-slot aprobat si a identitatii LOCKED.

4. Include obligatoriu:
   - 18 step-titles, structurate 6 etape x 3 pasi
   - 2 prompturi Copilot
   - 8 final-labels
   - fenomene mapate pe asset
   - delimitari explicite vs C14, C15, C17

5. Pastreaza identitatea C16:
   - C16 nu sintetizeaza mesajul, C15 face asta
   - C16 nu face layout vizual general, C14 face asta
   - C16 nu creeaza sistem recurent sau automatizare, C17 face asta
   - C16 livreaza raportul ca foaie-raport de decizie

6. Nu implementa artefacte.
7. Nu modifica c16/**.
8. Nu modifica fisiere sistem.
9. Nu modifica alte constructii.
10. Daca apare nevoie de SYSTEM, scrie CERERE SYSTEM si opreste executia.

## RAPORT
Scrie raportul in _brain/c16/CLAUDE-TO-BRAIN.md.
