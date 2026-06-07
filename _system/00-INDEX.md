# Trainity · Pack 02 Excel · INDEX SISTEM

**Versiune sistem:** V40 · ultima actualizare: 28 mai 2026

---

## Ce este acest sistem

Un pachet de **20 de construcții educaționale Excel** (C01-C20), augmentate cu AI, organizate pe 5 trepte SCARA. Fiecare construcție livrează 7 artefacte canonice (studiu interactiv, film cinematic, dataset, narativă, script video) + folder `assets/` cu 6 imagini exec-stage jpg.

Acesta este sistemul TRAINITY pentru produsele B2C (Pack Work 10X Excel) și B2B (Sistem Trainity Excel).

---

## Cum citești sistemul (ordinea recomandată)

Dacă ești **Bogdan** (ARHITECT) și vrei să dai o comandă rapidă → citește direct **03-COMENZI-OPERATIONALE**.

Dacă ești **Claude** (motor) la primul chat → citește în ordine:
1. `CLAUDE.md` la rădăcină (boot rapid, 30 sec)
2. `STARE-CURENTA.md` la rădăcină (status, 30 sec)
3. `00-INDEX.md` (acest fișier, 3 min)
4. `02-GLOSAR.md` (3 min)
5. `01-REGULI-ACTIVE.md` (10 min)
6. `04-ARHITECTURA-LIVRABILE.md` (5 min)
7. `03-COMENZI-OPERATIONALE.md` (5 min)
8. Restul se consultă specific când e nevoie.

---

## Cele 8 documente operaționale

