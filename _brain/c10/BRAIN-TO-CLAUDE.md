# BRAIN → CLAUDE · C10 MĂSURI

## STATUS
SPEC_FROZEN_FINAL

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
Construcția C10 are SPEC final înghețat. Claude C10 poate genera C10 dacă regulile locale permit.

## REGULĂ SYSTEM
Dacă ai nevoie de fișier comun, NU îl modifica.
Scrie `CERERE SYSTEM` în `_brain/c10/CLAUDE-TO-BRAIN.md`.

---

# CONFIRMARE BRAIN C10

BRAIN confirmă raportul Claude C10 și acceptă cele 3 recomandări:

1. DA, se scot din C10 fenomenele `ranking`, `contribuție`, `comparație contextuală`.
2. DA, `variație` și `abatere` se păstrează doar ca abatere față de reper / țintă definită, fără trend temporal și fără comparație lună-la-lună.
3. DA, C10 lucrează cu 6 fenomene, nu cu 12.

Motiv: C10 trebuie să rămână strict pe verbul `a defini`, întrebarea-mamă `Cât?`, și nu trebuie să invadeze C11, unde verbul este `a compara`.

---

# SPEC C10 FINAL ÎNGHEȚAT

## 1. SLUG
`masuri`

## 2. INTRIGA
Relațiile sunt corecte, tabelele comunică, modelul este interogabil. Totuși, simpla existență a datelor legate nu produce decizii. Apar totaluri, medii și procente, dar ele pot induce în eroare dacă nu sunt definite ca măsuri clare, ancorate într-o întrebare reală. Intriga C10 este trecerea de la "avem cifre" la "știm exact ce măsurăm și de ce".

## 3. PROBLEMELE
- se calculează totaluri fără întrebare clară
- se folosesc medii care ascund realitatea
- se confundă cifra brută cu indicatorul util
- se folosesc procente fără bază de raportare clară
- aceeași cifră este recalculată diferit în locuri diferite
- măsura se rupe când se schimbă tăietura sau filtrul
- se trag concluzii din calcule izolate
- nu există criteriu stabil pentru ce merită măsurat

## 4. MIZA
Cursantul transformă datele legate corect în măsuri utile, controlabile, explicabile.

**O măsură bună reduce haosul, nu îl amplifică.**

## 5. MANTRA
**Măsura corectă răspunde întrebării corecte.**

## 6. WOW
Același set de date poate susține concluzii complet diferite în funcție de măsura aleasă. Problema nu este lipsa cifrelor, ci alegerea greșită a cifrei care primește autoritate.

## 7. MOTTO
**Nu calcula mai mult. Măsoară mai corect.**

## 8. FENOMENE C10
1. Măsura ca definiție unică, single source of truth.
2. Baza de raportare, procentul sau raportul își declară numitorul.
3. Reperul / pragul, măsura capătă sens raportată la o țintă sau limită definită.
4. Context-awareness, aceeași definiție produce rezultat corect pe orice tăietură sau filtru.
5. Cifra utilă vs cifra decorativă, criteriul prin care alegi ce merită promovat la rang de măsură.
6. Semnalul controlabil, măsura produce un semnal explicabil, nu doar o cifră.

## 9. STEP-TITLES FINALE
1. Confirmă că datele sunt legate corect
2. Formulează întrebarea de business, "Cât?"
3. Alege măsura potrivită întrebării
4. Definește baza de raportare a măsurii
5. Ancorează măsura într-un reper
6. Separă cifra utilă de cifra decorativă
7. Verifică robustețea măsurii
8. Confirmă setul de măsuri controlabile

---

## AHA C10
**Nu cifra contează. Contează ce întrebare răspunde cifra.**

## Schimbare mentală urmărită
De la: **Ce pot calcula?**
La: **Ce trebuie să măsor ca să pot decide?**

## Formula finală C10
**Date legate corect + întrebare clară + măsură potrivită = decizie controlabilă.**

---

# MANDAT CĂTRE CLAUDE C10

La următorul `sync`, Claude C10 trebuie să:

1. trateze acest SPEC ca final și înghețat,
2. genereze C10 dacă regulile locale permit,
3. păstreze C10 strict pe `a defini`, nu pe `a compara`,
4. nu includă ranking, contribuție, comparație contextuală, ABC sau Pareto,
5. nu modifice fișiere sistem,
6. nu modifice alte construcții,
7. raporteze rezultatul în `_brain/c10/CLAUDE-TO-BRAIN.md`.
