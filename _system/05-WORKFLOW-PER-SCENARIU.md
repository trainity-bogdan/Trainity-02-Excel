# Workflow per scenariu · Pas cu pas (V41)

Cele 5 scenarii reale pe care le vei face zilnic / lunar.

**Versionare:** git (commit + branch + tag) cu remote `github.com/trainity-bogdan/Trainity-02-Excel`. Reguli G1-G5 în `CLAUDE.md` secțiunea „VERSIONARE GIT". Tool oficial pentru ARHITECT: GitHub Desktop pentru sync local; GitHub web UI pentru PR-uri, review, merge.

**Structură construcție:** versiune unică `cNN/` (NU canonic/editat). Vezi `04-ARHITECTURA-LIVRABILE.md`.

---

# SCENARIUL 1 — Prima generare construcție nouă (C06)

**Contextul:** C06 nu există în repo. Vrei să creezi prima ei versiune.

## Pasul 1 — Pregătirea SPEC (în chat BRAIN sau curent)

Înainte de generare, SPEC C06 trebuie să fie ÎNGHEȚAT cu toate cele 9 elemente (în `_system/arhiva/SISTEM_TRAINITY-versiuni.md`):

| Element | Conținut |
|---|---|
| 1. SLUG | „Cifre" sau „KPI" sau „Cantitate" |
| 2. INTRIGA | „Setul are cifre. Excel le știe. Tu nu." |
| 3. PROBLEMELE | Cantitate care vorbește vs cifre incoerente |
| 4. MIZA | Decizii pe cifre care nu reprezintă realitatea |
| 5. MANTRA | „Înainte de raport, cifra exactă" |
| 6. WOW (PAYOFF) | Inventar cantitativ complet |
| 7. MOTTO | „Un set măsurabil. Apoi orice raport." |
| 8. FENOMENE | 5 cantități semnificative (sumă totală, medii pe categorii, top-N, distribuție, Pareto) |
| 9. STEP-TITLES | 18 titluri specifice axei CANTITATIVE (NU clone din C01) |

Procedeul SPEC FREEZING (R-V03.56) cu format grilă A/B/C per element. Confirmare ARHITECT.

În paralel, IDENTITATE_TEHNICA C06 completă în `_system/referinte/IDENTITATE-TEHNICA.md`.

## Pasul 2 — Comanda generare

În chat (oricare cu Claude):

> *„Genereaza C06"*

## Pasul 3 — Ce fac EU automat

1. **Rulez `pre_generation_check.py 06`** (cele 3 checks HARD):
   - R-V03.55 SPEC C06 înghețat?
   - L142 IDENTITATE_TEHNICA C06 populată?
   - L143 FENOMENE vs asset fizic Date_MASTER-initial.xlsx aliniate?
   - Dacă FAIL → te anunț cu eroare clară, OPRESC generarea

2. **Verific working tree clean** (`git status`). Dacă dirty, te întreb dacă commit înainte sau abandonez modificările.

3. **Creez branch dedicat** (G1):
   ```
   git checkout -b feat/c06-generare
   ```

4. **Citesc referința** `c01/`:
   - HTML-Studiu, HTML-Editor-Studiu, HTML-Video, HTML-Editor-Video
   - Tot ca string, voi modifica doar zone narrative

5. **Aplic COPY+MODIFY** pe cele 4 HTML-uri:
   - Înlocuiesc cover-title cu noua axă
   - Înlocuiesc INTRIGA, MIZA, MANTRA, WOW, MOTTO (din SPEC)
   - Înlocuiesc cele 18 step-titles (specifice axei CANTITATIVE)
   - Înlocuiesc prompturile Copilot
   - Înlocuiesc final-text și final-label cu cifrele specifice
   - Imaginile cinematic rămân placeholder din `c01/assets/` (regenerezi cu Banana 2 — scenariul 3)

6. **Generez `Date_MASTER-C06.xlsx`** din `_system/referinte/Date_MASTER-initial.xlsx`

7. **Generez `Creativ-Excel-06-{slug}.txt`** și **`FILM-Excel-06-{slug}.docx`**

8. **Copiez 6 imagini jpg placeholder** din `c01/assets/` în `c06/assets/`

