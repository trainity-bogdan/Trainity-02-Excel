# SETUP GITHUB — pas cu pas, fără jargon

Acest ghid te duce de la zero la repo funcțional în 30-45 minute. Niciun pas nu necesită comenzi în terminal.

## Înainte să începi

Ai nevoie de:
- O adresă de email (pentru cont GitHub)
- Browser (Chrome, Firefox, Edge)
- ~500 MB liber pe disc

Nu ai nevoie de:
- Cunoștințe Git
- Cunoștințe linie de comandă
- Cunoștințe programare

---

## PASUL 1 — Cont GitHub (5 minute)

1. Mergi la [github.com](https://github.com)
2. Click pe **"Sign up"** (dreapta sus)
3. Introduce email + parolă + username (poate fi `bogdan-tarla` sau ce vrei)
4. Verifică email-ul → click pe link-ul de confirmare
5. La întrebarea "free or pro?" → alege **Free** (suficient pentru ce vrei)

**Gata.** Acum ai cont GitHub.

---

## PASUL 2 — Instalează GitHub Desktop (5 minute)

GitHub Desktop e o aplicație cu butoane, simplă ca Dropbox.

1. Mergi la [desktop.github.com](https://desktop.github.com)
2. Click pe **"Download for Windows"** (sau Mac)
3. Instalează fișierul descărcat (Next → Next → Finish)
4. Deschide GitHub Desktop
5. Click pe **"Sign in to GitHub.com"** → introduce username + parolă

**Gata.** Acum GitHub Desktop e conectat la contul tău.

---

## PASUL 3 — Creează repository (3 minute)

Repository = folder online + folder local sincronizate.

1. În GitHub Desktop, click pe **"File"** → **"New repository"**
2. Completează:
   - **Name**: `trainity-pack-02-excel`
   - **Description**: `Sistem de constructii educationale Excel · Trainity`
   - **Local path**: alege un loc pe calculator (ex: `C:\Users\Bogdan\Documents\`)
   - **Initialize with README**: BIFEAZĂ (nu lasa nebifat)
   - **Git ignore**: lasa "None"
   - **License**: lasa "None"
3. Click pe **"Create repository"**
4. Click pe **"Publish repository"** (buton albastru sus)
5. **DEBIFEAZĂ** "Keep this code private" → vrei să rămână privat? **MEȚINE BIFAT** (privat = doar tu vezi)
6. Click **"Publish repository"**

**Gata.** Acum ai un folder `trainity-pack-02-excel` pe calculator și pe github.com.

Verifică: deschide [github.com](https://github.com) → ar trebui să vezi repo-ul tău în listă.

---

## PASUL 4 — Import structură inițială (10 minute)

Eu am pregătit toată structura cu C01-C05, sistem complet, scripturi, totul. Trebuie doar să o copiezi.

1. **Descarcă** `trainity-repo-import.zip` (link de la Claude)
2. **Dezarhivează** undeva temporar (ex: `Downloads\trainity-import\`)
3. **Deschide** Windows Explorer la 2 ferestre:
   - **Stânga**: `Downloads\trainity-import\trainity-repo\` (conținutul dezarhivat)
   - **Dreapta**: `C:\Users\Bogdan\Documents\trainity-pack-02-excel\` (repo-ul tău local)
4. **Selectează tot** din stânga (Ctrl+A) și **mută în dreapta** (drag & drop sau Ctrl+X / Ctrl+V)
5. Confirmă **"Replace files in the destination"** când întreabă (suprascrie README.md inițial)

În dreapta ar trebui să vezi acum:
```
_system/
c01/
c02/
c03/
c04/
c05/
README.md
.gitignore
GHID-SETUP-GITHUB.md  ← acest fișier
```

---

## PASUL 5 — Primul commit (5 minute)

Commit = "salvează acum și ține minte ce s-a schimbat".

1. Deschide **GitHub Desktop**
2. Pe stânga, ar trebui să vezi o listă lungă cu zeci de fișiere bifate — astea sunt toate fișierele importate
3. Jos-stânga, completează:
   - **Summary**: `Import initial V38 - sistem complet T1`
   - **Description**: (poți lăsa gol)
4. Click pe **"Commit to main"** (buton albastru jos)
5. Sus, click pe **"Push origin"** (buton albastru)

Așteaptă 2-3 minute (urcă toate fișierele pe GitHub).

**Gata.** Acum repo-ul tău online conține tot sistemul.

Verifică: deschide github.com → click pe repo → ar trebui să vezi structura completă.

---

## PASUL 6 — Conectare Claude la GitHub (2 minute)

Asta îmi dă mie acces să citesc și scriu direct în repo, fără să-mi atașezi arhive.

1. În orice chat cu mine, scrie: **"conecteaza GitHub"**
2. Eu îți voi cere autorizare prin connector — vei vedea un buton "Connect"
3. Click pe **"Connect"** → te trimite la github.com → click pe **"Authorize Anthropic"**
4. Revii la chat → eu confirm "conectat"

**Gata.** Acum eu pot:
- Citi orice fișier din repo
- Scrie/modifica fișiere prin commit
- Vedea istoricul
- Aplica patch-uri batch peste toate construcțiile

---

## CUM FOLOSEȘTI ZILNIC

### A. Vrei să editezi C03

1. Deschide Windows Explorer → `Documents\trainity-pack-02-excel\c03\editat\`
2. Dublu-click pe `HTML-Editor-Studiu-Excel-03-Auditare.html` → se deschide în browser
3. Editează ca de obicei
4. Apasă EXPORT → primesti fișier descărcat
5. Înlocuiește `c03\editat\HTML-Studiu-Excel-03-Auditare.html` cu fișierul descărcat
6. Deschide **GitHub Desktop** → ar trebui să vezi modificarea în stânga
7. Scrie în "Summary": `C03 editat - revizuit step-action stage 2`
8. Click **"Commit to main"** → click **"Push origin"**

**Gata.** Modificarea ta e salvată cu istorie și sincronizată.

### B. Vrei să generez C06

1. În orice chat cu mine, scrie: **"genereaza C06"**
2. Eu citesc starea actuală din repo prin connector
3. Generez cele 7 artefacte + scriu în `c06/canonic/` și `c06/editat/`
4. Fac commit cu mesaj clar
5. În GitHub Desktop, click pe **"Fetch origin"** → click **"Pull"** → primești fișierele noi local

**Gata.** Ai C06 generat cu sincronizare automată.

### C. Eu fac upgrade KIT (de exemplu R-V03.65 buton nou)

1. Spui: **"vreau buton X pe HTML-Studiu peste toate construcțiile"**
2. Eu scriu scriptul de patch
3. Rulez patch peste `c02/editat/`, `c03/editat/`, `c04/editat/`, `c05/editat/`
4. Rulez `audit_sync.py` → confirm zero drift
5. Commit unic cu mesaj clar: `Buton X aplicat pe editat C02-C05 (R-V03.65)`
6. În GitHub Desktop, click **"Fetch"** → **"Pull"** → primești toate modificările

Modificările tale de conținut **NU SE PIERD** — patch-ul țintește doar zona specifică.

---

## CELE 3 BUTOANE PE CARE TREBUIE SĂ LE ȘTII

În GitHub Desktop:

| Buton | Ce face |
|---|---|
| **Fetch / Pull** | Descarcă modificările făcute de mine sau de pe alt calculator |
| **Commit to main** | Salvează modificările tale cu mesaj |
| **Push origin** | Urcă modificările tale pe GitHub (după Commit) |

**Atât.** Nu trebuie să înveți altceva.

---

## PROBLEME COMUNE ȘI CUM LE REZOLVI

### "GitHub Desktop nu vede modificările mele"

- Verifică că ai salvat fișierul (Ctrl+S în browser după EXPORT)
- Click pe **"View"** → **"Show Changes in Status Bar"** → vezi imediat ce s-a modificat

### "Nu pot face Push - error"

- Click pe **"Fetch origin"** întâi → apoi **"Pull"** → apoi **"Push"**
- Asta se întâmplă când eu am făcut modificări între timp

### "Am modificat ceva și vreau să revin"

- Click pe **"History"** (tab sus) → găsește commit-ul vechi → click **"Revert"**

### "Vreau să încerc o variantă fără să afectez ce am acum"

- Click pe **"Branch"** → **"New branch"** → dă un nume (ex: `experiment-1`) → lucrezi acolo
- Când termini, ori faci merge la `main`, ori îl ștergi

---

## DUPĂ SETUP

Spune-mi în chat: **"setup terminat"** → eu fac audit-ul prin connector și confirm că totul e OK.

De acum încolo, nu mai e nevoie să-mi atașezi arhive niciodată. Eu citesc direct din repo.
