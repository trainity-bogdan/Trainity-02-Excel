# Index căutare global · Trainity Pack 02 Excel

Toți termenii, conceptele, regulile, comenzile și scripturile sortate alfabetic, cu pointer exact unde sunt definite/folosite.

**Cum se folosește:** caută termenul aici. Citește pointer-ele. Mergi direct la locația definiției.

**Versiune:** V40 · 28 mai 2026

---

## A

**aditiv (decizii)**
- `_system/02-GLOSAR.md` "Aditiv"
- L149 în `_system/arhiva/brain-evolutia-V01-V38.md` (V30)

**AGGREGATE (funcție Excel)**
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` C01 (fenomen 7 — leac modern)
- Folosită în Power Query whitelist (R-V02.11)

**ARHITECT**
- `_system/02-GLOSAR.md` "ARHITECT"
- `CLAUDE.md` (boot rapid)

**arhiva**
- `_system/arhiva/` (folder cu istorie V01-V38)
- `_system/00-INDEX.md` (descriere arhivă)

**asset perpetuu**
- `_system/02-GLOSAR.md` "Asset perpetuu"
- `_system/04-ARHITECTURA-LIVRABILE.md` secțiune "Asset-urile partajate"
- `_system/referinte/` (locația fizică)

**audit empiric**
- `_system/01-REGULI-ACTIVE.md` §G (R-V03.63)
- `_system/02-GLOSAR.md` "Audit empiric"
- `_system/generatoare/audit_sync.py` (scriptul)
- Comandă: `verifica sincronizare` → `COMENZI.yaml` id=verifica_sincronizare

**audit_sync.py**
- `_system/generatoare/audit_sync.py` (scriptul)
- Documentație: `_system/01-REGULI-ACTIVE.md` R-V03.63
- 8 detectoare empirice activate (V40)

**axa CALITATIVĂ / CANTITATIVĂ / TEMPORALĂ**
- `_system/02-GLOSAR.md` "Axa CALITATIVĂ / CANTITATIVĂ / TEMPORALĂ"
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` Treapta 2 CUNOAȘTERE

**AutoFilter (Excel)**
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` C01 (fenomen 6 — eronat cu SUM)

---

## B

**Banana 2**
- `_system/02-GLOSAR.md` "Banana 2"
- R-V03.38 în `_system/01-REGULI-ACTIVE.md`
- Folosire: `_system/05-WORKFLOW-PER-SCENARIU.md` scenariu 3

**base64 inline**
- R-V03.33 în `_system/01-REGULI-ACTIVE.md` §C
- `_system/02-GLOSAR.md` "Base64 inline"
- `_system/04-ARHITECTURA-LIVRABILE.md` (HTML-Video self-contained)
- Detector empiric: audit_sync.py `_r0333`

**brand colors Trainity**
- `_system/07-BRAND-OPERATIONAL.md` secțiune "Brand colors"
- Yellow `#FFD400` (NU `#F2C94C`)

---

## C

