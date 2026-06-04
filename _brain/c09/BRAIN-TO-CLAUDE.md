# BRAIN → CLAUDE · C09 RELAȚII

## STATUS
MANDAT_ACTIV

## MANDAT-ID
C09-M023-MONSTER-AUDIT

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
C09 este raportată de Claude ca `READY_FOR_FINAL_REVIEW_C09`.

Ultimul raport confirmă:
- toate livrabilele C09 prezente;
- GATE PASS;
- C09 ZERO DRIFT;
- 6/6 imagini exec-stage integrate;
- FILM prezent;
- JS valid;
- fără termeni interziși;
- fără em-dash / en-dash;
- fără cifre business concrete;
- fără CERERE SYSTEM;
- fără blocante pedagogice.

## MANDAT ACTIV
Execută AUDIT MONSTRU C09 RELAȚII.

Acesta nu este un audit de bifă. Este un audit adversarial, brutal, complet, pentru a încerca să distrugă C09 înainte să o declare finală.

## OBIECTIV
Verifică dacă C09 poate fi considerată finală nu doar tehnic, ci și pedagogic, narativ, vizual, structural și operațional.

Nu genera conținut nou decât dacă descoperi defecte reale în `c09/**` care trebuie reparate.

Dacă există defecte reparabile local, repară-le în `c09/**`, apoi rulează din nou validările și raportează exact ce ai reparat.

Dacă există defect de sistem, nu modifica sistemul. Scrie CERERE SYSTEM în `_brain/c09/CLAUDE-TO-BRAIN.md`.

## AUDIT TEHNIC EXTINS
Verifică:
- toate fișierele C09 prezente;
- nume fișiere corecte;
- HTML-uri deschizibile;
- JS valid în HTML-Video și HTML-Editor-Video;
- Editor-Studiu și Editor-Video funcționează ca pagini editor;
- localStorage keys nu se bat cu alte construcții;
- navigația pași / fragmente funcționează;
- butoanele nu sunt lipite;
- panourile editor sunt utilizabile;
- mobile/responsive nu rupe layout-ul evident;
- nu există referințe către fișiere externe lipsă;
- imaginile exec-stage sunt 6/6;
- imaginile sunt unice și nu clone C01-C08;
- base64 există în Video și Editor-Video unde trebuie;
- assets conține jpg-urile corecte;
- FILM este valid docx;
- Date_MASTER-C09 există și poate fi deschis;
- nu există artefacte temporare, backup-uri, scripturi de lucru sau fișiere accidentale în c09.

## AUDIT DE CONȚINUT
Verifică strict:
- C09 este despre relații, nu despre modelare BI;
- Join vs Union este explicat clar și corect;
- Left / Right sunt folosite ca audit al potrivirilor lipsă;
- Inner Join nu este prezentat ca soluție universală;
- Union nu este prezentat ca relație;
- cheile PK/FK sunt coerente;
- cardinalitatea 1:1 / 1:M este folosită corect;
- orfanii sunt tratați ca risc logic;
- duplicatele sunt tratate ca risc de relație;
- granularitatea nu este amestecată cu agregarea;
- stabilizarea relațiilor este înainte de analiză;
- handoff-ul către C10 este legitim, fără să execute C10;
- handoff-ul din C08 este legitim, fără contaminare narativă.

## AUDIT PEDAGOGIC
Verifică:
- AHA-ul este clar;
- WOW-ul există;
- cursantul înțelege de ce un tabel singur nu răspunde;
- cursantul înțelege de ce tabelele pot fi corecte separat, dar greșite împreună;
- nu există salturi pedagogice;
- nu există concepte introduse fără pregătire;
- pașii au progres logic;
- finalul pregătește C10 fără să promită raportare;
- filmul este filmabil de un trainer real;
- indicațiile din FILM sunt utile, nu decorative.

## AUDIT NARATIV ȘI TRAINITY
Verifică:
- intriga este puternică;
- progresia este cinematică;
- limbajul este clar, rapid, ușor, fără efort inutil;
- nu există fraze plate sau generice;
- nu există ton de manual vechi;
- nu există exces de abstractizare;
- polarizarea controlată funcționează;
- C09 are identitate proprie față de C06-C08;
- motto-ul și mantra sunt aliniate cu relațiile.

## AUDIT DE CONTAMINARE
Caută și raportează explicit orice apariție problematică de:
- C06, C07, C08, C10, C11, C12;
- top, ranking, Pareto, măsură, dashboard, raportare finală, Power BI, DAX, Power Pivot, BI-ready, Power Query;
- cartografiere, ecosistem, satelit, hartă, dacă apar în afara handoff-ului legitim din C08;
- comparații, rank, variații, cauze, decizii, dacă apar ca funcție executată în C09.

Handoff legitim permis:
- C08 ca input anterior;
- C10 ca pas următor.

Orice altă contaminare trebuie clasificată:
- BLOCKER;
- MAJOR;
- MINOR;
- FALSE POSITIVE.

## AUDIT DE STIL
Verifică:
- fără em-dash;
- fără en-dash;
- fără cifre business concrete;
- fără simboluri sau formulări care trădează copy AI;
- fără limbaj pompos inutil;
- fără fraze lungi imposibil de filmat;
- fără inconsecvențe între Studiu, Video și FILM;
- fără diferențe de terminologie între livrabile.

## VALIDĂRI OBLIGATORII
Rulează tot ce este disponibil fără modificare de sistem:
- gate C09;
- audit_sync;
- tier_guard_t3 C09;
- verificare JS;
- scan termeni interziși;
- scan em-dash / en-dash;
- scan cifre business;
- scan contaminare;
- verificare assets;
- verificare docx;
- verificare Date_MASTER-C09.

## RAPORT AȘTEPTAT
Scrie raport complet în:
`_brain/c09/CLAUDE-TO-BRAIN.md`

Raportul trebuie să aibă structură clară:
1. STATUS FINAL.
2. Verdict scurt: FINAL / NU FINAL.
3. Audit tehnic.
4. Audit conținut.
5. Audit pedagogic.
6. Audit narativ.
7. Audit contaminare.
8. Audit stil.
9. Validări rulate.
10. Defecte găsite, cu severitate.
11. Reparații aplicate, dacă există.
12. Riscuri rămase.
13. CERERE SYSTEM, dacă există.
14. Recomandare finală BRAIN.

## CRITERIU DE ACCEPTARE
C09 poate rămâne finală doar dacă după audit monstru:
- nu există BLOCKER;
- nu există MAJOR nerezolvat;
- C09 rămâne ZERO DRIFT;
- GATE PASS;
- 6/6 imagini;
- FILM prezent;
- nu există CERERE SYSTEM;
- identitatea RELAȚII este curată.

## STATUS AȘTEPTAT
Dacă auditul monstru confirmă finalizarea:
READY_FINAL_C09_MONSTER_PASS

Dacă există defecte reparabile și le repari:
READY_FINAL_C09_MONSTER_PASS_AFTER_FIX

Dacă există defecte nerezolvate:
C09_MONSTER_AUDIT_FAILED
