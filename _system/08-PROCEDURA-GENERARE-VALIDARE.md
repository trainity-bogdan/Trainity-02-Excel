# Procedura de generare + validare a construcțiilor (V43)

Document creat după controlul complet C06: prevenire a clonării de conținut
între construcții (drift narativ). OBLIGATORIU înainte de orice livrare CNN.

---

## 0. De ce există acest document

**Cauza reală a bug-urilor de tip „conținut de la altă lecție":**
generarea prin COPY+MODIFY cu înlocuiri de string prinde DOAR zonele pe care
le anticipează motorul. Orice zonă narativă nemapată rămâne moștenită literal
de la construcția-sursă. Empiric (V42-V43):
- C05 inv-list = clonă C01 (prins V42, R-V03.69).
- C03/C05 `exec-emotion` = clonă C01; C05 `exec-phrase` = clonă C01 (prins V43, R-V03.71).
- C06 a moștenit toate clonele de la C05.

Gate-urile nu prindeau pentru că verificau structură + 3 zone din Studiu, NU
zonele de conținut din Video.

**Principiul nou:** o construcție = un MANIFEST de conținut complet + o
matriță. Generarea = injectare manifest în matriță. Validarea = niciun slot
de conținut nu coincide cu altă construcție (exceptând zonele de brand).

---

## 1. Fișiere reper confirmate

| Rol | Cale | Notă |
|---|---|---|
| Matriță structură (HTML) | `_template/` | C01 fork; sursa pentru structură + JS + CSS |
| Referință axă T2 narativă | `c05/` (CLASIFICARE) | cea mai apropiată soră T2 (doar ca model de TON, nu de conținut) |
| Schema date | `_system/referinte/` | Date_MASTER-initial + IDENTITATE-TEHNICA + SCHEMA-MASTER |

ATENȚIE: `c05` se folosește ca model de TON, NU se copiază conținutul lui.
Fiecare slot din manifest se rescrie pe axa construcției noi.

---

## 2. Manifestul de conținut (toate sloturile construcție-specifice)

Înainte de generare, motorul COMPLETEAZĂ explicit fiecare slot de mai jos.
Niciun slot nu rămâne moștenit. Grupate pe machetă.

### Comun (toate 4 machete)
- identitate: cod, nume_hero, slug, meta_treaptă (bold pe curentă), footer,
  topbar, localStorage, next_cod/next_title, title tag
- intriga (cover-subtitle / hero hook + twist) — atenție la acord gramatical
  (ex. „cifre" → „le", „dicționar" → „îl")
- mantra, motto

### Studiu + Editor-Studiu
- cover-title, exec-hero-label, exec-hero-sharp
- section-marker (x2)
- stage-label (x6), stage-quote (x6)
- step-title (x18), step-action (x18)
- prompt-label (x2), prompt-text (x2)
- inv-item-label (x6), inv-item-desc (x6)         ← R-V03.69
- anomaly-title (x5), anomaly-desc (x5)            ← R-V03.69
- final-label (x8), final-text (x8)               ← R-V03.69
- payoff-line, payoff-motto
- next-label/title/desc

### Video + Editor-Video
- hero-prelabel, hero-hook (lead + twist), hero-sub  ← R-V03.71 (hero-sub)
- exec-title (x6) = REALITATE..CONFIRMARE  [BRAND, NU se schimbă]
- exec-label (x6) = Etapa 01..06           [GENERIC, NU se schimbă]
- exec-emotion (x6)                         ← R-V03.71 (CONSTRUCȚIE-SPECIFIC)
- exec-phrase (x6)                          ← R-V03.71 (CONSTRUCȚIE-SPECIFIC)
- FLOW narațiune (x18: num/title)           ← construcție-specific
- verify-title / verify-sub                 [în mare generic]
- conclusion-title-yellow = „Construcția NN" ← atenție: număr bare, nu cod CNN
- exec-closing-motto = motto brand          [BRAND, identic în toate]

### Date (Date_MASTER-CNN.xlsx)
- sheet-uri de analiză specifice axei + CONTROL_FINAL (sumă conservată)

---

## 3. Zone de BRAND (au voie să fie identice între construcții)

Detectorii NU le verifică (whitelist intenționat):
- exec-title (REALITATE / INVESTIGAȚIE / TRANSFORMARE / VERIFICARE /
  STABILIZARE / CONFIRMARE)
