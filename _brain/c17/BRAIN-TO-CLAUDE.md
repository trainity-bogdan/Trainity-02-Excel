# BRAIN -> CLAUDE C17

## STATUS
MANDAT_SYSTEM_IDENTITATE_TEHNICA_C17

## CONTEXT
C17 a fost generat complet si este pregatit pentru audit, dar gate_v20 B2 este blocat de lipsa identitatii tehnice C17 in fisier SYSTEM.
Status curent verificat in _brain/c17/CLAUDE-TO-BRAIN.md:
C17_GENERATED_READY_FOR_AUDIT.

Raport Claude:
- 6/6 artefacte C17 generate.
- Date_MASTER-C17.xlsx generat si verificat.
- _SISTEM generat si verificat.
- 4 HTML generate.
- FILM-Excel-17-Sistematizare.docx generat.
- audit_sync B3 trece detectoarele de continut.
- gate_v20 B2 este blocat deoarece lipseste identitatea tehnica C17 in _system/referinte/IDENTITATE-TEHNICA.md.

## MANDAT
CERERE SYSTEM · ADAUGA IDENTITATE TEHNICA C17

Ai voie sa modifici doar fisiere SYSTEM permise.

Nu modifica:
- c17/**
- c18/**
- c19/**
- c20/**
- HTML-uri
- Date_MASTER
- FILM
- build scripts
- nomenclatura LOCKED

Obiectiv:
Adauga blocul de identitate tehnica C17 in:
_system/referinte/IDENTITATE-TEHNICA.md

Date identitate C17:
- constructie: C17
- identitate: SISTEMATIZAREA
- slug: Sistematizare
- cuvant LOCKED: SISTEM
- verb LOCKED: SISTEMATIZEZ
- treapta: T5
- treapta nume: AUTONOMIE
- rol T5: scoate autorul din OCAZIE
- artefact central: _SISTEM

Dupa modificare ruleaza:
- gate_v20 17 c17 c01
- audit_sync daca este aplicabil
- verificare nomenclatura LOCKED neatinsa
- verificare zero em-dash
- verificare ca nu ai modificat c17/**

## OUTPUT CERUT
SYSTEM REPORT · IDENTITATE TEHNICA C17

Include:
- fisiere modificate
- commit
- verificari rulate
- status gate_v20
- status final

Raspunde la final:
C17_READY_FOR_FINAL_AUDIT
sau
C17_SYSTEM_IDENTITY_FAILED
