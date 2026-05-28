# SCHEMA-MASTER.md — Schema canonică Date_MASTER

Versiune: V18 (înghețat 25 mai 2026)
Status: SURSA UNICĂ DE ADEVĂR pentru toate datele Excel din C01-C20.

---

## CONCEPT FUNDAMENTAL

**Date_MASTER** este universul de date Excel partajat de toate construcțiile
C01-C20 ale Pack 02 Excel. Fiecare construcție pleacă de la rezultatul
construcției precedente și produce rezultatul pentru construcția
următoare. Progresia este cap-coadă, NU paralelă.

Nu mai există convenția veche "Date-Input + Date-Output" duplicat per
construcție. Există un singur fișier Excel per construcție care
reprezintă starea Date_MASTER după trecerea construcției respective.

## SCHEMA CANONICĂ (14 coloane, înghețat V18)

Sheet principal: `Vanzari` (înghețat, nu se schimbă între construcții)

| # | Nume coloană | Tip | Descriere |
|---|---|---|---|
| 1 | `nr_factura` | text | Identificator unic factură (ex: F-2026-001234) |
| 2 | `data_factura` | date | Data emiterii facturii |
| 3 | `client_nume` | text | Numele clientului |
| 4 | `judet` | text | Județul clientului (București, Cluj, Timiș...) |
| 5 | `cod_produs` | text | Cod produs SKU (ex: PRD-001) |
| 6 | `produs_nume` | text | Numele produsului |
| 7 | `categorie` | text | Categoria produsului |
| 8 | `cantitate` | number | Cantitate vândută |
| 9 | `pret_unitar` | number | Preț unitar (lei) |
| 10 | `valoare_neta` | number | Valoarea netă (cantitate × pret_unitar) |
| 11 | `cota_tva` | number | Cota TVA (0.05, 0.09, 0.19) |
| 12 | `valoare_tva` | number | Valoarea TVA (valoare_neta × cota_tva) |
| 13 | `valoare_totala` | number | Total (valoare_neta + valoare_tva) |
| 14 | `moneda` | text | Codul monedei (RON, EUR, USD) |

## SHEETS AUXILIARE (consistente între construcții)

Sheets de lookup care apar în toate Date_MASTER-urile:

- `CLIENTI` — nomenclator clienți (cod, nume, judet)
- `PRODUSE` — nomenclator produse (cod, nume, categorie)
- `AGENTI` — nomenclator agenți (cod, nume)
- `DEPOZITE` — nomenclator depozite (cod, nume)

Sheets opționale per construcție (adăugate la nevoie):
- `_PARCURS` — narativ progresia până la construcția curentă
- `_AUDIT_NN` — rezultat audit construcție NN (doar pentru construcții
  care produc raport audit)

## REGULĂ ABSOLUTĂ R-V03.47 — SCHEMA STABILĂ ÎNTRE CONSTRUCȚII

Cele 14 coloane din sheet `Vanzari` rămân INVARIANTE între
construcțiile C01-C20. O construcție poate adăuga coloane noi (ex:
`status_validare`, `motiv_anomalie` în C02), dar NU poate:
- Redenumi o coloană existentă
- Elimina o coloană existentă
- Schimba tipul unei coloane fără declarație explicită în SPEC
- Schimba sheet name principal (`Vanzari` rămâne canonic)

## NOMENCLATURĂ FIȘIERE DATE_MASTER

Fiecare construcție livrează exact UN fișier Excel:

```
Date_MASTER-dupa-C{NN}.xlsx
```

Acest fișier conține Date_MASTER după trecerea construcției NN și
servește ca INPUT pentru construcția NN+1.

Pentru construcția C01 (prima), INPUT-ul este:
```
Date_MASTER-initial.xlsx
```
Acesta reprezintă exportul ERP brut, neatins de niciun proces Trainity.

**Comportament în chat CONSTRUCTIE NN:**

Chat-ul CONSTRUCTIE NN (pentru NN >= 02) primește în arhiva atașată:
- Pentru NN = 01: `Date_MASTER-initial.xlsx`
- Pentru NN >= 02: `Date_MASTER-dupa-C{NN-1}.xlsx` (= OUTPUT-ul C{NN-1})

Generatorul citește acest fișier, aplică transformările SPEC C{NN} și
produce:
```
Date_MASTER-dupa-C{NN}.xlsx
```

Care intră în arhiva `OUT-{NN}-V{VV}-{TIMESTAMP}.zip` și devine INPUT
pentru chat-ul CONSTRUCTIE NN+1.

## CONSERVAREA SUMEI VALOARE_NETA

Suma `valoare_neta` este invariantă semantic între construcții, cu
excepții explicit declarate în SPEC:

- C01 STRUCTURA: conservare strictă (delta 0)
- C02 CONTROL: conservare strictă (marcare, nu eliminare)
- C03 AUDIT: conservare strictă (curățare formă, nu valoare)
- C04 NORMALIZARE: delta declarat (rânduri subtotal/total general
  eliminate; valoarea reală conservată)
- C05+ : per SPEC fiecare

GATE V18 verifică automat conservarea și raportează delta vs SPEC.

## DIMENSIUNI

Date_MASTER conține ~2000 rânduri de date reale (semantic plauzibile)
plus sheets auxiliare. Fiecare construcție poate adăuga 0-3 sheets
suplimentare (rapoarte audit, parcurs, control_final), dar sheet-ul
principal `Vanzari` rămâne neclintit ca dimensiune și schemă.

## VOCABULAR INTERZIS PE COLOANE

NU se folosesc denumiri vechi (din arhive C02 V17 deprecate):
- `data` → folosește `data_factura`
- `cod_client` / `nume_client` → folosește `client_nume`
- `nume_produs` → folosește `produs_nume`
- `cod_agent` / `nume_agent` / `cod_depozit` → nu apar în schema canonică

Aceste denumiri vechi sunt **DEPRECATED V18**. Construcțiile C02 V17,
C03 V17, C04 V17 livrate înainte de V18 sunt valide doar la nivel
intern, dar NU sunt cap-coadă. Vor fi regenerate cu schema canonică
la nevoie.
