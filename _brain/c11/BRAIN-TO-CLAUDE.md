# BRAIN → CLAUDE · C11 COMPARAȚII / RANK

## STATUS
MANDAT_SYSTEM_REGULA_REPO_ACTIV

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C11.

La comanda `sync`, citește:
- `_brain/c11/CHAT-CONTEXT.md`
- `_brain/c11/BRAIN-TO-CLAUDE.md`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C11
C11 a fost raportată ca livrabilă, dar verificarea externă BRAIN a arătat că `c11/Date_MASTER-C11.xlsx` nu există fizic în repo.
Raportul Claude nu mai este acceptat ca dovadă suficientă pentru închiderea unei construcții.
Repo-ul este sursa de adevăr.

## MANDAT C11-07 · SYSTEM RULE · VERIFICARE FIZICĂ REPO OBLIGATORIE

### STATUS
MANDAT_SYSTEM_REGULA_REPO_ACTIV

### OBIECTIV
Introdu o regulă permanentă în specificațiile sistemului: nicio construcție nu poate fi declarată PASS / CLEAN / ZERO DRIFT / LIVRABIL / ÎNCHISĂ doar pe baza raportului Claude.

Înainte de închiderea unei construcții, trebuie verificată existența fizică în repo a tuturor artefactelor obligatorii.

### MOTIV
C11 a fost raportată ca generată complet, inclusiv cu `c11/Date_MASTER-C11.xlsx`, dar verificarea externă în GitHub a găsit doar mențiuni text, nu fișierul fizic.
Această situație a blocat C12, care are nevoie de `Date_MASTER-C11.xlsx` ca input.

### FIȘIERE SYSTEM AUTORIZATE
Ai voie să modifici strict fișierele sistem unde sunt definite regulile operaționale active, preferabil:
- `_system/01-REGULI-ACTIVE.md`
- `_system/03-COMENZI-OPERATIONALE.md`, dacă este necesar pentru workflow
- `_system/INDEX-CAUTARE.md`, dacă este necesar pentru indexarea regulii

Nu modifica:
- artefacte C11
- alte construcții
- `index.html`
- fișiere HTML / xlsx / docx / assets

### REGULĂ NOUĂ DE INTRODUS
Adaugă o regulă permanentă, cu număr nou conform convenției existente, cu sensul următor:

`VERIFICARE FIZICĂ REPO OBLIGATORIE`

Text obligatoriu de inclus conceptual:

Un artefact nu poate fi declarat `GENERAT`, `PASS`, `CLEAN`, `ZERO DRIFT`, `LIVRABIL` sau `ÎNCHIS` doar pe baza raportului Claude.

Înainte de validarea finală a oricărei construcții, trebuie verificată existența fizică în repo a tuturor artefactelor obligatorii:
- `HTML-Studiu`
- `HTML-Editor-Studiu`
- `HTML-Video`
- `HTML-Editor-Video`
- `Date_MASTER-CNN.xlsx`
- `FILM-Excel-NN-{slug}.docx`
- `assets/`

Pentru construcțiile cu dependențe, dacă `C(N)` produce un fișier consumat de `C(N+1)`, atunci `C(N)` nu poate fi închisă până când acel fișier nu există fizic în repo.

Raportul Claude nu constituie dovadă suficientă.
Repo-ul este sursa de adevăr.

### REGULĂ DE STATUS
Dacă raportul declară un artefact creat, dar fișierul nu există fizic în repo, statusul devine:

`LIVRABIL INVALIDAT · ARTEFACT LIPSĂ`

și construcția trebuie redeschisă punctual pentru repararea artefactului lipsă.

### APLICARE IMEDIATĂ C11
După introducerea regulii, C11 trebuie considerată redeschisă punctual până când:
- `c11/Date_MASTER-C11.xlsx` există fizic în repo
- existența lui este verificată explicit
- C12 poate consuma fișierul

### LIVRARE CERUTĂ
Actualizează `_brain/c11/CLAUDE-TO-BRAIN.md` cu:
- fișiere sistem modificate
- numărul / numele regulii introduse
- confirmarea că regula repo-check este salvată permanent
- confirmarea că C11 rămâne redeschisă punctual pentru artefact lipsă

Nu repara încă `Date_MASTER-C11.xlsx` în acest mandat. Acest mandat este doar pentru salvarea regulii în specificațiile sistemului.
