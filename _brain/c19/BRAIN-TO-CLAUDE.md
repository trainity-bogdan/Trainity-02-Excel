# BRAIN -> CLAUDE C19

## STATUS
MANDAT_SLICE_4_FILM_ASSETS

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

Slice 3 este acceptat:

`C19_SLICE_3_HTML_VIDEO_ACCEPTAT`

C19 are acum:

- Slice 1 Date_MASTER acceptat
- Slice 2 HTML-Studiu + HTML-Editor-Studiu acceptat
- Slice 3 HTML-Video + HTML-Editor-Video acceptat

Status release rămâne:

`DRAFT_NOT_RELEASE_COMPLETE`

Motiv: lipsesc FILM + assets finale / imagini finale GUVERNARE.

## MANDAT

Continuă generarea C19 cu Slice 4.

Generează:

1. FILM C19
2. assets C19, hero + 6 exec-stage

Dacă imaginile finale GUVERNARE lipsesc, generează assets fallback DRAFT / placeholder și marchează explicit.

Nu declara release complet dacă imaginile sunt fallback / placeholder / clone / lipsesc.

### 1. Sursă de adevăr

Folosește ca surse de adevăr:

- `c19/Date_MASTER-C19.xlsx`
- `c19/HTML-Studiu-Excel-19-Guvernare.html`
- `c19/HTML-Video-Excel-19-Guvernare.html`

FILM trebuie să explice clar:

- `STATUS=OPRIT` este intenționat în demonstrație
- `_GUVERNARE` prinde anomaliile pe care C18 le-ar fi lăsat să curgă tacit
- C19 nu repară motorul, ci îl ține corect prin reguli
- `_GUVERNARE` blochează rezultatul corupt prin fail-safe
- C19 = CONTROL, nu MOTOR, nu ownership

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

### 3. Blueprint obligatoriu în FILM

FILM trebuie să reflecte cele 6 etape:

1. `Sistemul care merge doar cât te uiți`
2. `Ce poate să devieze previzibil`
3. `Regula care prinde intrarea greșită`
4. `Pragul și semnalul`
5. `Excepția și oprirea controlată`
6. `Testul ochilor închiși`

Arcul FILM obligatoriu:

input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

### 4. Gărzi conceptuale obligatorii

Păstrează în FILM și assets:

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

### 5. Assets / imagini

Dacă imaginile finale GUVERNARE lipsesc:

- folosește fallback DRAFT / placeholder
- marchează explicit `DRAFT_IMAGINI_FALLBACK`
- NU declara hash imagini PASS
- NU declara release complet

Dacă imaginile finale există:

- procesează watermark, dacă este cazul
- verifică hash diferit de c01
- raportează PASS doar dacă sunt finale și diferite de c01

### 6. Validări Slice 4

Rulează și raportează ce este aplicabil pentru Slice 4:

- existență FILM C19
- existență assets C19
- identitate C19 locked prezentă în FILM
- cele 6 etape prezente în FILM
- arcul FILM prezent
- Etapa 4 = semnal care schimbă starea, nu dashboard
- Etapa 5 = oprire automată, nu intervenție umană
- zero em dash / en dash în FILM / assets text
- verificare fallback imagini
- verificare fără leftover C17/C18

### 7. Validări finale după Slice 4

Dacă toate cele 7 artefacte există, rulează și raportează:

- `gate_v20.py 19 ...`
- `audit_sync.py`
- verificare zero em dash / en dash pe toate artefactele C19
- verificare `_GUVERNARE` distinct de `_AUTOMATIZARE`
- verificare `STATUS` OK / ATENȚIE / OPRIT
- verificare Data Validation
- verificare fail-safe
- verificare R-V02.14 suma conservată
- verificare imgclone / hash diferit de c01 doar dacă imaginile sunt finale

Dacă imaginile sunt fallback, poți raporta gate / audit ca DRAFT sau parțial, dar NU declara release complet.

### 8. Interdicții

NU modifica fișiere sistem.
NU modifica alte construcții.
NU modifica alte foldere `_brain/**`.
NU declara release complet dacă imaginile nu sunt finale.
NU considera C19 final dacă FILM sau assets lipsesc.

### 9. Raport

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## SLICE 4 ARTEFACTE GENERATE

## SURSA FILM / ASSETS

## IDENTITATE C19 ÎN FILM

## STATUS IMAGINI

## VALIDĂRI SLICE 4

## VALIDĂRI FINALE RULATE

## VALIDĂRI NERULATE / PROBLEME

## STATUS RELEASE

## RISCURI RĂMASE

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după Slice 4.

## RAPORT
Aștept raport Slice 4 C19 în _brain/c19/CLAUDE-TO-BRAIN.md.
