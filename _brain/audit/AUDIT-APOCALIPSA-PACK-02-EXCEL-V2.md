# AUDIT APOCALIPSĂ · PACK 02 EXCEL · V2

> Audit total, adversarial, empiric, mod auditor pur (ZERO reparații, ZERO patch, ZERO commit pe livrabile).
> Rulat de la zero pe starea actuală a `main`, NU pe audituri vechi.
> Data: 4 iunie 2026 · Scope: C01-C12 (toate construcțiile existente) · Branch sursă: `main`.
> HEAD auditat: `e75c243837769d80e2d059ed9cd76c31237d3985` ("fix(c10): hero name MASURI -> MASURA POTRIVITA").
> Working tree: curat (zero modificări necomise la rulare).
>
> Acest V2 succede AUDIT-APOCALIPSA-PACK-02-EXCEL.md (V1), care a rulat când existau doar C01-C09
> (C10-C12 absente/abia livrate). V2 acoperă pachetul complet C01-C12 și reconciliază constatările V1
> care persistă sau s-au închis.

---

## 1. REZUMAT EXECUTIV

**Infrastructura tehnică a pachetului rămâne foarte solidă, dar maturitatea NU e uniformă: T1+T2 (C01-C08) sunt complete și livrabile, T3 (C09-C12) e în diferite stadii de finisare vizuală, cu defecte concrete vizibile.**

Ce e impecabil, confirmat empiric:
- `gate_v20.py` PASS pe toate 12 construcțiile (5/5 livrabile fiecare).
- `pre_generation_check.py` PASS pe toate 12 (SPEC înghețat + IDENTITATE + FENOMENE aliniate).
- `audit_sync.py`: un singur DRIFT (C12 fără folder `assets`); restul zero.
- Conservare sumă cap-coadă PERFECTĂ: reper `7.986.019,38` conservat byte-exact C03 -> C12.
- localStorage namespace unic per construcție, ZERO contaminare de coduri.
- ZERO em-dash / en-dash în tot HTML-ul livrabil.
- Sync Studiu <-> Editor-Studiu perfect pe toate 12 (36/36 pași, 8/8 final-labels).
- 48/48 linkuri index valide.
- Toate 12 pe matrița premium uniformă (hero-visual-overlay).

Problemele reale, concentrate pe T3 și pe câteva reziduuri vechi:
- **C11**: hero-ul din HTML-Studiu este clona byte-identică a hero-ului C01 (STRUCTURARE) pe pagina de COMPARAȚII (instanță a gap-ului L202 deja cunoscut, detector neimplementat).
- **C10 și C12**: imaginile sunt PLACEHOLDER-e SVG (text literal "exec-stage-N · placeholder"), nu fotografii reale; C12 nu are deloc folder `assets`.
- **C06**: HTML-Video (learner-facing) narează cifra business `7.986.019,38 lei` -> încălcare R-V02.15.
- **FILM C01-C04**: conțin cifra business `7.986.019,38 lei` repetat -> încălcare R-V02.15 (în scriptul de producție).
- **C02**: Video <-> Editor-Video desincronizate la imagini (0/6 comune) - MAJOR persistent din V1, NEREPARAT.
- **C09**: breadcrumb de treaptă vechi ("CARTOGRAFIERE · RELAȚII · MĂSURI · CLASAMENT") față de canonicul T3 ("RELAȚII · MĂSURI · COMPARAȚII · INTERPRETARE") afișat corect de C10/C11/C12.
- **Sistemic**: `detect_form_drift.py` (R-V65) raportează FAIL pe forma retorică (PAYOFF/GRESEALA/MANTRA/MOTTO/CINE-DEVII reciclate ca schelet) - parțial semnătură de brand intenționată, cu risc de saturație recunoscut.
- **README.md** grav depășit (declară V40, "5/20 livrate", tag-uri git) față de realitatea V68, 12 construcții.

**Verdict global:** C01-C08 = LIVRABIL (FINAL / FINAL CU MINORE). C09 = APROAPE FINAL (reziduuri de treaptă + assets). C10, C11, C12 = NU FINAL (placeholdere / hero clonă / fără assets). T3 cap-coadă e corect CONCEPTUAL și în date (model -> măsură -> clasament -> explicație confirmat în foile Excel), dar finisajul vizual al T3 este incomplet.

---

## 2. SCOPE ȘI METODĂ

**Construcții auditate:** C01-C12 (12 existente; C13-C20 nu există, în queue).

**Surse citite empiric:** `index.html`, `README.md`, `STARE-CURENTA.md`, `CLAUDE.md`, `COMENZI.yaml`, validatoarele (`audit_sync.py`, `gate_v20.py`, `pre_generation_check.py`, `tier_guard_t3.py`, `detect_c06_purity.py`, `detect_form_drift.py`), `_brain/**` (status C09-C12, audit V1), `_system/governance/**`, toate cele 48 de HTML-uri, toate 12 FILM `.docx`, toate 12 `Date_MASTER-*.xlsx`, `Date_MASTER-initial.xlsx`, toate folderele `assets/`.

**Validatoare rulate:** cele 6 scripturi din `_system/generatoare/` (vezi §3).

