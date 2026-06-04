# DATA-INSTRUCTIUNI.md — Transformări per construcție pe Date_MASTER-initial

Versiune: V19 (înghețat 25 mai 2026)

Acest document specifică EXACT ce trebuie să facă fiecare construcție
C01-C08 cu fișierul `Date_MASTER-initial.xlsx`. Generatorul citește
acest document împreună cu SPEC C{NN} din SISTEM_TRAINITY.md și aplică
modificările listate.

---

## DATE_MASTER-INITIAL — SURSA UNICĂ DE ADEVĂR

Fișierul `referinte/Date_MASTER-initial.xlsx` este asset perpetuu
înghețat V19. Conține:

- **2000 facturi** pe 12 luni (iunie 2025 — mai 2026)
- **Schema canonică** 14 coloane (R-V03.47)
- **Sheets auxiliare:** CLIENTI (15), PRODUSE (13), AGENTI (6), DEPOZITE (5)
- **Sumă valoare_neta canonică:** ~7,986,000 lei
- **Pattern sezonier:** vârf nov-dec, valle iul-aug

Toate construcțiile C01-C08 pornesc de la acest fișier. Niciuna nu
modifică Date_MASTER-initial. Fiecare livrează `Date_MASTER-C{NN}.xlsx`
ca rezultat propriu.

---

## TREAPTA 1 — SCAN (datele murdărite, demonstrare curățare)

### C01 STRUCTURA TABELELOR

**Intent:** demonstrare curățare structurală export ERP brut.

**Modificări pe Date_MASTER-initial:**
1. Adaugă 3 rânduri antet ERP brut deasupra header-ului real
   (linii cu "RAPORT VANZARI", "Perioada: ...", "Generat la: ...")
2. Inserează rânduri SUBTOTAL după fiecare lună (12 rânduri)
3. Adaugă 1 rând TOTAL GENERAL la final
4. Inserează ~53 blank-uri false (rânduri complet goale între pachete)
5. Adaugă coloana fantomă `ambalaj` între `categorie` și `cantitate` (cu valori
   ce arată ca date dar nu au sens business)
6. AutoFilter setat în zonă greșită
7. Formula SUM eronată într-un rând "TOTAL" (sumează antetul + datele)

**Conservare semantică:** Suma valoare_neta a celor 2000 facturi
reale = neschimbată (~7,986,000 lei). Toate intervenițile sunt
"ambalaj" peste date reale.

### C02 CONTROLUL DATELOR

**Intent:** demonstrare marcare anomalii logice.

**Modificări pe Date_MASTER-initial:**
1. Plantează 8 facturi cu `data_factura` viitoare (după 31 mai 2026)
2. Plantează 5 facturi cu `cod_produs` care nu există în nomenclator
   (ex: PRD-999, PRD-XX1)
3. Plantează 12 facturi cu `client_nume` care nu există în CLIENTI
4. Plantează 10 perechi fuzzy duplicate (aceeași factură cu mici
   variații: spațiu, virgulă în loc de punct la valoare)
5. Plantează 6 facturi cu `cantitate` sau `pret_unitar` gol (mandatory gol)
6. Plantează 4 facturi cu `valoare_neta` ≤ 0

**Adăugări în output (Date_MASTER-C02.xlsx):**
- Coloana nouă `status_validare`: VALID / DE VERIFICAT / EXCLUS
- Coloana nouă `motiv_anomalie`: text descriptiv
- Sheet nou `CONTROL_FINAL`: agregare per status, per motiv

**Distribuție așteptată OUTPUT:**
- VALID: ~1955 facturi
- DE VERIFICAT: ~10 facturi (fuzzy duplicate)
- EXCLUS: ~35 facturi (toate celelalte anomalii)

**Conservare semantică:** Suma valoare_neta = neschimbată (marcare,
nu eliminare).

### C03 AUDITAREA DATELOR

**Intent:** demonstrare audit forensic + curățare contaminare invizibilă.

**Modificări pe Date_MASTER-initial:**
1. Pe `client_nume`: 80 celule cu trailing spaces, 35 cu ZWSP (\u200B),
   25 cu SHY (\u00AD)
2. Pe `produs_nume`: 70 celule cu trailing spaces, 70 cu trailing
   newline (\n)
3. Pe `valoare_neta`: 150 celule cu numere stocate ca text
   (ex: "1234.56" cu tip Text)
4. Pe `data_factura`: 120 celule cu date stocate ca string
   ("01.10.2025" în loc de date real)
5. Total: 550 contaminări invizibile distribuite disjunct

**Sheets în output (Date_MASTER-C03.xlsx):**
- Sheet `Vanzari` cu contaminări (= input audit)
- Sheet `Vanzari_AUDIT` rezultat curățare PQ
- Sheet `_AUDIT_REPORT`: pe categorii contaminare găsite + neutralizate

