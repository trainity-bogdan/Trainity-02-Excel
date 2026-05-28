# Glosar Trainity · Termeni cheie

Definiții scurte, ordonate alfabetic. Toți termenii folosiți în sistem.

---

## A

**Aditiv (vs înlocuire)**
Pattern arhitectural: când introduci o regulă nouă, o adaugi peste cele existente fără să șterge funcționalități. Confirmat L149 (V30).

**ARHITECT**
Rol operațional al lui Bogdan în relație cu motorul (Claude). ARHITECT decide ce, motorul execută cum. ARHITECT face confirmări concise ("da", "confirm tot"), motorul propune și execută.

**Asset perpetuu**
Resursă reutilizabilă care nu se schimbă între construcții (Date_MASTER-initial.xlsx, snippets, schema docs). Centralizate în `_system/referinte/`. NOTĂ: `assets_canonice/` partajat a fost eliminat V39 — imaginile exec-stage trăiesc acum per construcție în `cNN/assets/`.

**Audit empiric**
Verificare automată prin script (audit_sync.py) că toate regulile fișier-bazate sunt aplicate uniform peste construcții. Zero drift = sincronizat.

**Axa CALITATIVĂ / CANTITATIVĂ / TEMPORALĂ**
Cele 3 axe de analiză descriptivă T2 CUNOAȘTERE.
- **CALITATIVĂ** (C05): etichete, dicționar, granularitate, tipologie.
- **CANTITATIVĂ** (C06): cifre, sume, distribuții, top-N, Pareto.
- **TEMPORALĂ** (C07-C08): evoluții lună-de-lună, memoria setului.

---

## B

**Banana 2**
Tool de generare imagini cinematice (asset Trainity perpetuu). Produce imagini 3:2 format jpg + png pentru exec-stage-1..6 (cele 6 stadii cinematice din HTML-Video).

**Base64 inline (R-V03.33)**
Imaginile cinematic sunt încorporate în HTML-Video ca data URI, nu ca fișiere separate. HTML-Video e self-contained ~800KB.

---

## C

**Canonic — ABSORBIT V39**
Era stare istorică pre-V39 (`cNN/canonic/`). ELIMINATĂ la V39 (versiune unică `cNN/`). Rolurile fostei stări canonic sunt acum împărțite:
- Matriță pentru generare construcții viitoare = `_template/` (separat explicit)
- Backup automat = `cNN_BACKUP_AAAALLZZ_pre-{op}/` la operațiuni distructive (regula V1 din CLAUDE.md)
- Snapshots oficiale V{N} = `_system/snapshots/V{N}_AAAALLZZ/` (regula V2)
- Referință pentru audit/diff = OneDrive Version History per fișier (regula V3)

**Capture phase**
Tehnică JavaScript: `addEventListener('click', fn, true)`. Permite intercepție event înainte de bubble la parent. Folosit în highlighter V34 pentru a opri advance-ul slide-ului la click pe text marcat (L153).

**Construcție**
Una dintre cele 20 unități pedagogice din pack (C01-C20). Fiecare are 7 artefacte canonice și e parte dintr-o treaptă SCARA.

**COPY+MODIFY (R-V03.54)**
Strategie de generare: pentru C02-C20, motorul copiază structura din C01 pilot și modifică doar conținutul specific construcției respective. Asigură consistență vizuală și tehnică.

**Cover-meta**
Bloc din HTML-Studiu cu metadate (TREAPTĂ + CONSTRUCȚIE + AI INTEGRAT). Reducerea la 3 rânduri canonice (R-V03.60) după eliminarea rândurilor INPUT/OUTPUT obsolete.

---

## D

**Date_MASTER-CNN.xlsx**
Fișier Excel unificat per construcție. Conține sheet-uri de input (cu fenomene) + sheet-uri de output (curățate) + dicționar/control. Înlocuiește schema veche Date-Input + Date-Output (R-V03.47).

**Date_MASTER-initial.xlsx**
Asset perpetuu în `_system/referinte/`. 2000 facturi sintetice B2B multi-categorie, sumă conservată 7.986.019,38 lei. Folosit ca sursă pentru toate Date_MASTER-CNN.

**Drift**
Diferență detectată empiric între ce ar trebui să fie (reguli active) și ce e (livrabil real). Detectat de audit_sync.py.

---

## E

**Editat — ABSORBIT V39**
Era stare istorică pre-V39 (`cNN/editat/`). ELIMINATĂ la V39 (versiune unică `cNN/`). Tot conținutul fostei stări "editat" trăiește acum direct în `cNN/`. Modificările ARHITECT și patch-urile sistemice se aplică acolo.

