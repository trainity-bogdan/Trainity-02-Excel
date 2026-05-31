# T2_CHANGE_PROTOCOL.md · Protocol de modificare fără drift

> **REGULA DE AUR:** nicio modificare locală nu se aplică fără întrebarea:
> *„Ce poziții structurale echivalente sunt afectate în celelalte construcții?"*
> Acesta e protocolul care previne exact driftul din auditul T2 (fix-uri secvențiale
> nepropagate).

---

## CELE 7 ETAPE ALE ORICĂREI MODIFICĂRI

### 1. CHANGE REQUEST
Descrie: ce se schimbă, în ce construcție a fost observat, de ce. Tip: terminologic /
structural / pedagogic / metodologic / handoff / retoric / hero.

### 2. IMPACT ANALYSIS
Întrebări obligatorii:
- E o poziție structurală (apare în T2_POSITION_MATRIX)? DA → propagare obligatorie.
- E o regulă SACRĂ (T2_ARCHITECTURE_BIBLE)? DA → aprobare arhitect.
- E identitate locked (AHA/nume)? DA → aprobare arhitect.
- Atinge garda T2/T3? DA → audit advers.

### 3. POSITION MAPPING
Localizează poziția în T2_POSITION_MATRIX. Identifică echivalentul în C05, C06, C07, C08.
Dacă poziția NU e în matrice → e element local (vezi T2_DNA §10) → modificare punctuală OK.

### 4. TRANSVERSAL PROPAGATION
Aplici modificarea pe TOATE construcțiile unde poziția există, în aceeași pasă, NU
secvențial. (Lecția T2: fix-ul AUDIT→VERIFICARE aplicat doar la C07/C08 a creat split.)

### 5. DRIFT CHECK
Rulează T2_DRIFT_DETECTOR (checklist relevant + drift score). Confirmă uniformitate
transversală post-modificare.

### 6. RELEASE GATE
Treci gate-urile afectate (minim Gate 2/9 pentru terminologie, Gate 4 pentru metodologie).

### 7. APPROVAL
ARHITECT aprobă dacă: regulă sacră / identitate locked / decizie arhitecturală / Gate 10.
Altfel: motor + auditor.

---

## EXEMPLE CONCRETE (din istoric T2)

**Schimbare nume etapă** (ex. AUDIT→VERIFICARE):
- Poziție structurală DA → mapează E4 la toate 4 → aplică la toate care au „AUDIT" →
  drift check → Gate 2. *Greșeala făcută: aplicat doar la C07/C08, lăsat C05/C06.*

**Schimbare phase-tag** (ex. RECALC→RECALCUL):
- Poziție E5 → verifică toate 4 → C05 era „RECALC", restul „RECALCUL" → aliniază C05.

**Schimbare handoff** (ex. „Setul vine" → „Setul predat de"):
- Poziție PAS 01 → verifică tiparul la toate 4 → corectează abaterea (C06).

**Schimbare completion** (ex. scoate „auditabil"):
- Poziție completion-title → tipar „[Livrabil] validat" → aliniază C05.

**Schimbare prompt AI:**
- Poziție E2/E3 → verifică ambele prompturi la toate 4 → propagă formularea.

**Schimbare verificare** (ex. funcții E4):
- Poziție E4 → verifică dacă e variație acceptabilă (pe axă) sau drift → dacă C06
  construiește în loc să verifice = decizie arhitecturală, NU propagare mecanică.

---

## ANTI-PATTERN INTERZIS
„Am observat X în C06, repar doar C06." → INTERZIS dacă X e poziție structurală.
Orice fix de poziție = pasă transversală pe toate 4.
