# Workflow per scenariu · Pas cu pas (V40)

Cele 5 scenarii reale pe care le vei face zilnic / lunar.

**Versionare:** OneDrive auto-sync + Version History per fișier + backup/snapshot discipline (regulile V1/V2/V3 din CLAUDE.md). **NU Git, NU GitHub Desktop.**

**Structură construcție:** versiune unică `cNN/` (NU canonic/editat). Vezi `04-ARHITECTURA-LIVRABILE.md`.

---

# SCENARIUL 1 — Prima generare construcție nouă (C06)

**Contextul:** C06 nu există în repo. Vrei să creezi prima ei versiune.

## Pasul 1 — Pregătirea SPEC (în chat BRAIN sau curent)

Înainte de generare, SPEC C06 trebuie să fie ÎNGHEȚAT cu toate cele 9 elemente (în `_system/arhiva/SISTEM_TRAINITY-versiuni.md`):

| Element | Conținut |
|---|---|
| 1. SLUG | "Cifre" sau "KPI" sau "Cantitate" |
| 2. INTRIGA | "Setul are cifre. Excel le știe. Tu nu." |
| 3. PROBLEMELE | Cantitate care vorbește vs cifre incoerente |
| 4. MIZA | Decizii pe cifre care nu reprezintă realitatea |
| 5. MANTRA | "Înainte de raport, cifra exactă" |
| 6. WOW (PAYOFF) | Inventar cantitativ complet |
| 7. MOTTO | "Un set măsurabil. Apoi orice raport." |
| 8. FENOMENE | 5 cantități semnificative (sumă totală, medii pe categorii, top-N, distribuție, Pareto) |
| 9. STEP-TITLES | 18 titluri specifice axei CANTITATIVE (NU clone din C01) |

Procedeul SPEC FREEZING (R-V03.56) cu format grilă A/B/C per element. Confirmare ARHITECT.

În paralel, IDENTITATE_TEHNICA C06 completă în `_system/referinte/IDENTITATE-TEHNICA.md`.

## Pasul 2 — Comanda generare

În chat (oricare cu Claude):

> *"Genereaza C06"*

## Pasul 3 — Ce fac EU automat

1. **Rulez `pre_generation_check.py 06`** (cele 3 checks HARD):
   - R-V03.55 SPEC C06 înghețat?
   - L142 IDENTITATE_TEHNICA C06 populată?
   - L143 FENOMENE vs asset fizic Date_MASTER-initial.xlsx aliniate?
   - Dacă FAIL → te anunț cu eroare clară, OPRESC generarea

2. **Citesc matrița** `_template/`:
   - HTML-Studiu, HTML-Editor-Studiu, HTML-Video, HTML-Editor-Video
   - Tot ca string, voi modifica doar zone narrative

3. **Aplic COPY+MODIFY** pe cele 4 HTML-uri:
   - Înlocuiesc cover-title cu noua axă
   - Înlocuiesc INTRIGA, MIZA, MANTRA, WOW, MOTTO (din SPEC)
   - Înlocuiesc cele 18 step-titles (specifice axei CANTITATIVE)
   - Înlocuiesc prompturile Copilot (Prompt 1 audit, Prompt 2 transformare)
   - Înlocuiesc final-text și final-label cu cifrele specifice
   - Înlocuiesc imaginile cinematic dacă sunt diferite (rar — de obicei placeholder din _template, regenerezi ulterior cu Banana 2)

4. **Generez `Date_MASTER-C06.xlsx`** din `_system/referinte/Date_MASTER-initial.xlsx`:
   - Sheet input cu fenomene cantitative
   - Sheet output cu inventar cantitativ
   - Sumă conservată cu predecesoarea (C05)

5. **Generez `Creativ-Excel-06-{slug}.txt`** și **`FILM-Excel-06-{slug}.docx`**

6. **Copiez 12 imagini placeholder** din `_template/assets/` în `c06/assets/` (le vei regenera ulterior cu Banana 2 specifice axei)

7. **Scriu toate în `c06/`** (un singur folder, fără canonic/editat)

8. **Audit empiric:**
   - Rulez `audit_sync.py` → confirm zero drift (8 reguli × 6 zone = 48 verificări PASS)
   - Rulez `gate_v20.py 06 c06 _template` → PASS pe 6 clase

9. **Raportez în chat:**
   > "C06 generată cu zero drift. Cele 7 artefacte + 12 imagini placeholder prezente. Gate v20 PASS. OneDrive sync în background. Imaginile sunt placeholder din pilot; regenerează cu Banana 2 pentru axa cantitativă (vezi Scenariul 3)."

