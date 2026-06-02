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

### C02 · MARCARE ✓

| Aspect | Conținut |
|---|---|
| **INTRIGA** | Tabelul cu date pare curat. Datele însă mint. |
| **MIZA** | Datele predate ca "curate structural" încă mint operațional. |
| **MANTRA** | Înainte de orice raport, controlul. |
| **MOTTO** | Nu reconstruim tabelul. Îl facem controlabil. |
| **FENOMENE** | 5 categorii anomalii: facturi datate în viitor (5), coduri client inexistente (8), duplicate exacte (10), vânzări sâmbătă pe filiala L-V (6), câmpuri obligatorii goale (7). Total: 36 anomalii. |
| **Date_MASTER** | C02 input cu cele 36 anomalii planted, output cu coloana STATUS + MOTIV |
| **Sumă conservată** | 8.018.087,99 lei (suma input cu duplicate planted) |
| **Status** | LIVRABIL CANONIC V26 |

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
| **TITLU (cover)** | Cum construim un flux care normalizează automat (model premium V50) |
| **INTRIGA** | Fișierul curat nu e rezultatul. Fluxul este. (bombă Studiu) |
| **MIZA** | Curățare manuală nu se reproduce luna viitoare. Power Query da. |
| **MANTRA** | O dată construit. De fiecare dată identic. |
| **AHA** | Munca pe care o repeți la fiecare export nu trebuia făcută de mână niciodată. |
| **WOW** | Sursa nouă vine. Apăsăm Refresh. Totul se reconstruiește singur. |
| **MOTTO** | Nu curățăm de mână. Construim fluxul. |
| **FENOMENE** | 10 transformări Power Query canonice: Promoted Headers, Filtered Rows (SUBTOTAL+TOTAL), Removed Blank Rows, Removed Duplicates, Removed Other Columns, Changed Type, Trim & Clean Text, Parsed Date, Normalized Diacritics, Loaded as Excel Table |
| **Date_MASTER** | C04 input cu contaminări, output `Vanzari_Normalizat` Excel Table |
| **Sumă conservată** | DELTA 0 |
| **Status** | LIVRABIL CANONIC V27 → model premium V50 (hero cockpit + arc TU + transformare-section gated) |

---

## TREAPTA 2 · CUNOAȘTERE

**Promisia pedagogică:** transformă tabelul normalizat într-un set CUNOSCUT — operatorul știe ce conține, ce categorii, ce cifre, ce trend-uri. Profilare descriptivă, NU KPI business.

**Lecția L139:** Această treaptă a fost redenumită V24 din "CALCUL" în "CUNOAȘTERE" — pentru că nu calculăm KPI-uri (care vine la T3 ANALIZA), ci cunoaștem setul descriptiv.

**Tehnologie:** Excel + Power Query (Group By, Pivot, Distinct, Top N).

### C05 · DICȚIONAR ✓

| Aspect | Conținut |
|---|---|
| **AXA** | DICȚIONAR — ce reprezintă datele (inventar categorii, cardinalități, granularitate) |
| **INTRIGA** | Setul are un dicționar. Excel îl știe. Tu nu. |
| **MIZA** | Decizii pe categorii pe care nu le cunoști exhaustiv. |
| **MANTRA** | Nu privim tabelul. Îl interogăm. |
| **MOTTO** | Un set cunoscut. Apoi orice decizie. |
| **FENOMENE** | 5 fenomene calitative (inventar dicționar): cardinalitate clienți, categorii, cantități, top frecvențe (Pareto), granularitate atomică |
| **Sumă conservată** | DELTA 0 |
| **Status** | LIVRABIL V44 (rename din CLASIFICARE; conținut = inventar) |

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

### C07 · DATARE — MEMORIA SETULUI (PROPUS, AXĂ LOCK V43)

| Aspect | Conținut |
|---|---|
| **AXA** | TEMPORALĂ (unică pe treaptă) — „cum se mișcă setul în timp" |
| **OBIECT** | memoria |
| **ÎNTREBARE-MAMĂ** | Cum se comportă setul în timp? |
| **INTRIGA propusă** | Setul are memorie. Excel o ține minte. Tu nu. |
| **MARKER** | memorie |
| **FENOMENE propuse** | perioada reală acoperită (prima→ultima lună), goluri în timp (luni lipsă), ritmul/volumul pe lună, luna dominantă, accelerare/încetinire (trend), sezonalitate (recurență), săptămâna tipică |
| **LIVRABIL** | Fișa temporală a setului (Memoria setului) |
| **Status** | LIVRABIL V44 |

### C08 · TIPIZARE — HARTA ECOSISTEMULUI (PROPUS, AXĂ LOCK V43)

| Aspect | Conținut |
|---|---|
| **AXA** | RELAȚIONALĂ DESCRIPTIVĂ — „cu cine vorbește setul" (RECUNOAȘTERE, nu modelare) |
| **OBIECT** | ecosistemul |
| **ÎNTREBARE-MAMĂ** | Cu cine vorbește setul? |
| **INTRIGA propusă** | Setul are un ecosistem. Excel îl vede. Tu nu. |
| **MARKER** | ecosistem / satelit / cheie / rol / câmp extern |
| **FENOMENE propuse** | ce seturi-satelit există în jur (CLIENTI/PRODUSE/AGENTI/DEPOZITE), rolul fiecăruia (fapt vs descriere), ce chei par comune (cod_client, cod_produs), ce câmpuri lipsesc din setul principal dar există în sateliți, ce convenții diferă și trebuie aliniate înainte de modelare |
| **LIVRABIL** | Harta ecosistemului de date |
| **Status** | LIVRABIL V44 (închide T2) |

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
