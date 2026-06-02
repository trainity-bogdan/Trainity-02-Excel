# PLAN DE EXECUȚIE · C02 CONTROL (LOCK → PRODUS)

> Document de PROJECT MANAGEMENT. NU redeschide arhitectura, NU propune anomalii,
> NU modifică blueprint-ul. Transformă C02 LOCK în produs livrabil.
> Pereche cu `BLUEPRINT-C02-CONTROL.md` (target) + `SPEC-DATE-MASTER-C02.md` (date+reguli).
> Stare intrare: identitate + 5 anomalii + ordine + roluri AF/CF/DV = LOCK. Treaptă: T1.

---

## 0. STARE LOCK (rezumat operațional, NU se redeschide)
- Temă: CORESPONDENȚA CU REALITATEA · AHA: „Valid nu înseamnă corect."
- Anomalii LOCK în ordine: Orașe → TVA → Scadență → NETWORKDAYS → CNP.
- Roluri: AF=DESCOPERIRE · CF=SEMNALIZARE · DV=ergonomie marginală. DV prevenție/cascadă=T5.
- Corpul `c02/` actual = versiunea veche MARCARE (36 anomalii structurale). Se SUPRASCRIE.

---

## 1. PLANUL EXACT DE CONSTRUIRE `Date_MASTER-C02.xlsx` (în ordine recomandată)

> Principiu de construcție: întâi ADEVĂRUL (nomenclatoarele corecte), apoi DATELE curate,
> apoi se INJECTEAZĂ anomaliile controlat, apoi se ADAUGĂ semnalizarea. Niciodată invers.

**Pas D1 — Nomenclatoarele de referință (sursa de adevăr).**
Construiește cele 4 tabele satelit ÎNAINTE de orice anomalie, pentru că ele definesc ce e „corect":
`tbl_Localitati` (oraș↔județ oficial), `tbl_RegulriTVA` (categorie→cotă legală),
`tbl_SarbatoriLegale` (calendarul anului setului), `tbl_CodJudetCNP` (cod→județ).
*De ce primul:* fără referința oficială nu poți nici planta o abatere, nici semnaliza una.

**Pas D2 — `Vanzari` curat + coloane noi de input.**
Pleacă de la setul existent (~2000 tranzacții, `valoare_neta` invariant). Adaugă coloanele de input
`oras` și `data_scadentei` cu valori CORECTE peste tot (oraș aliniat la nomenclator, scadență = factură + termen plauzibil). Niciun flag încă.
*De ce:* baza trebuie să fie 100% curată ca să controlezi exact câte anomalii există.

**Pas D3 — Satelitul `CONTACTE` curat.**
Generează ~50 persoane de contact (FK `client_nume`), fiecare cu CNP VALID, coerent (sex/județ/dată/cifră de control toate corecte), `Data_Nasterii` = data din CNP.
*De ce separat:* CNP trăiește pe persoane, nu pe rândurile B2B (decizie V58).

**Pas D4 — Injecția controlată a anomaliilor (în ordinea LOCK).**
Plantează exact numerele din spec §6, marcând în paralel un registru intern (ce rând, ce anomalie) pentru verificare:
- C02.01 Orașe ~50 (mix scriere inconsecventă + oraș↔județ imposibil)
- C02.02 TVA ~35 (cotă validă ca număr, greșită fiscal pentru categorie)
- C02.03 Scadență ~25 (scadență < factură)
- C02.04 Zi nelucrătoare ~20 (sărbători legale + duminici)
- C02.05 CNP ~25/50 contacte (sex / județ / dată / cifră de control, pot coexista)
- ~10-15 rânduri cu anomalii MULTIPLE (intenționat, ca o celulă să poarte mai multe boli).
*De ce după curățare:* numai pe o bază curată poți garanta că totalul afectat = ~130 (~6.5%), nu mai mult.

**Pas D5 — Coloanele de semnalizare (formule, NU corecții).**
Adaugă pe `Vanzari`: `flag_oras`, `flag_tva`, `flag_scadenta`, `flag_zi`, `status_validare`, `motiv_anomalie`.
Pe `CONTACTE`: `flag_sex`, `flag_judet`, `flag_data`, `flag_control`, `status_validare`, `motiv_anomalie`.
Formule = cele din spec §7. Reguli: niciun flag nu rescrie valoarea originală (R-MET-1).

