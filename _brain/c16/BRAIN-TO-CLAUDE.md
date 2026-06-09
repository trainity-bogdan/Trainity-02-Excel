# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV_C16_GENERARE

## CONTEXT
C16 = LIVRAREA
T4 = RAPORTARE
CUVANT LOCKED = LIVRARE
VERB LOCKED = LIVREZ

## STATUS CURENT
C16 = READY_FOR_GENERATION FINAL.
SPEC_NARATIV_MA_REVIZUIT este aprobat si inghetat.
Hero descriptor "DECIZIA GATA" este BRAIN-CONFIRMED.
pre_generation_check 16 = 3/3 PASS.
B2 SYSTEM/gate = READY_FOR_GENERATION.

## MANDAT C16-GENERARE

Claude C16, la urmatorul sync:

1. Lucreaza exclusiv pe main, fara branch-uri.

2. Citeste strict:
   - _brain/c16/CHAT-CONTEXT.md
   - _brain/c16/BRAIN-TO-CLAUDE.md
   - _brain/c16/CLAUDE-TO-BRAIN.md
   - fisierele C16 permise si necesare pentru generare
   - sursele COPY+MODIFY din c01, doar cat este necesar pentru generarea C16

3. Genereaza C16 prin COPY+MODIFY din c01, conform standardului curent.

4. Artefacte cerute:
   - c16/HTML-Studiu-Excel-16-Livrarea.html
   - c16/HTML-Editor-Studiu-Excel-16-Livrarea.html
   - c16/HTML-Video-Excel-16-Livrarea.html
   - c16/HTML-Editor-Video-Excel-16-Livrarea.html
   - c16/FILM-Excel-16-Livrarea.md
   - c16/STUDIU-Excel-16-Livrarea.md
   - c16/VIDEO-Excel-16-Livrarea.md

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
   - input C16 = Date_MASTER-C15-Sintetizare.xlsx, daca exista in flux
   - nu inventa date numerice in HTML/FILM
   - cifrele business raman in Excel

8. Dupa generare ruleaza validarile relevante:
   - pre_generation_check 16
   - gate_v20 16 c16 c01
   - audit_sync, daca este standard in flux

9. Nu modifica:
   - alte constructii cNN/**
   - fisiere sistem, cu exceptia cazului in care validarea cere explicit si opreste pentru CERERE SYSTEM
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
C16_GENERAT si gate_v20 16 c16 c01 = B2 PASS.
