# Trainity · Pack 02 Excel

Sistem de construcții educaționale Excel augmentate cu AI · Bogdan Târlă · Dr.Excel & Trainity

---

## Status la zi

**Versiune sistem:** V40 (28 mai 2026)
**Construcții livrate:** 5/20 (25%)
**Audit:** ZERO DRIFT (8 reguli × 5 construcții = 40 verificări PASS)

Pentru status detaliat → `STARE-CURENTA.md`

---

## Structura repository

```
trainity-pack-02-excel/
├── README.md
├── CLAUDE.md                         ← boot rapid pentru motor (Claude)
├── STARE-CURENTA.md                  ← single source of truth status
├── GHID-SETUP-GITHUB.md
├── .gitignore
│
├── _template/                        MATRIȚĂ de generare (clonă structură)
│   ├── HTML × 4
│   ├── Date_MASTER + Creativ + FILM
│   └── assets/                       imagini placeholder
│
├── _system/                          SISTEMUL
│   ├── 00-INDEX.md ... 07-BRAND-OPERATIONAL.md
│   ├── COMENZI.yaml, INDEX-CAUTARE.md
│   ├── arhiva/                       istoric V01-V38
│   ├── generatoare/                  scripturi Python
│   ├── patch_recipes/                rețete YAML patch
│   └── referinte/                    Date_MASTER-initial, snippets, scheme
│
├── c01/                              CONSTRUCȚIE (o singură versiune)
│   ├── HTML × 4 (Studiu, Editor-Studiu, Video, Editor-Video)
│   ├── Date_MASTER-C01.xlsx
│   ├── Creativ + FILM
│   └── assets/                       cele 6 imagini exec-stage ALE C01
│
├── c02/  c03/  c04/  c05/            idem (fiecare cu assets/ proprii)
└── (c06-c20: queue)
```

---

## Arhitectura: o singură versiune per construcție

Fiecare construcție are **un singur set** de fișiere în `cNN/`. NU mai există canonic/editat.

**Versionarea o face git:**
- Remote: `github.com/trainity-bogdan/Trainity-02-Excel`
- Branch per task semnificativ (`feat/cNN-*`, `fix/*`, `refactor/*`), merge pe main
- Tag anotat `v{N}` la incrementare versiune sistem (echivalent „snapshot oficial")
- Restore = `git show <sha>:path`, `git checkout v40 -- cNN/`, `git revert <sha>`
- Detalii: `CLAUDE.md` secțiunea „VERSIONARE GIT" (regulile G1-G5)

**Matrița pentru generare** = `_template/` (clonă a structurii, folosită la COPY+MODIFY pentru C06+).

**Imaginile sunt DIFERITE per construcție** — fiecare `cNN/assets/` conține cele 6 imagini exec-stage (jpg+png) specifice acelei construcții. La generare nouă, se înlocuiesc cu poze Banana specifice axei.

---

## Cele 7 artefacte per construcție

1. HTML-Studiu
2. HTML-Editor-Studiu
3. HTML-Video (base64 inline)
4. HTML-Editor-Video
5. Date_MASTER-CNN.xlsx
6. Creativ-Excel-NN-{slug}.txt
7. FILM-Excel-NN-{slug}.docx

Plus folder `assets/` cu cele 12 fișiere imagine (6 × jpg+png).

---

## Comenzi de scurtătură

| Vreau să... | Comandă |
|---|---|
| Status rapid | `status` |
| Generez C06 | `genereaza C06` (din _template) |
| Editez local | direct local + Commit/Push |
| Aplic bug fix | `aplica fix [desc]` |
| Adăug poză specifică | `pentru CNN poza X` + atașez |
| Verific drift | `verifica sincronizare` |

---

## Versiune sistem: V41 · 28 mai 2026

**V41 = fix responsive complet pe matrița HTML-Studiu (safe-area iPhone, breakpoint ≤380px, a11y aria/keyboard) + refactor invers OneDrive → git (V40 a presupus OneDrive bazat pe artefacte istorice; V41 confirmă git ca singura sursă de versionare).**

Versionarea = git commit + branch + tag + remote GitHub. Restore via `git checkout/show/revert`. Imaginile organizate per construcție (diferite per axă). Documentația operațională ~84 KB în 8 fișiere + meta-fișiere.
