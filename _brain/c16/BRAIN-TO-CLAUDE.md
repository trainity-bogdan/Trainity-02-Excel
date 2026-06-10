# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV_C16_GENERARE_FINALA

## CONTEXT
C16 = LIVRAREA
T4 = RAPORTARE
CUVANT LOCKED = LIVRARE
VERB LOCKED = LIVREZ

## STATUS CURENT
C16 = GENERARE_IN_PROGRES.
3/5 livrabile gate sunt generate si trec gate:
- c16/Date_MASTER-C16.xlsx
- c16/HTML-Studiu-Excel-16-Livrare.html
- c16/HTML-Editor-Studiu-Excel-16-Livrare.html

Raman:
- c16/HTML-Video-Excel-16-Livrare.html
- c16/HTML-Editor-Video-Excel-16-Livrare.html
- documentele FILM / STUDIU / VIDEO conform standardului repo
- gate final cu toate livrabilele

## DECIZIE BRAIN
BRAIN confirma:
- continua fara redeschidere conceptuala
- alinierea la gate ramane: Livrare
- NU se cere schimbare SYSTEM catre Livrarea
- C15-GAP ramane dependenta de pipeline, nu blocaj C16

## MANDAT C16-GENERARE-FINALA

Claude C16, la urmatorul sync:

1. Continua generarea C16 din punctul curent si inchide faza finala.

2. Pastreaza artefactele deja generate si validate.

3. Genereaza artefactele ramase:
   - c16/HTML-Video-Excel-16-Livrare.html
   - c16/HTML-Editor-Video-Excel-16-Livrare.html
   - documentele FILM / STUDIU / VIDEO pentru C16, in formatul standard real al repo-ului

4. Respecta obligatoriu:
   - C16 = foaie-raport de decizie
   - C16 nu sintetizeaza, C15 face asta
   - C16 nu face layout vizual general, C14 face asta
   - C16 nu creeaza sistem recurent, C17 face asta
   - C16 nu este logistica, nu email/export/PDF/share/trimitere
   - C16 livreaza raportul ca obiect decision-ready
   - hero descriptor: "DECIZIA GATA"
   - final-label ancora: "Un raport care nu produce o decizie nu e livrat, e doar trimis."

5. Respecta SPEC_NARATIV_MA_REVIZUIT:
   - 18 step-titles
   - 2 prompturi Copilot
   - 8 final-labels
   - fenomene / operatii mapate pe asset
   - granitele vs C12, C14, C15, C17

6. Respecta regulile de date:
   - nu inventa date numerice in HTML/FILM
   - cifrele business raman in Excel
   - C15-GAP se pastreaza doar ca nota de pipeline

7. Ruleaza validarile finale:
   - pre_generation_check 16
   - gate_v20 16 c16 c01
   - audit_sync, daca este standard in flux

8. Nu modifica:
   - alte constructii cNN/**
   - fisiere sistem
   - nomenclatura locked
   - continutul conceptual aprobat

9. Daca apare blocaj SYSTEM real, scrie CERERE SYSTEM in _brain/c16/CLAUDE-TO-BRAIN.md si opreste executia.

## RAPORT FINAL
Scrie raportul in _brain/c16/CLAUDE-TO-BRAIN.md cu:
- status final
- artefacte generate
- validari rulate
- rezultat validari
- commit
- blocaje ramase, daca exista

## REZULTAT ASTEPTAT
C16_GENERAT_COMPLET si gate_v20 16 c16 c01 = B2 PASS real, cu toate livrabilele gate prezente.
