# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-014-REV1

## MANDAT
C09 RELAȚII, SLICE 3A: creează companionul `HTML-Editor-Studiu-Excel-09-Relatii.html` pentru HTML-Studiu C09 deja livrat, fără Video, fără Editor-Video, fără FILM, fără imagini, fără index.html.

## CONTEXT RAPORT CLAUDE
Am citit raportul `CLAUDE-TO-BRAIN.md` pentru BRAIN-013-REV1.

Confirm că BRAIN-013-REV1 este acceptat ca SLICE 2 C09:
- `c09/HTML-Studiu-Excel-09-Relatii.html` este creat.
- Este autorat genuin pe RELAȚII.
- Are cele 6 operații C09.
- Are SCENA 5 fenomene.
- Are 2 prompturi AI.
- Respectă granițele C09/C10/C11/C12/T4/T5.
- GATE PASS.
- tier_guard are 0 blocante.
- audit_sync C01-C08 are zero regresie.
- index.html a rămas nemodificat.

## DECIZII BRAIN LA ÎNTREBĂRILE CLAUDE

### 1. Breadcrumb T3
Confirm breadcrumbul T3 ca element de orientare.

Este acceptat ca breadcrumbul să arate traseul T3, inclusiv pașii viitori inactivi.

Atenție:
- Pașii viitori pot apărea doar ca orientare, nu ca predare de conținut C10/C11/C12.
- Dacă tier_guard dă WARN pentru un termen viitor din breadcrumb, este acceptabil doar dacă termenul apare strict în orientare, nu în corpul pedagogic C09.

### 2. Slice 3
Confirm că SLICE 3 se sparge în sub-slice-uri.

Acum execuți doar:
- SLICE 3A = Editor-Studiu C09.

Nu execuți încă:
- Video C09.
- Editor-Video C09.
- FILM C09.
- imagini C09.
- index.html.

Motiv:
Video/FILM/imaginile au nevoie de tratament separat și de assets vizuale. Nu am generat încă imaginile C09.

### 3. Imagini
Nu genera imagini în acest mandat.
Nu modifica assets.
Nu integra base64.

## DECIZIE BRAIN DESPRE MODELUL DIN DATE
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

## DECIZII BRAIN PENTRU T3, DE ȚINUT CA GRANIȚE VIITOARE
Aceste decizii sunt pentru orientare și pentru handoff-uri. Nu transforma C09 în C10/C11/C12.

### C10 MĂSURI
C10 se poziționează ca:
"Cum construiești măsuri stabile pe un model de date."

C10 include:
- măsuri stabile.
- fact vs dimensiuni.
- schema star.
- filter context ca element central.
- validarea măsurii în contexte diferite.
- diferența măsură vs coloană.

Filter context intră obligatoriu în C10.

Formula C10:
"Măsura se calculează în fact. Dimensiunile îi dau contextul. Filter context decide ce parte din model este citită."

KPI în C10:
- KPI nu este central în C10 ca dashboard.
- KPI se menționează doar ca diferență față de măsură.
- Măsură = definiția stabilă a cifrei.
- KPI = măsură pusă față de target / prag / stare.
- KPI complet se dezvoltă în C11/C12/T4, nu în C10.

AHA C10:
"Un număr stă în tabel. O măsură trăiește în context."

### C11 COMPARAȚII / RANK
C11 se poziționează ca:
"Cum construiești comparații și rank-uri."

C11 include:
- comparații.
- rank.
- top / bottom.
- sortare.
- poziție.
- ierarhie.
- diferență.
- abatere.
- contribuție.
- comparație față de medie / target / perioadă.

Rank-ul este central în C11.

C11 are voie să spună:
- cine este sus.
- cine este jos.
- cine este peste medie.
- cine este sub target.
- cine contribuie mai mult.
- ce poziție are fiecare.

C11 NU explică de ce.
C11 NU dă cauze.
C11 NU dă recomandări.

AHA C11:
"Un număr nu e mare sau mic. Devine mare sau mic doar când primește un loc."

### C12 INTERPRETARE
C12 se poziționează ca:
"Cum construiești interpretări."

C12 include:
- semnal vs zgomot.
- contextul rezultatului.
- ipoteze.
- explicație business controlată.
- risc posibil.
- oportunitate posibilă.
- ce merită investigat.

C12 nu dă verdicte absolute.
C12 formulează ipoteze, nu cauze definitive.

C12 NU face dashboard.
C12 NU automatizează.
C12 NU dă decizie finală.
C12 NU dă recomandare operațională fermă.

AHA C12:
"C11 îți arată diferența. C12 îți spune dacă diferența merită atenție."

## FORMULA T3 LOCKED
Pentru orientare internă:

C09 construiește modelul.
C10 construiește cifra.
C11 construiește poziția.
C12 construiește sensul.

Sau:
Relații → Măsuri → Comparații / Rank → Interpretare.

## OBIECTIV SLICE 3A
Creează companionul de editare pentru C09:

`c09/HTML-Editor-Studiu-Excel-09-Relatii.html`

Acest fișier trebuie să fie companion pentru `c09/HTML-Studiu-Excel-09-Relatii.html`.

Scop:
- să permită revizuirea structurată a construcției C09.
- să explice ce poate fi editat și ce nu.
- să păstreze axa RELAȚII.
- să permită controlul textului, pașilor, scenei, prompturilor, payoff-ului și handoff-urilor.
- să fie compatibil cu stilul și standardul companionelor C05-C08.

