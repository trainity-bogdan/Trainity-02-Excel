# WORKFLOW CAP-COADĂ BRAIN ↔ CONSTRUCȚIE

Documentul principal al sistemului Trainity V23+. Înghețat 25 mai 2026.

Citește acest document la deschiderea oricărui chat BRAIN sau CONSTRUCȚIE.
Este sursa de adevăr a workflow-ului. Tot ce e în brain.md sau
SISTEM_TRAINITY.md trebuie să respecte ce e aici. Dacă există conflict,
acest document câștigă.

---

## SCHIMBĂRI MAJORE V20 (25 mai 2026)

**1. CONSTRUCȚIILE SUNT INDEPENDENTE** — RENUNȚAT la cap-coadă strict V18.
Fiecare construcție pleacă de la `Date_MASTER-initial.xlsx` (asset
înghețat) și produce `Date_MASTER-C{NN}.xlsx`. C05 nu mai depinde de C04.
Chat-urile CONSTRUCȚIE pot rula paralel (cum cere R-V01.5).

**2. DATE_MASTER-INITIAL ca asset perpetuu canonic** în
`referinte/Date_MASTER-initial.xlsx`. Conține 2000 facturi sintetice,
schema canonică, sheets auxiliare, sumă ~7,986,000 lei. Toate
construcțiile C01-C08 pleacă de aici.

**3. DATA-INSTRUCTIUNI.md** detaliază pentru fiecare construcție EXACT
ce modificări să aplice pe Date_MASTER-initial.

**4. GATE V20 simplificat** — CLASA 6 verifică acum vs Date_MASTER-initial
(nomenclatoare identice, sumă în range conservare semantică), NU vs
construcția precedentă. Schema canonică păstrată.

---

## SCHIMBĂRI ISTORICE V18 (păstrate)

**1. CELE 6 LIVRABILE PER CONSTRUCȚIE** (NU mai 7):
- 4 HTML-uri (Studiu, Editor-Studiu, Video, Editor-Video) — neschimbat
- 1 Creativ-Excel-{NN}-{slug}.txt — neschimbat
- **1 Date_MASTER-C{NN}.xlsx — NOU, înlocuiește Date-Input + Date-Output**

**2. DATE_MASTER PROGRESIV CAP-COADĂ**: fiecare construcție pleacă de
la `Date_MASTER-initial.xlsx` (= OUTPUT-ul construcției precedente)
și produce `Date_MASTER-C{NN}.xlsx`. NU mai există dualitate
INPUT/OUTPUT duplicată.

**3. SCHEMA CANONICĂ ÎNGHEȚATĂ** (R-V03.47): cele 14 coloane standard
ale sheet-ului `Vanzari` rămân invariante între construcții. Vezi
`referinte/SCHEMA-MASTER.md`.

**4. CLASA 6 NOUĂ ÎN GATE: DATA-CONTINUITY** — verifică automat schema
canonică, continuitatea cap-coadă, conservarea sumei semantice între
construcții consecutive.

**5. FILTRE ANTI-FALS-POZITIV CODIFICATE** în gate_v20.py: CSS values
(opacity, transform, scale), Power Query whitelist (Refresh All,
Architecture, Applied Steps, Text.Trim etc.) recunoscute ca legitime.

---

## NOMENCLATURĂ ARHIVE (R-V03.46, INGHEȚAT V17)

**Arhive produse de chat BRAIN (`checkout brain`):**
```
OUT-V{NN}.zip
```
- NN = versiunea brain (V01, V02, ..., V17, V18, ...)
- Exemplu actual: `OUT-V17.zip`

**Arhive produse de chat CONSTRUCȚIE (`checkout constructie`):**
```
OUT-{CC}-V{NN}-{YYYYMMDD_HHMMSS}.zip
```
- CC = numărul construcției (01, 02, ..., 20)
- NN = versiunea brain de la care a plecat (de pe `OUT-V{NN}.zip` atașat)
- YYYYMMDD_HHMMSS = timestamp generare (data și ora) pentru unicitate
- Exemplu: `OUT-04-V17-20260525_143055.zip` = construcția 04, generată
  cu brain V17, la 25 mai 2026 14:30:55

