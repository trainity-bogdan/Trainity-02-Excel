# Stare curentă Trainity · Pack 02 Excel

**Versiune sistem:** V42 (în lucru, fără tag git încă — se va consolida la finalul rundei C06+)
**Ultima actualizare:** 29 mai 2026
**Ultima sesiune V42 — sumar:**

Refactor masiv naming + UX editor + audit narativ + deploy live Pages:

1. **Naming -ARE peste tot** (T1+T2): denumiri scurte unifilament în filenames + titluri lungi „Cum construim X" în Hero. Schimbări vizibile:
   - C01 STRUCTURA → STRUCTURARE
   - C02 CONTROL → MARCARE (era CONTROL, descris corect ce face: marchează anomalii fără șterge)
   - C03 AUDIT → AUDITARE
   - C04 NORMALIZARE (rămâne)
   - C05 CLASIFICARE (rămâne)
   - Treaptele: SCAN → SCANARE; CARE → CUNOAȘTERE; ANALIZA → ANALIZARE
   - T2 plan: C06 CUANTIFICARE / C07 DATARE / C08 TIPIZARE (înlocuiește KPI/MEMORIA SETULUI/TIPARE TEMPORALE)
2. **Cover-meta restructurat în 4 rânduri**: DENUMIRE TREAPTĂ / CONSTRUCȚIILE TREPTEI (cu bold pe curentă) / CONSTRUCȚIE CURENTĂ / AI INTEGRAT. Aplicat în matriță Studiu+Editor-Studiu + propagat la c01-c05.
3. **Editor live editabil EXTINS** (V42 EDITABLE_SELECTORS): acum și mantra-band-main, cover-label, cover-subtitle, cover-meta-key/val, exec-hero-label/sharp, section-marker/sublabel, stage-label/quote, next-label/title/desc, payoff-line/motto, completion-title/subtitle. Aplicat matriță + c01-c05 Editor-Studiu.
4. **Video navigation tableta**: click stânga = prevFrag, click dreapta = nextFrag (split L/R). Combinat cu: click pe text = edit (browser default), click între texte = nav. Eliminat IIFE blockStageInteractions (era piedică pentru background clicks).
5. **Editor-Video tastatură fix critic** (V42 R-V03.70): Enter în mod edit crea newline (nu nextFrag), ArrowKeys mută cursor în text (nu schimbă slide). Folosit `stopImmediatePropagation` în CAPTURE phase pe document.keydown (stopPropagation simplu nu era suficient — nu oprește alte listeneri pe ACELAȘI nod). Plus walk manual prin parentNode pentru Text nodes fără closest. Aplicat matriță + propagat c01-c05.
6. **Reset video = hard refresh + cleanup**: `editorReset()` acum șterge cheile localStorage `trainity_*`, sessionStorage similar, apoi `location.replace(pathname + '?_=' + timestamp + hash)` cu cache-bust + entry curat în history. Plus recuperare c04 (lipseau editorExport + editorReset complet — drift preexistent).
7. **GitHub Pages activ**: repo trecut la public, workflow `.github/workflows/pages.yml` deploy automat la fiecare push pe main. URL live: `https://trainity-bogdan.github.io/Trainity-02-Excel/`. Dashboard index.html cu link-uri direct, toate cu `?v=2` cache-bust. Privacy: robots.txt + noindex meta pe toate paginile (nu sunt indexate Google).
8. **Audit narativ R-V03.69 ANTI-CLONĂ NARATIVĂ**: detector nou care prinde cazul când două cNN au liste titlare identice literal (inv-item-label, anomaly-title, final-label). Descoperit empiric drift c05 inv-list = clonă C01 (din generarea V28, neprins în 7 sesiuni). Fixat + detector permanent în audit_sync.py. Total audit: 9 detectori × 5 cNN = 45 verificări PASS.
9. **Assets PNG eliminate** (~40 MB economisit): doar JPG rămâne (lossless PNG inutil pentru fotografii foto-realistice Banana 2). Detector V39.assets actualizat la 6 jpg per folder.
10. **Banana 2 exec-stage C02**: aplicate primele 2 imagini dedicate (REALITATE, INVESTIGAȚIE) + fix prompt „future date" → „4 OCT 2036" (independent de când vede cursantul cursul).

