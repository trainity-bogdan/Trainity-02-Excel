# BRAIN -> CLAUDE C19

## STATUS
MANDAT_PREGATIRE_GENERARE

## CONTEXT
C19 GUVERNAREA. T5 AUTONOMIE. CUVÂNT LOCKED = CONTROL. VERB LOCKED = GUVERNEZ.

Rol C19 în T5: scoate autorul din ATENȚIE.

Axa C19:
DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.

## DECIZIE BRAIN

C19 are acum:

- SEED acceptat
- SPEC 11-slot frozen acceptat
- Blueprint conceptual acceptat

Status:

`C19_BLUEPRINT_CONCEPTUAL_ACCEPTAT`

Nu mai este nevoie de iterație pe Blueprint.

## MANDAT

Pregătește raportul de readiness pentru generarea C19.

Atenție: acesta NU este mandat de generare. Este doar mandat de pregătire a generării.

Nu genera artefacte.
Nu crea folder `c19/`.
Nu genera HTML.
Nu genera Excel.
Nu genera FILM.
Nu genera build script.
Nu modifica fișiere sistem.
Nu modifica alte construcții.

### 1. Verificare readiness

Raportează dacă C19 este pregătit pentru mandat de generare, pe baza celor trei niveluri:

- SEED acceptat
- SPEC frozen acceptat
- Blueprint conceptual acceptat

### 2. Checklist de generare viitoare

Pregătește checklist-ul care trebuie inclus într-un mandat viitor de generare C19.

Checklist obligatoriu:

- creează folder `c19/` doar la mandat explicit de generare
- generează cele 7 artefacte canonice doar la mandat explicit
- păstrează `_GUVERNARE` distinct de `_AUTOMATIZARE`
- include `STATUS` OK / ATENȚIE / OPRIT
- include Data Validation la sursă
- include praguri vii
- include listă de excepții
- include fail-safe automat
- păstrează zero responsabil / owner / escaladare
- Etapa 4 = semnal care schimbă starea, nu dashboard
- Etapa 5 = oprire automată, nu intervenție umană
- arcul Excel: input greșit -> regulă -> prag / stare -> excepție -> oprire controlată -> testul ochilor închiși

### 3. Riscuri de generare

Identifică riscurile care trebuie păzite în mandatul de generare:

- contaminare C18
- contaminare C20
- contaminare T4 dashboard
- contaminare C04 refresh
- babysitting / monitorizare zilnică
- QA generic / audit clasic
- folosirea `motor` ca identitate C19

### 4. Raport

Scrie raportul exclusiv în:

`_brain/c19/CLAUDE-TO-BRAIN.md`

Format raport:

# CLAUDE -> BRAIN C19

## STATUS

## READINESS GENERARE C19

## CHECKLIST MANDAT GENERARE VIITOARE

## RISCURI DE GENERARE

## BLOCAJE / DEPENDENȚE

## CERERI CĂTRE BRAIN / SYSTEM

## COMMIT

Fă commit descriptiv pe main după scrierea raportului.

## RAPORT
Aștept raport readiness pentru generare C19 în _brain/c19/CLAUDE-TO-BRAIN.md.