**De ce timestamp:** pentru că Bogdan poate rula chat-uri CONSTRUCȚIE
paralele (chat-uri separate, simultane). Două arhive cu același CC și
același V_N pot exista — timestamp-ul distinge varianta canonică.

**Format vechi (deprecated):**
- `CHECKOUT_VNN.zip` → înlocuit cu `OUT-V{NN}.zip`
- `CHECKOUT_FROM_VNN_CMM_TIMESTAMP.zip` → înlocuit cu
  `OUT-{CC}-V{NN}-{YYYYMMDD_HHMMSS}.zip`

---

## ARHITECTURA SISTEMULUI

```
[Chat BRAIN V_N] ─────► OUT-V{N}.zip
                             │            (ex: OUT-V17.zip)
                             ▼
                    [Chat CONSTRUCTIE NN]
                             │
                             ├── 1. CHECKIN CONSTRUCTIE NN
                             ├── 2. Genereaza CONSTRUCTIA NN
                             ├── 3. GATE V20 ruleaza OBLIGATORIU
                             │      ├── PASS → continua pas 4
                             │      └── FAIL → regenerare (NU iese din chat)
                             ├── 4. checkout constructie
                             └─────► OUT-{CC}-V{N}-{YYYYMMDD_HHMMSS}.zip
                                            │ (ex: OUT-04-V17-20260525_143055.zip)
                                            ▼
                                  [Chat BRAIN V_N] (vine cu arhiva)
                                            │
                                            ├── 5. CHECKIN BRAIN
                                            ├── 6. Audit livrabilele
                                            ├── 7. Detecteaza erorile
                                            ├── 8. Codifica regula (clasa, nu caz)
                                            ├── 9. checkout brain
                                            └─────► OUT-V{N+1}.zip
                                                          │ (ex: OUT-V24.zip)
                                                          ▼
                                                  (cycle se repeta)
```

## DOUĂ TIPURI DE CHAT, DOUĂ ROLURI

### Chat BRAIN

**Scop:** sistem, arhitectură, consolidare. Brain învață din arhivele
CONSTRUCTIE care vin la el și codifică reguli noi.

**NU se generează construcții în chat BRAIN.** Excepție: livrabile pilot
ad-hoc (overlay-uri, bug-fix universal, modificări UX pe matriță).

**Comenzile:**
- `CHECKIN BRAIN` — la deschiderea chatului, cu arhivă atașată.
  Brain citește integral brain.md + SISTEM_TRAINITY.md + KIT-V16 +
  WORKFLOW-CAP-COADA + referințe + creative_banana2 + pilot.
- `checkout brain` — la finalul chatului. Produce OUT-V_(N+1).zip
  ca unicul fișier livrat. Conține brain consolidat cu lecțiile noi.

### Chat CONSTRUCȚIE NN

**Scop:** construire deterministă a celor 7 livrabile pentru o construcție
specifică (C01, C02, ..., C20).

**Comenzile:**
- `CHECKIN CONSTRUCTIE NN` — la deschiderea chatului, cu aceeași arhivă
  OUT-V_N.zip ca BRAIN. Motorul citește integral, intră în context.
- `Genereaza CONSTRUCTIA NN` — produce cele 7 livrabile prin COPY-MODIFY
  pe pilot C01 V12, cu SPEC C{NN} și IDENTITATE_TEHNICA C{NN} aplicate.
- Automat după generare: **GATE V20 RULEAZĂ OBLIGATORIU**. Dacă picătură,
  prezent_files BLOCAT, se cere regenerare în chatul curent.
- `checkout constructie` — la finalul chatului, doar după GATE PASS.
  Produce dual:
  - `OUT-CC-V_N-YYYYMMDD_HHMMSS.zip` (arhivă completă pentru BRAIN)
  - Toate livrabilele individuale la `/mnt/user-data/outputs/`

