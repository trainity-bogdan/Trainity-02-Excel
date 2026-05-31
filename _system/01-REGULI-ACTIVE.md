# Reguli active Trainity · Sursa de adevăr

Versiune: V38 · 27 mai 2026

Acest document conține **doar regulile vii**, distilate din arhiva V01-V38. Fiecare regulă are:
- **Cod**: R-V0X.Y (cod canonic)
- **Nume scurt**: ce face în 1 frază
- **Status**: ACTIVĂ / ABSORBITĂ / ABANDONATĂ
- **Detector** (opțional): cum se verifică empiric

Regulile **ABSORBITE** sunt cele care au fost extinse/modificate de alte reguli — păstrăm referința dar implementarea trăiește în regula nouă.

Regulile **ABANDONATE** sunt cele care au fost explicit eliminate (ex: PPT, formate vechi).

---

## Cele 6 categorii

| # | Categoria | Câte reguli |
|---|---|---|
| **A** | Permanente nucleu (R-V01.x) | 6 |
| **B** | Tehnice fundamentale (R-V02.x) | 11 |
| **C** | Livrabile și nomenclatură (R-V03.1-5, R-V03.47-50) | ~10 |
| **D** | Pre-generation checks (R-V03.37-45) | ~9 |
| **E** | Gate-uri și audit (R-V03.39, 45, 48, 50, 53, 63) | ~6 |
| **F** | Workflow și fluxuri (R-V03.51-56) | ~6 |
| **G** | Stratificate runtime (R-V03.58-65) | ~7 |

**Total: ~55 reguli active + abandonate marcate.**

---

# A. REGULI PERMANENTE NUCLEU

Acestea NU se schimbă niciodată. Sunt fundament Trainity.

## R-V01.1 · TAG LA INCREMENTARE V
**Status:** ACTIVĂ permanentă (V41 update: git tag, NU folder snapshot)
La `consolideaza brain` / incrementare V, motor creează tag git anotat `v{N}` cu sumar în mesaj, apoi `git push --tags`. Permite `git checkout v{N}` pentru rollback complet la orice versiune oficială. Vezi CLAUDE.md „VERSIONARE GIT" regula G3.

**Istoric:** pre-V40 arhive zip OUT-V{N}.zip; V40 a încercat folder snapshots `_system/snapshots/V{N}_AAAALLZZ/` bazat pe presupunerea greșită OneDrive; V41 revine la git tag (idiomatic).

## R-V01.2 · LIVRARE TOATE ODATĂ
**Status:** ACTIVĂ permanentă (EXTINSĂ V04 la 7 artefacte, V30 la includere FILM+assets)
La livrarea unei construcții, toate cele 7 artefacte trebuie generate și verificate înainte de present_files. Niciodată parțial.

## R-V01.3 · EDITABIL = LIVRABIL CANONIC AUTOMAT
**Status:** ACTIVĂ permanentă
HTML-Editor-Studiu și HTML-Editor-Video sunt parte din cele 7 livrabile canonice, nu accesorii.

## R-V01.5 · CHECK-IN CONSTRUCȚIE SIMULTAN
**Status:** ABSORBITĂ în R-V03.51 (acceptarea check-in implicit la generare directă)
**Pre-refactor V38:** chat-urile `CHECKIN CONSTRUCTIE NN` rulau paralel cu plan zip-arhivare. **Post-V38:** workflow simplificat — generare directă în `cNN/`, audit, commit + push la finalizare (workflow git V41).

## R-V01.7 · F-BIS ANOMALY-GRID PARAMETRIZAT
**Status:** ACTIVĂ permanentă
Grila de anomalii din HTML-Studiu este parametrizată per construcție (nu hardcodată), reușește auto-update la modificări în datele input.

## R-V01.9 · BUTON `VERIFICA ETAPA` POST-CLICK
**Status:** ACTIVĂ permanentă
Fiecare step din HTML-Studiu are buton `VERIFICĂ` care, după click, schimbă vizual (background, icon) ca să marcheze pasul completat.

---

# B. REGULI TEHNICE FUNDAMENTALE

## R-V02.0 · NUMIRE ARHIVE CHECKOUT
**Status:** ABSORBITĂ în R-V01.1 (git tag v{N} în loc de zip arhive sau folder snapshot).

