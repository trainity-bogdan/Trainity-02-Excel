# D3 · REALITATEA C02 (universul de date perfect, ZERO anomalii)

> Document de construcție a REALITĂȚII. Consolidează D1 (nomenclatoare) + D2 (Vanzari) +
> CONTACTE (CNP coerent) într-un singur univers credibil de companie reală.
> NU anomalii (D4), NU semnalizare/CF/AF/DV (D5), NU formule de control, NU HTML/copy.
> Tot ce urmează e starea CURATĂ pe care C02 o va pune ulterior sub semnul întrebării.

---

## 0. UNIVERSUL (8 foi)

| Foaie | Rol | Stare |
|---|---|---|
| `Vanzari` | corpul de tranzacții (~2000 rânduri) | construit la D2, recapitulat aici |
| `CONTACTE` | satelit persoane de contact (~50) — gazda CNP | construit AICI (D3) |
| `tbl_Localitati` | nomenclator oraș↔județ (20) | D1 LOCK |
| `tbl_RegulriTVA` | nomenclator categorie→cotă (7) | D1 LOCK |
| `tbl_SarbatoriLegale` | calendar sărbători 2026 (16) | D1 LOCK |
| `tbl_CodJudetCNP` | nomenclator cod→județ (15) | D1 LOCK |
| `_README` · `CONTROL_FINAL` | existente | păstrate |

Cele 15 județe canonice (identice în toate foile geografice): Alba, Argeș, Bacău, Bihor, Brașov, Cluj, Constanța, Dolj, Galați, Iași, Mureș, Prahova, Sibiu, Timiș, București.

---

## 1. FOAIA `Vanzari` (16 coloane — recapitulare D2)

| # | Coloană | Stare | Tip |
|---|---|---|---|
| 1 | `nr_factura` | existentă | text |
| 2 | `data_factura` | existentă | dată |
| 3 | `client_nume` | existentă | text |
| 4 | `judet` | existentă | text |
| 5 | `oras` | nouă | text |
| 6 | `cod_produs` | existentă | text |
| 7 | `produs_nume` | existentă | text |
| 8 | `categorie` | existentă | text |
| 9 | `cantitate` | existentă | număr |
| 10 | `pret_unitar` | existentă | număr |
| 11 | `valoare_neta` | existentă | număr (INVARIANT) |
| 12 | `cota_tva` | existentă | procent |
| 13 | `valoare_tva` | existentă | număr |
| 14 | `valoare_totala` | existentă | număr |
| 15 | `moneda` | existentă | text (RON) |
| 16 | `data_scadentei` | nouă | dată |

Reguli de generare curată (din D2): `oras` prin selecție din `tbl_Localitati` (oraș + județ din aceeași linie); `data_scadentei` = `data_factura` + {15/30/45/60} zile, mereu ulterioară; `data_factura` doar în zile lucrătoare (nu weekend, nu sărbătoare); `cota_tva` = `cota_legala` a categoriei; `valoare_neta` moștenită (R-V02.14); `valoare_tva`/`valoare_totala` recalculate aritmetic.

---

## 2. FOAIA `CONTACTE` (satelit, gazda CNP) — construcție D3

**Structură (7 coloane de input — coloanele de semnalizare vin la D5):**

| # | Coloană | Tip | Rol |
|---|---|---|---|
| 1 | `id_contact` | text | identificator unic (CTC-0001 ...) |
| 2 | `client_nume` | text | FK către clientul din `Vanzari` |
| 3 | `nume_persoana` | text | persoana de contact (Nume Prenume) |
| 4 | `CNP` | text 13 cifre | identificatorul iconic |
| 5 | `Sex` | text (M/F) | sexul declarat |
| 6 | `Judet` | text | județul declarat (din cele 15) |
| 7 | `Data_Nasterii` | dată | data nașterii declarată |

**Volum: ~50 contacte** (câte ~1 persoană per client distinct din `Vanzari`).

### 2.1 Anatomia CNP (S AA LL ZZ JJ NNN C — 13 cifre)
- **S** (cifra 1) = sex + secol: `1`=M / `2`=F (1900-1999); `5`=M / `6`=F (2000-2099).
- **AA** (2-3) = anul nașterii (2 cifre).
- **LL** (4-5) = luna (01-12).
- **ZZ** (6-7) = ziua (01-31, validă pentru lună).
- **JJ** (8-9) = codul de județ (din `tbl_CodJudetCNP`; București = 40).
- **NNN** (10-12) = secvențial (001-999), paritatea liberă.
- **C** (13) = cifra de control.

