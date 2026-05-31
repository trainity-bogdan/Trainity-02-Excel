# TRAINITY_RELEASE_GATE.md · Condiții de maturitate (tier-aware)

> O construcție nu intră în producție până nu trece gate-urile. Fiecare gate
> **referă reguli prin ID** (Bible) + checklist-uri (Detector) — nu le re-enunță.
> Verdict calitativ (nu scor). Două moduri (R-SEED-1): EXISTING TIER / TIER SEED.

---

## GATE-URI (5 reale, consolidate)

| Gate | Verifică (referință) | Aprobă | Fail → |
|---|---|---|---|
| **G1 · Structură** | R-STR-1/2/3/4, S4 · Detector ch.1 | motor (automat) | BLOCAT |
| **G2 · Terminologie + garda treptei** | R-TERM-* , R-NAME-1 + lista §TIER (R-TIER-PARAM) · Detector ch.2/8 | motor + auditor | BLOCAT |
| **G3 · Pedagogie + AI + Handoff** | R-PED-*, R-HAND-* · Detector ch.3/6/7 | auditor | remediere |
| **G4 · Metodologie** | R-MET-1/2/3 · Detector ch.4 | ARHITECT (decizie structurală) | decizie arhitecturală |
| **G5 · Cross-construction + Approval final** | uniformitate pe poziții (Position Matrix) + identitate (test cursant/manager) + AHA locked + hero dedicat · Detector ch.5/9 | ARHITECT | **N/A pe G5-cross în TIER SEED**; restul → nu se publică |

**Verdict global** = cel mai sever rezultat de gate (vezi Detector: MATUR / PASS CU
OBSERVAȚII / BLOCAT).

---

## MODUL TIER SEED (prima construcție a unei trepte)
- **G5-cross-construction = N/A** (nu există frate de comparat — R-SEED-2).
- G5-approval (identitate + AHA + hero) **rămâne activ**.
- G1-G4 rulează identic, cu lista de garda din §TIER nou-definit (R-TIER-PARAM).
- Output suplimentar: secțiunea §TIER nouă în Bible (aprobată) — vezi TIER SEED în OS.

---

## STAREA GATE-URILOR T2 (EXISTING TIER, azi)
| Gate | C05 | C06 | C07 | C08 |
|---|---|---|---|---|
| G1 Structură | PASS | PASS | PASS | PASS |
| G2 Terminologie | PASS | PASS | PASS | PASS |
| G3 Pedagogie/AI/Handoff | PASS | PASS | PASS | PASS |
| G4 Metodologie | PASS | **decizie** (E4 construiește) | PASS | PASS |
| G5 Cross + Approval | decizii deschise (E3 phase-tag) + pending DEZAMBIGUIZARE | | | |

**Verdict T2: PASS CU OBSERVAȚII.** Blocante = decizii arhitecturale (G4 C06, G5 E3,
dezambiguizare), nu bug-uri.