**Verificări ad-hoc empirice** (acolo unde validatorul nu acoperă): hash MD5 pe toate imaginile assets, decodare + hash MD5 pe base64-ul embed-uit în HTML (hero Studiu + 6 exec-stage Video), matrice de integritate assets-vs-HTML, analiză Excel (foi, schemă, sumă valoare_neta, nomenclatoare) prin `openpyxl`, extragere text FILM prin `python-docx`, grep cifre business / em-dash / localStorage / cockpit/KPI / breadcrumb / linkuri index.

**Mod auditor pur:** nicio reparație, niciun patch, niciun commit pe livrabile sau pe `_system/**`. Singurul fișier scris = acest raport (`_brain/audit/`).

**Mediu:** `Python 3.11.15`; instalat în sesiune `openpyxl 3.1.5`, `python-docx 1.2.0`, `pillow 12.2.0`, `beautifulsoup4` (nu erau preinstalate; validatoarele au nevoie de `openpyxl` pentru clasa DATA-CONTINUITY).

---

## 3. COMENZI RULATE

```bash
# Sincronizare + confirmare stare
git fetch origin                       # HEAD local == origin/main == e75c243
git pull origin main                   # "Already up to date"
git rev-parse HEAD                     # e75c243...
git status --porcelain                 # gol (working tree curat)

# Validatoare oficiale
python3 _system/generatoare/audit_sync.py                        # DRIFT: 1 (C12 R-V39.assets)
for nn in 01..12: python3 _system/generatoare/gate_v20.py $nn c$nn/ c01/   # 12x PASS
for nn in 01..12: python3 _system/generatoare/pre_generation_check.py $nn  # 12x PASS
python3 _system/generatoare/tier_guard_t3.py --self-test         # PASS (10 cazuri)
python3 _system/generatoare/tier_guard_t3.py c09 c10 c11 c12     # C11 PASS, rest WARNING (0 blocante)
python3 _system/generatoare/detect_c06_purity.py                 # 6/6 PASS
python3 _system/generatoare/detect_form_drift.py                 # VERDICT SISTEM R-V65: FAIL

# Empiric (ad-hoc)
md5sum c*/assets/*.jpg                  # gasit c10==c11 (7/7 identice); c12 fara assets
python3 (decode base64 HTML -> md5)     # hero C11 == hero C01; C10/C12 = SVG placeholder
python3 (openpyxl: foi/schema/suma/nomenclatoare pe cele 12 xlsx + initial)
python3 (python-docx: text FILM + cifre business + arc)
grep (linkuri index / em-dash / localStorage / cockpit/KPI / breadcrumb / cifre)
```

---

## 4. MATRICE MECANICĂ C01-C12 (empiric)

Legendă: OK = prezent/corect · FAIL = lipsă/greșit · PLH = placeholder SVG · CLONĂ = imagine clonată.

| | Studiu | EdStud | Video | EdVideo | FILM | xlsx | assets | LS unic | em-dash | gate | audit_sync |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | OK | OK | OK | OK | OK | OK | OK (8 fișiere) | OK | 0 | PASS | OK |
| C02 | OK | OK | OK | OK | OK | OK | OK (7) | OK | 0 | PASS | OK |
| C03 | OK | OK | OK | OK | OK | OK | OK (7) | OK | 0 | PASS | OK |
| C04 | OK | OK | OK | OK | OK | OK | OK (7) | OK | 0 | PASS | OK |
| C05 | OK | OK | OK | OK | OK | OK | OK (7) | OK | 0 | PASS | OK |
| C06 | OK | OK | cifră business | cifră business | OK | OK | OK (7) | OK | 0 | PASS | OK |
| C07 | OK | OK | OK | OK | OK | OK | OK (7) | OK | 0 | PASS | OK |
| C08 | OK | OK | OK | OK | FILM fără arc | OK | OK (7) | OK | 0 | PASS | OK |
| C09 | OK | OK | OK | OK | FILM fără arc | OK | OK (7, ≠HTML) | OK | 0 | PASS | OK |
| C10 | PLH | PLH | PLH | PLH | FILM fără arc | OK | CLONĂ c11 (nefolosite) | OK | 0 | PASS | OK |
| C11 | hero=CLONĂ C01 | OK | OK | OK | OK | OK | CLONĂ c10 (nefolosite) | OK | 0 | PASS | OK |
| C12 | PLH | PLH | PLH | PLH | FILM fără arc | OK | **FAIL (lipsă)** | OK | 0 | PASS | **FAIL** |

### Matricea celor 30 de verificări obligatorii