## R-V02.2 · DIACRITICE ROMÂNEȘTI
**Status:** ACTIVĂ permanentă
Toate textele Trainity folosesc diacritice românești corecte (ă, â, î, ș, ț). Validate empiric prin grep.

## R-V02.3 · GATE 3 OBLIGATORIU — COERENȚĂ FILM + HTML
**Status:** ACTIVĂ permanentă (PPT eliminat V11+)
FILM.docx, HTML-Studiu și HTML-Video trebuie să fie coerente narativ (același HOOK, aceeași MIZA, aceleași 6 etape).

## R-V02.5 · STORAGE KEYS + EXPORT FILENAME IZOLATE
**Status:** ACTIVĂ permanentă
Fiecare construcție folosește chei localStorage și nume export specifice (CNN), niciodată generice. Previne contaminare cross-browser între tabs.

## R-V02.6 · PATTERN COPY-MODIFY GENERATOARE
**Status:** ACTIVĂ permanentă
Generatoarele pentru C02-C20 sunt clone-modificate ale generatorului pilot C01 V12. Niciodată rescriere de la zero. Vezi R-V03.54 pentru detalii operaționale.

## R-V02.7 · VOCABULAR ARHITECTURAL LA ÎNCHIDERE TREAPTĂ
**Status:** ACTIVĂ permanentă
La ultima construcție din fiecare treaptă (C04, C08, C12, C16, C20), HTML-ul include vocabular care închide pedagogic treapta ("am completat treapta SCAN", "am cunoscut setul cap-coadă", etc.).

## R-V02.9 · NUMĂR PROMPTURI COPILOT = COUNT FIZIC
**Status:** ACTIVĂ permanentă
Gate v20 verifică: `count(.prompt-box) în HTML-Studiu == count în Creativ.txt`. Niciodată un prompt nu poate fi inventat sau pierdut.

## R-V02.11 · CUVINTE INTERZISE CU CONTEXT AWARENESS
**Status:** ACTIVĂ permanentă
Lista vocabularului interzis (curs, cursant, lecție, modul, tutorial, masterclass, webinar, productivitate, AI hype) verificată prin gate v20 cu awareness de context (de ex. "lecție" e ok într-o citare a tradiției pedagogice, dar nu ca termen Trainity).

## R-V02.13 · ORDINE PRODUCȚIE ≠ ORDINE CANONICĂ
**Status:** ACTIVĂ permanentă
Construcțiile pot fi produse în orice ordine (de ex. C05 înainte de C04). Dar ordinea canonică pentru cursant rămâne 01-20.

## R-V02.14 · CONSERVARE SUMĂ = SEMANTICĂ
**Status:** ACTIVĂ permanentă
Suma valoare_neta se conservă cap-coadă între construcții. Excepție: eliminări explicite (C02 elimină 10 duplicate planted, deltează cu valoarea lor). Verificare în CONTROL_FINAL.

## R-V02.15 · ZERO CIFRE BUSINESS ÎN HTML/FILM
**Status:** ACTIVĂ permanentă · BLOCANT
NICIODATĂ cifre absolute de business în HTML-Studiu, HTML-Video, FILM.docx. Toate cifrele trăiesc în Date_MASTER.xlsx, fișierele HTML/Word doar fac referință generică ("suma martor", "valoarea de control"). Box-uri decorative ok, cifre concrete nu. Verificat empiric prin gate v20.

---

# C. LIVRABILE ȘI NOMENCLATURĂ

## R-V03.1 · HTML-VIDEO = LIVRABIL CANONIC AL 3-LEA
**Status:** ABSORBITĂ în R-V03.47 (schema unificată)
HTML-Video este unul dintre cele 7 artefacte canonice (nu accesoriu).

## R-V03.2 · GENERATORUL PRODUCE 7 LIVRABILE
**Status:** ABSORBITĂ în R-V03.47 (extinsă V05 → 8 → V30 → 7+1 = 7 canonice + FILM)
La final cifra canonică e 7 (din care 1 e FILM.docx adăugat prin R-V03.58).

## R-V03.3 · HTML-VIDEO-EDITABIL = LIVRABIL CANONIC AL 4-LEA
**Status:** ABSORBITĂ în R-V03.47

