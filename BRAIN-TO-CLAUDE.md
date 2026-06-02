# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-011

## MANDAT
C09 RELAȚII, SLICE 1: Date_MASTER-C09 relațional + Creativ-Excel-09-Relatii.

## DECIZII BRAIN
Confirm explicit:

1. NU vrem C08 relabelat ca C09.
2. NU vrem clonă narativă.
3. NU vrem clonă vizuală.
4. NU vrem implementare completă forțată într-un singur mandat dacă scade calitatea.
5. Mergem slice-by-slice.
6. În acest mandat livrezi doar baza reală C09: Date_MASTER + brief creativ / prompturi imagini.

C09 trebuie autorată genuin pe axa RELAȚII.

## CONTEXT
BRAIN-010 a produs parțial:
- C09 introdus în gate config / load_identitate = DONE
- tier_guard_t3 se activează pentru C09 = DONE
- artefactele C09 nu au fost livrate, corect, pentru că scaffold-ul din C08 ar fi fost clonă

Această decizie este corectă.
Calitatea C09 este mai importantă decât viteza.

## OBIECTIV
Construiește fundamentul real al C09:

1. Date_MASTER-C09.xlsx, cu model relațional autentic.
2. Creativ-Excel-09-Relatii.txt, cu brief vizual complet pentru ARHITECT / Banana / Gemini.
3. Pregătire clară pentru următorul slice: HTML-Studiu C09.

Nu implementa încă HTML.
Nu implementa FILM.
Nu propaga Editor / Video.
Nu genera imagini.

## DOCUMENTE DE CITIT
Citește obligatoriu:
- BRAIN-TO-CLAUDE.md
- CLAUDE-TO-BRAIN.md, raportul BRAIN-010
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md
- _system/06-MAP-CONSTRUCTII-T1-T5.md
- _system/blueprints/BLUEPRINT-C09-RELATII.md
- c08 artefacte relevante doar pentru handoff, NU pentru clonare
- _system/generatoare/gate_v20.py
- _system/generatoare/tier_guard_t3.py
- _system/generatoare/audit_sync.py

## PRINCIPIU SACRU
C09 nu este C08 redenumit.

C08 = hartă descriptivă / ecosistem.
C09 = relații / model interogabil.

C08 recunoaște sursele.
C09 leagă sursele.

C08 arată ce există.
C09 arată cum sursele pot răspunde împreună.

## CERINȚE Date_MASTER-C09.xlsx
Construiește un workbook real, relațional, pentru C09.

Trebuie să includă:

1. Tabel fact principal, de exemplu vânzări / tranzacții.
2. Tabele dimensiune reale, de exemplu:
   - produse
   - clienți
   - regiuni / agenți / canale
   - calendar / perioade
3. Chei clare între tabele.
4. Relații 1:M gândite explicit.
5. O foaie _MODEL sau echivalent, care documentează relațiile.
6. O zonă de verificare a integrității modelului.
7. Cel puțin o situație în care citirea dintr-un singur tabel este insuficientă.
8. Cel puțin o citire demonstrativă cross-tabel, fără măsuri numite.
9. Date suficient de bogate pentru HTML-Studiu, dar fără să devină C10/C11/C12.

Workbook-ul trebuie să susțină pedagogic ideea:
"Fără relații ai date. Cu relații ai răspunsuri."

## INTERDICȚII Date_MASTER-C09.xlsx
Nu crea:
- măsuri DAX numite
- KPI finali reutilizabili
- clasamente
- top/bottom
- Pareto
- dashboard
- raport final
- explicații de cauză
- recomandări de acțiune

C09 permite doar citire demonstrativă cross-tabel.
Nu transforma C09 în C10.

## CERINȚE Creativ-Excel-09-Relatii.txt
Creează brief complet pentru imagini C09.

Trebuie să includă:

