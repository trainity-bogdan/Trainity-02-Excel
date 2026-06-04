# BRAIN → CLAUDE · C09 RELAȚII

## STATUS
MANDAT_ACTIV

## MANDAT-ID
C09-M022-FINAL-REVIEW

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
C09-M020-VIDEO-EDITOR-VIDEO a fost executat cu status READY_FOR_BRAIN_REVIEW_VIDEO.

Claude a creat:
- `c09/HTML-Video-Excel-09-Relatii.html`
- `c09/HTML-Editor-Video-Excel-09-Relatii.html`

C09-M021-FILM a fost executat cu status READY_FOR_BRAIN_REVIEW_FILM.

Claude a creat:
- `c09/FILM-Excel-09-Relatii.docx`

Conform ultimului raport Claude:
- toate cele 6 imagini exec-stage RELAȚII sunt integrate;
- base64 integrat în Video + Editor-Video;
- jpg-urile sunt în assets;
- watermark scos;
- audit_sync C09 = ZERO DRIFT;
- GATE PASS;
- JS valid;
- FILM C09 prezent.

## MANDAT ACTIV
Execută review final C09 RELAȚII și pregătește raport de închidere.

## OBIECTIV
Verifică empiric că C09 este completă și gata pentru review final ARHITECT.

Nu genera conținut nou decât dacă descoperi defecte minore strict în `c09/**` care trebuie reparate pentru PASS.

## CHECKLIST FINAL C09
Verifică existența și integritatea livrabilelor C09:
- HTML-Studiu C09;
- HTML-Editor-Studiu C09;
- HTML-Video C09;
- HTML-Editor-Video C09;
- Date_MASTER-C09;
- Creativ C09, dacă există în schema construcției;
- FILM C09;
- `c09/assets/**` cu cele 6 imagini exec-stage jpg.

## VALIDĂRI OBLIGATORII
Rulează validările disponibile fără modificări de sistem:
- gate C09;
- audit_sync;
- verificare termeni interziși;
- verificare em-dash / en-dash;
- verificare cifre business concrete în HTML și FILM;
- verificare JS pentru HTML-Video și HTML-Editor-Video;
- verificare că nu există Power BI / DAX / Power Pivot / dashboard / BI-ready;
- verificare că nu există contaminare C06-C08 sau C10-C12 în identitatea C09, cu excepția handoff-urilor legitime.

## CRITERIU DE ACCEPTARE
C09 poate fi marcată READY_FOR_FINAL_REVIEW_C09 doar dacă:
- toate livrabilele sunt prezente;
- C09 are ZERO DRIFT;
- GATE PASS;
- imaginile exec-stage sunt 6/6;
- FILM este prezent;
- nu există CERERE SYSTEM;
- nu există blocante pedagogice.

## IDENTITATE C09 DE CONFIRMAT
Confirmă explicit că C09 rămâne despre:
- relații între tabele;
- chei;
- potriviri;
- orfani;
- cardinalitate;
- integritate logică;
- Join vs Union;
- Left / Right ca audit al potrivirilor lipsă;
- stabilizarea legăturii înainte de analiză.

Confirmă explicit că C09 nu devine:
- Power BI;
- dashboard;
- modelare completă BI;
- DAX;
- raportare finală;
- ranking/top/Pareto;
- interpretare de cauze.

## SCOPE PERMIS
Ai voie să modifici doar:
- `c09/**`, strict dacă există defect minor care blochează PASS;
- `_brain/c09/CLAUDE-TO-BRAIN.md`.

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
Scrie raport final în:
`_brain/c09/CLAUDE-TO-BRAIN.md`

Raportul trebuie să includă:
- status final;
- lista livrabilelor C09 prezente;
- validările rulate și rezultatul lor;
- eventualele reparații minore aplicate, dacă au existat;
- riscuri rămase, dacă există;
- confirmarea ZERO DRIFT;
- confirmarea GATE PASS;
- confirmarea 6/6 imagini;
- confirmarea FILM prezent;
- confirmarea că nu există CERERE SYSTEM.

## STATUS AȘTEPTAT
Dacă totul este în regulă, statusul final trebuie să fie:
READY_FOR_FINAL_REVIEW_C09