## Pasul 4 — Ce faci TU

**Nimic activ.** Fișierele apar în OneDrive sync (vezi iconița OneDrive în system tray devine bifă verde când e sync). 

**Verifică deschizând** `c06/HTML-Studiu-Excel-06-{slug}.html` direct (dublu-click în Explorer sau eu îți deschid cu `start`). Dacă ceva nu pare bine, scrii: *"C06 are problema X"* — eu o repar fie prin patch, fie prin regenerare punctuală (cu backup auto pre-distructiv).

**Timp total estimat:** 5-10 minute (3-5 generare + 2-5 verificare).

---

# SCENARIUL 2 — Bug fix HTML-Studiu propagat peste toate construcțiile

**Contextul:** Observi că pe HTML-Studiu, butonul "VERIFICĂ" are font 12px (prea mic pe mobile). Vrei să fie 14px peste TOATE construcțiile (C01-C06).

## Pasul 1 — Tu raportezi bug-ul în chat

> *"Bug: butonul VERIFICĂ în HTML-Studiu are font 12px pe mobile, ar trebui 14px. Aplică pe C01-C06."*

Opțional, atașezi un screenshot pentru context vizual.

## Pasul 2 — Ce fac EU

1. **Citesc** `c01/HTML-Studiu-Excel-01-Structura.html`, localizez CSS-ul:
   ```css
   .step-verify-btn {
     ...
     font-size: 12px;
   }
   ```

2. **Confirm cu tine soluția:**
   > "Propun:
   > - Desktop: `font-size: 13px` (de la 12px, pentru lizibilitate)
   > - Mobile (@media max-width 768px): `font-size: 14px`
   > 
   > Aplic pe C01-C06. Patch atinge >3 fișiere — creez BACKUP AUTO (regula V1) `cNN_BACKUP_AAAALLZZ_pre-fix/` pentru fiecare construcție afectată. Confirmi?"

3. **Tu:** *"da"*

4. **BACKUP AUTO**: copiez `c01/`, `c02/`, ..., `c06/` → `c0N_BACKUP_AAAALLZZ_pre-fix/` (regula V1)

5. **Scriu patch script** în `_system/patch_recipes/R-V03.66-font-buton-responsive.yaml`:
   - Regex pe regula `.step-verify-btn { ... font-size: 12px ... }`
   - Idempotent: re-rularea NU strică nimic, recunoaște ce e deja patch-uit
   - Anti-duble-inject: nu adaugă @media de două ori

6. **Aplic peste toate folderele:**
   - `c01/HTML-Studiu-...html` + `HTML-Editor-Studiu-...html`
   - `c02/...` similar
   - ... până la `c06/...`

7. **Rulez audit_sync.py** → confirm zero drift rămas

8. **Adaug regulă nouă** R-V03.66 în `01-REGULI-ACTIVE.md`:
   ```
   ## R-V03.66 · FONT BUTON VERIFICĂ RESPONSIVE
   Status: ACTIVĂ (V40+)
   Buton .step-verify-btn: 13px desktop, 14px mobile.
   Detector empiric: regex pe @media max-width 768px cu .step-verify-btn font-size: 14px
   ```

9. **Adaug detector** în `audit_sync.py`:
   ```python
   @detector('R-V03.66', 'Font buton VERIFICĂ responsive', 'studiu')
   def _r0366(c):
       return '.step-verify-btn' in c and 'font-size: 14px' in c
   ```

10. **Re-rulez audit** → confirm noul detector PASS pe toate 6 zone

11. **Raportez:**
    > "Fix aplicat pe C01-C06. Audit PASS pe noua regulă R-V03.66. Backup-uri salvate la cNN_BACKUP_AAAALLZZ_pre-fix/. OneDrive sync în background. Dacă vrei rollback: ștergi cNN/ și redenumești backup-ul."

## Pasul 3 — Ce faci TU

Nimic activ. OneDrive sync-uiește automat. Verifici un fișier deschizând în browser dacă vrei să confirmi vizual.

---

# SCENARIUL 3 — Imagine nouă cu Banana 2 pentru C06

**Contextul:** Pentru C06 (axa CANTITATIVĂ), vrei poza exec-stage-1 să fie un grafic specific cantitativ, nu poza placeholder.

## Variant A — Atașezi pozele

În chat:

