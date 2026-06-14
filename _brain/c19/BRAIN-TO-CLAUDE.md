# BRAIN -> CLAUDE C19

## STATUS
MANDAT_SLICE_3_HTML_VIDEO

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

Slice 2 este acceptat:

`C19_SLICE_2_HTML_STUDIU_ACCEPTAT`

C19 are acum:

- Slice 1 Date_MASTER acceptat
- Slice 2 HTML-Studiu + HTML-Editor-Studiu acceptat

Status release rămâne:

`DRAFT_NOT_RELEASE_COMPLETE`

## MANDAT

Continuă generarea C19 cu Slice 3.

Generează:

1. HTML-Video C19
2. HTML-Editor-Video C19

Nu genera încă:

- FILM final
- release complet

### 1. Sursă de adevăr

Folosește `c19/Date_MASTER-C19.xlsx` și HTML-Studiu C19 ca surse de adevăr.

Video trebuie să explice clar:

- `STATUS=OPRIT` este intenționat în demonstrație
- `_GUVERNARE` prinde anomaliile pe care C18 le-ar fi lăsat să curgă tacit
- C19 nu repară motorul, ci îl ține corect prin reguli
- `_GUVERNARE` blochează rezultatul corupt prin fail-safe

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

### 3. Blueprint obligatoriu în Video

HTML-Video trebuie să reflecte cele 6 etape:

1. `Sistemul care merge doar cât te uiți`
2. `Ce poate să devieze previzibil`
3. `Regula care prinde intrarea greșită`
4. `Pragul și semnalul`
5. `Excepția și oprirea controlată`
6. `Testul ochilor închiși`

Arcul video obligatoriu:

input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

### 4. Gărzi conceptuale obligatorii

Păstrează în Video:

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

### 6. Validări Slice 3

Rulează și raportează ce este aplicabil pentru Slice 3:

- existență HTML-Video C19
- existență HTML-Editor-Video C19
- identitate C19 locked prezentă în Video
- cele 6 etape prezente
- arcul video prezent
- Etapa 4 = semnal care schimbă starea, nu dashboard
- Etapa 5 = oprire automată, nu intervenție umană
- zero em dash / en dash în Video
- verificare fallback imagini
- editor video fără leftover C17/C18

Nu rula `gate_v20.py 19` ca PASS complet dacă lipsesc artefacte. Dacă îl rulezi parțial sau nu îl rulezi, marchează explicit.

### 7. Interdicții

NU modifica fișiere sistem.
NU modifica alte construcții.
NU modifica alte foldere `_brain/**`.
NU declara release complet.
NU considera Slice 3 executat fără cele două HTML-uri video.

### 8. Raport

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## SLICE 3 ARTEFACTE GENERATE

## SURSA VIDEO

## IDENTITATE C19 ÎN VIDEO

## DATE_MASTER FOLOSIT

## STATUS IMAGINI

## VALIDĂRI SLICE 3

## VALIDĂRI NERULATE / PROBLEME

## STATUS RELEASE

## RISCURI RĂMASE

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după Slice 3.

## RAPORT
Aștept raport Slice 3 C19 în _brain/c19/CLAUDE-TO-BRAIN.md.
