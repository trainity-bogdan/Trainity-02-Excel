# TRAINITY_ARCHITECTURE_BIBLE.md · Sursa UNICĂ de reguli (T2-T5)

> **STATUT: NORMĂ. SURSĂ UNICĂ DE ADEVĂR.** Orice regulă se enunță integral AICI.
> Detector și Release Gate o REFERĂ prin ID, nu o re-enunță.
> Structură: **§SHARED RULES** (toate treptele) + **§TIER RULES** (per treaptă).
> Pornirea unei trepte noi = moștenești §SHARED + scrii o secțiune §TIER nouă.

---

# §SHARED RULES (se aplică la TOATE treptele, T2-T5)

## REGULI SACRE (nu se încalcă fără aprobarea arhitectului)
- **S1 · Un singur scop per construcție.** O construcție răspunde la O SINGURĂ întrebare.
- **S2 · Garda de treaptă.** Fiecare construcție stă în competența treptei ei; nu predă
  competențe ale treptei următoare, nu reia treapta anterioară. *(Conținutul gărzii =
  în §TIER, pentru că diferă pe treaptă.)*
- **S3 · Invariant de valori sursă.** valoare_neta conservată cap-coadă (R-V02.14);
  zero cifre business în HTML/FILM (R-V02.15).
- **S4 · Schelet fix.** 6 etape · 18 pași · 5 fenomene · 8 verificări finale · 2 prompturi.
- **S5 · Identitate locked.** AHA + numele construcției nu se schimbă fără aprobare.

## REGULI DE PORNIRE A UNEI TREPTE (TIER SEED)
- **R-SEED-1 · Prima construcție = mod TIER SEED.** Moștenește §SHARED, definește §TIER
  (identitate + gardă), sare verificările cross-construction. · CRITICĂ · Obligatorie.
  · Procedura: vezi `TRAINITY_OPERATING_SYSTEM` §TIER SEED.
- **R-SEED-2 · DNA + Position Matrix = post-2-construcții.** Nu se forțează pe prima
  construcție a treptei; se creează retroactiv după a 2-a. · CRITICĂ · Obligatorie.
- **R-SEED-3 · Schelet moștenit, identitate diferită.** O treaptă nouă MOȘTENEȘTE
  scheletul (S4) dar IDENTITATEA ei DIFERĂ de treapta anterioară. Consistența
  structurală = cerută; consistența de identitate = INTERZISĂ. · CRITICĂ · Obligatorie.
- **R-TIER-PARAM · Detector și Gate sunt tier-aware.** Lista de „termeni interziși" e a
  treptei curente (din §TIER), nu hardcodată. Ce e contaminare într-o treaptă e
  competență în alta. · CRITICĂ · Obligatorie.

## REGULI STRUCTURALE (SHARED)
- **R-STR-1 · Cele 6 etape canonice.** REALITATE→INVESTIGAȚIE→TRANSFORMARE→VERIFICARE→
  STABILIZARE→CONFIRMARE, ordine și roluri fixe. · CRITICĂ. · Neconform: 5/7 etape.
- **R-STR-2 · 3 pași/etapă (18 total).** · CRITICĂ.
- **R-STR-3 · 5 fenomene SCENA.** · MEDIE.
- **R-STR-4 · Meniu mobil fără bandă nav-brand** (R-V03.73, automat). · MEDIE.

## REGULI TERMINOLOGICE (SHARED)
- **R-TERM-1 · Etapa 4 = „VERIFICAREA [obiect]".** Niciodată „AUDIT" (= ADN C03). ·
  CRITICĂ. · Conform: „VERIFICAREA CRONOLOGIEI". · Neconform: „AUDIT AL REGULILOR".