## R-V03.4 · VOCE NARATIVĂ DIVERGENTĂ COCKPIT vs BROADCAST
**Status:** ACTIVĂ permanentă
HTML-Studiu vorbește cu utilizatorul direct (voce "tu" sau "noi" practic). HTML-Video are voce narativă (plural "deschidem", "marcăm", "verificăm"). Voce trainer (Bogdan) consistentă în Video.

## R-V03.5 · NOMENCLATURA UNIFICATĂ HTML
**Status:** ACTIVĂ permanentă (V06 stabil)
- `HTML-Studiu-Excel-NN-{slug}.html`
- `HTML-Editor-Studiu-Excel-NN-{slug}.html`
- `HTML-Video-Excel-NN-{slug}.html`
- `HTML-Editor-Video-Excel-NN-{slug}.html`

Slug e capitalizat (prima literă majusculă), ex: Structura, Control, Auditare, Normalizare, Clasificare.

## R-V03.33 · IMAGINI EXECUTIVE = BASE64 INLINE
**Status:** ACTIVĂ permanentă
Imaginile cinematic exec-stage-1..6 sunt encodate base64 și incluse inline în HTML-Video. HTML-Video e self-contained (~800 KB). NU referințe externe la fișiere.

**Detector empiric:** `html.count('data:image/') >= 5`

## R-V03.47 · SCHEMA CANONICĂ DATE_MASTER
**Status:** ACTIVĂ · STRUCTURA MAJORĂ
Fiecare construcție are 1 fișier `Date_MASTER-CNN.xlsx` unificat cu sheet-uri:
- `_REALITATE` (narativ scena)
- Sheet input cu fenomene (ex. `Vanzari` cu cele 7 fenomene C01)
- Sheet output curățat (ex. `Vanzari_Curat`)
- Nomenclatoare (CLIENTI, PRODUSE, AGENTI, DEPOZITE)
- `CONTROL_FINAL` (ritual cap-coadă)

Schema veche cu `Date-Input-Excel-NN.xlsx` + `Date-Output-Excel-NN.xlsx` separate = **ABANDONATĂ**.

**Detector empiric:** prezența celor 6 livrabile canonice + extensia .xlsx pentru `Date_MASTER-CNN`.

## R-V03.48 · GATE V18 FILTRE ANTI-FALS-POZITIV
**Status:** ABSORBITĂ în R-V03.50 (Gate V19 simplificat)

## R-V03.49 · DATE_MASTER-INITIAL ASSET CANONIC
**Status:** ACTIVĂ permanentă
`_system/referinte/Date_MASTER-initial.xlsx` e asset perpetuu — 2000 facturi sintetice B2B, sumă 7.986.019,38 lei. Toate Date_MASTER-CNN derivă din el (cu modificările specifice construcției).

## R-V03.50 · GATE V19 SIMPLIFICAT CLASA 6
**Status:** ABSORBITĂ în R-V03.53 (Gate v20)

## R-V03.53 · GATE V20 — INPUT/OUTPUT DISTINCT
**Status:** ACTIVĂ · BLOCANT (script: `gate_v20.py`)
Gate v20 verifică 6 clase de erori:
1. Brand (vocabular, diacritice, ZERO cifre business)
2. Identitate (slug, treaptă, axa)
3. Continuitate (sumă conservată, predare cap-coadă)
4. Structurale (cele 6+1 livrabile prezente, format corect)
5. Voce (plural în Video, divergență cu Studiu)
6. Power Query whitelist (termeni canonici Microsoft)

Gate v20 e BLOCANT — niciun present_files fără PASS.

---

# D. PRE-GENERATION CHECKS

## R-V03.37 · ARHIVA BRAIN = MINIMUM NECESAR
**Status:** ABSORBITĂ în noua structură `_system/` (V38 refactor)
Post-V38: nu mai există "arhiva brain" ca artefact separat. Tot ce e activ trăiește în `_system/` (acest folder cu cele 8 documente operaționale + arhiva istorică separată în `_system/arhiva/`).

## R-V03.38 · PROMPTURI BANANA 2 = ASSET PERPETUU
**Status:** ACTIVĂ permanentă
Prompturile Banana 2 (pentru generare imagini cinematic) sunt stocate ca asset perpetuu — folosite la generare imagini noi pentru construcții viitoare.

## R-V03.39 · POST-FLIGHT GATE CROSS-CONTAMINATION
**Status:** ACTIVĂ · BLOCANT
După generare CNN, verificare automată că NU există referințe la altă construcție (de ex. în C03 să nu apară accidental "Structura" sau "Control" în loc de "Auditare"). Empiric: grep pe slug-uri.

