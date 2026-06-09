# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV_C16_GENERARE_FAZA_2

## CONTEXT
C16 = LIVRAREA
T4 = RAPORTARE
CUVANT LOCKED = LIVRARE
VERB LOCKED = LIVREZ

## STATUS CURENT
C16 = GENERARE_IN_PROGRES.
Date_MASTER-C16.xlsx este generat si validat.
1/5 livrabile gate sunt gata.
Raman 4 HTML + documentele FILM/STUDIU/VIDEO + gate final.

## DECIZIE BRAIN
BRAIN accepta alinierea la gate:
- foloseste forma de fisier derivata din gate: Livrare
- NU cere schimbare SYSTEM catre Livrarea
- NU schimba nume_slug

## MANDAT C16-GENERARE-FAZA-2

Claude C16, la urmatorul sync:

1. Continua generarea C16 de unde ai ramas.

2. Pastreaza artefactele deja generate:
   - c16/Date_MASTER-C16.xlsx
   - c16/build_date_master_c16.py

3. Genereaza artefactele gate cu forma acceptata de BRAIN: Livrare
   - c16/HTML-Studiu-Excel-16-Livrare.html
   - c16/HTML-Editor-Studiu-Excel-16-Livrare.html
   - c16/HTML-Video-Excel-16-Livrare.html
   - c16/HTML-Editor-Video-Excel-16-Livrare.html

4. Genereaza si documentele cerute de mandat, aliniate la standardul repo:
   - FILM / STUDIU / VIDEO pentru C16
   - foloseste formatul standard deja folosit in constructiile T4 precedente
   - daca standardul real este .docx pentru FILM, foloseste standardul repo, nu presupunerea .md din mandatul anterior

5. Respecta obligatoriu:
   - C16 = foaie-raport de decizie
   - C16 nu sintetizeaza, C15 face asta
   - C16 nu face layout vizual general, C14 face asta
   - C16 nu creeaza sistem recurent, C17 face asta
   - C16 nu este logistica, nu email/export/PDF/share/trimitere
   - C16 livreaza raportul ca obiect decision-ready
   - hero descriptor: "DECIZIA GATA"
   - final-label ancora: "Un raport care nu produce o decizie nu e livrat, e doar trimis."

6. Respecta SPEC_NARATIV_MA_REVIZUIT:
   - 18 step-titles
   - 2 prompturi Copilot
   - 8 final-labels
   - fenomene / operatii mapate pe asset
   - granitele vs C12, C14, C15, C17

7. Respecta dependenta de pipeline:
   - C16 se va re-chainui dupa C15 cand C15 va fi generat
   - pana atunci pastreaza nota C15-GAP ca dependenta de pipeline, nu ca blocaj C16
   - nu inventa date numerice in HTML/FILM
   - cifrele business raman in Excel

8. Ruleaza validarile relevante:
   - pre_generation_check 16
   - gate_v20 16 c16 c01
   - audit_sync, daca este standard in flux

9. Nu modifica:
   - alte constructii cNN/**
   - fisiere sistem
   - nomenclatura locked
   - continutul conceptual aprobat

10. Daca apare blocaj SYSTEM, scrie CERERE SYSTEM in _brain/c16/CLAUDE-TO-BRAIN.md si opreste executia.

## RAPORT FINAL
Scrie raportul in _brain/c16/CLAUDE-TO-BRAIN.md cu:
- status final
- artefacte generate
- validari rulate
- rezultat validari
- commit
- blocaje ramase, daca exista

## REZULTAT ASTEPTAT
C16_GENERAT si gate_v20 16 c16 c01 = B2 PASS real, cu toate livrabilele gate prezente.
