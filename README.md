# Trainity · Pack 02 Excel

Sistem de construcții educaționale Excel augmentate cu AI · Bogdan Târlă · Dr.Excel & Trainity

---

## Status la zi

**Versiune sistem:** V68 (iunie 2026)
**Construcții existente în repo:** C01-C12 (din 20 planificate)

**Maturitate pe trepte:**
- **T1 SCANARE (C01-C04):** livrabile.
- **T2 CUNOAȘTERE (C05-C08):** livrabile.
- **T3 ANALIZĂ (C09-C12):** corecte conceptual și în date; finisaj vizual în curs.
  - C09 RELAȚII aproape final.
  - C10 MĂSURI, C11 COMPARAȚII, C12 INTERPRETARE complete conceptual; imaginile reale
    rămân dependență ARHITECT (până atunci, unde lipsesc, placeholder neutru marcat temporar).

**Lanțul T3 (locked):** model -> măsură -> clasament -> explicație
(C09 a lega · C10 a defini · C11 a compara · C12 a explica).

Pentru status detaliat -> `STARE-CURENTA.md`.

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
├── index.html                        panou preview live C01-C12
│
├── c01/ ... c12/                     CONSTRUCȚII (o singură versiune fiecare)
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER-CNN.xlsx
│   ├── FILM-Excel-NN-{slug}.docx
│   └── assets/                       hero + cele 6 imagini exec-stage ALE construcției
│
├── _system/                          SISTEMUL
│   ├── 00-INDEX.md ... 12-ARHITECTURA-CONCEPTUALA-T3.md
│   ├── COMENZI.yaml, INDEX-CAUTARE.md
│   ├── generatoare/                  validatoare + scripturi Python
│   ├── governance/                   Bible, change protocol, release gate
│   └── referinte/                    Date_MASTER-initial, snippets, scheme
│
└── _brain/                           protocol BRAIN <-> CLAUDE + audituri
    ├── audit/                        rapoarte audit (apocalipsă V1, V2)
    └── cNN/                          mandate + context per construcție T3
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