## R-V03.40 · BLOC IDENTITATE_TEHNICA PER CONSTRUCȚIE
**Status:** ACTIVĂ permanentă (Lecția L142)
Înainte de generare CNN, motor citește `_system/referinte/IDENTITATE-TEHNICA.md`, secțiunea construcției respective. Blochează generarea dacă lipsește.

## R-V03.41 · SIMILARITY CHECK STEP-TITLES vs PILOT
**Status:** ACTIVĂ permanentă
Step-titles din CNN NU pot fi identice cu cele din C01 pilot. Verificare empirică (max 30% similaritate per titlu).

## R-V03.42 · CHECKLIST EXPLICIT COVER-HEADER
**Status:** ACTIVĂ permanentă
Cover-header HTML-Studiu conține EXACT 3 rânduri: TREAPTA + CONSTRUCȚIE + AI INTEGRAT. Nu mai mult, nu mai puțin. Vezi R-V03.60.

## R-V03.43 · CAPITALIZARE META-VAL TREAPTĂ
**Status:** ACTIVĂ permanentă
Valoarea TREAPTA în cover-meta e SCRIS COMPLET CU MAJUSCULE: "TREAPTA 1 · STRUCTURA", nu "Treapta 1 · Structura".

## R-V03.44 · PROMPT-TEXT CLONE CHECK
**Status:** ACTIVĂ · TOLERANȚĂ ZERO (Lecția L144)
Prompturile Copilot din HTML-Studiu NU pot fi clonate textual din C01 pilot. Fiecare construcție are prompturi SPECIFICE generate per axa și FENOMENE. Verificare empirică prin diff.

## R-V03.45 · GATE V18 BLOCANT PRE-PRESENT_FILES
**Status:** ABSORBITĂ în R-V03.53 (Gate v20)

---

# E. GATE-URI ȘI AUDIT

## R-V03.51 · CHECK-IN IMPLICIT LA GENERARE DIRECTĂ
**Status:** ACTIVĂ permanentă
La comanda `genereaza CNN`, motorul nu cere SPEC adițional — folosește SPEC-ul deja înghețat în sistem. Acceptă conținut implicit din `_system/`.

## R-V03.52 · LIVRARE INCREMENTALĂ OBLIGATORIE
**Status:** ABSORBITĂ în R-V03.62 (canonic + editat la prima generare = livrare atomică)

## R-V03.55 · SPEC ÎNGHEȚAT BLOCANT
**Status:** ACTIVĂ · BLOCANT
Înainte de orice `genereaza CNN`, motor verifică:
1. SPEC CNN există în sistem
2. SPEC e marcat ÎNGHEȚAT (nu draft)
3. Cele 9 elemente narative complete (SLUG, INTRIGA, PROBLEMELE, MIZA, MANTRA, WOW, MOTTO, FENOMENE, STEP-TITLES)

Dacă FAIL → blochează generarea, anunță ARHITECT să înghețe SPEC.

## R-V03.56 · SPEC FREEZING FORMAT GRILĂ
**Status:** ACTIVĂ permanentă
Procesul de SPEC FREEZING folosește format grilă cu 3 variante creative (A/B/C) per element. ARHITECT alege A/B/C sau cere "alte 3 variante". Niciodată variantă unică propusă autoritar de motor.

---

# F. WORKFLOW ȘI FLUXURI

## R-V03.54 · COPY+MODIFY (DETALIAT)
**Status:** ACTIVĂ permanentă
Strategia operațională pentru generare C02-C20:
1. Motorul citește `c01/canonic/HTML-Studiu...html` (matriță) ca string
2. Aplică modificări strict pe text/conținut (titluri, paragrafe, prompturi, step-actions, voce trainer)
3. NU modifică CSS, JS, structura HTML, nomenclatura claselor
4. Validează diferențe lexicale: peste 50% conținut text trebuie schimbat (similarity check)
5. Output în `cNN/canonic/` + copie identică în `cNN/editat/`

**Lectia L153** clarifică: lectura selectivă din pilot Video — nu citește tot HTML-Video, ci doar secțiunile narative ce trebuie schimbate.

