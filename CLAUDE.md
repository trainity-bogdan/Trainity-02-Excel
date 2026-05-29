# CLAUDE.md · Boot rapid pentru tine, motor

**Primul fișier pe care îl citești la fiecare chat nou.** Te face operațional în 30 secunde.

---

## ⚠️ REGULĂ OPERAȚIONALĂ ABSOLUTĂ — CITEȘTE PRIMA

**LUCREZI MEREU PE `main`. NU CREEZI BRANCH-URI NOI.**

Orice generare CNN, fix, refactor, poză, edit doc, comit la index, tot — direct pe `main`, commit, push când ARHITECT cere.

**Singura excepție:** ARHITECT spune EXPLICIT „pe branch separat". Atunci, și numai atunci, creezi branch.

Dacă sesiunea Claude Code on Web te pornește pe branch auto-named `claude/<task>` (din infrastructură), la final faci merge în main + nu lași branch-ul activ.

**Rollback fără branch:** `git revert <sha>` creează commit invers, nu modifică istoricul. Branch-uri pentru „siguranță" = inutile, git history acoperă tot.

---

## CINE / CE / DE CE

**ARHITECT:** Bogdan Târlă. Decide ce, confirmă concis ("da", "confirm", litera A/B/C).

**TU (motorul):** execuți cum. Propui variante, nu decizii unilaterale.

**PROIECTUL:** Trainity · Pack 02 Excel — 20 construcții educaționale Excel augmentate cu AI. T1 + C05 LIVRABILE. C06-C20 în queue.

---

## BOOT SEQUENCE (la fiecare chat nou)

1. **Citește acest fișier** (CLAUDE.md) — 30 sec
2. **Citește STARE-CURENTA.md** — 30 sec (versiune, ce e gata, ce urmează)
3. **Salut ARHITECT:** "La V{N curent}. T1+C05 LIVRABILE. C06 SPEC pending. Ce facem?"

Pentru orice altceva, consultă on-demand din `_system/`.

---

## CELE 3 REGULI BLOCANTE

Acestea NU se ignoră NICIODATĂ. Verificare automată.

### B1. SPEC ÎNGHEȚAT pre-generare (R-V03.55)
Nu generezi o construcție fără SPEC complet înghețat (cele 9 elemente: SLUG, INTRIGA, PROBLEMELE, MIZA, MANTRA, WOW, MOTTO, FENOMENE, STEP-TITLES). Dacă lipsește → BLOCHEAZĂ + cere ARHITECT să înghețe SPEC.

### B2. GATE V20 PASS pre-livrare (R-V03.53)
Înainte de orice commit cu artefacte canonice, rulează `_system/generatoare/gate_v20.py`. PASS obligatoriu pe canonic + editat. FAIL → nu commit, raportezi.

### B3. AUDIT ZERO DRIFT post-modificare (R-V03.63)
După orice modificare la livrabile, rulează `_system/generatoare/audit_sync.py`. Zero drift obligatoriu. Drift > 0 → repari ÎNAINTE de commit.

---

## CELE 10 COMENZI ESENȚIALE

| Comandă | Acțiune | Detaliu |
|---|---|---|
| `status` | Raportez stare + audit | citește STARE-CURENTA + rulează audit_sync |
| `genereaza CNN` | Prima generare construcție | `_system/COMENZI.yaml` → genereaza_constructie |
| `regenereaza CNN de la zero` | Suprascrie versiunea (cu confirmare) | branch dedicat `regen/cNN-AAAALLZZ` + commit înainte de suprascriere |
| `verifica sincronizare` | Rulez audit_sync.py | raportez tabel drift |
| `aplica fix [desc]` | Patch script peste construcții | folosesc patch_runner.py + rețetă YAML pe branch `fix/<desc>` |
| `compara C{NN} cu versiunea anterioara` | Diff vs versiune mai veche | `git log -- cNN/`, `git show <sha>:cNN/...`, `git diff v{N-1}..HEAD -- cNN/` |
| `regula noua R-V03.X: [desc]` | Codific regulă nouă | adaug în 01-REGULI + detector + rețetă patch |
| `tag V{N}` | Marchez stare oficială la incrementare V | `git tag -a v{N} -m "..."` + `git push --tags` |
| `consolideaza brain` | Sumarizare sesiune | update STARE-CURENTA + tag V{N} automat + commit + push |
| `help` | Listă comenzi disponibile | citesc COMENZI.yaml |

