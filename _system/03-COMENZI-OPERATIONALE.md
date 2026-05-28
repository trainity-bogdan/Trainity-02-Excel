# Comenzi operaționale Trainity (V40)

Toate comenzile pe care le poți da în chat cu Claude, organizate după **intenție**.

**Workflow:** OneDrive auto-sync, versiune unică per `cNN/` (NU canonic/editat), NU Git. Detalii: `CLAUDE.md` + `_system/COMENZI.yaml`.

---

## Comenzi de generare

| Vrei să... | Scrii în chat | Atinge |
|---|---|---|
| Generezi C06 de la zero | `genereaza C06` | `c06/` (cu 7 artefacte + assets/) |
| Regenerezi C03 COMPLET de la zero | `regenereaza C03 de la zero` | `c03/` (cu confirmare + BACKUP AUTO pre-execuție) |
| Generezi mai multe construcții odată | `genereaza C06-C08 in serie` | C06, apoi C07, apoi C08 (cu pauze pentru confirmare) |

### Detalii `genereaza CNN`

Motorul face:
1. Rulează `pre_generation_check.py NN` (cele 3 checks HARD):
   - R-V03.55 SPEC CNN înghețat?
   - L142 IDENTITATE_TEHNICA CNN populată?
   - L143 FENOMENE vs asset fizic aliniate?
2. Citește `_template/` ca matriță
3. Aplică COPY+MODIFY pe cele 4 HTML-uri
4. Generează Date_MASTER-CNN.xlsx din `_system/referinte/Date_MASTER-initial.xlsx`
5. Generează Creativ-Excel-NN-{slug}.txt + FILM-Excel-NN-{slug}.docx
6. Copiază 12 imagini placeholder în `cNN/assets/`
7. Scrie totul în `cNN/`
8. Rulează `audit_sync.py` → confirmă zero drift
9. Rulează `gate_v20.py NN cNN _template` → PASS
10. Raportează ZERO DRIFT + cele 7 livrabile prezente. OneDrive sync în background.

**Durată estimată:** 3-5 minute pentru o construcție.

### Detalii `regenereaza CNN de la zero`

**Cerere distructivă.** Motorul:
1. Cere confirmare explicită
2. **BACKUP AUTO (regula V1):** copy `cNN/` → `cNN_BACKUP_AAAALLZZ_pre-regen/`
3. Șterge `cNN/`
4. Aplică flow `genereaza` de la zero

Detalii: `05-WORKFLOW-PER-SCENARIU.md` scenariu 5.

---

## Comenzi de editare conținut (FĂRĂ chat)

Modificările de conținut le faci local, fără să-mi scrii nimic.

### Editezi text în HTML-Studiu sau HTML-Video

1. Deschide `cNN/HTML-Editor-Studiu-Excel-NN-{slug}.html` în Chrome
2. Click pe text → editezi inline
3. Apasă **💾 EXPORT** (toolbar sus) → primesti fișier descărcat
4. Înlocuiește `cNN/HTML-Studiu-Excel-NN-{slug}.html` cu fișierul descărcat (suprascrie cel existent)

**OneDrive sync automat în câteva secunde.** Version History capturează versiunea veche pentru rollback (drept-click → Version History).

### Vrei să-mi semnalizezi că ai modificat ceva

| Scrii în chat | Eu fac |
|---|---|
| `am modificat C03, verifica` | Citesc fișierul, raportez ce e diferit (dacă am referință de comparat: backup local sau snapshot) |
| `am modificat C03, aplica audit` | Rulez audit_sync.py → confirm că modificările tale nu sparg sistemul |

---

## Comenzi de upgrade KIT (bug-uri, regule noi)

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Repari un bug peste toate construcțiile | `bug: [descriere]. Aplică pe C01-C06` | Propun fix, BACKUP AUTO dacă >3 fișiere, scriu patch, aplic batch, audit |
| Adaugi o regulă nouă | `regulă nouă: [descriere]. Codifică ca R-V03.X` | Adaug în 01-REGULI-ACTIVE, scriu detector în audit_sync, aplic retroactiv (cu backup auto) |
| Schimbi setarea vizuală globală | `schimba [X] pe toate HTML-Studiu` | Backup auto + patch script + aplicare + audit |
| Verifici sincronizarea după modificări | `verifica sincronizare` | Rulez audit_sync.py → raportez tabel cu drift |

### Exemplu concret: bug fix font buton

> **Tu**: "bug: butonul VERIFICĂ are font 12px pe mobile, ar trebui 14px. Aplică pe C01-C06"

> **Eu**:
> 1. Citesc `c01/HTML-Studiu-Excel-01-Structura.html` să localizez CSS-ul
> 2. Confirm cu tine: "Propun `@media (max-width: 768px) { .step-verify-btn { font-size: 14px; } }`. Patch atinge >3 fișiere → BACKUP AUTO pe C01-C06. Confirmi?"
> 3. **Tu**: "da"
> 4. BACKUP AUTO: copy `cNN/` → `cNN_BACKUP_AAAALLZZ_pre-fix/` pentru fiecare construcție
> 5. Scriu rețetă patch în `_system/patch_recipes/R-V03.66-font-buton-responsive.yaml`
> 6. Aplic peste `c01/, c02/, ..., c06/`
> 7. Adaug regulă R-V03.66 în 01-REGULI-ACTIVE.md + detector în audit_sync.py
> 8. Audit → zero drift
> 9. Raportez: "Fix aplicat. Backup-uri salvate. OneDrive sync."

---

## Comenzi de poze (Banana 2)

