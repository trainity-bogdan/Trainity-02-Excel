# D2 · `Vanzari` CURAT (corpul coerent, fără anomalii)

> Pasul D2 din `PLAN-EXECUTIE-C02.md`. Construiește REALITATEA: setul 100% coerent.
> NU anomalii (vin în D4), NU semnalizări/CF/AF/DV, NU formule de detecție (vin în D5).
> Pereche cu `D1-NOMENCLATOARE-C02.md` (sursele de adevăr, LOCK).
> Acoperă C02.01-04 (geografie, TVA, scadență, calendar). C02.05 CNP = `CONTACTE`, la D3.

---

## 1. STRUCTURA FINALĂ a foii `Vanzari`

> În D2 foaia conține DOAR coloane de INPUT. Coloanele de semnalizare (`flag_*`,
> `status_validare`, `motiv_anomalie`) se adaugă la D5 — NU acum.

| # | Coloană | Stare | Tip | Rol în model |
|---|---|---|---|---|
| 1 | `nr_factura` | existentă | text | identificator tranzacție |
| 2 | `data_factura` | existentă | dată | data emiterii (ancoră C02.04) |
| 3 | `client_nume` | existentă | text | clientul (FK către `CONTACTE` la D3) |
| 4 | `judet` | existentă | text | județul tranzacției (pereche cu `oras` — C02.01b) |
| 5 | **`oras`** | **NOUĂ** | text | orașul declarat (ancoră C02.01) |
| 6 | `cod_produs` | existentă | text | cod produs |
| 7 | `produs_nume` | existentă | text | denumire produs |
| 8 | `categorie` | existentă | text | categoria (ancoră C02.02, cheie către `tbl_RegulriTVA`) |
| 9 | `cantitate` | existentă | număr | cantitate |
| 10 | `pret_unitar` | existentă | număr | preț unitar |
| 11 | `valoare_neta` | existentă | număr | baza fără TVA (**INVARIANT R-V02.14**) |
| 12 | `cota_tva` | existentă | procent | cota aplicată (ancoră C02.02) |
| 13 | `valoare_tva` | existentă | număr | TVA calculat |
| 14 | `valoare_totala` | existentă | număr | net + TVA |
| 15 | `moneda` | existentă | text | RON |
| 16 | **`data_scadentei`** | **NOUĂ** | dată | scadența facturii (ancoră C02.03) |

**Coloane noi: 2** (`oras`, `data_scadentei`). Restul = existente, păstrate.

---

## 2. DE CE EXISTĂ fiecare coloană nouă (rațiune, nu conținut)

**`oras`** — județul (`judet`) exista deja, dar județul singur nu poate purta anomalia de nomenclator. Localitatea e nivelul la care apar cele două forme de fals valid din C02.01: (a) aceeași localitate scrisă în mai multe feluri și (b) o localitate plasată într-un județ în care nu există. Fără o coloană `oras` distinctă de `judet`, nu există obiect pe care AF să descopere nomenclatorul real și pe care confruntarea oraș↔județ să se aplice. `oras` e purtătorul fenomenului geografic.

**`data_scadentei`** — `data_factura` exista, dar o singură dată nu poate exprima o ordine imposibilă. C02.03 e despre RELAȚIA cronologică dintre două date ale aceleiași facturi: emiterea și scadența. Ai nevoie de a doua dată ca să poată exista perechea în care „ambele valori sunt valide, dar ordinea lor e imposibilă". `data_scadentei` e a doua ancoră temporală fără de care fenomenul de cronologie nu are suport.

---

## 3. REGULI DE GENERARE pentru setul 100% COERENT

> Principiu general anti-contaminare: în D2 NU se tastează valori libere care ar putea
> deveni accidental anomalii. Tot ce e geografic/temporal se DERIVĂ din nomenclatoare.

**`oras` (+ coerența cu `judet`):**
- Se generează prin SELECTAREA unei linii din `tbl_Localitati`, niciodată prin tastare liberă.
- Linia aleasă dă SIMULTAN `oras` = `oras_oficial` ȘI `judet` = `judet`-ul ei. Astfel perechea (oraș, județ) este, prin construcție, o pereche care există în nomenclator.
- Scriere: exact forma oficială (`Cluj-Napoca`, nu `Cluj`/`CJ`). Zero abateri de scriere în D2.
- Distribuție realistă: pondere mai mare pe orașele mari (București, Cluj-Napoca, Timișoara, Iași, Constanța, Brașov), restul mai rar. Toate cele 20 de localități apar de cel puțin câteva ori.

