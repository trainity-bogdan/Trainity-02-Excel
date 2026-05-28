# CLAUDE.md · Boot rapid pentru tine, motor

**Primul fișier pe care îl citești la fiecare chat nou.** Te face operațional în 30 secunde.

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
| `regenereaza CNN de la zero` | Suprascrie versiunea (cu confirmare) | backup auto `cNN_BACKUP_AAAALLZZ_pre-regen/` înainte |
| `verifica sincronizare` | Rulez audit_sync.py | raportez tabel drift |
| `aplica fix [desc]` | Patch script peste construcții | folosesc patch_runner.py + rețetă YAML + backup auto dacă >3 fișiere |
| `compara C{NN} cu versiunea anterioara` | Diff vs versiune mai veche OneDrive | folosesc OneDrive Version History per fișier |
| `regula noua R-V03.X: [desc]` | Codific regulă nouă | adaug în 01-REGULI + detector + rețetă patch |
| `snapshot V{N}` | Salvez snapshot oficial la incrementare V | copie c01..cN în `_system/snapshots/V{N}_AAAALLZZ/` |
| `consolideaza brain` | Sumarizare sesiune | update STARE-CURENTA + snapshot V{N} automat |
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
└── assets/           ← cele 6 imagini exec-stage ALE construcției (jpg+png)
```

**MATRIȚA pentru COPY+MODIFY** = `_template/`. La generare CNN, citești de aici.

**Imaginile sunt DIFERITE per construcție** — fiecare cNN/assets/ are pozele lui.

---

## VERSIONARE ONEDRIVE + BACKUP DISCIPLINE

**Proiectul trăiește în OneDrive cloud.** NU folosim Git. Versionarea = OneDrive auto-sync + Version History per fișier (~30 zile).

**Limitarea OneDrive:** nu există restore la nivel de folder întreg nativ. Pentru asta folosim disciplina backup manual prin 3 reguli:

### V1. BACKUP PRE-DESTRUCTIVE (auto)
Înainte de orice operațiune care **suprascrie un folder** sau **modifică >3 fișiere simultan**, motor creează automat:
```
cNN/                              ← original (va fi suprascris)
cNN_BACKUP_AAAALLZZ_pre-{op}/     ← copie de siguranță, sync OneDrive
```
Aplicabil la: `regenereaza CNN de la zero`, `aplica fix [desc]` (dacă atinge >3 fișiere), refactor masiv.

### V2. SNAPSHOT LA INCREMENTARE V (auto, în `consolideaza brain`)
La fiecare bump versiune (V40 → V41), motor creează automat:
```
_system/snapshots/V{N}_AAAALLZZ/
├── c01/  c02/  ...  c{ultima}/   ← copii ale construcțiilor la momentul V{N}
└── manifest.md                    ← ce conține V{N}, ce s-a schimbat vs V{N-1}
```
Asta e echivalent Git "tag" în OneDrive. Permite întoarcere la orice V istoric.

### V3. RESTORE FIȘIER UNIC = OneDrive Version History
Dacă strici un singur fișier: drept-click în Explorer → **Version History** → alegi versiunea → Restore. Nu necesită implicarea motorului.

**Sumar disciplină:**
- Modificări mici (1-3 fișiere): OneDrive auto-version e suficient
- Modificări medii (>3 fișiere) sau distructive: backup folder auto
- Increment V: snapshot oficial în `_system/snapshots/`

Detalii operațional: `_system/COMENZI.yaml` (comenzi cu backup auto) + `_system/03-COMENZI-OPERATIONALE.md`.

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
- **Întrebări ca grilă** A/B/C, niciodată variantă unică autoritară.
- **Filtrul SIGUR/CONFLICT** la feedback extern (vezi G-06 în arhivă).
- **Limbaj** românesc cu diacritice.

---

## CÂND CONSOLIDEZI BRAIN

La sfârșit de sesiune cu decizii importante:
1. Actualizezi `STARE-CURENTA.md` (versiune nouă, lecții noi)
2. Update `_system/arhiva/brain-evolutia-V01-V38.md` cu sumar V{N curent}
3. **Snapshot V{N} automat** (regula V2): creez `_system/snapshots/V{N}_AAAALLZZ/` cu copii ale construcțiilor + manifest.md
4. Raportez ARHITECT: "V{N} consolidat. Snapshot salvat. OneDrive sync în background."

---

**FINAL:** orice e ambiguu, consultă INDEX-CAUTARE.md. Orice e blocant, oprește și raportează.

Versiune document: V40 · 28 mai 2026