## R-V03.62 · PRIMA GENERARE ÎNGHEȚATĂ + PATCH OVER EDITED
**Status:** ACTIVĂ · STRUCTURA MAJORĂ V36
Vezi `04-ARHITECTURA-LIVRABILE.md` pentru detalii complete.

Rezumat:
- `cNN/canonic/` = snapshot înghețat la V01 (NU se modifică)
- `cNN/editat/` = versiunea evolutivă (modificări ARHITECT + patch-uri KIT)
- Upgrade-urile KIT se aplică DOAR pe `editat/`, NU pe `canonic/`
- Meta marker: `<meta name="trainity-snapshot" content="canonic-V01">` sau `="editat"`

**Detectori empirici:** R-V03.62-c (canonic marker), R-V03.62-e (editat marker).

---

# G. STRATIFICATE RUNTIME (V30+)

## R-V03.58 · ARHIVARE EXTINSĂ — FILM + ASSETS
**Status:** ACTIVĂ permanentă (V30, retroactiv aplicat V38)
Cele 7 artefacte includ:
- 6 livrabile cursant (R-V03.47: HTML × 4 + Date_MASTER + Creativ)
- 1 artefact arhivare: `FILM-Excel-NN-{slug}.docx`

Asset-urile cinematic (6 imagini exec-stage jpg per construcție, V39+) sunt în `cNN/assets/`, **diferite per axă** (regula R-V39.assets). Schema veche `_system/referinte/assets_canonice/` cu poze partajate — eliminată V39.

**Detector empiric:** prezența `FILM-Excel-NN-*.docx` în folderul construcției.