| # | Verificare | Verdict | Dovadă scurtă |
|---|---|---|---|
| 1 | Existență livrabile | PASS cu 1 FAIL | gate 5/5 pe toate 12; C12 fără `assets` |
| 2 | Linkuri index valide | PASS | 48/48 fișiere linkuite există |
| 3 | Continuitate Date_MASTER | PASS | schema canonică + nomenclatoare stabile C02-C12 |
| 4 | Sumă conservată cap-coadă | PASS | `7.986.019,38` exact C03->C12 |
| 5 | Foi pierdute / adăugate | PASS cu notă | T3 aditiv cumulativ; `Relatii_Model` (C09) nepropagat la C10-C12 |
| 6 | Studiu vs Editor-Studiu sync | PASS | 36/36 pași, 8/8 final pe toate 12 |
| 7 | Video vs Editor-Video sync | 1 FAIL | C02 0/6 imagini comune; rest IDENTICE / PLH consistent |
| 8 | FILM aliniat cu Video | PASS cu notă | nume + topic aliniate; arc absent C08/C09/C10/C12 |
| 9 | Assets existente | 1 FAIL | C12 fără folder `assets` |
| 10 | Imagini duplicate între construcții | FAIL | c10/assets == c11/assets (7/7 byte-identice) |
| 11 | Hero clonat | FAIL | C11 hero HTML == C01 hero; c10 hero == c11 hero |
| 12 | Base64 suspect | FAIL | C10/C12 = placeholder SVG în loc de fotografii |
| 13 | localStorage unic | PASS | `trainity_cNN_*` corect, zero contaminare |
| 14 | Tokeni vechi / contaminări | 1 FAIL | C09 breadcrumb "CLASAMENT/CARTOGRAFIERE" (T3 vechi) |
| 15 | Cifre business în HTML/FILM | FAIL | C06 video + FILM C01-C04 = `7.986.019,38 lei` |
| 16 | Em-dash / en-dash | PASS (HTML) | 0 în HTML; prezente în docs interne md |
| 17 | Termeni T4/T5 unde nu trebuie | PASS (T3) | tier_guard 0 blocante; C01-C08 au "cockpit/KPI" vizibil (cross-tier) |
| 18 | Dashboard/cockpit/KPI/what-if etc. | PASS cu notă | zero în T3 vizibil; "Cockpit operațional" în footer C01-C08 |
| 19 | Consistență breadcrumb | 1 FAIL | C09 lanț vechi; C02 "STRUCTURARE" vs "STRUCTURĂ" |
| 20 | Cache-bust links | PASS | toate au `?v=N`; necoordonat între construcții |
| 21 | Calitate AHA | MEDIU | R-V65 AHA = singurul slot PASS pe formă |
| 22 | Calitate WOW | MEDIU | R-V65 WOW = WARNING; descriptiv (semnal V1) |
| 23 | Diferențiere între construcții | MEDIU | conținut diferențiat (R-V03.69/71 PASS); formă reciclată (R-V65 FAIL) |
| 24 | Progresie pedagogică T1/T2/T3 | PASS cu notă | T1 secvențial corect; T2 paralel; T3 cumulativ corect |
| 25 | T2 paralel vs secvențial | MEDIU | 4 lentile ortogonale prezentate ca scară (semnal V1) |
| 26 | T3 model->măsură->clasament->explicație | PASS | confirmat în foile Excel cumulative |
| 27 | Release readiness | PARȚIAL | C01-C08 da; T3 nu (vizual incomplet) |
| 28 | Reguli noi necesare | DA | vezi §20 (detector hero clonă, cifre FILM, assets gate) |
| 29 | Top probleme locale | vezi §16 | |
| 30 | Top probleme sistemice | vezi §15 | |

---

## 5. VERDICT PER CONSTRUCȚIE

- **C01 Structurare** - FINAL CU MINORE. Complet, imagini reale (hero+video coincid cu assets). Minor: FILM conține cifra business `7.986.019,38 lei` (R-V02.15).
- **C02 Control** - FINAL CU MINORE. Complet. MAJOR local: Video <-> Editor-Video desincronizate (0/6 imagini comune). Minor: breadcrumb "STRUCTURARE", FILM cifră business, Video cel mai greu (1349 KB).
- **C03 Auditare** - FINAL CU MINORE. Complet, imagini coincid cu assets. Minor: FILM cifră business + format numeric mixt (`7,986,019.38` și `7.986.019,38` în același FILM).
- **C04 Normalizare** - FINAL CU MINORE. Complet. Minor: FILM cifră business. Hero `hero-normalizare.jpg` (nume neconform).
- **C05 Dicționar** - FINAL CU MINORE. Complet. Minor: paralelism T2; video nu coincide cu assets (drift base64-vs-assets, non-vizibil).
- **C06 Clasificare** - FINAL CU REZERVĂ. Complet, dar HTML-Video (learner-facing) narează cifra `7.986.019,38 lei` (R-V02.15, mai grav decât FILM). WOW slab (semnal V1).
- **C07 Datare** - FINAL CU MINORE. Complet, arc FILM prezent.
- **C08 Cartografiere** - FINAL CU MINORE. Complet. Minor: FILM fără arc (ARC/CINE DEVII/DE ACUM absent).
- **C09 Relații** - APROAPE FINAL. Toate 6 artefacte + assets (progres real față de V1). Probleme: breadcrumb T3 vechi; hero din assets (`5e0cceef`) ≠ hero embed-uit în HTML (`8e945d47`); FILM fără arc. (Clona hero=C08 din V1 = ÎNCHISĂ.)
- **C10 Măsuri** - NU FINAL. Structură/Excel/FILM reale, narativ T3 bun, dar TOATE imaginile = placeholder SVG; `assets/` are JPG-uri clonate din c11 dar HTML nu le folosește; FILM fără arc.
- **C11 Comparații** - NU FINAL. Video are 6 imagini reale unice, dar HERO-ul din Studiu = clona byte-identică a hero-ului C01 (STRUCTURARE); `assets/` clonat cu c10, nefolosit de HTML.
- **C12 Interpretare** - NU FINAL. Toate imaginile = placeholder SVG; ZERO folder `assets`; `_brain/c12/CHAT-CONTEXT.md` încă descrie identitatea veche ("KPI/FILTER CONTEXT").

