# BRAIN → CLAUDE · C09 RELAȚII

## STATUS
MANDAT_ACTIV

## MANDAT-ID
C09-M021-FILM

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

C09-M020-VIDEO-EDITOR-VIDEO a fost executat cu status READY_FOR_BRAIN_REVIEW_VIDEO.

Claude a creat:
- `c09/HTML-Video-Excel-09-Relatii.html`
- `c09/HTML-Editor-Video-Excel-09-Relatii.html`

Conform raportului Claude:
- Video și Editor-Video sunt curate pe em-dash / en-dash.
- Nu conțin cifre business concrete.
- Nu conțin Power BI / DAX / Power Pivot / BI-ready / dashboard.
- GATE PASS pe 5/5 livrabile prezente.
- JS PASS.
- Lipsesc încă cele 6 imagini exec-stage RELAȚII.
- FILM C09 este următorul livrabil separat.

## MANDAT ACTIV
Construiește FILM C09 RELAȚII.

## OBIECTIV
Generează livrabilul:
- `c09/FILM-Excel-09-Relatii.docx`

FILM trebuie să fie companionul de filmare al C09 și să fie coerent cu:
- Studiu C09;
- Editor-Studiu C09;
- HTML-Video C09;
- HTML-Editor-Video C09.

## DIRECȚIE CONCEPTUALĂ C09
C09 este construcția RELAȚII.

AHA central:
Fără relații corecte, datele par valide, dar concluziile pot fi false.

FILM trebuie să arate clar că:
- tabelele pot fi corecte separat;
- adevărul apare doar când legăturile sunt testate;
- o cheie greșită schimbă analiza;
- un Join greșit ascunde date;
- un Union greșit amestecă structuri;
- orfanii, duplicatele și cardinalitatea greșită trebuie văzute înainte de analiză;
- C09 nu construiește raport, ci stabilizează legătura dintre tabele.

## PROGRES NARATIV OBLIGATORIU
FILM trebuie să păstreze progresia video:
1. Seturile par corecte separat.
2. În momentul unirii apar rupturile.
3. Relațiile greșite produc concluzii false.
4. Cursantul învață să verifice legătura înainte de analiză.
5. Finalul confirmă că analiza poate continua doar după ce relațiile sunt validate.

## CADRU PEDAGOGIC
FILM trebuie să fie util pentru trainer la filmare, nu doar o rescriere de HTML.

Include:
- intenția fiecărei secvențe;
- ce trebuie demonstrat pe ecran;
- ce trebuie spus vocal;
- unde se face pauză;
- unde se marchează AHA-ul;
- unde se insistă pe diferența Join / Union;
- unde se arată rolul Left / Right ca audit al potrivirilor lipsă;
- unde se confirmă trecerea către C10.

## STRUCTURĂ CERUTĂ
Respectă structura standard de FILM folosită în construcțiile conforme:
- titlu și meta C09;
- obiectiv de filmare;
- setup narativ;
- secvențe de filmare pe pași;
- indicații de ecran;
- indicații de voce;
- momente AHA / WOW;
- concluzie;
- handoff către C10.

Dacă există un FILM conform în C08 sau altă construcție, folosește-l doar ca schelet structural, nu copia narativul.

## REGULI DE STIL
- Fără em-dash.
- Fără en-dash.
- Fără cifre business concrete.
- Fără Power BI.
- Fără DAX.
- Fără Power Pivot.
- Fără dashboard.
- Fără `BI-ready`.
- Fără formulări de raportare finală.
- Fără transformarea C09 în modelare BI.
- Limbaj românesc, clar, filmabil, profesional.
- C09 trebuie să rămână despre relații, chei, potriviri, orfani, cardinalitate și integritate logică.

## IMAGINI
Nu integra imagini acum.
Nu inventa assets.
Nu modifica `assets/`.
Cele 6 imagini exec-stage RELAȚII rămân dependență ARHITECT și vor primi mandat separat.

## SCOPE PERMIS
Ai voie să modifici doar:
- `c09/FILM-Excel-09-Relatii.docx`
- `_brain/c09/CLAUDE-TO-BRAIN.md`

Dacă ai nevoie să citești alte fișiere C09 sau C08 ca referință structurală, citește-le doar pentru context, fără modificare.

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
- fișiere din alte construcții;
- HTML-Studiu C09;
- HTML-Editor-Studiu C09;
- HTML-Video C09;
- HTML-Editor-Video C09;
- Date_MASTER-C09;
- `c09/assets/**`.

Dacă apare nevoie de sistem, raportează `CERERE SYSTEM` în `_brain/c09/CLAUDE-TO-BRAIN.md`.

## VALIDARE AȘTEPTATĂ
După generare:
- verifică existența FILM C09;
- verifică termenii interziși;
- verifică em-dash / en-dash;
- verifică faptul că nu ai introdus cifre business concrete;
- rulează validările disponibile fără a modifica sistemul.

## OUTPUT AȘTEPTAT
După execuție, scrie raport în:
`_brain/c09/CLAUDE-TO-BRAIN.md`

Raportul trebuie să includă:
- fișiere create sau modificate;
- sursa structurală folosită, dacă ai folosit una;
- ce ai păstrat din identitatea C09;
- ce ai evitat explicit;
- validări rulate;
- riscuri rămase;
- dacă există CERERE SYSTEM;
- status final.

## STATUS AȘTEPTAT
Dacă totul este în regulă, statusul final trebuie să fie:
READY_FOR_BRAIN_REVIEW_FILM