| # | Document | Rol | Mărime |
|---|---|---|---|
| **00** | `00-INDEX.md` | Punctul de intrare. Hartă a sistemului. | ~5 KB |
| **01** | `01-REGULI-ACTIVE.md` | Toate regulile vii cu detector empiric. Sursa de adevăr. | ~17 KB |
| **02** | `02-GLOSAR.md` | Termenii cheie definiți scurt. | ~10 KB |
| **03** | `03-COMENZI-OPERATIONALE.md` | "Vreau X, comanda e Y". FAQ operațional. | ~8 KB |
| **04** | `04-ARHITECTURA-LIVRABILE.md` | Schema 7 artefacte + versiune unică per cNN (V39+). | ~8 KB |
| **05** | `05-WORKFLOW-PER-SCENARIU.md` | Cele 5 scenarii reale, pas cu pas. | ~13 KB |
| **06** | `06-MAP-CONSTRUCTII-T1-T5.md` | Cele 20 construcții mapate pe 5 trepte. | ~11 KB |
| **07** | `07-BRAND-OPERATIONAL.md` | Cum se exprimă brand-ul în fișiere. | ~11 KB |
| **11** | `11-ARHITECTURA-CONCEPTUALA-T2.md` | **AUTORITATE conceptuală T2** (axe C05-C08, ce face/NU face, garda T2/T3, prioritate peste istoric pre-V45). Citește înainte de orice C05-C08. | ~6 KB |
| **12** | `12-ARHITECTURA-CONCEPTUALA-T3.md` | **AUTORITATE conceptuală T3** (lanț C09-C12, verbe-semnătură, granițe, formula T3/T4/T5). Citește înainte de orice C09-C12. | ~6 KB |
| **13** | `13-ARHITECTURA-CONCEPTUALA-T4.md` | **AUTORITATE conceptuală T4** (lanț C13-C16, pilon „T4 consumă răspunsul T3", granițe, voce, testul 2030). Citește înainte de orice C13-C16. | ~8 KB |

Plus `COMENZI.yaml` (catalog machine-readable) + `INDEX-CAUTARE.md` (search alphabetic).

---

## Structura repository (V41)

```
Trainity-02-Excel/                    (git repo, remote: github.com/trainity-bogdan/Trainity-02-Excel)
│
├── CLAUDE.md                         boot rapid pentru motor (Claude)
├── STARE-CURENTA.md                  single source of truth status
├── README.md                         prima pagină proiect
├── .gitignore                        config git
│
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER + FILM
│   └── assets/                       hero + 6 imagini exec-stage
│
├── _system/                          SISTEMUL
│   ├── 00-INDEX.md                   (acest fișier)
│   ├── 01-REGULI-ACTIVE.md           reguli vii
│   ├── 02-GLOSAR.md
│   ├── 03-COMENZI-OPERATIONALE.md
│   ├── 04-ARHITECTURA-LIVRABILE.md
│   ├── 05-WORKFLOW-PER-SCENARIU.md
│   ├── 06-MAP-CONSTRUCTII-T1-T5.md
│   ├── 07-BRAND-OPERATIONAL.md
│   ├── COMENZI.yaml                  catalog machine-readable
│   ├── INDEX-CAUTARE.md              search alphabetic
│   │
│   ├── arhiva/                       istoric V01-V41, NU pentru referință zilnică
│   │   ├── brain-evolutia-V01-V38.md
│   │   ├── SISTEM_TRAINITY-versiuni.md
│   │   ├── KIT-V38-INSTRUCTIUNI.md
│   │   ├── WORKFLOW-CAP-COADA.md
│   │   └── RAPORT-CONSTRUCTIE-C04-V27.md
│   │
│   ├── generatoare/                  scripturi Python operationale
│   │   ├── audit_sync.py             ✓ esential (8 detectoare)
│   │   ├── gate_v20.py               ✓ esential (6 clase)
│   │   ├── pre_generation_check.py   ✓ esential (3 checks)
│   │   ├── patch_runner.py           ✓ esential (motor patch unificat)
│   │   ├── gen_date_master_initial.py
│   │   ├── gen_imagini_base64.py
│   │   ├── init_canonic_editat.py    LEGACY V36 (nu mai e folosit din V39)
│   │   └── arhiva/                   scripturi învechite (V32-V33-V34 patch-uri individuale)
│   │
│   ├── patch_recipes/                rețete YAML pentru patch-uri
│   │   └── R-V03.{XX}-{slug}.yaml
│   │
│   └── referinte/                    asset perpetuu
│       ├── Date_MASTER-initial.xlsx  dataset canonic 2000 facturi
│       ├── IDENTITATE-TEHNICA.md     schema R-V03.47
│       ├── DATA-INSTRUCTIUNI.md
│       ├── SCHEMA-MASTER.md
│       ├── COVER-CHECKLIST.md
│       ├── PROTOCOL-FILM-OBS.md
│       ├── highlighter-snippet.css
│       └── highlighter-snippet.js
│
├── c01/                              CONSTRUCȚIE (o singură versiune V39+)
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER-C01.xlsx
│   ├── FILM
│   └── assets/                       hero + 6 imagini exec-stage SPECIFICE C01 (jpg, 3:2 cinematic)
│
├── c02/  c03/  c04/  c05/            idem (fiecare cu assets/ proprii)
└── (c06-c20: queue)
```

**Versionare:** git ține istoricul complet. Branch-uri per task semnificativ (`feat/cNN-generare`, `fix/<slug>`, `regen/cNN-AAAALLZZ`, `chore/brand-*`). Tag-uri anotate `v{N}` la incrementare versiune sistem. Rollback prin `git checkout`, `git revert`, `git show`.

---

## Filozofia sistemului (V41)

Sistemul respectă patru principii:

**1. Matriță explicit separată (V39+)**
`c01/` e construcția de referință (cobaiul) folosită la generare CNN+ (V46: `_template/` eliminat). Construcțiile cNN/ sunt fiecare o versiune unică (NU canonic/editat split). Modificările live se aplică direct în cNN/.

**2. Patch over Edited (R-V03.62 absorbită, V39+)**
Upgrade-urile KIT se aplică ca patch-uri izolate în cNN/. Conținutul ARHITECT rămâne intact prin natura faptului că patch-ul țintește doar zona specifică. Pattern confirmat empiric V32-V34. Pentru schimbări sistemice, branch dedicat + commit + PR (recomandat).

**3. Audit empiric exhaustiv (R-V03.63)**
La fiecare consolidare/finalizare batch, `audit_sync.py` verifică toate regulile active per zonă. Zero drift = sistem sincronizat. Drift sau ERR > 0 = blocant, se repară înainte de continuare.

**4. Versionare git (V41+)**
Versionarea o face git: commit per modificare logică + branch per task semnificativ + tag anotat `v{N}` la incrementare versiune sistem. Restore via `git checkout/show/revert`. Remote: GitHub. Vezi CLAUDE.md „VERSIONARE GIT" (regulile G1-G5).

---

## Status actual (verificat empiric V41)

```
✓ 40 verificări empirice PASS (8 detectoare × 5 construcții)
✓ ZERO DRIFT real
✓ Cele 7 artefacte + assets/ prezente per construcție
✓ Gate v20 PASS pe construcțiile testate (C02 confirmat)
✓ Scripturile validare funcționale (encoding utf-8, stdout reconfigure)
✓ Workflow git documentat (regulile G1-G5)
```

---

## Comenzi de scurtătură (pentru orientare rapidă)

| Vreau să... | Comandă în chat | Document de citit |
|---|---|---|
| ...generez C06 | `genereaza C06` | 03 + 05 scenariu 1 |
| ...verific sincronizarea | `verifica sincronizare` | 03 |
| ...modific text într-o construcție | (lucrezi local + commit/push în GitHub Desktop, opțional ceri eu commit-ul) | 05 scenariu 4 |
| ...aplic bug fix la toate | `aplica fix [descriere]` | 05 scenariu 2 |
| ...adaug poză nouă cu Banana | `pentru CNN poza X` + atașez | 05 scenariu 3 |
| ...regenerez CNN cu SPEC nou | `regenereaza CNN de la zero` (branch dedicat + git history păstrează versiunea veche) | 05 scenariu 5 |
| ...marchez stare oficială V{N} | `tag V{N}` | CLAUDE.md regula G3 |
| ...urc commit-urile pe GitHub | `push` | 03 secțiunea remote git |

Pentru detalii pas cu pas → `03-COMENZI-OPERATIONALE.md`.
