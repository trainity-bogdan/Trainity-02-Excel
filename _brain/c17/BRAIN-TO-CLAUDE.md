# BRAIN -> CLAUDE C17

## STATUS
MANDAT_SYSTEM_FREEZE_BLUEPRINT_C17

## CONTEXT
C17 Blueprint a fost revizuit si confirmat de BRAIN.
Status curent verificat in _brain/c17/CLAUDE-TO-BRAIN.md:
C17_BLUEPRINT_CONFIRMED.

C17:
- SISTEMATIZAREA
- CUVANT LOCKED = SISTEM
- VERB LOCKED = SISTEMATIZEZ
- T5 = AUTONOMIE
- iese din OCAZIE
- axa: RELUABILITATEA / forma reluabila
- slug final: Sistematizare
- artefact obligatoriu: _SISTEM
- _SISTEM = structura/harta functionala nativ-Excel, legata de workbook, nu SOP, nu documentatie
- garda OGLINDA: FORMULATEXT, ROWS, COUNTA si referintele live sunt oglinzi de stare, nu reguli, nu validari, nu control C19

Blueprint confirmat:
- 6 etape
- 18 pasi, 3 pasi per etapa
- foaie _SISTEM cu blocuri A-F
- named ranges SRC_, INPUT_, PARAM_, OBJ_
- hyperlink-uri interne
- START AICI
- punct de reluare
- test anti-SOP
- test substitut
- granita C17->C18 prin pasi etichetati candidat C18, neautomatizati

Cele 6 etape confirmate:
1. Munca pe care o stii doar tu
2. Inventarul componentelor reale
3. O singura sursa pentru fiecare intrare
4. Ordinea de reluare, legata de obiecte
5. Cunoasterea scoasa din cap
6. Testul substitutului

## MANDAT
CERERE SYSTEM · FREEZE BLUEPRINT C17

Ai voie sa modifici doar fisiere SYSTEM permise.

Nu modifica:
- c17/**
- HTML-uri
- Date_MASTER
- build scripts
- FILM
- C18/C19/C20
- nomenclatura LOCKED

Obiectiv:
Consemneaza in sistem inghetarea Blueprint C17 si marcheaza C17 pregatit pentru generare controlata.

Actualizeaza, dupa caz:
- STARE-CURENTA.md
- _system/14-ARHITECTURA-CONCEPTUALA-T5.md
- _system/00-INDEX.md, doar daca indexul trebuie sa reflecte noua stare

Trebuie consemnate:
- status: C17_BLUEPRINT_FROZEN_READY_FOR_GENERATION
- slug final: Sistematizare
- nume fisiere propuse
- 6 etape confirmate
- artefact _SISTEM
- garda OGLINDA
- test anti-SOP
- test substitut
- granite C18/C19/C20
- faptul ca template-ul T5 "Pleci, si munca [...]" ramane CANDIDAT, nu LOCKED

Ruleaza:
- audit_sync
- verificare nomenclatura LOCKED neatinsa
- verificare zero em-dash
- verificare ca nu ai atins c17/**
- verificare ca nu ai generat artefacte

## OUTPUT CERUT
SYSTEM REPORT · C17 BLUEPRINT FREEZE

Include:
- fisiere modificate
- commit
- verificari rulate
- status final

Raspunde la final:
C17_BLUEPRINT_FROZEN_READY_FOR_GENERATION
sau
C17_BLUEPRINT_FREEZE_FAILED