1. Hero vizual C09, axa RELAȚII.
2. 6 imagini exec-stage, una pentru fiecare etapă C09.
3. Pentru fiecare imagine:
   - scop pedagogic
   - descriere vizuală
   - elemente obligatorii
   - elemente interzise
   - prompt pentru generare imagine
   - negative prompt
   - stil vizual Trainity
   - relația cu AHA-ul C09
4. Instrucțiuni clare pentru ARHITECT / Banana / Gemini.

## DIRECȚIE VIZUALĂ C09
Imaginea nu trebuie să semene cu C08.

C09 trebuie să arate:
- surse separate care se conectează
- linii / noduri / chei / poduri
- model care devine interogabil
- relații curate, nu haos descriptiv
- activarea unei rețele de date

Evită:
- hărți de ecosistem tip C08
- inventar descriptiv
- dashboard-uri
- grafice publicabile
- clasamente
- oameni generic business fără sens
- imagini decorative

## FIȘIERE PERMISE LA MODIFICARE / CREARE
Ai voie să modifici sau creezi doar:
- fișiere C09 necesare pentru Date_MASTER-C09.xlsx
- Creativ-Excel-09-Relatii.txt sau c09 echivalentul standard dacă există convenție
- eventual fișiere index/registry strict necesare pentru ca Date_MASTER să fie recunoscut
- CLAUDE-TO-BRAIN.md
- STARE-CURENTA.md doar dacă fluxul standard cere actualizare de stare

## FIȘIERE INTERZISE
Nu modifica:
- C01-C08 artefacte
- C10-C12
- HTML C09
- FILM C09
- Editor-Studiu C09
- Video C09
- Editor-Video C09
- governance / Bible
- 06-MAP
- doc 12 T3
- tier_guard_t3.py
- gate_v20.py, cu excepția cazului în care descoperi un bug real deja produs de BRAIN-010, explicat clar
- README.md
- CLAUDE.md

## VALIDĂRI CERUTE
Rulează ce este relevant pentru acest slice:

1. Verifică workbook-ul C09 generat.
2. Verifică existența tabelelor și cheilor.
3. Verifică documentarea relațiilor în _MODEL.
4. Rulează audit_sync.
5. Rulează tier_guard_t3 self-test dacă ai modificări care pot afecta fluxul.
6. Rulează gate_v20 C09 doar informativ, dacă HTML-urile lipsesc va pica pe livrabile lipsă, ceea ce este acceptat pentru acest slice.

Nu forța PASS de release complet. Acesta este SLICE 1, nu C09 final.

## CRITERII DE PASS PENTRU SLICE 1
Mandatul trece doar dacă:

1. Date_MASTER-C09.xlsx există și este genuin relațional.
2. Nu este clonă C08.
3. Are tabele multiple și chei clare.
4. Are foaie _MODEL / documentare relații.
5. Susține pedagogic C09, nu C10/C11/C12.
6. Creativ-Excel-09-Relatii.txt există și conține prompturi pentru hero + 6 exec-stage.
7. Raportul explică ce a fost livrat și ce rămâne pentru SLICE 2.
8. Nu s-au modificat fișiere interzise.

## LIVRABIL
Scrie raport complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere create / modificate
5. Structura Date_MASTER-C09.xlsx
6. Tabele, chei și relații
7. Cum workbook-ul susține C09, nu C10/C11/C12
8. Structura Creativ-Excel-09-Relatii.txt
9. Prompturi imagini pregătite
10. Validări rulate
11. Rezultate PASS / WARNING / FAIL
12. Ce rămâne pentru SLICE 2
13. Decizii cerute de la BRAIN
14. Commit / status Git

## MANDAT CURENT
Execută BRAIN-011.
C09 RELAȚII, SLICE 1.
Livrează Date_MASTER-C09.xlsx + Creativ-Excel-09-Relatii.txt.
Zero HTML.
Zero FILM.
Zero imagini generate.
Zero clonare C08.
