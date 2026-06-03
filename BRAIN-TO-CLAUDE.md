# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-015-REV1

## MANDAT
C09 RELAȚII, AUDIT COMPLET SISTEMIC înainte de orice alt livrabil C09.

## DECIZIE BRAIN IMPORTANTĂ
BRAIN anulează mandatul anterior BRAIN-014-REV1 ca direcție de execuție imediată.

Nu crea încă `HTML-Editor-Studiu-Excel-09-Relatii.html`.
Nu trece la Editor-Studiu, Video, Editor-Video, FILM, imagini sau index.

Motiv: înainte de orice companion C09 trebuie făcut un audit complet sistemic pe HTML-ul de bază și pe integrarea lui în arhitectura T3.

## REGULĂ PERMANENTĂ NOUĂ
Fișierele de editare NU se creează la cerere ca livrabile separate independente.

Fișierele de editare co-există cu fișierul de bază și trebuie să fie perfect sincronizate cu el.

Regula:
1. Dacă se modifică `HTML-Studiu`, atunci `HTML-Editor-Studiu` se regenerează sau se sincronizează obligatoriu în același ciclu de lucru.
2. Dacă se modifică `HTML-Video`, atunci `HTML-Editor-Video` se regenerează sau se sincronizează obligatoriu în același ciclu de lucru.
3. Fișierele de editare reflectă starea curentă a fișierului de bază, nu o versiune veche.
4. Nu se livrează un fișier de bază modificat fără companionul de editare sincronizat, decât dacă BRAIN cere explicit audit izolat sau prototip izolat.
5. Dacă HTML-ul de bază are probleme, NU generezi companionul. Întâi auditezi și repari baza.
6. Companionul de editare se face după stabilizarea bazei, nu înainte.

Această regulă trebuie tratată ca regulă durabilă Trainity.

## CONTEXT
BRAIN a analizat `c09/HTML-Studiu-Excel-09-Relatii.html` și a găsit semnale bune, dar și probleme de model pedagogic:

1. Identitatea C09 este corectă.
2. AHA-ul C09 este corect.
3. Cele 6 operații sunt în mare acoperite.
4. Join vs Union este explicat.
5. Granița C09/C10 este ținută.
6. Dar există inconsistență de model: în unele locuri se spune "patru tabele", deși modelul pedagogic este "un fact și patru dimensiuni".
7. În unele enumerări lipsește Regiuni.
8. Există risc de confuzie între foile din workbook și modelul analitic.

Nu aplica doar aceste fixuri punctual încă. Mai întâi faci audit complet sistemic.

## MODEL ANALITIC CANONIC C09-C12
Pentru C09, C10, C11, C12, modelul analitic de bază este:

Fact:
- Vanzari

Dimensiuni:
- PRODUSE
- CLIENTI
- Regiuni
- Calendar

Clarificare:
- START este foaie de onboarding, nu tabel de model.
- Relatii_Model este foaie pedagogică / control / documentare, nu tabel de business.
- AGENTI și DEPOZITE sunt hidden și există doar pentru contract tehnic DATA-CONTINUITY / gate. Nu le trata ca parte din modelul pedagogic principal.

Formula corectă:
"Fișierul are mai multe foi. Modelul are un fact și patru dimensiuni."

## DECIZII T3 LOCKED PENTRU AUDIT
Auditul trebuie să verifice dacă C09 pregătește corect traseul T3:

C09 construiește modelul.
C10 construiește cifra.
C11 construiește poziția.
C12 construiește sensul.

Relații → Măsuri → Comparații / Rank → Interpretare.

C10 include măsuri stabile, fact vs dimensiuni, schema star, filter context, validarea măsurii în contexte diferite și diferența măsură vs coloană.

Filter context intră obligatoriu în C10.

KPI nu este central în C10 ca dashboard. KPI se menționează doar ca diferență față de măsură: măsură = definiția stabilă a cifrei, KPI = măsură pusă față de target / prag / stare. KPI complet se dezvoltă în C11/C12/T4, nu în C10.

C11 include comparații, rank, top / bottom, sortare, poziție, ierarhie, diferență, abatere, contribuție, comparație față de medie / target / perioadă. Rank-ul este central în C11. C11 nu explică de ce, nu dă cauze, nu dă recomandări.

C12 include semnal vs zgomot, contextul rezultatului, ipoteze, explicație business controlată, risc posibil, oportunitate posibilă, ce merită investigat. C12 formulează ipoteze, nu cauze definitive.

## OBIECTIV AUDIT COMPLET
Auditează `c09/HTML-Studiu-Excel-09-Relatii.html` cap-coadă, cu standard de arhitect.

Nu te limita la gate_v20.
Nu te limita la tier_guard.
Nu te limita la audit_sync.

Fă audit conceptual, pedagogic, structural, tehnic, UX, T3, C09/C10/C11/C12, DATE, text, flow, promisiune, granițe, risc de confuzie.