---

## 6. SCORURI PER CONSTRUCȚIE

Scală 0-10. Tehnic = infrastructură/validatoare/date. Pedagogic = claritate parcurs. Narativ = AHA/WOW/voce. Vizual = imagini/hero. Trainity = respect invariante + brand.

```
        TEH  PED  NAR  VIZ  TRA  MEDIE  VERDICT
C01      10    9    8    9    8    8.8   FINAL CU MINORE
C02       7    8    8    7    8    7.6   FINAL CU MINORE
C03      10    7    7    9    8    8.2   FINAL CU MINORE
C04      10    9    8    9    8    8.8   FINAL CU MINORE
C05      10    7    7    9    8    8.2   FINAL CU MINORE
C06       9    7    6    9    6    7.4   FINAL CU REZERVĂ (cifră video)
C07      10    7    7    9    8    8.2   FINAL CU MINORE
C08       9    8    8    9    8    8.4   FINAL CU MINORE
C09       8    8    8    6    7    7.4   APROAPE FINAL
C10       8    8    7    3    6    6.4   NU FINAL (placeholdere)
C11       8    8    7    4    6    6.6   NU FINAL (hero clonă C01)
C12       7    7    7    2    5    5.6   NU FINAL (placeholdere + fără assets)
-----------------------------------------------------------------
MEDIE C01-C08: TEH 9.4 · PED 7.8 · NAR 7.4 · VIZ 8.8 · TRA 7.8 = 8.2 (livrabil)
MEDIE C09-C12: TEH 7.8 · PED 7.8 · NAR 7.2 · VIZ 3.8 · TRA 6.0 = 6.5 (vizual incomplet)
```

Justificări-cheie:
- C06 Trainity 6: cifra business în video (invariant R-V02.15) e în livrabilul văzut de cursant.
- C09 vizual 6: hero assets ≠ hero HTML (drift), restul corect.
- C10/C12 vizual 3/2: placeholdere SVG; C12 fără assets deloc.
- C11 vizual 4: video real, dar hero = imaginea unei alte trepte (C01 Structurare).

---

## 7. AUDIT T1 (C01-C04, SCANARE)

**Status: cel mai matur strat al pachetului. Livrabil.** `gate` + `pre_generation_check` PASS; imagini reale care coincid cu assets (hero+video) pe C01/C03/C04 (C02 are desync Video/Editor-Video); breadcrumb "STRUCTURĂ·CONTROL·AUDIT·NORMALIZARE" consistent (excepție typo C02 "STRUCTURARE").

Progresia pedagogică T1 e secvențială și corectă: structură -> control -> audit -> normalizare. Salt T1->T2 (C04->C05) bine motivat.

**Reziduuri T1:**
- FILM C01-C04 conțin cifra `7.986.019,38 lei` repetat (R-V02.15). Context: narațiunea AGGREGATE/SUM/martor. C05-C12 FILM sunt curate, deci regula a fost aplicată de la C05 încolo dar C01-C04 nu au fost retrofitate.
- C01 nomenclatoare proprii (PRODUSE=12, AGENTI=5, DEPOZITE=4) și sumă proprie `1.247.893,50` - excepție documentată (dataset ERP propriu).
- C02 = singura desincronizare Video/Editor-Video (vezi §16), MAJOR persistent.
- C01 are fișier extra `assets/infografic-excel-01-structura.jpg` (unic, doar C01) + nume hero neconform (`hero-structura.jpg` în loc de `hero-poster-excel-01-...`).

---

## 8. AUDIT T2 (C05-C08, CUNOAȘTERE)

**Status: complet tehnic, livrabil, cu un defect learner-facing pe C06.** `gate` + `pre_generation_check` + `detect_c06_purity` (6/6) PASS. Breadcrumb "DICȚIONAR·CLASIFICARE·DATARE·CARTOGRAFIERE" consistent pe toate 4. Imagini reale.

**Caracterul paralel al T2 (categoria 25):** cele 4 construcții sunt lentile ORTOGONALE de cunoaștere a setului (ce reprezintă fiecare rând / ce clase ascunde / ce memorie temporală are / ce ecosistem îl conține). Sunt prezentate ca o SCARĂ secvențială (breadcrumb cu treaptă curentă bold), deși ordinea nu e obligatorie. Risc pedagogic recunoscut și în V1: cursantul poate crede că e o progresie forțată.

