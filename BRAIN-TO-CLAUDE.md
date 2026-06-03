# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-016-REV1

## MANDAT
C09 RELAȚII, fixuri punctuale după auditul sistemic.

Aplică doar corecțiile stabilite de raportul BRAIN-015-REV1 pe `c09/HTML-Studiu-Excel-09-Relatii.html`.

Nu crea încă Editor-Studiu.
Nu crea Video.
Nu crea Editor-Video.
Nu crea FILM.
Nu crea imagini noi.
Nu modifica index.html.

## CONTEXT
Am citit raportul `CLAUDE-TO-BRAIN.md` pentru BRAIN-015-REV1.

Decizia BRAIN:
- Accept decizia auditului: PASS CU FIXURI PUNCTUALE.
- Nu reconstruim C09.
- Nu mergem la companion înainte de stabilizarea HTML-ului de bază.
- Aplicăm fixurile punctuale MAJOR-1, MAJOR-2, MINOR-1, MINOR-2.

## REGULĂ DURABILĂ DE CODIFICAT ȘI ÎN CLAUDE.md
Actualizează `CLAUDE.md` cu regula durabilă despre companion files:

Fișierele de editare nu se creează la cerere ca livrabile independente. Ele co-există cu fișierul de bază și trebuie să fie sincronizate cu el.

Regula:
1. Dacă se modifică `HTML-Studiu`, atunci `HTML-Editor-Studiu` se regenerează sau se sincronizează în același ciclu de lucru, după stabilizarea bazei.
2. Dacă se modifică `HTML-Video`, atunci `HTML-Editor-Video` se regenerează sau se sincronizează în același ciclu de lucru, după stabilizarea bazei.
3. Companionul reflectă starea curentă a fișierului de bază.
4. Dacă HTML-ul de bază are probleme, întâi se auditează și se repară baza, apoi se face companionul.

Important: în acest mandat nu crea companionul C09. Doar codifici regula în `CLAUDE.md` și repari baza.

## FIXURI OBLIGATORII

### FIX 1, model DATE
Elimină formulările incorecte de tip "patru tabele" când se referă la modelul complet.

Modelul corect este:
- un fact: Vanzari.
- patru dimensiuni: PRODUSE, CLIENTI, Regiuni, Calendar.

Corectează aparițiile semnalate de audit:
- cover-subtitle / intro.
- before / after.
- dovada transformării.
- PAS 17.

Formulări recomandate:
- "Ai un fact și patru dimensiuni.".
- "Vanzari plus patru dimensiuni.".
- "tabele separate" dacă numărul nu este necesar.
- "un fact și patru dimensiuni, încă nelegate".
- "nu mai multe tabele alăturate".

Adaugă explicit formula BRAIN într-un loc potrivit, preferabil PAS 01 sau Raport AI:
"Fișierul are mai multe foi. Modelul are un fact și patru dimensiuni."

### FIX 2, hero vizual
Auditul a descoperit că hero-ul vizual din C09 este copiat din C08.

În acest mandat nu genera imagine nouă și nu crea assets.

Soluția cerută:
- elimină imaginea base64 copiată din C08 din HTML-Studiu C09.
- înlocuiește temporar cu placeholder vizual neutru, fără imagine externă, bazat pe CSS / fundal grafit / model relațional abstract simplu.
- placeholderul trebuie să transmită RELAȚII, nu CARTOGRAFIERE.
- nu introduce cifre business.

Placeholderul poate conține text vizual scurt:
"FACT → DIMENSIUNI → RĂSPUNS".

### FIX 3, hero blueprint
Aliniază hero-question și cover-title la slotul LOCKED:
"Cum transform legăturile în răspunsuri?"

Poți păstra ideea "tabelele răspund împreună" în corp, dar nu ca titlu principal.

### FIX 4, termenul "datate"
Elimină sau reformulează "datate" din cover-subtitle / intro.

Reformulare recomandată:
"Ai un fact, patru dimensiuni și date corecte. Și tot nu ai un răspuns care să le traverseze."

## CE NU SE MODIFICĂ
Nu schimba:
- cele 6 operații C09.
- SCENA 5 fenomene, decât dacă o formulare depinde de fixurile de mai sus.
- prompturile AI, decât dacă apar formulări contaminate.
- granițele C09/C10/C11/C12.
- structura 6 stages / 18 steps / 8 finals.
- index.html.
- Date_MASTER-C09.xlsx.
- Creativ-Excel-09-Relatii.txt.
- Video / Editor-Video / FILM / assets.

## FIȘIERE PERMISE
Ai voie să modifici doar:
- `c09/HTML-Studiu-Excel-09-Relatii.html`.
- `CLAUDE.md`, pentru regula durabilă despre companion files.
- `CLAUDE-TO-BRAIN.md`.
- `STARE-CURENTA.md`, doar dacă fluxul standard cere actualizare.

Nu crea `HTML-Editor-Studiu` în acest mandat.

## VALIDĂRI CERUTE
Rulează:
1. `gate_v20 09 c09 c01`.
2. `tier_guard_t3` pentru C09.
3. `audit_sync`.
4. verificare că nu mai există formulările incorecte "patru tabele" în contexte de model complet.
5. verificare că formula BRAIN despre fișier vs model există.
6. verificare că hero-ul C09 nu mai folosește imaginea copiată din C08.
7. verificare că nu există cifre business statice în text vizibil.
8. verificare că nu ai creat Editor-Studiu / Video / Editor-Video / FILM / assets.
9. verificare că index.html este neatins.
10. git diff sumar pentru fișiere modificate.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet:
1. Status.
2. Rezumat executiv.
3. Fișiere citite.
4. Fișiere modificate.
5. Fix model DATE aplicat.
6. Fix hero vizual aplicat.
7. Fix hero blueprint aplicat.
8. Fix termen "datate" aplicat.
9. Regula permanentă adăugată în CLAUDE.md.
10. Validări rulate.
11. PASS / WARNING / FAIL.
12. Ce nu ai modificat.
13. Decizie: baza C09 este stabilă sau mai cere audit.
14. Ce rămâne pentru pasul următor.
15. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-016-REV1.
Aplică fixurile punctuale post-audit pe HTML-Studiu C09.
Codifică regula companion files în CLAUDE.md.
Nu crea companionul încă.
Nu trece la alte fișiere C09.