9. **Scriu toate în `c06/`** (un singur folder, fără canonic/editat)

10. **Audit empiric:**
    - `audit_sync.py` → zero drift (8 detectoare × 6 zone = 48 verificări PASS)
    - `gate_v20.py 06 c06 c01` → PASS

11. **Commit (G2):**
    ```
    git add c06/
    git commit -m "feat(c06): generare initiala T2 cantitativ"
    ```

12. **Raportez în chat:**
    > „C06 generată pe branch `feat/c06-generare`. Zero drift. Gate PASS. Imagini placeholder (regenerează cu Banana 2 pentru axa cantitativă — vezi Scenariul 3). Pentru push + PR: spune-mi `push C06` sau `deschide PR pentru C06`."

## Pasul 4 — Ce faci TU

**Decizi când publici:**
- *„push C06"* → eu fac `git push -u origin feat/c06-generare`. Apoi vezi în GitHub Desktop branch-ul nou.
- *„deschide PR pentru C06"* → push + creez PR pe GitHub `feat/c06-generare` → `main`. Tu review-uiezi în UI și faci merge.
- *„merge direct pe main"* → fac `git checkout main && git merge feat/c06-generare` local + push. Fără review formal.

**Verificare locală înainte de merge:** dublu-click pe `c06/HTML-Studiu-Excel-06-{slug}.html` direct din Explorer (după ce GitHub Desktop a făcut pull pe branch). Dacă ceva nu pare bine: *„C06 are problema X"* — eu repar.

**Timp total estimat:** 5-10 min generare + 2-5 verificare + 1 min merge/PR.

---

# SCENARIUL 2 — Bug fix HTML-Studiu propagat peste toate construcțiile

**Contextul:** Observi că pe HTML-Studiu, butonul „VERIFICĂ" are font 12px (prea mic pe mobile). Vrei să fie 14px peste TOATE construcțiile (C01-C06).

## Pasul 1 — Tu raportezi bug-ul în chat

> *„Bug: butonul VERIFICĂ în HTML-Studiu are font 12px pe mobile, ar trebui 14px. Aplică pe C01-C06."*

Opțional, atașezi un screenshot pentru context vizual.

## Pasul 2 — Ce fac EU

1. **Citesc** `c01/HTML-Studiu-Excel-01-Structurare.html`, localizez CSS-ul

2. **Confirm cu tine soluția:**
   > „Propun:
   > - Desktop: `font-size: 13px` (de la 12px)
   > - Mobile (@media max-width 768px): `font-size: 14px`
   > 
   > Aplic pe C01-C06 pe branch `fix/font-buton-verifica-responsive`. Confirmi?"

3. **Tu:** *„da"*

4. **Creez branch dedicat:**
   ```
   git checkout -b fix/font-buton-verifica-responsive
   ```

5. **Scriu patch script** în `_system/patch_recipes/R-V03.66-font-buton-responsive.yaml` (idempotent, anti-double-inject)

6. **Aplic peste toate folderele** (c01-c06)

7. **Rulez audit_sync.py** → confirm zero drift rămas

8. **Adaug regulă nouă** R-V03.66 în `01-REGULI-ACTIVE.md` + detector în `audit_sync.py`

9. **Re-rulez audit** → confirm noul detector PASS pe toate 6 zone

10. **Commit (cu detalii în body):**
    ```
    git commit -m "fix(buton): font-size 13/14px desktop/mobile pe .step-verify-btn

    Regula nouă R-V03.66 + detector audit_sync.
    Aplicat pe C01-C06. Rețetă patch în _system/patch_recipes/."
    ```

11. **Raportez:**
    > „Fix aplicat pe branch `fix/font-buton-verifica-responsive`. Regula R-V03.66 codificată. Audit PASS pe toate cele 6 zone. Pentru merge: spune-mi `push fix` sau `deschide PR`."

## Pasul 3 — Ce faci TU

Decizi cum mergi: push + PR (recomandat pentru schimbări sistemice), sau merge direct pe main. Rollback: `git revert <sha>` dacă observi probleme post-merge.

---

# SCENARIUL 3 — Imagine nouă cu Banana 2 pentru C06

**Contextul:** Pentru C06, vrei poza exec-stage-1 să fie un grafic specific cantitativ, nu placeholder-ul.

