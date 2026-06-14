# BRAIN -> CLAUDE C19

## STATUS
MANDAT_FREEZE_SPEC_11_SLOT

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19, confirmată în CHAT-CONTEXT:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

SPEC 11-slot C19 este acceptat pentru freeze:

`C19_SPEC_11_SLOT_ACCEPTAT_PENTRU_FREEZE`

Aprobări BRAIN:

- SLUG: `guvernare`
- MIZA HERO: `GUVERNAREA SISTEMULUI PRIN REGULI`
- HERO: `Cum se ține corect fără ochiul meu?`
- BOMBĂ: `Motorul tău rulează. Dar tot tu verifici că n-a greșit, de fiecare dată.`
- MANTRA: `Nu o supraveghez. O guvernez prin reguli.`
- WOW: `Un sistem care mergea doar cât stăteai cu ochii pe el. Acum, pe o intrare greșită, se oprește singur și aprinde semnalul, fără tine.`
- MOTTO candidat: `Pleci, și munca se ține singură.`
- GREȘEALA: `Confunzi «merge» cu «merge corect».`
- AHA: `Un sistem în care ai încredere nu e cel pe care îl urmărești. E cel care se prinde singur când greșește.`
- Artefact confirmat: `_GUVERNARE`

## MANDAT

Pregătește versiunea de freeze pentru SPEC 11-slot C19, fără implementare.

Nu genera artefacte.
Nu modifica c19/**.
Nu modifica fișiere sistem.
Nu genera HTML, Date_MASTER, build scripts sau FILM.

### 1. Ajustare obligatorie STEP 5

În STEP-TITLES, ajustează etapa 5 ca să nu sugereze escaladare, ownership sau responsabil uman.

Înlocuiește formularea riscantă:

`Exceptia si fail-safe-ul (_GUVERNARE: ce opreste lantul, ce cere atentie umana - granita C20)`

cu formularea recomandată:

`Excepția și oprirea controlată`

Descriere obligatorie pentru etapa 5:

`_GUVERNARE marchează excepția, oprește lanțul sau schimbă starea, dar nu desemnează responsabilul.`

### 2. Sloturi de păstrat

Păstrează toate sloturile aprobate anterior:

1. SLUG
2. INTRIGA
3. PROBLEMELE
4. MIZA
5. MANTRA
6. WOW
7. MOTTO
8. FENOMENE
9. STEP-TITLES
10. GREȘEALA
11. AHA

### 3. Granițe obligatorii

Păstrează explicit distincția:

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

### 4. MOTTO

Marchează MOTTO ca:

`acceptat pentru C19, dar dependent de ratificarea template-ului T5`

Conținutul MOTTO rămâne:

`Pleci, și munca se ține singură.`

### 5. Output cerut

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## SPEC 11-SLOT C19 FREEZE

## AJUSTARE STEP 5

## GRANIȚE CONFIRMATE

## MOTTO STATUS

## RISCURI RĂMASE

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după scrierea raportului.

## RAPORT
Aștept SPEC 11-slot C19 freeze în _brain/c19/CLAUDE-TO-BRAIN.md.
