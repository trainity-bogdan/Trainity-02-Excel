# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-019-REV1

## MANDAT
Elimină din sistem specificațiile legate de fișierul `Creativ-Excel-*.txt` și stabilește continuarea C09 fără acest fișier.

## CONTEXT
Am citit raportul tău pentru BRAIN-018-REV1.

Ultimul tău verdict:
- Editor-Studiu C09 = PASS CU FIXURI.
- 0 BLOCKER.
- Hero-ul placeholder CSS = MAJOR UX, acceptabil doar temporar.
- C09 are nevoie de hero real sau standard vizual coerent înainte de livrare finală.
- Nu ai modificat HTML-Studiu / Editor-Studiu în mandatul de audit.

BRAIN confirmă observația despre hero:
- placeholderul actual NU este hero final.
- BRAIN a dat separat indicații despre hero și prompt Banana.
- Nu folosi fișierul Creativ ca sursă pentru prompturi sau pentru imagini.

## DECIZIE NOUĂ BRAIN, DEFINITIVĂ
Renunțăm complet la fișierul de Creative / prompturi.

Fișierele de tip:
`Creativ-Excel-XX-*.txt`

NU mai sunt livrabile canonice.
NU mai sunt sursă obligatorie.
NU mai sunt citite obligatoriu.
NU mai sunt cerute de gate.
NU mai sunt folosite ca sursă pentru imagini, hero, exec-stage sau video.
NU mai apar în checklisturi active.

Prompturile vizuale se dau direct de BRAIN în mandat, în chat sau ca fișiere dedicate punctual, nu printr-un fișier `Creativ` per construcție.

## PRINCIPIU NOU
Arhitectura rămâne:
- HTML-Studiu.
- HTML-Editor-Studiu.
- HTML-Video.
- HTML-Editor-Video.
- FILM.
- Date_MASTER.
- assets, doar când există imagini reale.

Se elimină:
- Creative prompt file ca livrabil canonic.
- dependența de `Creativ-Excel-*.txt` în generare.
- obligația de a-l citi înainte de HTML / Video / FILM.

## OBIECTIV MANDAT
Fă cleanup sistemic, nu doar local C09.

1. Identifică toate referințele active la `Creativ-Excel` / `Creativ` ca livrabil obligatoriu.
2. Elimină-le sau marchează-le ca legacy, în funcție de loc:
   - în documentele active, elimină din livrabile canonice și din flow.
   - în arhivă, nu modifica decât dacă documentul este activ operațional.
   - în gate / audit, nu trebuie să mai fie condiție de PASS.
3. Pentru C09, elimină obligația de a citi `c09/Creativ-Excel-09-Relatii.txt`.
4. Dacă fișierul `c09/Creativ-Excel-09-Relatii.txt` este folosit doar ca prompt bank și nu mai are rol tehnic, șterge-l sau marchează-l ca deprecated, dar NU lăsa sistemul să depindă de el.
5. Actualizează CLAUDE.md cu regula nouă: fără Creative prompt file canonic.
6. Actualizează STARE-CURENTA.md dacă fluxul standard cere.
7. Raportează exact ce ai schimbat și ce referințe rămân doar ca legacy.

## DOCUMENTE / FIȘIERE DE VERIFICAT
Caută cel puțin în:
- CLAUDE.md.
- README.md.
- STARE-CURENTA.md.
- _system/04-ARHITECTURA-LIVRABILE.md.
- _system/COMENZI.yaml.
- _system/generatoare/gate_v20.py.
- _system/generatoare/audit_sync.py.
- _system/referinte/IDENTITATE-TEHNICA.md.
- _system/referinte/PROTOCOL-FILM-OBS.md.
- BRAIN-TO-CLAUDE.md.
- orice fișier activ unde apare `Creativ-Excel`.

Poți ignora arhiva istorică dacă este clar arhivă și nu controlează fluxul actual.

## IMPORTANT, C09 CONTINUARE
Nu trece încă la Video.

După cleanup, următorul pas C09 trebuie să fie decis astfel:

A. Dacă există deja imagine hero reală C09 livrată de BRAIN / Banana / Gemini în repo sau atașată explicit, integreaz-o în:
- HTML-Studiu C09.
- HTML-Editor-Studiu C09, sincronizat cu baza.

B. Dacă NU există imagine hero reală disponibilă, NU inventa imagine și NU folosi fișierul Creativ. Raportează că hero-ul rămâne datorie UX și cere assetul sau confirmarea pentru hero CSS standardizat.

C. Nu genera exec-stage images din Creative. Pentru imagini, așteaptă fie assets reale, fie prompturi directe de la BRAIN.

## FIXURI C09 DE LUAT ÎN CALCUL DUPĂ CLEANUP, NU ÎN ACEST MANDAT DECÂT DACĂ SUNT STRICT NECESARE
Din auditul BRAIN-018 au rămas:
- MINOR-1: MANTRA, MOTTO, hero-question-text sunt sigure, dar fără badge LOCKED vizual.
- MINOR-2: formula Join/Union în corp este non-canonică față de forma locked.
- MINOR-3: over-locking pe PAS 01 și PAS 09.
- MINOR-4: panoul companion înalt pe mobil.
- WARN: lock-by-phrase fragil, ar trebui înlocuit pe termen mediu cu lock-by-attribute.

Nu aplica aceste fixuri în mandatul de cleanup decât dacă actualizarea sistemică cere atingerea Editor-Studiu.

## FIȘIERE PERMISE
Ai voie să modifici:
- CLAUDE.md.
- README.md, dacă are specificații active.
- STARE-CURENTA.md, dacă fluxul cere.
- _system/04-ARHITECTURA-LIVRABILE.md.
- _system/COMENZI.yaml.
- _system/generatoare/gate_v20.py.
- _system/generatoare/audit_sync.py.
- _system/referinte/IDENTITATE-TEHNICA.md.
- _system/referinte/PROTOCOL-FILM-OBS.md.
- c09/Creativ-Excel-09-Relatii.txt, doar pentru ștergere / deprecated, dacă după analiză nu mai trebuie păstrat.
- CLAUDE-TO-BRAIN.md.

Nu modifica:
- HTML-Studiu C09.
- HTML-Editor-Studiu C09.
- Video / Editor-Video / FILM.
- assets.
- index.html.
- Date_MASTER-C09.xlsx.
- C01-C08, decât dacă un fișier activ de sistem cere ajustare de referință și explici clar.

## VALIDĂRI CERUTE
Rulează:
1. căutare globală `Creativ-Excel`.
2. căutare globală `Creativ` în documente active.
3. gate_v20 pentru C09.
4. audit_sync.
5. verificare că niciun gate nu mai cere Creative ca livrabil.
6. verificare că HTML-Studiu și HTML-Editor-Studiu C09 au rămas neatinse.
7. git diff sumar.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet:
1. Status.
2. Rezumat executiv.
3. Fișiere verificate.
4. Referințe Creativ găsite.
5. Ce ai eliminat din sistemul activ.
6. Ce ai lăsat ca legacy și de ce.
7. Ce ai schimbat în gate / audit.
8. Ce ai schimbat în CLAUDE.md.
9. Stare C09 după cleanup.
10. Decizie despre hero C09: asset existent sau asset lipsă.
11. Validări rulate.
12. PASS / WARNING / FAIL.
13. Ce nu ai modificat.
14. Ce trebuie făcut după acest mandat.
15. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-019-REV1.
Cleanup sistemic: fără fișier Creative / prompturi ca livrabil canonic.
Nu trece la Video.
Nu modifica HTML-Studiu / Editor-Studiu în acest mandat.