## CELE 6 LIVRABILE PER CONSTRUCȚIE (V19)

1. `HTML-Studiu-Excel-{NN}-{slug}.html` — cockpit operațional (Studiu)
2. `HTML-Editor-Studiu-Excel-{NN}-{slug}.html` — variantă editabilă
3. `HTML-Video-Excel-{NN}-{slug}.html` — broadcast pentru filmare
4. `HTML-Editor-Video-Excel-{NN}-{slug}.html` — variantă editabilă
5. `Creativ-Excel-{NN}-{slug}.txt` — prompturi Banana 2 pentru imagini
6. `Date_MASTER-C{NN}.xlsx` — Date_MASTER cu modificările specifice C{NN}

**Filosofia V19 — CONSTRUCȚII INDEPENDENTE:**

Toate construcțiile C01-C08 pleacă de la `referinte/Date_MASTER-initial.xlsx`
(asset perpetuu înghețat în arhivă). Fiecare construcție citește acest
fișier, aplică modificările specifice SPEC C{NN} (vezi
`referinte/DATA-INSTRUCTIUNI.md`), livrează `Date_MASTER-C{NN}.xlsx`.

**NU există dependență cap-coadă obligatorie.** C05 NU dependă de C04.
C03 NU dependă de C02. Chat-urile CONSTRUCȚIE pot rula paralel.

**Schema canonică** rămâne identică în toate Date_MASTER-C{NN}.xlsx
(14 coloane sheet Vanzari, sheets auxiliare CLIENTI/PRODUSE/AGENTI/DEPOZITE).
Construcțiile pot adăuga coloane noi (ex: C05 adaugă `segment_client`,
`prioritate_produs`) sau sheets noi (ex: C04 adaugă `_NORMALIZARE`),
dar NU modifică schema canonică existentă.

**Chat-ul CONSTRUCTIE NN** primește în arhiva atașată asset-ul comun
Date_MASTER-initial.xlsx (din `referinte/`). Acest fișier nu se modifică
niciodată. Construcția produce Date_MASTER-C{NN}.xlsx ca livrabil propriu.

## REGULĂ ABSOLUTĂ R-V03.45 — GATE V20 OBLIGATORIU

**Înainte de orice present_files în chat CONSTRUCȚIE, motorul DEVE
rula `python3 generatoare/gate_v20.py NN livrabile_CNN/ pilot_C01_V12/`.**

- Dacă GATE PASS → motorul continuă cu present_files și checkout constructie
- Dacă GATE FAIL → motorul NU livrează, raportează erorile la Bogdan,
  cere regenerare în chatul curent

**Această regulă nu admite excepții.** Dacă chat CONSTRUCȚIE NN livrează
fără să fi rulat gate-ul, Bogdan refuză arhiva și cere refacere.

## CE VERIFICĂ GATE V20

6 CLASE de erori (nu cazuri specifice):

### Clasa 1 — NO-CLONE GENERIC
Pentru fiecare zonă textuală vulnerabilă, verifică similarity cu pilot
C01 V12. Threshold per zonă:
- prompt-text: 0% (toleranță zero)
- step-title, step-action, anomaly-card-desc, payoff-line, stage-quote: 30%
- prompt-label, cover-subtitle, cover-miza: 50%
- final-label: 70% (generice OK)

Adăugarea unei zone noi vulnerabile = update lista TEXTUAL_ZONES în
gate_v20.py, nu regulă separată.

### Clasa 2 — IDENTITY
Verifică string-urile cu identitate construcție:
- cover-label: "CONSTRUCȚIA C{NN}" exact
- cover-title: conține nume_hero_caps_rand1 din IDENTITATE_TEHNICA
- meta-val-treapta: match exact format din IDENTITATE_TEHNICA
- footer: conține codul C{NN}
- topbar (Video): conține codul C{NN}
- localStorage: keys = trainity_c{NN}_*
- <title> (Video): conține codul C{NN}

