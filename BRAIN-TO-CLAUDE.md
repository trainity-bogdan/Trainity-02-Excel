# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-006

## MANDAT
Îngheț T3 cap-coadă înainte de implementarea C09.

## CONTEXT
BRAIN-005 a confirmat că arhitectura T3 este coerentă conceptual, dar nu este complet înghețată.

Verdict BRAIN-005:
- C09 este complet LOCKED.
- C10/C11/C12 sunt încă PROPUNERE.
- C10 are WARNING, dar are o variantă revizuită bună.
- 06-MAP conține teme vechi care contrazic lanțul locked.
- Granițele T3/T4/T5 există ca propunere, dar nu sunt înghețate în governance.

Nu implementăm C09 încă.
Mai întâi înghețăm T3 complet.

## DECIZII BRAIN
Aplică următoarele decizii:

1. C10 rămâne MĂSURI ca nume de construcție.
2. Motto-ul de treaptă C10 rămâne: „Întrebi cât. Modelul măsoară."
3. Verbul de construcție C10 devine: „a defini".
4. Identitatea C10 revizuită se adoptă:
   - măsura vie
   - define once
   - context-aware
   - single source of truth
5. AHA C10 adoptat:
   „Un număr stă în tabel. O măsură trăiește în întrebare."
6. C12 rămâne INTERPRETARE / „de ce".
7. Tema veche „What-if / scenarii business" se retrage din identitatea C12.
8. Formula granițelor se adoptă:
   - T3 produce răspunsul.
   - T4 îl face vizibil.
   - T5 îl pune în acțiune.
9. Formula „Oamenii / Profesioniștii" rămâne permisă în T3 ca semnătură, dar marchează risc de saturație pentru treptele următoare.

## OBIECTIV
Îngheață arhitectura T3 completă, cap-coadă, în documentele de sistem.

T3 trebuie să conțină clar:
- scopul treptei
- problema mare rezolvată
- transformarea cap-coadă
- C09/C10/C11/C12
- problema rezolvată de fiecare construcție
- ce produce fiecare construcție
- instrumentele fiecărei construcții
- livrabilul fiecărei construcții
- granițele între construcții
- granițele T2/T3/T4/T5
- gărzi anti-contaminare

## FIȘIERE PERMISE LA MODIFICARE
Ai voie să modifici doar documente de arhitectură / governance:

- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md, dacă nu există, creează-l
- STARE-CURENTA.md, doar pentru status scurt al înghețului T3
- CLAUDE-TO-BRAIN.md

