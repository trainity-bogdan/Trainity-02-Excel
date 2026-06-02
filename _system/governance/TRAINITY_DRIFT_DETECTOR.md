# TRAINITY_DRIFT_DETECTOR.md · Evaluează abaterile (tier-aware)

> Verifică abaterile de la reguli. **Nu enunță reguli** — le REFERĂ prin ID din
> `TRAINITY_ARCHITECTURE_BIBLE`. Verdict **calitativ** (nu scor numeric).
> Două moduri (R-SEED-1): **EXISTING TIER** / **TIER SEED**.

---

## MODURI DE RULARE

| | EXISTING TIER (≥2 construcții) | TIER SEED (prima construcție) |
|---|---|---|
| Checklist-uri SHARED | toate | toate |
| Cross-construction (ch. 9) | DA | **N/A** |
| Lista de contaminare | a treptei curente (§TIER) | a treptei curente (§TIER) |
| DNA / Position Matrix | există | **nu există încă** (R-SEED-2) |

**Parametru obligatoriu la rulare:** `tier` (T2/T3/T4/T5). Lista de „termeni interziși" se
ia din §TIER al treptei curente (R-TIER-PARAM) — NU hardcodată. *Ce e contaminare în T2 e
competență în T3.*

---

## CHECKLIST-URI (fiecare referă regula prin ID, nu o re-enunță)

**1 · Structural** → R-STR-1, R-STR-2, R-STR-3, R-STR-4, S4. *(6/18/5/8/2; automat via audit_sync.)*
**2 · Terminologic** → R-TERM-1, R-TERM-2, R-TERM-5, R-TERM-6, R-NAME-1. *(+ lista §TIER curentă.)*
**3 · Pedagogic** → R-PED-1, R-PED-2.
**4 · Metodologic** → R-MET-1, R-MET-2.
**5 · Experiență cursant** → test cursant 10s (R-V03.74); ritm uniform (R-STR-2).
**6 · Handoff** → R-HAND-1, R-HAND-2, R-HAND-3.
**7 · AI-driven** → R-PED-1, R-PED-2, R-PED-3.
**8 · Contaminare trepte** → garda §TIER curentă (anterioare + următoare). *tier-aware.*
**9 · Cross-construction** → uniformitate pe poziții (Position Matrix). **N/A în TIER SEED.**
**10 · Phase-tag / completion** → R-PHASE-1, R-PHASE-2, R-COMP-1.

---

## VERDICT (calitativ — fără scor numeric)

Verdictul se derivă din severitatea regulilor încălcate (din Bible), NU dintr-un scor:

| Verdict | Condiție |
|---|---|
| **MATUR** | zero încălcări CRITICE și MAJORE; max câteva MEDII documentate |
| **PASS CU OBSERVAȚII** | zero CRITICE; ≥1 MAJORĂ sau decizie arhitecturală deschisă |
| **BLOCAT** | ≥1 încălcare CRITICĂ neremediată |

**Decizii arhitecturale deschise** NU sunt încălcări — se listează separat, nu blochează
automat, dar se semnalează la Gate.

**Stare actuală T2 (EXISTING TIER):** zero CRITICE; deschise: R-MET-1 (C06 E4), R-PHASE-2
(E3 Power Query), backlog DEZAMBIGUIZARE. → **PASS CU OBSERVAȚII.**

---

## DETECTOR TRANSVERSAL (instrument)
`audit_sync.py` verifică drift **per fișier** (structural, terminologic automat).
Checklist 9 (cross-construction, uniformitate pe poziții) e azi **manual** prin
Position Matrix. Un `cross_consistency.py` automat = propunere deschisă (decizie
arhitect). Până atunci, ch.9 se rulează manual în mod EXISTING TIER.