## Variant A — Atașezi pozele în chat

> *„Pentru C06, poza nouă exec-stage-1: [atașat exec-stage-1-c06.jpg]. Aplică în HTML-Video."*

## Variant B — Pozele sunt deja pe disk local

Tu le-ai salvat manual în `c06/assets/exec-stage-1.jpg` și commit-uit. Apoi:

> *„Pentru C06, exec-stage-1 e schimbat în assets/. Reaplică base64 în HTML-Video."*

## Pasul 1 — Ce fac EU

1. **Salvez pozele** (dacă atașate) în `c06/assets/exec-stage-1.{jpg,png}`

2. **Encode base64** pozele

3. **Localizez în `c06/HTML-Video-Excel-06-{slug}.html`** secțiunea exec-stage-1 și înlocuiesc base64-ul vechi (în HTML-Video + HTML-Editor-Video)

4. **Commit:**
   ```
   git add c06/
   git commit -m "chore(c06): poza exec-stage-1 actualizată (Banana 2)"
   ```

5. **Raportez:**
   > „C06 exec-stage-1 actualizat. assets/ + HTML-Video + HTML-Editor-Video sincronizate. Commit local. Push când vrei."

## Caz special — poză aplicată la TOATE construcțiile (brand)

> *„Aceasta poză înlocuiește exec-stage-final la TOATE construcțiile"*

Eu:
1. **Confirm impact pe toate**
2. Creez branch `chore/brand-exec-stage-final`
3. Pentru fiecare cNN/: salvez în `cNN/assets/exec-stage-final.{jpg,png}` + re-encode base64
4. Audit → confirm PASS
5. Commit + raportez. Pentru merge: PR pe GitHub (recomandat pentru schimbare brand-wide).

---

# SCENARIUL 4 — Editezi tu HTML-Studiu local

**Contextul:** La C03, vrei să modifici niște text în step-action 5.

## Pasul 1 — Pull local înainte de editare

În **GitHub Desktop**:
1. Verifică branch curent (default `main`)
2. Apasă **Fetch origin** (sus dreapta) → trage ultimele schimbări
3. Dacă există modificări remote, apasă **Pull origin**

## Pasul 2 — Editare locală

1. Deschide Explorer la calea clonei locale a repo-ului
2. **Dublu-click** pe `c03/HTML-Editor-Studiu-Excel-03-Auditare.html` → se deschide în Chrome
3. **Click pe textul** pe care vrei să-l modifici (step-action 5) → cursorul intră în mod edit → tastezi
4. **Apasă butonul** 💾 **EXPORT** sus → primesti în Downloads: `HTML-Studiu-Excel-03-Auditare-Editat.html`
5. **Înlocuiește** fișierul: redenumește la `HTML-Studiu-Excel-03-Auditare.html` și mut în `c03/` (suprascrie cel existent)

## Pasul 3 — Commit + push în GitHub Desktop

GitHub Desktop detectează automat modificarea în `c03/HTML-Studiu-Excel-03-Auditare.html`:

1. **Stânga jos**: vezi „Summary" → scrii `docs(c03): editare step-action 5 frazare`
2. **Apasă** „Commit to main" (sau crează branch dedicat dacă e schimbare semnificativă)
3. **Push origin** (buton sus dreapta)

Sau alternativ, în chat:
> *„Am modificat C03 local și am pus în c03/. Verifică, fă commit cu mesaj clar și push."*

Eu fac `git status` + diff + commit + push.

## Pasul 4 — Dacă vrei să vezi ce ai modificat vs versiunea veche

În chat:
> *„Verifică ce am modificat la C03 vs versiunea de săptămâna trecută"*

Eu:
1. `git log --follow --oneline -- c03/HTML-Studiu-Excel-03-Auditare.html` → arăt commit-urile relevante
2. Te las să alegi commit-ul referință (sau folosesc HEAD~5 sau tag-ul `v40` automat)
3. `git diff <ref>..HEAD -- c03/HTML-Studiu-Excel-03-Auditare.html`
4. Raportez: *„Ai modificat la step-action 5 — 2 fraze. Înainte: '...'. Acum: '...'. Restul identic."*

---

