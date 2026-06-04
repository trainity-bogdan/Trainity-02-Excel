# BRAIN → CLAUDE · C10 MĂSURI

## STATUS
SPEC_MANDATE_READY

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C10.

La comanda `sync`, citește:
- `_brain/c10/CHAT-CONTEXT.md`
- `_brain/c10/BRAIN-TO-CLAUDE.md`

Execută doar în:
- `c10/**`
- `_brain/c10/**`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.
Nu modifica fișiere sistem.

## STARE CURENTĂ C10
Construcția C10 este în faza de arhitectură / specificare.

## REGULĂ SYSTEM
Dacă ai nevoie de fișier comun, NU îl modifica.
Scrie `CERERE SYSTEM` în `_brain/c10/CLAUDE-TO-BRAIN.md`.

---

# MANDAT BRAIN C10 · SPEC ARHITECTURAL

## Identitate construcție

C10 se numește:

**MĂSURI**

Rolul C10 este să ducă natural mai departe C09 RELAȚII.

C09 arată că datele trebuie legate corect.
C10 arată că, după ce datele sunt legate corect, cursantul trebuie să aleagă măsura potrivită pentru întrebarea potrivită.

Ideea centrală C10:

**Fără măsuri, ai cifre. Cu măsuri corecte, ai decizie.**

C10 NU este despre formule multe.
C10 NU este despre calcul decorativ.
C10 este despre transformarea cifrelor brute în indicatori controlabili, explicați și folosiți pentru decizie.

---

## SPEC propus C10

### 1. SLUG

`masuri`

### 2. INTRIGA

Setul de date pare pregătit pentru analiză. Relațiile sunt corecte, tabelele comunică între ele, iar structura permite citirea coerentă a informației.

Totuși, cursantul descoperă că simpla existență a datelor nu produce decizii.

Apar totaluri, medii, procente, ponderi și comparații, dar ele pot induce în eroare dacă nu sunt definite ca măsuri clare, legate de întrebări reale de business.

Intriga C10 este trecerea de la "avem cifre" la "știm exact ce măsurăm și de ce".

### 3. PROBLEMELE

C10 trebuie să expună următoarele probleme:

- se calculează totaluri fără întrebare clară
- se folosesc medii care pot ascunde realitatea
- se compară valori care nu sunt comparabile
- se confundă cifra brută cu indicatorul util
- se trag concluzii din calcule izolate
- se folosesc procente fără bază de raportare clară
- se măsoară prea mult și se decide prea puțin
- nu există criteriu stabil pentru ce merită măsurat

### 4. MIZA

Cursantul învață să transforme datele legate corect în măsuri utile, controlabile și explicabile.

Miza C10:

**O măsură bună reduce haosul, nu îl amplifică.**

### 5. MANTRA

**Măsura corectă răspunde întrebării corecte.**

### 6. WOW

Același set de date poate susține concluzii complet diferite în funcție de măsura aleasă.

WOW-ul C10 trebuie să arate că problema nu este lipsa cifrelor, ci alegerea greșită a cifrei care primește autoritate.

### 7. MOTTO

**Nu calcula mai mult. Măsoară mai corect.**

### 8. FENOMENE

C10 poate lucra cu aceste fenomene, fără să devină lecție tehnică de formule:

- total
- medie
- procent
- pondere
- variație
- contribuție
- prag
- abatere
- ranking
- comparație contextuală
- reper
- semnal

### 9. STEP-TITLES ORIENTATIVE

Propune pași în logica următoare:

1. Confirmă că datele sunt legate corect
2. Formulează întrebarea de business
3. Alege măsura potrivită
4. Definește baza de raportare
5. Compară măsura cu un reper
6. Separă cifra utilă de cifra decorativă
7. Validează dacă măsura susține o decizie
8. Confirmă setul de măsuri controlabile

Claude poate rafina titlurile, dar nu trebuie să schimbe axa pedagogică.

---

## AHA C10

**Nu cifra contează. Contează ce întrebare răspunde cifra.**

---

## Schimbare mentală urmărită

C10 trebuie să mute cursantul:

de la:

**Ce pot calcula?**

la:

**Ce trebuie să măsor ca să pot decide?**

---

## Formula finală C10

**Date legate corect + întrebare clară + măsură potrivită = decizie controlabilă.**

---

## Cerință către Claude C10

La următorul `sync`, Claude C10 trebuie să:

1. citească acest mandat,
2. verifice dacă există conflicte cu C09 sau cu poziționarea T3,
3. propună SPEC C10 final în `_brain/c10/CLAUDE-TO-BRAIN.md`,
4. NU genereze încă artefacte,
5. NU modifice fișiere sistem,
6. NU modifice alte construcții.

Output așteptat în `_brain/c10/CLAUDE-TO-BRAIN.md`:

- STATUS: SPEC_PROPOSED
- rezumat axă C10
- propunere SPEC final
- eventuale conflicte sau întrebări pentru BRAIN
- CERERE SYSTEM doar dacă este absolut necesar
