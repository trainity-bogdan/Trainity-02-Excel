# BRAIN → CLAUDE · C13 VIZUALIZAREA

## STATUS
BRAIN_C13_REAUTHORIZE_GENERATION_AFTER_SYSTEM_READY

## MANDAT-ID
C13-GENERATE-AFTER-SYSTEM-READY-009

## RAPORT CLAUDE ANALIZAT
BRAIN a citit addendumul SYSTEM din `_brain/c13/CLAUDE-TO-BRAIN.md`.

Status relevant:
`SYSTEM_C13_PRE_GENERATION_READY`

## VERDICT BRAIN
PASS.

Gate-ul B1 de pre-generare este deblocat. C13 poate reintra în generare.

## STARE C13
- SPEC C13 = FROZEN
- Blueprint C13 = APPROVED
- Tensiune dashboard = RESOLVED
- Registru SYSTEM = READY
- Pre-generation check = EXIT 0
- ARHITECT a confirmat deja: `confirm generate C13`

## DECIZIE BRAIN
Claude C13 este autorizat să genereze artefactele C13.

## REGULĂ CRITICĂ
C13 = obiect vizual onest.
C14 = compunerea paginii / dashboard-ului.

C13 nu generează dashboard final, layout final, pagină finală sau mesaj C15.
Workbook-ul C13 este suport pentru construirea și verificarea obiectului vizual onest.

## SPEC LOCKED
Intriga: "Cifra e corectă. Graficul minte."
Miza: "O decizie este luată cu încredere pe o imagine falsă construită peste date corecte."
Mantra: "Nu desenez frumos. Desenez adevărat."
AHA: "Forma greșită minte cu cifra corectă."
WOW: "Aceeași cifră, două grafice, două concluzii opuse. Apoi forma onestă repară percepția."
Motto: "Forma nu se nimerește. Se alege."

## STEP-TITLES LOCKED
1. Răspunsul corect, dar invizibil
2. Nimeni nu decide privind un model
3. Aceeași cifră, încă fără formă
4. O cifră, mai multe forme posibile
5. Promptul 1: ce formă cere rezultatul
6. Aceeași cifră, două grafice, două concluzii
7. Tipul de grafic urmează natura rezultatului
8. Promptul 2: generezi vizualul, corectezi axa și scala
9. Scoți codarea care sugerează fals
10. Vizualul față de cifra brută: aceeași concluzie?
11. Testul celui de-al doilea ochi
12. Marchezi forma care spune mai mult decât cifra
13. Cele șase reguli de onestitate a formei
14. Eticheta, unitatea, contextul: nimic de ghicit
15. Un obiect vizual onest, repetabil
16. Forma onestă repară percepția
17. Devii garantul a ceea ce vede altcineva
18. Predai către C14: obiectul, gata de așezat în pagină

## LIVRABILE CERUTE
Generează în `c13/`:
1. `HTML-Studiu-Excel-13-Vizualizare.html`
2. `HTML-Editor-Studiu-Excel-13-Vizualizare.html`
3. `HTML-Video-Excel-13-Vizualizare.html`
4. `HTML-Editor-Video-Excel-13-Vizualizare.html`
5. `Date_MASTER-C13-Vizualizare.xlsx`
6. `FILM-Excel-13-Vizualizare.docx`
7. `assets/`, dacă patternul construcțiilor anterioare o cere.

## VALIDĂRI
Rulează validările disponibile pentru C13, inclusiv:
- pre_generation_check.py 13
- existența fizică a livrabilelor
- sincronizare Studiu / Editor-Studiu
- sincronizare Video / Editor-Video
- verificare că nu există dashboard final în C13
- verificare că cele 18 step-titles sunt respectate
- verificare că nu există modificări în afara scope-ului

## FIȘIERE PERMISE
- `c13/**`
- `_brain/c13/CLAUDE-TO-BRAIN.md`

## FIȘIERE INTERZISE
- fișiere sistem
- alte construcții
- alte foldere `_brain/cXX`
- fișiere globale repo

## RAPORT FINAL
Scrie în `_brain/c13/CLAUDE-TO-BRAIN.md`:
1. STATUS
2. livrabile generate
3. fișiere modificate
4. validări rulate
5. rezultate validări
6. cum ai păstrat C13 ca obiect vizual onest, nu dashboard
7. commit SHA
8. verdict final

## STATUS AȘTEPTAT
`CLAUDE_C13_GENERATED_READY_FOR_BRAIN_AUDIT`

Dacă apare blocaj:
`CLAUDE_C13_GENERATION_BLOCKED`

## CERERE DIRECTĂ
Generează C13 complet, controlat, conform SPEC-ului înghețat, blueprint-ului aprobat și înregistrării SYSTEM. Fără modificări sistem.