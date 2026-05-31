# T2_DRIFT_DETECTOR.md · Detector de abateri (reguli → verificări)

> Transformă regulile din Bible în verificări concrete. O parte sunt deja
> automatizabile (audit_sync.py); restul = checklist manual + propunere de detector.
> Fiecare verificare: ce · unde · cum detectezi · severitate · exemplu · acțiune ·
> propagare transversală (DA/NU).

---

## CHECKLIST 1 · CONSISTENȚĂ STRUCTURALĂ
- [ ] 6 etape (regex `stage-label">ETAPA [1-6]`). Severitate CRITICĂ. Propagare: N/A (per fișier).
- [ ] 18 pași (count `step-marker">PAS`). CRITICĂ.
- [ ] 5 fenomene SCENA (count `anomaly-num`). MEDIE.
- [ ] 8 verificări finale. MEDIE.
- [ ] 2 prompturi (count `prompt-label`). MEDIE.
- [ ] nav-brand absent (R-V03.73, deja automat). MEDIE.

## CHECKLIST 2 · CONSISTENȚĂ TERMINOLOGICĂ *(necesită detector transversal nou)*
- [ ] Etapa 4 = „VERIFICAREA", niciodată „AUDIT". Cum: `ETAPA 4 · ([^<]*)` → trebuie să înceapă cu „VERIFICAREA". CRITICĂ. Propagare: **DA** (toate 4).
- [ ] phase-tag E5 = „RECALCUL" exact. MEDIE. Propagare DA.
- [ ] Zero termeni T3 interziși (XLOOKUP/LOOKUP-aducere, conectat/conexiune, Data Model în corp, BI-ready, trend, KPI, dominant). CRITICĂ. Propagare DA.
- [ ] Zero ecou „sumă" (Suma rămâne/martorul de sumă). MEDIE. Propagare DA.
- [ ] Zero em/en-dash (R-V03.72, automat). MEDIE.

## CHECKLIST 3 · CONSISTENȚĂ PEDAGOGICĂ
- [ ] type-tag E3 = „Promptul 2" în toate 4. MAJORĂ. Propagare **DA**.
- [ ] 2 prompturi prezente, formulate ca interogare. MEDIE.

## CHECKLIST 4 · CONSISTENȚĂ METODOLOGICĂ
- [ ] Pașii E4 verifică (verbe: Confruntă/Verifică/Marchează), NU construiesc (Compune/Construiește/Calculează). MAJORĂ. *C06 încalcă azi — decizie deschisă.*
- [ ] Funcții E4 din familia numărare/potrivire. MEDIE.

## CHECKLIST 5 · CONSISTENȚĂ DE EXPERIENȚĂ CURSANT
- [ ] Test cursant 10s: obiect/întrebare/AHA distincte între cele 4 (R-V03.74). MAJORĂ.
- [ ] Ritm uniform (3 pași/etapă). MEDIE.

## CHECKLIST 6 · CONSISTENȚĂ DE HANDOFF
- [ ] PAS 01 = „Setul predat de C0(N-1)". MAJORĂ. Propagare DA.
- [ ] Teaser = „C0(N+1) deschide...". MEDIE.

## CHECKLIST 7 · CONSISTENȚĂ AI-DRIVEN
- [ ] E2 + E3 ancorate pe Promptul 1 / Promptul 2. MEDIE.
- [ ] Fără pași 100% manuali prezentați ca normă (filozofie 2015). MEDIE.

## CHECKLIST 8 · CONTAMINĂRI DIN TREPTE ANTERIOARE
- [ ] Fără „AUDIT" (C03), fără ecou „sumă/normalizare" (C04), fără „profil numeric" (C06-vechi). CRITICĂ. Propagare DA.

## CHECKLIST 9 · VARIAȚII PHASE-TAG
- [ ] phase-tag pe poziție echivalentă identic între cele 4 (excepție E3 = decizie). MEDIE. Propagare DA.

## CHECKLIST 10 · VARIAȚII COMPLETION
- [ ] completion-title = „[Livrabil] validat", fără adjective extra. MEDIE. Propagare DA.

---

## DRIFT SCORE (0-100)

**Formula:** pornești de la 100 și scazi:
- Fiecare încălcare CRITICĂ: **−15**
- Fiecare încălcare MAJORĂ: **−8**
- Fiecare încălcare MEDIE: **−3**
- Fiecare „decizie arhitecturală" deschisă (nerezolvată): **−5**
- Fiecare variație acceptabilă: **−0** (nu penalizează)

Scorul se calculează **per treaptă** (suma abaterilor pe toate construcțiile, pe poziții
structurale), NU per fișier — pentru a prinde driftul transversal.

**Praguri:**
| Scor | Stare | Acțiune |
|---|---|---|
| 90-100 | MATUR | intră în producție |
| 80-89 | PASS CU OBSERVAȚII | producție + ticket de remediere |
| 70-79 | RISC MAJOR | nu intră până nu se remediază criticele |
| <70 | BLOCAT | nu intră în producție |

**Stare actuală T2 (estimare, post-uniformizare):**
- Critice rezolvate (AUDIT, XLOOKUP-aducere, terminologie). 
- Decizii deschise: phase-tag E3 Power Query (−5), C06 E4 construire (−5).
- Drift retoric payoff/WOW/motto (3× MEDIE-MAJORĂ, intră în DEZAMBIGUIZARE).
- **Scor estimat: ~84/100 → PASS CU OBSERVAȚII** (deciziile deschise + dezambiguizarea trag în jos).

---

## DETECTOR TRANSVERSAL PROPUS (gap de instrument)

`audit_sync.py` verifică drift **per fișier**. Lipsește un detector care compară
**aceeași poziție structurală între cele 4 construcții** și semnalează când diferă.
Propunere: `cross_consistency.py` care extrage {nume-etapă, phase-tag, type-tag,
handoff, completion} pentru fiecare poziție × construcție și raportează non-uniformitatea.
Acesta ar fi prins toate drifturile din auditul T2 (AUDIT/VERIFICARE, RECALC/RECALCUL)
ÎNAINTE să apară. **Necesită aprobare arhitect pentru implementare (cod nou).**
