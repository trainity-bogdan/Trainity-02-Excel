# BRAIN → CLAUDE · C11 COMPARAȚII / RANK

## STATUS
MANDAT_SYSTEM_ACTIV

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C11.

La comanda `sync`, citește:
- `_brain/c11/CHAT-CONTEXT.md`
- `_brain/c11/BRAIN-TO-CLAUDE.md`

Execută doar în:
- `c11/**`
- `_brain/c11/**`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C11
C11 este construcția COMPARAȚII / RANK.
SPEC C11 este înghețat.
Generarea C11 este blocată de precondiții sistem.
Este activ mandatul SYSTEM pentru deblocarea precondițiilor C11.

## MANDAT C11-04 · SYSTEM FIX PENTRU DEBLOCARE C11

### STATUS
MANDAT_SYSTEM_ACTIV

### OBIECTIV
Deblochează precondițiile sistem pentru C11, fără să generezi încă artefactele C11.

Acest mandat autorizează intervenții strict necesare în fișierele sistem indicate mai jos, pentru ca C11 să fie recunoscut corect ca SPEC înghețat în arhitectura actuală.

### CONTEXT
În raportul tău anterior ai blocat corect generarea C11 din cauza următoarelor probleme:
1. Registrul sistem păstrează identitatea legacy `DATA MODEL` pentru C11.
2. Registrul sistem marchează C11 ca `NEGENERAT`, deși SPEC C11 este înghețat în BRAIN.
3. Lipsește blocul `IDENTITATE_TEHNICA` pentru C11.
4. C10 nu este încă generat fizic, deci C11 nu trebuie generat înainte de C10.

### DECIZIE BRAIN
Nu generăm C11 înainte de C10.

C11 trebuie doar pregătit sistemic, astfel încât după livrarea C10 să poată fi generat corect.

### FIȘIERE SYSTEM AUTORIZATE
Ai voie să modifici strict următoarele fișiere:
- `_system/arhiva/SISTEM_TRAINITY-versiuni.md`
- `_system/referinte/IDENTITATE-TEHNICA.md`

Nu modifica alte fișiere sistem.
Nu modifica `CLAUDE.md`.
Nu modifica `README.md`.
Nu modifica `STARE-CURENTA.md`.
Nu modifica `index.html`.
Nu modifica `_system/generatoare/**`.
Nu modifica construcții existente.
Nu crea `c11/` încă.

### CERINȚE PENTRU `_system/arhiva/SISTEM_TRAINITY-versiuni.md`
Reconciliază C11 cu arhitectura actuală T3:
- C11 nu mai este `DATA MODEL`.
- C11 este `COMPARAȚII / RANK`.
- C11 are verb-semnătură `a compara`.
- C11 răspunde la întrebarea `Care?`.
- C11 vine după C10 MĂSURI și înainte de C12 INTERPRETARE.

Inserează sau actualizează SPEC C11 cu cele 9 elemente înghețate:
1. SLUG: `comparatii`
2. INTRIGA: trecerea de la listă plată la ierarhie clară
3. PROBLEMELE: lista din SPEC_FROZEN
4. MIZA: transformi măsurile corecte într-o ierarhie decizională
5. MANTRA: `Nu toate valorile sunt egale. Unele conduc rezultatul.`
6. WOW: puțini actori duc majoritatea rezultatului
7. MOTTO: `Nu citi lista. Citește ierarhia.`
8. FENOMENE: cele 6 fenomene confirmate
9. STEP-TITLES: cei 8 pași confirmați

Marchează C11 ca SPEC înghețat / `INGHETAT`, nu ca generat.

### CERINȚE PENTRU `_system/referinte/IDENTITATE-TEHNICA.md`
Adaugă sau actualizează blocul tehnic C11.

Identitate minimă obligatorie:
- cod: `C11`
- nume: `COMPARAȚII / RANK`
- slug: `comparatii`
- hero: `COMPARAȚII`
- motto: `Nu citi lista. Citește ierarhia.`
- input: `Date_MASTER-C10.xlsx`
- output: `Date_MASTER-C11.xlsx`
- localStorage prefix: `trainity_c11_`
- title studiu/video/editor adaptat pentru C11
- prompt-label specific C11, nu clonă din C10

Dacă formatul fișierului cere câmpuri suplimentare, completează-le coerent cu C11 și raportează exact ce ai adăugat.

### REGULĂ VOCABULAR ȘI ADRESARE C11
În orice text C11 introdus în sistem, respectă:
- adresare directă cu `tu` în textele de experiență
- fără `cursant`
- fără `cursantul`
- fără `participant`
- fără `participantul`
- fără `elev`
- fără `student`

### DELIMITĂRI HARD
C11 NU redefinește măsura. Măsura vine din C10.
C11 NU explică de ce apare ierarhia. Cauza rămâne pentru C12.
C11 NU construiește dashboard. Raportarea rămâne pentru T4.
C11 compară actori agregați, nu etichetează rânduri individuale.

### VALIDARE CERUTĂ
După modificările SYSTEM:
1. Rulează `pre_generation_check.py 11`, dacă este permis.
2. Confirmă că B1 nu mai blochează SPEC C11.
3. NU genera C11, chiar dacă pre-check trece.
4. Actualizează `_brain/c11/CLAUDE-TO-BRAIN.md` cu raport complet.

### LIVRARE CERUTĂ
În `_brain/c11/CLAUDE-TO-BRAIN.md`, raportează:
- fișiere sistem modificate
- ce ai modificat în registrul sistem
- ce ai modificat în IDENTITATE-TEHNICA
- rezultat pre_generation_check.py 11
- confirmarea că NU ai generat C11
- eventuale blocaje rămase

## SPEC C11 ÎNGHEȚAT, REFERINȚĂ SCURTĂ
Slug: `comparatii`
Motto: `Nu citi lista. Citește ierarhia.`
Mantra: `Nu toate valorile sunt egale. Unele conduc rezultatul.`
Fenomene: clasament, diferență reală vs zgomot, contribuție/pondere, concentrare Pareto/ABC, comparabilitate, reper relativ.
Step titles:
1. Confirmă măsura pe care compari
2. Asigură comparabilitatea
3. Așază actorii în clasament
4. Citește diferențele reale
5. Calculează contribuția în total
6. Identifică concentrarea
7. Raportează poziția la reper
8. Confirmă ierarhia decizională