**Conservare semantică:** Sumă valoare_neta INPUT (numeric + text-conv)
= Sumă valoare_neta OUTPUT (numeric pur).

### C04 NORMALIZAREA DATELOR

**Intent:** consolidare T1 în flux refresh idempotent.

**Modificări pe Date_MASTER-initial:**
Aplică TOATE perturbările T1 cumulativ (C01 + C02 + C03):
- Antet ERP brut + subtotale + total general
- Anomalii logice plantate
- Contaminări invizibile

Plus 3 perturbări noi specifice C04:
1. Diacritice mixte (unele celule au "ș" vs "s", "ț" vs "t")
2. Format date amestec (DD.MM.YYYY și YYYY-MM-DD în aceeași coloană)
3. Spații multiple consecutive în text

**Sheets în output (Date_MASTER-C04.xlsx):**
- Sheet `_ARHIVA` cu cele 10 fenomene plantate
- Sheet `Vanzari_Normalizat` rezultat după 10 Applied Steps
- Sheet `_NORMALIZARE` cu cei 10 pași Power Query documentați
- Sheet `CONTROL_FINAL` cu validare finală

**Delta declarat:** subtotale + total general eliminate
(~13 rânduri = ~5% din volum). Suma valoare_neta reală = neschimbată.

---

## TREAPTA 2 — CUNOAȘTERE (operatorul înțelege ce este setul)

**Reasezare V24/V25 (L136):** T2 nu este "atribuie semnificație business
prin clasificări" (aia e T3 ANALIZA). T2 e PROFILAREA SETULUI - operator
află din ce e făcut setul, fără să-i atribuie încă semnificație
strategică.

**Două axe ortogonale în T2 (separare obsesivă L136.A):**
- **C05 CALITATIVA** - categorial, taxonomic - "Ce conține setul?"
  (etichete unice, dicționar, granularitate, tipologie coloane)
- **C06 CANTITATIVA** - numeric, statistic - "Cum arată numeric setul?"
  (sume, medii, distribuții, top N)

### C05 CLASIFICAREA DATELOR (axa CALITATIVA)

**Intent:** dicționar complet al setului - operator inventariază
etichetele unice și înțelege taxonomia datelor (NU clasificare business).

**SPEC inghețat V25** (vezi SISTEM_TRAINITY.md sectiunea SPEC C05).

**Modificări pe Date_MASTER-initial:**
NU plantează nimic. Datele sunt deja curate.

**Operatii descriptive cheie (NU clasificare business):**
- Inventar etichete unice per coloană categorical
- Granularitate (câte valori distincte per coloană)
- Top frecvente (cele mai des întâlnite valori)
- Tipologie coloane (text vs număr vs dată vs categorial)
- Detectare anomalii dicționar (valori rare, outlieri taxonomici)

**Sheets în output (Date_MASTER-C05.xlsx):**
- Sheet `Vanzari` neschimbat
- Sheet `_DICTIONAR`: inventar etichete unice per coloană
- Sheet `_GRANULARITATE`: count distinct + frecvențe per coloană
- Sheet `_TIPOLOGIE`: clasificare tipuri coloane
- Sheet `_PROFIL`: rezumat profilare completa

**FENOMENE canonice așteptate (5 cifre fizice C05):**
- 15 CLIENTI unici (sau câți există în set)
- 4 CATEGORII produse
- 8 JUDETE clienți
- 2000 RANDURI total
- TOP-3 80% (concentrare top 3 clienti = ~X% din volum)

**Conservare semantică:** Suma valoare_neta = neschimbată
(profilare = inventariere, nu modifică valori).

### C06 KPI & CALCULE (axa CANTITATIVA)

**Intent:** profilare numerică - operator obține statistici cuantificate
despre set. (NU "business strategy" - aia e T3.)

**Modificări pe Date_MASTER-initial:**
NU plantează nimic.

**Adăugări în output (Date_MASTER-C06.xlsx):**
- Coloana `marja_estimata`: calculată per categorie (40% Hardware,
  60% Software, 30% Consumabile, 70% Servicii) - **CIFRA TEHNICA**,
  NU "strategie comercială"
- Coloana `valoare_marja`: valoare_neta × marja_estimata
- Sheet nou `_KPI_GENERAL`: ASP (Average Selling Price), frecventa
  vanzari, top 10 clienti, top 5 produse, marja totala
- Sheet nou `_KPI_FORMULE`: documentația formulelor

**Cuvinte marker stricte axa CANTITATIVA (L136.A):**
- "cifra", "sumă", "medie", "distribuție", "procentaj"
- NU "segment client" (aia ar fi clasificare strategică = T3)
- NU "prioritate produs" (aia ar fi decizie comercială = T3)

