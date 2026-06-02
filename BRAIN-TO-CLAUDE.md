# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-007

## MANDAT
Implementare gardă tehnică T3 în detector / gate, înainte de implementarea C09.

## CONTEXT
BRAIN-006 a înghețat T3 cap-coadă în governance.

Rezultat BRAIN-006:
- Bible §T3 conține C09-C12 complet.
- C10 WARNING a fost rezolvat: motto = măsoară, verb de construcție = a defini.
- C12 rămâne INTERPRETARE / „de ce"; What-if a fost retras din identitate.
- 06-MAP a fost realiniat.
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md a fost creat.
- T3/T4/T5 au granițe locked.
- Zero artefacte C01-C12 au fost modificate.

Problema rămasă importantă:
Gărzile T3 sunt acum documentare, dar nu sunt încă verificate mecanic în detector / gate.
Înainte de implementarea C09, vrem ca sistemul să poată detecta mecanic contaminările T3.

## OBIECTIV
Adaugă sau actualizează verificările tehnice pentru T3, astfel încât C09-C12 să fie validate tier-aware.

Nu implementa C09.
Nu genera HTML.
Nu genera FILM.
Nu genera xlsx.
Nu modifica artefacte C01-C12.

Acest mandat este tehnic / sistemic: detector + gate + eventual teste.

## DOCUMENTE DE CITIT
Citește înainte:
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- CLAUDE.md
- scripturile existente de verificare din _system/generatoare/

## CE TREBUIE IMPLEMENTAT

### 1. Detector tier-aware T3
Verificările trebuie să știe diferența dintre:
- T2, unde Data Model / join / comparație / trend erau interzise
- T3, unde acestea devin competențe permise

Pentru T3:
PERMIS:
- Data Model
- relații
- join / merge
- 1:M
- comparații
- trend
- performanță
- cel mai mare / cel mai mic
- citire cross-tabel

INTERZIS T3, pentru că aparține T4/T5:
- dashboard
- grafic publicabil
- raport vizual
- cockpit / scorecard dacă sunt livrabil vizual final
- alertă
- acțiune automată
- recomandare executată
- flux decizional automat

### 2. Regula verb-semnătură T3
Adaugă verificare pentru contaminare între construcțiile T3:

C09 RELAȚII:
- verb construcție: a lega
- are voie să ancoreze: relații, legături, model, tabele conectate
- nu trebuie să ancoreze: a defini / măsură vie / clasament / de ce / explicație

C10 MĂSURI:
- motto folosește măsoară
- verb construcție: a defini
- are voie să ancoreze: măsură, definire, context, single source of truth
- nu trebuie să ancoreze: ranking, top, bottom, clasament, explicație, de ce

C11 COMPARAȚII:
- verb construcție: a compara
- are voie să ancoreze: comparație, clasament, diferență, contribuție, ranking, top / bottom, ABC / Pareto ca instrumente
- nu trebuie să ancoreze: cauză, de ce, explicație, insight final

C12 INTERPRETARE:
- verb construcție: a explica
- are voie să ancoreze: de ce, cauză, explicație, insight verbal
- nu trebuie să ancoreze: dashboard, grafic publicabil, alertă, acțiune, recomandare executată
- What-if nu trebuie să fie identitate principală C12

### 3. C09 guard special
Pentru C09, verifică mecanic că rămâne la RELAȚII:
- poate avea Data Model / relații / chei / cardinalitate / 1:M
- poate avea prima citire cross-tabel demonstrativă
- nu trebuie să definească măsuri numite C10
- nu trebuie să facă ranking / top / bottom C11
- nu trebuie să explice cauze C12
- nu trebuie să facă dashboard T4

### 4. Integrare în gate / audit
Integrează aceste verificări în sistemul existent, după arhitectura repo-ului:
- gate_v20.py, dacă acolo este locul corect
- audit_sync.py, dacă acolo este locul corect
- un modul separat tier_guard / detector, dacă arhitectura existentă recomandă separarea
- teste / fixtures, dacă există deja model de testare

Nu strica verificările T1/T2 existente.
T2 trebuie să rămână strict descriptiv.
T3 trebuie să permită exact ce T2 interzicea.

### 5. Raportare clară
La rulare, raportul trebuie să distingă:
- contaminare T2 -> T3
- contaminare intra-T3
- contaminare T3 -> T4/T5
- avertismente non-blocante
- erori blocante

## FIȘIERE PERMISE LA MODIFICARE
Ai voie să modifici doar:
- _system/generatoare/**
- fișiere de test / fixtures din _system, dacă există
- documente tehnice strict necesare pentru descrierea detectorului, dacă există deja un loc clar pentru asta
- CLAUDE-TO-BRAIN.md

## FIȘIERE INTERZISE LA MODIFICARE
Nu modifica:
- c01/** până la c12/**
- orice HTML
- orice FILM
- orice xlsx
- orice imagine
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- STARE-CURENTA.md, decât dacă este absolut necesar pentru status scurt
- README.md
- CLAUDE.md

## TESTE / VERIFICĂRI
După implementare:

1. Rulează testele existente relevante.
2. Rulează audit / gate pe cel puțin o construcție T2 existentă, ca să confirmi că T2 nu s-a relaxat greșit.
3. Rulează verificare pe C09 dacă există artefacte / blueprint disponibile, fără să implementezi C09.
4. Demonstrează cu exemple că:
   - Data Model este interzis în T2 dar permis în T3.
   - dashboard este interzis în T3.
   - „a defini" este permis ca verb de construcție C10.
   - ranking este permis în C11, nu în C10.
   - What-if nu este identitate C12.

Dacă nu poți rula un test, explică exact de ce și marchează WARNING.

## LIVRABIL
Scrie raportul complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere modificate / create
5. Unde ai implementat detectorul T3
6. Ce reguli T3 au fost adăugate
7. Cum ai protejat T2 de relaxare greșită
8. Cum ai protejat C09 de contaminare C10-C12
9. Cum ai protejat T3 de T4/T5
10. Teste / verificări rulate
11. Rezultate PASS / WARNING / FAIL
12. Probleme rămase
13. Decizii cerute de la BRAIN
14. Commit / status Git

## MANDAT CURENT
Execută BRAIN-007.
Gărzi tehnice T3 înainte de implementarea C09.
Zero implementare C09.
