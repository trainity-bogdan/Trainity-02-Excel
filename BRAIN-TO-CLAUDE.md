# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-012

## MANDAT
C09 RELAȚII, SLICE 2: HTML-Studiu-Excel-09-Relatii.html autorat genuin.

## DECIZII BRAIN
Confirm explicit:

1. SLICE 1 este acceptat.
2. Accept generatorul _system/generatoare/build_date_master_c09.py pentru reproductibilitate.
3. Continuăm cu SLICE 2, HTML-Studiu C09 autorat complet.
4. Nu generăm încă imagini.
5. Nu propagăm încă Editor-Studiu, Video, Editor-Video.
6. Nu implementăm încă FILM.
7. Nu forțăm release complet C09 în acest mandat.

## CONTEXT
BRAIN-011 a livrat:
- c09/Date_MASTER-C09.xlsx, model relațional genuin
- c09/Creativ-Excel-09-Relatii.txt, brief hero + 6 exec-stage
- _system/generatoare/build_date_master_c09.py, generator reproductibil

Validări BRAIN-011:
- Slice 1 PASS
- conservare R-V02.14 PASS
- garda C09 PASS
- zero regresie C01-C08
- C09 are încă warning așteptat pentru HTML și imagini lipsă

Acum construim primul artefact learner-facing real al C09: HTML-Studiu.

## OBIECTIV
Creează HTML-Studiu-Excel-09-Relatii.html autorat genuin, pe axa RELAȚII, folosind Date_MASTER-C09.xlsx ca bază pedagogică.

Studiul trebuie să fie premium, memorabil, operațional și clar diferit de C08.

C09 nu este hartă descriptivă.
C09 este activarea relațiilor.

## DOCUMENTE DE CITIT
Citește obligatoriu:
- BRAIN-TO-CLAUDE.md
- CLAUDE-TO-BRAIN.md, raportul BRAIN-011
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/blueprints/BLUEPRINT-C09-RELATII.md
- c09/Date_MASTER-C09.xlsx
- c09/Creativ-Excel-09-Relatii.txt
- c08 artefacte relevante doar pentru handoff, nu pentru clonare
- _system/generatoare/gate_v20.py
- _system/generatoare/tier_guard_t3.py
- _system/generatoare/audit_sync.py

## PRINCIPIU SACRU
Nu clona C08.

C08 = recunoaștere ecosistem.
C09 = legare relațională.

C08 spune: "uite ce există".
C09 spune: "uite cum legi ce există ca să poți întreba peste tabele".

## REGULĂ IMPORTANTĂ DESPRE CIFRE
Nu hardcoda în HTML cifrele exacte din Excel.

Valorile numerice concrete se citesc, se demonstrează și se validează live în workbook, nu se transformă în slide/page statică.

În HTML poți descrie tipul de citire:
- valoare pe regiune
- număr tranzacții pe client
- verificare orfani
- sumă conservată

Dar nu transforma HTML-ul într-un raport cu cifre finale.

C09 este construcție, nu dashboard.

## IDENTITATE C09
C09 RELAȚII.

Verb: a lega.
Obiect: sursele / tabelele / modelul.
Promisiune: poți întreba peste mai multe tabele.
AHA: "Fără relații ai date. Cu relații ai răspunsuri."

Miza business:
O companie nu are o problemă de date, are o problemă de date care nu vorbesc între ele.

## STRUCTURĂ CERUTĂ PENTRU HTML-STUDIU
Urmează standardul premium al construcțiilor C05-C08, dar fără clonare narativă.

HTML-ul trebuie să includă:

1. HERO C09 puternic
2. Problemă reală de business
3. Reframe C09
4. Cele 6 etape C09 din blueprint
5. SCENA cu 5 fenomene reale de relații
6. 2 prompturi AI / Copilot, strict ca accelerator, nu ca substitut
7. Arc TU, cursantul trece de la tabele separate la model interogabil
8. Handoff C08 -> C09
9. Handoff C09 -> C10
10. Final memorabil, cu AHA-ul C09

## CELE 6 ETAPE C09
Folosește etapele din BLUEPRINT-C09-RELATII.md.

Dacă blueprint-ul are denumiri exacte, păstrează-le.
Dacă există ambiguitate, raportează și folosește cea mai apropiată structură locked.

Fiecare etapă trebuie să aibă:
- intenție
- acțiune în workbook
- verificare
- rezultat pedagogic
- ce NU facem încă

## SCENA 5 FENOMENE
Construiește scena C09 pe relații, nu pe analiză finală.

Fenomene recomandate, adaptează la blueprint dacă are altă listă locked:
1. Tabelul singur pare complet, dar nu poate răspunde la întrebarea corectă.
2. Cheia există, dar nu este activată ca relație.
3. Relația greșită produce citiri greșite sau imposibile.
4. O dimensiune fără cheie activă rămâne mută.
5. Modelul legat permite prima citire cross-tabel, fără să devină măsură numită.

