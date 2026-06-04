# CLAUDE → BRAIN · C10 MĂSURI

## STATUS
SPEC_PROPOSED

## RAPORT SYNC (2026-06-04)

Sync executat în chat dedicat C10.

Pași parcurși:
1. `git fetch origin main` (e85a318 `freeze C10 spec status`).
2. Citit `_brain/c10/CHAT-CONTEXT.md` + `_brain/c10/BRAIN-TO-CLAUDE.md` (mandat SPEC).
3. Verificat conflicte cu C09 (read-only `c09/`) și cu poziționarea T3 (read-only `_system/06-MAP-CONSTRUCTII-T1-T5.md`).
4. NU am generat artefacte. NU am atins fișiere sistem sau alte construcții.

---

## REZUMAT AXĂ C10 (confirmat)

C10 = **MĂSURI**. Verb-semnătură **a defini**. Întrebare-mamă **„Cât?"**.

Axa pedagogică (de acord 100% cu mandatul BRAIN):
**Fără măsuri, ai cifre. Cu măsuri corecte, ai decizie.**

C10 duce mai departe C09 (RELAȚII / „a lega" / „Ce pot întreba?"): după ce datele sunt legate corect într-un model interogabil, cursantul trebuie să transforme cifra brută într-o **măsură** definită o singură dată, repetabilă și context-aware (single source of truth). C10 NU e despre multe formule, ci despre alegerea și definirea corectă a măsurii.

---

## VERIFICARE CONFLICTE

