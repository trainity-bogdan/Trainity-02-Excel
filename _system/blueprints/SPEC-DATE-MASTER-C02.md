# SPEC TEHNIC · Date_MASTER-C02 + implementare pedagogică

> Specificație de implementare, NU HTML / NU copy. Pereche cu `BLUEPRINT-C02-CONTROL.md`.
> Identitate + anomalii + ordine = LOCK. Aici se specifică DATELE și REGULILE de semnalizare.
> Principiu: C02 **semnalează / demonstrează / construiește dovezi** — NU repară / modifică / șterge / previne.
> Bază presupusă: ~2000 tranzacții în `Vanzari` (aliniat packului). Valoarea_neta = invariant (semnalizarea NU modifică valori — R-V02.14/15).

---

## 1. STRUCTURA Date_MASTER-C02 (foi)

| Foaie | Rol |
|---|---|
| `Vanzari` | setul principal de tranzacții (input + coloane de semnalizare adăugate) |
| `CONTACTE` | satelit nou — persoane de contact ale clienților (gazda CNP iconic) |
| `tbl_Localitati` | nomenclator oraș↔județ oficial (C02.01) |
| `tbl_RegulriTVA` | nomenclator categorie→cotă TVA legală (C02.02) |
| `tbl_SarbatoriLegale` | calendar sărbători legale (C02.04) |
| `tbl_CodJudetCNP` | nomenclator cod-județ-CNP → județ (C02.05) |
| `_SEMNALIZARE` | foaia de profil generată — sinteza anomaliilor semnalate (livrabilul vizibil) |
| `_README` · `CONTROL_FINAL` | existente, păstrate |

## 2. COLOANE `Vanzari`

**Existente (păstrate):** `nr_factura, data_factura, client_nume, judet, cod_produs, produs_nume, categorie, cantitate, pret_unitar, valoare_neta, cota_tva, valoare_tva, valoare_totala, moneda`.

**De ADĂUGAT (input):**
- `oras` (text) — orașul declarat al tranzacției → C02.01.
- `data_scadentei` (dată) — scadența facturii → C02.03.

**De ADĂUGAT (semnalizare / output — generate prin formule, NU modifică datele):**
- `flag_oras` · `flag_tva` · `flag_scadenta` · `flag_zi` (text/boolean per fenomen).
- `status_validare` (OK / DE INVESTIGAT) · `motiv_anomalie` (concatenarea flag-urilor active).

## 3. COLOANE `CONTACTE` (satelit, gazda CNP)

`id_contact, client_nume (FK), nume_persoana, CNP, Sex, Judet, Data_Nasterii`
+ coloane de semnalizare: `flag_sex, flag_judet, flag_data, flag_control, status_validare, motiv_anomalie`.
*(CNP trăiește pe persoane de contact, NU pe rândurile B2B de vânzare — fit mai natural decât pe `Vanzari`. CNP = iconic, injectat conștient, decizie V58.)*

## 4. TABELE SATELIT / NOMENCLATOARE

| Tabel | Coloane | Conținut |
|---|---|---|
| `tbl_Localitati` | `oras_oficial, judet` | lista oficială oraș↔județ (ex. Cluj-Napoca→Cluj, Brașov→Brașov...) |
| `tbl_RegulriTVA` | `categorie, cota_legala` | ex. Alimente→9%, Hardware→19%, Servicii→19%... |
| `tbl_SarbatoriLegale` | `data, denumire` | sărbătorile legale ale anului setului (ex. 13.04.2026 = a 2-a zi de Paște) |
| `tbl_CodJudetCNP` | `cod, judet` | 01→Alba ... 12→Cluj ... 40-46→București ... 51→Călărași etc. |

## 5. ANOMALII CONCRETE per fenomen

### C02.01 ORAȘE NEALINIATE
- (a) **Scriere inconsecventă:** aceeași localitate ca „Cluj" / „CJ" / „Cluj-Napoca" / „Clum Napoca" (typo). Valoare validă ca text, neoficială.
- (b) **Oraș↔județ imposibil:** `oras`=Brașov, `judet`=Constanța (combinație care nu există).

### C02.02 TVA GREȘIT
- `categorie`=Alimente (cotă legală 9%) dar `cota_tva`=19%. Număr valid, greșit fiscal.

### C02.03 SCADENȚĂ < FACTURĂ
- `data_factura`=15.05.2026, `data_scadentei`=10.05.2026. Ambele date valide, ordine imposibilă.