**C01-C20 (construcții)**
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` (toate cele 20 mapate)
- Locații fizice: `c01/` ... `c20/`
- Status: `STARE-CURENTA.md`

**canonic (stare) — ABSORBITĂ V39**
- Era stare istorică pre-V39 (`cNN/canonic/`). ELIMINATĂ la V39 (versiune unică `cNN/`).
- Pentru istoric: `_system/04-ARHITECTURA-LIVRABILE.md` "Schema veche (pre-V39)"
- Backup pre-destructive azi: `cNN_BACKUP_AAAALLZZ_pre-{op}/` (CLAUDE.md regula V1)

**capture phase (JavaScript)**
- `_system/02-GLOSAR.md` "Capture phase"
- L153 în arhivă (V34)
- R-V03.59 în `_system/01-REGULI-ACTIVE.md` §G

**CHECK-IN construcție**
- R-V01.5 (ABSORBITĂ) → R-V03.51 în `_system/01-REGULI-ACTIVE.md`

**chat BRAIN / chat CONSTRUCȚIE**
- Sub GitHub: aceste chat-uri NU mai sunt separate — toate comenzile pot fi date în oricare chat
- Documentație istorică: `_system/arhiva/`

**CLAUDE.md**
- `CLAUDE.md` la rădăcina repo
- Boot rapid pentru motor

**comenzi**
- Listă completă: `_system/03-COMENZI-OPERATIONALE.md`
- Format machine-readable: `_system/COMENZI.yaml`
- Boot esențial: `CLAUDE.md` secțiune "Cele 10 comenzi esențiale"

**conservare sumă**
- R-V02.14 în `_system/01-REGULI-ACTIVE.md` §B
- Detector: gate_v20.py CONTROL_FINAL check
- Excepție: C02 duplicate planted (vezi `_system/06-MAP-CONSTRUCTII-T1-T5.md` C02)

**COPY+MODIFY**
- R-V02.6 în `_system/01-REGULI-ACTIVE.md` §B
- R-V03.54 (detaliată) în `_system/01-REGULI-ACTIVE.md` §F
- `_system/02-GLOSAR.md` "COPY+MODIFY"
- Folosire: `_system/05-WORKFLOW-PER-SCENARIU.md` scenariu 1

**cover-meta**
- R-V03.60 în `_system/01-REGULI-ACTIVE.md` §G
- `_system/02-GLOSAR.md` "Cover-meta"
- `_system/07-BRAND-OPERATIONAL.md` secțiune "Cover-header"
- Detector empiric: audit_sync.py `_r0360`

**Creativ.txt** — ABANDONAT (V68)
- Nu mai e artefact stocat. Prompturile imaginilor le face ARHITECT extern (cu ChatGPT); motorul nu mai stochează prompturi, doar integrează imaginile primite în `assets/` + base64.
- Vezi `_system/04-ARHITECTURA-LIVRABILE.md` (secțiunea „Creativ ABANDONAT").

**cuvinte interzise**
- R-V02.11 în `_system/01-REGULI-ACTIVE.md` §B
- Lista completă: `_system/07-BRAND-OPERATIONAL.md` secțiune "Vocabular INTERZIS"

---

## D

**Date_MASTER-CNN.xlsx**
- `_system/02-GLOSAR.md` "Date_MASTER-CNN.xlsx"
- R-V03.47 în `_system/01-REGULI-ACTIVE.md` §C (schema)
- `_system/04-ARHITECTURA-LIVRABILE.md` secțiune "Schema sheet-uri"

**Date_MASTER-initial.xlsx**
- R-V03.49 în `_system/01-REGULI-ACTIVE.md` §C
- Locație: `_system/referinte/Date_MASTER-initial.xlsx`
- 2000 facturi, sumă 7.986.019,38 lei

**diacritice românești**
- R-V02.2 în `_system/01-REGULI-ACTIVE.md` §B
- Verificare: gate_v20.py brand check

**drift**
- `_system/02-GLOSAR.md` "Drift"
- Detectat de audit_sync.py
- Reparare: vezi `_system/05-WORKFLOW-PER-SCENARIU.md`

---

## E

**editat (stare) — ABSORBITĂ V39**
- Era stare istorică pre-V39 (`cNN/editat/`). ELIMINATĂ la V39 (versiune unică `cNN/`).
- Conținut actual: tot ce era în editat live e acum în `cNN/` direct.
- Vezi `_system/04-ARHITECTURA-LIVRABILE.md` "Versiune unică per construcție (V39)"

**Editor (HTML-Editor-Studiu, HTML-Editor-Video)**
- `_system/02-GLOSAR.md` "Editor"
- `_system/04-ARHITECTURA-LIVRABILE.md` secțiune "Diferența HTML-Studiu vs HTML-Editor-Studiu"
- R-V01.3 în `_system/01-REGULI-ACTIVE.md` §A

**exec-stage (imagini cinematic)**
- 12 fișiere per construcție în `cNN/assets/` (V39: per construcție, NU partajat)
- Folosire: HTML-Video base64 inline (R-V03.33)
- Înlocuire: `_system/05-WORKFLOW-PER-SCENARIU.md` scenariu 3

**EXPORT (buton Editor)**
- `_system/02-GLOSAR.md` "Editor"
- Workflow: `_system/05-WORKFLOW-PER-SCENARIU.md` scenariu 4

---

## F

**FENOMENE (element SPEC)**
- `_system/02-GLOSAR.md` "FENOMENE"
- Lista per construcție: `_system/06-MAP-CONSTRUCTII-T1-T5.md`
- Detector: R-V03.55 (SPEC freezing)

**FILM-Excel-NN-{slug}.docx**
- `_system/02-GLOSAR.md` "FILM-Excel-NN.docx"
- `_system/04-ARHITECTURA-LIVRABILE.md` (livrabil #7)
- R-V03.58 în `_system/01-REGULI-ACTIVE.md` §G
- Structura: 8 secțiuni canonice

---

## G

**Gate v20**
- `_system/02-GLOSAR.md` "Gate v20"
- R-V03.53 în `_system/01-REGULI-ACTIVE.md` §C
- Script: `_system/generatoare/gate_v20.py`
- 6 clase de verificare (brand, identitate, continuitate, structurale, voce, PQ whitelist)

**generare construcție**
- Comandă: `genereaza CNN` → `COMENZI.yaml` id=genereaza_constructie
- Workflow detaliat: `_system/05-WORKFLOW-PER-SCENARIU.md` scenariu 1

**generatoare (folder)**
- `_system/generatoare/` (scripturi active)
- `_system/generatoare/arhiva/` (scripturi învechite)

**granularitate atomică**
- `_system/02-GLOSAR.md` "Granularitate atomică"
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` C05 (fenomen 5)

