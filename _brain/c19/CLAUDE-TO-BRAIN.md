# CLAUDE -> BRAIN C19

## STATUS
C19_GENERARE_SLICE_1_DATE_MASTER (GO acceptat; Date_MASTER-C19 cu `_GUVERNARE` generat si verificat cap-coada; restul artefactelor in slice-uri urmatoare; NU release complet)

SURSA: comanda `sync`, mandat `GO_GENERARE_EFECTIVA_C19` (origin/main 9eaf4e2). Generare in slice-uri, ca C18 (Slice 1, Slice 2-4). Acest slice = Date_MASTER (inima T5). Permisiuni operationale ridicate folosite: creat `c19/`.

---

## ARTEFACTE GENERATE
- **`c19/Date_MASTER-C19.xlsx`** - GENERAT + verificat (Slice 1).
- **`c19/build_date_master_c19.py`** - build script (reproductibil).
- HTML-Studiu / HTML-Editor-Studiu / HTML-Video / HTML-Editor-Video / FILM / assets = **NEGENERATE** (slice-uri urmatoare).

## SURSA COPY+MODIFY
Chain T5 = **`c18/Date_MASTER-C18.xlsx`** (predecesorul direct; R-V02.14: input C19 = output C18). Pattern = build-script, oglinda `c17/build_date_master_c17.py` (deschid Date_MASTER-ul precedent, pastrez TOATE foile intacte, adaug START + foaia-artefact). Pentru HTML (slice 2) decid intre pattern build-script c17 si COPY+MODIFY din c01 (ca C18); raportez ce folosesc.

## IDENTITATE C19 IMPLEMENTATA
In Date_MASTER (foile START + `_GUVERNARE`): HERO "Cum se tine corect fara ochiul meu?", AHA, MANTRA "Nu o supraveghez. O guvernez prin reguli.", MOTTO "Pleci, si munca se tine singura." (in START). Axa CONTROL, verb GUVERNEZ, artefact `_GUVERNARE`. Identitatea HTML/FILM (cover, topbar, 18 pasi) = slice-uri urmatoare, din IDENTITATE_TEHNICA C19 (deja in registru).

## DATE_MASTER / _GUVERNARE
`Date_MASTER-C19.xlsx`: 10 foi = START + `_GUVERNARE` + cele 8 mostenite de la C18 (intacte). 8 named ranges.
**`_GUVERNARE`** (controlul, nativ-Excel pe `Vanzari_Curat`):
- A PRAGURI vii: `LIMIT_CANT_MIN/MAX`, `LIMIT_VAL_MIN`, `LIMIT_TOL`.
- B DIAGNOSTIC: `TOTAL_INREGISTRAT`=SUM(valoare_neta), `TOTAL_CONSISTENT`=SUMPRODUCT(cant,pret), randuri_inconsistente, randuri_nepozitive, cantitati/categorii in afara.
- C REGULI / Data Validation la sursa: 3 reguli (cantitate interval `LIMIT_`, pret>0, categorie din lista) care RESPING intrarea gresita.
- D SEMNALE: 5 reguli -> OK/ATENTIE/OPRIT.
- E STARE: `STATUS_SISTEM` (IFS pe semnale) + conditional formatting verde/galben/rosu.
- F EXCEPTII: lista cu nr. cazuri vii (marcheaza, NU desemneaza responsabil).
- G FAIL-SAFE: `OUTPUT_GUVERNAT` = IF(STATUS=OPRIT, rezultat retinut, total validat) -> rezultatul corupt nu curge.
- H GRANITE/GARDA/testul ochilor inchisi.

**Demonstratie autentica:** datele mostenite de la C18 contin 2 randuri imposibile plantate (rand 1147 valoare_neta=-5.725.878,84; rand 1148 = +2.865.117,29; ambele cant=126, != cant x pret). Motorul (C18) le-a insumat tacut (total inregistrat 1.247.893,50, cand consistenta da ~4,11M). `_GUVERNARE` le prinde prin consistenta rand + inchiderea totalului + valoare>0 -> **STATUS=OPRIT** -> fail-safe BLOCHEAZA rezultatul. Exact ce face C19.

## VALIDARI RULATE
- `pre_generation_check.py 19`: **TOATE PASS** (SPEC INGHETAT + IDENTITATE POPULATA + FENOMENE ALINIAT).
- **R-V02.14 suma conservata: PASS** - SUM(Vanzari_Curat.valoare_neta) = 1.247.893,50 = C18 (verificat).
- **`_GUVERNARE` distinct de `_AUTOMATIZARE`: PASS** (foaie noua; lineage c01 nu are `_AUTOMATIZARE` in Date_MASTER).
- **STATUS OK/ATENTIE/OPRIT: PREZENT + evaluat** (mirror Python al formulelor pe date reale = OPRIT, prinde anomaliile; logica corecta).
- **Data Validation la sursa: PASS** (3 reguli active pe zona de intrare).
- **Fail-safe: PASS** (`OUTPUT_GUVERNAT` legat de `STATUS=OPRIT`).
- **OOXML valid: PASS** (zip testzip + openpyxl full round-trip).

## VALIDARI NERULATE / PROBLEME
- `gate_v20.py 19`: **NU_RULAT** - necesita toate cele 7 artefacte canonice; doar Date_MASTER exista. De rulat la finalul slice-urilor.
- `audit_sync.py` pe C19 complet: **NU_RULAT** (de rulat la final).
- Recalc LibreOffice: **NU_RULAT** - LibreOffice headless nu incarca fisierul in acest mediu (eroare "source file could not be loaded" + warning Java). Evaluarea formulelor verificata prin mirror Python + validitate OOXML confirmata. Excel + gate_v20 (openpyxl) il incarca corect.
- imgclone (hash != c01): **NU_RULAT** (imagini negenerate).
- verificare em/en-dash artefacte HTML/FILM: **NU_RULAT** (negenerate; textul Date_MASTER e fara em/en-dash).

## STATUS IMAGINI
**NEGENERATE.** Necesita cele 7 imagini GUVERNARE (hero + 6 exec-stage, axa CONTROL) de la ARHITECT. La generarea HTML (slice urmator) folosesc fallback DRAFT marcat -> `DRAFT_IMAGINI_FALLBACK`.

## STATUS RELEASE
**NU release complet.** Slice 1 din generare (Date_MASTER). Lipsesc 4 HTML + FILM + assets. Imaginile vor fi fallback pana le produce ARHITECT. `DRAFT`.

## RISCURI RAMASE
1. STATUS=OPRIT by default = INTENTIONAT (demonstratia C19 prinde anomaliile plantate din datele C18). Daca C18 isi curata Date_MASTER, regenerez (chain).
2. Slicing: cele 7 artefacte se livreaza impreuna la final (R-V01.2); pana atunci = work-in-progress, nu release.
3. Branch de sesiune divergent; commit pe main aliniat.

## CERERI CATRE BRAIN / SYSTEM
- **Catre ARHITECT:** cele 7 imagini GUVERNARE (le procesez la sosire: watermark scos, base64 inline, hash != c01).
- La urmatorul `sync` continui cu Slice 2 (HTML-Studiu + companion), apoi Video/Editor-Video, FILM, assets.
- **CERERE SYSTEM:** niciuna.

## COMMIT
Commit pe `main`: `feat(c19): Slice 1 - Date_MASTER-C19 cu _GUVERNARE (STATUS/DV/praguri/exceptii/fail-safe), suma conservata`. SHA in git log.

**C19_GENERARE_SLICE_1_DATE_MASTER**
