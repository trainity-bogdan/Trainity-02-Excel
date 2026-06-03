# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-017-REV1

## MANDAT
C09 RELAȚII, generează `HTML-Editor-Studiu-Excel-09-Relatii.html`, sincronizat perfect cu HTML-Studiu C09 stabilizat.

## CONTEXT
Am citit raportul `CLAUDE-TO-BRAIN.md` pentru BRAIN-016-REV1.

Decizia BRAIN:
- Baza C09 este stabilă.
- Cele 4 fixuri post-audit sunt acceptate.
- Regula companion files a fost codificată în CLAUDE.md.
- Acum este permis să generezi companionul Editor-Studiu, pentru că baza este stabilizată.

## REGULĂ CRITICĂ
Acest Editor-Studiu nu este un livrabil făcut la cerere.

Este companion sincronizat cu baza stabilă:
`c09/HTML-Studiu-Excel-09-Relatii.html`.

Companionul trebuie să reflecte starea curentă a bazei după BRAIN-016-REV1, inclusiv:
- hero-title LOCKED: "Cum transform legăturile în răspunsuri?".
- model corect: un fact și patru dimensiuni.
- formula: "Fișierul are mai multe foi. Modelul are un fact și patru dimensiuni.".
- placeholder hero RELAȚII, fără base64 C08.
- zero formulări incorecte "patru tabele" în contexte de model complet.

## OBIECTIV
Creează:
`c09/HTML-Editor-Studiu-Excel-09-Relatii.html`

Scop:
- companion de editare și control pentru HTML-Studiu C09.
- reflectă exact structura, identitatea, pașii, verificările și granițele HTML-Studiu C09.
- permite revizuirea textelor C09 fără să rupă arhitectura.
- marchează clar zonele editabile și zonele LOCKED.
- include controale de sincronizare cu baza.

## DOCUMENTE DE CITIT OBLIGATORIU
Citește:
- CLAUDE.md.
- STARE-CURENTA.md.
- BRAIN-TO-CLAUDE.md.
- CLAUDE-TO-BRAIN.md, raport BRAIN-016-REV1.
- c09/HTML-Studiu-Excel-09-Relatii.html.
- c09/Date_MASTER-C09.xlsx.
- c09/Creativ-Excel-09-Relatii.txt.
- companioni Editor-Studiu existenți C05-C08, ca schelet tehnic și standard UX, nu ca text de copiat.
- _system/04-ARHITECTURA-LIVRABILE.md.
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md.
- _system/blueprints/BLUEPRINT-C09-RELATII.md.
- _system/generatoare/gate_v20.py.
- _system/generatoare/tier_guard_t3.py.
- _system/generatoare/audit_sync.py.

## CE TREBUIE SĂ CONȚINĂ EDITOR-STUDIU C09
Include cel puțin:

1. Meta construcție C09.
2. Identitate C09.
3. Hero locked: "Cum transform legăturile în răspunsuri?".
4. AHA locked: "Fără relații ai date. Cu relații ai răspunsuri.".
5. Mantra: "Nu mutăm datele. Le legăm.".
6. Model DATE: un fact, Vanzari, și patru dimensiuni, PRODUSE, CLIENTI, Regiuni, Calendar.
7. Formula locked: "Fișierul are mai multe foi. Modelul are un fact și patru dimensiuni.".
8. Cele 6 operații C09.
9. SCENA 5 fenomene.
10. Cele 2 prompturi AI.
11. Cele 6 etape și 18 pași.
12. Cele 8 verificări finale.
13. Handoff C09 -> C10.
14. Controale anti-contaminare C10/C11/C12/T4/T5.
15. Controale anti-cifre business statice.
16. Controale anti-clonă C08, inclusiv verificare hero vizual.
17. Zone editabile.
18. Zone LOCKED.
19. Checklist de sincronizare cu HTML-Studiu.