**Regulile noi în CLAUDE.md** (V42):
- ⚠️ **REGULĂ ABSOLUTĂ:** LUCREZI MEREU PE `main`. NU CREEZI BRANCH-URI NOI. Excepție: ARHITECT cere EXPLICIT.
- **Întrebări în text liber**, NU în grile A/B/C cu AskUserQuestion.

**Reguli noi în 01-REGULI-ACTIVE.md**:
- **R-V03.69 ANTI-CLONĂ NARATIVĂ**: detector permanent în audit_sync
- **R-V03.70 STOP IMMEDIATE KEYDOWN ÎN EDIT**: pattern blockKeyboardInEditor (capture + stopImmediatePropagation)

---

**Ultima actualizare V41:** Fix responsive complet pe matrița HTML-Studiu (safe-area iPhone, breakpoint-uri 380px/landscape, a11y aria-expanded/keyboard) + **refactor invers OneDrive → git** (V40 a fost OneDrive, V41 revine la git ca singura sursă de versionare; reguli G1-G5 noi în CLAUDE.md)

---

## Construcții — status complet

| Cod | Nume | Versiune | Stare | Audit |
|-----|------|----------|-------|-------|
| **C01** | STRUCTURARE (cum construim o structură tabelară corectă) | V12 → V42 nume | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C02** | MARCARE (cum construim controlul anomaliilor de date) | V26 → V42 nume + 2/6 exec-stage Banana dedicate | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C03** | AUDITARE (cum construim un audit valoric) | V26 → V42 nume | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C04** | NORMALIZARE (cum construim o formă normalizată) | V27 → V42 (drift editor fix) | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C05** | CLASIFICARE (cum construim un dicționar al setului) | V28 → V42 (inv-list fix din clonă C01) | versiune unica + assets/ | ✓ ZERO DRIFT |
| C06 | CUANTIFICARE (T2 CUNOAȘTERE, axă cantitativă) | — | SPEC pending | — |
| C07 | DATARE (T2 CUNOAȘTERE, axă temporală-range) | — | NESTAR | — |
| C08 | TIPIZARE (T2 CUNOAȘTERE, axă temporală-pattern) | — | NESTAR | — |
| C09-C12 | (T3 ANALIZARE: CORELARE / COMPARARE / SEGMENTARE / PROIECTARE — draft) | — | NESTAR | — |
| C13-C16 | (T4 RAPORTARE: VIZUALIZARE / SINTETIZARE / NARARE / PUBLICARE — draft) | — | NESTAR | — |
| C17-C20 | (T5 AUTOMATIZARE: DECLANȘARE / PROGRAMARE / INTEGRARE / STANDARDIZARE — draft) | — | NESTAR | — |

**Progres: 5/20 (25%) livrate. T1 SCANARE complet + C05 (T2 CUNOAȘTERE, primul pas calitativ) livrat.**

---

## Audit empiric (rulează `_system/generatoare/audit_sync.py`)

```
✓ 8 detectoare empirice × 5 construcții = 40 verificări PASS
✓ ZERO DRIFT (versiune unică per cNN — git ține istoricul complet via log/tags/branches)
✓ Toate cele 7 artefacte + assets/ prezente per construcție
```

Detectori activi (V40):
- R-V03.60 cover-meta fără INPUT/OUTPUT
- R-V03.61 buton lipit responsive (`.nav-controls` fără `margin-top:auto`)
- R-V03.59 highlighter V34 (capture phase, fără buton, fără ESC)
- V32-fix zero referințe Date-Output/Input
- R-V03.33 imagini base64 inline în Video
- R-V03.47 cele 6 livrabile canonice
- R-V03.58 FILM.docx prezent
- R-V39.assets folder `assets/` cu 6 imagini exec-stage jpg (V41 update: eliminat PNG duplicate wasteful)

---

## Pe agenda imediată

