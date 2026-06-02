# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-009

## MANDAT
AUDIT T3 FINAL înainte de implementarea C09.

## CONTEXT
BRAIN-008 este DONE. Garda T3 a fost cuplată în gate_v20, guarded strict pe NN 09-12.

Starea curentă:
- T3 arhitectură = LOCK
- T3 governance = LOCK
- T3 detector = LOCK
- T3 gate = LOCK
- C09 nu este implementată încă

Înainte de implementarea C09 vrem un audit final, ostil, al întregii trepte T3.

## OBIECTIV
Audit arhitectural final pentru T3, cap-coadă.

Nu implementa C09.
Nu genera HTML.
Nu genera FILM.
Nu genera xlsx.
Nu modifica artefacte.
Nu modifica governance.
Nu modifica detector.
Nu modifica gate.

Audit numai.

## DOCUMENTE DE CITIT
Citește și folosește ca surse:
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/blueprints/BLUEPRINT-C09-RELATII.md
- CLAUDE-TO-BRAIN.md, rapoartele BRAIN-005, BRAIN-006, BRAIN-007, BRAIN-008 dacă sunt disponibile în istoric/git
- _system/generatoare/tier_guard_t3.py
- _system/generatoare/gate_v20.py

## AUDIT OBLIGATORIU
Atacă T3 ca auditor ostil.

Nu presupune că arhitectura este corectă.
Încearcă să o spargi.
Caută:
- redundanțe
- suprapuneri
- contaminări
- verbe greșite
- handoff-uri slabe
- construcții care pot fi eliminate
- zone în care cursantul nu percepe diferența
- zone în care un director non-Excel nu înțelege de ce există 4 construcții separate

## TREAPTA AUDITATĂ
T3 = ANALIZĂ / INTERPRETARE

C09 RELAȚII
C10 MĂSURI
C11 COMPARAȚII
C12 INTERPRETARE

Lanțul declarat:
C08 hartă descriptivă → C09 model interogabil → C10 măsură stabilă → C11 clasament / diferență → C12 cauză / insight verbal → T4 raportare vizuală

## TESTE SPECIFICE

### 1. TEST IDENTITATE
Pentru fiecare C09-C12, verifică dacă identitatea este clară, memorabilă și imposibil de confundat.

Întrebări:
- Care este verbul real al construcției?
- Care este obiectul real al construcției?
- Care este promisiunea concretă?
- Poate fi explicată în 30 secunde?

### 2. TEST MEMORABILITATE
Verifică dacă fiecare construcție are o formulă memorabilă, nu doar corectă tehnic.

Caută formule slabe, prea academice, prea tehnice, prea apropiate între ele.

### 3. TEST HANDOFF
Verifică fiecare trecere:
- C08 → C09
- C09 → C10
- C10 → C11
- C11 → C12
- C12 → T4

Pentru fiecare răspunde:
- ce predă construcția anterioară?
- ce primește construcția următoare?
- ce se rupe dacă handoff-ul este slab?

### 4. TEST CONTAMINARE
Verifică:
- C09 intră în C10?
- C10 intră în C11?
- C11 intră în C12?
- C12 intră în T4?
- C12 intră în T5?
- T3 reia T2?

### 5. TEST ELIMINARE CONSTRUCȚIE
Pentru fiecare construcție, simulează eliminarea:
- dacă elimin C09, ce se rupe?
- dacă elimin C10, ce se rupe?
- dacă elimin C11, ce se rupe?
- dacă elimin C12, ce se rupe?

Dacă o construcție poate fi eliminată fără pierdere majoră, marchează FAIL.

### 6. TEST DIRECTOR NON-EXCEL
Imaginează-ți că explici T3 unui director non-Excel.

Poate înțelege diferența dintre:
- relații
- măsuri
- comparații
- interpretare

fără jargon Excel?

Dacă nu, marchează WARNING și propune o formulare mai bună.

### 7. TEST SCALARE T4/T5
Verifică dacă T3 se oprește unde trebuie:
- T3 produce răspunsul
- T4 îl face vizibil
- T5 îl pune în acțiune

Caută orice element din T3 care forțează prea devreme vizualizarea, raportarea, decizia sau automatizarea.

## AXE DE AUDIT DETALIAT

### C09 vs C10
- C09 este clar despre relații?
- C10 este clar despre măsuri?
- C09 intră prea mult în măsurare?
- C10 începe prea târziu?
- Granița model vs măsură este suficient de clară?

### C10 vs C11
- C10 este suficient de puternic separat?
- Sau este doar o etapă tehnică înainte de comparații?
- C10 are miză de business suficientă?
- Diferența dintre măsură și clasament este clară?

### C11 vs C12
- C11 spune „care".
- C12 spune „de ce".
- Este linia suficient de dură?
- C12 poate deveni prea ușor raportare sau recomandare?

### T3 vs T4
- Există dashboard / raport / vizualizare publicabilă infiltrată în T3?
- Dacă da, unde?

### T3 vs T5
- Există alertă / acțiune / recomandare executată / decizie automată infiltrată în T3?
- Dacă da, unde?

## VERIFICARE DETECTOR / GATE
Verifică logic, fără să modifici codul:
- dacă tier_guard_t3 acoperă riscurile reale identificate
- dacă gate_v20 activează garda la momentul potrivit
- dacă există riscuri care nu sunt prinse mecanic
- dacă sunt reguli prea dure care ar putea bloca inutil C09

## LIVRABIL
Scrie raport complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Verdict global T3: PASS / WARNING / FAIL
5. Audit identitate C09-C12
6. Audit memorabilitate C09-C12
7. Audit handoff C08 → C09 → C10 → C11 → C12 → T4
8. Audit contaminare T2/T3/T4/T5
9. Audit eliminare construcții
10. Audit director non-Excel
11. Audit detector / gate
12. Probleme critice
13. Probleme warning
14. Ce trebuie schimbat înainte de C09
15. Este T3 gata de implementare?
16. Următorul mandat recomandat
17. Commit / status Git

## RESTRICȚII
Poți modifica doar CLAUDE-TO-BRAIN.md.

Nu modifica:
- BRAIN-TO-CLAUDE.md
- c01/** până la c12/**
- orice HTML
- orice FILM
- orice xlsx
- orice imagine
- governance / Bible
- 06-MAP
- doc 12 T3
- detector
- gate
- README.md
- CLAUDE.md
- STARE-CURENTA.md

## MANDAT CURENT
Execută BRAIN-009.
AUDIT T3 FINAL.
Audit numai.
Zero implementare C09.
