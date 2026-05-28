# Arhitectura livrabilelor Trainity

Schema canonică a artefactelor per construcție. Sursă: R-V03.47 + R-V03.58 + R-V39.assets.

**Versiune doc: V40 (28 mai 2026)** — actualizat la colapsul canonic/editat (V39).

---

## Cele 7 artefacte canonice per construcție

Fiecare folder `cNN/` conține următoarele 7 fișiere + folderul `assets/`:

| # | Fișier | Rol funcțional | Format |
|---|---|---|---|
| 1 | `HTML-Studiu-Excel-NN-{slug}.html` | Modul studiu interactiv — flow procedural cu 18 step-actions, prompturi Copilot, verificări finale | HTML self-contained ~80KB |
| 2 | `HTML-Editor-Studiu-Excel-NN-{slug}.html` | Variantă editabilă a modulului studiu — toolbar EXPORT + contenteditable | HTML self-contained ~90KB |
| 3 | `HTML-Video-Excel-NN-{slug}.html` | Film cinematic — 6 etape, prompturi, slide-uri, imagini base64 inline | HTML self-contained ~800KB |
| 4 | `HTML-Editor-Video-Excel-NN-{slug}.html` | Variantă editabilă a filmului — toolbar EXPORT | HTML self-contained ~810KB |
| 5 | `Date_MASTER-CNN.xlsx` | Fișier Excel unificat — sheet-uri input (cu fenomene) + output (curățate) + dicționar | XLSX |
| 6 | `Creativ-Excel-NN-{slug}.txt` | Narativa creativă a construcției — voce trainer, identitate cinematică | TXT |
| 7 | `FILM-Excel-NN-{slug}.docx` | Script video procedural cinematic ~150 paragrafe pentru OBS recording | DOCX |

Plus folderul `cNN/assets/` cu 6 imagini exec-stage (jpg, 3:2 cinematic), **specifice axei construcției**.

---

## Versiune unică per construcție (V39)

```
cNN/
├── HTML-Studiu-Excel-NN-{slug}.html
├── HTML-Editor-Studiu-Excel-NN-{slug}.html
├── HTML-Video-Excel-NN-{slug}.html
├── HTML-Editor-Video-Excel-NN-{slug}.html
├── Date_MASTER-CNN.xlsx
├── Creativ-Excel-NN-{slug}.txt
├── FILM-Excel-NN-{slug}.docx
└── assets/
    ├── exec-stage-1.jpg
    ├── exec-stage-2.jpg
    ├── ...
    └── exec-stage-6.jpg
```

**Schema veche (pre-V39):** existau `cNN/canonic/` (înghețat) + `cNN/editat/` (evolutiv) cu meta marker `trainity-snapshot`. Eliminată — versionarea o face git (commit + branch + tag v{N}) conform regulilor G1-G5 din CLAUDE.md.

**Avantaje versiune unică:**
- O singură copie pe disk (50% storage)
- Workflow editare simplificat (nu mai e nevoie de "patch peste editat")
- git log + tag v{N} sunt sursa de adevăr pentru evoluție (per fișier prin `git log --follow -- path`, per stare oficială prin `git checkout v{N}`)
- Audit simplificat (8 detectoare × N construcții, nu × 2 versiuni)

---

## Matrița pentru COPY+MODIFY: `_template/`

La generare CNN+ (C06+), motorul folosește `_template/` ca șablon — clonă cu aceeași structură ca `c01/` dar marcată explicit ca matriță.

```
_template/
├── HTML-Studiu-Excel-01-Structura.html      ← șablon, se modifică conținut/identitate
├── HTML-Editor-Studiu-Excel-01-Structura.html
├── HTML-Video-Excel-01-Structura.html
├── HTML-Editor-Video-Excel-01-Structura.html
├── Date_MASTER-C01.xlsx
├── Creativ-Excel-01-Structura.txt
├── FILM-Excel-01-Structura.docx
└── assets/                                   ← 6 imagini placeholder jpg
```

**Flow generare CNN:**
1. Citește `_template/` ca matriță
2. Aplică COPY+MODIFY (text/identitate per CNN, păstrează CSS/JS/structura)
3. Generează Date_MASTER-CNN.xlsx pornind de la `_system/referinte/Date_MASTER-initial.xlsx`
4. Generează Creativ + FILM pe SPEC CNN
5. Scrie în `cNN/`
6. Audit empiric (audit_sync.py) → confirmare ZERO DRIFT
7. Gate v20 → confirmare PASS
8. `git add c{NN}/ && git commit -m 'feat(c{NN}): generare initiala'` (push când ARHITECT cere; tag v{N} la consolidare)

---

## Asset-urile partajate

```
_system/referinte/
├── Date_MASTER-initial.xlsx          ← dataset canonic 2000 facturi B2B
├── IDENTITATE-TEHNICA.md             ← bloc per construcție: slug, treaptă, axa, FENOMENE
├── DATA-INSTRUCTIUNI.md              ← instrucțiuni T2 CUNOAȘTERE
├── SCHEMA-MASTER.md                  ← schema canonică 14 coloane Vanzari
├── COVER-CHECKLIST.md                ← cele 20 puncte atomice cover-header
├── PROTOCOL-FILM-OBS.md              ← protocol producție FILM.docx
├── highlighter-snippet.css           ← snippet CSS R-V03.59 V34
└── highlighter-snippet.js            ← snippet JS R-V03.59 V34
```

