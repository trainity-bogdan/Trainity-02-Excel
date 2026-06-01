# D4 · BUILD REPORT — Date_MASTER-C02.xlsx (C02 CONTROL)

> Raport de execuție cap-coadă. Fișierul construit prin `_system/generatoare/build_date_master_c02.py`
> (determinist, seed=42). Realitate curată + 5 anomalii LOCK + semnalizare + reconciliere.

## Fișier
`c02/Date_MASTER-C02.xlsx` — 13 foi.

## Foi
`Vanzari` (corp, 2010 rânduri, 22 coloane) · `CONTACTE` (50 contacte, 13 coloane) ·
`tbl_Localitati` · `tbl_RegulriTVA` · `tbl_SarbatoriLegale` · `tbl_CodJudetCNP` · `_SEMNALIZARE` ·
`CLIENTI` · `PRODUSE` · `AGENTI` · `DEPOZITE` · `_README` · `CONTROL_FINAL` (auxiliare păstrate verbatim).

Tabele Excel (ListObjects) live: `tbl_Vanzari`, `tbl_Contacte` + cele 4 nomenclatoare.

## Anomalii plantate vs detectate (reconciliere independentă)

| Fenomen | Plantate | Detectate | Stare |
|---|---|---|---|
| C02.01 Orașe nealiniate | 50 | 50 | MATCH |
| C02.02 TVA greșit | 47 | 47 | MATCH |
| C02.03 Scadență < Factură | 25 | 25 | MATCH |
| C02.04 NETWORKDAYS (zi nelucrătoare) | 20 | 20 | MATCH |
| C02.05 CNP contradictoriu (contacte) | 25 | 25 | MATCH |

Detaliu C02.05: sex=7, județ=11, dată=6, cifră control=6 (toate MATCH; 5 contacte cu contradicție dublă).
Detaliu C02.02: 35 plantate direct + 12 pe rândurile multi-anomalie (oraș + TVA) = 47.

- Rânduri `Vanzari` afectate (distinct): **130 / 2010 (6.5%)**.
- Rânduri cu anomalii multiple: **12**.
- Reconciliere prin logică independentă (Python) identică formulelor: **zero fals pozitiv, zero fals negativ**.

## Semnalizare (D5, în fișier)
- `Vanzari`: `flag_oras`, `flag_tva`, `flag_scadenta`, `flag_zi`, `status_validare`, `motiv_anomalie` (formule live: COUNTIF + XLOOKUP + NETWORKDAYS.INTL + TEXTJOIN).
- `CONTACTE`: `flag_sex`, `flag_judet`, `flag_data`, `flag_control`, `status_validare`, `motiv_anomalie` (derivare CNP + cifră de control prin SUMPRODUCT cu ponderi 2-7-9-1-4-6-3-5-8-2-7-9).
- `_SEMNALIZARE`: sinteză plantate vs detectate (live COUNTIF) + total de investigat + SUM(valoare_neta).
- Conditional Formatting: rândurile `DE INVESTIGAT` marcate vizual. **CF marchează, NU corectează.**

## Conservarea valorilor sursă (R-V02.14)
- SUM(`valoare_neta`) sursă: **8.018.087,99**
- SUM(`valoare_neta`) după injectare: **8.018.087,99** → **CONSERVATĂ exact**.
- `valoare_neta` moștenită per rând, neatinsă de injectare sau semnalizare. Doar `valoare_tva`/`valoare_totala` recalculate aritmetic (derivate). Datele operaționale (`data_factura`) regenerate în anul operațional 2026, aliniat la `tbl_SarbatoriLegale`; valorile financiare nu au fost regenerate.

## Verificări care au trecut
- `gate_v20.py 02` → **GATE PASS** (schema canonică 14 coloane prezentă; foi auxiliare păstrate; sumă conservată în prag).
- `audit_sync.py` → **ZERO DRIFT — 112/112**.
- Reîncărcare openpyxl → structură validă (13 foi, tabele intacte, CNP-uri 13 cifre text).
- Reconciliere injectat==detectat → toate MATCH.

## Reguli respectate
NU reparat · NU modificat valori sursă după injectare · NU șters · NU prevenit (zero DV ca prevenție, zero DV în cascadă) · NU C03 (variantele de oraș sunt dezacorduri vizibile uman: `Cluj`/`CJ`/`Clum Napoca`/abrevieri/typo — nu spații/diacritice/Unicode invizibil; CNP doar contradicție multi-câmp + cifră de control, niciodată lungime/caractere) · identitate, ordine și anomalii neschimbate.

## Riscuri rămase
1. **Evaluarea formulelor live nu a putut fi rulată cu un motor de calcul în acest mediu** (LibreOffice nefuncțional în sandbox — eșuează și pe fișiere cunoscute bune). Validarea detecției = prin logică Python identică formulelor, nu printr-un engine de spreadsheet. La prima deschidere în Excel se recomandă o verificare vizuală că `_SEMNALIZARE` afișează 50/47/25/20/25.
2. **Formula cifrei de control CNP** folosește `SUMPRODUCT(VALUE(MID(...,{1;...;12},1)),{ponderi})` — pattern standard care funcționează în Excel modern; în Excel foarte vechi (pre-dynamic-arrays) ar putea cere confirmare.
3. **HTML/FILM/Creativ încă pe identitatea veche MARCARE** — neatinse (în afara scopului acestei etape). Date_MASTER e acum pe identitatea CONTROL; restul artefactelor se aliniază la etapele următoare (M3-M6 din planul de execuție).

## Concluzie
Universul de date C02 e construit complet: realitate coerentă + 5 anomalii LOCK injectate controlat + semnalizare live + reconciliere perfectă (plantate==detectate) + sumă financiară conservată exact. GATE PASS, ZERO DRIFT.
