# BRAIN → CLAUDE · C13 VIZUALIZAREA

## STATUS
BRAIN_C13_GENERATION_BLOCK_CONFIRMED_SYSTEM_REGISTRATION_REQUIRED

## MANDAT-ID
C13-GENERATION-BLOCK-SYSTEM-REGISTRATION-008

## RAPORT CLAUDE ANALIZAT
BRAIN a analizat raportul:

`CLAUDE_C13_GENERATION_BLOCKED`

din:

`_brain/c13/CLAUDE-TO-BRAIN.md`

## VERDICT BRAIN
PASS PE BLOCAJ.

Blocajul este legitim și nu trebuie forțat.

Claude C13 a procedat corect:
- a rulat gate-ul de pre-generare;
- a identificat lipsa înregistrării SPEC C13 în registrul sistemic;
- a identificat lipsa identității tehnice C13;
- nu a modificat fișiere `_system/**` din chatul C13;
- nu a generat artefacte înainte de gate.

## STARE C13

### Conceptual
`C13_CONCEPTUAL_READY`

### SPEC
`SPEC_C13_FROZEN`

### Blueprint
`BLUEPRINT_C13_APPROVED`

### System dashboard tension
`SYSTEM_C13_DASHBOARD_TENSION_RESOLVED`

### Generation
`BLOCKED_PENDING_SYSTEM_REGISTRATION`

## BLOCAJE CONFIRMATE

### Blocaj 1
Lipsește înregistrarea SPEC C13 în:

`_system/arhiva/SISTEM_TRAINITY-versiuni.md`

Gate-ul cere secțiune de tip:

`## SPEC C13 — VIZUALIZAREA   [Status: INGHETAT]`

### Blocaj 2
Lipsește identitatea tehnică C13 în:

`_system/referinte/IDENTITATE-TEHNICA.md`

Gate-ul cere secțiune de tip:

`## IDENTITATE_TEHNICA C13 — VIZUALIZAREA`

## DECIZIE BRAIN
C13 NU se generează până când înregistrarea SYSTEM nu este făcută și `pre_generation_check.py 13` nu trece.

## FINAL-LABELS C13 APROBATE PENTRU REGISTRUL SYSTEM
Pentru completarea registrului, BRAIN aprobă următoarele 8 FINAL-LABELS C13:

1. Cifra corectă nu garantează grafic corect.
2. Forma este o decizie.
3. Axa poate exagera adevărul.
4. Tipul de grafic urmează natura rezultatului.
5. Scala trebuie să fie declarată.
6. Codarea vizuală spune un singur lucru.
7. Eticheta, unitatea și contextul elimină ghicitul.
8. Vizualul corect produce aceeași concluzie ca cifra brută.

Acestea sunt aprobate doar pentru înregistrarea SYSTEM a SPEC C13 și trebuie păstrate în logica:

C13 = obiect vizual onest, nu dashboard.

## TASK SYSTEM DE EXECUTAT SEPARAT DE CLAUDE

