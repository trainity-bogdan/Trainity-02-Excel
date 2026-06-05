# RAPORT · LOCKED NAMING C01-C12

## STATUS

**C01-C12_NAMING_LOCKED** — aplicat pe suprafețele PRIMARE learner-facing (hero keyword,
cover-title, breadcrumb/system-map, index). NU integral: 4 suprafețe rămân blocate de validatoare
hardcodate sau sunt strat separat (vezi §Conflicte + §Reziduuri). Nimic ocolit, totul raportat.

## SHA

- Inițial: `ded49616ae11f2d58c156b28bd9a1f0cd0e65856`
- Final: acest commit (`copy(system): lock c01-c12 naming methodology`)

## Nomenclatura aplicată (LOCKED)

| C | Keyword (hov-object) | Nume extins (cover-title) | Verb (metoda) |
|---|---|---|---|
| C01 | STRUCTURAREA | Structurarea corectă a tabelului | STRUCTUREZ |
| C02 | CONFRUNTAREA | Testarea datelor cu realitatea | CONFRUNT |
| C03 | AUDITAREA | Auditarea problemelor ascunse | AUDITEZ |
| C04 | NORMALIZAREA | Curățarea automată a datelor | NORMALIZEZ |
| C05 | INVENTARIEREA | Cunoașterea setului de date | INVENTARIEZ |
| C06 | CLASIFICAREA | Clasificarea rândurilor | CLASIFIC |
| C07 | DATAREA | Datarea tranzacțiilor | DATEZ |
| C08 | MAPAREA | Maparea tabelelor | MAPEZ |
| C09 | LEGAREA | Legarea tabelelor | LEG |
| C10 | MĂSURAREA | Definirea măsurilor | MĂSOR |
| C11 | COMPARAREA | Construirea clasamentelor | COMPAR |
| C12 | INTERPRETAREA | Interpretarea rezultatelor | INTERPRETEZ |

Notă C10: keyword = MĂSURAREA, nume extins = Definirea măsurilor. Ambele LOCKED (NU schimbat în
DEFINIREA ca nume scurt, NU în MĂSURILE).
Notă de stil: cover-title aplicat în propoziție-case (prima literă majusculă), ca să păstreze
stilizarea h1 existentă; semantica e identică cu numele LOCKED (scrise cu majuscule în mandat).

## Ce a fost schimbat (25 fișiere)

Per construcție, în HTML-Studiu + HTML-Editor-Studiu (24 fișiere):
1. **HERO KEYWORD** — text `<span class="hov-object">` -> keyword nou.
2. **COVER TITLE** — text `<h1 class="cover-title">` -> nume extins (atributele, ex. data-locked, păstrate).
3. **BREADCRUMB / SYSTEM MAP** — cele 4 `<span class="sm-step">` (harta treptei) -> tokenii noi ai treptei.

Plus **index.html**: cele 12 `card-title` -> numele extinse noi.

Listă fișiere:
```
c01..c12 / HTML-Studiu-Excel-NN-*.html
c01..c12 / HTML-Editor-Studiu-Excel-NN-*.html
index.html
```

## Validări (toate trec)

| Validator | Rezultat |
|---|---|
| `audit_sync.py` | DRIFT 1 (DOAR C12 assets, preexistent) - fara regresie |
| `gate_v20.py` C01-C12 | **12/12 PASS** |
| `pre_generation_check.py` C01-C12 | **12/12 (3/3)** PASS |
| `tier_guard_t3.py` c09-c12 | 0 blocante (c11 PASS; restul WARNING = false-pozitive `top`/`explic`) |
| em-dash / en-dash introdus | 0 |
| cedila introdusa | 0 |

gate_v20 trece pentru că schimbarea atinge hov-object/cover-title/breadcrumb (neverificate de gate la
premium), iar `mobile-topbar-title` (singurul verificat, pe `nume_slug`) a fost lăsat neatins.

## Conflicte cu validatoare hardcodate (NU ocolite, raportate)

**`_system/generatoare/gate_v20.py` — TOP NAV blocat.**
- `check_identity` (calea premium) cere: `fold_diac(nume_slug)` să fie substring în
  `mobile-topbar-title`.
- `IDENTITATI` (dict hardcodat, ~liniile 1066-1127) ține `nume_slug`: Structurare, Control, Auditare,
  Normalizare, Dictionar, Clasificare, Datare, Cartografiere, Relatii, Masuri, Comparatii, Interpretare.
- Impact: dacă schimb `mobile-topbar-title` din „CNN · Slug" în keyword-ul nou, gate PICĂ pentru
  **C02, C05, C08, C09, C10, C11** (keyword nu conține slug-ul: CONFRUNTAREA≠Control,
  INVENTARIEREA≠Dictionar, MAPAREA≠Cartografiere, LEGAREA≠Relatii, MĂSURAREA≠Masuri,
  COMPARAREA≠Comparatii).
- Decizie: am LĂSAT topbar-ul „CNN · Slug" (gate trece). Actualizarea TOP NAV necesită editarea
  `gate_v20.IDENTITATI[nume_slug]` = modificare de regulă gate, INTERZISĂ de mandat. Necesită
  decizie SYSTEM separată.
- Tot în `IDENTITATI`, câmpurile `nume_hero_caps_rand1` (STRUCTURA, DICȚIONARUL, MĂSURA, CINE,
  DE CE-UL...) și `meta_val_treapta` (string-uri breadcrumb vechi) sunt acum stale, dar NU sunt
  verificate la premium, deci nu pică nimic. Rămân stale până la o curățare SYSTEM a dict-ului.

## Reziduuri (suprafețe neatinse în acest pas)

1. **HTML-Video + HTML-Editor-Video (24 fișiere)** — structură de identitate DIFERITĂ: folosesc
   hero-title cinematic (ex. „DICȚIONARUL DATELOR", „MĂSURA POTRIVITĂ", „CINE CONDUCE",
   „DE CE-UL DIN DATE", „RELAȚIILE DINTRE DATE"), NU keyword/cover-title/breadcrumb. Schimbarea lor =
   rescriere de titlu cinematic (graniță cu „conținut", pe care mandatul îl păstrează). Necesită
   decizie separată ARHITECT/regie video.
2. **TOP NAV (mobile-topbar-title)** — blocat de gate (vezi Conflicte).
3. **README.md, STARE-CURENTA.md, IDENTITATE-TEHNICA.md, system maps doc, documentație activă,
   registre/SPEC** — referințe narative/structurate. IDENTITATE-TEHNICA.md ține câmpuri tehnice
   (pre_generation_check verifică doar PREZENȚA câmpurilor, nu valorile, deci nu pică), dar e doc de
   sistem, nu display learner-facing. README/STARE narrative mari. Neatinse aici; de aliniat într-un
   pas de documentație dedicat.

## Confirmare

Nomenclatura LOCKED e aplicată **integral pe suprafețele primare learner-facing afișate cursantului**:
hero keyword (hov-object), titlul construcției (cover-title), harta treptei (breadcrumb/system-map) în
Studiu + Editor-Studiu, și titlurile din index. Validatoarele trec (gate 12/12, audit_sync fără
regresie).

Suprafețele rămase (Video cinematic, TOP NAV, docs de sistem) NU pot fi aliniate fără fie editarea
regulilor gate (interzisă), fie decizii de conținut cinematic/narativ. Sunt raportate exact mai sus,
nu ocolite.

C01-C12_NAMING_LOCKED