- exec-label (Etapa 01..06)
- motto de brand de închidere („Mai întâi structura. Apoi orice.")
- mantra T2 partajată („Nu privim tabelul. Îl interogăm.")
- etichete UI (butoane, panel-label, toast, modal)

---

## 4. Procedura de generare (pas cu pas)

1. `pre_generation_check.py NN` → 3/3 PASS (SPEC înghețat + IDENTITATE + FENOMENE vs asset).
2. Completează MANIFESTUL (secțiunea 2) integral, pe axa construcției.
3. Copiază machetele din matriță/soră și INJECTEAZĂ fiecare slot din manifest.
   Niciun slot nemapat.
4. Generează Date_MASTER-CNN.xlsx (sumă conservată DELTA 0).
5. Copiază assets/ (placeholder) sau generează Banana 2 dedicat.

## 5. Pipeline de validare (TOATE trebuie PASS înainte de livrare)

| Gate | Comandă | Ce verifică |
|---|---|---|
| 1 | `pre_generation_check.py NN` | SPEC + identitate + fenomene reale |
| 2 | `gate_v20.py NN cNN/ c{NN-1}/` | identitate HTML, brand, cross-contaminare, date |
| 3 | `audit_sync.py` | 10 detectori × toate cNN, ZERO DRIFT (incl. R-V03.69 Studiu + R-V03.71 Video) |
| 4 | scan leak-markeri | zero termeni de pe altă axă (vezi mai jos) |

**Gate 4 (scan manual leak-markeri)** — grep pe machetele noi pentru:
- termeni de pe alte axe (ex. la T2-cantitativ: zero „dicționar/etichetă/
  cardinalitate/frecvențe" = teritoriu C05 calitativ);
- markeri din C01 („Arată ca tabel", „nu era unul", „reconstruit infrastructura");
- număr bare al altei construcții („Construcția 0X" ≠ NN).

## 6. Verdict de livrare

Livrare DOAR dacă: Gate1 ∧ Gate2(sau paritate documentată) ∧ Gate3 ZERO DRIFT
∧ Gate4 zero leak. Altfel: BLOCAJ + raport.

---

## 8. Workflow FILM-CA-SURSĂ (V43) — sursa de adevăr textuală

**Principiu:** FILM-ul (`.docx`) este SURSA DE ADEVĂR pentru toate textele
narative ale unei construcții. ARHITECT rafinează textele în FILM (mantre,
intrigi, fraze exec etc.) pana la ~90% final, apoi le propag in toate cele 4
machete. In editabile raman doar rafinari fine, nu rescrieri.

**De ce:** editarea directa in 4 machete (x HTML mari, base64) e lenta si
predispusa la desincronizare. Un singur document sursa = un singur loc de
adevar + propagare deterministica + verificare round-trip.

### 8.1 FILM conține (manifestul textual, în ordinea din document)
- IDENTITATE CINEMATICĂ: INTRIGA (HOOK), MIZA, MANTRA, WOW (PAYOFF), MOTTO
- **SLIDES EXECUTIVE · SHOW FINAL VIDEO** (NOU V43, plasat imediat după MOTTO
  pentru acces rapid la rafinare, după blocul de identitate): cele 6 slide-uri
  exec, fiecare cu STARE (exec-emotion) + FRAZĂ DE IMPACT (exec-phrase)
- DESCHIDERE · DE CE CNN
- ROLURI · CINE FACE CE
- SCENA REALĂ · fenomene (lista axei)
- CELE 6 ETAPE · SCRIPT VIDEO (per etapă: OBIECTIV, STARE, VOCEA TRAINERULUI,
  DEMONSTRAȚIA, INTERVENȚIA AI, MOMENT DE CONTROL, REVEAL, TRANZIȚIE)
- FINAL · SEMNĂTURĂ

Secțiunile de rafinare creativă (INTRIGA, MIZA, MANTRA, WOW, MOTTO, urmate de
SLIDES EXECUTIVE) sunt grupate în partea de sus a FILM-ului. ARHITECT le
rafinează acolo; urmează apoi un rând de rafinări fine direct în editoarele
vizuale.

### 8.2 Maparea FILM → machete (deterministă, verificabilă)
| Câmp în FILM | Slot(uri) în machete |
|---|---|
| INTRIGA (HOOK) | Studiu `cover-subtitle`; Video `hero-hook` (lead+twist) — cu acord gramatical |
| MANTRA | Studiu `mantra-band-main`; Video `mantra` |
| WOW (PAYOFF) | Studiu `payoff` accent; Video `accent` |
| MOTTO | Studiu `payoff-motto`/motto construcție |
| SLIDE EXEC N · STARE | Video + Editor-Video `exec-emotion` [N] |
| SLIDE EXEC N · FRAZĂ DE IMPACT | Video + Editor-Video `exec-phrase` [N] |
| ETAPA N · VOCEA TRAINERULUI | Video FLOW / narațiune etapă [N] |
| SCENA REALĂ fenomene | Studiu `inv-item`/`anomaly` (după caz) |

### 8.3 Pașii workflow-ului
1. ARHITECT deschide FILM-ul construcției, rafinează textele (inclusiv
   secțiunea SLIDES EXECUTIVE).
2. ARHITECT uploadează FILM-ul modificat.
3. Motor PARSEAZĂ FILM-ul pe secțiuni etichetate și extrage fiecare câmp.
4. Motor PROPAGĂ fiecare câmp în slotul mapat, în toate cele 4 machete
   (Studiu, Editor-Studiu, Video, Editor-Video), cu acord gramatical.
5. Motor rulează **verificarea round-trip FILM↔machete**: re-extrage fiecare
   câmp din fiecare machetă și confirmă că == valoarea din FILM. Orice
   nepotrivire = BLOCAJ + raport.
6. Motor rulează pipeline-ul de 4 gate-uri (secțiunea 5).
7. ARHITECT face doar rafinări fine în editabile, dacă mai e nevoie.

### 8.4 Reguli de fortificare (nenegociabile)
- **FILM = singura sursă** pentru câmpurile mapate. Nu se editează direct în
  machete un câmp care există în FILM (s-ar desincroniza). Modificarea pleacă
  MEREU din FILM → propagare.
- **Completitudine FILM:** înainte de propagare, FILM trebuie să conțină
  TOATE secțiunile din 8.1. Lipsă secțiune = BLOCAJ.
- **Round-trip obligatoriu:** livrare doar dacă fiecare câmp din FILM apare
  identic în toate machetele mapate (verificare automată).
- **Idempotență:** re-propagarea aceluiași FILM nemodificat produce zero
  diferențe (semn că maparea e completă și corectă).

---

## 7. Lecția durabilă (L162)

Detectorii de coerență trebuie să acopere TOATE machetele (Studiu + Video +
companion editare), nu doar Studiu. Orice zonă de conținut construcție-specific
trebuie să aibă un detector de anti-clonă pe tuplu complet. R-V03.71 a extins
acoperirea pe Video; orice machetă/zonă nouă de conținut primește detector la
introducere.