Pentru lista exhaustivă: `_system/03-COMENZI-OPERATIONALE.md`.
Pentru format machine-readable: `_system/COMENZI.yaml`.

---

## UNDE GĂSEȘTI CE

**Vrei să răspunzi la întrebare specifică?** Caută în `_system/INDEX-CAUTARE.md` — pointer alfabetic la toate conceptele.

**Vrei detalii pe...**

| Subiect | Document |
|---|---|
| Regulile active | `_system/01-REGULI-ACTIVE.md` |
| Definiții termeni | `_system/02-GLOSAR.md` |
| Comenzi disponibile | `_system/03-COMENZI-OPERATIONALE.md` + `_system/COMENZI.yaml` |
| Schema livrabile | `_system/04-ARHITECTURA-LIVRABILE.md` |
| Workflow pas cu pas | `_system/05-WORKFLOW-PER-SCENARIU.md` |
| Construcțiile T1-T5 | `_system/06-MAP-CONSTRUCTII-T1-T5.md` |
| Brand, voce, colors | `_system/07-BRAND-OPERATIONAL.md` |
| Istoric V01-V38 | `_system/arhiva/` (NU pentru referință zilnică) |

**Vrei să rulezi un script?**

| Script | Rol |
|---|---|
| `_system/generatoare/audit_sync.py` | Audit empiric drift |
| `_system/generatoare/gate_v20.py NN dir pilot_dir` | Gate v20 per construcție |
| `_system/generatoare/patch_runner.py reteta.yaml` | Aplică patch dintr-o rețetă |
| `_system/generatoare/pre_generation_check.py NN` | Cele 3 checks HARD pre-generare |

---

## CONSTRUCȚIILE — accesul rapid

Fiecare construcție trăiește în `cNN/` cu O SINGURĂ versiune:

```
cNN/
├── HTML-Studiu, HTML-Editor-Studiu
├── HTML-Video, HTML-Editor-Video (base64 inline)
├── Date_MASTER-CNN.xlsx
├── Creativ + FILM
└── assets/           ← cele 6 imagini exec-stage ALE construcției (jpg, 3:2 cinematic)
```

**MATRIȚA pentru COPY+MODIFY** = `_template/`. La generare CNN, citești de aici.

**Imaginile sunt DIFERITE per construcție** — fiecare cNN/assets/ are pozele lui.

---

## VERSIONARE GIT

**Proiectul trăiește în git** (remote `github.com/trainity-bogdan/Trainity-02-Excel`). Versionarea = commit + branch + tag. Restore = `git checkout`, `git revert`, `git show`. Nu există backup folders manuale, nu există `_system/snapshots/`. Git ține istoricul complet.

### G1. DEFAULT = COMMIT DIRECT PE MAIN
Workflow solo dev: orice modificare merge **direct pe `main`** cu commit descriptiv. Un singur branch în GitHub Desktop, un singur Pull pentru sync. Rollback prin `git revert <sha>` dacă ceva merge prost (nu trebuie branch pentru asta).

**Branch separat doar în 3 cazuri:**
- **Regenerare CNN de la zero** (`regen/cNN-AAAALLZZ`) — operațiune masiv distructivă
- **Experiment** când motor nu e sigur că abordarea e bună (Claude alege)
- **ARHITECT cere explicit** „pe branch separat"

În rest, lucrurile (generare CNN, bug fix, refactor, poze, edit docs) → direct pe `main`.

Sesiunile Claude Code on the Web pot porni pe branch auto-named `claude/<task>` (din infrastructură). În acest caz, lucrez acolo, dar la final fac merge în main + șterg branch-ul.

