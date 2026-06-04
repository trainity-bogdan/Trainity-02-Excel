# AUDIT ATOMIC · PACK 02 EXCEL

> Audit chirurgical la nivel de litera/octet pe TOT repo-ul. Rulat cap-coada pe starea curenta a `main`.
> Data: 4 iunie 2026 · Perimetru: 274 fisiere git-tracked (toate) · Branch: `main`.
> Metoda: 13 straturi atomice, scriptere deterministe (stdlib + openpyxl/docx), fiecare constatare cu coordonate exacte.
> Principiu cheie: separ REALUL de ZGOMOT. Un `getElementById` fara id static, dar gardat `if(!hud)return`, NU e bug.

---

## 1. REZUMAT EXECUTIV

Scanate 274 fisiere; 502 semnale brute triate atomic. **Dupa de-zgomotare: 8 probleme reale HIGH/MEDIUM si un strat de LOW (igiena/consistenta).** Stratul tehnic-dur e curat la nivel de octet: conservare suma la banut, identitate corecta, cod care compileaza, base64 valid, zero id duplicat, companion sincronizat.

**Probleme reale (de-zgomotate):**
- **NOU - C02 FILM (13) si C04 FILM (17) au em-dash** (`—`, U+2014) in narativ -> incalca regula brand "fara em/en-dash". Nici audit_sync, nici gate nu citesc `.docx` pentru dash, deci au scapat la V2.
- **NOU - C04 Studiu + Editor-Studiu: "delta sub 0,01 lei"** in final-label (learner-facing). Zona gri R-V02.15: e un PRAG de precizie (un ban), nu o valoare business -> sever mic, dar mentioneaza "lei" + cifra.
- **C10 cuvant cheie "MASURA POTRIVITA" != "MASURI"** (decizie BRAIN explicita, commit e75c243) si **C11 cuvant cheie "IERARHIE" != "COMPARATII"** (pare bug: e singura constructie care nu foloseste cuvantul identitatii treptei).
- **C12 fara folder `assets`** + **C10/C11/C12 imagini placeholder SVG** (ne-reale) -> dependenta ARHITECT.
- **c10/assets == c11/assets byte-identice (7/7)** (clona).

**Curat atomic (PASS):** Excel (suma 7.986.019,38 la banut C03->C12; 14 headere canonice scrise exact), identitate (breadcrumb/localStorage/footer/title/hov-kicker corecte 12/12), cod (25 scripturi compileaza; slug gate_v20 == filename), cover-title (12/12 prezent post-fix), HTML (0 id duplicat, base64 100% valid, companion sincronizat), index (48/48 + cache-bust).

---

## 2. METODA: 13 STRATURI ATOMICE

| Strat | Ce verifica | Scope |
|---|---|---|
| 0 | Octeti invizibili (BOM, NBSP, ZWSP, CRLF, trailing) | 166 fisiere text |
| 1 | Diacritice cedila gresita (ş/ţ U+015F/0163 vs ș/ț) | toate text |
| 2 | Tipografie (em/en-dash, ghilimele, ellipsis) | toate text |
| 3 | Matrice identitate (cuvant cheie/breadcrumb/LS/footer/title/kicker) | 12 Studiu |
| 4 | Structura HTML (id unic, base64, referinte id, taguri, cover-title) | 48 HTML |
| 5 | Sync companion (step-titles Studiu==Editor) | 12 perechi |
| 6 | Cifre business R-V02.15 | 48 HTML + 12 FILM |
| 7 | Excel atomic (headere, suma la banut) | 12 xlsx |
| 8 | FILM docx (cedila/dash/arc) | 12 docx |
| 9 | Assets (hash/duplicate/placeholder/naming) | 78 imagini |
| 10 | Cod Python (compilare, dict identitate vs real) | 25 scripturi |
| 11 | Docs (referinte interne, afirmatii de stare) | 66 .md |
| 12 | Meta (git tracked junk, cache-bust) | repo |

Comanda: scriptere in `/tmp/atomic/`, output JSONL agregat (502 randuri).

---

## 3. MATRICE FINDINGS (brut vs real)

