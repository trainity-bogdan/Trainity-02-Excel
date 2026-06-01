# D1 · NOMENCLATOARELE C02 (surse de adevăr)

> Pasul D1 din `PLAN-EXECUTIE-C02.md`. NU Date_MASTER, NU HTML, NU copy.
> Doar cele 4 tabele de referință care definesc ce înseamnă „corect".
> Principiu: REALIST dar PEDAGOGIC. Nu exhaustiv, nu complet național.
> Suficient pentru a demonstra cele 5 anomalii + toate mecanismele de semnalizare.

---

## REGULA DE INTEGRITATE (de ce cele 4 se țin împreună)
Cele trei tabele geografice folosesc **același set de 15 județe**, cu aceeași scriere:
`tbl_Localitati.judet` ⊆ județele · `tbl_CodJudetCNP.judet` = aceleași județe · `CONTACTE.Judet` (din Date_MASTER) referă aceeași listă.
Fără asta, verificarea oraș↔județ (C02.01b) și verificarea CNP↔județ (C02.05b) nu s-ar putea închide. Coerența între nomenclatoare e condiția ca semnalizarea să fie deterministă.

Cele 15 județe canonice ale setului: **Alba, Argeș, Bacău, Bihor, Brașov, Cluj, Constanța, Dolj, Galați, Iași, Mureș, Prahova, Sibiu, Timiș, București.**

---

## 1. `tbl_Localitati` — oraș↔județ oficial (C02.01)

**Structură:** `oras_oficial` (text, cheie pentru COUNTIF/XLOOKUP) · `judet` (text, din cele 15).

**Înregistrări: 20** (15 județe, cu mai multe orașe în 5 dintre ele).

| oras_oficial | judet |
|---|---|
| Alba Iulia | Alba |
| Pitești | Argeș |
| Bacău | Bacău |
| Oradea | Bihor |
| Brașov | Brașov |
| Făgăraș | Brașov |
| Cluj-Napoca | Cluj |
| Turda | Cluj |
| Constanța | Constanța |
| Mangalia | Constanța |
| Craiova | Dolj |
| Galați | Galați |
| Iași | Iași |
| Târgu Mureș | Mureș |
| Ploiești | Prahova |
| Câmpina | Prahova |
| Sibiu | Sibiu |
| Mediaș | Sibiu |
| Timișoara | Timiș |
| București | București |

**Justificarea dimensiunii (20):**
- Conține DOAR forma oficială. Variantele greșite (`Cluj`, `CJ`, `Cluj-Napoca` scris prost, `Clum Napoca`) NU trăiesc aici — trăiesc în date și pică pentru că nu se găsesc prin COUNTIF. Nomenclatorul e curat prin definiție.
- 5 județe cu câte 2 orașe (Cluj: Cluj-Napoca+Turda; Constanța: Constanța+Mangalia; Brașov: Brașov+Făgăraș; Prahova: Ploiești+Câmpina; Sibiu: Sibiu+Mediaș) → demonstrează că un oraș aparține unui județ anume, deci „Brașov în Constanța" e imposibil (C02.01b).
- Conține exact orașele țintă ale anomaliilor: `Cluj-Napoca` (pentru abaterea de scriere) și perechea `Brașov`/`Constanța` (pentru oraș↔județ imposibil).
- 20 acoperă toți clienții setului fără să fie listă națională (România are ~320 orașe). Pedagogic: găsibil dintr-o privire, suficient pentru AF (unique records) și XLOOKUP.

---

## 2. `tbl_RegulriTVA` — categorie→cotă legală (C02.02)

**Structură:** `categorie` (text, cheie XLOOKUP) · `cota_legala` (procent).

> Cotele reflectă regimul folosit în pachetul de curs (19% / 9% / 5%), aliniat la coloana
> `cota_tva` existentă în set. NU sunt o referință fiscală live (regimul real se schimbă).

**Înregistrări: 7** (3 cote distincte).

| categorie | cota_legala |
|---|---|
| Hardware IT | 19% |
| Licențe software | 19% |
| Servicii consultanță | 19% |
| Echipamente birou | 19% |
| Alimente | 9% |
| Produse farmaceutice | 9% |
| Cărți și manuale | 5% |

**Justificarea dimensiunii (7):**
- 3 cote distincte (19/9/5) = minimul care face anomalia demonstrabilă: o categorie cu cotă redusă scrisă la cota standard. Exemple de plantat: `Alimente` cu 19% (corect 9%), `Cărți și manuale` cu 19% (corect 5%).
- Cota greșită e mereu o cotă REALĂ (alt procent valid), nu un număr aberant — aberantul ar fi eroare structurală (C01/C03), nu falsul valid (C02).
- 7 categorii acoperă mix-ul de produse al unui set B2B (IT + servicii + consumabile + câteva cu regim redus) fără să fie nomenclator CAEN complet.

---

## 3. `tbl_SarbatoriLegale` — calendar sărbători legale 2026 (C02.04)

**Structură:** `data` (dată) · `denumire` (text).