## DOCUMENTE DE CITIT OBLIGATORIU
Citește:
- CLAUDE.md.
- STARE-CURENTA.md.
- BRAIN-TO-CLAUDE.md.
- CLAUDE-TO-BRAIN.md, raport BRAIN-013-REV1.
- c09/HTML-Studiu-Excel-09-Relatii.html.
- c09/Date_MASTER-C09.xlsx.
- c09/Creativ-Excel-09-Relatii.txt.
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md.
- _system/06-MAP-CONSTRUCTII-T1-T5.md.
- _system/blueprints/BLUEPRINT-C09-RELATII.md.
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md.
- _system/04-ARHITECTURA-LIVRABILE.md.
- _system/generatoare/gate_v20.py.
- _system/generatoare/tier_guard_t3.py.
- _system/generatoare/audit_sync.py.

## AUDITURI CERUTE
Fă raport separat pentru fiecare zonă:

A. Audit identitate C09: întrebarea construcției, AHA, mantra, miza business, promisiune, graniță față de C10/C11/C12.

B. Audit model DATE: fiecare apariție despre tabele, fact, dimensiuni, foi, model. Caută "patru tabele" vs "un fact și patru dimensiuni", enumerări incomplete, Regiuni lipsă, confuzie între foi și schema star.

C. Audit operații C09: verifică cele 6 operații, PK/FK/1:M, Inner/Left/Right/Union, Left/Right ca audit, Union ca reunire, model final.

D. Audit Join vs Union: verifică formula "Join leagă tabele diferite. Union adună tabele de același fel." și faptul că Union nu este prezentat ca relație clasică.

E. Audit SCENA 5 fenomene: verifică dacă sunt reale, clare, memorabile, fără alunecare spre C10/C11/C12.

F. Audit prompturi AI: verifică dacă prompturile accelerează verificarea, nu înlocuiesc gândirea cursantului, nu cer cifre finale, nu sar în măsuri / rank / interpretare.

G. Audit graniță C09/C10: fără măsuri numite, fără măsură vie, fără filter context dezvoltat, fără KPI dezvoltat.

H. Audit graniță C09/C11: fără rank predat, fără top / bottom predat, fără comparații de performanță. Breadcrumbul rămâne orientare, nu predare.

I. Audit graniță C09/C12: fără cauze, fără interpretare finală, fără verdict business.

J. Audit T4/T5: fără dashboard, fără raport publicabil, fără acțiuni, fără automatizare decizională.

K. Audit cifre business: fără cifre exacte din Excel ca rezultat static. Permis: zero orfani, 1:M, numere de pași / etape / verificări.

L. Audit UX / progresie pedagogică: verifică cele 6 etape, cei 18 pași, repetiții, etapa 5 stabilizare, logica progresiei.

M. Audit limbaj: română cu diacritice, fără termeni confuzi, fără fraze generice, fără contradicții, fără em-dash / en-dash.

N. Audit tehnic HTML: structură HTML, tag-uri închise, script, CSS, base64 hero, localStorage key C09, 18 pași, 8 verificări, responsive.

O. Audit anti-clonă C08: verifică urme conceptuale C08 în conținut, clase, comentarii, etichete, wording, identitate. CSS reutilizat ca schelă este permis, dar conținutul nu trebuie să fie C08.

P. Decizie: PASS curat / PASS cu fixuri punctuale / reparație majoră / reconstrucție.

Nu aplica fixuri în acest mandat decât dacă sunt buguri tehnice critice care împiedică auditul.

## FIȘIERE PERMISE
Ai voie să modifici doar:
- `CLAUDE-TO-BRAIN.md`.
- `STARE-CURENTA.md`, doar dacă fluxul standard cere actualizare.

Nu modifica HTML-ul în acest mandat.
Nu crea Editor-Studiu.
Nu crea Video.
Nu crea FILM.
Nu crea imagini.
Nu modifica index.html.

## VALIDĂRI AUTOMATE CERUTE
Pe lângă auditul manual complet, rulează:

1. `gate_v20 09 c09 c01`.
2. `tier_guard_t3` pentru C09.
3. `audit_sync`.
4. orice verificare HTML locală disponibilă în repo.
5. căutare text pentru termeni C10/C11/C12/T4/T5.
6. căutare text pentru cifre business statice.
7. căutare text pentru "patru tabele", "patru tabele separate", enumerări incomplete, Regiuni lipsă.
8. git diff ca să confirmi că HTML-ul nu a fost modificat.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet, structurat astfel:

1. Status.
2. Rezumat executiv.
3. Fișiere citite.
4. Validări automate rulate.
5. Audit identitate C09.
6. Audit model DATE.
7. Audit operații C09.
8. Audit Join vs Union.
9. Audit SCENA 5 fenomene.
10. Audit prompturi AI.
11. Audit graniță C09/C10.
12. Audit graniță C09/C11.
13. Audit graniță C09/C12.
14. Audit T4/T5.
15. Audit cifre business.
16. Audit UX / progresie pedagogică.
17. Audit limbaj.
18. Audit tehnic HTML.
19. Audit anti-clonă C08.
20. Lista completă de probleme găsite, cu severitate: BLOCKER / MAJOR / MINOR / WARN.
21. Fixuri recomandate, dar NU aplicate.
22. Decizie: PASS / PASS CU FIXURI / REPARAȚIE MAJORĂ / RECONSTRUCȚIE.
23. Ce NU ai modificat.
24. Ce rămâne de făcut după audit.
25. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-015-REV1.
Audit complet sistemic C09 HTML-Studiu.
Nu modifica HTML-ul.
Nu crea Editor-Studiu.
Nu trece la alte fișiere C09.
Raportează complet în CLAUDE-TO-BRAIN.md.
