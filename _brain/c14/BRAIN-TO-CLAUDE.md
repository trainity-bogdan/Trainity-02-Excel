# BRAIN -> CLAUDE C14

## STATUS
MANDAT_PATCH_TITLURI_C14

## CONTEXT
C14 COMPUNEREA. T4 RAPORTARE. CUVÂNT LOCKED COMPOZIȚIE. VERB LOCKED COMPUN.

C14 este generat tehnic, cu B1 PASS, B2 GATE PASS și B3 zero drift real.

Auditul conceptual a identificat o singură abatere minoră: step-title-urile afișate nu sunt 1:1 cu cele 11 sloturi aprobate.

Status BRAIN curent:

`C14_GENERAT_GATE_PASS_ASSETS_PENDING_PATCH_TITLURI`

Assets rămân pending.

Nu se face integrare globală încă.

Nu se marchează C14 LIVRAT 100% încă.

## DECIZIE BRAIN

Aplică PATCH CONCEPTUAL MINOR, obligatoriu, strict pe titluri și propagarea lor.

Nu regenera conceptual C14.
Nu modifica Date_MASTER dacă nu este necesar.
Nu modifica assets.
Nu integra global.

## PROBLEMA DE REPARAT

Step-title-urile afișate în HTML-Studiu și HTML-Video nu sunt 1:1 cu cele 11 sloturi aprobate.

Probleme exacte:

- slotul 6, "Retrogradarea elementelor secundare", nu apare ca titlu propriu
- conceptul există în corp, dar nu ca titlu
- un titlu "Promptul 1" ocupă loc de step-title
- prompturile trebuie să stea în corpul pașilor relevanți, nu în titlu

## STEP-TITLES FINALE OBLIGATORII

După patch, cele 11 step-title-uri afișate trebuie să fie exact:

1. Pagina fără "întâi"
2. Primul punct de contact al ochiului
3. Poziția ca semnal de importanță
4. Focarul vizual
5. Traseul de citire
6. Retrogradarea elementelor secundare
7. Ierarhia vizuală pentru decizie
8. Gruparea elementelor legate
9. Spațiul gol ca instrument de ierarhie
10. Compunerea guvernată de răspunsul venit din T3
11. Testul celui de-al doilea ochi

## PATCH OBLIGATORIU

1. Adaugă "Retrogradarea elementelor secundare" ca titlu propriu.
2. Elimină "Promptul 1" ca titlu de pas.
3. Mută prompturile Copilot în corpul pașilor relevanți, ca box / secțiune internă, nu ca step-title.
4. Păstrează cele 11 concepte intacte.
5. Păstrează toate granițele C13 / C15 / C16.

## PROPAGARE

Aplică patch-ul, dacă este afectat, în:

- `c14/HTML-Studiu-Excel-14-Compunere.html`
- `c14/HTML-Editor-Studiu-Excel-14-Compunere.html`
- `c14/HTML-Video-Excel-14-Compunere.html`
- `c14/HTML-Editor-Video-Excel-14-Compunere.html`
- `c14/FILM-Excel-14-Compunere.docx`, doar dacă titlurile sunt afectate acolo

## VALIDARE

După patch:

- rulează B1
- rulează B2
- rulează B3
- verifică explicit că cele 11 step-title-uri afișate sunt 1:1 cu lista aprobată

## INTERDICȚII

Nu modifica:

- `c01/**`
- `c13/**`
- alte `cNN/**`
- `_system/**`
- index / STARE / constructii
- assets

Nu integra global.
Nu marca C14 LIVRAT 100%.
Nu schimba SPEC-ul conceptual.
Nu schimba identitatea C14.
Nu schimba granițele C13 / C15 / C16.

## RAPORT

La final, actualizează `_brain/c14/CLAUDE-TO-BRAIN.md` cu:

# CLAUDE -> BRAIN · C14 PATCH TITLURI RAPORT

Raportul trebuie să includă:

- ce ai modificat
- unde ai propagat patch-ul
- lista finală a celor 11 step-title-uri detectate în artefacte
- status B1
- status B2
- status B3
- riscuri rămase
- dacă C14 poate intra în reaprobarea finală BRAIN