### C02.04 ZI NELUCRĂTOARE
- `data_factura`=13.04.2026 (a 2-a zi de Paște, sărbătoare legală) sau o duminică. Dată validă, firma închisă prin lege.

### C02.05 CNP CONTRADICTORIU (iconic, pe `CONTACTE`)
- (a) **Sex:** prima cifră CNP indică M, `Sex`=F.
- (b) **Județ:** cifrele 8-9 → cod 40 (București), `Judet`=Cluj.
- (c) **Dată:** AALLZZ din CNP ≠ `Data_Nasterii` declarată, sau dată imposibilă (ex. luna 13 / ziua 32).
- (d) **Cifra de control:** algoritm oficial → cifra a 13-a calculată ≠ cifra prezentă.
*(Pot coexista mai multe pe același CNP — realist. Anti-drift: NU lungime≠13 / caractere alfabetice = C03.)*

## 6. DISTRIBUȚIA anomaliilor (teaching density, ~2000 rânduri)

| Fenomen | Nr. rânduri afectate | % | Note |
|---|---|---|---|
| C02.01 Orașe | ~50 | 2.5% | mix (a) scriere + (b) oraș-județ |
| C02.02 TVA | ~35 | 1.75% | |
| C02.03 Scadență | ~25 | 1.25% | |
| C02.04 Zi nelucrătoare | ~20 | 1.0% | sărbători + duminici |
| C02.05 CNP | ~25 din ~50 contacte | — | densitate mare ca să demonstreze toate 4 verificările |

- **Total `Vanzari` afectat:** ~130 rânduri (~6.5%) — găsibil, nu copleșitor.
- **Rânduri cu MAI MULTE anomalii** (realist): ~10-15 (ex. oraș greșit + TVA greșit). De plantat intenționat, pentru a arăta că o celulă poate purta mai multe boli.
- Restul: rânduri curate, ca semnalul să iasă în evidență.

## 7. REGULI DE SEMNALIZARE (formule de detecție — NU corectează)

```
flag_oras (scriere):   =IF(COUNTIF(tbl_Localitati[oras_oficial],[@oras])=0, "ORAS NEALINIAT", "")
flag_oras (județ):     =IF(XLOOKUP([@oras],tbl_Localitati[oras_oficial],tbl_Localitati[judet],"?")<>[@judet], "JUDET NECORESPUNZATOR", "")
flag_tva:              =IF(XLOOKUP([@categorie],tbl_RegulriTVA[categorie],tbl_RegulriTVA[cota_legala])<>[@cota_tva], "TVA GRESIT", "")
flag_scadenta:         =IF([@data_scadentei]<[@data_factura], "SCADENTA INAINTEA FACTURII", "")
flag_zi:               =IF(NETWORKDAYS.INTL([@data_factura],[@data_factura],1,tbl_SarbatoriLegale[data])=0, "ZI NELUCRATOARE", "")
status_validare:       =IF(motiv_anomalie="", "OK", "DE INVESTIGAT")
```
**CNP (`CONTACTE`):**
```
sex_derivat:    din prima cifră CNP (1/3/5/7=M, 2/4/6/8=F, +secol)  → flag_sex daca ≠ Sex
judet_derivat:  XLOOKUP(MID(CNP,8,2), tbl_CodJudetCNP[cod], [judet]) → flag_judet daca ≠ Judet
data_derivata:  din secol + MID(CNP,2,6) (AALLZZ) → flag_data daca ≠ Data_Nasterii sau dată imposibilă
control:        suma(cifra_i * pondere_i) mod 11, ponderi 2-7-9-1-4-6-3-5-8-2-7-9, regula 10→1 → flag_control daca ≠ cifra 13
```
**Toate flag-urile = coloane derivate de semnalizare. NICIUNA nu rescrie valoarea originală (R-MET-1).**

## 8. UTILIZAREA Advanced Filter (DESCOPERIRE)
- **C02.01:** AF „copy to another location, unique records only" pe `oras` → extrage **nomenclatorul real existent** (toate scrierile). Acesta e materialul brut din care business-ul decide forma oficială. *AF e arma centrală a C02.01.*
- Extragerea excepțiilor (rânduri cu `status_validare="DE INVESTIGAT"`) pentru raportul de investigație.

## 9. UTILIZAREA Conditional Formatting (SEMNALIZARE)
- Regulă pe `status_validare` = „DE INVESTIGAT" → fundal de atenție pe rând.
- Reguli per flag (opțional, granular): colorează celula `oras`/`cota_tva`/`data_scadentei`/`data_factura` când flag-ul corespunzător e activ.
- Pe `CONTACTE`: colorează componenta CNP inconsistentă (sex/județ/dată/control).
- **Rol: marchează vizual ce necesită decizie — NU corectează.**