**`data_scadentei`:**
- `data_scadentei` = `data_factura` + termen, unde termen ∈ {15, 30, 45, 60} zile (mix B2B realist, 30 dominant).
- Regula dură: `data_scadentei` > `data_factura` pe FIECARE rând (termen ≥ 15, niciodată 0 sau negativ). Zero scadențe anterioare facturii în D2.

**`data_factura` (curățare pentru coerența C02.04):**
- În setul curat, `data_factura` cade DOAR în zile lucrătoare: nu în weekend (sâmbătă/duminică) și nu într-o dată din `tbl_SarbatoriLegale`.
- Dacă un rând moștenit are `data_factura` într-o zi nelucrătoare, se mută pe cea mai apropiată zi lucrătoare. Astfel C02.04 are zero anomalii înainte de D4.

**`categorie` ↔ `cota_tva` (coerență fiscală):**
- Pentru fiecare rând, `cota_tva` = `cota_legala` corespunzătoare `categorie`-i din `tbl_RegulriTVA`. Zero discordanțe TVA în D2.

**`valoare_neta` / `valoare_tva` / `valoare_totala` (coerență aritmetică + invariant):**
- `valoare_neta` se **MOȘTENEȘTE din setul existent**, NU se reinventează (conservarea sumei cap-coadă, R-V02.14).
- `valoare_tva` = `valoare_neta` × `cota_tva` (rotunjit). `valoare_totala` = `valoare_neta` + `valoare_tva`.
- Recalculul TVA pe cota corectă NU atinge `valoare_neta`; suma bazei rămâne identică.

---

## 4. ALTE COLOANE necesare ACUM? (pentru coerența modelului, NU pentru anomalii)

**Verdict: NU. Cele 2 coloane noi (`oras`, `data_scadentei`) sunt suficiente. Nu se adaugă altele în D2.**

Evaluare onestă a candidaților respinși:
- **`termen_plata_zile`** (ar documenta regula scadenței): RESPINS. `data_scadentei` poartă singură fenomenul C02.03; stocarea termenului ar introduce o a patra consistență derivată (scadență = factură + termen) pe care nu o verificăm și care nu aparține axei C02. Termenul rămâne regulă de generare, nu coloană.
- **`cod_judet` / `cod_localitate`** (chei numerice): RESPINS. Confruntarea oraș↔județ se face pe text prin `tbl_Localitati`; coduri în plus = complexitate de model fără rol pedagogic în C02.
- **`an` / `luna` derivate din `data_factura`**: RESPINS. Sunt dimensiuni de analiză temporală (trend, grupare) = T2/T3, nu C02. Le-am introduce abia într-o treaptă superioară.

Adăugarea oricărei alte coloane acum = scope creep. Modelul minim coerent = cele 16 coloane din §1.

---

## 5. RELAȚIILE de model (logică, FĂRĂ formule)

> ATENȚIE anti-drift: acestea sunt relații de REFERINȚĂ / CONFRUNTARE pentru validare,
> NU join-uri / Data Model / relații 1:M interogabile. Join + Data Model = competență T3,
> INTERZIS în C02 (garda T1). Aici nomenclatoarele sunt tabele de căutare pentru control,
> nu surse aduse într-un model relațional.

| Relație | Tip logic | Ce leagă | Semnificație în D2 (stare curată) |
|---|---|---|---|
| `Vanzari[oras]` → `tbl_Localitati[oras_oficial]` | căutare „există în" | orașul ↔ nomenclatorul oficial | în D2: TOATE orașele există în nomenclator |
| `Vanzari[oras,judet]` → `tbl_Localitati[oras_oficial,judet]` | confruntare pereche | perechea oraș-județ ↔ perechea oficială | în D2: TOATE perechile coincid |
| `Vanzari[categorie]` → `tbl_RegulriTVA[categorie]` | căutare cotă legală | categoria ↔ cota corectă | în D2: `cota_tva` = `cota_legala` peste tot |
| `Vanzari[data_factura]` ↮ `tbl_SarbatoriLegale[data]` | „NU se află în" + masca weekend | data emiterii ↔ zile nelucrătoare | în D2: nicio `data_factura` în sărbătoare/weekend |

`tbl_CodJudetCNP` NU se leagă de `Vanzari` (e relația CNP↔județ pe `CONTACTE`, la D3).

---

## 6. CRITERIUL DE INTEGRITATE D2 (definition of done)

„D2 este gata" = setul `Vanzari` trece TOATE următoarele, simultan, cu ZERO excepții:

1. **Volum:** ~2000 rânduri (aliniat packului), structura = exact cele 16 coloane din §1.
2. **Geografie (C02.01 curat):** fiecare `oras` există în `tbl_Localitati`; fiecare pereche (`oras`,`judet`) coincide cu nomenclatorul. Zero abateri de scriere.
3. **TVA (C02.02 curat):** pentru fiecare rând, `cota_tva` = `cota_legala` a categoriei din `tbl_RegulriTVA`. Zero discordanțe.
4. **Cronologie (C02.03 curat):** `data_scadentei` > `data_factura` pe fiecare rând. Zero scadențe anterioare.
5. **Calendar (C02.04 curat):** nicio `data_factura` în weekend sau în `tbl_SarbatoriLegale`. Toate emiterile în zile lucrătoare.
6. **Aritmetică:** `valoare_tva` = `valoare_neta` × `cota_tva` (rotunjit); `valoare_totala` = net + TVA, pe fiecare rând.
7. **Invariant sumă (R-V02.14):** SUM(`valoare_neta`) = totalul moștenit din setul C01/existent. Neschimbat.
8. **Zero anomalii latente:** dacă s-ar rula (mental) verificările C02.01-04, numărul de hit-uri = 0. Setul e curat prin construcție.

Dacă oricare punct nu e îndeplinit → D2 NU e gata; se repară înainte de D3/D4.

---

## 7. RISCURI D2 (unde s-ar putea strecura o anomalie înainte de D4)

| # | Risc | Mecanism | Mitigare |
|---|---|---|---|
| RD1 | **Abatere de scriere accidentală la `oras`** | tastare liberă → typo/abreviere | `oras` se ia prin SELECȚIE din `tbl_Localitati`, niciodată tastat |
| RD2 | **Pereche oraș↔județ ruptă accidental** | `oras` și `judet` setate independent | ambele vin din ACEEAȘI linie de nomenclator (§3) |
| RD3 | **`data_factura` pică pe weekend/sărbătoare** | generare aleatoare de date | generator de zile lucrătoare + mutare pe cea mai apropiată zi lucrătoare |
| RD4 | **Scadență ≤ factură accidental** | termen 0/negativ sau date inversate | termen ∈ {15,30,45,60}, mereu pozitiv; verificare `scadentei > factura` |
| RD5 | **`cota_tva` nealiniată la categorie** | cotă moștenită nepotrivită | `cota_tva` se DERIVĂ din `tbl_RegulriTVA` la generare |
| RD6 | **Drift de scriere județ vs nomenclator** | „Bucuresti" vs „București" | scrierea județului = exact cea din `tbl_Localitati` (diacritice incluse) |
| RD7 | **Ruperea invariantului sumă** | regenerarea valorilor `valoare_neta` | `valoare_neta` se MOȘTENEȘTE, nu se reinventează (§3) |
| RD8 | **Scope creep: coloane/semnalizări premature** | adăugare `flag_*`/CF/formule în D2 | D2 = doar input; semnalizarea e D5 (vezi §1 notă) |
| RD9 | **Anomalie de model (join/Data Model)** | tratarea nomenclatoarelor ca model relațional | relațiile = căutare/confruntare, NU join (§5, garda T1) |

---

## VERDICT D2

**Structura completă D2:** foaia `Vanzari` cu 16 coloane (14 existente + `oras` + `data_scadentei`), toate de input, fără semnalizare.

**Definition of done D2:** cele 8 puncte din §6 îndeplinite simultan, cu zero excepții — set curat, coerent, cu invariantul sumă conservat și zero anomalii latente.

**Checklist de validare D2 (de bifat la implementare):**
- [ ] ~2000 rânduri, exact 16 coloane (ordinea din §1)
- [ ] toate orașele ∈ `tbl_Localitati` (COUNTIF mental = 0 lipsuri)
- [ ] toate perechile (oraș, județ) coincid cu nomenclatorul
- [ ] `cota_tva` = `cota_legala` pe fiecare rând
- [ ] `data_scadentei` > `data_factura` pe fiecare rând
- [ ] nicio `data_factura` în weekend / `tbl_SarbatoriLegale`
- [ ] `valoare_tva` / `valoare_totala` aritmetic corecte
- [ ] SUM(`valoare_neta`) = totalul moștenit (R-V02.14)
- [ ] zero coloane de semnalizare prezente (acelea sunt D5)
- [ ] scrierea diacritică a județelor = identică cu nomenclatoarele

**Următorul pas (PENDING):** D3 — satelitul `CONTACTE` curat (CNP coerent), apoi D4 injecția anomaliilor.