### 2.2 Cifra de control (algoritm oficial)
Ponderi fixe: `2 7 9 1 4 6 3 5 8 2 7 9`. Înmulțești fiecare din primele 12 cifre cu ponderea ei, însumezi, `rest = sumă mod 11`. Cifra de control = `rest`, iar dacă `rest = 10` atunci `= 1`.

### 2.3 Exemplu coerent (clean, fără anomalie)
Bărbat, născut 12.03.1985, județ Cluj (cod 12), secvențial 045:
`CNP = 1 85 03 12 12 045 C`. Cifre: 1,8,5,0,3,1,2,1,2,0,4,5.
Sumă ponderată = 2+56+45+0+12+6+6+5+16+0+28+45 = 221. `221 mod 11 = 1` → **C = 1**.
`CNP = 1850312120451`. Coerent: `Sex`=M (S=1), `Data_Nasterii`=1985-03-12 (din AA/LL/ZZ + secol), `Judet`=Cluj (JJ=12), control corect.

---

## 3. RELAȚIILE universului (logică de model, FĂRĂ formule)

> Anti-drift (garda T1): toate sunt relații de REFERINȚĂ / CONFRUNTARE pentru integritate,
> NU join-uri / Data Model / relații interogabile (acelea = T3, INTERZIS în C02).
> Nomenclatoarele = tabele de căutare; satelitul = sursă de identitate, nu model relațional.

| Relație | Tip logic | În realitatea curată |
|---|---|---|
| `Vanzari[oras]` → `tbl_Localitati[oras_oficial]` | există în | toate orașele există |
| `Vanzari[oras,judet]` → `tbl_Localitati[oras_oficial,judet]` | confruntare pereche | toate perechile coincid |
| `Vanzari[categorie]` → `tbl_RegulriTVA[categorie]` | căutare cotă | `cota_tva` = `cota_legala` peste tot |
| `Vanzari[data_factura]` ↮ `tbl_SarbatoriLegale[data]` + masca weekend | nu se află în | nicio emitere în zi nelucrătoare |
| `CONTACTE[client_nume]` → `Vanzari[client_nume]` | apartenență client | fiecare contact aparține unui client real din `Vanzari` |
| `CONTACTE[Judet]` → `tbl_CodJudetCNP[judet]` | există în | toate județele ∈ cele 15 |
| `CONTACTE[CNP] (JJ)` → `tbl_CodJudetCNP[cod]` → `Judet` | derivare + confruntare | codul din CNP dă același județ ca `Judet` |
| `CONTACTE[CNP] (S, AALLZZ)` ↔ `Sex`, `Data_Nasterii` | derivare internă | sexul și data derivate din CNP = cele declarate |
| `CONTACTE[CNP] (C)` | aritmetică internă | cifra de control = cea calculată |

`tbl_CodJudetCNP` NU se leagă de `Vanzari` (relație exclusiv pe `CONTACTE`).

---

## 4. REGULILE DE GENERARE (realitate credibilă, zero anomalii)

### 4.1 `Vanzari`
1. `valoare_neta` se **moștenește** din setul existent (conservarea sumei, R-V02.14). Nu se reinventează.
2. `oras` + `judet`: se alege o linie din `tbl_Localitati`; ambele câmpuri vin din ACEEAȘI linie (perechea există prin construcție). Pondere mai mare pe orașele mari (București, Cluj-Napoca, Timișoara, Iași, Constanța, Brașov).
3. `categorie`: din cele 7; `cota_tva` = `cota_legala` corespunzătoare. `valoare_tva` = round(`valoare_neta` × `cota_tva`); `valoare_totala` = net + TVA.
4. `data_factura`: în intervalul anului operațional, DOAR zile lucrătoare (nu sâmbătă/duminică, nu în `tbl_SarbatoriLegale`).
5. `data_scadentei` = `data_factura` + termen ∈ {15, 30, 45, 60} (30 dominant), mereu ulterioară.

### 4.2 `CONTACTE` (CNP coerent prin construcție — generat înainte-spre-înapoi)
> Principiu: CNP-ul NU se „verifică" după ce e scris; se CONSTRUIEȘTE corect din start,
> apoi `Sex`/`Judet`/`Data_Nasterii` se copiază din aceleași surse. Imposibil să iasă incoerent.

