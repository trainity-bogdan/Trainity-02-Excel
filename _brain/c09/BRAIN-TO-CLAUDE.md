# BRAIN → CLAUDE · C09 RELAȚII

## STATUS
MANDAT_ACTIV

## MANDAT-ID
C09-M020-VIDEO-EDITOR-VIDEO

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C09.

La comanda `sync`, citește:
- `_brain/c09/CHAT-CONTEXT.md`
- `_brain/c09/BRAIN-TO-CLAUDE.md`

Execută doar în:
- `c09/**`
- `_brain/c09/**`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.
Nu modifica fișiere sistem.

## STARE CURENTĂ C09
BRAIN-019-REV2 a fost executat cu PASS.

Editor-Studiu C09 este reparat:
- LOCK vizual complet.
- Join/Union canonic.
- lock granular PAS 01 și PAS 09.
- panou companion colapsabil pe mobil.
- lock-by-attribute principal, lock-by-phrase fallback.
- bază și companion sincronizate 1:1.

## MANDAT ACTIV
Construiește livrabilele video pentru C09 RELAȚII.

## OBIECTIV
Generează și aliniază:
1. HTML-Video C09.
2. HTML-Editor-Video C09.

Scopul este ca partea video să fie coerentă cu Studiu + Editor-Studiu deja reparate și să ducă C09 mai aproape de finalizare.

## DIRECȚIE CONCEPTUALĂ C09
C09 este construcția RELAȚII.

Rolul ei este să arate că analiza nu înseamnă doar coloane curate sau cifre corecte, ci legături corecte între entități.

AHA central:
Fără relații corecte, datele par valide, dar concluziile pot fi false.

C09 trebuie să facă vizibilă problema:
- tabele care par corecte separat;
- tabele care nu se potrivesc între ele;
- clienți fără tranzacții;
- tranzacții fără client valid;
- produse inexistente în nomenclator;
- categorii rupte de realitatea vânzărilor;
- relații care schimbă total analiza.

C09 trebuie să fie despre verificarea relațiilor, nu despre construirea BI.

## CADRU PEDAGOGIC
Respectă identitatea C09:
- relații;
- chei;
- potriviri;
- orfani;
- cardinalitate;
- integritate logică;
- verificare între tabele.

Nu transforma C09 în:
- Power BI;
- dashboard;
- modelare completă;
- DAX;
- raportare;
- BI-ready.

## CERINȚE HTML-VIDEO
Construiește varianta video C09 cu ton cinematografic, clar, orientat spre demonstrație.

Progres narativ obligatoriu:
1. Seturile par corecte separat.
2. În momentul unirii apar rupturile.
3. Relațiile greșite produc concluzii false.
4. Cursantul învață să verifice legătura înainte de analiză.
5. Finalul confirmă că analiza poate continua doar după ce relațiile sunt validate.

## CERINȚE EDITOR-VIDEO
Construiește companionul Editor-Video C09 în aceeași logică structurală cu celelalte construcții conforme.

Editorul trebuie să ajute la:
- filmare;
- ritm;
- accent vizual;
- observații pentru trainer;
- momente de pauză;
- evidențierea AHA-ului.

## REGULI DE STIL
- Fără em-dash.
- Fără en-dash.
- Fără cifre business concrete în HTML.
- Fără promisiuni de dashboard.
- Fără `BI-ready`.
- Fără terminologie de Power BI.
- Limbaj românesc, clar, profesional.
- C09 trebuie să aibă identitate proprie, nu să repete C06-C08.

## SCOPE PERMIS
Ai voie să modifici doar:
- `c09/**`
- `_brain/c09/CLAUDE-TO-BRAIN.md`

## SCOPE INTERZIS
Nu modifica:
- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `index.html`
- `_system/**`
- `gate_v20.py`
- `audit_sync.py`
- `COMENZI.yaml`
- fișiere din alte construcții.

Dacă apare nevoie de sistem, raportează `CERERE SYSTEM` în `_brain/c09/CLAUDE-TO-BRAIN.md`.

## OUTPUT AȘTEPTAT
După execuție, scrie raport în:
`_brain/c09/CLAUDE-TO-BRAIN.md`

Raportul trebuie să includă:
- ce fișiere ai creat sau modificat;
- ce ai păstrat din blueprint;
- ce riscuri există;
- ce nu ai modificat;
- dacă există CERERE SYSTEM;
- status final.

## STATUS AȘTEPTAT
Dacă totul este în regulă, statusul final trebuie să fie:
READY_FOR_BRAIN_REVIEW_VIDEO