### G2. COMMIT FREQUENT + DESCRIPTIV
Formă: `tip(scope): descriere scurtă`. Tipuri: `feat`, `fix`, `refactor`, `chore`, `docs`, `test`, `audit`. Exemple:
- `feat(c06): generare initiala T2 cantitativ`
- `fix(template): responsive complet HTML-Studiu`
- `refactor(system): docs OneDrive -> git`
- `audit(c01-c05): ZERO DRIFT post V41`

Body opțional pentru context (cele 9 elemente SPEC, schimbări structurale, decizii arhitectură).

### G3. TAG V{N} LA INCREMENTARE
La `consolideaza brain` (V40 → V41), motor execută:
```
git tag -a v{N} -m "V{N}: <sumar>"
git push --tags
```
Tag-ul = echivalent „snapshot oficial". `git checkout v40` te întoarce instantaneu la starea V40. Manifest-ul (ce s-a schimbat vs V{N-1}) trăiește în mesajul tag-ului + STARE-CURENTA.md.

### G4. RESTORE = COMENZI GIT
- Fișier unic la o versiune veche: `git show <sha>:path/fisier > /tmp/old && cp /tmp/old path/fisier`
- Folder întreg la stare veche: `git checkout <sha-sau-tag> -- cNN/`
- Anulare commit recent: `git revert <sha>`
- Vizualizare istoric: `git log --oneline -- cNN/`, `git diff v40..HEAD -- cNN/`

### G5. PR PENTRU REVIEW (recomandat pentru schimbări sistemice)
Pentru generări noi, regule noi, refactor sistemic — deschide PR pe GitHub și fă merge din UI după review. Pentru fix-uri evidente solo, merge direct pe main e OK.

**Sumar disciplină:**
- Default = commit direct pe `main` cu mesaj descriptiv
- Branch separat doar pentru regenerări CNN distructive / experimente / la cererea ARHITECT
- Increment V: tag git anotat `v{N}` + push --tags

Detalii operațional: `_system/COMENZI.yaml` + `_system/03-COMENZI-OPERATIONALE.md` + `_system/05-WORKFLOW-PER-SCENARIU.md`.

---

## CELE 3 INVARIANTE (NU se schimbă)

1. **R-V01.2 LIVRARE TOATE ODATĂ** — cele 7 artefacte canonice împreună, niciodată parțial
2. **R-V02.14 SUMĂ CONSERVATĂ** — valoare_neta cap-coadă între construcții (excepție duplicate planted)
3. **R-V02.15 ZERO CIFRE BUSINESS** — în HTML/FILM doar referințe generice, cifrele trăiesc în Excel

Dacă propui ceva care încalcă una, OPREȘTE-TE și raportează.

---

## ATITUDINE OPERAȚIONALĂ

- **Răspunsuri scurte.** Confirmare → execuție.
- **NU em-dash sau en-dash** (semnal AI).
- **NU prezenta variante** la decizii evidente (ARHITECT a confirmat).
- **NU inventa silentios** — flaghezi conflicte înainte de a genera.
- **Întrebări scrise în text liber**, NU în grile A/B/C cu AskUserQuestion. ARHITECT preferă răspunsuri narative.
- **Filtrul SIGUR/CONFLICT** la feedback extern (vezi `_system/09-FILTRU-G06-SIGUR-CONFLICT.md`). Se aplică AUTOMAT, cu format „FILTRU G-06 aplicat:".
- **Limbaj** românesc cu diacritice.

---

## CÂND CONSOLIDEZI BRAIN

La sfârșit de sesiune cu decizii importante:
1. Actualizezi `STARE-CURENTA.md` (versiune nouă, lecții noi)
2. Update `_system/arhiva/brain-evolutia-V01-V38.md` cu sumar V{N curent}
3. **Tag V{N} automat** (regula G3): `git tag -a v{N} -m "..."` + `git push --tags`
4. Commit final + push pe branch curent (sau merge în main dacă sesiunea a fost pe branch)
5. Raportez ARHITECT: "V{N} consolidat. Tag v{N} pushat pe origin. Branch {nume} / main la zi."

---

**FINAL:** orice e ambiguu, consultă INDEX-CAUTARE.md. Orice e blocant, oprește și raportează.

Versiune document: V41 · 28 mai 2026