### Clasa 3 — BRAND (V18 cu whitelist Power Query)
- Zero em-dash (U+2014)
- Zero en-dash (U+2013) în text vizibil
- Zero engleză forbidden: Normalize, Tutorial, Lesson, Quiz, Module,
  Course, Webinar, Masterclass
- Zero vocab brand forbidden în text vizibil: tutorial, masterclass,
  webinar, productivitate, lecție, lectie

**Whitelist V18**: termeni Microsoft canonici (Refresh All, Refresh,
Applied Steps, Power Query, Power BI, Pivot Table, Architecture
în context flux PQ, Text.Trim, Text.Replace, Number.FromText etc.)
recunoscuți ca legitimi.

Excepție: comentarii CSS/JS pot conține "curs/cursant/modul" pentru
context tehnic.

### Clasa 4 — CROSS-CONTAMINATION
Niciun cod CXX vizibil ≠ C{NN} curent, cu excepții legitime:
- Filename link cu cod construcție curentă
- next-section: predare la next_cod (C{NN+1})
- Final-block: "predăm baza către C{NN+1}"

### Clasa 5 — VOCE
- HTML-Studiu: persoana 2 singular ("Deschide", "Verifică")
- HTML-Video: persoana 3 plural ("Deschidem", "Verificăm")

### Clasa 6 — DATA-CONTINUITY (NOU V18, R-V03.47)
Pentru `Date_MASTER-C{NN}.xlsx`:
- Sheet principal exact `Vanzari`
- Cele 14 coloane canonice prezente în ordine (vezi SCHEMA-MASTER.md)
- Sheets auxiliare canonice prezente (CLIENTI, PRODUSE, AGENTI, DEPOZITE)
- Dacă există `Date_MASTER-initial.xlsx` ca referință:
  - Schema curentă ⊇ schema precedentă (coloane se păstrează, doar
    se adaugă)
  - Suma `valoare_neta` conservată (delta < 0.01 lei sau declarat în SPEC)

## CICLUL DE ÎNVĂȚARE

Ce face BRAIN când primește o arhivă CONSTRUCȚIE:

1. **Citește arhiva OUT-CC-V_N-YYYYMMDD_HHMMSS.zip**
2. **Rulează GATE V20** pe livrabile (audit independent)
3. **Pentru fiecare eroare detectată:**
   - Întreabă: din ce CLASĂ face parte?
   - Dacă clasa există → extinde verificatorul existent
   - Dacă clasa e nouă → adaugă verificator nou (rare)
   - Codifică regula GENERIC (nu specific)
4. **Documentează în brain.md** ca lecție nouă L{n}
5. **Update IDENTITATE_TEHNICA** dacă apar valori noi (next_title, etc.)
6. **`checkout brain` la final** — produce OUT-V_(N+1).zip

**Filosofia învățării:** "ce CLASĂ de eroare am făcut", nu "ce eroare
specifică". Fix de cauză, nu fix de simptom.

## SCENARII

### Scenariu 1 — Construcție nouă C{NN} (RECOMANDAT V20)