- **R-TERM-2 · phase-tag E5 = „RECALCUL".** Niciodată „RECALC". · MEDIE.
- **R-TERM-3 · „auditabil" permis** (adjectiv = verificabil; nu se confundă cu „AUDIT").
- **R-TERM-5 · Fără ecouri C04** („Suma rămâne conservată/martorul de sumă") în copy;
  conservarea trăiește în Excel (S3). · MEDIE.
- **R-TERM-6 · Fără em/en-dash** (R-V03.72, automat). · MEDIE.
- **R-NAME-1 · Nume construcție = LOCK.** Numele istorice (TIPIZARE etc.) abandonate. · CRITICĂ.
- **R-TEASER-1 · Teaserul poate numi construcția+treapta următoare**, inclusiv termeni ai
  treptei superioare, dacă e explicit „C0(N+1) deschide...". NU contaminează. · Clarificare.

> **NOTĂ:** interdicțiile terminologice CONCRETE (ce termeni sunt interziși) trăiesc în
> §TIER, pentru că diferă pe treaptă (R-TIER-PARAM). §SHARED stabilește doar disciplina.

## REGULI PEDAGOGICE (SHARED)
- **R-PED-1 · Etapa 3 e AI-assisted.** type-tag E3 = „Promptul 2"; formula = output-ul
  promptului, nu muncă manuală. · MAJORĂ.
- **R-PED-2 · Două prompturi AI/construcție** (Promptul 1 etapa 2, Promptul 2 etapa 3). · MEDIE.
- **R-PED-3 · Promptul = interogare, nu execuție.** · Recomandată.

## REGULI METODOLOGICE (SHARED)
- **R-MET-1 · Etapa 4 verifică, nu construiește.** Pașii E4 CONFRUNTĂ/VERIFICĂ/MARCHEAZĂ;
  nu construiesc livrabilul. · MAJORĂ. · *Încălcată azi de C06 (E4 construiește) → decizie
  arhitecturală deschisă.*
- **R-MET-2 · Verificare prin confruntare cu setul** („Nu avem încredere oarbă..."). · MEDIE.
- **R-MET-3 · Funcții de verificare pe axă = variație acceptabilă** (UNIQUE vs MIN/MAX vs
  COUNTIF, după tipul de date). · Clarificare.

## REGULI DE HANDOFF (SHARED)
- **R-HAND-1 · Intrare explicită.** PAS 01: „Setul predat de C0(N-1) [stare]". · MAJORĂ.
- **R-HAND-2 · Ieșire + teaser.** „Predă către C0(N+1)... C0(N+1) deschide [axa]." · MEDIE.
- **R-HAND-3 · Stare moștenită corectă.** · Obligatorie.

## REGULI PHASE-TAG / COMPLETION (SHARED)
- **R-PHASE-1 · Phase-tags fixe:** E1=INPUT, E2=AI, E4=CONTROL, E5=RECALCUL, E6=PAYOFF. · MEDIE.
- **R-PHASE-2 · E3 phase-tag variabil pe axă** (din familia transformării). · *decizie deschisă:
  Power Query trage spre treaptă superioară.*
- **R-COMP-1 · completion-title = „[Livrabil] validat"**, fără adjective suplimentare. · MEDIE.

---

# §TIER RULES

## §T2 — CUNOAȘTERE (descrie, nu interpretează)
- **Axă:** setul devine CUNOSCUT. C05 vocabular · C06 sens · C07 calendar · C08 context.
- **Întrebări:** „Ce există?" / „Ce înseamnă fiecare rând?" / „Când se întâmplă?" / „Cu cine se leagă?"
- **GARDA T2/T3 (lista de interziși pentru R-TIER-PARAM):** trend, performanță, prioritizare,
  decizie, comparație, „cel mai mare/mic", dominant, prioritar/strategic/critic, join, Data
  Model, XLOOKUP/LOOKUP ca aducere, „conectat/conexiune", Power Query (ca operațiune),
  BI-ready, KPI. Toate = T3/T4. · Excepție: teaser explicit (R-TEASER-1).
- **AHA locked:** C05 „Nu cunoști un set până nu-l poți enumera." · C06 „Un rând nu are
  sens până nu primește o regulă." · C07 „Un set fără poziție în timp e un set fără
  memorie." · C08 „Cele mai importante date despre un rând nu sunt în rând."
- **Detaliu complet:** `_system/11-ARHITECTURA-CONCEPTUALA-T2.md` (autoritate conceptuală T2).

## §T3 — ANALIZĂ (inițiată prin TIER SEED la C09 · aprobat ARHITECT V58)
- **Axă:** setul cunoscut (T2) devine INTERPRETAT. T3 = ANALIZĂ.
- **Ce produce T3:** relații reale, măsuri, comparații, interpretare; răspuns la „de ce /
  cât / care e mai mare / care e mai bun".
- **Ce NU produce T3:** vizualizare/dashboard/raport (= T4 RAPORTARE), decizie/acțiune
  automată/recomandare executată (= T5 AUTOMATIZARE).
- **Lanț (provizoriu, rafinabil):** C09 RELAȚII · C10 MĂSURI · C11 COMPARAȚII · C12 INTERPRETARE.
- **Întrebări:** C09 „Cum se leagă datele într-un model pe care pot să-l interoghez?" *(C10-C12 la SEED-ul lor.)*
- **GARDA T3/T4-T5 (lista pentru R-TIER-PARAM):**
  - **PERMIS** (competența T3, era INTERZIS în T2): join, Data Model, relații 1:M, merge,
    măsuri/agregări peste model, comparații, trend, performanță, „cel mai mare/mic",
    „care e mai bun", interpretare, citire cross-tabel.
  - **INTERZIS** (= T4/T5): dashboard, vizualizare, grafic publicabil, raport (T4); decizie
    automată, alertă, acțiune, recomandare executată (T5).
- **AHA locked (S5):** C09 „Fără relații ai date. Cu relații ai răspunsuri."
- **NOTĂ inversiune:** termenii din garda §T2 (join/Data Model/trend/„cel mai mare") sunt
  AICI competență, nu contaminare. Detectorul tier-aware (R-TIER-PARAM) îi tratează corect.

## §T4 — RAPORTARE · §T5 — AUTOMATIZARE
- *Goale. Se completează prin TIER SEED la prima construcție a fiecărei trepte.*

---

# BACKLOG DECIZII (reguli candidate, ÎNCĂ NEDECISE — NU sunt norme)
> Aici trăiesc regulile propuse dar nedecise. NU se aplică la audit până nu sunt aprobate
> și mutate sus. Se decid în runda DEZAMBIGUIZARE.
- **(pending) Payoff specific, nereutilizabil** între construcții. *(Neverificabil mecanic;
  decizie DEZAMBIGUIZARE.)*
- **(pending) WOW cu deschidere distinctă** între construcții. *(idem.)*
- **(pending) Motto cu terminație distinctă** (C05↔C06 „Apoi orice decizie").
