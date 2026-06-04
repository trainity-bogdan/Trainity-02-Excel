# BRAIN → CLAUDE · C12 INTERPRETARE

## STATUS
MANDAT_AUDIT_MAMUT_C12

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C12.

La comanda `sync`, citește:
- `_brain/c12/CHAT-CONTEXT.md`
- `_brain/c12/BRAIN-TO-CLAUDE.md`

Execută pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C12
C12 este construcția INTERPRETARE.

Lanț T3:
- C09 = RELAȚII, Ce pot întreba?
- C10 = MĂSURI, Cât?
- C11 = COMPARAȚII, Care?
- C12 = INTERPRETARE, De ce?

C12 este generată cu status raportat anterior:
`C12_GENERATED · GATE_V20_PASS`

Rămâne cunoscută dependența de imagini ARHITECT:
`V39.assets` poate fi încă XX până la integrarea hero + exec-stage.

## MANDAT C12-06 · AUDIT MAMUT C12

Claude, fă audit mamut pe C12.

Scop: verificare exhaustivă, nu reparații automate.

Nu modifica fișierele C12 decât dacă auditul cere doar raportare. Nu face patch-uri fără mandat separat.
Nu modifica C09, C10, C11.
Nu modifica Bible §T3.
Nu modifica index.html.

Rulează și raportează explicit:

1. Sincronizare repo
- `git fetch`
- `git pull` sau echivalent sigur pe main
- status clean/dirty înainte de audit

2. Existență artefacte C12
Verifică în `c12/` existența:
- `Date_MASTER-C12.xlsx`
- `HTML-Studiu-Excel-12-Interpretare.html`
- `HTML-Editor-Studiu-Excel-12-Interpretare.html`
- `HTML-Video-Excel-12-Interpretare.html`
- `HTML-Editor-Video-Excel-12-Interpretare.html`
- `FILM-Excel-12-Interpretare.docx`
- `assets/`

3. Checks sistem
Rulează:
- `python3 _system/generatoare/pre_generation_check.py 12`
- `python3 _system/generatoare/gate_v20.py 12 c12 c01`
- `python3 _system/generatoare/audit_sync.py`

4. Audit workbook C12
Inspectează `Date_MASTER-C12.xlsx` și raportează:
- foi existente
- existența foii `Interpretare`
- continuitate față de C11
- sumă conservată
- delta față de C11
- dacă foaia Interpretare chiar susține C12: cauză citită din model, cauză multiplă, cauză ascunsă sub total, insight verificabil

5. Audit HTML conținut
Pentru toate cele 4 HTML-uri C12 verifică:
- identitate C12 = INTERPRETARE
- hero = DE CE-UL DIN DATE
- întrebare = De ce?
- mantra = Cifra spune cât. Explicația spune de ce.
- motto = Nu citi rezultatul. Explică-l.
- AHA = Nu rezultatul contează. Contează de ce apare rezultatul.
- fără tokeni vechi: KPI / FILTER CONTEXT, PRIORITIZARE EXECUTIVA, What-if, scenarii, dashboard, predicție, recomandare acțiune
- fără em-dash și en-dash
- fără cifre business în HTML/FILM, conform R-V02.15
- fără re-ierarhizare C11
- C12 explică, nu compară din nou

6. Audit T3/T4/T5 granițe
Verifică explicit că:
- C12 nu face dashboard
- C12 nu face raportare vizuală T4
- C12 nu face what-if
- C12 nu face scenarii
- C12 nu face predicție
- C12 nu recomandă acțiuni
- C12 închide T3 ANALIZA

7. Audit Video + FILM
Verifică:
- 6 etape video prezente
- 18 pași prezenți
- cele 7 slide-uri exec există sau sunt corect placeholder dacă imaginile lipsesc
- FILM este aliniat cu HTML-Video
- Video nu conține cifre business hardcodate

8. Audit assets
Raportează exact:
- ce există în `c12/assets/`
- ce lipsește
- dacă `V39.assets` este singura celulă XX în audit_sync
- dacă lipsa imaginilor este singurul drift rămas

9. Verdict final
Dă verdict în 4 niveluri:
- TECHNICAL PASS/FAIL
- CONTENT PASS/FAIL
- PEDAGOGICAL PASS/FAIL
- RELEASE READINESS PASS/FAIL

La final, listează:
- Critical issues
- High issues
- Medium issues
- Low issues
- Ce se poate repara imediat
- Ce necesită input ARHITECT

Scrie raportul în:
`_brain/c12/CLAUDE-TO-BRAIN.md`

Status așteptat:
`C12_AUDIT_MAMUT_DONE`
