# CLAUDE → BRAIN · C11 COMPARAȚII / RANK

## STATUS
SPEC_PROPOSED

## RAPORT SYNC (2026-06-04)

Sync executat în chat dedicat C11.

Pași parcurși:
1. `git fetch origin main` — origin la `3760e66` (`add C11 first SPEC mandate`).
2. Local main divergit (force-update pe origin). Am aliniat local main la canonicul `origin/main`. Commit-urile vechi locale (C05-C08, tip `19efcd5`) rămân recuperabile via reflog — NU le-am atins. Vezi NOTĂ SYSTEM la final.
3. Citit `_brain/c11/CHAT-CONTEXT.md` + `_brain/c11/BRAIN-TO-CLAUDE.md` (mandat C11-01 SPEC).
4. Verificat poziționarea T3 (read-only `_system/06-MAP-CONSTRUCTII-T1-T5.md`) și delimitarea față de C10 (read-only `_brain/c10/`).
5. NU am generat HTML/artefacte. NU am atins fișiere sistem sau alte construcții.

---

## REZUMAT AXĂ C11 (din harta T3, autoritate BRAIN-006)

C11 = **COMPARAȚII**. Verb-semnătură **a compara**. Întrebare-mamă **„Care?"**.

Lanțul T3 LOCKED: model (C09) -> măsură (C10) -> **clasament (C11)** -> explicație (C12).

Axa pedagogică (de acord 100% cu mandatul BRAIN):
**Fără comparație, analiza rămâne plată. Cu comparație, datele capătă ierarhie.**

C11 duce mai departe C10 (MĂSURI / „a defini" / „Cât?"): după ce cifra brută a devenit o măsură corectă, repetabilă și context-aware, cursantul trebuie să așeze măsurile **una lângă alta** și să vadă cine conduce rezultatul. C11 NU redefinește măsura, o **ordonează, diferențiază și ponderează**. ABC/Pareto și RANKX sunt instrumente de comparație, NU identitatea axei.

---

## VERIFICARE CONFLICTE

### Cu C10 (MĂSURI) — FĂRĂ CONFLICT (granița deja negociată)
C10 a EXCLUS explicit și a rezervat pentru C11: ranking/clasament, contribuție/pondere-în-total, comparație contextuală între entități, ABC/Pareto. C11 le primește integral. Granița: C10 = „cât / care e răspunsul măsurat" (o măsură, definită o dată); C11 = „care / cine conduce" (măsuri așezate în competiție). C11 pornește din măsura curată moștenită din C10 (Pasul 1), nu o reia.

### Cu C12 (INTERPRETARE) — DELIMITARE FERMĂ
C11 spune **CARE / CINE** conduce (faptul ierarhiei: clasament, gap, contribuție, concentrare). C12 spune **DE CE** (cauza din spatele ierarhiei, insight verbal). C11 se oprește la constatarea ierarhiei; orice „de ce / pentru că" alunecă în C12. Verbul „a explica" și întrebarea „De ce?" rămân ABSENTE din C11.

### Cu C06 (CLASIFICARE) — RISC MINOR (delimitare)
C06 etichetează per-rând prin reguli (scor/etichetă pe rând). C11 NU etichetează rânduri: compară **entități/actori agregați** (categorii, produse, regiuni) după o măsură. „Clasament" în C11 = ordonare relativă între actori, nu scor absolut pe rând. Notez delimitarea ca să evităm redrift C06↔C11.

### Cu C13+ (T4 RAPORTARE) — FĂRĂ CONFLICT
C11 produce ierarhia ca rezultat analitic; T4 o transformă în interfață/dashboard. C11 nu construiește dashboard.

---

## PROPUNERE SPEC C11

### 1. SLUG
`comparatii`

### 2. INTRIGA
Datele sunt legate corect (C09) și măsurate corect (C10). Totuși o listă de măsuri, oricât de corectă, rămâne o masă plată: sute de produse cu cifrele lor nu spun cine duce afacerea. Ochiul nu poate ierarhiza singur o coloană lungă de numere, iar „mare în listă" este confundat cu „important pentru rezultat". Intriga C11: trecerea de la „avem măsuri corecte" la „știm cine contează" — de la listă plată la ierarhie clară.

### 3. PROBLEMELE (8)
- se citește lista fără să se vadă cine conduce rezultatul
- se compară valori care nu sunt comparabile (unități, perioade sau baze diferite)
- se confundă „mare în listă" cu „important pentru rezultat"
- se tratează toate elementele ca egale, fără ierarhie
- se reacționează la diferențe minuscule (zgomot luat drept semnal)
- nu se vede concentrarea: că puțini actori duc majoritatea rezultatului
- se ignoră contribuția în total (poziție fără pondere)
- se decide pe baza ordinii brute, fără un reper relativ (lider/mediană)

### 4. MIZA
Cursantul transformă măsurile corecte într-o ierarhie decizională: vede instant cine duce rezultatul și cine doar apare în listă.
**Fără comparație, analiza rămâne plată. Cu comparație, datele capătă ierarhie.**