---

## H

**highlighter V34**
- `_system/02-GLOSAR.md` "Highlighter V34"
- R-V03.59 în `_system/01-REGULI-ACTIVE.md` §G
- Detector empiric: audit_sync.py `_r0359`
- Snippet-uri: `_system/referinte/highlighter-snippet.{css,js}`

**HOOK / MIZA / MANTRA / WOW / MOTTO (IDENTITATE CINEMATICĂ)**
- `_system/02-GLOSAR.md` "HOOK / MIZA / MANTRA / WOW (PAYOFF) / MOTTO"
- Componente SPEC: vezi R-V03.55
- Aplicare per construcție: `_system/06-MAP-CONSTRUCTII-T1-T5.md`

**HTML-Studiu / HTML-Video**
- `_system/04-ARHITECTURA-LIVRABILE.md` (livrabile #1 și #3)
- Diferență voce: R-V03.4 în `_system/01-REGULI-ACTIVE.md` §C

---

## I

**IDENTITATE_TEHNICA**
- `_system/02-GLOSAR.md` "IDENTITATE_TEHNICA"
- R-V03.40 în `_system/01-REGULI-ACTIVE.md` §D
- Locație: `_system/referinte/IDENTITATE-TEHNICA.md`
- L142 pre-generation check

**idempotent (script)**
- `_system/02-GLOSAR.md` "Idempotent"
- Pattern L151 în arhivă (V32)
- Aplicat în patch_runner.py

**INDEX-CAUTARE.md**
- `_system/INDEX-CAUTARE.md` (acest fișier)

**INTRIGA (sinonim HOOK)**
- `_system/02-GLOSAR.md` "INTRIGA"
- Înlocuit HOOK ca termen canonic în SPEC-uri

---

## L

**lecții L1XX**
- L01-L155 în `_system/arhiva/brain-evolutia-V01-V38.md`
- `_system/02-GLOSAR.md` "Lecție (L1XX)"

**livrabil canonic**
- `_system/02-GLOSAR.md` "Livrabil canonic"
- R-V03.47 în `_system/01-REGULI-ACTIVE.md` §C
- Lista 7 artefacte: `_system/04-ARHITECTURA-LIVRABILE.md`

---

## M

**matriță (pilot)**
- `_system/02-GLOSAR.md` "Matriță (pilot)"
- referință/cobai de generare = `c01/` (V46+: `_template/` eliminat)
- Folosire: COPY+MODIFY R-V03.54

**meta marker (`trainity-snapshot`) — ELIMINAT V39**
- Era atribut HTML pentru disting canonic/editat. Eliminat la V39 (versiune unică).
- Referință istorică: `_system/arhiva/SISTEM_TRAINITY-versiuni.md`

**Microsoft MVP**
- `_system/07-BRAND-OPERATIONAL.md` secțiune "Microsoft MVP"
- Formula canonică: "Microsoft MVP Excel pentru România, singurul"

---

## N

**non-regenerare**
- `_system/02-GLOSAR.md` "Non-regenerare"
- L154 în arhivă (V36)
- R-V03.62 codifică pattern-ul

**numire arhivă**
- R-V01.1 în `_system/01-REGULI-ACTIVE.md` §A (pre-GitHub)
- Sub GitHub: commit cu mesaj descriptiv

---

## P

**Pack 02 Excel**
- `_system/07-BRAND-OPERATIONAL.md` secțiune "Segmentare B2C vs B2B"
- Produs B2C — 20 construcții

**patch over edited**
- `_system/02-GLOSAR.md` "Patch over Edited"
- L154 în arhivă (V36)
- R-V03.62 în `_system/01-REGULI-ACTIVE.md` §G

**patch script (pattern)**
- `_system/02-GLOSAR.md` "Patch script"
- L151 în arhivă (V32)
- Acum unificat în `_system/generatoare/patch_runner.py`
- Rețete YAML: `_system/patch_recipes/`

**patch_runner.py**
- Script: `_system/generatoare/patch_runner.py`
- Rețete: `_system/patch_recipes/*.yaml`

**pilot**
- Sinonim cu matriță
- `c01/canonic/`
- `_system/02-GLOSAR.md` "Pilot"

**Power Query (PQ) whitelist**
- `_system/02-GLOSAR.md` "Power Query (PQ) whitelist"
- L146 în arhivă
- Verificare în gate_v20.py

**pre-generation check (3 HARD)**
- R-V03.40, R-V03.41, R-V03.44 în `_system/01-REGULI-ACTIVE.md` §D
- L142, L143, L144 în arhivă
- Script: `_system/generatoare/pre_generation_check.py`

**prompt Copilot (Prompt 1 / Prompt 2)**
- `_system/02-GLOSAR.md` "Prompt 1 / Prompt 2"
- R-V02.9 (count fizic) în `_system/01-REGULI-ACTIVE.md` §B
- R-V03.44 (clone check) în `_system/01-REGULI-ACTIVE.md` §D

---

## R

**R-V01.x / R-V02.x / R-V03.x (reguli)**
- Toate în `_system/01-REGULI-ACTIVE.md`
- Categorii: A (permanente), B (tehnice), C (livrabile), D (pre-check), E (gate), F (workflow), G (runtime)

**referințe **
- `_system/referinte/` (folder asset-uri perpetue)

**refacere construcție — ELIMINATĂ V40 (era refa_canonic)**
- Era pentru a regenera doar canonic. ELIMINATĂ (versiune unică V39).
- Azi: `regenereaza CNN de la zero` (cu BACKUP AUTO).
- Workflow: `_system/05-WORKFLOW-PER-SCENARIU.md` scenariu 5

**regenerare**
- Comandă: `regenereaza CNN de la zero` → `COMENZI.yaml` id=regenereaza_de_la_zero
- DISTRUCTIV — cere confirmare

---

## S

**SCARA (5 trepte)**
- `_system/02-GLOSAR.md` "SCARA"
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` (mapare completă)

**setup**
- Sinonim cu matriță, pilot
- `_system/02-GLOSAR.md` "Setup"

**SPEC**
- `_system/02-GLOSAR.md` "SPEC"
- R-V03.55 în `_system/01-REGULI-ACTIVE.md` §F
- 9 elemente: SLUG, INTRIGA, PROBLEMELE, MIZA, MANTRA, WOW, MOTTO, FENOMENE, STEP-TITLES

**SPEC FREEZING**
- R-V03.56 în `_system/01-REGULI-ACTIVE.md` §F
- Format grilă 3 variante A/B/C

**STARE-CURENTA.md**
- `STARE-CURENTA.md` la rădăcina repo
- Single source of truth pentru status

**step-title**
- `_system/02-GLOSAR.md` "Step-title"
- R-V03.41 similarity check + L144 toleranță zero clone
- 18 titluri per construcție

**suma martor**
- `_system/02-GLOSAR.md` "Suma martor"
- R-V02.14 conservare
- 7.986.019,38 lei (Date_MASTER-initial)

---

## T

**treaptă (T1-T5)**
- `_system/02-GLOSAR.md` "Treaptă"
- `_system/06-MAP-CONSTRUCTII-T1-T5.md`

---

## V

**V-cod (V01, V02, ..., V40)**
- Versiunea sistemului
- Curent: V40 (vezi `STARE-CURENTA.md`)
- Snapshot oficial per V: `_system/snapshots/V{N}_AAAALLZZ/`

**verificare fizică repo (repo = sursa de adevăr)**
- R-V03.75 în `_system/01-REGULI-ACTIVE.md`
- Niciun status de închidere (GENERAT/PASS/CLEAN/ZERO DRIFT/LIVRABIL) doar pe raport
- Cele 7 artefacte trebuie verificate fizic pe `origin/main` (git ls-tree / cat-file)
- Artefact lipsă → `LIVRABIL INVALIDAT · ARTEFACT LIPSĂ`

**voce trainer (plural)**
- `_system/02-GLOSAR.md` "Voce trainer (plural)"
- R-V03.4 în `_system/01-REGULI-ACTIVE.md` §C
- Aplicabil: HTML-Video și FILM.docx

---

## Z

**zero drift**
- `_system/02-GLOSAR.md` "Zero drift"
- R-V03.63 (audit empiric permanent)
- Confirmat de audit_sync.py

**ZWSP / SHY**
- `_system/02-GLOSAR.md` "ZWSP / SHY"
- C03 AUDITAREA (fenomen 2)

---

# SCRIPTURI — index

**audit_sync.py** → `_system/generatoare/audit_sync.py`
- Audit empiric exhaustiv. 8 detectoare (V40).

**gate_v20.py** → `_system/generatoare/gate_v20.py`
- Gate v20 verificare cap-coadă (6 clase).

**init_canonic_editat.py** → `_system/generatoare/init_canonic_editat.py`
- LEGACY V36 (migrare folder plat → canonic+editat). NU mai e folosit din V39 (colaps la versiune unică). Poate fi mutat în arhiva/.

**patch_runner.py** → `_system/generatoare/patch_runner.py`
- Motor unificat patch-uri din rețete YAML.

**pre_generation_check.py** → `_system/generatoare/pre_generation_check.py`
- Cele 3 checks HARD înainte de generare.

**gen_date_master_initial.py** → `_system/generatoare/gen_date_master_initial.py`
- Generator Date_MASTER-initial.xlsx (asset perpetuu).

**gen_imagini_base64.py** → `_system/generatoare/gen_imagini_base64.py`
- Utility encoding base64 pentru imagini cinematic.

---

# REȚETE PATCH — index

Folder: `_system/patch_recipes/`

Fiecare rețetă YAML conține: regula, target_files, operații, detector, mesaj_commit.

Lista activă:
- `R-V03.59-highlighter-v34.yaml` — highlighter cleanup (no-button, no-ESC)
- `R-V03.60-cover-meta-cleanup.yaml` — cover-meta fără INPUT/OUTPUT
- `R-V03.61-buton-lipit-responsive.yaml` — nav-controls fără margin-top:auto

Folosință: `python _system/generatoare/patch_runner.py {nume-rețetă} [--dry-run]` (flag `--target-canonic` eliminat V39, versiune unică)

---

# COMENZI — index

Lista completă în `_system/COMENZI.yaml`.

Top 10 (din `CLAUDE.md`, V40):
1. `status`
2. `genereaza CNN`
3. `regenereaza CNN de la zero` (cu BACKUP AUTO)
4. `verifica sincronizare`
5. `aplica fix [desc]` (cu BACKUP AUTO dacă >3 fișiere)
6. `compara C{NN} cu versiunea anterioara`
7. `regula noua R-V03.X: [desc]`
8. `snapshot V{N}` (regula V2)
9. `consolideaza brain` (cu SNAPSHOT AUTO V{N})
10. `help`

---

**Pentru orice nu găsești aici, întreabă-mă direct.** Eu actualizez acest index la fiecare adăugare de concept nou în sistem.