```text
ACEST TASK ESTE SYSTEM, EXECUTAT DE CLAUDE.

Repo:
trainity-bogdan/Trainity-02-Excel

Context:
C13 VIZUALIZAREA are SPEC înghețat, blueprint aprobat și tensiunea dashboard rezolvată. Generarea C13 este blocată de gate-ul B1 pentru că lipsesc înregistrările SYSTEM.

Obiectiv:
Deblochează pre-generation gate pentru C13 prin înregistrarea SPEC C13 și a identității tehnice C13 în fișierele sistemice cerute de validator.

Lucrează pe main:

git checkout main
git pull origin main

Citește înainte:
- _brain/c13/BRAIN-TO-CLAUDE.md
- _brain/c13/CLAUDE-TO-BRAIN.md
- _system/arhiva/SISTEM_TRAINITY-versiuni.md
- _system/referinte/IDENTITATE-TEHNICA.md

Modifică doar:
- _system/arhiva/SISTEM_TRAINITY-versiuni.md
- _system/referinte/IDENTITATE-TEHNICA.md

Nu modifica:
- c13/**
- c01/** până la c20/**
- CLAUDE.md
- README.md
- STARE-CURENTA.md
- index.html
- gate_v20.py
- audit_sync.py
- COMENZI.yaml
- orice alt fișier sistemic

PASUL A:
În _system/arhiva/SISTEM_TRAINITY-versiuni.md adaugă secțiunea:

## SPEC C13 — VIZUALIZAREA   [Status: INGHETAT]

Include cele 9 elemente cerute de gate:

1. INTRIGA:
"Cifra e corectă. Graficul minte."

2. PROBLEMELE:
- aceeași cifră produce concluzii diferite prin forme diferite
- graficul pare obiectiv, dar forma e aleasă de autor
- ochiul crede forma înainte să verifice cifra
- AI generează graficul, dar nu garantează onestitatea lui
- decidentul crede că vede datele, dar vede o formă vizuală prost aleasă

3. MIZA:
"O decizie este luată cu încredere pe o imagine falsă construită peste date corecte."

4. MANTRA / AHA:
"Nu desenez frumos. Desenez adevărat."
"Forma greșită minte cu cifra corectă."

5. MOTTO:
"Forma nu se nimerește. Se alege."

6. STEP-TITLES:
Cele 18 step-titles locked C13, în 6 etape x 3 pași:

ETAPA 1 REALITATE
1. Răspunsul corect, dar invizibil
2. Nimeni nu decide privind un model
3. Aceeași cifră, încă fără formă

ETAPA 2 INVESTIGAȚIE
4. O cifră, mai multe forme posibile
5. Promptul 1: ce formă cere rezultatul
6. Aceeași cifră, două grafice, două concluzii

ETAPA 3 TRANSFORMARE
7. Tipul de grafic urmează natura rezultatului
8. Promptul 2: generezi vizualul, corectezi axa și scala
9. Scoți codarea care sugerează fals

ETAPA 4 VERIFICARE
10. Vizualul față de cifra brută: aceeași concluzie?
11. Testul celui de-al doilea ochi
12. Marchezi forma care spune mai mult decât cifra

ETAPA 5 STABILIZARE
13. Cele șase reguli de onestitate a formei
14. Eticheta, unitatea, contextul: nimic de ghicit
15. Un obiect vizual onest, repetabil

ETAPA 6 CONFIRMARE
16. Forma onestă repară percepția
17. Devii garantul a ceea ce vede altcineva
18. Predai către C14: obiectul, gata de așezat în pagină

7. PROMPTURI:
- Promptul 1, E2 INVESTIGAȚIE: ce formă cere rezultatul
- Promptul 2, E3 TRANSFORMARE: generezi vizualul, corectezi axa și scala

8. FINAL-LABELS:
- Cifra corectă nu garantează grafic corect.
- Forma este o decizie.
- Axa poate exagera adevărul.
- Tipul de grafic urmează natura rezultatului.
- Scala trebuie să fie declarată.
- Codarea vizuală spune un singur lucru.
- Eticheta, unitatea și contextul elimină ghicitul.
- Vizualul corect produce aceeași concluzie ca cifra brută.

9. FENOMENE:
- Axa care exagerează → axa pleacă de la zero, sau abaterea e declarată explicit.
- Tipul de grafic nepotrivit → tipul urmează natura rezultatului.
- Scala care inventează relații → o singură scală liniară, declarată.
- Codarea care sugerează fals → o singură dimensiune codată coerent.
- Agregarea care ascunde variația → arăți distribuția / variația, nu doar media.
- Eticheta / unitatea / contextul lipsă → fiecare vizual poartă unitate, etichetă și context.

PASUL B:
În _system/referinte/IDENTITATE-TEHNICA.md adaugă secțiunea:

## IDENTITATE_TEHNICA C13 — VIZUALIZAREA

Construiește secțiunea pe tiparul C12 existent, adaptată la C13:
- cod: C13
- slug: Vizualizare
- output_filename: Date_MASTER-C13-Vizualizare.xlsx
- title_studiu: C13 · Vizualizare · Trainity
- topbar_text: Sistemul 02 - Excel · C13 · Vizualizare
- mobile_topbar: C13 · Vizualizare
- nav_brand_label: PACK 02 EXCEL · C13
- footer_text: TRAINITY · C13 VIZUALIZARE · VIZUAL
- next_cod: C14
- localStorage_studiu și celelalte câmpuri tehnice conform tiparului C12, adaptate la c13 / Vizualizare.

Nu inventa o schemă nouă. Copiază schema C12 și adapteaz-o.

PASUL C:
Rulează:

python3 _system/generatoare/pre_generation_check.py 13

Dacă trece, commit:

git add _system/arhiva/SISTEM_TRAINITY-versiuni.md _system/referinte/IDENTITATE-TEHNICA.md
git commit -m "docs(system): register C13 spec and technical identity"
git push origin main

Raport final obligatoriu:
- STATUS
- fișiere citite
- fișiere modificate
- secțiuni adăugate
- rezultatul pre_generation_check.py 13
- commit SHA

STATUS așteptat dacă trece:
SYSTEM_C13_PRE_GENERATION_READY

Dacă nu trece:
SYSTEM_C13_PRE_GENERATION_STILL_BLOCKED
și explică exact ce mai lipsește.
```

## MANDAT CĂTRE CLAUDE C13
Nu încerca din nou generarea C13 până când taskul SYSTEM de mai sus nu este executat și raportat cu status:

`SYSTEM_C13_PRE_GENERATION_READY`

La următorul sync C13, dacă acest status nu există, răspunde cu:

`WAITING_FOR_SYSTEM_C13_PRE_GENERATION_READY`

## FIȘIERE PERMISE C13
Până la rezolvarea SYSTEM, Claude C13 poate scrie doar în:
- `_brain/c13/CLAUDE-TO-BRAIN.md`

## STATUS AȘTEPTAT C13
`WAITING_FOR_SYSTEM_C13_PRE_GENERATION_READY`

## CERERE DIRECTĂ
Așteaptă înregistrarea SYSTEM. Nu genera C13 până când gate-ul B1 nu este deblocat.