**Defecte T2:**
- **C06 (CRITIC): HTML-Video și Editor-Video narează `7.986.019,38 lei`** (L1955: `instr: "Suma valoare_neta = 7.986.019,38 lei. Conservată din Date_MASTER-initial..."`). Învățatul vede cifra business în video -> R-V02.15.
- C08 FILM fără arc (ARC/CINE DEVII/DE ACUM absent).
- C05/C07/C08 au cele mai joase scoruri de diferențiere de formă (49% fiecare în R-V65).

---

## 9. AUDIT T3 (C09-C12, ANALIZĂ)

**Status: corect conceptual și în date, dar vizual INCOMPLET. NU livrabil ca strat.**

**Ce e corect (confirmat empiric):**
- Lanțul cap-coadă model -> măsură -> clasament -> explicație e implementat CUMULATIV în foile Excel:
  - C09 adaugă `Relatii_Model` (+ `START`, `Regiuni`, `Calendar`)
  - C10 adaugă `Masuri` + `Masuri_Context`
  - C11 adaugă `Comparatii`
  - C12 adaugă `Interpretare`
- Sumă `7.986.019,38` conservată exact pe toate 4.
- `tier_guard_t3` 0 blocante pe toate 4 (C11 chiar PASS curat); granițele T3/T4/T5 ținute (zero dashboard/cockpit/slicer/what-if real în text).
- Verbele-semnătură respectate (C09 a lega, C10 a defini, C11 a compara, C12 a explica).

**Ce e greșit / incomplet:**
- **C09 breadcrumb VECHI:** "CARTOGRAFIERE · RELAȚII · MĂSURI · CLASAMENT" în loc de canonicul "RELAȚII · MĂSURI · COMPARAȚII · INTERPRETARE" pe care îl afișează corect C10/C11/C12. (Tokeni din concepția T3 abandonată - "CLASAMENT" în loc de "COMPARAȚII", și includerea "CARTOGRAFIERE" din T2.)
- **C10 și C12: placeholdere SVG** în loc de fotografii reale (text literal `C10 · exec-stage-N · placeholder`), atât hero cât și 6 exec-stage. HTML-urile lor sunt mici (Video 205 KB vs 700-1300 KB la rest).
- **C12 fără folder `assets`** (singurul DRIFT din `audit_sync`).
- **C11 hero = clona C01.** HTML-Studiu C11 embed-uiește hero-ul `c01/assets/hero-structura.jpg` (md5 `80a50ef5`) pe pagina de COMPARAȚII.
- **Foldere `assets/` C10 și C11 byte-identice** (7/7), dar HTML-urile nu le folosesc (C10 = SVG, C11 = C01-hero + video propriu). Assets orfane.
- **Pipeline assets T3 desincronizat de HTML pe toate 4** (assets ≠ base64 embed-uit la C09, C10, C11; C12 nici n-are assets).
- FILM fără arc la C09, C10, C12.
- `detect_form_drift` (R-V65) NU acoperă C10-C12 (scanează doar C01-C09) - gap de acoperire.

---

## 10. AUDIT CROSS-PACK

**Continuitate date (categoriile 3-5):**
- Schema canonică Vanzari (14 coloane) prezentă pe toate; coloane extra justificate (C06 18 col = scoruri clasificare, C07/C09-C12 15 col = câmp temporal/relațional).
- Nomenclatoare CLIENTI/PRODUSE/AGENTI/DEPOZITE IDENTICE ca dimensiune C02-C12 (15/13/6/5). C01 propriu.
- **Sumă conservată cap-coadă: reper `7.986.019,38` (Date_MASTER-initial) conservat EXACT C03->C12.** C02 Vanzari = `8.018.087,99` (input cu anomalii plantate, +0,40%, sub pragul gate 15%). C01 = `1.247.893,50` (dataset propriu, excepție).
- Foi: T1/T2 folosesc model `_README` + foi specifice; T3 (C09-C12) trece la model `START`/`Regiuni`/`Calendar` + foi cumulative. Foaia `Relatii_Model` (C09) NU e dusă mai departe la C10-C12 (discontinuitate de documentare a modelului, non-blocantă).

**Identitate / contaminare (13, 14, 17, 18):**
- localStorage `trainity_cNN_study` + `trainity_cNN_video`, zero contaminare.
- gate `check_cross_contamination` PASS pe toate (zero coduri străine în text vizibil).
- "cockpit" + "KPI" în text vizibil C01-C08 (footer "Cockpit operațional"); vocabular de tip T4 moștenit de la pilot, scăpat fiindcă T1/T2 nu sunt sub garda T3.

**Diferențiere (21-23):**
- Conținut diferențiat: `audit_sync` R-V03.69 (anti-clonă narativă Studiu) + R-V03.71 (anti-clonă exec Video) PASS pe toate -> zero liste titlare/exec identice literal.
- FORMĂ reciclată: `detect_form_drift` R-V65 FAIL. PAYOFF identic ca schelet la 6/9 ("Nu am X. Nu am Y. Nu am Z."), GRESEALA ("Oamenii X. Profesioniștii Y."), MANTRA/MOTTO/CINE-DEVII clonate parțial. Diferențiere de formă: T1 73%, T2 52%, sistem 65%. (Recontextualizare: STARE-CURENTA confirmă "Oamenii/Profesioniștii" ca semnătură PERMISĂ intenționat, cu risc de saturație notat.)

