# BRAIN -> CLAUDE C20

## STATUS
GENERARE_C20_CONTINUA

## CONTEXT
Mandatul MANDAT_GENERARE_C20 este activ.
Blueprint C20 este BLUEPRINT_C20_FREEZE_FINAL.

## MANDAT
Continua cu generarea artefactelor standard C20 pe baza blueprint-ului inghetat.

## ARTEFACTE
Lucreaza pe setul standard C20:
- HTML-Studiu;
- HTML-Editor-Studiu;
- HTML-Video;
- HTML-Editor-Video;
- Date_MASTER, daca este posibil;
- FILM, daca protocolul il cere;
- fisiere auxiliare C20 necesare.

## REPERE
Pastreaza C20 ca DELEGAREA / AUTONOMIE / DELEG / PROPRIETATE.
Pastreaza _DELEGARE ca test viu, nu tabel pasiv.
Pastreaza AUTOR_ACTIV, ROL_DELEGAT, V1-V4 si STATUS calculat.
Pastreaza exemplul raportarii lunare a vanzarilor.
Pastreaza diferenta fata de C19 _GUVERNARE.

## STATUS LOGIC
NEPREDAT = harta incompleta sau ROL_DELEGAT nedefinit.
PARTIAL = harta completa, dar cel putin o verificare V1-V4 este FAIL.
DELEGAT = toate V1-V4 sunt OK + AUTOR_ACTIV=DA.
AUTONOM = toate V1-V4 sunt OK + AUTOR_ACTIV=NU.

## LIMITE
Nu modifica fisiere SYSTEM.
Nu redeschide SPEC.
Nu schimba blueprint-ul inghetat.

## RAPORT
Scrie in _brain/c20/CLAUDE-TO-BRAIN.md statusul:
GENERARE_C20_COMPLETA
sau
GENERARE_C20_PARTIALA
sau
GENERARE_C20_BLOCATA.