# SCENARIUL 5 — Refacere completă a unei construcții după SPEC schimbat

**Contextul:** După 2 luni, decizi că C03 AUDITAREA trebuie să fie complet altfel. Schimbi SPEC-ul, vrei să regenerez de la zero.

## Pasul 1 — Înghețezi SPEC nou

Procedeul SPEC FREEZING normal cu grilă A/B/C. La final, SPEC e înghețat în `_system/arhiva/SISTEM_TRAINITY-versiuni.md` + IDENTITATE_TEHNICA C03 update.

## Pasul 2 — Comanda refacere

> *„Regenereaza C03 de la zero cu noul SPEC."*

## Pasul 3 — Ce fac EU

1. **CER CONFIRMARE EXPLICITĂ** (cerere distructivă):
   > „Atenție: voi suprascrie `c03/` complet pe branch `regen/c03-AAAALLZZ`. Versiunea curentă rămâne în git history pe `main` — accesibilă oricând via `git checkout main -- c03/`. Confirmi regenerarea? (da/nu)"

2. **Tu:** *„da"*

3. **Pași efectivi:**
   - `git checkout -b regen/c03-AAAALLZZ`
   - `git rm -r c03/ && git commit -m "chore(c03): wipe pre-regen"`
   - Aplic flow `genereaza_constructie` din scenariul 1
   - `git add c03/ && git commit -m "feat(c03): regenerare de la zero cu noul SPEC"`
   - Audit empiric → confirm zero drift
   - Gate v20 PASS

4. **Raportez:**
   > „C03 regenerat cu noul SPEC pe branch `regen/c03-AAAALLZZ`. Versiunea anterioară accesibilă via `git log` sau `git show <sha>:c03/...`. Pentru rollback la versiunea veche: `git checkout main -- c03/`. Push când vrei + PR recomandat."

## Pasul 4 — Ce vezi TU

În GitHub Desktop după Fetch origin:
- Branch `regen/c03-AAAALLZZ` nou cu c03/ regenerat
- Branch `main` cu versiunea veche intactă

Compari side-by-side în UI înainte de merge.

## Pasul 5 — Dacă vrei să te întorci la versiunea veche

> *„Reverteaza C03 la versiunea din `main`"*

Eu:
1. Pe branch curent: `git checkout main -- c03/`
2. Commit „revert(c03): rollback la versiunea pre-regen"
3. Audit → confirm

Sau, dacă regen-ul a ajuns deja pe main și vrei rollback: `git revert <sha-regen-merge>`.

---

# Sumar fluxuri

| Scenariu | Cine inițiază | Eu | Tu | Branch dedicat | Timp estimat |
|---|---|---|---|---|---|
| 1. Generare CNN | Tu (comandă) | Generez, audit, commit | Push/PR/merge | Da (`feat/cNN-generare`) | 5-10 min |
| 2. Bug fix global | Tu (comandă) | Patch, audit, commit | Push/PR/merge | Da (`fix/<slug>`) | 10-20 min |
| 3. Imagine nouă (1 cNN) | Tu (comandă + atașez) | Encode, înlocuiesc, commit | Push | Nu (commit direct pe branch curent) | 5-10 min |
| 3b. Imagine brand (toate) | Tu (comandă + atașez) | Encode, înlocuiesc, commit | Push/PR/merge | Da (`chore/brand-*`) | 15-30 min |
| 4. Editare locală | Tu (local + GitHub Desktop) | Pasiv (sau audit la cerere) | Editare + Export + commit + push în GitHub Desktop | Decizi tu | 5-30 min |
| 5. Regenerare CNN | Tu (comandă) | Wipe + regenerez, audit, commit | Push/PR/merge | Da (`regen/cNN-AAAALLZZ`) | 10-20 min |

**Tool oficial pentru ARHITECT:** GitHub Desktop pentru sync local + GitHub web UI pentru PR-uri/review/merge.

**Singura excepție atașare în chat:** scenariul 3 (imagini Banana) când pozele NU sunt deja pe disk.

---

Pentru lista completă a comenzilor pe care le poți da → `03-COMENZI-OPERATIONALE.md`.

Pentru detalii versionare git → `CLAUDE.md` secțiunea „VERSIONARE GIT".