1. **SPEC C06 freezing** — axa CANTITATIVĂ (cifre, sume, distribuții, Pareto)
2. **Generare C06** sub schema V40 (versiune unică, _template ca matriță)
3. **SPEC C07** cinematic — axa TEMPORALĂ ("setul are memorie")
4. **Generare C07** după SPEC freezing
5. **SPEC C08** — axa TEMPORALĂ-COMBINATĂ ("setul are tipare")
6. **Setup B2C landing pages live** (paralel)

---

## Sesiunea V41 (28 mai 2026) — Responsive matriță + refactor git

**Lucrări:**
1. **Fix responsive complet pe `_template/HTML-Studiu`** (matriță, NU propagat la C01-C05):
   - Critical: safe-area iPhone (notch + home indicator) pe mobile-topbar/side-nav/continue-btn/scroll-top, padding-uri intermediare 641-1024px (exec-hero, payoff-section), cover-meta-row tabletă (150px gutter), inv-item-status mobile pill, prompt-box mobile padding + `word-break: break-word`, stage-number `clamp(56-96px)` unificat
   - Medium: breakpoint `≤380px` (iPhone SE / Android budget) + continue-btn condensat sub 380px + landscape phone drawer
   - A11y: `aria-expanded` dinamic pe mobile-toggle + `aria-hidden` pe overlay + Escape închide drawer + focus management + `role=button` / `tabindex=0` / `aria-label` pe `.step-check` + keyboard support (Space/Enter)
   - Commit: `2a31f46` pe branch `claude/status-7j30w`, push reușit pe origin
2. **Refactor invers OneDrive → git** (V40 a fost greșit înțeles — ARHITECT folosește git, nu OneDrive):
   - CLAUDE.md: secțiunea „VERSIONARE ONEDRIVE + BACKUP DISCIPLINE" rescrisă ca „VERSIONARE GIT" cu regulile G1-G5
   - STARE-CURENTA, README, COMENZI.yaml, 00-INDEX, 01-REGULI, 02-GLOSAR, 03-COMENZI-OPERATIONALE, 04-ARHITECTURA-LIVRABILE, 05-WORKFLOW-PER-SCENARIU: rescrise referințele OneDrive
   - Reguli noi git (G1 branch-per-task, G2 commit descriptiv, G3 tag V{N} la increment, G4 restore git, G5 PR pentru schimbări sistemice) — au înlocuit V1/V2/V3 OneDrive

**L159 (nou):** Sistemul a oscilat două sesiuni la rând între GitHub și OneDrive (V40 a refactorizat spre OneDrive bazat pe presupunere; V41 revine la git pe confirmare directă din partea ARHITECT). **Regulă durabilă:** orice schimbare a workflow-ului de versionare se face DOAR pe confirmare scrisă explicită din partea ARHITECT, nu pe deducție din artefacte existente.

---

## Sesiunea de audit V40 (28 mai 2026)

Audit exhaustiv din partea ARHITECT. Findings prioritizate (14 total, 4 critical), fix-uri aplicate în Sesiunea 2.

**CRITICAL fixate:**
- **#1 audit_sync.py encoding bug** — `open(f)` fără `encoding='utf-8'` arunca `UnicodeDecodeError` pe HTML cu base64, captat silent de `except Exception` generic. 5/8 detectoare silent-fail-uiau pe Windows. Raport spunea "ZERO DRIFT" fals. **FIX:** adăugat `encoding='utf-8'`, raportare ERR explicită pe stderr, tracking distinct OK/XX/ERR în output.
- **#2 STARE-CURENTA cifre false** — "9 detectoare × 10 zone = 80 verificări PASS" era inventat. **FIX:** corectat la "8 × 5 = 40 verificări PASS" (real măsurat).
- **#3 pre_generation_check.py** — căuta `SISTEM_TRAINITY.md` eliminat la refactor V38. **FIX:** adăugate candidate paths pentru `_system/arhiva/SISTEM_TRAINITY-versiuni.md`.
- **#4 gate_v20.py print crash** — `'✓' (✓)` nu putea fi printat în cp1252 Windows console. **FIX:** `sys.stdout.reconfigure(encoding='utf-8')` la pornire.