| Vrei să... | Scrii în chat | Atașez? |
|---|---|---|
| Înlocuiești poza X în C06 | `pentru C06, poza nouă exec-stage-1` + atașezi cele 2 fișiere (jpg + png) | DA, atașezi pozele |
| Înlocuiești poză peste toate | `aceasta poză înlocuiește exec-stage-1 la toate` + atașezi | DA |
| Folosești poză care e deja pe disk | `pentru C06, refoloseste imaginea curentă din c06/assets/` | NU, eu citesc din disk |

### Detalii

**Asset-uri per construcție:**
Imaginile sunt **diferite per construcție** (V39). Trăiesc în `cNN/assets/exec-stage-1..6.{jpg,png}`. Eu le pun acolo, le encodez base64, le inlinuesc în HTML-Video + HTML-Editor-Video.

**Asset-uri brand (toate construcțiile):**
Pentru o imagine care merge peste toate construcțiile (de ex. logo final actualizat), aplic în fiecare `cNN/assets/` separat (BACKUP AUTO pe toate). NU mai există `_system/referinte/assets_canonice/` (eliminat la V39).

---

## Comenzi de audit și verificare

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Vezi starea generală a sistemului | `arata status` | Rulez audit + raportez tabel + cele 7 artefacte verificate per construcție |
| Verifici o construcție specifică | `verifica C03` | Gate v20 + audit individual + raport |
| Vezi diferențele între versiuni | `compara C03 cu versiunea anterioara` | Folosesc backup local sau snapshot V{N} sau OneDrive Version History |
| Vezi diferențele între 2 construcții | `compara C02 si C03` | Diff structural pe HTML și Date_MASTER |

---

## Comenzi rare (cu confirmare)

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Migrarea unei construcții la altă schemă | `migreaza C03 la noua schema` | Cer confirmare + BACKUP AUTO obligatoriu |
| Ștergi o construcție | `sterge C12` | CER CONFIRMARE DUBLĂ + BACKUP AUTO |
| Restore o construcție dintr-un backup | `restore C03 din c03_BACKUP_AAAALLZZ_pre-regen/` | Ștergi versiunea actuală, redenumesc backup-ul |

---

## Comenzi de meta-sistem

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Actualizezi documentația sistem | `update sistem cu [nouă lecție / regulă]` | Modific 01-REGULI-ACTIVE + 02-GLOSAR dacă e cazul |
| Adaugi o lecție nouă | `lecție nouă: [descriere]` | Adaug L1X în arhivă cu numerotare continuă |
| Vezi versiunea curentă a sistemului | `ce versiune e?` | V curentă + ultima sesiune + status sistem |
| Pornesc o consolidare brain | `consolideaza brain` | Sumarizare sesiune + SNAPSHOT AUTO V{N} (regula V2) + update STARE-CURENTA |
| Creezi snapshot manual la V{N} | `snapshot V40` | Copy `c01..cN` → `_system/snapshots/V40_AAAALLZZ/` + manifest.md |

---

## Cazul "nu știu ce să-i cer"

Dacă nu știi exact ce comandă, scrie natural ce vrei:

> "vreau să schimb titlul din C03 dar nu știu cum"
> 
> Eu te ghidez: îți spun să deschizi `c03/HTML-Editor-Studiu-...`, click pe titlu, edit, EXPORT, înlocuire.

> "vreau să fac diferit doza între prompturi"
> 
> Eu îți explic: e ajustare CSS globală pe `.prompt-box`, pot face patch pe toate (cu backup auto), sau editezi local.

**Nu trebuie să memorezi comenzi.** Scrie natural, eu interpretez și propun comanda exactă.

---

## Cazul "comanda mea nu funcționează"

Dacă spui o comandă și nu se întâmplă ce așteptai, **întreabă-mă să verific**:

> "am dat comanda X, dar fișierul Y nu s-a modificat"
> 
> Eu rulez audit, verific ce s-a întâmplat efectiv, raportez. Dacă am stricat ceva, restorez din backup.

---

## Sumar cu cele mai folosite 10 comenzi

| # | Comandă | Frecvență estimată |
|---|---|---|
| 1 | `genereaza CNN` | La fiecare construcție nouă |
| 2 | `verifica sincronizare` | După orice modificare semnificativă |
| 3 | `bug: [descriere]. Aplică pe C01-C06` | Săptămânal/lunar |
| 4 | `compara C03 cu versiunea anterioara` | Ad-hoc pentru audit |
| 5 | `am modificat C03, verifica` | După editări locale |
| 6 | `arata status` | Începutul fiecărei sesiuni |
| 7 | `regula noua: [descriere]` | Lunar |
| 8 | `regenereaza CNN de la zero` | Rar (după SPEC nou) |
| 9 | `consolideaza brain` | La sfârșitul sesiunilor lungi |
| 10 | `pentru CNN poza X` + atașez | La fiecare schimbare vizuală |

---

## Workflow zilnic tipic

**Dimineața:**
> `arata status`

Eu raportez: versiune curentă, ce construcții sunt sincronizate, audit ZERO DRIFT, eventuale TODO-uri.

**Lucrul efectiv:**
- Modificări de conținut: tu local + EXPORT + suprascriu (OneDrive sync auto, fără chat)
- Modificări sistem: comandă în chat → eu lucrez (cu BACKUP AUTO dacă e cazul)

**Seara:**
> `consolideaza brain` (dacă a fost sesiune cu multe decizii)

Eu sumarizez sesiunea + creez SNAPSHOT AUTO V{N} (regula V2).

---

Pentru flux complet pas cu pas pe scenariile reale → `05-WORKFLOW-PER-SCENARIU.md`.

Pentru regulile de versionare OneDrive + backup → `CLAUDE.md` secțiunea "VERSIONARE ONEDRIVE + BACKUP DISCIPLINE".