## PROMPTURI AI
Include 2 prompturi utile pentru cursant:

1. Prompt de identificare relații posibile între tabele.
2. Prompt de verificare a riscurilor relaționale, orfani, cardinalitate, chei duplicate, relații inactive.

Prompturile trebuie să fie instrumente de verificare și accelerare.
Nu trebuie să înlocuiască gândirea cursantului.

## GRANIȚE STRICTE
C09 NU are voie să:
- definească măsuri numite
- explice măsura vie
- creeze KPI-uri reutilizabile
- facă ranking
- facă top/bottom
- facă Pareto
- explice cauze
- formuleze "de ce" ca insight final
- producă dashboard
- producă raport vizual publicabil
- dea recomandări de acțiune
- automatizeze decizii

C09 are voie doar:
- să lege tabele
- să documenteze relații
- să verifice integritatea relațiilor
- să facă o citire demonstrativă cross-tabel
- să pregătească nevoia de măsură stabilă pentru C10

## HANDOFF C08 -> C09
C08 a predat ecosistemul recunoscut.

C09 trebuie să pornească de aici:
"Am văzut tabelele. Acum le legăm."

Nu reface C08.
Nu reexplica inventarul.
Nu face hartă descriptivă.

## HANDOFF C09 -> C10
La finalul HTML-Studiu C09 trebuie să fie clar:
"Acum modelul poate răspunde. Dar dacă vrem o cifră stabilă, aceeași pentru toți, trebuie să definim măsura. Asta este C10."

Nu defini încă măsuri.
Doar creează tensiunea pentru C10.

## FIȘIERE PERMISE LA MODIFICARE / CREARE
Ai voie să creezi / modifici doar:
- c09/HTML-Studiu-Excel-09-Relatii.html
- eventual fișiere strict necesare de index / registry dacă standardul repo cere recunoașterea HTML-ului
- CLAUDE-TO-BRAIN.md
- STARE-CURENTA.md doar dacă fluxul standard cere actualizare

## FIȘIERE INTERZISE
Nu modifica:
- C01-C08
- C10-C12
- c09/Date_MASTER-C09.xlsx
- c09/Creativ-Excel-09-Relatii.txt, decât dacă descoperi o eroare factuală clară și o explici
- build_date_master_c09.py
- Editor-Studiu C09
- Video C09
- Editor-Video C09
- FILM C09
- imagini / assets generate
- governance / Bible
- 06-MAP
- doc 12 T3
- tier_guard_t3.py
- gate_v20.py
- README.md
- CLAUDE.md

## VALIDĂRI CERUTE
Rulează:

1. gate_v20 09 c09 c01, chiar dacă release complet nu este așteptat încă.
2. tier_guard_t3 pentru C09, direct sau prin gate.
3. audit_sync.
4. verificare anti-clonă narativă față de C08, pe cât permite tooling-ul existent.
5. verificare că HTML-ul nu conține contaminări C10/C11/C12/T4/T5.

## CRITERII DE PASS PENTRU SLICE 2
Mandatul trece doar dacă:

1. HTML-Studiu C09 există.
2. Este autorat genuin pe RELAȚII.
3. Nu este clonă C08.
4. Folosește Date_MASTER-C09 ca bază pedagogică.
5. Nu hardcodează cifre exacte ca raport static.
6. Respectă granița C09/C10.
7. Respectă granița C09/C11/C12/T4/T5.
8. Are 6 etape coerente.
9. Are SCENA 5 fenomene.
10. Are 2 prompturi AI utile.
11. Are handoff C08 -> C09 și C09 -> C10.
12. Raportul explică ce rămâne pentru SLICE 3.

## LIVRABIL
Scrie raport complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere create / modificate
5. Structura HTML-Studiu C09
6. Cum ai construit cele 6 etape
7. Cum ai construit SCENA 5 fenomene
8. Cum ai folosit Date_MASTER-C09 fără să faci raport static
9. Cum ai respectat granița C09/C10
10. Cum ai respectat granița C09/C11/C12/T4/T5
11. Validări rulate
12. Rezultate PASS / WARNING / FAIL
13. Ce rămâne pentru SLICE 3
14. Decizii cerute de la BRAIN
15. Commit / status Git

## MANDAT CURENT
Execută BRAIN-012.
C09 RELAȚII, SLICE 2.
Livrează HTML-Studiu-Excel-09-Relatii.html autorat genuin.
Zero Editor-Studiu.
Zero Video.
Zero Editor-Video.
Zero FILM.
Zero imagini generate.
Zero clonare C08.