## FIȘIERE INTERZISE LA MODIFICARE
Nu modifica:
- c01/** până la c12/**
- orice HTML
- orice FILM
- orice xlsx
- orice imagine
- blueprint-uri de construcție, cu excepția cazului în care raportezi explicit că este indispensabil
- README.md
- CLAUDE.md

## CE TREBUIE ÎNGHEȚAT ÎN BIBLE §T3
Extinde §T3 astfel încât să existe arhitectura completă pentru:

C09 RELAȚII
- întrebare: Ce pot întreba?
- verb construcție: a lega
- output: model interogabil
- instrumente: Data Model, relații 1:M, cardinalitate, chei, tabele conectate
- nu are voie: măsuri C10, comparații C11, explicații C12, raportare T4, acțiune T5

C10 MĂSURI
- întrebare: Cât?
- verb de treaptă în motto: măsoară
- verb de construcție: a defini
- output: măsură stabilă / măsură vie
- instrumente: măsuri, agregări, DAX de bază, context de filtrare, Power Pivot, single source of truth
- AHA: „Un număr stă în tabel. O măsură trăiește în întrebare."
- mantra recomandată: „Nu scriem cifra. O definim."
- nu are voie: ranking / top / bottom / comparații C11, explicații C12, dashboard T4

C11 COMPARAȚII
- întrebare: Care?
- verb construcție: a compara
- output: clasament / diferență / contribuție
- instrumente: ranking, top / bottom, diferențe, contribuții, sortare analitică, ABC/Pareto ca instrumente de comparație
- nu are voie: explicații cauzale C12, dashboard T4, decizie T5

C12 INTERPRETARE
- întrebare: De ce?
- verb construcție: a explica
- output: insight verbal / cauză / înțeles
- instrumente: citire din model, drill-down analitic, explicație, cauză, insight verbal
- nu are voie: What-if ca identitate, dashboard T4, raport vizual T4, decizie / alertă / acțiune T5

## SPEC 11-SLOT C10-C12
Adaugă în Bible §T3 SPEC 11-slot pentru C10, C11, C12.

Folosește ca bază WORKSHOP-C10-T3-T4-T5.md și raportul BRAIN-005.

Pentru C10 adoptă varianta revizuită, nu varianta slabă.

C10 trebuie să includă minimum:
- HERO
- BOMBĂ
- GREȘEALA
- AHA
- MANTRA
- WOW
- MOTTO
- CINE DEVII
- PAYOFF
- MIZA
- garda de contaminare

C11 și C12 trebuie să fie aliniate cu lanțul:
model -> măsură -> clasament -> explicație.

## GRANIȚE T3 / T4 / T5
Adaugă în Bible delimitarea:

T3 = ANALIZĂ / INTERPRETARE
- produce răspunsul
- output: model, măsură, clasament, cauză / insight verbal
- interzis: dashboard, grafic publicabil, raport vizual, alertă, acțiune, recomandare executată

T4 = RAPORTARE / COMUNICARE VIZUALĂ
- face răspunsul vizibil pentru altcineva
- output: dashboard / cockpit / scorecard / raport vizual
- interzis: să inventeze răspunsuri noi care țin de T3
- interzis: să acționeze automat, pentru că aceea este T5

T5 = AUTOMATIZARE / ACȚIUNE
- pune răspunsul în acțiune sau pe pilot automat
- output: refresh automat, alertă, flux, acțiune declanșată, sistem autonom
- interzis: să refacă analiza T3 sau designul vizual T4 ca lecție nouă

Notează nuanța:
- decizia umană stă între T4 și T5
- decizia automată / acțiunea declanșată este T5

## REALINIERE 06-MAP
Realiniază secțiunea T3 din _system/06-MAP-CONSTRUCTII-T1-T5.md la lanțul locked:

C09 RELAȚII
C10 MĂSURI
C11 COMPARAȚII
C12 INTERPRETARE

Elimină sau retrogradează temele vechi ca identitate principală:
- C10 „KPI compoziti DAX" nu mai este identitate principală
- C11 „Prioritizare ABC/Pareto" nu mai este identitate principală, ABC/Pareto pot rămâne instrumente C11
- C12 „What-if analysis / scenarii business" nu mai este identitate principală

## DOCUMENT T3 DEDICAT
Creează sau actualizează:
_system/12-ARHITECTURA-CONCEPTUALA-T3.md

Acest document trebuie să explice clar, pentru viitoare chat-uri:
- ce este T3
- ce rezolvă T3
- lanțul C09-C12
- arhitectura fiecărei construcții
- instrumente
- livrabile
- granițe
- riscuri
- decizii locked

## TESTE / VERIFICĂRI
După modificări, verifică:

1. Bible §T3 conține C09-C12 complet.
2. C10 are rezoluția corectă: motto măsoară, verb construcție definește.
3. C12 nu mai are What-if ca identitate.
4. 06-MAP nu mai contrazice Bible.
5. T3/T4/T5 au granițe explicite.
6. Nu s-a modificat niciun artefact c01-c12.
7. Nu s-au generat fișiere C09.

## LIVRABIL
Scrie raportul complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere modificate / create
5. Ce s-a înghețat în Bible §T3
6. Ce s-a modificat în 06-MAP
7. Ce conține documentul T3 dedicat
8. Cum s-a rezolvat C10 WARNING
9. Cum s-a rezolvat contaminarea C12 / What-if
10. Granițe T3/T4/T5 rezultate
11. Verificări rulate
12. Rezultate PASS / WARNING / FAIL
13. Probleme rămase
14. Decizii cerute de la BRAIN
15. Commit / status Git

## MANDAT CURENT
Execută BRAIN-006.
Îngheț T3 cap-coadă.
Zero implementare C09.