> *"Pentru C06, poza nouă exec-stage-1: [atașat exec-stage-1-c06.jpg + exec-stage-1-c06.png]. Aplică în HTML-Video."*

## Variant B — Pozele sunt deja pe disk

Tu salvezi manual pozele în `c06/assets/exec-stage-1.{jpg,png}` (suprascrii placeholderul). OneDrive sync automat. Apoi în chat:

> *"Pentru C06, exec-stage-1 e schimbat în assets/. Reaplică base64 în HTML-Video."*

## Pasul 1 — Ce fac EU

1. **Salvez pozele** (dacă atașate) în `c06/assets/exec-stage-1.{jpg,png}` (suprascrie placeholderul)

2. **Encode base64** pozele

3. **Localizez în `c06/HTML-Video-Excel-06-{slug}.html`** secțiunea Executive Show — exec-stage-1:
   ```html
   <img src="data:image/jpeg;base64,/9j/4AAQ..." class="exec-stage-img" data-stage="1">
   ```

4. **Înlocuiesc base64-ul** vechi cu noul (în HTML-Video + HTML-Editor-Video)

5. **Audit + raport:**
   > "C06 exec-stage-1 actualizat. assets/ + HTML-Video + HTML-Editor-Video sincronizate. OneDrive sync în background."

## Caz special — poză aplicată la TOATE construcțiile

Dacă noua imagine e brand (de ex. logo nou pentru slide finală):

> *"Aceasta poză înlocuiește exec-stage-final la TOATE construcțiile"*

Eu:
1. **Confirm impact pe toate** (atinge >3 fișiere — BACKUP AUTO regula V1)
2. Copy `c01/, c02/, ..., cN/` → `c0N_BACKUP_AAAALLZZ_pre-brand-update/`
3. Pentru fiecare cNN/: salvez în `cNN/assets/exec-stage-final.{jpg,png}` + re-encode base64 în HTML-Video + HTML-Editor-Video
4. Audit → confirm PASS
5. Raportez: "Imagine brand exec-stage-final actualizată în toate construcțiile. Backup-uri salvate. OneDrive sync."

---

# SCENARIUL 4 — Editezi tu HTML-Studiu local

**Contextul:** La C03, vrei să modifici niște text în step-action 5 (corectare frazare).

## Pasul 1 — Editare locală