**Progresie pedagogică (24-26):** T1 secvențial corect; T2 paralel (prezentat ca scară); T3 cumulativ corect (confirmat în date).

---

## 11. ISSUES CRITICAL

**CR-1. C11 hero-ul din HTML-Studiu = clona byte-identică a hero-ului C01.**
`c11/HTML-Studiu-Excel-11-Comparatii.html` embed-uiește `data:image/jpeg;base64,...` care decodează la md5 `80a50ef5` = `c01/assets/hero-structura.jpg`. Cursantul de la COMPARAȚII (T3) vede imaginea de STRUCTURARE (T1). Instanță directă a gap-ului L202 deja documentat ("copy structural cară hero-ul sursei; R-V59 nu acoperă hero Studiu"). Detector neimplementat.

**CR-2. C06 narează cifră business în HTML-Video (R-V02.15, learner-facing).**
`c06/HTML-Video-Excel-06-Clasificare.html` L1955: `instr: "Suma valoare_neta = 7.986.019,38 lei. Conservată din Date_MASTER-initial..."` (idem Editor-Video). Încalcă invariantul "ZERO CIFRE BUSINESS în HTML/FILM". Mai grav decât în FILM fiindcă e în deliverabilul vizionat.

---

## 12. ISSUES HIGH

**H-1. C10 și C12 = imagini placeholder SVG, nu fotografii.** Hero + 6 exec-stage = `data:image/svg+xml;utf8,<svg>...placeholder</svg>` în ambele. Listate ca live în `index.html` (`?v=1`).

**H-2. C12 fără folder `assets`** (singurul DRIFT `audit_sync`, R-V39.assets FAIL). Imaginile există doar ca SVG inline; nicio sursă pe disc.

**H-3. FILM C01-C04 conțin cifra `7.986.019,38 lei` repetat** (R-V02.15 în scriptul de producție). Verificat în cele 4 docx; C05-C12 curate.

**H-4. C02 Video <-> Editor-Video desincronizate la imagini (0/6 comune).** Cele 6 base64 din `HTML-Video-Excel-02-Control.html` au md5 complet diferit de cele din Editor-Video (recomprimate diferit). MAJOR persistent din V1, NEREPARAT. Restul 9 construcții cu imagini reale = IDENTICE; C10/C12 = ambele placeholder consistent.

**H-5. Sistemic: `detect_form_drift` (R-V65) = FAIL pe forma retorică.** Sloturi FAIL: GRESEALA, MANTRA, MOTTO, CINE-DEVII, PAYOFF. Risc de saturație la scară (C13-C20). Parțial semnătură de brand intenționată (decizie BRAIN deschisă).

---

## 13. ISSUES MEDIUM

**M-1. C09 breadcrumb de treaptă vechi:** "CARTOGRAFIERE · RELAȚII · MĂSURI · CLASAMENT" vs canonicul "RELAȚII · MĂSURI · COMPARAȚII · INTERPRETARE" (C10/C11/C12). Tokeni vechi + treaptă T2 amestecată.

**M-2. Foldere `assets/` C10 și C11 byte-identice (7/7 imagini).** Clonă completă (inclusiv hero `2ed32eda`). Nefolosite de HTML (orfane), dar `imagini duplicate între construcții` = FAIL la nivel de disc.

**M-3. Pipeline assets T3 desincronizat de HTML.** La C09 hero assets (`5e0cceef`) ≠ hero HTML (`8e945d47`); C10 assets reale dar HTML = SVG; C11 assets clonate dar HTML = C01-hero + video propriu. Asset-ul de pe disc nu reflectă ce se livrează.

**M-4. FILM fără arc (ARC TRANSFORMARE / CINE DEVII / DE ACUM ÎNAINTE) la C08, C09, C10, C12.** Prezent (total sau parțial) la C01-C07 și C11. Inconsistență de structură narativă FILM (parțial cunoscut: R-V62 notează C06/C08 pending).

**M-5. README.md grav depășit.** Declară "V40 (28 mai)", "5/20 livrate", "ZERO DRIFT 8 reguli x 5 construcții", tag-uri git și branch-per-task. Realitatea: V68, 12 construcții, fără tag-uri (G3), commit direct pe main (G1). Trimite la `GHID-SETUP-GITHUB.md` inexistent la rădăcină.

**M-6. Drift de documentație C12:** `_brain/c12/CHAT-CONTEXT.md` încă descrie C12 ca "KPI/FILTER CONTEXT" (identitate retrasă), nu INTERPRETARE.

**M-7. Foaia `Relatii_Model` (C09) nepropagată la C10-C12** - modelul relațional construit în C09 nu persistă ca foaie în construcțiile care îl folosesc.

---

## 14. ISSUES LOW

