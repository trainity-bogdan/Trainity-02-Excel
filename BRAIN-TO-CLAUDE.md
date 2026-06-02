# BRAIN → CLAUDE

## STATUS
PENDING

## CUVÂNT CHEIE

SYNC

Când Bogdan scrie `SYNC` către Claude Code, Claude trebuie să citească acest fișier, să execute mandatul curent și să scrie raportul complet în `CLAUDE-TO-BRAIN.md`.

Când Bogdan scrie `SYNC` către BRAIN, BRAIN va citi `CLAUDE-TO-BRAIN.md`, va da verdictul și va pregăti următorul mandat în `BRAIN-TO-CLAUDE.md`, dacă este cazul.

## PROTOCOL
Acest fișier este canalul oficial prin care BRAIN, ChatGPT / Andrei, transmite mandate către Claude Code.

Regula de lucru:
- BRAIN definește arhitectura, auditul, decizia pedagogică și mandatul.
- Claude Code execută în repository.
- Claude Code nu schimbă arhitectura fără mandat explicit.
- Claude Code lucrează doar pe `main`, conform instrucțiunii lui Bogdan.
- Claude Code scrie răspunsul complet în `CLAUDE-TO-BRAIN.md`.
- Claude Code nu folosește conversația ca raport principal, ci fișierul `CLAUDE-TO-BRAIN.md`.

## FIȘIERE DE COMUNICARE

- `BRAIN-TO-CLAUDE.md` = instrucțiunile de la BRAIN către Claude.
- `CLAUDE-TO-BRAIN.md` = raportul de la Claude către BRAIN.

## REGULA DE AUR

Claude execută exact mandatul curent din acest fișier.
Dacă mandatul este ambiguu, Claude oprește execuția și scrie `NEEDS DECISION` în `CLAUDE-TO-BRAIN.md`.

## MANDAT-ID
BRAIN-002

## MANDAT
Curățare punctuală reziduuri T1 descoperite în BRAIN-001.

## CONTEXT
BRAIN-001 a dat verdict T1 global PASS. FAIL-urile majore din Auditul Monstruos sunt închise:

- boilerplate corp FILM C02/C04 închis
- voce template/neutră C03 închisă
- canibalizare C02/C03 închisă, scor diferențiere 9/10
- corpurile narative 6x6 C01-C04 sunt curate

Au rămas doar 3 reziduuri minore NON-blocante, aflate în sloturi periferice cu schelet comun, nu în corpul 6x6.

Acest mandat este EXECUȚIE PUNCTUALĂ.
Ai voie să modifici doar fișierele necesare pentru cele 3 reziduuri de mai jos.
Nu atinge corpul narativ 6x6 dacă nu este strict necesar.
Nu rescrie construcții.
Nu optimiza în afara mandatului.

## OBIECTIV
Închide cele 3 reziduuri punctuale din BRAIN-001, fără să afectezi arhitectura T1 și fără să introduci drift nou.

## FIȘIERE PERMISE
Ai voie să citești:
- BRAIN-TO-CLAUDE.md
- CLAUDE-TO-BRAIN.md
- FILM C01-C04
- HTML-Studiu C01-C04, doar dacă ai nevoie să verifici sincronizarea sloturilor afectate
- documente de guvernanță relevante, doar pentru verificare

Ai voie să modifici DOAR fișierele care conțin reziduurile punctuale confirmate:
- C02 FILM, dacă acolo se află linia ROLURI reziduală
- C04 FILM, dacă acolo se află secțiunea CONTROL UMAN reziduală
- eventual C01/C03 FILM doar dacă reziduul de SLIDE EXEC este în acele fișiere și necesită distanțare minimă
- CLAUDE-TO-BRAIN.md pentru raport

## FIȘIERE INTERZISE
- Nu modifica xlsx.
- Nu modifica imagini.
- Nu modifica HTML dacă nu este strict necesar pentru sincronizare cu FILM.
- Nu modifica governance.
- Nu modifica STARE-CURENTA.md.
- Nu modifica README.md.
- Nu modifica CLAUDE.md.
- Nu modifica structura T1/T2/T3.
- Nu modifica AHA/MANTRA/WOW/MOTTO locked fără motiv explicit și raportat.

## REZIDUURI DE REPARAT

### 1. Ecou de șablon în SLIDE-uri executive
BRAIN-001 a raportat:
- SLIDE EXEC 6 are aceeași structură la C01 și C03:
  - C01: „Arată ca tabel. De data asta, chiar este."
  - C03: „Pare curat. De data asta, chiar este."
- SLIDE EXEC 2 are șablonul „AI-ul nu repară. AI-ul [verb]" la C01 și C03:
  - C01: „AI-ul nu repară. AI-ul scoate adevărul la suprafață."
  - C03: „AI-ul nu repară. AI-ul găsește ce nu se vede."

Cerință:
- păstrează sensul fiecărei construcții
- modifică minim doar unde este necesar ca forma C01 vs C03 să nu mai pară clonată
- C01 trebuie să rămână STRUCTURARE
- C03 trebuie să rămână AUDIT forensic
- nu schimba corpul 6x6

### 2. C02 ROLURI, linie reziduală nepotrivită
BRAIN-001 a raportat o linie reziduală de tip C01/C04:
„AI (Copilot): Audit + execuție controlată. Raportează ce vede, aplică transformări cerute explicit de noi."

Problema:
- limbajul „execuție / transformări" este nepotrivit pentru C02 CONTROL
- C02 trebuie să semnalizeze și să confrunte cu realitatea, nu să transforme

Cerință:
- elimină sau rescrie această linie
- păstrează linia corectă C02 despre „Interogare + semnalizare..." dacă există
- C02 trebuie să rămână CONTROL, nu AUDIT și nu AUTOMATIZARE

### 3. C04 CONTROL UMAN, ecou C01
BRAIN-001 a raportat în C04 un ecou de motto C01:
„Nu reconstruim, doar facem controlabil"

Problema:
- motto-ul real C04 este:
„Nu curățăm de mână. Construim fluxul."

Cerință:
- elimină ecoul C01
- aliniază formularea la C04 NORMALIZARE / AUTOMATIZARE
- păstrează ideea de control uman asupra fluxului, dar cu limbaj C04: flux, refresh, pași aplicați, automatizare, repetabilitate

## REGULI
- Lucrează doar pe main.
- Nu crea branch nou.
- Nu crea PR.
- Modifică strict minimul necesar.
- Nu atinge zonele care au primit PASS în BRAIN-001.
- Nu rescrie corpul narativ 6x6.
- Nu introduce termeni T3 în T1: relații, măsuri, comparații, DAX, KPI.
- Nu introduce dashboard / raportare vizuală.
- Nu modifica arhitectura locked.
- După modificări, rulează un re-check punctual pe cele 3 reziduuri.

## LIVRABIL
Scrie raportul complet în `CLAUDE-TO-BRAIN.md`.

## FORMAT RĂSPUNS CERUT
1. Status
2. Mandat executat
3. Rezumat executiv
4. Fișiere citite
5. Fișiere modificate
6. Schimbări efectuate, cu înainte / după pentru fiecare reziduu
7. Schimbări nefăcute
8. Re-check punctual
9. Rezultate PASS / WARNING / FAIL pentru fiecare din cele 3 reziduuri
10. Riscuri rămase
11. Decizii cerute de la BRAIN
12. Commit / status Git

## MANDAT CURENT
Execută BRAIN-002.
Curățare punctuală a celor 3 reziduuri T1.
Raport complet în `CLAUDE-TO-BRAIN.md`.