**Editor (HTML-Editor-Studiu, HTML-Editor-Video)**
Variantă de editare a fișierelor canonice. Are toolbar cu butoane "EXPORT", "RESET". Permite editare inline a textului prin `contenteditable`. EXPORT produce HTML curat (fără toolbar) pentru livrare.

---

## F

**FENOMENE**
Element din SPEC (#7 din 9 elemente narative). Lista exhaustivă de probleme/categorii detectate în datele unei construcții. Ex: C03 are 5 FENOMENE de contaminări (whitespace, ZWSP, numere ca text, etc.).

**FILM-Excel-NN.docx**
Document Word cu scriptul video procedural cinematic (~150 paragrafe). Conține IDENTITATE CINEMATICĂ + ROLURI + SCENA + 6 ETAPE + FINAL. Folosit pentru OBS Studio recording cu voce trainer Bogdan.

---

## G

**Gate v20**
Script de verificare cap-coadă strictă (gate_v20.py). Verifică 6 clase de erori pe toate livrabilele unei construcții: brand, identitate, continuitate, structurale, voce, Power Query whitelist. PASS = construcție gata de present_files.

**Granularitate atomică**
Unitatea atomică a setului — un rând = ce înseamnă concret. Pentru Pack 02 Excel = 1 rând = 1 linie de factură. Determinată în C05.

---

## H

**Highlighter V34 (R-V03.59)**
Funcționalitate HTML-Video: selecție text → marcaj galben persistent (#FFD400 pe negru). Click pe marcaj = toggle off (revine textul, slide-ul NU avansează). Persistență localStorage. Fără buton Reset, fără ESC.

**HOOK / MIZA / MANTRA / WOW (PAYOFF) / MOTTO**
Cele 5 piese din IDENTITATE CINEMATICĂ. Definite per construcție în SPEC.
- **HOOK** = intriga, prima frază care prinde
- **MIZA** = ce se pierde dacă nu rezolvi
- **MANTRA** = principiu Trainity ("Înainte de orice calcul, structura")
- **WOW (PAYOFF)** = rezultatul demonstrabil
- **MOTTO** = semnătura operator după construcție

---

## I

**IDENTITATE_TEHNICA**
Bloc per construcție în `_system/referinte/IDENTITATE-TEHNICA.md`. Conține: slug, treaptă, axa, FENOMENE, schema sheet-uri. Cerută de L142 pre-generation.

**Idempotent (script)**
Proprietate: re-rularea aceluiași script pe același input nu produce schimbări dacă a fost deja aplicat. Esențială pentru patch-uri.

**INTRIGA (sinonim HOOK)**
Prima frază a construcției. Sub R-V03.X, INTRIGA a înlocuit HOOK în SPEC-uri ca termen canonic român (vezi brain pentru evoluție).

---

## L

**Lecție (L1XX)**
Învățătură codificată numeric (L129-L155). Distilare a unei decizii arhitecturale sau a unei probleme rezolvate. Stocate în arhivă, marcate când influențează o regulă R-V03.

**Livrabil canonic**
Una dintre cele 6 piese livrate per construcție conform R-V03.47:
1. HTML-Studiu
2. HTML-Editor-Studiu
3. HTML-Video
4. HTML-Editor-Video
5. Date_MASTER-CNN.xlsx
6. Creativ-Excel-NN-{slug}.txt

Plus 1 artefact arhivare (R-V03.58): FILM-Excel-NN.docx. Total = 7 artefacte.

---

## M

**Matriță (pilot)**
`_template/` la rădăcina proiectului (V39+). Clonă structurală a primei construcții pilot (C01 V12), servește ca șablon COPY+MODIFY pentru toate celelalte construcții. NU se modifică spontan; modificările matriței sunt comandă explicită.

**Meta marker (`<meta name="trainity-snapshot">`) — ELIMINAT V39**
Era atribut HTML pentru a distinge canonic/editat. Eliminat la V39 (versiune unică, marker fără sens). Detectoarele R-V03.62-c/e din audit_sync.py au fost eliminate corespunzător.

---

## N

**Non-regenerare (L154)**
Principiu: după prima generare a unei construcții, NU se regenerează automat conținutul. Modificările vin ca patch-uri țintite peste fișierele existente în `cNN/`. Prima rulare e singura "fresh", restul sunt evoluție. Pentru regenerare deliberată: comanda `regenereaza CNN de la zero` cu BACKUP AUTO (regula V1).

---

## P

**Patch over Edited (L154) — REINTERPRETAT V39**
Pre-V39: upgrade-urile KIT se aplicau doar pe `editat/`, NU pe `canonic/`. Post-V39 (versiune unică): patch-urile se aplică direct în `cNN/`, cu BACKUP AUTO (regula V1) când ating >3 fișiere. Conținutul ARHITECT rămâne intact prin țintirea precisă a patch-ului.

**Patch script (pattern L151)**
Pre-V38: scripturi izolate per regulă (`inject_highlighter.py`, `fix_reset_button_position.py`, `remove_input_output_meta.py` — acum în `_system/generatoare/arhiva/`). Post-V38: motor unificat `_system/generatoare/patch_runner.py` + rețete YAML în `_system/patch_recipes/R-V03.X-{slug}.yaml`. Structura comună: regex strict + idempotent + anti-duble-inject.

**Pilot**
Sinonim cu Matriță. `_template/` (V39+). Inițial inspirat din C01 V12.

**Power Query (PQ) whitelist (L146)**
Lista de termeni canonici Microsoft acceptați în gate_v20 brand check (Promoted Headers, Filtered Rows, Applied Steps, Normalized Diacritics, etc.). Necesari în C04 NORMALIZAREA pentru prompturi Copilot.

**Prompt 1 / Prompt 2**
Cele 2 prompturi Copilot per construcție. Vizibile în HTML-Studiu cu prompt-label specific construcției (NU clonate din C01 pilot — L144).

---

## R

**R-V03.XX (regulă)**
Cod de regulă activă în sistem. R-V01.x = reguli permanente nucleu, R-V02.x = reguli tehnice, R-V03.x = reguli stratificate per versiune. Vezi `01-REGULI-ACTIVE.md`.

---

## S

**SCARA (5 trepte)**
Structura pedagogică macro a pack-ului:
- **T1 SCAN** (C01-C04): Structura, Control, Audit, Normalizare
- **T2 CUNOAȘTERE** (C05-C08): Clasificare, KPI, Memorie, Tipare
- **T3 ANALIZA** (C09-C12)
- **T4 RAPORTARE** (C13-C16)
- **T5 AUTOMATIZARE** (C17-C20)

**Setup**
Sinonim: matriță, pilot. `_template/` (V39+).

**SPEC**
Specificația narativă inghețată per construcție. Conține 9 elemente: SLUG, INTRIGA (HOOK), PROBLEMELE, MIZA, MANTRA, WOW (PAYOFF), MOTTO, FENOMENE, STEP-TITLES. Format grilă cu 3 variante per element (R-V03.56).

**SPEC FREEZING**
Procesul de înghețare a SPEC-ului în chat BRAIN cu format grilă. ARHITECT alege A/B/C pentru fiecare element sau cere "alte 3" variante. Blocant pre-generation (R-V03.55).

**Step-title**
Titlu pas în HTML-Studiu (max 18 per construcție). Format: verb la imperativ + obiect. Trebuie să fie SPECIFIC construcției, NU clonat din pilot (L144).

**Suma martor**
Suma de control a coloanei valoare_neta din Date_MASTER, conservată cap-coadă între construcții (R-V02.14). Pentru Date_MASTER-initial = 7.986.019,38 lei.

---

## T

**Treaptă (T1-T5)**
Una dintre cele 5 trepte SCARA. Fiecare treaptă are 4 construcții. Treapta dă coerența pedagogică (T1 = "facem datele controlabile", T2 = "cunoaștem setul", etc.).

---

## V

**V-cod (V01, V02, ..., V40)**
Versiunea curentă a sistemului. Se incrementează la fiecare `consolideaza brain`. V40 e versiunea actuală. Snapshot oficial per V: `_system/snapshots/V{N}_AAAALLZZ/` (regula V2 din CLAUDE.md).

**Versiunea LIVE**
Pre-V39: era sinonim cu starea "editat". Post-V39: este `cNN/` direct (versiune unică). E ce primesc cursanții finalmente.

**Voce trainer (plural)**
În HTML-Video, toate verbele sunt la persoana 1 plural ("deschidem", "marcăm", "verificăm"). NU singular. Confirmat empiric pe C01-C05 (18/18 titluri în voce plural).

---

## Z

**Zero drift**
Stare ideală sistem: toate regulile fișier-bazate active aplicate uniform pe toate construcțiile. Verificat de audit_sync.py.

**ZWSP / SHY**
Caractere Unicode invizibile (Zero Width Space, Soft Hyphen). Fenomene de contaminare în C03 AUDITAREA — întâlnite în date reale din ERP.