**Imaginile NU sunt partajate** — fiecare construcție are propriul `cNN/assets/` cu poze specifice axei sale (V39).

**Imaginile cinematic** sunt în HTML-Video ca base64 inline pentru funcționalitate (HTML self-contained, R-V03.33). Fișierele din `cNN/assets/` sunt pentru:
- Re-encodare în caz de modificare imagine
- Înlocuire poze (când vrei nouă imagine cu Banana 2)
- Backup independent de HTML-uri
- Refolosire în alte contexte (prezentări, social media)

---

## Diferența HTML-Studiu vs HTML-Editor-Studiu

Ambele au același conținut narativ + structural, dar:

| Aspect | HTML-Studiu | HTML-Editor-Studiu |
|---|---|---|
| **Audiență** | Cursant | ARHITECT (Bogdan) |
| **Editare text** | Nu se poate (read-only) | Da, prin `contenteditable` |
| **Toolbar editor** | Nu | Da (EDITOR PAGINĂ VIE cu butoane EXPORT, RESET) |
| **Butoane șterge element** | Nu | Da (la hover apare ✕) |
| **Export funcțional** | N/A | Buton 💾 EXPORT descarcă HTML curat (fără toolbar) |
| **Rol în workflow** | Versiunea livrată cursantului | Versiunea cu care lucrezi tu, ARHITECT |

**Workflow editare V39 (git V41):** ARHITECT deschide `HTML-Editor-Studiu` → editează inline → EXPORT → înlocuiește `HTML-Studiu` cu fișierul exportat (fără toolbar) în `cNN/` → `git add c{NN}/ && git commit -m 'docs(c{NN}): editare ARHITECT'`. Istoricul per fișier accesibil via `git log --follow -- c{NN}/HTML-Studiu-...html`.

Aceeași logică pentru `HTML-Video` vs `HTML-Editor-Video`.

---

## Schema sheet-uri Date_MASTER-CNN.xlsx

Conform R-V03.47 (schema unificată):

| Sheet | Conținut |
|---|---|
| `_REALITATE` | Narativ scena construcției (15 rânduri × 1 col) |
| `Vanzari` | **INPUT** — date cu fenomenele specifice construcției (2062 rânduri × 16 col pentru C01, similar pentru altele) |
| `Vanzari_Curat` (sau nume specific per cNN) | **OUTPUT** — date după transformare controlată (2001 rânduri × 14 col canonice) |
| `CLIENTI`, `PRODUSE`, `AGENTI`, `DEPOZITE` | Nomenclatoare auxiliare |
| `CONTROL_FINAL` | Ritual de verificare cap-coadă (15 rânduri × 3 col) |

**Sume conservate (R-V02.14):** suma valoare_neta input → output în general DELTA 0 (excepție: C02 are DELTA explicit +32K pentru cele 10 duplicate planted).

**Schema veche** (pre-R-V03.47): `Date-Input-Excel-NN.xlsx` + `Date-Output-Excel-NN.xlsx` separate. **Eliminată.** Toate construcțiile actuale folosesc Date_MASTER unificat.

---

## Schema FILM-Excel-NN-{slug}.docx

Script video procedural cinematic. 8 secțiuni canonice:

1. **HEADER** — titlu, treaptă, poziție în pack
2. **IDENTITATE CINEMATICĂ** — HOOK + MIZA + MANTRA + WOW + MOTTO
3. **DESCHIDERE · DE CE C{NN}** — context narativ
4. **ROLURI** — AI / Excel-PQ / OPERATOR (cine face ce)
5. **SCENA REALĂ** — cele N fenomene specifice construcției
6. **CELE 6 ETAPE** — fiecare cu structura HOOK→DEMO→CONTROL→REVEAL:
   - REALITATE → INVESTIGAȚIE → TRANSFORMARE → VERIFICARE → STABILIZARE → CONFIRMARE
7. **TRANZIȚIE** — predare către construcția următoare cap-coadă
8. **FINAL · SEMNĂTURĂ TRAINITY**

**Folosință:** documentul e referință pentru OBS Studio recording. ARHITECT recordează voce trainer Bogdan peste HTML-Video care rulează în browser. FILM.docx ține scriptul în paralel.

---

## Cum se generează un set complet (rezumat V40)

La comanda `genereaza CNN`:

1. Motor citește `_template/` (matriță)
2. Aplică COPY+MODIFY pe HTML-Studiu, HTML-Editor-Studiu, HTML-Video, HTML-Editor-Video → conținut specific CNN
3. Generează Date_MASTER-CNN.xlsx din `_system/referinte/Date_MASTER-initial.xlsx` + SPEC CNN (schema sheet-uri input/output)
4. Generează Creativ-Excel-NN-{slug}.txt din SPEC narativ
5. Generează FILM-Excel-NN-{slug}.docx prin sablon + completare cu specificul CNN
6. Copiază/generează 6 imagini exec-stage jpg în `cNN/assets/` (placeholder din _template inițial; ARHITECT regenerează cu Banana 2 specifice axei)
7. Scrie în `cNN/` (un singur folder)
8. Audit empiric (audit_sync.py) → confirmare ZERO DRIFT
9. Gate v20 → confirmare PASS
10. Commit Git unic cu mesaj clar