**Pas D6 — Reconciliere injecție ↔ semnalizare.**
COUNTIF pe fiecare flag = numărul plantat la D4. Dacă nu coincide → ai un fals pozitiv/negativ în formulă SAU în injecție. Se repară până la potrivire perfectă. *Acesta e gardul de calitate al fișierului.*

**Pas D7 — Foaia `_SEMNALIZARE` (livrabilul vizibil).**
Sinteza: extrage rândurile `status_validare="DE INVESTIGAT"`, grupate pe fenomen, ca raport de investigație. Plus CF aplicat (vezi spec §9). AF demonstrat pe `oras` (unique records) = materialul brut al nomenclatorului.

**Pas D8 — Validări de integritate.**
`valoare_neta` SUMĂ neschimbată față de setul de intrare (R-V02.14). Zero cifre business scurse. Foaia `Vanzari` are exact coloanele specificate. `_README` + `CONTROL_FINAL` păstrate/actualizate.

---

## 2. LISTA TUTUROR ARTEFACTELOR DE PRODUS

> Convenție de nume: identitatea nouă = „CONTROL". Fișierele vechi poartă „Marcare" și se
> REDENUMESC/SUPRASCRIU. Referința COPY+MODIFY = `c01/`.

**A. Date (sursă de adevăr a construcției)**
1. `c02/Date_MASTER-C02.xlsx` — rescris integral (8 foi: Vanzari, CONTACTE, 4 nomenclatoare, _SEMNALIZARE, _README/CONTROL_FINAL).

**B. HTML (4 canonice)**
2. `c02/HTML-Studiu-Excel-02-Control.html`
3. `c02/HTML-Editor-Studiu-Excel-02-Control.html`
4. `c02/HTML-Video-Excel-02-Control.html` (base64 inline)
5. `c02/HTML-Editor-Video-Excel-02-Control.html` (base64 inline)

**C. Film + Creativ**
6. `c02/FILM-Excel-02-Control.docx`
7. `c02/Creativ-Excel-02-Control.txt`
8. `c02/PROMPTURI-SLIDES-EXEC-C02.txt` (există — se aliniază la identitatea CONTROL)

**D. Imagini (`c02/assets/`)**
9. `hero-control.jpg` — hero dedicat (3:2 cinematic, prompt Banana, watermark Gemini eliminat).
10-15. `exec-stage-1..6.jpg` — 6 imagini exec-stage ale C02 (cele 6 etape).
16. `infografic-excel-02-control.jpg` (echivalent c01).

**E. Curățenie**
17. Ștergerea/redenumirea celor 5 fișiere vechi „Excel-02-Marcare" (HTML×4 + FILM + Creativ) după ce noile artefacte trec gate.

---

## 3. ORDINEA OPTIMĂ DE EXECUȚIE + DEPENDENȚE

> Regula lanțului: nimic „de afișare" (HTML/FILM) nu se construiește înainte ca SURSA pe care
> o descrie (Date_MASTER) să fie finală. Altfel HTML descrie un fișier care încă se schimbă = drift garantat.

```
FAZA 1 · DATE        Date_MASTER-C02 (D1→D8)          ──┐ blochează tot ce urmează
FAZA 2 · CREATIV     Creativ-Excel-02-Control          │ depinde de: structura finală a datelor
FAZA 3 · VIZUAL      hero + 6 exec-stage + infografic  │ depinde de: Creativ (prompturile vin din el)
FAZA 4 · HTML-Studiu HTML-Studiu                        │ depinde de: Date (anomalii reale) + assets
FAZA 5 · HTML rest   Editor-Studiu, Video, Editor-Video │ depinde de: HTML-Studiu (sursa de copy)
FAZA 6 · FILM        FILM-Excel-02-Control              │ depinde de: HTML (sincronizare 1:1 conținut)
FAZA 7 · GATE+CLEAN  gate_v20 + audit_sync + ștergere vechi Marcare
```

**Dependențe explicate:**
- **Date înainte de tot:** anomaliile, numerele, formulele trăiesc în Excel. HTML/FILM doar le povestesc. Dacă Date se schimbă după HTML, HTML minte. (R-V02.15: cifrele trăiesc în Excel.)
- **Creativ înainte de Vizual:** prompturile Banana pentru hero + exec-stage se scriu din Creativ (atmosfera, scena fiecărei etape). Fără Creativ, pozele n-au brief.
- **Vizual înainte de HTML:** HTML-Video/Editor-Video înglobează base64 inline; ai nevoie de imaginile finale, curățate de watermark, înainte de a le inline-ui.
- **HTML-Studiu prima, restul după:** Editor-Studiu/Video/Editor-Video derivă din HTML-Studiu (aceeași substanță, ambalaj diferit). Studiu = sursa de copy.
- **FILM ultimul (înainte de gate):** FILM trebuie să fie 1:1 cu conținutul HTML final. Construit înainte → desincronizare (lecția C07/C08).
- **Gate la final:** `gate_v20.py` + `audit_sync.py` validează canonic + editat. PASS obligatoriu înainte de ștergerea fișierelor vechi.

