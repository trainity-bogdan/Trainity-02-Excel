# BRAIN -> CLAUDE C17

## STATUS
MANDAT_GENERARE_CONTROLATA_C17

## CONTEXT
C17 Blueprint este inghetat in sistem si pregatit pentru generare controlata.
Status curent verificat in _brain/c17/CLAUDE-TO-BRAIN.md:
C17_BLUEPRINT_FROZEN_READY_FOR_GENERATION.

C17:
- SISTEMATIZAREA
- CUVANT LOCKED = SISTEM
- VERB LOCKED = SISTEMATIZEZ
- T5 = AUTONOMIE
- iese din OCAZIE
- slug final: Sistematizare
- artefact obligatoriu: _SISTEM
- garda OGLINDA: FORMULATEXT, ROWS, COUNTA si referintele live sunt oglinzi de stare, nu reguli, nu validari, nu control C19

Blueprint confirmat si inghetat:
- 6 etape
- 18 pasi, 3 pasi per etapa
- foaie _SISTEM cu blocuri A-F
- named ranges SRC_, INPUT_, PARAM_, OBJ_
- hyperlink-uri interne
- START AICI
- punct de reluare
- test anti-SOP
- test substitut
- granite C18/C19/C20

Fisiere tinta C17:
- c17/HTML-Studiu-Excel-17-Sistematizare.html
- c17/HTML-Editor-Studiu-Excel-17-Sistematizare.html
- c17/HTML-Video-Excel-17-Sistematizare.html
- c17/HTML-Editor-Video-Excel-17-Sistematizare.html
- c17/Date_MASTER-C17.xlsx
- c17/FILM-Excel-17-Sistematizare.docx

## MANDAT
Genereaza controlat artefactele C17, respectand Blueprint-ul inghetat.

Ai voie sa lucrezi doar in:
- c17/**

Nu modifica:
- _system/**
- STARE-CURENTA.md
- CLAUDE.md
- README.md
- index.html
- gate_v20.py
- audit_sync.py
- COMENZI.yaml
- c18/**
- c19/**
- c20/**
- nomenclatura LOCKED

Cerinte obligatorii:
1. Creeaza folderul c17 daca nu exista.
2. Genereaza fisierele tinta C17.
3. Respecta slug-ul final: Sistematizare.
4. Respecta cele 6 etape confirmate:
   - Munca pe care o stii doar tu
   - Inventarul componentelor reale
   - O singura sursa pentru fiecare intrare
   - Ordinea de reluare, legata de obiecte
   - Cunoasterea scoasa din cap
   - Testul substitutului
5. Integreaza artefactul _SISTEM ca obiect central.
6. Pastreaza garda OGLINDA:
   - oglindeste
   - leaga
   - navigheaza
   - nu executa
   - nu judeca
   - nu deleaga
7. Nu transforma C17 in SOP.
8. Nu introduce automatizare C18.
9. Nu introduce reguli, validari, praguri, alerte sau control C19.
10. Nu introduce ownership, responsabil, escaladare sau delegare C20.
11. Nu afisa cifre din Excel in prezentare sau pagina, cifrele trebuie citite si validate live in Excel.
12. Pastreaza tonul Trainity: clar, simplu, rapid, usor, nivel 2030, AI/Copilot ca accelerator discret, fara hype.
13. Respecta regula zero em-dash.

Dupa generare:
- ruleaza audit_sync daca este aplicabil;
- verifica nomenclatura LOCKED neatinsa;
- verifica zero em-dash;
- verifica prezenta tuturor fisierelor tinta;
- verifica granitele C18/C19/C20;
- verifica testul anti-SOP;
- verifica filmabilitatea 8-12 minute.

## OUTPUT CERUT
CLAUDE -> BRAIN

Include:
- fisiere create/modificate;
- commit;
- verificari rulate;
- riscuri ramase;
- status final.

Raspunde la final:
C17_GENERATED_READY_FOR_AUDIT
sau
C17_GENERATION_FAILED