1. Deschide **Windows Explorer**:
   `D:\Desktop\___TRAINITY\__Cloud\OneDrive\__TRAINITY\____CONSTRUCTII Trainity\02 Excel\c03\`

2. **Dublu-click** pe `HTML-Editor-Studiu-Excel-03-Auditare.html` → se deschide în Chrome

3. **Click pe textul** pe care vrei să-l modifici (în step-action 5) → cursorul intră în mod edit → tastezi noul text

4. **Apasă butonul** 💾 **EXPORT** sus → primesti în Downloads:
   `HTML-Studiu-Excel-03-Auditare-Editat.html`

5. **Înlocuiește** fișierul:
   - Mergi în Downloads
   - Redenumește `HTML-Studiu-Excel-03-Auditare-Editat.html` → `HTML-Studiu-Excel-03-Auditare.html`
   - Mut în `c03\` (suprascrie cel existent — OneDrive captează versiunea veche în Version History automat)

## Pasul 2 — Salvare

**Nimic explicit.** OneDrive sync-uiește automat în câteva secunde. Vezi iconița OneDrive în system tray.

**Version History capturează modificarea** — pentru rollback: drept-click pe fișier → Version History → alegi versiunea anterioară.

## Pasul 3 — Ce fac EU

**Nimic activ.** Modificările tale sunt pe disk. Le văd când le voi consulta în următoarea sesiune.

Dacă ulterior îmi ceri:

> *"Verifică ce am modificat la C03 vs versiunea de săptămâna trecută"*

Eu:
1. Citesc `c03/HTML-Studiu-Excel-03-Auditare.html` (versiunea actuală)
2. Te rog să deschizi OneDrive Version History pentru fișier și să-mi spui aproximativ care versiune e cea veche (sau o restorezi temporar în alt nume ca `HTML-Studiu-C03_OLD.html`)
3. Diff
4. Raportez: *"Ai modificat la step-action 5 — 2 fraze. Înainte: '...'. Acum: '...'. Restul identic."*

---

# SCENARIUL 5 — Refacere completă a unei construcții după SPEC schimbat

**Contextul:** După 2 luni, decizi că C03 AUDITAREA trebuie să fie complet altfel. Schimbi SPEC-ul, vrei să regenerez de la zero.

## Pasul 1 — Înghețezi SPEC nou

În chat:

> *"Pentru C03, propun SPEC nou. Axa rămâne AUDIT, dar fenomenele se concentrează pe AUDIT VALORIC (nu structural):
> - INTRIGA: 'Suma e corectă. Componentele mint.'
> - MIZA: ...
> - FENOMENE: 5 fenomene valorice (rotunjiri, TVA inconsistent, calcule eronate, conversii valutare, marje negative)
> - ..."*

Procedeul SPEC FREEZING normal cu grilă A/B/C. La final, SPEC e înghețat în `_system/arhiva/SISTEM_TRAINITY-versiuni.md` + IDENTITATE_TEHNICA C03 update în `_system/referinte/IDENTITATE-TEHNICA.md`.

## Pasul 2 — Comanda refacere

> *"Regenereaza C03 de la zero cu noul SPEC."*

## Pasul 3 — Ce fac EU

1. **CER CONFIRMARE EXPLICITĂ** (cerere distructivă):
   > "Atenție: voi suprascrie `c03/` complet. Creez BACKUP AUTO (regula V1):
   > - `c03_BACKUP_AAAALLZZ_pre-regen/` cu starea curentă (poți recupera oricând)
   > 
   > Confirmi regenerarea? (da/nu)"

2. **Tu:** *"da"*

3. **Pași efectivi:**
   - Copiez `c03/` → `c03_BACKUP_AAAALLZZ_pre-regen/` (BACKUP AUTO)
   - Șterg `c03/`
   - Aplic flow `genereaza_constructie` din scenariul 1
   - Audit empiric → confirm zero drift
   - Gate v20 PASS

4. **Raportez:**
   > "C03 regenerat cu noul SPEC. Backup la c03_BACKUP_AAAALLZZ_pre-regen/ (poți recupera oricând ștergând c03/ + redenumind backup-ul). OneDrive sync în background."

## Pasul 4 — Ce vezi TU

Pe disc local (OneDrive sync):
```
c03/                                  ← C03 nou (cu SPEC actualizat)
c03_BACKUP_AAAALLZZ_pre-regen/        ← vechiul C03, păstrat ca backup local
```

OneDrive sync-uiește ambele în cloud. Backup-ul rămâne acolo până când îl ștergi manual (sau decizi că nu mai ai nevoie).

## Pasul 5 — Dacă vrei să te întorci la versiunea veche

> *"Reverteaza C03 la versiunea din backup"*

Eu:
1. Ștergi `c03/` (versiunea nouă)
2. Redenumesc `c03_BACKUP_AAAALLZZ_pre-regen/` → `c03/`
3. Audit → confirm

Sau alternativ: dacă a trecut mai mult timp și ai pierdut backup-ul local, dar ai sync-uit cloud, deschizi OneDrive web → restore folder din Recycle Bin sau "Restore your OneDrive" (vezi CLAUDE.md secțiunea VERSIONARE).

---

# Sumar fluxuri

| Scenariu | Cine inițiază | Eu | Tu | Backup auto | Timp estimat |
|---|---|---|---|---|---|
| 1. Generare CNN | Tu (comandă) | Generez, audit | Nimic (verifică opțional) | Nu (nu suprascrie) | 5-10 min |
| 2. Bug fix global | Tu (comandă) | Patch, backup, audit | Nimic | Da (>3 fișiere) | 10-20 min |
| 3. Imagine nouă (1 cNN) | Tu (comandă + atașez) | Encode, înlocuiesc | Nimic | Nu (1 cNN) | 5-10 min |
| 3b. Imagine brand (toate) | Tu (comandă + atașez) | Backup, encode, înlocuiesc | Nimic | Da | 15-30 min |
| 4. Editare locală | Tu (local) | Nimic (pasiv) | Editare + EXPORT + suprascriu | Nu (OneDrive Version History per fișier acoperă) | 5-30 min |
| 5. Regenerare CNN | Tu (comandă) | Backup, regenerez, audit | Nimic | Da | 10-20 min |

**Nicio comandă nu necesită setup remote** (Git/GitHub Desktop nu sunt folosite). 

**Singura excepție atașare:** scenariul 3 (imagini Banana) când pozele NU sunt deja pe disk.

---

Pentru lista completă a comenzilor pe care le poți da → `03-COMENZI-OPERATIONALE.md`.

Pentru detalii backup și versionare → `CLAUDE.md` secțiunea "VERSIONARE ONEDRIVE + BACKUP DISCIPLINE".