## 10. UTILIZAREA Data Validation — vezi secțiunea dedicată.

---

# DV ca PREVENȚIE vs DV ca ERGONOMIE (secțiune dedicată — cerință explicită)

## Cele două utilizări

| | DV ca PREVENȚIE | DV ca ERGONOMIE / FORMALIZARE |
|---|---|---|
| Intenția | „Nu te las să alegi greșit" — blochează intrarea viitoare | „Iată lista oficială, pentru uz comod și consecvent" |
| Orientare | spre VIITOR (apără datele ce vor veni) | spre PREZENT (formalizează decizia deja luată) |
| Moment | *înainte* de a ști ce e corect | *după* descoperire (AF) + curățare + aprobare business |
| Rol | gardian permanent | artefactul utilizabil al nomenclatorului aprobat |
| Treaptă | **T5** (prevenție / control permanent) | **C02** (formalizarea livrabilului) |

## Unde DV este T5 (INTERZIS în corpul C02)
- DV ca **scop** al construcției („să închidem poarta").
- DV **în cascadă / dependentă** (oraș filtrat după județ) — face simultan comoditate ȘI **împiedică combinații invalide viitoare** = mecanism de prevenție. Aparține T5.
- Orice cadru care prezintă DV ca „așa eviți problema pe viitor".

## Unde DV este C02 (PERMIS, marginal)
- DV ca **pas final, de ~30 secunde**, DUPĂ ce: AF a descoperit nomenclatorul → business a decis forma oficială → s-a aprobat.
- DV **simplă, o singură listă** (`tbl_Localitati[oras_oficial]`), oferită ca **dropdown de comoditate** pentru uz consecvent.
- Cadrul corect: „acum că ai nomenclatorul oficial **aprobat**, îl pui la dispoziție ca listă, ca utilizatorul să-l folosească ușor și consecvent" = **formalizarea livrabilului**, nu prevenție.

## Zona gri (și cum o tratăm)
- **DV în cascadă (oraș după județ):** comoditate (ergonomie) DAR și împiedicare de combinații (prevenție). **Verdict: înclină T5.** Ține-o AFARĂ din corpul C02. Dacă apare, doar ca mențiune-bonus („se poate face și o listă dependentă — dar aceea e teritoriu de automatizare, T5"), niciodată ca pas demonstrat.
- **DV care respinge valori invalide la tastare:** e prevenție → T5.

## VERDICT EXPLICIT privind rolul DV în C02

**DV ESTE permis în C02, dar STRICT ca ergonomie/formalizare:** ultimul pas marginal al lui C02.01, care **formalizează nomenclatorul oficial aprobat** ca listă derulantă simplă, pentru uz comod și consecvent. NU e competența, NU e tema, NU e scopul.

**DV NU este permis în C02 ca prevenție:** orice utilizare orientată spre „blocarea intrării viitoare" sau orice DV **în cascadă/dependentă** = **T5**, în afara construcției.

**Recomandare de implementare (de trecut în corpul C02.01):**
- Competența predată = **AF (descoperire) + CF (semnalizare)**. Acolo stă lecția.
- DV apare **o singură dată, la final, ca listă simplă**, încadrat explicit ca „**formalizarea nomenclatorului aprobat**, pentru ergonomie" — nu ca „prevenție".
- **Interzis în corp:** DV în cascadă, DV ca scop, DV ca „așa previi pe viitor".
- Linia de demarcație de pus în text (la copy, ulterior): *„C02 descoperă și semnalează; formalizarea aprobată o pui la dispoziție comod. A o transforma în gardian permanent care apără datele viitoare e treaba treptei de automatizare (T5)."*

---

## OBSERVAȚII (notate separat — NU redeschid arhitectura)
1. **CNP pe satelitul `CONTACTE`**, nu pe `Vanzari` — fit mai natural (B2B). Refinare de implementare a deciziei „CNP iconic injectat".
2. **`data_scadentei` + `oras`** = singurele coloane noi pe `Vanzari`; restul anomaliilor folosesc coloane existente + nomenclatoare satelit.
3. **Sumă conservată:** semnalizarea adaugă DOAR coloane de status; `valoare_neta` rămâne invariant. De confirmat numeric la implementare (R-V02.14).
4. **Implementare HTML + rescriere Date_MASTER:** PENDING. Acest spec = target. Corpul c02/ e încă versiunea veche MARCARE.
