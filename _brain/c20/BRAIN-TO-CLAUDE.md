# BRAIN -> CLAUDE C20

## STATUS
APLICA_MICRO_FIX_BLUEPRINT_C20

## CONTEXT
Auditul blueprint C20 a dat verdictul BLUEPRINT_C20_VALIDAT_CU_MICRO_FIX.
BRAIN aproba aplicarea micro-fixurilor MF1, MF2 si MF3 in blueprint-ul conceptual.

## MANDAT
Aplica micro-fixurile in blueprint-ul C20 si emite freeze final daca nu apar probleme noi.
Nu redeschide SPEC.
Nu modifica SYSTEM.
Nu genera artefacte.

## MICRO-FIXURI APROBATE

### MF1 - STATUS logic corect
Inlocuieste definitia STATUS cu logica:
- NEPREDAT = harta incompleta sau ROL_DELEGAT nedefinit;
- PARTIAL = harta completa, dar cel putin o verificare V1-V4 este FAIL;
- DELEGAT = toate V1-V4 sunt OK + AUTOR_ACTIV=DA;
- AUTONOM = toate V1-V4 sunt OK + AUTOR_ACTIV=NU.

### MF2 - V1 pinned real
Fixeaza V1 ca verificare live pe referinte reale, nu declarativa.
V1 trebuie sa pice daca un input critic ramane AUTHOR_ONLY sau citit din zona autorului cand AUTOR_ACTIV=NU.
V1 trebuie sa treaca doar cand toate inputurile critice sunt mutate in surse accesibile rolului.

### MF3 - semnatura vizuala _DELEGARE
Marcheaza explicit comutatorul AUTOR_ACTIV ca semnatura vizuala a foii _DELEGARE si ca diferentiator fata de C19 _GUVERNARE.

## PASTREAZA
- 6 etape / 18 pasi;
- exemplul concret cu raportarea lunara a vanzarilor;
- drama FAIL -> reparare -> AUTONOM;
- granita C20 = PROPRIETATE;
- rol, nu persoana;
- proprietate, nu ownership;
- MOTTO candidat treapta T5.

## INTERDICTII
Nu genera HTML.
Nu genera Date_MASTER.
Nu genera FILM.
Nu genera build scripts.
Nu modifica fisiere SYSTEM.
Nu modifica artefacte de constructie.

## RAPORT CERUT
Scrie in _brain/c20/CLAUDE-TO-BRAIN.md status final:
BLUEPRINT_C20_FREEZE_FINAL
sau
BLUEPRINT_C20_RAMANE_CU_REZERVE.
Include clar ce ai modificat la MF1, MF2 si MF3.
