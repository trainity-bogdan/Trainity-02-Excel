# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-010

## MANDAT
IMPLEMENTARE C09 RELAȚII din SPEC LOCKED.

## CONTEXT
BRAIN-009 a făcut auditul final T3.

Verdict:
- T3 = PASS CU WARNING-uri
- Zero FAIL blocant
- C09 = gata de implementare
- warning-urile vizează C10-C12, nu blochează C09

C09 este prima construcție din T3.

T3 lanț:
C08 hartă descriptivă → C09 model interogabil → C10 măsură stabilă → C11 clasament / diferență → C12 cauză / insight verbal → T4 raportare vizuală

C09 rol:
- leagă sursele
- activează Data Model
- face prima citire cross-tabel
- NU definește măsuri numite / reutilizabile
- NU face clasament
- NU explică de ce
- NU produce dashboard
- NU intră în acțiuni / recomandări

## OBIECTIV
Implementează complet C09 RELAȚII pe baza SPEC LOCKED și BLUEPRINT-C09-RELATII.md.

C09 trebuie să fie o construcție reală, livrabilă, memorabilă, coerentă cu T3 și validată prin gate.

## DOCUMENTE DE CITIT ÎNAINTE
Citește obligatoriu:
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/blueprints/BLUEPRINT-C09-RELATII.md
- CLAUDE-TO-BRAIN.md, raportul BRAIN-009
- c08 artefacte relevante pentru handoff
- _system/generatoare/gate_v20.py
- _system/generatoare/tier_guard_t3.py
- _system/generatoare/audit_sync.py

## REGULI CRITICE C09

### Identitate C09
C09 = RELAȚII.

Verb: a lega.
Obiect: sursele / tabelele / modelul.
Promisiune: pot întreba peste mai multe tabele.
AHA: Fără relații ai date. Cu relații ai răspunsuri.

### Graniță C09 / C10
C09 are voie să facă doar citire demonstrativă cross-tabel.

C09 NU are voie să:
- definească măsuri numite
- creeze măsuri reutilizabile
- explice conceptul de măsură vie
- folosească identitatea C10
- transforme citirea demonstrativă în lecție despre măsurare

C10 este despre a defini măsuri.
C09 este despre a lega modelul ca să poți întreba.

### Graniță C09 / C11
C09 NU face:
- ranking
- top/bottom
- clasament
- Pareto
- comparații sistematice

### Graniță C09 / C12
C09 NU explică de ce.
Nu caută cauze.
Nu face insight final.

### Graniță C09 / T4
C09 NU produce dashboard.
C09 NU produce raport vizual publicabil.
C09 NU construiește cockpit / scorecard.

### Graniță C09 / T5
C09 NU recomandă acțiuni.
C09 NU generează decizii.
C09 NU automatizează fluxuri.

## TASKURI OBLIGATORII

### 1. Adaugă C09 în gate config
Adaugă intrarea C09 în load_identitate sau mecanismul echivalent din gate_v20, astfel încât C09 să poată fi validată oficial de gate.

Aceasta a fost problema rămasă din BRAIN-008 și BRAIN-009.

### 2. Implementează artefactele C09
Implementează pachetul complet C09 conform structurii repo și standardului C01-C08.

Respectă naming-ul și arhitectura existentă.
Nu inventa structură nouă dacă există deja convenție.

### 3. Integrează handoff C08 → C09
C09 trebuie să pornească natural din C08.

C08 predă harta descriptivă / ecosistemul.
C09 activează relațiile și transformă sursele în model interogabil.

### 4. Pregătește handoff C09 → C10
La final C09 trebuie să predea către C10:
- modelul legat
- prima citire cross-tabel
- nevoia de cifră stabilă

Dar fără să definească încă măsuri numite.

### 5. Rulează validări
Rulează obligatoriu:
- gate_v20 pentru C09
- tier_guard_t3 pentru C09, direct sau prin gate
- audit_sync
- orice verificare standard folosită pentru C01-C08

## FIȘIERE PERMISE LA MODIFICARE
Ai voie să modifici:
- fișierele C09 necesare
- index / registry / mapări necesare pentru C09
- gate_v20.py doar pentru intrarea C09 în load_identitate sau config echivalent
- CLAUDE-TO-BRAIN.md
- STARE-CURENTA.md doar dacă este standard în fluxul de finalizare

## FIȘIERE INTERZISE LA MODIFICARE
Nu modifica:
- C01-C08 artefacte existente
- C10-C12 artefacte, dacă există doar ca blueprint/spec
- governance / Bible
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- detectorul tier_guard_t3.py, decât dacă descoperi bug real și îl explici clar
- README.md
- CLAUDE.md

## CRITERII DE PASS
Mandatul trece doar dacă:

1. C09 este implementată complet.
2. C09 este aliniată cu SPEC LOCKED.
3. C09 nu contaminează C10/C11/C12/T4/T5.
4. C09 are intrare în gate config.
5. gate_v20 rulează pe C09.
6. tier_guard_t3 verifică C09.
7. audit_sync nu introduce drift nejustificat.
8. raportul explică orice warning rămas.
9. zero modificări nepermise în C01-C08 și governance.

## LIVRABIL
Scrie raport complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere modificate
5. Ce ai implementat în C09
6. Cum ai respectat granița C09/C10
7. Cum ai respectat granița C09/C11/C12/T4/T5
8. Cum ai integrat C09 în gate config
9. Teste rulate
10. Rezultate PASS / WARNING / FAIL
11. Probleme rămase
12. Decizii cerute de la BRAIN
13. Commit / status Git

## MANDAT CURENT
Execută BRAIN-010.
Implementează C09 RELAȚII.
Respectă strict SPEC LOCKED.
Zero implementare C10-C12.