## ZONE LOCKED
Marchează clar ca LOCKED:
- Hero-title: "Cum transform legăturile în răspunsuri?".
- AHA: "Fără relații ai date. Cu relații ai răspunsuri.".
- Formula model: "Fișierul are mai multe foi. Modelul are un fact și patru dimensiuni.".
- Formula Join vs Union: "Join leagă tabele diferite. Union adună tabele de același fel.".
- C09 nu definește măsuri.
- C09 nu predă filter context.
- C09 nu dezvoltă KPI.
- C09 nu face rank.
- C09 nu face top / bottom.
- C09 nu interpretează cauze.
- C09 nu produce dashboard.
- C09 nu dă acțiuni.

## ZONE EDITABILE
Permite editare controlată pentru:
- formulări de introducere.
- microcopy de pași.
- exemple pedagogice fără cifre finale.
- text de prompt AI, păstrând scopul de verificare.
- explicații scurte pentru learner.
- formulări de payoff, dacă nu rup locked slots.

## SINCRONIZARE CU BAZA
Editor-Studiu trebuie să fie sincronizat cu baza stabilizată.

Verifică explicit:
- titlul din Editor = titlul din HTML-Studiu.
- AHA din Editor = AHA din HTML-Studiu.
- lista celor 18 pași = lista din HTML-Studiu.
- cele 8 verificări finale = lista din HTML-Studiu.
- cele 5 fenomene = lista din HTML-Studiu.
- cele 2 prompturi AI = prompturile din HTML-Studiu.
- modelul DATE = formula corectă.
- nu apare hero base64 C08.

## FIȘIERE PERMISE
Ai voie să modifici / creezi doar:
- `c09/HTML-Editor-Studiu-Excel-09-Relatii.html`.
- `CLAUDE-TO-BRAIN.md`.
- `STARE-CURENTA.md`, doar dacă fluxul standard cere actualizare.

Nu modifica `c09/HTML-Studiu-Excel-09-Relatii.html` în acest mandat, decât dacă descoperi o eroare critică de sincronizare și o explici explicit.

Nu modifica:
- index.html.
- Date_MASTER-C09.xlsx.
- Creativ-Excel-09-Relatii.txt.
- Video C09.
- Editor-Video C09.
- FILM C09.
- assets / imagini.
- C01-C08.
- C10-C12.
- generatoare.
- governance / Bible / doc 12 / 06-MAP.

## VALIDĂRI CERUTE
Rulează:
1. `gate_v20 09 c09 c01`.
2. `tier_guard_t3` pentru C09.
3. `audit_sync`.
4. verificare sincronizare HTML-Studiu vs HTML-Editor-Studiu.
5. verificare că Editor-Studiu conține 18 pași, 8 verificări, 5 fenomene, 2 prompturi.
6. verificare că Editor-Studiu nu introduce măsuri / filter context / KPI / rank / dashboard / cauze.
7. verificare că Editor-Studiu nu conține cifre business statice.
8. verificare că index.html este neatins.
9. verificare că nu ai creat Video / Editor-Video / FILM / assets.
10. git diff sumar.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet:
1. Status.
2. Rezumat executiv.
3. Fișiere citite.
4. Fișiere create / modificate.
5. Structura Editor-Studiu C09.
6. Cum este sincronizat cu HTML-Studiu.
7. Zone LOCKED.
8. Zone editabile.
9. Cum păstrează axa RELAȚII.
10. Cum păstrează modelul un fact + patru dimensiuni.
11. Cum păstrează cele 6 operații.
12. Cum păstrează SCENA 5 fenomene.
13. Cum păstrează prompturile AI.
14. Cum respectă granițele C09/C10/C11/C12/T4/T5.
15. Validări rulate.
16. PASS / WARNING / FAIL.
17. Ce nu ai modificat.
18. Ce rămâne pentru pasul următor.
19. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-017-REV1.
Generează doar HTML-Editor-Studiu C09, sincronizat cu HTML-Studiu stabilizat.
Zero Video.
Zero Editor-Video.
Zero FILM.
Zero imagini.
Zero index.html.
