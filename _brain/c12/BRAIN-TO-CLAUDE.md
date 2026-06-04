# BRAIN → CLAUDE · C12 INTERPRETARE

## STATUS
MANDAT_SPEC_FREEZE

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C12.

La comanda `sync`, citește:
- `_brain/c12/CHAT-CONTEXT.md`
- `_brain/c12/BRAIN-TO-CLAUDE.md`

Execută doar în:
- `c12/**`
- `_brain/c12/**`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.
Nu modifica fișiere sistem.

## STARE CURENTĂ C12
C12 este construcția INTERPRETARE.

Conform hărții oficiale T3:
- C09 = RELAȚII, model interogabil, întrebarea „Ce pot întreba?”
- C10 = MĂSURI, întrebarea „Cât?”
- C11 = COMPARAȚII, întrebarea „Care?”
- C12 = INTERPRETARE, întrebarea „De ce?”

Verb-semnătură C12: a explica.
Rol C12: explică insight-ul verbal, cauza citită din model, interpretarea rezultatului după relații, măsuri și comparații.

Nu porni C12 ca „KPI / FILTER CONTEXT”. Aceasta nu mai este identitatea principală.

## MANDAT C12-02 · ÎNGHEȚARE SPEC

Claude, lucrează exclusiv pe C12.

Am analizat SPEC C12 propus. Direcția este confirmată:

C12 = INTERPRETARE
Verb-semnătură = a explica
Întrebare-mamă = De ce?

Te rog să îngheți SPEC C12 cu următoarele decizii BRAIN:

### 1. Număr fenomene
Confirm 6 fenomene.

### 2. Număr STEP-TITLES
Confirm 8 step-titles.

### 3. Hero vizual
Hero name confirmat:
DE CE-UL DIN DATE

### 4. Corelație vs cauză
Nu păstra formularea tehnică „corelație vs cauză” ca titlu principal de fenomen.
Reformulează operațional:
„Ce apare împreună nu explică automat ce produce rezultatul.”

### 5. Cauză multiplă
Introdu explicit fenomenul „cauză multiplă”:
în business, rezultatul rar are o singură cauză; interpretarea bună identifică factorii principali și nu forțează o explicație unică.

### 6. Elemente confirmate
Păstrează:

MANTRA:
Cifra spune cât. Explicația spune de ce.

MOTTO:
Nu citi rezultatul. Explică-l.

AHA:
Nu rezultatul contează. Contează de ce apare rezultatul.

FORMULA FINALĂ:
Rezultat numeric + cauză citită din model + frază verificabilă = insight care închide analiza.

### 7. Delimitări obligatorii
C12 nu face dashboard.
C12 nu face what-if.
C12 nu face scenarii.
C12 nu face predicție.
C12 nu recomandă acțiuni.
C12 explică ce s-a întâmplat și de ce, pe baza modelului.

Nu genera artefacte.
Nu modifica fișiere sistem.
Nu modifica alte construcții.

Scrie SPEC final înghețat în:
`_brain/c12/CLAUDE-TO-BRAIN.md`

Status așteptat:
`SPEC_FROZEN`

## REGULĂ SYSTEM
Dacă ai nevoie de fișier comun, NU îl modifica.
Scrie `CERERE SYSTEM` în `_brain/c12/CLAUDE-TO-BRAIN.md`.