**HIGH fixate:**
- **#5 04-ARHITECTURA-LIVRABILE.md** rewrite complet pentru V39 versiune unică (eliminat canonic/editat).
- **#6 COMENZI.yaml** rewrite — eliminate comenzile fără sens (refa_canonic, aplica_si_pe_canonic), simplificate restul.
- **#7 assets_canonice/** — eliminate referințele din 04-ARHITECTURA, 07-BRAND-OPERATIONAL, COMENZI.yaml (per construcție în V39, nu partajat).
- **#8 IDENTITATE-TEHNICA.md schema** — C01-C04 actualizate la `Date_MASTER-initial.xlsx` + `Date_MASTER-CNN.xlsx` (schema R-V03.47), aliniate cu C05.

**MEDIUM/LOW fixate:**
- **#9 c04/RAPORT-CONSTRUCTIE-C04.md** mutat în `_system/arhiva/RAPORT-CONSTRUCTIE-C04-V27.md`.
- **#11 README.md** data sincronizată.
- **#12 STARE-CURENTA detectori** — eliminat R-V03.62-c/e marker (nu se mai folosesc).
- **#13 .gitignore** — eliminat `*-Editat.html.bak` (convenție nume veche).

**Finding adițional V40 (REVOCAT în V41):**
- **#15 V40 a presupus că ARHITECT folosește OneDrive.** Presupunerea greșită — ARHITECT lucrează doar cu git. V41 a rescris înapoi toate docurile spre workflow git (vezi sesiunea V41 mai sus).

**Confirmate empiric PASS:**
- Zero em-dash (—), zero en-dash (–), zero vocab interzis în HTML-uri C01-C05
- 40/40 verificări audit_sync REAL PASS (post-fix)
- Gate v20 PASS pe C02 (testat post-fix)

---

## Reguli noi de la ultima sesiune (V38)

- **R-V03.62** PRIMA GENERARE ÎNGHEȚATĂ + PATCH OVER EDITED (V36 consolidat V37) — **ABSORBITĂ V39:** versiune unică, fără meta marker
- **R-V03.63** AUDIT EMPIRIC PERMANENT (V38)

Reguli existente, statusuri actuale: vezi `_system/01-REGULI-ACTIVE.md`.

---

## Lecții noi V36-V40

- **L154** Persistarea editorilor prin non-regenerare (V36)
- **L155** Punctarea permanentă a sincronizării prin audit empiric (V38)
- **L156** Audit infrastructure poate ascunde drift real prin exception silent capture — orice `except Exception:` fără raportare pe stderr e suspect. Toate scripturile de validare TREBUIE să raporteze ERR explicit, nu doar PASS/FAIL.
- **L157** Documentația sistemului poate diverge silent de realitatea pe disk la refactor (V38→V39 a lăsat 4 docs stale). La fiecare refactor structural, audit sync docs-vs-disk e obligatoriu.
- **L158** [REVOCAT în V41] V40 a presupus OneDrive bazat pe artefacte istorice (foldere `OUT-V{N}.zip`, lipsa `.gitignore` clar). Confirmare directă V41: ARHITECT folosește exclusiv git.
- **L159** Workflow-ul de versionare nu se schimbă pe deducție din artefacte. Doar pe confirmare scrisă explicită din partea ARHITECT. Două sesiuni consecutive au oscilat între GitHub și OneDrive pentru că am inferat în loc să întreb. **Regulă durabilă:** la orice schimbare de model (versionare, structură repo, convenție livrabile), motor întreabă ARHITECT direct înainte de a refactoriza docs.
- **L160** (V42) Drift narativ poate trăi luni în repo fără detectare dacă audit verifică doar structură + prezență CSS. Cazul empiric: c05 inv-list era clonă C01 literal de la V28 (7 sesiuni nedetectat). audit_sync.py verifica „6 jpg present", „CSS class X există", dar nu „lista titlară A == lista titlară B → DRIFT". **Regulă durabilă:** detectorii noi trebuie să acopere și COERENȚĂ SEMANTICĂ (nu doar prezență tehnică). Detector R-V03.69 ANTI-CLONĂ NARATIVĂ adăugat ca prevenție viitoare.
- **L161** (V42) `e.stopPropagation()` NU oprește alte event listenere de pe ACELAȘI nod. Doar oprește propagarea spre alte noduri (DOM tree). Pentru a opri și listener-ele bubble pe același nod (document) când e capture, folosesc `e.stopImmediatePropagation()`. Cauza descoperită empiric: blockKeyboardInEditor cu stopPropagation simplu nu opera Enter→nextFrag pentru că bubble handler-ul global pe document rula oricum. **Regulă durabilă:** când vrei blocare totală a unui event în fază capture pe nod cu multipli listenere (document), foloseşte stopImmediatePropagation, nu stopPropagation.

