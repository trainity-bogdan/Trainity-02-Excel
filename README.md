# Trainity · Pack 02 Excel

Sistem de construcții educaționale Excel augmentate cu AI · Bogdan Târlă · Dr.Excel & Trainity

---

## Status la zi

**Versiune sistem:** V79 (iunie 2026 · nomenclatură SCARA C01-C20 LOCKED · PACK C01-C20 COMPLET)
**Construcții existente în repo:** C01-C20 (toate 20 generate: 4 HTML + Date_MASTER + FILM fiecare)

**Maturitate pe trepte (structură + date + FILM = complet pe toate 20):**
- **T1 SCANARE (C01-C04):** livrabile, imagini reale.
- **T2 CUNOAȘTERE (C05-C08):** livrabile, imagini reale.
- **T3 ANALIZĂ (C09-C12):** livrabile structural; C09 imagini reale; C10-C12 hero real, video placeholder.
- **T4 RAPORTARE (C13-C16):** complete structural; imagini placeholder (folder `assets/` + foto reale = dependență ARHITECT).
- **T5 AUTONOMIE (C17-C20):** complete structural; dataset propriu C01 (by design, înregistrat în gate `CONSTRUCTII_DATASET_C01`); imagini draft placeholder pending ARHITECT.

**Finisaj de imagine reală pe C10-C20 = dependență ARHITECT** (pipeline extern de imagini); structura, datele și FILM sunt complete.

**Lanțul T3 (locked):** model -> măsură -> clasament -> explicație
(C09 a lega · C10 a defini · C11 a compara · C12 a explica).

Pentru status detaliat -> `STARE-CURENTA.md`.

---

## Nomenclatura SCARA (LOCKED · 6 iunie 2026)

Cele 5 trepte: **SCANARE · CUNOAȘTERE · ANALIZĂ · RAPORTARE · AUTONOMIE** (S-C-A-R-A).

Fiecare construcție are două straturi de identitate:
- **STRAT 1 = CUVÂNT** (un cuvânt, majuscule): copertă, index, nume fișier, branding.
- **STRAT 2 = MIZĂ HERO**: descriptor metodologic afișat în Hero, derivat din nomenclatura oficială.

Sursă unică de adevăr: `_system/NOMENCLATURA-LOCKED-SCARA.md` (oglindit în `constructii.xlsx`).

| Cod | CUVÂNT | MIZĂ HERO | Verb |
|---|---|---|---|
| C01 | STRUCTURĂ | STRUCTURAREA TABELELOR | STRUCTUREZ |
| C02 | ADEVĂR | CONFRUNTAREA CU REALITATEA | CONFRUNT |
| C03 | AUDIT | AUDITAREA ERORILOR ASCUNSE | AUDITEZ |
| C04 | FLUX | NORMALIZAREA DATELOR | NORMALIZEZ |
| C05 | INVENTAR | INVENTARIEREA SETULUI DE DATE | INVENTARIEZ |
| C06 | REGULI | CLASIFICAREA RÂNDURILOR | CLASIFIC |
| C07 | TIMP | DATAREA TRANZACȚIILOR | DATEZ |
| C08 | HARTĂ | MAPAREA TABELELOR | MAPEZ |
| C09 | RELAȚII | LEGAREA TABELELOR | LEG |
| C10 | MĂSURĂ | DEFINIREA MĂSURILOR | MĂSOR |
| C11 | CLASAMENT | CONSTRUIREA CLASAMENTELOR | COMPAR |
| C12 | CAUZĂ | INTERPRETAREA REZULTATELOR | INTERPRETEZ |
| C13 | VIZUAL | FORMA ADEVĂRATĂ | VIZUALIZEZ |
| C14 | COMPOZIȚIE | ORDINEA PRIVIRII | COMPUN |
| C15 | SINTEZĂ | MESAJUL ESENȚIAL | SINTETIZEZ |
| C16 | LIVRARE | DECIZIA GATA | LIVREZ |
| C17 | SISTEM | SISTEMATIZAREA MUNCII RELUABILE | SISTEMATIZEZ |
| C18 | MOTOR | AUTOMATIZAREA MUNCII RECURENTE | AUTOMATIZEZ |
| C19 | CONTROL | GUVERNAREA SISTEMULUI PRIN REGULI | GUVERNEZ |
| C20 | AUTONOMIE | DELEGAREA SISTEMULUI DE LUCRU | DELEG |