- **L-1.** C02 breadcrumb "STRUCTURARE" vs "STRUCTURĂ" (C01/C03/C04) - typo cosmetic.
- **L-2.** Em-dash / en-dash în docs interne md (`CLAUDE.md`, `README.md`, `STARE-CURENTA.md`, `CLAUDE-TO-BRAIN.md`, `WORKSHOP-C10-T3-T4-T5.md`) - contrazic regula "fără dash" dar nu sunt livrabile.
- **L-3.** C02 Video cel mai greu (1349 KB); C03 1286 KB, C06 1257 KB - peste norma de optimizare.
- **L-4.** Cache-bust necoordonat (C01 Studiu `?v=5`/Video `?v=4`; C05 `?v=6`; C09 Studiu `?v=2`, rest `?v=1`).
- **L-5.** Nume hero neconforme: `c01/assets/hero-structura.jpg`, `c04/assets/hero-normalizare.jpg` (vs convenția `hero-poster-excel-NN-{slug}.jpg`).
- **L-6.** C03 FILM folosește format numeric mixt (`7,986,019.38` US și `7.986.019,38` RO).
- **L-7.** Fișier extra unic `c01/assets/infografic-excel-01-structura.jpg` (nicio altă construcție nu are infografic).

---

## 15. PROBLEME SISTEMICE

1. **Detectoare de clonă imagine cu gap real (CONFIRMAT prin C11).** `R-V59.imgclone` verifică doar exec-stage din Video, doar vs C01, doar pe premium. NU prinde: hero clonă în Studiu (C11=C01), clonă între construcții surori (c10==c11), placeholdere SVG. L202 a identificat pattern-ul; detectorul lipsește.
2. **Niciun validator nu verifică cifre business în FILM `.docx` (R-V02.15).** Gate citește doar HTML pentru cifre; FILM C01-C04 + video C06 au scăpat.
3. **gate_v20 nu verifică existența folderului `assets/`.** C12 a trecut gate PASS fără assets (doar `audit_sync` R-V39 a prins).
4. **gate_v20 nu are detector numeric pentru R-V02.15.** `CSS_CONTEXT_PATTERNS`/`NU_VALORI_LEGITIME` sunt definite dar neutilizate; cifra `7.986.019` din C06 video a trecut gate.
5. **`detect_form_drift` (R-V65) acoperă doar C01-C09**, nu C10-C12 - audit de formă orb pe T3 nou.
6. **Saturație de formă retorică (R-V65 FAIL).** PAYOFF/GRESEALA/MANTRA/MOTTO/CINE-DEVII reciclate ca schelet; risc crescând spre C13-C20.
7. **Calitate WOW uniform descriptivă** (semnal V1 persistent; R-V65 WOW = WARNING).
8. **T2 paralel prezentat ca secvențial** (semnal V1 persistent).
9. **Pipeline assets-vs-HTML fără invariant de sincronizare** - assets pe disc pot diverge de base64-ul embed-uit fără ca vreun validator să prindă (C01 video, C05/C07/C08/C09 video, C11 hero).
10. **Vocabular cross-tier nepăzit** ("cockpit"/"KPI" vizibil în C01-C08).

---

## 16. PROBLEME LOCALE

1. **[CR · C11]** hero Studiu = clona C01.
2. **[CR · C06]** cifră business în Video.
3. **[H · C10]** placeholdere SVG (toate imaginile).
4. **[H · C12]** placeholdere SVG + ZERO assets.
5. **[H · C02]** Video/Editor-Video desync (0/6).
6. **[M · C09]** breadcrumb T3 vechi (CLASAMENT/CARTOGRAFIERE).
7. **[M · C09]** hero assets ≠ hero HTML.
8. **[M · C10+C11]** assets byte-identice (clonă) + orfane.
9. **[M · C12]** CHAT-CONTEXT identitate veche (KPI/FILTER).
10. **[L · C02]** typo breadcrumb "STRUCTURARE".
11. **[L · C01/C04]** nume hero neconforme.

---

## 17. CE SE POATE REPARA AUTOMAT

- Fix breadcrumb C09 (search-replace la lista sm-step -> "RELAȚII·MĂSURI·COMPARAȚII·INTERPRETARE").
- Fix typo breadcrumb C02 ("STRUCTURARE" -> "STRUCTURĂ", 1 string).
- Scoatere/generic-izare cifră `7.986.019,38 lei` din C06 video + Editor-Video și din FILM C01-C04 (search-replace -> "suma conservată" fără cifră).
- Re-sync C02 Video/Editor-Video (copiere identică a celor 6 base64 din Video în Editor-Video) + reoptimizare.
- Eliminare assets clonate orfane c10/c11 SAU înlocuire cu placeholdere coerente.
- Redenumire hero-uri neconforme C01/C04 la convenția standard.
- Normalizare format numeric FILM C03 (RO peste tot).
- Cei 4-5 detectoare noi (vezi §20) - stdlib only, integrabile în `audit_sync`/`gate_v20`.

## 18. CE NECESITĂ DECIZIE BRAIN

