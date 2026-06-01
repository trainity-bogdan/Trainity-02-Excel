# Harta construcțiilor · T1 → T5

Cele 20 de construcții mapate pe 5 trepte SCARA. Status actual + axă + identitate.

---

## Privire generală — SCARA cele 5 trepte

| Treapta | Cod | Nume | Construcții | Tehnologie dominantă | Status |
|---|---|---|---|---|---|
| T1 | **SCAN** | STRUCTURA | C01-C04 | Excel basic + AGGREGATE + Power Query (Promoted Headers, Filtered Rows) | ✓ COMPLET LIVRABIL |
| T2 | **CUNOAȘTERE** | CUNOAȘTERE | C05-C08 | Excel (UNIQUE, IFS/SWITCH/XLOOKUP, funcții dată, lookup) + Power Query | ✓ COMPLET LIVRABIL |
| T3 | **ANALIZA** | ANALIZA | C09-C12 | Power Pivot + Data Model | NESTAR |
| T4 | **RAPORTARE** | RAPORTARE | C13-C16 | Dashboards + BI UX | NESTAR |
| T5 | **AUTOMATIZARE** | AUTOMATIZARE | C17-C20 | Power Query Refresh + Operational Flows | NESTAR |

---

## TREAPTA 1 · SCANARE · STRUCTURA

**Promisia pedagogică:** transformă exporturile ERP brute în baze curate, controlabile, BI-ready. Operatorul recunoaște fenomenele structurale care contaminează datele și le neutralizează prin uneltele native Excel + Power Query.

**Tehnologie:** Excel basic (AutoFilter, AGGREGATE, IFERROR), Power Query (Promoted Headers, Filtered Rows, Removed Top Rows, Removed Blank Rows, Removed Duplicates).

### C01 · STRUCTURARE ✓

| Aspect | Conținut |
|---|---|
| **INTRIGA** | Arată ca tabel. Nu este unul. |
| **MIZA** | Decizii ancorate în date care doar par tabel. |
| **MANTRA** | Înainte de orice calcul, structura. |
| **MOTTO** | Nu reconstruim tabelul. Îl facem controlabil. |
| **WOW (PAYOFF)** | Tabelul nu mai pare curat. Este demonstrabil curat. |
| **FENOMENE** | 7 fenomene structurale: header 3-etaj merged, SUBTOTAL/TOTAL parazite, coloană ascunsă fizic, blank rows separator, cell-merging chaotic, AutoFilter+SUM eronat, AGGREGATE modern (leac) |
| **Date_MASTER** | 2062 rd × 16 col → 2001 rd × 14 col după curățare |
| **Sumă conservată** | 7.986.019,38 lei |
| **Status** | LIVRABIL CANONIC V12 (matriță pentru toate celelalte) |

### C02 · CONTROL — CORESPONDENȚA CU REALITATEA (IDENTITATE LOCK V58)

| Aspect | Conținut |
|---|---|
| **TEMA** | CORESPONDENȚA CU REALITATEA |
| **AHA (lock)** | Valid nu înseamnă corect. |
| **Regula oficială** | Excel acceptă valoarea. Business-ul trebuie să o investigheze. *(Reclamantul = omul → C02; reclamantul = motorul Excel → C03.)* |
| **Competență** | Identific valori pe care Excel le acceptă, dar care încalcă reguli ale lumii reale. |
| **Filozofia** | C02 NU repară / NU șterge / NU modifică / NU decide / NU previne. Semnalează și construiește dovezi pentru o decizie de business. |
| **MANTRA** | Înainte de orice raport, controlul. |
| **MOTTO** | Nu reconstruim tabelul. Îl facem controlabil. |
| **FENOMENE (5 anomalii LOCK)** | 1. Orașe nealiniate (nomenclator) · 2. CNP invalid (ICONIC) · 3. TVA greșit (regulă fiscală) · 4. Dată în viitor (regulă temporală) · 5. Vânzare în zi închisă (regulă operațională) |
| **Instrumente** | Advanced Filter = DESCOPERIRE (valori unice, excepții, nomenclatoare) · Conditional Formatting = SEMNALIZARE · Data Validation = FORMALIZARE (marginală, DOAR după decizia business; NU e competența, NU e tema). |
| **Delimitare C02↔C03** | C02 = greșit față de REALITATE (Excel acceptă, omul contestă). C03 = greșit față de MOTORUL Excel (omul acceptă, Excel contestă). Criteriu: *cine reclamă eroarea.* |
| **Status** | **IDENTITATE LOCK V58.** Implementare HTML + Date_MASTER: **PENDING** — corpul actual al c02/ e încă versiunea veche „MARCARE" (36 anomalii structurale). Numele de fișier (`02-Marcare`) + identitatea HTML se aliniază la implementare. |