| Strat | Brute | Reale (dupa triere) | Zgomot/fals-pozitiv |
|---|---|---|---|
| 0/1 | 15 | cedila in docs active (LOW) | cedila in tabelele de pliere ale validatoarelor = legitim |
| 2 | 218 | inconsistenta ghilimele pachet (LOW) | dash/quote in docs interne = informational |
| 3 | 2 | C10 + C11 cuvant cheie (MEDIUM) | - |
| 4 | 216 | 0 | 24 getElementById (HUD dormant, gardat `if(!hud)return`) + 192 href="#final" (navigare JS onclick) = FALS-POZITIV, identic in C01 referinta |
| 6 | 2 | C04 "0,01 lei" zona gri (LOW) | auto-marcat CRITICAL de regex, real = prag de precizie |
| 8 | 6 | C02/C04 FILM em-dash (MEDIUM) + arc lipsa (LOW) | - |
| 9 | 16 | c12 fara assets (HIGH), placeholdere (HIGH), clona c10==c11 (MEDIUM), naming (LOW) | - |
| 11 | 26 | ~6 referinte rupte in docs ACTIVE (LOW) | ~25 in `_system/arhiva/**` = istoric, stale asteptat |
| 12 | 1 | 1 `.pyc` trackat (LOW) | - |

---

## 4. PROBLEME REALE

### CRITICAL
Niciuna confirmata. (Cele 2 auto-marcate la L6 = "delta sub 0,01 lei", reclasate LOW: prag de precizie, nu valoare business.)

### HIGH
- **H-1. C12 fara folder `assets`.** Singura constructie fara imagini-sursa pe disc. (audit_sync R-V39 = FAIL.) RAMANE ARHITECT.
- **H-2. C10/C12 imagini placeholder SVG** (hero + 6 exec-stage fiecare) si **C11 hero placeholder SVG** (pus de reparatia anterioara, in locul clonei C01). Ne-reale, marcate temporar. RAMANE ARHITECT (imagini reale).

### MEDIUM
- **M-1 (NOU). C02 FILM = 13 em-dash, C04 FILM = 17 em-dash** (`—` U+2014). Ex.: "nomenclatoare — LOCALITATI", "ordinea — Promoted Headers". Incalca regula brand. C01/C03/C05-C12 FILM = 0. REPARABIL automat (-> ", " sau ": ").
- **M-2. C11 cuvant cheie hero = "IERARHIE"** in loc de "COMPARATII". Singura constructie unde `hov-object` != cuvantul identitatii treptei. Pare bug de generare. REPARABIL (cu confirmare).
- **M-3. C10 cuvant cheie hero = "MASURA POTRIVITA"** in loc de "MASURI". Decizie BRAIN explicita (commit `e75c243`), rupe tiparul cuvant-unic. DECIZIE BRAIN.
- **M-4. c10/assets == c11/assets byte-identice (7/7)** inclusiv hero. Clona; nefolosite de HTML (orfane). RAMANE ARHITECT (imagini reale per constructie).

### LOW (igiena / consistenta)
- **L-1 (NOU). C04 Studiu + Editor-Studiu: "delta sub 0,01 lei"** in final-label SUMA. Zona gri R-V02.15. Sugestie: "delta sub un ban" / "delta neglijabila".
- **L-2 (NOU). Inconsistenta ghilimele pe pachet:** C05-C09 drepte ("), C11 majoritar romanesti („"), C10/C12 mixt. Tipografic, C11 e mai corect; restul ar trebui aliniate la un singur stil.
- **L-3 (NOU). Diacritice cedila in docs active:** `_system/10-MAP-FILM-HTML.md` (11x ş/ţ), `STARE-CURENTA.md` (2x). In livrabilele HTML = 0. (Cedila din gate_v20/tier_guard/audit_sync e in tabelele de pliere = legitim.)
- **L-4 (NOU). 1 `.pyc` trackat in git:** `_system/generatoare/__pycache__/audit_sync.cpython-314.pyc` (ar trebui in .gitignore).
- **L-5 (NOU). ~6 referinte rupte in docs ACTIVE:** `PROMPTURI-SLIDES-EXEC-C02.txt`/`C03.txt`, `R-V03.66-...yaml`, `cross_consistency.py`, `SISTEM_TRAINITY.md`, naming vechi `...-Editat.html`. (Restul ~25 sunt in `_system/arhiva/**` = istoric, stale asteptat.)
- **L-6. FILM fara arc complet** (ARC/CINE DEVII/DE ACUM) la C08, C09, C10, C12.
- **L-7. Nume hero neconform:** `c01/assets/hero-structura.jpg`, `c04/assets/hero-normalizare.jpg` (vs `hero-poster-excel-NN-slug.jpg`); `c01/assets/infografic-...jpg` extra unic.

---

## 5. CURAT ATOMIC (PASS verificat la nivel de octet)

