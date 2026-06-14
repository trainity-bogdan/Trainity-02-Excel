# BRAIN -> CLAUDE C19

## STATUS
GO_GENERARE_EFECTIVA_C19

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

Status real după ultimul sync:

`C19_B1_DEBLOCAT_READY_TO_GENERATE`

B1 este raportat deblocat. Generarea efectivă NU a început încă.

Acesta este GO explicit pentru generarea efectivă C19.

## RIDICARE EXPLICITĂ INTERDICȚII OPERAȚIONALE

Pentru acest mandat, ridic explicit interdicțiile necesare generării C19.

AI VOIE să creezi / modifici:

- folder `c19/`
- fișiere HTML C19
- `Date_MASTER-C19.xlsx`
- FILM C19
- build / scripturi locale necesare C19, doar în limita modelului existent
- `c19/assets/**`
- `_brain/c19/CLAUDE-TO-BRAIN.md`

NU AI VOIE să modifici:

- fișiere sistem (`CLAUDE.md`, `README.md`, `STARE-CURENTA.md`, `index.html`, `_system/**`, `governance/**`, `constructii.xlsx`, `gate_v20.py`, `audit_sync.py`, `COMENZI.yaml`)
- alte construcții `cNN/**`
- alte foldere `_brain/cYY/**`

## MANDAT

Generează efectiv C19 GUVERNAREA complet, pe baza SPEC frozen, Blueprint acceptat și B1 deblocat.

Nu mai face doar readiness.
Nu mai face doar freeze de registru.
Nu mai cere GO.
Acesta este GO.

### 1. Sursă COPY+MODIFY

Folosește sursa COPY+MODIFY conform regulilor curente ale repo-ului:

- preferat: `c01/`, dacă acesta este modelul canonic curent
- dacă există pattern build-script mai potrivit pentru construcțiile recente, raportează exact ce ai folosit și de ce

Nu inventa structură nouă dacă există model canonic.

### 2. Cele 7 artefacte canonice

Generează împreună cele 7 artefacte canonice C19:

1. HTML-Studiu C19
2. HTML-Editor-Studiu C19
3. HTML-Video C19
4. HTML-Editor-Video C19
5. `Date_MASTER-C19.xlsx`
6. FILM C19
7. `assets/` C19, hero + 6 exec-stage

Dacă imaginile finale originale GUVERNARE lipsesc, ai voie să folosești fallback DRAFT.

Obligație:
- marchează explicit `DRAFT_IMAGINI_FALLBACK` dacă imaginile sunt fallback / placeholder / clone
- NU declara release complet dacă imaginile sunt fallback / placeholder / clone / lipsesc
- declară release complet doar dacă imaginile sunt finale și hash diferit de c01

### 3. Identitate C19 obligatorie

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
- Artefact: `_GUVERNARE`
- STEP 5: `Excepția și oprirea controlată`

### 4. Blueprint obligatoriu

Construiește C19 pe cele 6 etape acceptate:

1. `Sistemul care merge doar cât te uiți`
2. `Ce poate să devieze previzibil`
3. `Regula care prinde intrarea greșită`
4. `Pragul și semnalul`
5. `Excepția și oprirea controlată`
6. `Testul ochilor închiși`

Arcul Excel obligatoriu:

input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

### 5. Excel / Date_MASTER obligatoriu

`Date_MASTER-C19.xlsx` trebuie să includă explicit:

- `_GUVERNARE` distinct de `_AUTOMATIZARE`
- `STATUS` OK / ATENȚIE / OPRIT
- Data Validation la sursă
- praguri vii (`LIMIT_MIN`, `LIMIT_MAX` sau echivalent)
- listă de excepții
- fail-safe automat
- output legat de `STATUS=OPRIT`, astfel încât rezultatul corupt să nu curgă mai departe
- conservarea sumei față de C18 conform R-V02.14, verificată explicit la generare

### 6. Gărzi conceptuale obligatorii

Păstrează în toate artefactele:

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

### 7. Validări obligatorii

Rulează și raportează:

- `pre_generation_check.py 19`
- `gate_v20.py 19 ...` pe artefactele canonice
- `audit_sync.py`
- verificare zero em dash / en dash
- verificare `_GUVERNARE` distinct de `_AUTOMATIZARE`
- verificare `STATUS` OK / ATENȚIE / OPRIT
- verificare Data Validation
- verificare fail-safe
- verificare R-V02.14 suma conservată
- verificare imagini: hash diferit de c01, dacă există imagini finale

Dacă o validare nu poate fi rulată, marchează explicit NU_RULAT și motivul. Nu declara PASS pentru ce nu ai rulat.

### 8. Raport

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## ARTEFACTE GENERATE

## SURSA COPY+MODIFY

## IDENTITATE C19 IMPLEMENTATĂ

## DATE_MASTER / _GUVERNARE

## VALIDĂRI RULATE

## VALIDĂRI NERULATE / PROBLEME

## STATUS IMAGINI

## STATUS RELEASE

## RISCURI RĂMASE

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după generare și raport.

## RAPORT
Aștept raportul de generare efectivă C19 în _brain/c19/CLAUDE-TO-BRAIN.md.
