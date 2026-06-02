# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-005

## MANDAT
Brainstorming arhitectural T3 cap-coadă, înainte de orice implementare C09.

## STOP EXECUȚIE
Mandatul anterior BRAIN-004, despre construirea C09, este ANULAT.
Nu implementa C09.
Nu genera HTML.
Nu genera FILM.
Nu genera xlsx.
Nu modifica artefacte C09.
Nu modifica fișiere de conținut.

Suntem în faza de TIER SEED / BRAINSTORMING pentru TREAPTA 3.

Atenție critică:
T3 = TREAPTA 3.
C03 = Construcția 03.
Nu le confunda.

## OBIECTIV
Construiește arhitectura completă T3 cap-coadă înainte de orice implementare.

Nu vrem doar SPEC C09.
Nu vrem doar HERO / AHA / MANTRA.
Nu vrem să construim C09 încă.

Vrem să înțelegem întreaga treaptă:

T3 = ANALIZĂ / INTERPRETARE

C09 RELAȚII
C10 MĂSURI
C11 COMPARAȚII
C12 INTERPRETARE

## DOCUMENTE DE CITIT OBLIGATORIU
Citește și folosește ca bază:

1. _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
   - §SHARED RULES
   - §TIER SEED
   - §T2
   - §T3

2. CLAUDE.md
   - regulile blocante
   - regula SPEC înghețat înainte de generare
   - structura livrabilelor

3. STARE-CURENTA.md
   - starea reală a proiectului

4. _system/06-MAP-CONSTRUCTII-T1-T5.md
   - harta completă C01-C20

5. _system/11-ARHITECTURA-CONCEPTUALA-T2.md
   - ce predă T2 către T3

6. c08/artefactele finale
   - handoff C08 → C09

7. _system/blueprints/BLUEPRINT-C09-RELATII.md
   - doar ca punct de pornire C09, nu ca motiv de implementare

8. WORKSHOP-C10-T3-T4-T5.md, dacă există
   - propunerile C10-C12 și granițele T3/T4/T5

## ÎNTREBĂRI DE BRAINSTORMING
Răspunde profund, nu formal:

1. Ce își propune T3 ca treaptă?
2. Ce problemă mare rezolvă T3?
3. Ce transformare produce T3?
4. Ce primește T3 de la T2?
5. Ce predă T3 către T4?
6. Unde se termină T3?
7. Unde începe T4?
8. Unde începe T5?

## ARHITECTURA CERUTĂ PENTRU FIECARE CONSTRUCȚIE
Pentru fiecare:

C09 RELAȚII
C10 MĂSURI
C11 COMPARAȚII
C12 INTERPRETARE

definește:

1. Problema pe care o rezolvă
2. Ce își propune
3. Întrebarea-mamă
4. Ce primește de la construcția anterioară
5. Ce produce
6. Ce predă mai departe
7. Instrumentele folosite
8. Livrabilul concret
9. Ce NU are voie să facă
10. Riscul principal de contaminare
11. Diferența față de construcția anterioară
12. Diferența față de construcția următoare

## INSTRUMENTE
Clarifică instrumentele fiecărei construcții.

Punct de plecare, de verificat împotriva documentelor:

C09 RELAȚII
- Data Model
- relații 1:M
- cardinalitate
- chei
- tabele conectate

C10 MĂSURI
- măsuri
- agregări
- DAX de bază
- context de filtrare
- single source of truth

C11 COMPARAȚII
- ranking
- top / bottom
- diferențe
- contribuții
- sortare analitică

C12 INTERPRETARE
- drill-down
- cauză
- explicație
- insight verbal
- citire din model

Corectează această listă dacă documentele din repo indică altceva.

## AUDIT DE LANȚ
Testează lanțul:

C08 → C09 → C10 → C11 → C12 → T4

Răspunde explicit:

1. Se rupe T3 dacă elimin C09?
2. Se rupe T3 dacă elimin C10?
3. Se rupe T3 dacă elimin C11?
4. Se rupe T3 dacă elimin C12?
5. C09 intră prea mult în C10?
6. C10 se confundă cu C11?
7. C11 se confundă cu C12?
8. C12 fuge în T4?
9. C12 fuge în T5?

## C10 WARNING
C10 a fost identificat ca posibil punct slab.
Analizează separat:

1. Este MĂSURI suficient de puternic?
2. Verbul corect este a măsura sau a defini?
3. AHA actual / propus este suficient?
4. C10 justifică o construcție separată?
5. Ce s-ar rupe dacă eliminăm C10?
6. Cum facem C10 memorabil fără să-l transformăm în C11?

## GRANIȚE T3 / T4 / T5
Definește clar:

T3 = ?
T4 = ?
T5 = ?

Pentru fiecare:

1. Întrebarea treptei
2. Output-ul treptei
3. Ce este permis
4. Ce este interzis
5. Unde începe treapta următoare

Verifică formula:
T3 produce răspunsul.
T4 îl face vizibil.
T5 îl pune în acțiune.

Spune dacă formula este corectă sau trebuie ajustată.

## LIVRABIL CERUT
Scrie în CLAUDE-TO-BRAIN.md un raport amplu cu structura:

1. STATUS
2. Documente citite
3. Ce spune sistemul existent despre TIER SEED
4. Ce este T3
5. Problema mare rezolvată de T3
6. Transformarea T3 cap-coadă
7. Harta completă C09-C12
8. Arhitectura C09
9. Arhitectura C10
10. Arhitectura C11
11. Arhitectura C12
12. Instrumente per construcție
13. Livrabile per construcție
14. Granițe C09-C10-C11-C12
15. Granițe T2-T3-T4-T5
16. Audit de lanț
17. Audit de redundanță
18. Audit de contaminare
19. C10 WARNING, analiză specială
20. Ce trebuie înghețat înainte de C09
21. Ce NU trebuie implementat încă
22. Recomandare finală
23. Decizii cerute de la BRAIN

## RESTRICȚII
Nu modifica nimic în afară de CLAUDE-TO-BRAIN.md.
Nu implementa C09.
Nu genera fișiere C09.
Nu modifica Bible.
Nu modifica STARE.
Nu modifica blueprint-uri.
Nu face commit-uri de conținut.

Acesta este brainstorming arhitectural, nu execuție.

## VERDICT FINAL CERUT
La final răspunde clar:

1. Avem deja arhitectură T3 completă?
2. Ce lipsește?
3. Este C09 gata de implementare sau nu?
4. Ce trebuie decis de BRAIN înainte de implementare?
5. Care ar trebui să fie următorul mandat corect?

## MANDAT CURENT
Execută BRAIN-005.
Brainstorming arhitectural T3 cap-coadă.
Zero implementare.