---

## 4. RISCURI DE IMPLEMENTARE (unde se rupe ceva)

| # | Risc | Unde apare | Semn de avertizare | Mitigare |
|---|---|---|---|---|
| R1 | **Contaminare T5 (prevenție)** | C02.01, la DV | DV prezentată ca „așa eviți pe viitor" / DV în cascadă oraș-după-județ | DV = pas final marginal, încadrat „formalizarea nomenclatorului aprobat". Cascada = doar mențiune-bonus „e T5", niciodată demonstrată (spec §DV). |
| R2 | **Contaminare C03 (motorul reclamă)** | C02.01 orașe, C02.05 CNP | apar „spații ascunse", „text vs număr", „lungime≠13", „Unicode invizibil" | Garda T1: C02 = greșit față de REALITATE (omul reclamă). Format/lungime/caractere invizibile = C03. CNP doar „arată perfect, totuși fals" (contradicție multi-câmp + cifră control). |
| R3 | **C02 repară în loc să semnaleze** | etapa 4 VERIFICARE, formule | apare o coloană `oras_corectat` / `cota_corecta` / ștergere de rânduri | R-MET-1: E4 CONFRUNTĂ/CUANTIFICĂ/MARCHEAZĂ. Output = `status_validare`+`motiv_anomalie`, NU corecție. Valorile sursă neatinse (S3). |
| R4 | **Ruperea identității (AHA)** | HTML/FILM copy | apare „validăm și corectăm" / „curățăm datele" / accent pe reparare | AHA LOCK „Valid nu înseamnă corect". C02 demonstrează falsul valid, nu îl repară. Numele etapelor E1-E6 din blueprint §3. |
| R5 | **Drift terminologic transversal** | numele etapei 4, phase-tags | „AUDIT" la E4 (= ADN C03), „RECALC" la E5 | R-TERM-1 (E4=„VERIFICAREA CORESPONDENȚEI"), R-TERM-2 (E5=„RECALCUL"). Detector le prinde. |
| R6 | **Cifre business scurse în HTML/FILM** | orice slot cu exemple | apar sume/valori reale din Vanzari | R-V02.15: doar referințe generice. Cifrele rămân în Excel. |
| R7 | **Desincronizare HTML↔FILM** | FAZA 6 | FILM povestește alte etape/anomalii decât HTML | FILM construit DUPĂ HTML, verificat 1:1. R-V58.filmname: titlul FILM conține stem-ul cover-title. |
| R8 | **Nume fișier nealiniat** | redenumire Marcare→Control | cover-title „CONTROL" dar fișier „Marcare" → detector filmname FAIL | Redenumire completă + aliniere titluri la „C02 CONTROL". |
| R9 | **Injecție anomalii necontrolată** | D4 | COUNTIF flag ≠ numărul plantat | Pas D6 reconciliere obligatoriu înainte de a trece la HTML. |
| R10 | **Suma neconservată** | D5/D8 | `valoare_neta` total diferă față de intrare | Semnalizarea adaugă DOAR coloane status; verificare numerică R-V02.14 la D8. |

---

## 5. PER ANOMALIE · CE TREBUIE PREGĂTIT ÎNAINTE DE IMPLEMENTARE