- **R-V65 / saturație de formă:** se diversifică matrițele retorice (PAYOFF/GRESEALA/MANTRA) înainte de C13, sau se confirmă ca semnătură permisă cu risc acceptat?
- **Cifre business "de proces" (`7.986.019,38`):** sunt interzise strict de R-V02.15 inclusiv în narațiunea de verificare a conservării (T1/C06), sau martorul de conservare e o excepție acceptată?
- **T2 paralel vs secvențial:** recadrare ca "4 lentile" sau păstrare ca progresie?
- **Calitate WOW:** prag impus (revizuire C06/C07) sau acceptare?
- **Breadcrumb T3 pentru construcții afișate dar incomplete** (C10/C12 placeholder): se afișează ca live sau se marchează "în lucru"?

## 19. CE NECESITĂ ARHITECT

- **Imagini reale C10 și C12** (hero + 6 exec-stage fiecare) - acum placeholdere SVG; pipeline-ul extern de imagini (ChatGPT/Banana) nu a fost finalizat pentru ele.
- **Hero real C11** (acum = imaginea C01) și hero coerent C09 (assets ≠ HTML).
- **Decizie finisaj T3:** se promovează C09-C12 la "FINAL" doar după imagini reale, sau se acceptă un release intermediar cu placeholdere?
- Confirmare scoatere cifre business din FILM C01-C04 + C06 (atinge narațiunea pedagogică).

## 20. CE NECESITĂ MODIFICARE DE SISTEM

- **R-NOUĂ (hero Studiu anti-clonă):** extinde `R-V59.imgclone` să verifice hero-ul base64 din HTML-Studiu (md5) vs C01 și vs construcțiile surori. (Ar fi prins C11=C01.)
- **R-NOUĂ (clonă assets cross-construcție):** detector md5 între folderele `assets/` (ar fi prins c10==c11).
- **R-NOUĂ (placeholder vs imagine reală):** flag dacă HTML embed-uiește `data:image/svg+xml` în sloturile hero/exec-stage (ar fi prins C10/C12).
- **R-NOUĂ (cifre business în FILM):** extinde detectorul R-V02.15 să citească `.docx` (ar fi prins FILM C01-C04).
- **R-NOUĂ (cifre business numerice în gate):** activează detectorul numeric pe HTML-Video (ar fi prins C06).
- **gate_v20 + assets:** include verificarea folderului `assets/` în gate (azi doar `audit_sync` o face).
- **Extinde `detect_form_drift` la C10-C12** (azi se oprește la C09).
- **Sync assets <-> HTML:** invariant care cere ca base64-ul embed-uit = md5-ul fișierului din `assets/`.
- **Actualizare README.md** la starea reală (V68, 12 construcții, fără tag-uri, commit pe main).

## 21. ORDINEA RECOMANDATĂ DE REPARAȚII

**Faza 1 - defecte vizibile learner-facing (CRITICAL):**
1. C11: înlocuire hero clonă C01 cu hero real C11 (sau placeholder neutru până la imagine).
2. C06: scoatere cifră `7.986.019,38 lei` din Video + Editor-Video.

**Faza 2 - finisaj T3 (HIGH):**
3. C10 + C12: imagini reale (ARHITECT) + creare `assets/` C12.
4. C09: fix breadcrumb T3 + aliniere hero assets/HTML.
5. C02: re-sync Video/Editor-Video.

**Faza 3 - igienă + invariante (MEDIUM/LOW):**
6. FILM C01-C04: generic-izare cifră business.
7. README.md update; CHAT-CONTEXT C12 update.
8. assets clonate c10/c11; nume hero C01/C04; typo C02; format FILM C03.

**Faza 4 - sistem (detectoare noi §20)** ca aceste clase să nu mai scape.

## 22. VERDICT FINAL

**C01-C08 (T1+T2) = LIVRABIL** (medie 8.2; infrastructură impecabilă; minore de igienă). Două rezerve de invariant: cifra business în FILM C01-C04 și în VIDEO C06 (R-V02.15) - de decis dacă "martorul de conservare" e excepție acceptată sau încălcare de reparat.

**C09 (T3) = APROAPE FINAL** - progres real față de V1 (toate 6 artefacte + assets); rămân breadcrumb vechi + drift hero assets/HTML.

**C10, C11, C12 (T3) = NU FINAL** - finisaj vizual incomplet: C10/C12 placeholdere SVG (C12 fără assets), C11 hero = clona C01. Conceptual și în date (model -> măsură -> clasament -> explicație) sunt CORECTE și cap-coadă; problema e exclusiv stratul vizual + un reziduu de breadcrumb.

**Cea mai valoroasă descoperire de sistem (confirmă V1):** gap-ul detectoarelor de clonă/placeholder imagine este REAL și încă deschis. V1 a prezis-o (R-NOUĂ-1, L202); C11=C01 și C10/C12=placeholder o confirmă pe pachetul nou. Plus gap-uri noi: cifre business în FILM/Video nepăzite, assets neverificate de gate.

**Conservarea datelor cap-coadă (`7.986.019,38` exact C03->C12) este punctul cel mai puternic al pachetului** - invariantul R-V02.14 ținut perfect.

**Nicio reparație, niciun patch, niciun commit pe livrabile aplicate în această rundă.** Raport pur, conform mandatului.

---

AUDIT_APOCALIPSA_V2_DONE