```
1. Bogdan: deschide chat CONSTRUCTIE NN cu OUT-V_N.zip atasat
2. Bogdan: scrie DIRECT "Genereaza CONSTRUCTIA NN" (fara CHECKIN explicit)
3. Motor: recunoaste implicit CHECKIN, citeste toate documentele,
   confirma scurt "Am citit. Procedez la generare." (R-V03.51)
4. Motor LIVREAZA INCREMENTAL cele 6 livrabile - cate un fisier per
   mesaj (R-V03.52, ordine de la mic la mare):
   - Mesaj 1: Date_MASTER-C{NN}.xlsx
   - Mesaj 2: Creativ-Excel-{NN}-{slug}.txt
   - Mesaj 3: HTML-Studiu-Excel-{NN}-{slug}.html
   - Mesaj 4: HTML-Editor-Studiu-Excel-{NN}-{slug}.html
   - Mesaj 5: HTML-Video-Excel-{NN}-{slug}.html
   - Mesaj 6: HTML-Editor-Video-Excel-{NN}-{slug}.html
5. Motor: ruleaza gate_v20.py automat (R-V03.45)
6. Daca GATE PASS:
   - Motor: ofera checkout constructie
   - Produce arhiva OUT-{NN}-V_N-{TIMESTAMP}.zip + livrabile la /outputs
   - Bogdan: descarca, verifica vizual, aproba
7. Daca GATE FAIL:
   - Motor: raporteaza erorile la Bogdan
   - Cere regenerare in chatul curent
   - Repeat de la pas 5 pana PASS
8. Bogdan: deschide chat BRAIN cu arhiva CONSTRUCTIE
9. Brain: audit, codifica regula (clasa), checkout brain
```

### Scenariu 1b — Construcție cu CHECKIN explicit (cand vrei pauza)

```
1. Bogdan: deschide chat CONSTRUCTIE NN cu OUT-V_N.zip atasat
2. Bogdan: "CHECKIN CONSTRUCTIE NN"
3. Motor: citeste integral, confirma context complet (lista documente
   citite + SPEC C{NN} extras + intentie generare)
4. Bogdan: poate cere modificari SPEC inainte de generare
5. Bogdan: "Genereaza CONSTRUCTIA NN"
6. Motor: procedeaza la generare + gate + checkout (ca in Scenariul 1)
```

### Scenariu 2 — Regenerare parțială C{NN}

Când doar unele livrabile sunt invalidate (ex: HTML-Studiu+Editor din C03 V14):

```
1. Bogdan: deschide chat CHECKIN CONSTRUCTIE NN cu OUT-V_N.zip
2. Bogdan: explică ce trebuie regenerat și ce se păstrează
3. Motor: regenerează doar ce e cerut
4. Motor: rulează gate_v20.py pe fișierele regenerate
5. Gate gestionează "Fișiere lipsă" (nu picătură pe Video lipsă
   dacă regenerare e pe Studiu)
6. Dacă GATE PASS pe regenerate:
   - "checkout constructie" produce arhiva parțială + README explicit
   - Bogdan integrează cu livrabilele păstrate din arhiva veche
```

### Scenariu 3 — Update doar BRAIN (consolidare, fără construcție)

```
1. Bogdan: deschide chat CHECKIN BRAIN cu OUT-V_N.zip
2. Brain: citește integral, confirmă context
3. Bogdan: cere modificare sistem (regulă nouă, update IDENTITATE_TEHNICA,
   etc.)
4. Brain: aplică modificarea, documentează în brain.md ca lecție nouă
5. Brain: "checkout brain" produce OUT-V_(N+1).zip
```

## REGULI ANTI-FRAGILITATE

1. **Brain NU generează construcții.** Doar consolidează.
2. **Construcție NU codifică reguli noi.** Doar execută.
3. **Gate ruleaza automat, nu opțional.** Fără excepții.
4. **Erori se învață ca CLASE.** Nu cazuri specifice.
5. **Identitatea trăiește în IDENTITATE_TEHNICA.md.** Generator citește,
   nu interpretează.
6. **Toate decizinile ARHITECT (Bogdan) se documentează imediat în
   brain.md** ca lecții noi.

## DACĂ CEVA SE STRICĂ

Pattern de redresare:

1. Bogdan semnalează problema (cu exemplu concret)
2. Brain face audit exhaustiv pe arhive existente
3. Brain identifică **clasa** problemei (nu doar cazul)
4. Brain propune fix structural (mecanism, nu regulă specifică)
5. Bogdan confirmă direcția
6. Brain implementează în următorul checkout brain
7. Bogdan testează în chat CONSTRUCȚIE următor

**Pattern Trainity consacrat:** ARHITECT pune întrebări brutale,
CONSTRUCTOR răspunde onest cu cauza root, codifică regulă generică.