**Conservare semantică:** Suma valoare_neta = neschimbată.

### C07 LOGICA TEMPORALĂ (axa CINEMATICA, L136.B)

**Intent:** constructia POETICA a T2 - operator descopera ca setul
"are memorie" (pattern-uri sezoniere, evoluții, recurențe).

**Modificări pe Date_MASTER-initial:**
NU plantează nimic.

**Sheets în output (Date_MASTER-C07.xlsx):**
- Sheet `Vanzari` neschimbat
- Sheet `AGREGARE_LUNARA`: pivot pe luni cu sumă, count, ASP
- Sheet `AGREGARE_TRIMESTRIALA`: T1, T2, T3, T4
- Sheet `COMPARATIE_LUNI`: variație MoM (month over month)
- Sheet `PATTERN_SEZONIER`: detectie automată sezonalitate
  (varf nov-dec, valle iul-aug confirmat)

**Conservare semantică:** Suma valoare_neta = neschimbată
(doar agregări noi).

### C08 — TBD

SPEC NEGENERAT. Va fi adăugat la înghețarea finală T2.

---

## REGULĂ COMUNĂ TUTUROR CONSTRUCȚIILOR

1. **Pleacă de la Date_MASTER-initial.xlsx**, neschimbat în arhivă.
2. **Aplică modificările listate aici** pentru construcția curentă.
3. **Livrează Date_MASTER-C{NN}.xlsx** cu modificările aplicate.
4. **Gate V20** verifică:
   - Schema canonică prezentă (14 col, sheet Vanzari)
   - Sheets auxiliare neschimbate (CLIENTI, PRODUSE, AGENTI, DEPOZITE)
   - Suma valoare_neta în range conservare semantică **pe sheet OUTPUT
     canonic** (R-V03.53)
   - Modificările aplicate corespund DATA-INSTRUCTIUNI pentru C{NN}
5. **Construcții independente:** C05 NU dependă de C04. C03 NU dependă
   de C02. Fiecare pleacă din Date_MASTER-initial direct.

---

## SHEET OUTPUT CANONIC PER CONSTRUCȚIE (R-V03.53, V20)

Gate v20 verifică conservarea valorii_neta pe sheet-ul OUTPUT canonic
listat aici, NU pe sheet `Vanzari` (care poate fi intentionat
contaminat în C01-C04):

| Construcție | Sheet OUTPUT canonic | Suma așteptată |
|---|---|---|
| C01 STRUCTURA | `Vanzari` (curat) | ~7,986,019 lei |
| C02 CONTROL | `Vanzari` (cu status marcat) | ~7,986,019 lei |
| C03 AUDIT | `Vanzari_AUDIT` (curat) | ~7,986,019 lei |
| C04 NORMALIZARE | `Vanzari_Normalizat` (curat) | ~7,986,019 lei |
| C05 CLASIFICARE | `Vanzari` (neschimbat) + sheets `_DICTIONAR/_GRANULARITATE/_TIPOLOGIE/_PROFIL` | ~7,986,019 lei |
| C06 KPI | `Vanzari` (+marja_estimata) | ~7,986,019 lei |
| C07 LOGICA TEMPORALA | `Vanzari` (neschimbat) | ~7,986,019 lei |
| C08 | TBD | TBD |

**Toleranțe:** delta < 1% automat OK. Delta 1-15% acceptat doar dacă
declarat explicit în DATA-INSTRUCTIUNI (ex: C04 elimină subtotale,
delta ~0%). Delta >15% = FAIL automat.

---

## LIVRARE INCREMENTALĂ OBLIGATORIE (R-V03.52, V20)

Chat-ul CONSTRUCȚIE NN livrează **câte un fișier per mesaj** în
ordinea fixă (de la mic la mare ca size context):

1. `Date_MASTER-C{NN}.xlsx` (~170 KB)
2. `HTML-Studiu-Excel-{NN}-{slug}.html` (~80 KB)
3. `HTML-Editor-Studiu-Excel-{NN}-{slug}.html` (~90 KB)
4. `HTML-Video-Excel-{NN}-{slug}.html` (~800 KB)
5. `HTML-Editor-Video-Excel-{NN}-{slug}.html` (~800 KB)
6. Gate v20 rulat + verdict + offer `checkout constructie`

(Creativ abandonat V68: prompturile imaginilor le face ARHITECT extern, nu se mai livrează ca fișier.)

După fiecare livrare, motor confirmă scurt:
> *"Livrat: {nume_fisier}. Continui cu {N+1}/6 ({urmator})."*

Procedare automată, NU se așteaptă comanda Bogdan între livrabile.
Comanda `asteapta` întrerupe. Comanda `continua` reia.
