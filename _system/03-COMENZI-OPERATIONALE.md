# Comenzi operaționale Trainity (V41)

Toate comenzile pe care le poți da în chat cu Claude, organizate după **intenție**.

**Workflow:** versionare git (commit + branch + tag), versiune unică per `cNN/` (NU canonic/editat). Detalii: `CLAUDE.md` secțiunea „VERSIONARE GIT" + `_system/COMENZI.yaml`.

---

## Comenzi de generare

| Vrei să... | Scrii în chat | Atinge |
|---|---|---|
| Generezi C06 de la zero | `genereaza C06` | branch `feat/c06-generare` + `c06/` (7 artefacte + assets/) |
| Regenerezi C03 COMPLET de la zero | `regenereaza C03 de la zero` | branch `regen/c03-AAAALLZZ` + `c03/` (cu confirmare) |
| Generezi mai multe construcții odată | `genereaza C06-C08 in serie` | C06, apoi C07, apoi C08 (cu pauze pentru confirmare) |

### Detalii `genereaza CNN`

Motorul face:
1. Rulează `pre_generation_check.py NN` (cele 3 checks HARD):
   - R-V03.55 SPEC CNN înghețat?
   - L142 IDENTITATE_TEHNICA CNN populată?
   - L143 FENOMENE vs asset fizic aliniate?
2. `git checkout -b feat/cNN-generare`
3. Citește `c01/` ca referință (cobai)
4. Aplică COPY+MODIFY pe cele 4 HTML-uri
5. Generează Date_MASTER-CNN.xlsx din `_system/referinte/Date_MASTER-initial.xlsx`
6. Generează FILM-Excel-NN-{slug}.docx (Creativ abandonat V68: prompturile imaginilor le face ARHITECT extern, nu se stochează)
7. Integrează imaginile (hero + 6 exec-stage) primite de la ARHITECT în `cNN/assets/` + base64
8. Scrie totul în `cNN/`
9. Rulează `audit_sync.py` → confirmă zero drift
10. Rulează `gate_v20.py NN cNN c01` → PASS
11. `git add cNN/ && git commit -m "feat(cNN): generare initiala"`
12. Raportează ZERO DRIFT + cele 7 livrabile prezente + branch numele

**Durată estimată:** 3-5 minute pentru o construcție. Push când ARHITECT cere.

### Detalii `regenereaza CNN de la zero`

**Cerere distructivă, dar git ține istoricul complet.** Motorul:
1. Cere confirmare explicită
2. Verifică working tree clean
3. `git checkout -b regen/cNN-AAAALLZZ`
4. `git rm -r cNN/ && git commit -m "chore(cNN): wipe pre-regen"`
5. Aplică flow `genereaza` de la zero pe branch-ul nou
6. Commit final cu noua versiune

**Rollback:** `git checkout main -- cNN/` aduce înapoi versiunea de pe main. Sau `git revert <sha>` post-merge.

Detalii: `05-WORKFLOW-PER-SCENARIU.md` scenariu 5.

---

## Comenzi de editare conținut (în GitHub Desktop + chat)

Modificările de conținut le faci local, le commit-uiești în GitHub Desktop. Chat-ul e doar pentru semnalizare opțională.

### Editezi text în HTML-Studiu sau HTML-Video

1. **GitHub Desktop**: Fetch origin + Pull (asigură-te că ești la zi)
2. Deschide `cNN/HTML-Editor-Studiu-Excel-NN-{slug}.html` în Chrome
3. Click pe text → editezi inline
4. Apasă **💾 EXPORT** (toolbar sus) → primesti fișier descărcat
5. Înlocuiește `cNN/HTML-Studiu-Excel-NN-{slug}.html` cu fișierul descărcat
6. **GitHub Desktop**: detectează modificarea automat → Summary (`docs(cNN): editare X`) → Commit to main → Push origin

Sau, dacă vrei să fac eu commit-ul:
> *„Am modificat `c03/HTML-Studiu-...html` local. Fă commit cu mesaj clar și push."*

### Vrei să-mi semnalizezi că ai modificat ceva

| Scrii în chat | Eu fac |
|---|---|
| `am modificat C03, verifica` | `git diff` + raportez ce e diferit |
| `am modificat C03, aplica audit` | Rulez audit_sync.py → confirm că modificările tale nu sparg sistemul |
| `am modificat C03, commit si push` | `git status` + diff + `git add` + commit cu mesaj clar + push |