> **CNP = EXEMPLU ICONIC (statut special, decizie ARHITECT V58).**
> CNP NU e ales pentru că există în Date_MASTER (setul e B2B, nu are coloană CNP) — e ales ca **cea mai memorabilă demonstrație a principiului „valid ≠ corect"**: 13 cifre, arată perfect, Excel nu reclamă nimic, și totuși cifra de control e greșită / data încorporată e imposibilă → identificator invalid.
>
> **REGULĂ ANTI-DRIFT CNP:** rămâne strict în registrul „arată perfect și totuși e fals" (**cifră de control + dată imposibilă**). NU se folosește lungime≠13 / caractere alfabetice / erori de format ca element central — acelea sunt **C03-adjacent**. NU se mută CNP în C03. NU devine exercițiu de validare tehnică.
>
> **Ancora de memorabilitate:** după luni/ani, cursantul trebuie să-și amintească spontan „CNP-ul părea perfect și totuși era fals." Rezultat C02: *„Excel acceptă datele. Eu nu le cred până nu le verific împotriva realității."*

### C03 · AUDITARE ✓

| Aspect | Conținut |
|---|---|
| **TITLU (cover)** | Cum auditezi ce nu se vede în date (V50: era „Cum construim un audit valoric" — prea contabil/vag) |
| **INTRIGA** | Tabelul controlat valoric pare gata. Contaminările tehnice îl blochează. (bombă Studiu: „Arată curat. Nu este.") |
| **MIZA** | VLOOKUP, XLOOKUP, MATCH eșuează silentios pe contaminări invizibile. Formulele, rapoartele și AI-ul lucrează pe o minciună tehnică. |
| **MANTRA** | Înainte de orice analiză, auditul tehnic. |
| **MOTTO** | Auditam ce nu se vede. |
| **FENOMENE** | 5 categorii × 110 fiecare = 550 contaminări: whitespace invizibil (trailing spaces), Unicode/ZWSP/SHY, numere ca text (blocheaza SUM), date ca string (blochează filtru), trailing newlines. |
| **Date_MASTER** | C03 input cu 550 contaminări planted, output curat |
| **Sumă conservată** | DELTA 0 (audit non-distructiv) |
| **Status** | LIVRABIL CANONIC V26 |

**⚠️ GRANIȚĂ C03/C04 (rescope V50, feedback extern prin G-06):** C03 = **demonstrează + audit + dovadă + conservare**. Auditul e repetabil ca **VERIFICARE** (îl re-rulezi pe un export nou ca să confirmi dacă datele sunt curate), non-distructiv, DELTA 0. C03 **NU** construiește mecanismul permanent refreshabil — îl predă explicit lui C04. C04 = **mecanismul permanent** (Refresh All, pași PQ versionați, documentat). Markeri care NU au voie în C03: „flux refreshabil", „Refresh activ", „fluxul muncește pentru noi", „protocol permanent" (toate = teritoriu C04). Driftul empiric (V50): etapa 5 STABILIZARE + prompt 2 + outcomes revendicaseră fluxul permanent → corectat.


### C04 · NORMALIZARE ✓

| Aspect | Conținut |
|---|---|
| **INTRIGA** | Auditul a arătat unde sunt contaminările. Acum aplicăm fix-ul. |
| **MIZA** | Curățare manuală nu se reproduce luna viitoare. Power Query da. |
| **MANTRA** | Înainte de orice raport, normalizarea reproductibilă. |
| **MOTTO** | Nu curățăm de mână. Construim fluxul. |
| **FENOMENE** | 10 transformări Power Query canonice: Promoted Headers, Filtered Rows (SUBTOTAL+TOTAL), Removed Blank Rows, Removed Duplicates, Removed Other Columns, Changed Type, Trim & Clean Text, Parsed Date, Normalized Diacritics, Loaded as Excel Table |
| **Date_MASTER** | C04 input cu contaminări, output `Vanzari_Normalizat` Excel Table |
| **Sumă conservată** | DELTA 0 |
| **Status** | LIVRABIL CANONIC V27 |

---

## TREAPTA 2 · CUNOAȘTERE

**Promisia pedagogică:** transformă tabelul normalizat într-un set CUNOSCUT — operatorul știe ce conține, ce categorii, ce cifre, ce trend-uri. Profilare descriptivă, NU KPI business.

**Lecția L139:** Această treaptă a fost redenumită V24 din "CALCUL" în "CUNOAȘTERE" — pentru că nu calculăm KPI-uri (care vine la T3 ANALIZA), ci cunoaștem setul descriptiv.

**Tehnologie:** Excel + Power Query (Group By, Pivot, Distinct, Top N).

### C05 · DICȚIONAR ✓

| Aspect | Conținut |
|---|---|
| **AXA** | DICȚIONAR — ce reprezintă datele (inventar categorii, cardinalități, granularitate) |
| **INTRIGA** | Tabelul este curat. Dar știm ce conține? |
| **MIZA** | Transformă tabelul curat într-un teritoriu pe care îl poți enumera. |
| **MANTRA** | Nu privim tabelul. Îl interogăm. |
| **MOTTO** | Un set cunoscut. Apoi orice decizie. |
| **WOW** | Setul nu mai este o masă de date. Acum are hartă. |
| **FENOMENE** | 5 fenomene calitative (inventar dicționar): cardinalitate clienți, categorii, cantități, top frecvențe (Pareto), granularitate atomică |
| **Sumă conservată** | DELTA 0 |
| **Status** | LIVRABIL V53 (rename din CLASIFICARE; conținut = inventar; copy ascuțit G-06) |

**Poziționare (graniță valoare narativă):** C01-C04 răspund la „pot avea încredere în set?" (structură, control, audit, normalizare). C05 răspunde la o întrebare fundamental diferită: „știu ce există în set?". Nu descoperă etichete izolate, ci universul setului — îl transformă dintr-o masă de date într-un teritoriu cartografiat, enumerabil. C05 = poarta către T2 (Cunoaștere).

### C06 · CLASIFICARE ✓

| Aspect | Conținut |
|---|---|
| **AXA** | CLASIFICARE — cum capătă sens datele (reguli, etichetare descriptivă) |
| **OBIECT** | clasa / regula / scorul |
| **ÎNTREBARE-MAMĂ** | Cum capătă sens datele? |
| **INTRIGA** | Setul are clase ascunse. Excel le poate construi. Tu nu le-ai scris. |
| **MARKER** | clasă / regulă / scor |
| **FENOMENE** | clasa ABC (IFS pe valoare_neta), segment (SWITCH pe categorie), etichetă externă (XLOOKUP din nomenclator), regulă compusă (IFS condiții multiple), scor 0-100 |
| **Date_MASTER** | coloane derivate clasa_valoare/segment_produs/scor + sheet-uri _CLASE/_SEGMENTE/_SCORURI |
| **Garda T2/T3** | atribuie etichete descriptiv; prioritizarea strategică pe segmente = C11/T3 |
| **Status** | LIVRABIL V44 (rebuild din CUANTIFICARE) |

> **NOTĂ ANTI-REDRIFT (lock V58, după L186 repetat de 3x).** C06 **ESTE CLASIFICARE**, decizie definitivă confirmată de ARHITECT. NU este „profil numeric / KPI / sume-medii-distribuții" — aceea era harta T2 **pre-V45** (C06 = CUANTIFICARE), abandonată la rebuild-ul V45 tocmai ca să elimine suprapunerea cu C05. Orice feedback extern care cere „C06 = profil numeric" lucrează pe harta veche și se RESPINGE (G-06 CONFLICT). C06 produce **etichete operaționale prin reguli** (clasă/segment/scor), NU decizii business. Limbaj INTERZIS în C06 (mută în T3/C11): „prioritar", „critic", „strategic", „irelevant", „valoros", „important pentru business". **Formula de control:** C05 = ce există · C06 = ce înseamnă fiecare rând · C07 = când se întâmplă · C08 = cu cine se leagă.

### C07 · DATARE ✓

| Aspect | Conținut |
|---|---|
| **AXA** | TEMPORALĂ DESCRIPTIVĂ — „când se întâmplă fiecare rând" (atașarea timpului, NU analiza lui) |
| **OBIECT** | calendarul setului |
| **ÎNTREBARE-MAMĂ** | Când se întâmplă fiecare rând? |
| **INTRIGA** | Setul are memorie. Excel o ține minte. Tu nu i-ai citit-o. |
| **MARKER** | calendar / poziție temporală |
| **FENOMENE** | perioada reală (prima→ultima dată, MIN/MAX), granularitate temporală (zi/lună/trimestru/an/zi a săptămânii derivate), acoperire temporală (luni prezente/lipsă, goluri), calendar operațional (sezon, perioadă comercială, weekend vs zi lucrătoare), fișa temporală (_TIMELINE auditabil) |
| **Garda T2/T3** | C07 ATAȘEAZĂ timpul (descriptiv); interpretarea lui = T3. INTERZIS în C07: trend, direcție, accelerare, încetinire, delta, evoluție, creștere/scădere, comparație lună-la-lună, lună-vârf/minim, zi dominantă/predilectă, săptămână tipică, performanță temporală. Acestea migrează în T3. |
| **LIVRABIL** | Calendarul setului (fișa temporală) |
| **Status** | LIVRABIL V44 · DATARE PURĂ (lock V58: trend/direcție/accelerare scoase în T3, decizie fermă ARHITECT) |

> **NOTĂ ANTI-REDRIFT C07 (lock V58).** C07 răspunde EXCLUSIV la „când se întâmplă fiecare rând", NU la „ce se întâmplă în timp / cum evoluează". Regula de aur: C07 atașează timpul, T3 interpretează timpul. C07 = calendarul setului; T3 = analiza calendarului. „Ritm" se folosește doar reformulat ca „granularitate" / „frecvență calendaristică", fără dominantă/comparație. Sheet `_TREND` (delta+direcție) a fost ELIMINAT din Date_MASTER; rămân `_TIMELINE` / `_CALENDAR` / `_SEZON` (datare pură).

### C08 · CARTOGRAFIERE ✓

| Aspect | Conținut |
|---|---|
| **AXA** | RELAȚIONALĂ DESCRIPTIVĂ — „cu cine se leagă fiecare rând / unde trăiește contextul" (RECUNOAȘTERE, nu modelare) |
| **OBIECT** | contextul / harta surselor |
| **ÎNTREBARE-MAMĂ** | Cu cine se leagă fiecare rând? |
| **INTRIGA** | Te uiți la un tabel întreg. Jumătate din el e în altă parte. |
| **MARKER** | hartă / satelit / cheie / rol / câmp extern |
| **AHA oficial (lock V58)** | Cele mai importante date despre un rând nu sunt în rând. |
| **FENOMENE** | ce seturi-satelit există în jur (CLIENTI/PRODUSE/AGENTI/DEPOZITE), rolul fiecăruia (fapt vs descriere), ce chei sunt comune, ce câmpuri externe trăiesc doar în sateliți, ce convenții diferă (limbi diferite) |
| **Garda T2/T3** | C08 LOCALIZEAZĂ contextul (descriptiv), NU îl aduce. INTERZIS în C08: XLOOKUP/LOOKUP/join/aducere de valori, Data Model, relații activate, măsuri, conectat/conexiune, BI-ready. Acestea = C09/T3/T4. |
| **LIVRABIL** | Harta ecosistemului de date (`_ECOSISTEM`) |
| **Status** | LIVRABIL · CARTOGRAFIERE (nume LOCK V58). Premium + identitate rafinată + hero dedicat. Închide T2. |

**Delimitare obsesivă C08 ↔ C09 (T2 vs T3):**
C08 **cartografiază**, NU unește. C08 = *vezi relațiile posibile* (recunoaștere
descriptivă). C09 (T3) = *construiești relațiile reale* (merge, append, 1:M,
Data Model, măsuri, analiză prin relații). Tot ce e join/model/măsură →
teritoriu C09. C08 doar recunoaște ecosistemul; C09 îl activează.

---

## TREAPTA 3 · ANALIZARE (C09-C12)

**Promisia pedagogică:** transformă datele, cunoașterea, în insight, prioritizare, decizie. Datele încep să spună povestea business-ului.

**Tehnologie dominantă:** Power Pivot + Data Model (Pivot Tables, DAX measures, relații).

| Construcție | Tema posibilă | Status |
|---|---|---|
| C09 | Relații între seturi — ACTIVAREA ecosistemului recunoscut în C08 (merge/1:M/Data Model) | NESTAR |
| C10 | KPI-uri compozite cu DAX | NESTAR |
| C11 | Prioritizare (ABC analysis, Pareto avansat) | NESTAR |
| C12 | What-if analysis (scenarii business) | NESTAR |

**T3 e închidere treaptă:** la C12 se închide blocul ANALIZA cu vocabular pedagogic ("am completat analiza setului, treapta T3 finalizată") conform R-V02.7.

---

## TREAPTA 4 · RAPORTARE (C13-C16)

**Promisia pedagogică:** transformă analiza în dashboard-uri executive, cockpit-uri, control vizual.

**Tehnologie dominantă:** Dashboards, BI UX (charts, slicers, scorecards, narrative BI, visual hierarchy).

| Construcție | Tema posibilă | Status |
|---|---|---|
| C13 | Dashboard executiv 1-page | NESTAR |
| C14 | Cockpit operațional cu drill-down | NESTAR |
| C15 | Narrative BI (storytelling cu date) | NESTAR |
| C16 | Scorecard ierarhic + alerte | NESTAR |

**T4 e închidere treaptă** la C16.

---

## TREAPTA 5 · AUTOMATIZARE (C17-C20)

**Promisia pedagogică:** transformă raportarea într-un sistem autonom, repetabil, predictibil, scalabil.

**Tehnologie dominantă:** Power Query Refresh Architecture + Operational Flows.

| Construcție | Tema posibilă | Status |
|---|---|---|
| C17 | Refresh All architecture | NESTAR |
| C18 | Operational flows recurente | NESTAR |
| C19 | Sistem de alerte automate | NESTAR |
| C20 | Sistem complet end-to-end | NESTAR (CONSTRUCȚIA SEMNĂTURĂ) |

**T5 e închidere PACK** la C20 cu sumarul pedagogic complet.

---

## Continuitate cap-coadă între construcții

**Principiul R-V02.14:** suma valoare_neta se conservă cap-coadă. Output C{N} = Input C{N+1}.

```
Date_MASTER-initial  →  C01  →  C02  →  C03  →  C04  →  C05  →  C06 → ... → C20
   7.986.019,38         7.986.019         8.018.087    7.986.019    7.986.019
                       (curat                          (+32K duplicat)
                        structural)                    (-32K)
```

**Excepție explicită:** C02 elimină 10 duplicate planted cu valoare totală +32K, recuperată în C04 după Removed Duplicates.

**Verificare:** sheet `CONTROL_FINAL` în fiecare Date_MASTER-CNN.xlsx menționează suma conservată.

---

## Identitate cinematică per axă

**T1 SCAN — voce structurală**, fenomene fizice ale tabelului:
- Toate cele 4 construcții au INTRIGA pe "pare X, nu este X"
- Voce: "nu reconstruim, facem controlabil"

**T2 CUNOAȘTERE — voce profilare descriptivă**:
- C05 axa DICȚIONAR (ce reprezintă): "setul are un dicționar"
- C06 axa CLASIFICARE (cum capătă sens): "setul are clase ascunse" — reguli IFS/SWITCH/XLOOKUP/scor
- C07 axa temporală (memorie): "setul are memorie"
- C08 axa relațională descriptivă (ecosistem): "setul are un ecosistem" — RECUNOAȘTERE, nu modelare (modelarea = C09/T3)
- Cele 4 obiecte: dicționar (CE reprezintă) · clasificare (CUM capătă sens) · memorie (CÂND) · ecosistem (CU CINE)
- Voce: "nu privim, interogăm"

**T3 ANALIZA — voce decizională**:
- Cifrele devin insight
- Voce: "decizia stă în relații, nu în volum"

**T4 RAPORTARE — voce executive**:
- Raportul devine interfață
- Voce: "dashboard-ul nu e document, e cockpit"

**T5 AUTOMATIZARE — voce sistemică**:
- Refresh devine ritual
- Voce: "nu rebuild luna viitoare. Apăs Refresh."

---

## Status detailed cu data ultimei modificări

| Construcție | Versiune | Stare | Ultima modificare | Audit |
|---|---|---|---|---|
| C01 | V12 | LIVRABIL canonic+editat | 27 mai 2026 (V34) | ✓ ZERO DRIFT |
| C02 | V26 | LIVRABIL canonic+editat | 27 mai 2026 (V38) | ✓ ZERO DRIFT |
| C03 | V26 | LIVRABIL canonic+editat | 27 mai 2026 (V38) | ✓ ZERO DRIFT |
| C04 | V27 | LIVRABIL canonic+editat | 27 mai 2026 (V38) | ✓ ZERO DRIFT |
| C05 | V28 | LIVRABIL canonic+editat | 27 mai 2026 (V38) | ✓ ZERO DRIFT |
| C06-C20 | — | NESTAR | — | — |

**Sumar:** 5 din 20 construcții live (25%). T1 + C05 complete. T2 restul + T3-T5 în queue.

---

## Calea de evoluție pe care o anticipez

1. **C06-C08 generate** sub schema V38+ (canonic+editat automat la prima rulare)
2. T2 încheiat complet
3. **T3 ANALIZA** începe cu C09 — primul SPEC cu axă DAX
4. La C13 (T4) se introduce un nou tip de livrabil: **dashboard XLSX** (Power Pivot + Pivot Tables vizibile)
5. La C20 (semnătura pack-ului) avem un livrabil bonus: **SISTEMUL COMPLET** funcțional Refresh All

**La C20 pack-ul Pack 02 Excel e gata.** Total: ~140 livrabile (20 × 7 artefacte) + sistemul de generare reutilizabil.