### 5. MANTRA
**Nu toate valorile sunt egale. Unele conduc rezultatul.**

### 6. WOW
Într-un set cu sute de elemente, de obicei o mână duce majoritatea rezultatului. Comparația corectă scoate la lumină că „mult" și „important" nu sunt același lucru — iar lista plată ascundea o ierarhie brutală în care câțiva actori decid totul.

### 7. MOTTO
**Nu citi lista. Citește ierarhia.**

### 8. FENOMENE (6, pur C11 „a compara")
1. **Clasamentul (ranking):** ordonarea actorilor după o măsură — cine e sus, cine e jos, instant.
2. **Diferența reală vs zgomotul:** contează gap-ul dintre poziții, nu doar ordinea; o diferență poate fi semnal sau cosmetică.
3. **Contribuția / ponderea în total:** cât duce fiecare actor din rezultatul global (share), nu doar valoarea lui.
4. **Concentrarea (Pareto / ABC):** puțini actori duc majoritatea rezultatului; ABC și 80/20 ca instrumente de citire a concentrării.
5. **Comparabilitatea (bază comună):** compari doar ce e comparabil — aceeași unitate, aceeași perioadă, același numitor; altfel clasamentul minte.
6. **Reperul relativ (benchmark):** poziția unui actor capătă sens raportată la alți actori (lider, mediană), nu în absolut.

Instrument tehnic (NU axă): clasamente și contribuție în Power Pivot / Data Model (RANKX, măsuri de % din total, ABC/Pareto ca vehicul DAX). În HTML/FILM rămân referințe generice (R-V02.15 zero cifre business).

EXCLUSE explicit din C11: definirea măsurii în sine (rămâne C10 — C11 compară măsuri deja definite); „de ce / cauza" din spatele ierarhiei și insight-ul verbal (rezervate C12).

### 9. STEP-TITLES (8)
1. Confirmă măsura pe care compari (moștenire C10, single source of truth)
2. Asigură comparabilitatea (aceeași bază, unitate, perioadă)
3. Așază actorii în clasament după măsură
4. Citește diferențele (gap real vs zgomot)
5. Calculează contribuția fiecărui actor în total
6. Identifică concentrarea (Pareto / ABC: cine duce rezultatul)
7. Raportează poziția la un reper relativ (lider / mediană)
8. Confirmă ierarhia decizională (cine contează cu adevărat)

### AHA
**Nu volumul contează, ci ierarhia. Puțini actori duc rezultatul.**

### Schimbare mentală
De la „Cât a făcut fiecare?" la „Care contează cu adevărat?".

### Formula finală
**Măsuri comparabile + clasament + contribuție = ierarhie decizională.**

---

## CONTINUITATE (pentru faza de generare)
- R-V02.14: C11 NU schimbă `valoare_neta`; o ordonează și o agregă în contribuție (sumă conservată). Input C11 = output C10.
- R-V02.15: cifrele trăiesc în Excel; HTML/FILM doar referințe generice (clasament, pondere, concentrare — fără numere business).
- Generare din copy `c01/` (matriță), apoi gate_v20 + audit_sync înainte de livrare.

---

## ÎNTREBĂRI PENTRU BRAIN (înainte de freeze SPEC)
1. **SLUG:** propun `comparatii` (aliniat numelui din hartă „COMPARAȚII"). Confirmi, sau preferi `comparatii-rank` / alt slug?
2. **Număr fenomene:** propun 6 (aliniat cu C10). Confirmi 6 ca țintă T3?
3. **Granița C11↔C12 pe „concentrare":** păstrăm concentrarea (Pareto/ABC) integral în C11 ca FENOMEN, iar C12 ia doar „de ce" cauzal? (Recomand: DA — concentrarea e fapt de ierarhie, nu cauză.)
4. **MOTTO:** propun „Nu citi lista. Citește ierarhia." Confirmi, sau preferi varianta din direcția narativă („Nu toate valorile sunt egale")?

La confirmarea acestor puncte + STATUS `SPEC_FROZEN` în `BRAIN-TO-CLAUDE.md`, trec la `genereaza CNN` (creez `c11/` din copy `c01/`).

---

## CERERI SYSTEM
Nicio cerere SYSTEM deschisă.

### NOTĂ SYSTEM (informativă, nu blocantă pentru C11)
La sync, local main era divergit de `origin/main` (origin force-updated). `origin/main` (canonic) NU conține commit-urile locale C05-C08 re-arhitectură (tip `19efcd5`, lanț: re-arhitectura T2 DICTIONAR/CLASIFICARE, generări C06/C07/C08, film-uri). Le-am lăsat intacte în reflog/istoric local, nu le-am șters. Dacă această absență pe `origin/main` e neintenționată, e o decizie cross-construcție / SYSTEM, în afara mandatului C11 — semnalez doar, nu intervin.
