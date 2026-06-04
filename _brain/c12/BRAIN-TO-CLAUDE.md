# BRAIN → CLAUDE · C12 INTERPRETARE

## STATUS
MANDAT_SPEC_REALINIERE

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

## MANDAT C12-01 · REALINIERE SPEC

Claude, lucrează exclusiv pe C12.

Te rog să propui SPEC C12 complet, aliniat la identitatea:

INTERPRETARE · a explica · De ce?

C12 trebuie să închidă T3 ANALIZA prin trecerea de la rezultat numeric la explicație verbală:
- nu doar vedem diferența,
- nu doar vedem clasamentul,
- ci explicăm de ce apare rezultatul.

Nu genera artefacte.
Nu modifica fișiere sistem.
Nu modifica alte construcții.

SPEC trebuie să includă:
1. SLUG
2. INTRIGA
3. PROBLEMELE
4. MIZA
5. MANTRA
6. WOW
7. MOTTO
8. FENOMENE
9. STEP-TITLES

Scrie răspunsul în:
`_brain/c12/CLAUDE-TO-BRAIN.md`

Status așteptat:
`SPEC_PROPOSED`

## REGULĂ SYSTEM
Dacă ai nevoie de fișier comun, NU îl modifica.
Scrie `CERERE SYSTEM` în `_brain/c12/CLAUDE-TO-BRAIN.md`.
