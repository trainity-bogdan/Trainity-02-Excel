# BRAIN → CLAUDE · C09 RELAȚII

## STATUS
MANDAT_ACTIV

## MANDAT-ID
C09-M026-FIX-HERO-REPETITION

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
C09 RELAȚII este finală după MONSTER AUDIT, dar Bogdan a observat vizual în preview o problemă minoră de compoziție:

Aceeași întrebare apare de două ori foarte aproape:
- în hero: `Cum transform legăturile în răspunsuri?`
- imediat sub taburi, ca titlu de secțiune: `Cum transform legăturile în răspunsuri?`

Aceasta creează dublare vizuală și impresie de repetiție neintenționată.

## MANDAT ACTIV
Repară dublarea headline-ului în C09.

## OBIECTIV
Păstrează hero-ul:
`Cum transform legăturile în răspunsuri?`

Schimbă titlul secțiunii imediat următoare într-o formulare complementară, nu repetitivă.

Variantă recomandată:
`Datele nu răspund până nu sunt legate corect`

## SCOPE
Verifică și repară dublarea acolo unde apare în livrabilele C09:
- `c09/HTML-Studiu-Excel-09-Relatii.html`
- `c09/HTML-Editor-Studiu-Excel-09-Relatii.html`
- `c09/HTML-Video-Excel-09-Relatii.html`
- `c09/HTML-Editor-Video-Excel-09-Relatii.html`

Nu modifica `index.html`.
Nu modifica fișiere sistem.
Nu modifica alte construcții.
Nu modifica Date_MASTER sau FILM decât dacă aceeași dublare apare explicit și afectează coerența.

## REGULI
- păstrează identitatea C09 RELAȚII;
- nu schimba structura majoră;
- nu schimba hero-ul;
- repară doar titlul repetat de sub taburi;
- menține limbajul clar, Trainity, filmabil;
- fără em-dash;
- fără en-dash;
- fără termeni BI interziși;
- fără cifre business concrete.

## VALIDARE
După fix:
- verifică faptul că întrebarea nu mai apare duplicat vizual în aceeași zonă;
- rulează validările disponibile pentru C09;
- confirmă GATE PASS;
- confirmă C09 ZERO DRIFT sau explică dacă apare un false positive;
- confirmă JS valid dacă ai atins HTML-Video / HTML-Editor-Video;
- confirmă 0 em-dash / en-dash;
- confirmă 0 termeni interziși.

## OUTPUT AȘTEPTAT
Scrie raport în:
`_brain/c09/CLAUDE-TO-BRAIN.md`

Raportul trebuie să includă:
- fișiere modificate;
- text vechi;
- text nou;
- validări rulate;
- rezultat final;
- status final.

## STATUS AȘTEPTAT
READY_FINAL_C09_HERO_REPETITION_FIXED
