# BRAIN -> CLAUDE C19

## STATUS
STOP_C19

## DECIZIE BRAIN

Nu mai executa alte slice-uri.
Nu mai genera artefacte.
Nu mai modifica C19.

Status curent acceptat:

- Date_MASTER = generat
- HTML-Studiu = generat
- HTML-Editor-Studiu = generat
- HTML-Video = generat
- HTML-Editor-Video = generat
- FILM = generat
- assets = generate DRAFT

C19 este acum:

`C19_DRAFT_COMPLET`

## OBSERVATII

Ultimul sync confirma:

- cele 7 artefacte exista
- audit_sync C19 = ZERO DRIFT
- gate_v20 este blocat de SYSTEM
- imaginile sunt DRAFT placeholder

Aceste blocaje NU mai apartin chatului C19.

## INTERDICTIE

Nu mai modifica:

- `c19/**`
- `Date_MASTER-C19.xlsx`
- HTML-Studiu
- HTML-Editor-Studiu
- HTML-Video
- HTML-Editor-Video
- FILM
- assets

pana la unul dintre urmatoarele mandate:

- `MANDAT_GATE_RETEST`
- `MANDAT_IMAGINI_FINALE`

## ACTIUNI PERMISE DOAR LA MANDAT EXPLICIT

### MANDAT_GATE_RETEST

dupa ce SYSTEM deblocheaza gate_v20 pentru C18/C19:

- ruleaza `gate_v20.py 19`
- ruleaza `audit_sync.py`
- raporteaza PASS / FAIL / NU_RULAT

### MANDAT_IMAGINI_FINALE

dupa ce ARHITECT livreaza cele 7 imagini finale GUVERNARE:

- inlocuieste placeholder-ele DRAFT
- verifica hash != c01
- regenereaza assets daca este necesar
- reruleaza validarile finale

## STATUS FINAL BRAIN

`C19_DRAFT_COMPLET`

Asteapta:

1. SYSTEM -> deblocare gate_v20
2. ARHITECT -> imagini finale GUVERNARE

Nu mai executa alte modificari pana la unul dintre aceste doua evenimente.

## RAPORT

Nu este nevoie de raport nou daca doar confirmi asteptarea. Urmatorul raport va fi doar dupa `MANDAT_GATE_RETEST` sau `MANDAT_IMAGINI_FINALE`.