## R-V03.59 · HIGHLIGHTER V34
**Status:** ACTIVĂ permanentă (V31 → V34 finalizat)
HTML-Video are funcționalitate highlighter cu:
- Selecție text → marcaj galben persistent (#FFD400 pe negru)
- Click pe marcaj = toggle off (prin capture phase, NU oprește advance slide)
- Persistență localStorage per construcție
- ELIMINATE: buton Reset, ESC keybind (V34)

**Detector empiric:** prezența `onClickCapture, true` + absența `class="hl-reset"` + absența `keyCode === 27`.

## R-V03.60 · COVER-META CURAT
**Status:** ACTIVĂ permanentă (V32)
Cover-meta din HTML-Studiu și HTML-Editor-Studiu conține EXACT 3 rânduri canonice:
- TREAPTA: TREAPTA X · NUME
- CONSTRUCȚIE: NN · NUME
- AI INTEGRAT: COPILOT

Rândurile INPUT și OUTPUT (schema veche pre-R-V03.47) sunt **ELIMINATE**.

**Detector empiric:** `count(cover-meta-key">(INPUT|OUTPUT)<) == 0`.

## R-V03.61 · BUTON RESET LIPIT DE MENIU
**Status:** ACTIVĂ permanentă (V33)
Butonul "RESETEAZĂ PROGRES" din nav-controls e lipit imediat sub meniu, fără gap pe orice viewport. Implementare: `.nav-controls` NU are `margin-top: auto`.

**Detector empiric:** regex pe `.nav-controls { ... }` → absența `margin-top: auto`.

## R-V03.63 · AUDIT EMPIRIC PERMANENT
**Status:** ACTIVĂ · STRUCTURĂ MAJORĂ V38
La fiecare consolidare brain / commit major, motorul rulează `_system/generatoare/audit_sync.py` care:
- Verifică 9 reguli fișier-bazate × N zone (canonic + editat per construcție)
- Raportează tabel cu zero drift sau drift detectat
- Drift > 0 e BLOCANT — se repară înainte de a continua

Vezi `_system/generatoare/audit_sync.py` pentru lista detectoarelor.

## R-V03.69 · ANTI-CLONĂ NARATIVĂ
**Status:** ACTIVĂ V42 · introdusă după drift c05 inv-list = clonă C01

Construcțiile generate prin COPY+MODIFY pot lăsa zone narative netraduse
în axa noii construcții. Cazul descoperit empiric: `c05/HTML-Studiu` step 06
avea `inv-list` cu fenomenele C01 (ANTET DE RAPORT, SUBTOTALURI, TOTAL
GENERAL, BLANK-URI FALSE, TRANZACȚII REALE) în loc de cardinalitățile C05
CLASIFICARE (CLIENT_NUME · 15, COD_PRODUS · 13 etc.). Drift de la V28
neprins în 7 sesiuni ulterioare pentru că audit_sync verifica STRUCTURĂ,
NU IDENTITATE NARATIVĂ.

**Detector empiric R-V03.69:** verifică ca două cNN să NU aibă liste
identice literal în zone titlare distinctive:
- `inv-item-label` (raport AI)
- `anomaly-title` (cele 5-6 fenomene)
- `final-label` (verificările finale)

Dacă cNN-A și cNN-B au aceeași listă (după trim) într-una din aceste zone
→ FAIL (clonă netradusă).

**Status post-V42 fix:** c05 inv-list reparat cu cardinalitățile corecte.
Detector adăugat în audit_sync.py ca rulare permanentă.

**False positive cunoscut:** dacă două construcții au LEGITIM aceleași
fenomene (nu e cazul în T1+T2 actual), regula necesită refinare.

---

# REGULI ABANDONATE EXPLICIT

| Cod | Ce era | De ce abandonată |
|---|---|---|
| R-V03.19 | PPT livrabil canonic | V11 a decis ZERO PPT (HTML-Video înlocuiește) |
| R-V03.20-31 | Reguli intermediare V08-V14 | Absorbite în R-V03.47 (schema unificată) |
| R-V03.46 | Date-Output gate distinct | Absorbită în R-V03.53 (gate v20 unificat) |
| R-V03.52 | Livrare incrementală în chat | Absorbită în R-V03.62 (canonic+editat atomic) |
| R-V03.65 | (rezervată, neimplementată) | NU ÎN PRODUCȚIE |

---

# REGULI INTRODUSE ÎN VIITOARE VERSIUNI (semnal)

Nu sunt în producție acum, dar înregistrate pentru viitor:

- **R-V03.64+**: pattern unificat patch_runner.py care substituie scripturile individuale `inject_highlighter.py`, `fix_reset_button_position.py`, `remove_input_output_meta.py`
- **R-V03.66+**: git pre-commit hook pentru `audit_sync.py` (rulare automată la fiecare commit; blochează commit-urile cu DRIFT > 0). De explorat — momentan rulare manuală.

---

## R-V49.1 · WATERMARK GEMINI SCOS AUTOMAT (fără întrebare)

- **Status:** ACTIVĂ
- **Ce face:** Gemini / Banana 2 (Imagen) ștampilează AUTOMAT o steluță ✦ în colțul dreapta-jos pe ORICE imagine generată. Nu se poate elimina prin prompt (reapare la fiecare generare). Motorul o scoate ÎNTOTDEAUNA, fără să întrebe ARHITECT, înainte ca imaginea să ajungă în `cNN/assets/`.
- **Cum:** `python3 _system/generatoare/strip_watermark.py IN.jpg OUT.jpg` (clonare verticală a coltului din zona de deasupra — invizibil pe fundal matte-black). Reglaj opțional `--w` / `--h` pentru dimensiunea casetei.
- **Regulă durabilă:** orice asset Banana/Gemini integrat (hero, infografic, exec-stage) trece prin `strip_watermark.py` ca pas obligatoriu de finisare. Motorul NU mai cere confirmare pentru asta — e parte din procedura de integrare imagine.

---

## Cum se adaugă o regulă nouă

1. **Identifică** problema sau pattern-ul nou
2. **Alege cod**: următorul R-V03.X disponibil (R-V03.66 acum)
3. **Documentează aici** cu format: cod + nume + status + detector empiric (dacă există)
4. **Adaugă detector în `audit_sync.py`** (dacă e fișier-bazată)
5. **Aplică retroactiv** pe construcțiile existente (pattern Patch over Edited)
6. **Audit final** → confirmă zero drift
7. **Commit** cu mesaj clar: `R-V03.X: [scurt descriere]`

## Cum se abandonează o regulă

1. **Mută în secțiunea ABANDONATE** cu motiv clar
2. **Șterge detectorul** din audit_sync.py
3. **Audit final** → confirmă funcționarea fără ea
4. **Commit** cu mesaj clar: `Abandonată R-V03.X: [motiv]`

---

**Notă finală:** acest document este sursa de adevăr LIVE. Arhiva istorică completă (cu evoluția fiecărei reguli prin sesiuni) trăiește în `_system/arhiva/SISTEM_TRAINITY-versiuni.md`.