1. **Clientul:** `client_nume` = un client real existent în `Vanzari`.
2. **Județul:** alege un județ din cele 15 → `Judet` ȘI codul `JJ` din `tbl_CodJudetCNP` (București → 40).
3. **Data nașterii:** alege o dată plauzibilă de adult (interval ~1960-2002) → `Data_Nasterii`; din ea derivă AA/LL/ZZ și secolul.
4. **Sexul:** alege M/F → `Sex`; cifra `S` = funcție de sex + secol (1900s: 1/2; 2000s: 5/6).
5. **Secvențial:** `NNN` = 001-999.
6. **Control:** calculează `C` cu ponderile 2-7-9-1-4-6-3-5-8-2-7-9 (mod 11, 10→1).
7. **Asamblare:** `CNP = S+AA+LL+ZZ+JJ+NNN+C`. Pentru că toate câmpurile derivă din aceleași alegeri, `Sex`/`Judet`/`Data_Nasterii` sunt prin definiție coerente cu CNP.
8. `nume_persoana`: nume românesc plauzibil; `id_contact` = CTC-0001 incremental.

---

## 5. DEFINITION OF DONE (realitatea perfectă)

„Realitatea C02 e gata" = TOATE, simultan, cu ZERO excepții:

**Vanzari:**
1. ~2000 rânduri, exact 16 coloane (ordinea §1), niciuna de semnalizare.
2. Fiecare `oras` ∈ `tbl_Localitati`; fiecare pereche (oraș, județ) coincide.
3. `cota_tva` = `cota_legala` pe fiecare rând.
4. `data_scadentei` > `data_factura` pe fiecare rând.
5. Nicio `data_factura` în weekend / `tbl_SarbatoriLegale`.
6. `valoare_tva`/`valoare_totala` aritmetic corecte; SUM(`valoare_neta`) = totalul moștenit (R-V02.14).

**CONTACTE:**
7. ~50 contacte, exact 7 coloane, niciuna de semnalizare.
8. Fiecare `client_nume` există în `Vanzari`.
9. Fiecare `Judet` ∈ cele 15; codul `JJ` din CNP dă același județ.
10. Cifra `S` a CNP corespunde lui `Sex` + secolului din `Data_Nasterii`.
11. AA/LL/ZZ din CNP = `Data_Nasterii` (dată calendaristic validă).
12. Cifra de control = cea calculată, pe fiecare CNP.
13. CNP unic per contact, exact 13 cifre numerice.

**Global:**
14. Zero anomalii latente: orice verificare C02.01-05 rulată mental dă 0 hit-uri.
15. Impresia de companie reală: nume, orașe, produse, date plauzibile și consistente.

---

## 6. CHECKLIST DE VALIDARE (de bifat la implementarea xlsx)

**Vanzari**
- [ ] ~2000 rânduri, 16 coloane în ordinea din §1
- [ ] toate orașele ∈ `tbl_Localitati`
- [ ] toate perechile (oraș, județ) coincid cu nomenclatorul
- [ ] `cota_tva` = `cota_legala` pe fiecare rând
- [ ] `data_scadentei` > `data_factura` pe fiecare rând
- [ ] nicio `data_factura` în weekend / sărbătoare legală
- [ ] aritmetică TVA corectă pe fiecare rând
- [ ] SUM(`valoare_neta`) = totalul moștenit
- [ ] scriere diacritică județe identică cu nomenclatoarele
- [ ] zero coloane de semnalizare

**CONTACTE**
- [ ] ~50 contacte, 7 coloane
- [ ] `id_contact` unic; `client_nume` ∈ clienții din `Vanzari`
- [ ] toate CNP-urile = 13 cifre numerice, unice
- [ ] `Sex` ↔ cifra S a CNP (M: 1/5, F: 2/6)
- [ ] `Data_Nasterii` ↔ AA/LL/ZZ + secol din CNP
- [ ] `Judet` ↔ codul JJ din CNP (via `tbl_CodJudetCNP`)
- [ ] cifra de control corectă pe fiecare CNP
- [ ] toate județele ∈ cele 15
- [ ] zero coloane de semnalizare

**Integritate globală**
- [ ] zero anomalii latente (C02.01-05 → 0 hit-uri)
- [ ] cele 15 județe scrise identic în `Vanzari`, `CONTACTE`, `tbl_Localitati`, `tbl_CodJudetCNP`
- [ ] aspect de fișier provenit dintr-o companie reală (coerent, credibil, consistent)

---

## VERDICT D3

Universul de date C02 e specificat integral și CURAT: `Vanzari` (16 coloane) + `CONTACTE` (7 coloane, CNP coerent prin construcție) + cele 4 nomenclatoare D1, legate prin relații de referință (nu join). Regulile de generare garantează că nicio anomalie nu poate apărea accidental: orașul vine din nomenclator, scadența e mereu ulterioară, factura cade în zi lucrătoare, cota urmează regula, iar CNP-ul e construit corect din start, nu verificat ulterior.

**Următorul pas (PENDING):** D4 — injecția controlată a celor 5 anomalii peste această realitate perfectă.