Toate lecțiile cumulate (L01-L161) în `_system/arhiva/brain-evolutia-V01-V38.md` (până V41) + STARE-CURENTA (V42+).

---

## Modificări sistem aplicate V38

**Refactor documentație** (de la 580 KB împrăștiată la 84 KB în 8 fișiere):
- `_system/00-INDEX.md` (punctul de intrare)
- `_system/01-REGULI-ACTIVE.md` (reguli distilate)
- `_system/02-GLOSAR.md` (termenii cheie)
- `_system/03-COMENZI-OPERATIONALE.md` (FAQ)
- `_system/04-ARHITECTURA-LIVRABILE.md` (schema 7 artefacte)
- `_system/05-WORKFLOW-PER-SCENARIU.md` (5 scenarii)
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` (cele 20 mapate)
- `_system/07-BRAND-OPERATIONAL.md` (brand, voce, colors)

**Setup definitiv (V38 extins):**
- `CLAUDE.md` la rădăcină (boot rapid)
- `STARE-CURENTA.md` la rădăcină (acest fișier)
- `_system/COMENZI.yaml` (catalog machine-readable)
- `_system/INDEX-CAUTARE.md` (search index)
- `_system/generatoare/patch_runner.py` (motor patch unificat)
- `_system/patch_recipes/` (rețete YAML)

**Migrare retroactivă R-V03.58:** generat FILM.docx + copiere assets/ pentru C02-C05 (drift detectat și reparat).

**Restructurare repo:** eliminat `_pilot/`, mutat în `c01/canonic/+editat/` ca celelalte construcții.

---

## Asset-uri perpetue verificate (V40)

| Asset | Locație | Stare |
|---|---|---|
| Date_MASTER-initial.xlsx | `_system/referinte/` | ✓ (2000 facturi, sumă 7.986.019,38) |
| IDENTITATE-TEHNICA.md | `_system/referinte/` | ✓ schema R-V03.47 |
| DATA-INSTRUCTIUNI.md | `_system/referinte/` | ✓ |
| SCHEMA-MASTER.md | `_system/referinte/` | ✓ |
| COVER-CHECKLIST.md | `_system/referinte/` | ✓ |
| PROTOCOL-FILM-OBS.md | `_system/referinte/` | ✓ |
| highlighter-snippet.{css,js} | `_system/referinte/` | ✓ |
| 6 imagini exec-stage per cNN | `cNN/assets/` | ✓ jpg 3:2 cinematic (diferite per construcție; PNG eliminat V41) |
| _template/ matriță | rădăcină | ✓ 7 livrabile + assets/ |

---

## Cum se actualizează acest fișier

**Cine îl scrie:** Claude (motor) la fiecare modificare semnificativă.

**Când îl scrie:**
- După `genereaza CNN` cu PASS → update tabel construcții
- După `aplica fix` → update reguli noi
- După `consolideaza brain` → update sumar sesiune
- La fiecare incrementare V → update versiune + data

**Cum îl citește ARHITECT:** la fiecare sesiune nouă, primul lucru. 2 minute pentru a fi orientat.

---

## Următorul checkpoint așteptat

**V41 — generare C06**

Trigger: ARHITECT îngheaţă SPEC C06 (cele 9 elemente narrative) în `_system/arhiva/SISTEM_TRAINITY-versiuni.md` → comandă `genereaza C06` → motor rulează `pre_generation_check.py 06` → PASS → execută → V41 marcat aici cu C06 LIVRABIL.
