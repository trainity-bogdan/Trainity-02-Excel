# BRAIN → CLAUDE · C12 INTERPRETARE

## STATUS
MANDAT_AUDIT_T3_COMPLET

## CONTEXT CHAT
Acest fișier este folosit de Chat Claude C12 pentru audit transversal T3.

La comanda `sync`, citește:
- `_brain/c12/CHAT-CONTEXT.md`
- `_brain/c12/BRAIN-TO-CLAUDE.md`

Execută pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ T3
Treapta T3 ANALIZA include:
- C09 = RELAȚII, întrebarea „Ce pot întreba?”
- C10 = MĂSURI, întrebarea „Cât?”
- C11 = COMPARAȚII, întrebarea „Care?”
- C12 = INTERPRETARE, întrebarea „De ce?”

Lanțul conceptual T3 este:
model -> măsură -> clasament -> explicație

C12 închide T3.

## MANDAT T3-01 · AUDIT TRANSVERSAL COMPLET C09-C12

Claude, fă audit complet pe toată treapta T3, adică C09, C10, C11, C12.

Scop: verificare transversală, nu reparații automate.
Nu modifica fișiere. Nu face patch-uri fără mandat separat.
Nu modifica Bible §T3.
Nu modifica index.html.

Rulează și raportează explicit:

1. Sincronizare repo
- `git fetch`
- `git pull` sau echivalent sigur pe main
- status clean/dirty înainte de audit

2. Artefacte pe fiecare construcție
Pentru fiecare dintre `c09`, `c10`, `c11`, `c12`, verifică existența:
- `Date_MASTER-Cxx.xlsx`
- `HTML-Studiu-Excel-xx-*.html`
- `HTML-Editor-Studiu-Excel-xx-*.html`
- `HTML-Video-Excel-xx-*.html`
- `HTML-Editor-Video-Excel-xx-*.html`
- `FILM-Excel-xx-*.docx`
- `assets/`

3. Checks sistem
Rulează:
- `python3 _system/generatoare/pre_generation_check.py 9`
- `python3 _system/generatoare/pre_generation_check.py 10`
- `python3 _system/generatoare/pre_generation_check.py 11`
- `python3 _system/generatoare/pre_generation_check.py 12`
- `python3 _system/generatoare/gate_v20.py 9 c09 c01`
- `python3 _system/generatoare/gate_v20.py 10 c10 c01`
- `python3 _system/generatoare/gate_v20.py 11 c11 c01`
- `python3 _system/generatoare/gate_v20.py 12 c12 c01`
- `python3 _system/generatoare/audit_sync.py`

4. Audit continuitate Date_MASTER
Verifică lanțul:
- C09 pornește corect din C08
- C10 pornește corect din C09
- C11 pornește corect din C10
- C12 pornește corect din C11

Pentru fiecare trecere raportează:
- foi păstrate
- foaie nouă adăugată
- sumă Vanzari conservată
- delta
- dacă există pierderi sau drift workbook

5. Audit conceptual T3
Verifică dacă fiecare construcție are identitate distinctă:
- C09 construiește model interogabil, nu măsuri
- C10 definește măsuri, nu clasamente
- C11 compară și produce/folosește clasamente, nu interpretează cauzal
- C12 explică de ce, nu re-ierarhizează și nu recomandă acțiuni

6. Audit granițe T3/T4/T5
Verifică pentru toate C09-C12:
- fără dashboard
- fără cockpit
- fără raportare vizuală T4
- fără what-if
- fără scenarii
- fără predicție
- fără recomandare de acțiune
- fără tranziție prematură spre T4/T5

7. Audit HTML + FILM transversal
Pentru toate HTML-urile și FILM-urile T3 verifică:
- identitatea corectă pe construcție
- hero corect pe construcție
- lipsă contaminare între C09/C10/C11/C12
- lipsă tokeni vechi sau abandonați
- zero cifre business în HTML/FILM conform R-V02.15
- zero em-dash/en-dash
- consistență între Studiu, Editor-Studiu, Video, Editor-Video, FILM

8. Audit pedagogic lanț T3
Verifică dacă experiența cursantului construiește progresiv:
- după C09 poate întreba modelul
- după C10 poate calcula controlat
- după C11 poate compara corect
- după C12 poate explica rezultatul

Raportează dacă există salturi, repetiții, redundanțe sau goluri pedagogice.

9. Audit assets T3
Pentru fiecare construcție raportează:
- existență `assets/`
- hero image prezentă/lipsă
- exec-stage images prezente/lipsă
- dacă lipsa imaginilor este singurul drift rămas

10. Verdict final T3
Dă verdict în 5 niveluri:
- TECHNICAL PASS/FAIL
- DATA CONTINUITY PASS/FAIL
- CONTENT PASS/FAIL
- PEDAGOGICAL PASS/FAIL
- RELEASE READINESS PASS/FAIL

La final listează:
- Critical issues
- High issues
- Medium issues
- Low issues
- Recomandări de reparație, dar fără să le aplici
- Ce depinde de ARHITECT
- Ce poate fi reparat de Claude prin mandat separat

Scrie raportul în:
`_brain/c12/CLAUDE-TO-BRAIN.md`

Status așteptat:
`T3_AUDIT_COMPLET_DONE`
