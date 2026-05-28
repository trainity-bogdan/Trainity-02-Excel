# Trainity · Pack 02 Excel · INDEX SISTEM

**Versiune sistem:** V40 · ultima actualizare: 28 mai 2026

---

## Ce este acest sistem

Un pachet de **20 de construcții educaționale Excel** (C01-C20), augmentate cu AI, organizate pe 5 trepte SCARA. Fiecare construcție livrează 7 artefacte canonice (studiu interactiv, film cinematic, dataset, narativă, script video) + folder `assets/` cu 12 imagini exec-stage.

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

Plus `COMENZI.yaml` (catalog machine-readable) + `INDEX-CAUTARE.md` (search alphabetic).

---

## Structura repository (V40)

```
trainity-pack-02-excel/                (în OneDrive, NU Git)
│
├── CLAUDE.md                         boot rapid pentru motor (Claude)
├── STARE-CURENTA.md                  single source of truth status
├── README.md                         prima pagină proiect
├── .gitignore                        artefact istoric (NU folosim Git)
│
├── _template/                        MATRIȚĂ de generare (clonă structură pentru C06+)
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER + Creativ + FILM
│   └── assets/                       imagini placeholder
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
│   ├── arhiva/                       istoric V01-V40, NU pentru referință zilnică
│   │   ├── brain-evolutia-V01-V38.md
│   │   ├── SISTEM_TRAINITY-versiuni.md
│   │   ├── KIT-V38-INSTRUCTIUNI.md
│   │   ├── WORKFLOW-CAP-COADA.md
│   │   ├── GHID-SETUP-GITHUB-PLAN-NEEXECUTAT.md  (plan istoric, neadoptat)
│   │   └── RAPORT-CONSTRUCTIE-C04-V27.md
│   │
│   ├── generatoare/                  scripturi Python operationale
│   │   ├── audit_sync.py             ✓ esential (8 detectoare V40)
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
│   ├── referinte/                    asset perpetuu
│   │   ├── Date_MASTER-initial.xlsx  dataset canonic 2000 facturi
│   │   ├── IDENTITATE-TEHNICA.md     schema R-V03.47
│   │   ├── DATA-INSTRUCTIUNI.md
│   │   ├── SCHEMA-MASTER.md
│   │   ├── COVER-CHECKLIST.md
│   │   ├── PROTOCOL-FILM-OBS.md
│   │   ├── highlighter-snippet.css
│   │   └── highlighter-snippet.js
│   │
│   └── snapshots/                    snapshots oficiale V{N} (regula V2 din CLAUDE.md)
│       └── V{N}_AAAALLZZ/            copii ale construcțiilor la momentul V{N} + manifest.md
│
├── c01/                              CONSTRUCȚIE (o singură versiune V39+)
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER-C01.xlsx
│   ├── Creativ + FILM
│   └── assets/                       12 imagini exec-stage SPECIFICE C01 (jpg+png)
│
├── c02/  c03/  c04/  c05/            idem (fiecare cu assets/ proprii)
└── (c06-c20: queue)
```

**Backup-uri ad-hoc** (regula V1): `cNN_BACKUP_AAAALLZZ_pre-{operatiune}/` apar temporar la rădăcină când motor face operațiune distructivă. ARHITECT le poate șterge după ce e sigur că modificarea e bună.

---

## Filozofia sistemului (V40)

Sistemul respectă trei principii:

**1. Matriță explicit separată (V39+)**
`_template/` e matrița curată folosită la generare CNN+. Construcțiile cNN/ sunt fiecare o versiune unică (NU canonic/editat split). Modificările live se aplică direct în cNN/.

**2. Patch over Edited (R-V03.62 absorbită, V39+)**
Upgrade-urile KIT se aplică ca patch-uri izolate în cNN/. Conținutul ARHITECT rămâne intact prin natura faptului că patch-ul țintește doar zona specifică. Pattern confirmat empiric V32-V34. Pentru operațiuni care ating >3 fișiere, BACKUP AUTO (regula V1) precede patch-ul.

**3. Audit empiric exhaustiv (R-V03.63)**
La fiecare consolidare/finalizare batch, `audit_sync.py` verifică toate regulile active per zonă. Zero drift = sistem sincronizat. Drift sau ERR > 0 = blocant, se repară înainte de continuare.

**4. Versionare OneDrive + backup discipline (V40+)**
OneDrive sync auto + Version History per fișier (~30 zile) + backup auto pre-destructive (V1) + snapshots V{N} la consolidare (V2) + restore fișier prin OneDrive Version History (V3). NU folosim Git. Vezi CLAUDE.md "VERSIONARE ONEDRIVE + BACKUP DISCIPLINE".

---

## Status actual (verificat empiric V40)

```
✓ 40 verificări empirice PASS (8 detectoare × 5 construcții)
✓ ZERO DRIFT real (post fix encoding audit_sync V40)
✓ Cele 7 artefacte + assets/ prezente per construcție
✓ Gate v20 PASS pe construcțiile testate (C02 confirmat)
✓ Scripturile validare reparate (encoding utf-8, stdout reconfigure, paths actualizate)
✓ Workflow OneDrive documentat (regulile V1/V2/V3)
```

---

## Comenzi de scurtătură (pentru orientare rapidă)

| Vreau să... | Comandă în chat | Document de citit |
|---|---|---|
| ...generez C06 | `genereaza C06` | 03 + 05 scenariu 1 |
| ...verific sincronizarea | `verifica sincronizare` | 03 |
| ...modific text într-o construcție | (nu necesită chat — lucrezi local, OneDrive sync auto) | 05 scenariu 4 |
| ...aplic bug fix la toate | `aplica fix [descriere]` | 05 scenariu 2 |
| ...adaug poză nouă cu Banana | `pentru CNN poza X` + atașez | 05 scenariu 3 |
| ...regenerez CNN cu SPEC nou | `regenereaza CNN de la zero` (cu backup auto) | 05 scenariu 5 |
| ...salvez snapshot oficial V{N} | `snapshot V{N}` | CLAUDE.md regula V2 |

Pentru detalii pas cu pas → `03-COMENZI-OPERATIONALE.md`.