---

## Cele 6 artefacte per construcție

1. HTML-Studiu
2. HTML-Editor-Studiu
3. HTML-Video (base64 inline)
4. HTML-Editor-Video
5. Date_MASTER-CNN.xlsx
6. FILM-Excel-NN-{slug}.docx

Plus folder `assets/` cu hero-poster + cele 6 imagini exec-stage (jpg, 3:2 cinematic),
specifice fiecărei construcții.

**Imaginile reale** se produc extern (ARHITECT + ChatGPT); motorul integrează imaginile
primite în `assets/` + base64. Prompturile de imagine NU se stochează în repo (Creativ abandonat V68).

---

## Structura repository

```
Trainity-02-Excel/
├── README.md
├── CLAUDE.md                         boot rapid pentru motor (Claude)
├── STARE-CURENTA.md                  single source of truth status
├── index.html                        panou preview live C01-C20
│
├── c01/ ... c20/                     CONSTRUCȚII (o singură versiune fiecare)
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER-CNN.xlsx
│   ├── FILM-Excel-NN-{slug}.docx
│   └── assets/                       hero + cele 6 imagini exec-stage ALE construcției
│
├── _system/                          SISTEMUL
│   ├── 00-INDEX.md ... 14-ARHITECTURA-CONCEPTUALA-T5.md
│   ├── COMENZI.yaml, INDEX-CAUTARE.md
│   ├── generatoare/                  validatoare + scripturi Python
│   ├── governance/                   Bible, change protocol, release gate
│   └── referinte/                    Date_MASTER-initial, snippets, scheme
│
└── _brain/                           protocol BRAIN <-> CLAUDE + audituri
    ├── audit/                        rapoarte audit (apocalipsă V1/V2, atomic, locked-naming)
    └── cNN/                          mandate + context per construcție (C09-C20)
```

---

## Arhitectura: o singură versiune per construcție

Fiecare construcție are **un singur set** de fișiere în `cNN/`. NU există canonic/editat.

**Construcția de referință** = `c01/` (cobaiul: COPY+MODIFY pentru construcții noi;
modificările ample de sistem se testează întâi aici).

**Versionarea o face git:**
- Remote: `github.com/trainity-bogdan/Trainity-02-Excel`
- Lucru direct pe `main` cu commit descriptiv (workflow solo dev). Branch separat doar pentru
  regenerări distructive, experimente, sau la cererea ARHITECT.
- FĂRĂ tag-uri git (abandonate; versionarea = commit descriptiv pe `main` + `STARE-CURENTA.md`).
- Restore = `git show <sha>:path`, `git checkout <sha> -- cNN/`, `git revert <sha>`.
- Detalii: `CLAUDE.md` secțiunea VERSIONARE GIT (regulile G1-G5).

---

## Validatoare (în `_system/generatoare/`)

| Script | Rol |
|---|---|
| `audit_sync.py` | audit empiric drift (zero drift obligatoriu) |
| `gate_v20.py NN cNN c01` | gate post-flight pe 6 clase de erori |
| `pre_generation_check.py NN` | cele 3 checks HARD pre-generare (SPEC/identitate/fenomene) |
| `tier_guard_t3.py` | garda tier-aware T3 (C09-C12) |
| `detect_c06_purity.py` | puritate C06 (clasificare) |
| `detect_form_drift.py` | audit de formă retorică (anti-saturație) |

---

## Comenzi de scurtătură

| Vreau să... | Comandă |
|---|---|
| Status rapid | `status` |
| Generez o construcție | `genereaza CNN` (din c01) |
| Editez local | direct pe `main` + commit/push |
| Aplic bug fix | `aplica fix [desc]` |
| Adaug poză specifică | `pentru CNN poza X` + atașez |
| Verific drift | `verifica sincronizare` |

---

Trainity · Pack 02 Excel · preview live în `index.html`.
