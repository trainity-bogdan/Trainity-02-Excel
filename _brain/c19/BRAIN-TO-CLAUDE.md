# BRAIN -> CLAUDE C19

## STATUS
MANDAT_AUDIT_COMPLET_C19

## DECIZIE BRAIN

C19 este DRAFT complet, dar NU release complet.

Status curent acceptat:

- Date_MASTER = generat
- HTML-Studiu = generat
- HTML-Editor-Studiu = generat
- HTML-Video = generat
- HTML-Editor-Video = generat
- FILM = generat
- assets = generate DRAFT

C19 este acum:

`C19_DRAFT_COMPLET`

## MANDAT

Fă AUDIT COMPLET C19, fără să modifici artefacte.

Acesta este mandat de AUDIT și RAPORTARE, nu mandat de reparație.

NU modifica `c19/**`.
NU modifica Date_MASTER.
NU modifica HTML.
NU modifica FILM.
NU modifica assets.
NU modifica fișiere sistem.
NU modifica alte construcții.

Ai voie să modifici doar:

`_brain/c19/CLAUDE-TO-BRAIN.md`

## AUDIT OBLIGATORIU

Auditul trebuie să verifice exhaustiv:

### 1. Existența celor 7 artefacte canonice

Verifică existența și statusul pentru:

1. HTML-Studiu C19
2. HTML-Editor-Studiu C19
3. HTML-Video C19
4. HTML-Editor-Video C19
5. `Date_MASTER-C19.xlsx`
6. FILM C19
7. `assets/` C19, hero + 6 exec-stage

Marchează pentru fiecare:

- EXISTĂ / LIPSEȘTE
- valid / invalid
- final / draft
- observații

### 2. Audit conceptual C19

Verifică dacă toate artefactele păstrează identitatea:

- C19 = GUVERNAREA
- CUVÂNT LOCKED = CONTROL
- VERB LOCKED = GUVERNEZ
- rol T5 = scoate autorul din ATENȚIE
- axă = DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE

Verifică dacă sunt prezente și corecte:

- MIZA HERO: `GUVERNAREA SISTEMULUI PRIN REGULI`
- HERO: `Cum se ține corect fără ochiul meu?`
- BOMBĂ: `Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.`
- MANTRA: `Nu o supraveghez. O guvernez prin reguli.`
- WOW: `Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.`
- MOTTO: `Pleci, și munca se ține singură.`
- GREȘEALA: `Confunzi «merge» cu «merge corect».`
- AHA: `Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.`
- STEP 5: `Excepția și oprirea controlată`

### 3. Audit granițe / contaminare

Verifică explicit că C19 nu alunecă în:

- C18: motor / automatizare / execuție ca identitate
- C20: responsabil / owner / ownership / escaladare / delegare
- T4: dashboard decorativ / raportare vizuală pentru om
- C04: refresh / actualizare set de date
- QA generic / audit clasic / management
- babysitting / monitorizare zilnică / persoană care verifică

Regula de pază:

- C18 = rulează
- C19 = se ține corect
- C20 = predă responsabilitatea

### 4. Audit Blueprint / 6 etape / 18 pași

Verifică în HTML-Studiu, HTML-Video și FILM:

1. `Sistemul care merge doar cât te uiți`
2. `Ce poate să devieze previzibil`
3. `Regula care prinde intrarea greșită`
4. `Pragul și semnalul`
5. `Excepția și oprirea controlată`
6. `Testul ochilor închiși`

Verifică dacă arcul este prezent:

input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

Verifică dacă Etapa 4 este semnal care schimbă starea, nu dashboard.

Verifică dacă Etapa 5 este oprire automată, nu intervenție umană.

### 5. Audit Date_MASTER / `_GUVERNARE`

Verifică în `Date_MASTER-C19.xlsx`:

- `_GUVERNARE` există
- `_GUVERNARE` este distinctă de `_AUTOMATIZARE`
- `STATUS` OK / ATENȚIE / OPRIT există
- Data Validation există la sursă
- praguri vii există
- listă de excepții există
- fail-safe automat există
- output legat de `STATUS=OPRIT`
- `STATUS=OPRIT` este intenționat în demonstrație
- R-V02.14 suma conservată față de C18

### 6. Audit tehnic texte / HTML / FILM

Verifică:

- zero em dash / en dash
- zero leftover C17 / C18 / C01 nelegitim
- localStorage corect C19
- title / topbar corecte C19
- NEXT corect către C20 Delegarea
- Editor-Studiu body identic cu Studiu
- Editor-Video body / STAGES identice cu Video
- fără cifre business în HTML / FILM conform R-V02.15

### 7. Audit imagini / assets

Verifică:

- există 7 imagini în `c19/assets/`
- hero + exec-stage-1..6 există
- dimensiuni / validitate imagini
- status DRAFT / final
- dacă sunt placeholder, marchează `DRAFT_IMAGINI_FALLBACK`
- NU declara release complet dacă imaginile sunt placeholder
- NU declara hash PASS de release pentru imagini DRAFT

### 8. Validări automate

Rulează ce este permis fără modificări:

- `audit_sync.py`
- `gate_v20.py 19`, dacă SYSTEM l-a deblocat
- verificări proprii read-only pentru artefacte

Dacă `gate_v20.py 19` este încă blocat de SYSTEM, marchează:

`GATE_SYSTEM_BLOCKED`

Nu încerca să modifici `gate_v20.py`.

### 9. Clasificare severitate

Pentru fiecare problemă găsită, marchează severitatea:

- BLOCKER = blochează release
- MAJOR = trebuie reparat înainte de final
- MINOR = nu blochează, dar trebuie notat
- INFO = observație

### 10. Verdict final audit

Raportează unul dintre statusurile:

- `C19_RELEASE_READY`
- `C19_DRAFT_COMPLET_GATE_BLOCKED`
- `C19_DRAFT_COMPLET_IMAGES_BLOCKED`
- `C19_DRAFT_COMPLET_GATE_AND_IMAGES_BLOCKED`
- `C19_AUDIT_FAIL_BLOCKERS`

Nu declara `C19_RELEASE_READY` dacă:

- gate_v20 nu a trecut
- imaginile sunt DRAFT
- există BLOCKER conceptual / tehnic

## FORMAT RAPORT

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format obligatoriu:

# CLAUDE -> BRAIN C19

## STATUS

## ARTEFACTE AUDITATE

## AUDIT CONCEPTUAL

## AUDIT GRANIȚE / CONTAMINARE

## AUDIT BLUEPRINT / 6 ETAPE / ARC

## AUDIT DATE_MASTER / _GUVERNARE

## AUDIT TEHNIC HTML / FILM

## AUDIT IMAGINI / ASSETS

## VALIDĂRI RULATE

## VALIDĂRI NERULATE / BLOCAJE

## LISTĂ PROBLEME CU SEVERITATE

## VERDICT FINAL AUDIT

## CERERI CĂTRE BRAIN / SYSTEM / ARHITECT

## COMMIT

Fă commit descriptiv pe main după raport.

## RAPORT

Aștept audit complet C19 în `_brain/c19/CLAUDE-TO-BRAIN.md`.
