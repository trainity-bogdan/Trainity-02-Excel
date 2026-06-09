# BRAIN -> CLAUDE C14

## STATUS
MANDAT_ASSETS_C14

## CONTEXT
C14 COMPUNEREA. T4 RAPORTARE. CUVÂNT LOCKED COMPOZIȚIE. VERB LOCKED COMPUN.

C14 este aprobat conceptual și tehnic.

Status acceptat:

`C14_APPROVED_TEHNIC_CONCEPTUAL_ASSETS_PENDING`

Nu mai sunt necesare patch-uri conceptuale.

Singurul element deschis este assets:

- hero-poster
- 6 exec-stage

## DECIZIE BRAIN

Intrăm în etapa ASSETS C14.

Scopul este pregătirea și integrarea assets C14 fără modificarea conceptului, structurii, pașilor sau granițelor.

## IDENTITATE VIZUALĂ C14

Assets trebuie să susțină C14 ca:

- COMPUNEREA
- COMPOZIȚIE
- organizarea spațială a obiectelor vizuale
- întrebarea-ax: "Ce vede ochiul întâi?"
- mantra: "Compun privirea, nu pagina."

Direcție vizuală:

- pagină de raportare / foaie Excel / material decision-ready în construcție
- aceleași grafice, altă ordine
- ierarhie vizuală
- traseu al privirii
- focar vizual
- spațiu gol folosit intenționat
- fără estetică decorativă
- fără dashboard ca identitate

## MANDAT

Pregătește etapa assets C14 în două faze.

### Faza 1, dacă imaginile reale NU există încă

Nu modifica artefactele.

Pregătește raportul:

# CLAUDE -> BRAIN · C14 ASSETS BRIEF RAPORT

Raportul trebuie să includă:

1. lista exactă de assets necesare
2. numele standard recomandate pentru fișiere
3. promptul pentru hero-poster C14
4. cele 6 prompturi pentru exec-stage C14
5. criterii vizuale obligatorii
6. criterii de respingere
7. instrucțiuni pentru ARHITECT / generatorul extern
8. ce trebuie livrat înapoi ca fișiere

### Faza 2, doar dacă imaginile reale există deja în repo sau sunt furnizate explicit

Poți integra assets C14.

Integrarea trebuie să includă:

- curățare watermark, dacă este cazul, conform R-V49.1
- salvare în `c14/assets/` cu nume standard
- integrare în HTML-urile C14 conform convenției existente
- re-rulare B1
- re-rulare B2
- re-rulare B3
- verificare `V39.assets`

## LIMITE

Poți modifica doar:

- `c14/assets/**`, dacă imaginile reale există
- HTML-urile C14, doar pentru integrarea assets
- scripturile C14 de build, doar dacă integrarea assets o cere
- `_brain/c14/CLAUDE-TO-BRAIN.md`

Nu modifica:

- conceptul C14
- cele 11 step-title-uri
- Date_MASTER-C14.xlsx, dacă nu este strict necesar
- FILM, dacă nu este strict necesar
- `c01/**`
- `c13/**`
- alte `cNN/**`
- `_system/**`
- index / STARE / constructii

Nu integra global.
Nu marca LIVRAT 100% decât dacă assets sunt reale, integrate și validate.
Nu folosi placeholder-e ca assets finale.
Nu inventa existența imaginilor.

## RAPORT FINAL

Actualizează `_brain/c14/CLAUDE-TO-BRAIN.md` cu unul dintre statusurile:

- `CLAUDE_C14_ASSETS_BRIEF_READY`, dacă imaginile nu există și ai produs doar brief/prompturi
- `CLAUDE_C14_ASSETS_INTEGRATED_PASS`, dacă imaginile reale au fost integrate și B1/B2/B3 trec
- `CLAUDE_C14_ASSETS_BLOCKED`, dacă există blocaj
