# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-008

## MANDAT
Cuplare tier_guard_t3 în gate_v20, guarded strict pe T3, înainte de implementarea C09.

## CONTEXT
BRAIN-007 a implementat garda tehnică T3 ca modul standalone:
- _system/generatoare/tier_guard_t3.py
- self-test 10/10 PASS
- T2 real C05-C08 PASS
- audit_sync ZERO DRIFT neatins
- zero artefacte de construcție atinse

Problema rămasă:
Detectorul T3 nu este încă rulat automat de gate_v20 la livrare.

Decizie BRAIN:
Cuplăm tier_guard_t3 în gate_v20 ACUM, înainte de implementarea C09.
Motiv: C09 trebuie să intre în lucru cu garda tehnică activă în pipeline, nu doar standalone.

## OBIECTIV
Integrează _system/generatoare/tier_guard_t3.py în gate_v20.py, cu activare strictă doar pentru construcțiile T3:
- C09
- C10
- C11
- C12

Nu modifica logica T1/T2.
Nu relaxa T2.
Nu schimba verdictul T1/T2.
Nu implementa C09.

## REGULĂ DE INTEGRARE
Integrarea trebuie să fie safe și izolată:

1. Pentru NN 09-12:
   - gate_v20 rulează și tier_guard_t3
   - FAIL blocant în tier_guard_t3 trebuie să blocheze gate-ul
   - WARNING trebuie raportat clar, fără să fie ascuns

2. Pentru NN 01-08:
   - gate_v20 trebuie să rămână neschimbat ca verdict
   - tier_guard_t3 nu trebuie să blocheze nimic
   - nu introduce false-positive pe T1/T2

3. Pentru folder lipsă:
   - comportamentul trebuie să fie curat
   - nu produce crash
   - raportează N/A sau skip controlat

## CE TREBUIE SĂ FACI

### 1. Citește codul existent
Citește:
- _system/generatoare/gate_v20.py
- _system/generatoare/tier_guard_t3.py
- _system/generatoare/audit_sync.py, doar pentru stil de raportare dacă e util

### 2. Integrează minimal
Adaugă apelul tier_guard_t3 în gate_v20 cu minimul de modificări necesare.

Preferință:
- import / funcție internă dacă modulul are API clar
- subprocess doar dacă API-ul existent nu permite import curat

Nu rescrie gate_v20.
Nu schimba regulile existente dacă nu este strict necesar.

### 3. Păstrează separarea
Detectorul T3 rămâne modul separat.
gate_v20 doar îl apelează pentru NN 09-12.

### 4. Testează regresia
Rulează verificări pe construcții existente:
- cel puțin o construcție T1
- cel puțin o construcție T2
- preferabil C05-C08, dacă timpul permite

Scop:
- verdictul T1/T2 nu trebuie afectat de integrarea T3.

### 5. Testează T3 pe fixturi / self-test
Rulează:
- tier_guard_t3.py --self-test
- gate_v20 cu scenariu T3 dacă există o metodă sigură fără a genera C09

Dacă nu există artefacte C09-C12, explică N/A și demonstrează prin self-test.

## FIȘIERE PERMISE LA MODIFICARE
Ai voie să modifici doar:
- _system/generatoare/gate_v20.py
- _system/generatoare/tier_guard_t3.py, doar dacă este necesar pentru API / integrare
- fișiere de test / fixtures din _system, dacă există și sunt necesare
- CLAUDE-TO-BRAIN.md

## FIȘIERE INTERZISE LA MODIFICARE
Nu modifica:
- c01/** până la c12/**
- orice HTML
- orice FILM
- orice xlsx
- orice imagine
- governance / Bible
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- STARE-CURENTA.md, dacă nu este absolut necesar
- README.md
- CLAUDE.md

## CRITERII DE PASS
Mandatul trece doar dacă:

1. tier_guard_t3 este cuplat în gate_v20 pentru NN 09-12.
2. gate_v20 nu rulează T3 guard blocant pentru NN 01-08.
3. self-test tier_guard_t3 rămâne PASS.
4. cel puțin o verificare T1/T2 confirmă zero regresie.
5. nu s-au modificat artefacte c01-c12.
6. raportul explică exact cum se vede rezultatul în gate_v20.

## LIVRABIL
Scrie raportul complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere modificate
5. Cum ai integrat tier_guard_t3 în gate_v20
6. Cum este limitată integrarea la NN 09-12
7. Cum ai protejat NN 01-08
8. Teste rulate
9. Rezultate PASS / WARNING / FAIL
10. Probleme rămase
11. Decizii cerute de la BRAIN
12. Commit / status Git

## MANDAT CURENT
Execută BRAIN-008.
Cuplează garda tehnică T3 în gate_v20.
Zero implementare C09.
