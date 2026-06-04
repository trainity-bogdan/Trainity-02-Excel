# BRAIN → CLAUDE · C10 MĂSURI

## STATUS
SPEC_FROZEN

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
Construcția C10 are SPEC înghețat. Cele 9 elemente SPEC de mai jos sunt definitive.

## REGULĂ SYSTEM
Dacă ai nevoie de fișier comun, NU îl modifica.
Scrie `CERERE SYSTEM` în `_brain/c10/CLAUDE-TO-BRAIN.md`.

---

# SPEC C10 ÎNGHEȚAT

## 1. SLUG
`masuri`

## 2. INTRIGA
Setul de date pare pregătit pentru analiză. Relațiile sunt corecte, tabelele comunică între ele, iar structura permite citirea coerentă a informației. Totuși, simpla existență a datelor nu produce decizii. Apar totaluri, medii, procente, ponderi și comparații, dar ele pot induce în eroare dacă nu sunt definite ca măsuri clare, legate de întrebări reale de business. Intriga C10 este trecerea de la "avem cifre" la "știm exact ce măsurăm și de ce".

## 3. PROBLEMELE
- se calculează totaluri fără întrebare clară
- se folosesc medii care pot ascunde realitatea
- se compară valori care nu sunt comparabile
- se confundă cifra brută cu indicatorul util
- se trag concluzii din calcule izolate
- se folosesc procente fără bază de raportare clară
- se măsoară prea mult și se decide prea puțin
- nu există criteriu stabil pentru ce merită măsurat

## 4. MIZA
Cursantul învață să transforme datele legate corect în măsuri utile, controlabile și explicabile. O măsură bună reduce haosul, nu îl amplifică.

## 5. MANTRA
Măsura corectă răspunde întrebării corecte.

## 6. WOW
Același set de date poate susține concluzii complet diferite în funcție de măsura aleasă. Problema nu este lipsa cifrelor, ci alegerea greșită a cifrei care primește autoritate.

## 7. MOTTO
Nu calcula mai mult. Măsoară mai corect.

## 8. FENOMENE
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

## 9. STEP-TITLES
1. Confirmă că datele sunt legate corect
2. Formulează întrebarea de business
3. Alege măsura potrivită
4. Definește baza de raportare
5. Compară măsura cu un reper
6. Separă cifra utilă de cifra decorativă
7. Validează dacă măsura susține o decizie
8. Confirmă setul de măsuri controlabile

---

## AHA C10
Nu cifra contează. Contează ce întrebare răspunde cifra.

## Schimbare mentală urmărită
De la: Ce pot calcula?
La: Ce trebuie să măsor ca să pot decide?

## Formula finală C10
Date legate corect + întrebare clară + măsură potrivită = decizie controlabilă.

## Cerință către Claude C10
La următorul `sync`, tratează SPEC C10 ca înghețat. Verifică regulile locale. Dacă generarea este permisă, generează C10. Nu modifica fișiere sistem. Nu modifica alte construcții. Dacă apare blocaj, raportează în `_brain/c10/CLAUDE-TO-BRAIN.md`.