- **Excel (Strat 7):** suma valoare_neta = `7.986.019,38` IDENTIC la banut C03->C12; C02=`8.018.087,99` (pre-audit), C01=`1.247.893,50` (dataset propriu). Cele 14 headere canonice scrise exact in toate foile-output. PASS.
- **Identitate (Strat 3):** breadcrumb (4 tokeni corecti per treapta), `trainity_cNN_*`, footer cu cod, `<title>` cu cod, `hov-kicker "OBIECTUL CONSTRUCTIEI · CNN"` - corecte 12/12. PASS (exceptie cele 2 cuvinte cheie M-2/M-3).
- **HTML (Strat 4/5):** 0 id duplicat; 100% base64 valid (decodeaza JPEG/PNG); cover-title prezent+negol 12/12 (post-fix); step-titles Studiu==Editor-Studiu. PASS.
- **Cod (Strat 10):** 25 scripturi compileaza; `IDENTITATI[nume_slug]` din gate_v20 == slug filename pe toate 12. PASS.
- **Index/meta (Strat 12):** 48/48 linkuri cu cache-bust `?v=N`. PASS.

---

## 6. FALS-POZITIVE IDENTIFICATE (valoarea auditului atomic)

Atomic-ul a evitat 4 capcane care la un audit superficial ar fi parut bug-uri:
1. **216 referinte HTML "rupte"** -> de fapt feature HUD dormant gardat `const hud=getElementById("hud"); if(!hud) return;` (comentariu "skip silent") + navigare prin `onclick="navigateFinal()"` + `data-final`. Identice in C01 (referinta validata). NU sunt bug-uri.
2. **248 referinte "rupte" in docs** -> fisiere mentionate pe nume scurt care EXISTA in alta parte (ex. `audit_sync.py` la `_system/generatoare/`). Doar 31 sunt absente real, din care ~25 in arhiva istorica.
3. **22 diacritice cedila** -> 13 sunt in tabelele de pliere diacritice ale validatoarelor (`'...șțşţ'`), legitim by design.
4. **2 "CRITICAL lei"** -> prag de precizie "0,01 lei", nu valoare business.

---

## 7. ORDINEA RECOMANDATA DE REPARATII

**Reparabil automat acum (fara ARHITECT):**
1. C02 + C04 FILM: em-dash -> virgula/doua puncte (M-1).
2. C11 cuvant cheie hero "IERARHIE" -> "COMPARATII" (M-2, cu confirmare).
3. C04 "delta sub 0,01 lei" -> "delta sub un ban" (L-1).
4. Aliniere stil ghilimele la unul singur (L-2).
5. Cedila ş/ţ -> ș/ț in docs active (L-3).
6. `.gitignore` += `__pycache__/` si scoatere `.pyc` trackat (L-4).
7. Curatare referinte rupte in docs active (L-5).

**Decizie BRAIN:** C10 "MASURA POTRIVITA" (M-3) - se pastreaza sau se aliniaza la "MASURI"?

**RAMANE ARHITECT (imagini reale):** C10/C12 placeholdere, C12 fara assets, C11 hero real, clona c10==c11 (H-1, H-2, M-4).

---

## 8. VERDICT FINAL

La nivel de **octet, infrastructura este foarte solida**: conservarea sumei e exacta la banut, identitatea e corecta pe toate 12, codul compileaza, base64 e valid, companionii sunt sincronizati, index-ul e complet. Stratul tehnic-dur trece atomic.

**Problemele reale sunt putine si concentrate:** doua FILM-uri cu em-dash (C02/C04, nou, reparabil), doua cuvinte cheie deviante (C10 decizie BRAIN, C11 bug), si finisajul vizual T3 (placeholdere/assets, dependenta ARHITECT). Restul = igiena (ghilimele, cedila docs, pyc, referinte docs).

**Cea mai valoroasa contributie a rundei atomice fata de V2:** a prins em-dash-urile din FILM C02/C04 si "0,01 lei" din C04 (clase de eroare pe care validatoarele actuale nu le acopera in `.docx`/final-label), si a demontat 216+248 fals-pozitive ca sa nu se iroseasca efort pe ele.

**Reguli noi propuse (detectoare):** (a) dash/cedila in `.docx` FILM; (b) cuvant cheie `hov-object` == identitatea treptei; (c) cover-title negol + distinct de hero-question; (d) `.pyc`/`__pycache__` interzise in git; (e) stil ghilimele unic.

Nicio reparatie aplicata in aceasta runda (audit pur). 502 semnale brute -> 8 reale HIGH/MEDIUM + LOW de igiena.

AUDIT_ATOMIC_DONE