---

## Comenzi de upgrade KIT (bug-uri, regule noi)

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Repari un bug peste toate construcțiile | `bug: [descriere]. Aplică pe C01-C06` | Branch `fix/<slug>` + propun fix + scriu patch + aplic batch + audit + commit |
| Adaugi o regulă nouă | `regulă nouă: [descriere]. Codifică ca R-V03.X` | Adaug în 01-REGULI-ACTIVE, scriu detector în audit_sync, aplic retroactiv pe branch dedicat |
| Schimbi setarea vizuală globală | `schimba [X] pe toate HTML-Studiu` | Branch dedicat + patch script + aplicare + audit + commit |
| Verifici sincronizarea după modificări | `verifica sincronizare` | Rulez audit_sync.py → raportez tabel cu drift |

### Exemplu concret: bug fix font buton

> **Tu**: „bug: butonul VERIFICĂ are font 12px pe mobile, ar trebui 14px. Aplică pe C01-C06"

> **Eu**:
> 1. Citesc `c01/HTML-Studiu-Excel-01-Structurare.html` să localizez CSS-ul
> 2. Confirm: „Propun `@media (max-width: 768px) { .step-verify-btn { font-size: 14px; } }`. Aplic pe C01-C06 pe branch `fix/font-buton-responsive`. Confirmi?"
> 3. **Tu**: „da"
> 4. `git checkout -b fix/font-buton-responsive`
> 5. Scriu rețetă patch în `_system/patch_recipes/R-V03.66-font-buton-responsive.yaml`
> 6. Aplic peste `c01/, c02/, ..., c06/`
> 7. Adaug regulă R-V03.66 în 01-REGULI-ACTIVE.md + detector în audit_sync.py
> 8. Audit → zero drift
> 9. `git commit -m "fix(buton): font-size responsive .step-verify-btn"`
> 10. Raportez: „Fix aplicat pe branch fix/font-buton-responsive. Pentru merge: spune-mi `push fix` sau `deschide PR`."

---

## Comenzi de poze (Banana 2)

| Vrei să... | Scrii în chat | Atașez? |
|---|---|---|
| Înlocuiești poza X în C06 | `pentru C06, poza nouă exec-stage-1` + atașezi fișierul (jpg sau png — îl salvez ca jpg) | DA |
| Înlocuiești poză peste toate | `aceasta poză înlocuiește exec-stage-1 la toate` + atașezi | DA |
| Folosești poză care e deja în repo | `pentru C06, refoloseste imaginea curentă din c06/assets/` | NU |

### Detalii

**Asset-uri per construcție:**
Imaginile sunt **diferite per construcție** (V39). Trăiesc în `cNN/assets/exec-stage-1..6.jpg` (3:2 cinematic, V41 eliminat PNG duplicate). Eu le pun acolo, le encodez base64, le inlinuesc în HTML-Video + HTML-Editor-Video, commit cu mesaj `chore(cNN): poza exec-stage-X`.

**Asset-uri brand (toate construcțiile):**
Pentru o imagine brand-wide, branch `chore/brand-exec-stage-X` + aplic în fiecare `cNN/assets/` separat. Merge prin PR (recomandat pentru schimbări brand-wide).

---

## Comenzi de audit și verificare

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Vezi starea generală a sistemului | `status` | Citesc STARE-CURENTA + rulez audit + `git status` + raportez tabel |
| Verifici o construcție specifică | `verifica C03` | Gate v20 + audit individual + raport |
| Vezi diferențele între versiuni | `compara C03 cu versiunea anterioara` | `git log --follow -- c03/` + `git diff <ref>..HEAD -- c03/` |
| Vezi diferențele între 2 construcții | `compara C02 si C03` | Diff structural pe HTML și Date_MASTER (nu git, ci comparație semantică) |
| Vezi istoricul unei construcții | `istoric C03` | `git log --oneline -- c03/` |

---

