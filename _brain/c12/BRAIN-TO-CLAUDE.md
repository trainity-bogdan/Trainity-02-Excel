# BRAIN → CLAUDE · T3 REPARAȚII POST-AUDIT

## STATUS
MANDAT_T3_REPARATII_POST_AUDIT

## CONTEXT
Acest mandat vine după auditul transversal T3 cu status:
`T3_AUDIT_COMPLET_DONE`

Auditul a confirmat:
- Technical: PASS
- Data Continuity: PASS
- Pedagogical: PASS
- Content: PASS cu o excepție
- Release Readiness: PASS cu rezerve

Treapta T3:
- C09 = RELAȚII, Ce pot întreba?
- C10 = MĂSURI, Cât?
- C11 = COMPARAȚII, Care?
- C12 = INTERPRETARE, De ce?

Lanț T3:
model -> măsură -> clasament -> explicație

## MANDAT T3-02 · REPARAȚII POST-AUDIT

Claude, lucrează pe main.

Fă doar reparațiile aprobate mai jos. Nu modifica altceva.
Nu modifica Bible §T3.
Nu modifica index.html.
Nu modifica HTML-urile C09-C12 dacă nu este necesar.
Nu modifica Date_MASTER.
Nu integra imaginile C12 acum, pentru că depind de ARHITECT.

### REPARAȚIA 1 · HIGH · C11 FILM R-V02.15

Auditul a găsit în:
`c11/FILM-Excel-11-Comparatii.docx`

problemă HIGH:
- conține suma business explicită `7.986.019,38 lei`
- apare și scrisă în litere
- încalcă R-V02.15, fără cifre business în FILM

Repară doar FILM-ul C11:
- elimină suma explicită
- elimină forma scrisă în litere a sumei
- înlocuiește cu formulări generice de tip:
  - „suma de control”
  - „valoarea totală verificată”
  - „totalul de control”
- păstrează sensul pedagogic
- nu introduce alte cifre business
- nu schimba identitatea C11

După reparare, verifică FILM C11 pentru:
- zero `lei`
- zero sumă explicită
- zero cifre business hardcodate
- zero em-dash/en-dash

### REPARAȚIA 2 · MEDIUM · C09 SPEC REGISTRY

Auditul a găsit:
`pre_generation_check.py 9` FAIL pentru că SPEC C09 este încă `NEGENERAT` în registrul de sistem.

C09 este livrat și `gate_v20.py 9 c09 c01` este PASS.
Trebuie doar sincronizare retroactivă de registru, ca la C10/C11/C12.

Ai mandat direct de sistem, limitat strict la C09, pentru:
- înscriere SPEC C09 ca INGHETAT în registrul de sistem
- înscriere sau completare IDENTITATE_TEHNICA C09 dacă lipsește sau este incompletă
- strict cât este necesar ca `pre_generation_check.py 9` să treacă

Nu schimba identitatea C09.
C09 rămâne:
- RELAȚII
- verb: a lega
- întrebare: Ce pot întreba?
- rol: model interogabil, relații corecte, activarea întrebărilor pe model

Folosește conținutul existent C09 din sistem și artefacte, nu inventa o identitate nouă.

### REPARAȚIA 3 · LOW · CHAT-CONTEXT C12

Actualizează cosmetic:
`_brain/c12/CHAT-CONTEXT.md`

Înlocuiește identitatea veche:
`KPI / FILTER CONTEXT`

cu identitatea corectă:
`INTERPRETARE`

Păstrează regulile utile ale chatului. Nu adăuga istoric inutil.

### VERIFICĂRI DUPĂ REPARAȚII

Rulează și raportează:
- `python3 _system/generatoare/pre_generation_check.py 9`
- `python3 _system/generatoare/pre_generation_check.py 10`
- `python3 _system/generatoare/pre_generation_check.py 11`
- `python3 _system/generatoare/pre_generation_check.py 12`
- `python3 _system/generatoare/gate_v20.py 9 c09 c01`
- `python3 _system/generatoare/gate_v20.py 10 c10 c01`
- `python3 _system/generatoare/gate_v20.py 11 c11 c01`
- `python3 _system/generatoare/gate_v20.py 12 c12 c01`
- `python3 _system/generatoare/audit_sync.py`

### RAPORT

Raportează:
- fișiere modificate exact
- ce ai reparat
- PASS/FAIL pentru fiecare verificare
- dacă H-1 este rezolvat
- dacă M-2 este rezolvat
- ce rămâne doar pe ARHITECT, adică imaginile C12

Scrie raportul în:
`_brain/c12/CLAUDE-TO-BRAIN.md`

Status așteptat:
`T3_REPARATII_POST_AUDIT_DONE`
