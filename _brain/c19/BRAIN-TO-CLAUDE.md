# BRAIN -> CLAUDE C19

## STATUS
EXECUTA_ACUM_SLICE_2_HTML_STUDIU

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

Ultimul sync a arătat că Slice 2 NU a fost executat. Raportul Claude a rămas pe Slice 1.

Status real:

`C19_SLICE_1_ACCEPTAT__SLICE_2_MANDATAT_NEEXECUTAT`

Acesta este ordin de execuție imediată pentru Slice 2.

Nu mai raporta Slice 1 ca rezultat principal.
Nu mai cere GO.
Nu mai face readiness.
Execută Slice 2.

## MANDAT

Generează acum:

1. HTML-Studiu C19
2. HTML-Editor-Studiu C19

Nu genera încă:

- HTML-Video
- HTML-Editor-Video
- FILM
- release complet

### 1. Sursă de adevăr

Folosește `c19/Date_MASTER-C19.xlsx` ca sursă de adevăr pentru demonstrația C19.

Trebuie explicat clar în HTML că:

- `STATUS=OPRIT` este intenționat în demonstrație
- `_GUVERNARE` prinde anomaliile pe care C18 le-ar fi lăsat să curgă tacit
- C19 nu repară motorul, ci îl ține corect prin reguli

### 2. Identitate locked

Păstrează locked:

- SLUG: `guvernare`
- MIZA HERO: `GUVERNAREA SISTEMULUI PRIN REGULI`
- HERO: `Cum se ține corect fără ochiul meu?`
- BOMBĂ: `Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.`
- MANTRA: `Nu o supraveghez. O guvernez prin reguli.`
- WOW: `Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.`
- MOTTO: `Pleci, și munca se ține singură.`
- GREȘEALA: `Confunzi «merge» cu «merge corect».`
- AHA: `Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.`
- STEP 5: `Excepția și oprirea controlată`

### 3. Blueprint obligatoriu în HTML-Studiu

HTML-Studiu trebuie să reflecte cele 6 etape:

1. `Sistemul care merge doar cât te uiți`
2. `Ce poate să devieze previzibil`
3. `Regula care prinde intrarea greșită`
4. `Pragul și semnalul`
5. `Excepția și oprirea controlată`
6. `Testul ochilor închiși`

Arcul obligatoriu:

input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

### 4. Gărzi conceptuale obligatorii

Păstrează în HTML:

- C18 = rulează
- C19 = se ține corect
- C20 = predă responsabilitatea

C19 NU este:

- management
- responsabil
- escaladare umană
- dashboard decorativ
- monitorizare zilnică
- QA generic
- audit clasic
- `motor` ca identitate C19
- ownership
- delegare
- persoană care verifică

Etapa 4 = semnal care schimbă starea, nu dashboard.
Etapa 5 = oprire automată, nu intervenție umană.

### 5. Imagini

Dacă imaginile finale GUVERNARE lipsesc, folosește fallback DRAFT.

Obligație:

- marchează explicit `DRAFT_IMAGINI_FALLBACK`
- NU declara release complet
- NU declara hash imagini PASS dacă imaginile sunt fallback / clone / placeholder

### 6. Validări Slice 2

Rulează și raportează ce este aplicabil pentru Slice 2:

- existență HTML-Studiu C19
- existență HTML-Editor-Studiu C19
- identitate C19 locked prezentă în HTML
- cele 6 etape prezente
- Etapa 4 = semnal care schimbă starea, nu dashboard
- Etapa 5 = oprire automată, nu intervenție umană
- zero em dash / en dash în HTML
- verificare imagini / fallback status

Nu rula `gate_v20.py 19` ca PASS complet dacă lipsesc artefacte. Dacă îl rulezi parțial sau nu îl rulezi, marchează explicit.

### 7. Interdicții

NU modifica fișiere sistem.
NU modifica alte construcții.
NU modifica alte foldere `_brain/**`.
NU declara release complet.
NU considera Slice 2 executat fără cele două HTML-uri.

### 8. Raport

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## SLICE 2 ARTEFACTE GENERATE

## SURSA HTML

## IDENTITATE C19 ÎN HTML

## DATE_MASTER FOLOSIT

## STATUS IMAGINI

## VALIDĂRI SLICE 2

## VALIDĂRI NERULATE / PROBLEME

## STATUS RELEASE

## RISCURI RĂMASE

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după Slice 2.

## RAPORT
Aștept raport Slice 2 C19 în _brain/c19/CLAUDE-TO-BRAIN.md.
