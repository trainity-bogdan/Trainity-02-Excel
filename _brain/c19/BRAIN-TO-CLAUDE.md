# BRAIN -> CLAUDE C19

## STATUS
MANDAT_BLUEPRINT_CONCEPTUAL

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

SPEC 11-slot C19 este înghețat și acceptat:

`C19_SPEC_11_SLOT_FROZEN_ACCEPTAT`

Nu mai este nevoie de iterație pe SPEC.

Sloturi locked pentru Blueprint:

- SLUG: `guvernare`
- MIZA HERO: `GUVERNAREA SISTEMULUI PRIN REGULI`
- HERO: `Cum se ține corect fără ochiul meu?`
- BOMBĂ: `Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.`
- MANTRA: `Nu o supraveghez. O guvernez prin reguli.`
- WOW: `Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.`
- MOTTO: `Pleci, și munca se ține singură.`
- GREȘEALA: `Confunzi «merge» cu «merge corect».`
- AHA: `Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.`
- Artefact confirmat: `_GUVERNARE`
- STEP 5 locked: `Excepția și oprirea controlată`

MOTTO status:
`acceptat pentru C19, dar dependent de ratificarea template-ului T5`.

## MANDAT

Pregătește Blueprint conceptual C19, fără implementare.

Nu genera artefacte.
Nu modifica c19/**.
Nu modifica fișiere sistem.
Nu genera HTML, Date_MASTER, build scripts sau FILM.

### 1. Structură Blueprint cerută

Blueprint-ul trebuie să conțină:

- cele 6 etape finale C19
- 18 pași, câte 3 pași per etapă
- scopul fiecărei etape
- obiectul Excel al fiecărei etape
- ce se vede în film
- ce NU trebuie să apară ca să nu contaminăm C18 / C20 / T4
- test de validare pe fiecare etapă

### 2. Cele 6 etape obligatorii

Păstrează această structură:

1. `Sistemul care merge doar cât te uiți`
2. `Ce poate să devieze previzibil`
3. `Regula care prinde intrarea greșită`
4. `Pragul și semnalul`
5. `Excepția și oprirea controlată`
6. `Testul ochilor închiși`

### 3. Arc demonstrativ obligatoriu Excel

Blueprint-ul trebuie să poată fi filmat în Excel prin arc clar:

input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

### 4. Granițe de păstrat

- C18 = rulează
- C19 = se ține corect
- C20 = predă responsabilitatea

C19 nu este:

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

### 5. Interdicții operaționale

Nu crea folder `c19/`.
Nu crea fișiere HTML.
Nu crea Excel.
Nu crea FILM.
Nu crea build script.
Nu modifica `_system/**`.
Nu modifica alte `_brain/**`.
Nu modifica alte construcții.

### 6. Raport

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## BLUEPRINT CONCEPTUAL C19

## CELE 6 ETAPE

## CEI 18 PAȘI

## ARC DEMONSTRATIV EXCEL

## GRANIȚE ȘI GARZI

## RISCURI

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după scrierea raportului.

## RAPORT
Aștept Blueprint conceptual C19 în _brain/c19/CLAUDE-TO-BRAIN.md.