## Comenzi rare (cu confirmare)

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Migrarea unei construcții la altă schemă | `migreaza C03 la noua schema` | Branch dedicat + cer confirmare + migrare + commit |
| Ștergi o construcție | `sterge C12` | CER CONFIRMARE DUBLĂ + branch `chore/remove-c12` + `git rm -r c12/` + commit |
| Restore o construcție la versiunea veche | `restore C03 la versiunea v40` | `git checkout v40 -- c03/` + commit „revert(c03)" |
| Anulezi un commit recent | `revert ultimul commit` | `git revert HEAD` (creează commit invers, nu modifică istoricul) |

---

## Comenzi de meta-sistem

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Actualizezi documentația sistem | `update sistem cu [nouă lecție / regulă]` | Modific 01-REGULI-ACTIVE + 02-GLOSAR dacă e cazul + commit |
| Adaugi o lecție nouă | `lecție nouă: [descriere]` | Adaug L1X în arhivă cu numerotare continuă + commit |
| Vezi versiunea curentă a sistemului | `ce versiune e?` | V curentă + ultima sesiune + branch curent |
| Pornesc o consolidare brain | `consolideaza brain` | Sumar sesiune + update STARE-CURENTA + `git tag -a v{N}` + push tags |
| Creezi tag manual la V{N} | `tag V41` | `git tag -a v41 -m "..."` + `git push --tags` |

---

## Comenzi de remote git

| Vrei să... | Scrii în chat | Eu fac |
|---|---|---|
| Urci commit-urile locale pe GitHub | `push` sau `push branch-ul curent` | `git push -u origin <branch>` |
| Aduci ultimele modificări de pe GitHub | `pull` | `git pull origin <branch>` |
| Deschizi PR | `deschide PR` sau `creează PR de la X la main` | Push (dacă nu e încă pushat) + creez PR via GitHub API |
| Merge un branch în main | `merge branch X în main` | Pe `main`: `git merge X` + push (recomandat via PR pentru review) |

**Important:** push-urile NU se fac automat. Eu commit local, tu confirmi push când vrei.

---

## Cazul „nu știu ce să-i cer"

Dacă nu știi exact ce comandă, scrie natural ce vrei:

> „vreau să schimb titlul din C03 dar nu știu cum"

Eu te ghidez: deschizi `c03/HTML-Editor-Studiu-...`, click pe titlu, edit, EXPORT, înlocuire, commit în GitHub Desktop.

> „vreau să fac diferit doza între prompturi"

Eu îți explic: e ajustare CSS globală pe `.prompt-box`, pot face patch pe toate (branch dedicat + commit), sau editezi local.

**Nu trebuie să memorezi comenzi.** Scrie natural, eu interpretez și propun comanda exactă.

---

## Sumar cu cele mai folosite 10 comenzi

| # | Comandă | Frecvență estimată |
|---|---|---|
| 1 | `genereaza CNN` | La fiecare construcție nouă |
| 2 | `verifica sincronizare` | După orice modificare semnificativă |
| 3 | `bug: [descriere]. Aplică pe C01-C06` | Săptămânal/lunar |
| 4 | `compara C03 cu versiunea anterioara` | Ad-hoc pentru audit |
| 5 | `status` | Începutul fiecărei sesiuni |
| 6 | `push` | După lucru local |
| 7 | `regula noua: [descriere]` | Lunar |
| 8 | `regenereaza CNN de la zero` | Rar (după SPEC nou) |
| 9 | `consolideaza brain` | La sfârșitul sesiunilor lungi |
| 10 | `pentru CNN poza X` + atașez | La fiecare schimbare vizuală |

---

## Workflow zilnic tipic

**Dimineața:**
> `status`

Eu raportez: versiune curentă, ce construcții sunt sincronizate, audit ZERO DRIFT, branch curent, eventuale TODO-uri.

**Lucrul efectiv:**
- Modificări de conținut local: tu editezi + EXPORT + commit în GitHub Desktop (sau îmi ceri să fac eu commit-ul)
- Modificări sistem: comandă în chat → eu lucrez pe branch dedicat → commit local → tu confirmi push când vrei

**Seara:**
> `consolideaza brain` (dacă a fost sesiune cu multe decizii)

Eu sumarizez + tag git v{N} + push tags.

---

Pentru flux complet pas cu pas pe scenariile reale → `05-WORKFLOW-PER-SCENARIU.md`.

Pentru regulile de versionare git → `CLAUDE.md` secțiunea „VERSIONARE GIT".