**C02.01 ORAȘE NEALINIATE**
- `tbl_Localitati` complet (oraș_oficial ↔ județ) pentru toate localitățile din set.
- Lista variantelor greșite plantate: scriere inconsecventă (Cluj / CJ / Cluj-Napoca / „Clum Napoca" typo) + oraș↔județ imposibil (Brașov / Constanța).
- Distribuție: ~50 rânduri, mix (a)+(b).
- Pregătit pentru AF: coloana `oras` populată ca să iasă nomenclatorul real prin „unique records".

**C02.02 TVA GREȘIT**
- `tbl_RegulriTVA` (categorie → cotă legală: Alimente 9%, Hardware 19%, Servicii 19% ...).
- Mapare categorie↔cotă corectă pe tot setul, apoi ~35 rânduri cu cotă validă ca număr dar greșită fiscal.
- Atenție: cota greșită = o cotă REALĂ (9/19/5), nu un număr aberant (aberantul ar fi structural = C01/C03).

**C02.03 SCADENȚĂ < FACTURĂ**
- Coloana `data_scadentei` populată corect (factură + termen) peste tot.
- ~25 rânduri cu scadență înaintea facturii, ambele date valide.
- Termenul de plată „normal" definit (ex. 30 zile) ca restul setului să fie coerent.

**C02.04 ZI NELUCRĂTOARE (NETWORKDAYS)**
- `tbl_SarbatoriLegale` cu sărbătorile anului setului (ex. 13.04.2026 = a 2-a zi de Paște).
- ~20 rânduri cu `data_factura` în sărbătoare legală sau duminică.
- Decizie ZILE LUCRĂTOARE: NETWORKDAYS.INTL cu masca de weekend + lista de sărbători.

**C02.05 CNP CONTRADICTORIU (iconic)**
- `tbl_CodJudetCNP` (cod → județ, inclusiv 40-46 București).
- Algoritmul cifrei de control (ponderi 2-7-9-1-4-6-3-5-8-2-7-9, mod 11, regula 10→1).
- ~50 contacte cu CNP valid coerent, din care ~25 cu cel puțin o contradicție: sex / județ / dată / cifră control (pot coexista).
- Registru intern: ce contact poartă ce tip de contradicție, pentru reconciliere.
- Anti-drift gata formulat: NU lungime≠13, NU caractere alfabetice (= C03).

---

## 6. MILESTONE-URI

| Milestone | Conținut | Criteriu de PASS (definition of done) |
|---|---|---|
| **M1 · DATE** | Date_MASTER-C02 (D1→D8) | 4 nomenclatoare + Vanzari + CONTACTE; COUNTIF flag = injecție (D6); suma conservată (D8) |
| **M2 · SEMNALIZARE** | foaia `_SEMNALIZARE` + CF + AF demonstrat | raport investigație pe fenomen; CF marchează, nu corectează; AF scoate nomenclatorul real |
| **M3 · CREATIV** | Creativ-Excel-02-Control + prompturi slides | 6 scene exec-stage + hero descrise; aliniat identității CONTROL |
| **M4 · VIZUAL** | hero + 6 exec-stage + infografic (assets) | 3:2 cinematic; watermark Gemini eliminat; pe disc în c02/assets |
| **M5 · HTML** | 4 HTML (Studiu→Editor-Studiu→Video→Editor-Video) | copy aliniat AHA LOCK; etape E1-E6 corecte; base64 inline pe Video |
| **M6 · FILM** | FILM-Excel-02-Control | 1:1 cu HTML; filmname aliniat |
| **M7 · GATE** | gate_v20 + audit_sync + curățare Marcare | PASS canonic+editat; ZERO DRIFT; fișiere vechi șterse; livrare HTML-Studiu către ARHITECT |

Drum critic: **M1 → M3 → M4 → M5 → M6 → M7** (M2 se face în interiorul M1/finalul lui Date). Blocajul cheie = M1: nimic vizibil nu pornește înainte ca Date să fie final.

---

## 7. VERDICT EXECUȚIE · PRIMA MUTARE OBLIGATORIE

**O singură acțiune acum: construiește `Date_MASTER-C02.xlsx`, începând cu Pasul D1 — cele 4 nomenclatoare de referință** (`tbl_Localitati`, `tbl_RegulriTVA`, `tbl_SarbatoriLegale`, `tbl_CodJudetCNP`).

**De ce exact aceasta și nimic altceva:**
- Sunt sursa de adevăr: definesc ce înseamnă „corect", deci condiționează și injecția anomaliilor (D4) și formulele de semnalizare (D5). Nu poți planta o abatere fără referința de la care abate.
- Sunt pe drumul critic (M1) care blochează tot restul (Creativ, Vizual, HTML, FILM).
- Sunt deterministe și verificabile: date factuale (geografie, fiscalitate, calendar, cod-județ), zero dependență de copy/identitate, zero risc de a redeschide arhitectura.

Tot ce urmează (Vanzari curat → CONTACTE → injecție → semnalizare → restul artefactelor) se construiește PESTE acest fundament, în ordinea din §1 și §3.

**PENDING aprobare ARHITECT** pentru a porni M1. La „start" execut D1.