**Înregistrări: 16** (setul legal complet al anului — aici „complet" = mic și realist).

| data | denumire |
|---|---|
| 01.01.2026 | Anul Nou |
| 02.01.2026 | Anul Nou |
| 06.01.2026 | Boboteaza |
| 07.01.2026 | Sfântul Ioan |
| 24.01.2026 | Unirea Principatelor Române |
| 10.04.2026 | Vinerea Mare |
| 12.04.2026 | Paștele |
| 13.04.2026 | A doua zi de Paște |
| 01.05.2026 | Ziua Muncii |
| 31.05.2026 | Rusalii |
| 01.06.2026 | A doua zi de Rusalii / Ziua Copilului |
| 15.08.2026 | Adormirea Maicii Domnului |
| 30.11.2026 | Sfântul Andrei |
| 01.12.2026 | Ziua Națională |
| 25.12.2026 | Crăciunul |
| 26.12.2026 | A doua zi de Crăciun |

**Justificarea dimensiunii (16):**
- Acesta e singurul nomenclator care e COMPLET pentru domeniul lui (sărbătorile legale ale anului 2026), pentru că domeniul însuși e mic. Realist și exact, fără a fi „exhaustiv național".
- Aliniat la calendarul ortodox 2026: Paștele 12.04 (duminică) → a 2-a zi 13.04 (luni); Rusalii 31.05 → 01.06. Exemplul din spec (13.04.2026 = a 2-a zi de Paște) e acoperit.
- NETWORKDAYS.INTL primește această listă ca argument `holidays`. **Duminicile NU sunt în tabel** — ele cad pe masca de weekend a funcției. Deci tabelul prinde sărbătorile, masca prinde weekendurile; împreună acoperă cele ~20 rânduri „zi nelucrătoare".

---

## 4. `tbl_CodJudetCNP` — cod→județ (C02.05)

**Structură:** `cod` (text de 2 cifre, cheie pentru `MID(CNP,8,2)`) · `judet` (text, aceleași 15).

**Înregistrări: 15** (codurile oficiale CNP ale celor 15 județe ale setului).

| cod | judet |
|---|---|
| 01 | Alba |
| 03 | Argeș |
| 04 | Bacău |
| 05 | Bihor |
| 08 | Brașov |
| 12 | Cluj |
| 13 | Constanța |
| 16 | Dolj |
| 17 | Galați |
| 22 | Iași |
| 26 | Mureș |
| 29 | Prahova |
| 32 | Sibiu |
| 35 | Timiș |
| 40 | București |

> Notă București: codurile 41-46 = sectoarele 1-6, toate → București. La implementare se mapează
> și ele pe „București" (sau se folosesc contacte cu cod 40), ca derivarea județului să fie corectă.

**Justificarea dimensiunii (15):**
- Codurile sunt EXACT cele 15 județe din `tbl_Localitati` (aceeași scriere), ca verificarea CNP↔județ să se închidă: `XLOOKUP(MID(CNP,8,2), cod, judet)` trebuie să dea un județ care există în restul setului.
- Include `40 București` pentru exemplul de anomalie din spec: CNP cu cod 40 (București) dar `Judet`=Cluj.
- Codurile oficiale reale (01 Alba, 12 Cluj, 13 Constanța, 40 București...), nu inventate — realismul e necesar ca lecția despre CNP să fie credibilă.
- 15 din 47 de coduri naționale = pedagogic suficient (acoperă geografia setului), nu nomenclator administrativ complet.

---

## SINTEZĂ D1

| Nomenclator | Coloane | Înregistrări | Demonstrează |
|---|---|---|---|
| `tbl_Localitati` | oras_oficial, judet | **20** | C02.01 (scriere inconsecventă + oraș↔județ imposibil) |
| `tbl_RegulriTVA` | categorie, cota_legala | **7** | C02.02 (cotă validă, greșită fiscal) |
| `tbl_SarbatoriLegale` | data, denumire | **16** | C02.04 (zi validă, firma închisă legal) |
| `tbl_CodJudetCNP` | cod, judet | **15** | C02.05b (CNP↔județ contradictoriu) |

**Acoperire mecanisme de semnalizare:**
- COUNTIF (oraș negăsit) → `tbl_Localitati`.
- XLOOKUP de confruntare (oraș→județ, categorie→cotă, cod→județ) → 3 nomenclatoare.
- NETWORKDAYS.INTL (holidays + weekend mask) → `tbl_SarbatoriLegale`.
- AF unique records (descoperă nomenclatorul real din date) → se aplică pe coloana `oras`, comparat cu `tbl_Localitati`.
- Algoritmul cifrei de control CNP NU cere nomenclator (e pur aritmetic) → singura verificare din C02.05 fără tabel de referință.

**Coerență garantată:** cele 15 județe sunt identice în `tbl_Localitati`, `tbl_CodJudetCNP` și (la D3) `CONTACTE.Judet`. Aceasta e precondiția ca toate verificările încrucișate să fie deterministe.

**Următorul pas (PENDING):** D2 — `Vanzari` curat + coloanele de input `oras`/`data_scadentei`, peste fundamentul acestor 4 nomenclatoare.