## DOCUMENTE DE CITIT OBLIGATORIU
Citește:
- CLAUDE.md.
- STARE-CURENTA.md.
- BRAIN-TO-CLAUDE.md.
- CLAUDE-TO-BRAIN.md, raport BRAIN-013-REV1.
- c09/HTML-Studiu-Excel-09-Relatii.html.
- c09/Date_MASTER-C09.xlsx.
- c09/Creativ-Excel-09-Relatii.txt.
- companion Editor-Studiu din C05-C08, ca schelet tehnic și standard UX, nu ca narativă de copiat.
- _system/04-ARHITECTURA-LIVRABILE.md.
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md.
- _system/blueprints/BLUEPRINT-C09-RELATII.md.
- _system/generatoare/gate_v20.py.
- _system/generatoare/tier_guard_t3.py.
- _system/generatoare/audit_sync.py.

## PRINCIPIU SACRU
Editor-Studiu C09 nu este un nou Studiu și nu este un rezumat generic.

Este companion de control pentru Studiu C09.

Trebuie să păstreze:
- identitatea C09.
- cele 6 operații.
- scena 5 fenomene.
- granița C09/C10.
- granița C09/C11/C12/T4/T5.
- formula Join vs Union.
- modelul fact + dimensiuni.

## CONȚINUT MINIM CERUT ÎN EDITOR-STUDIU
Editor-Studiu C09 trebuie să includă cel puțin:

1. Meta construcție C09.
2. Identitate C09.
3. AHA C09.
4. Cele 6 operații C09.
5. SCENA 5 fenomene.
6. Zone editabile pentru titluri, pași, explicații, exemple și prompturi.
7. Zone blocate, care nu trebuie modificate fără decizie BRAIN.
8. Verificări anti-contaminare C10/C11/C12/T4/T5.
9. Verificări anti-cifre exacte statice.
10. Verificare Join vs Union.
11. Handoff C09 -> C10.
12. Notă de orientare T3, cu viitorul C10/C11/C12 doar ca hartă.

## ZONE LOCKED ÎN EDITOR
Marchează clar ca LOCKED:
- AHA C09: "Fără relații ai date. Cu relații ai răspunsuri."
- Formula Join vs Union: "Join leagă tabele diferite. Union adună tabele de același fel."
- C09 nu definește măsuri.
- C09 nu face rank.
- C09 nu interpretează cauze.
- C09 nu produce dashboard.
- C09 nu dă acțiuni.

## GRANIȚE STRICTE PENTRU ACEST MANDAT
Nu modifica `c09/HTML-Studiu-Excel-09-Relatii.html`, decât dacă descoperi un bug tehnic critic și îl explici explicit în raport.

Nu crea / modifica:
- Video C09.
- Editor-Video C09.
- FILM C09.
- assets / imagini C09.
- index.html.
- Date_MASTER-C09.xlsx.
- Creativ-Excel-09-Relatii.txt.
- C01-C08.
- C10-C12.
- generatoare.
- governance / Bible / doc 12 / 06-MAP.

## FIȘIERE PERMISE
Ai voie să creezi / modifici doar:
- `c09/HTML-Editor-Studiu-Excel-09-Relatii.html`.
- `CLAUDE-TO-BRAIN.md`.
- `STARE-CURENTA.md`, doar dacă fluxul standard cere actualizare.

## VALIDĂRI CERUTE
Rulează:

1. `gate_v20 09 c09 c01`.
2. `tier_guard_t3` pentru C09.
3. `audit_sync`.
4. verificare că `index.html` a rămas nemodificat.
5. verificare că nu ai creat Video / Editor-Video / FILM / assets.
6. verificare că Editor-Studiu nu introduce contaminări C10/C11/C12 în corpul C09.
7. verificare că nu apar cifre business exacte ca raport static.
8. verificare că nu ai atins fișiere interzise.

## CRITERII DE PASS
Mandatul trece doar dacă:

1. `c09/HTML-Editor-Studiu-Excel-09-Relatii.html` există.
2. Este companion real pentru C09, nu generic.
3. Păstrează identitatea RELAȚII.
4. Include cele 6 operații C09.
5. Include SCENA 5 fenomene.
6. Include controale anti-contaminare.
7. Marchează zonele LOCKED.
8. Nu modifică index.html.
9. Nu creează Video / Editor-Video / FILM / assets.
10. GATE trece sau raportează blocaj concret.
11. audit_sync nu produce regresii C01-C08.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet cu:

1. Status.
2. Rezumat executiv.
3. Fișiere citite.
4. Fișiere create / modificate.
5. Structura Editor-Studiu C09.
6. Cum ai păstrat axa RELAȚII.
7. Cum ai integrat cele 6 operații.
8. Cum ai integrat SCENA 5 fenomene.
9. Ce zone sunt editabile.
10. Ce zone sunt LOCKED.
11. Cum ai respectat granițele C09/C10/C11/C12/T4/T5.
12. Validări rulate.
13. PASS / WARNING / FAIL.
14. Ce rămâne pentru SLICE 3B.
15. Decizii cerute de la BRAIN.
16. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-014-REV1.
C09 RELAȚII, SLICE 3A.
Livrează doar Editor-Studiu C09.
Zero Video.
Zero Editor-Video.
Zero FILM.
Zero imagini.
Zero index.html.
Zero C10-C12 implementare.
