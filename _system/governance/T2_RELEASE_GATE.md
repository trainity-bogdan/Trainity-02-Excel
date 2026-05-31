# T2_RELEASE_GATE.md · Condiții obligatorii de maturitate

> O construcție T2 NU intră în producție până nu trece toate cele 10 gate-uri.
> Format: criteriu · metodă · acceptat · respins · aprobă · consecință-fail.

---

## GATE 1 · STRUCTURĂ
- Criteriu: 6 etape · 18 pași · 5 fenomene · 8 verificări · 2 prompturi.
- Metodă: `audit_sync.py` + count regex.
- Acceptat: toate exacte. · Respins: orice abatere.
- Aprobă: automat (motor). · Fail → BLOCAT, se repară.

## GATE 2 · TERMINOLOGIE
- Criteriu: etapa 4 = VERIFICAREA; zero termeni T3/C03/C04 interziși; RECALCUL; zero em-dash.
- Metodă: T2_DRIFT_DETECTOR checklist 2 + 8.
- Acceptat: zero hituri. · Respins: orice contaminare.
- Aprobă: motor + auditor. · Fail → BLOCAT.

## GATE 3 · PEDAGOGIE
- Criteriu: E3 = Promptul 2; 2 prompturi ca interogare.
- Metodă: checklist 3. · Acceptat: type-tag E3 uniform. · Respins: E3 manual.
- Aprobă: auditor. · Fail → remediere.

## GATE 4 · METODOLOGIE
- Criteriu: E4 verifică (nu construiește); funcții de numărare/potrivire.
- Metodă: checklist 4 (verbe step-titles E4).
- Acceptat: verbe Confruntă/Verifică/Marchează. · Respins: Compune/Construiește/Calculează.
- Aprobă: ARHITECT (e decizie structurală). · Fail → decizie arhitecturală. *C06 azi: FAIL deschis.*

## GATE 5 · HANDOFF
- Criteriu: PAS 01 „Setul predat de C0(N-1)"; teaser „C0(N+1) deschide".
- Metodă: checklist 6. · Acceptat: tipar respectat. · Respins: „Setul vine cu...".
- Aprobă: auditor. · Fail → remediere.

## GATE 6 · VERIFICĂRI
- Criteriu: 8 carduri canonice; card 1 = CONTROL; card final = livrabil + valori sursă.
- Metodă: checklist 1 + 9. · Aprobă: motor. · Fail → remediere.

## GATE 7 · AI INTEGRATION
- Criteriu: 2 prompturi funcționale, formulate ca interogare, copiate în sheet profil.
- Metodă: checklist 7. · Aprobă: auditor. · Fail → remediere.

## GATE 8 · DRIFT SCORE
- Criteriu: scor ≥ 90 (matur) pentru release fără ticket; ≥ 80 cu ticket.
- Metodă: T2_DRIFT_DETECTOR formula.
- Acceptat: ≥80. · Respins: <80.
- Aprobă: ARHITECT. · Fail (<70) → BLOCAT.

## GATE 9 · CROSS-CONSTRUCTION CONSISTENCY
- Criteriu: fiecare poziție structurală uniformă pe toate 4 (sau marcată „variație
  acceptabilă"/„decizie" explicit).
- Metodă: T2_POSITION_MATRIX + detector transversal propus.
- Acceptat: zero `drift`/`contaminare` nemarcat. · Respins: drift transversal.
- Aprobă: ARHITECT. · Fail → propagare transversală (T2_CHANGE_PROTOCOL).

## GATE 10 · APPROVAL FINAL
- Criteriu: ARHITECT confirmă identitatea (test cursant 10s + test manager 30 zile) +
  AHA locked + hero dedicat prezent.
- Metodă: audit advers de identitate.
- Aprobă: ARHITECT (exclusiv). · Fail → nu se publică.

---

## STAREA GATE-URILOR T2 (azi)
| Gate | C05 | C06 | C07 | C08 |
|---|---|---|---|---|
| 1 Structură | PASS | PASS | PASS | PASS |
| 2 Terminologie | PASS | PASS | PASS | PASS |
| 3 Pedagogie | PASS | PASS | PASS | PASS |
| 4 Metodologie | PASS | **FAIL** (E4 construiește) | PASS | PASS |
| 5 Handoff | PASS | PASS | PASS | PASS |
| 6 Verificări | PASS | PASS | PASS | PASS |
| 7 AI | PASS | PASS | PASS | PASS |
| 8 Drift score | ~84 (treaptă) | | | |
| 9 Cross-consistency | decizii deschise: phase-tag E3 | | | |
| 10 Approval | pending DEZAMBIGUIZARE (payoff/WOW/motto) | | | |

**Concluzie:** T2 = PASS CU OBSERVAȚII. Blocante reale: Gate 4 (C06), Gate 9 (E3
phase-tag), Gate 10 (dezambiguizare). Toate = decizii arhitecturale, nu bug-uri.