### Cu C09 (RELAȚII) — FĂRĂ CONFLICT
C09 construiește relațiile reale (merge / 1:M / Data Model) și produce modelul interogabil. C10 pornește din acel model (Pasul 1 „Confirmă că datele sunt legate corect" = moștenire curată din C09, nu reluare). Granița e clară: C09 = „ce pot întreba", C10 = „cât / care e răspunsul măsurat".

### Cu C11 (COMPARAȚII) — CONFLICT DE DELIMITARE (de rezolvat)
Harta T3 (autoritate, lock BRAIN-006) fixează:
- C10 = a **defini** o măsură (Cât?).
- C11 = a **compara**: clasament / diferență / **contribuție** / ABC-Pareto (Care?).

FENOMENE-le propuse de BRAIN conțin 3 elemente care, în harta oficială, sunt teritoriu C11:
- **ranking** = clasament => C11
- **contribuție** = contribuție/pondere-în-total => C11
- **comparație contextuală** = comparație între entități => C11

Recomandarea mea: aceste 3 ies din C10 și se rezervă pentru C11, ca să nu repetăm la C10 ediția slabă a comparației și să golim C11 de substanță. Verbul „a compara" și întrebarea „Care?" trebuie să rămână ABSENTE din C10. C10 păstrează doar raportarea măsurii la un **reper/prag definit** (parte din definiția măsurii), nu comparația între entități.

### Cu C06 (CLASIFICARE) — RISC MINOR
C06 produce per-rând „scor 0-100" / etichetă prin reguli. C10 NU reia scorul per-rând. „Semnalul" din C10 este o **măsură agregată** care trece un prag (cantitativ, context-aware), nu o etichetă pe rând. Notez delimitarea ca să evităm redrift.

### Cu C12 (INTERPRETARE) — RISC PE „variație"
„variație" poate aluneca spre evoluție-în-timp / „de ce" (C12) sau spre comparație lună-la-lună (C11). Propun să o păstrăm în C10 DOAR ca măsură definită (ex. variație % față de un reper/țintă), nu ca narațiune de trend temporal. Întrebare deschisă mai jos.

---

## PROPUNERE SPEC C10 FINAL

### 1. SLUG
`masuri`

### 2. INTRIGA (confirmată, ușor ascuțită)
Relațiile sunt corecte, tabelele comunică, modelul e interogabil. Totuși simpla existență a datelor legate nu produce decizii. Apar totaluri, medii, procente, dar ele pot induce în eroare dacă nu sunt definite ca măsuri clare, ancorate într-o întrebare reală. Intriga C10: trecerea de la „avem cifre" la „știm exact ce măsurăm și de ce".

### 3. PROBLEMELE (confirmate, 8)
- se calculează totaluri fără întrebare clară
- se folosesc medii care ascund realitatea
- se confundă cifra brută cu indicatorul util
- se folosesc procente fără bază de raportare clară
- aceeași cifră e recalculată diferit în locuri diferite (lipsă single source of truth)
- măsura se rupe când schimbi tăietura/filtrul (nu e context-aware)
- se trag concluzii din calcule izolate
- nu există criteriu stabil pentru ce merită măsurat

(Am înlocuit cele 2 probleme care duceau spre C11, „se compară valori care nu sunt comparabile" și „se măsoară prea mult și se decide prea puțin", cu 2 probleme pur-definiționale: lipsa single source of truth și fragilitatea la context. Originalele se mută natural în C11.)

### 4. MIZA (confirmată)
Cursantul transformă datele legate corect în măsuri utile, controlabile, explicabile.
**O măsură bună reduce haosul, nu îl amplifică.**

### 5. MANTRA (confirmată)
**Măsura corectă răspunde întrebării corecte.**

### 6. WOW (confirmat)
Același set de date poate susține concluzii complet diferite în funcție de măsura aleasă. Problema nu e lipsa cifrelor, ci alegerea greșită a cifrei care primește autoritate.

### 7. MOTTO (confirmat)
**Nu calcula mai mult. Măsoară mai corect.**

### 8. FENOMENE (REVIZUITE — 6, pur C10 „a defini")
1. **Măsura ca definiție unică** (single source of truth): total/medie definite o dată, reutilizabile, nu recalculate ad-hoc.
2. **Baza de raportare**: procentul/raportul fără bază explicită minte; măsura relativă își declară numitorul.
3. **Reperul / pragul**: măsura capătă sens raportată la un reper definit (țintă/prag), parte din definiția ei.
4. **Context-awareness**: aceeași definiție produce rezultatul corect pe orice tăietură/filtru (esența măsurii vii în Data Model).
5. **Cifra utilă vs cifra decorativă**: criteriul prin care selectezi ce merită promovat la rang de măsură.
6. **Semnalul controlabil**: măsura produce un semnal explicabil (prag atins/abatere față de reper), nu doar o cifră.

Instrument tehnic (NU axă): măsuri în Power Pivot / Data Model (DAX ca vehicul, conform tehnologiei dominante T3). În HTML/FILM rămân referințe generice (R-V02.15 zero cifre business).

EXCLUSE explicit din C10 (rezervate C11): ranking/clasament, contribuție/pondere-în-total, comparație contextuală între entități, ABC/Pareto.

### 9. STEP-TITLES (rafinate, axa nemodificată, verbul „a compara" eliminat)
1. Confirmă că datele sunt legate corect (moștenire C09)
2. Formulează întrebarea de business („Cât?")
3. Alege măsura potrivită întrebării
4. Definește baza de raportare a măsurii
5. Ancorează măsura într-un reper (prag/țintă)
6. Separă cifra utilă de cifra decorativă
7. Verifică robustețea măsurii (context-aware: aceeași definiție pe orice tăietură)
8. Confirmă setul de măsuri controlabile (single source of truth)

(Singura modificare de fond față de mandat: pasul 5 „Compară măsura cu un reper" devine „Ancorează măsura într-un reper", ca să eliminăm verbul „a compara" care e semnătura C11. Pasul 7 capătă accent pe context-awareness, marca măsurii vii în Data Model. Axa pedagogică rămâne intactă.)

### AHA
**Nu cifra contează. Contează ce întrebare răspunde cifra.**

### Schimbare mentală
De la „Ce pot calcula?" la „Ce trebuie să măsor ca să pot decide?".

### Formula finală
**Date legate corect + întrebare clară + măsură potrivită = decizie controlabilă.**

---

## CONTINUITATE (pentru faza de generare)
- R-V02.14: C10 NU schimbă `valoare_neta`; definește măsuri peste aceleași date. Input C10 = output C09 (sumă conservată).
- R-V02.15: cifrele trăiesc în Excel; HTML/FILM doar referințe generice.
- Generare din copy `c01/` (matriță), apoi gate_v20 + audit_sync înainte de livrare.

---

## ÎNTREBĂRI PENTRU BRAIN (înainte de freeze SPEC final)
1. **Confirmi scoaterea din C10 a fenomenelor ranking / contribuție / comparație contextuală** (mutate în C11), păstrând în C10 doar reperul/pragul ca parte din definiția măsurii? (Recomand: DA, ca să respectăm lock-ul T3 a defini vs a compara.)
2. **„variație" și „abatere":** le păstrăm în C10 doar ca măsuri definite față de un reper/țintă (NU ca trend temporal sau comparație lună-la-lună, care ar fi C11/C12)? (Recomand: DA, reformulate ca „abatere față de reper definit", fără narațiune de evoluție.)
3. **Numărul de fenomene:** propun 6 (vs 12 în mandat). Confirmi 6, sau vrei aliniere la alt număr-țintă pentru T3?

La confirmarea acestor 3 puncte + STATUS `SPEC_FROZEN` în BRAIN-TO-CLAUDE, trec la `genereaza CNN` (creez `c10/` din copy `c01/`).

## CERERI SYSTEM
Nicio cerere deschisă. (Pentru verificarea conflictelor am citit `c09/` și `_system/06-MAP` strict read-only, fără modificări.)
