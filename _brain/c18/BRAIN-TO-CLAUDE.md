# BRAIN -> CLAUDE C18

## STATUS
C18_REPARATIE_CONTROL_FINAL_CERUTA

## CONTEXT
C18 AUTOMATIZAREA. T5 AUTONOMIE. CUVANT MOTOR. VERB AUTOMATIZEZ.

Claude a reparat P2 si a raportat o datorie noua in Date_MASTER-C18: formule sparte in foaia CONTROL_FINAL.

C18 ramane RELEASE = NU.

## P0 RAMAN DESCHISE
Nu repara P0 in acest mandat:
1. imaginile exec-stage sunt clone C01 si asteapta imagini ARHITECT;
2. hero base64 este clona C01 si asteapta imagine hero ARHITECT;
3. B2 gate este neverificabil si necesita decizie SYSTEM.

## OBIECTIV
Repara strict datoria noua din CONTROL_FINAL, fara sa atingi P0 si fara sa declari release.

## PROBLEMA DE REPARAT
In Date_MASTER-C18, foaia CONTROL_FINAL contine formule sparte care refera foaia `Date!`, desi foaia reala este `Vanzari`.

Formule raportate ca sparte:
- B5 `=COUNTA(Date!A2:A2001)`
- B7 `=ROUND(SUM(Date!...))`
- B9 `=ROUND(SUM(Date!...))`
- B11 `=SUMPRODUCT(...Date!...)`

## MANDAT
Alege solutia cea mai sigura:
1. fie corectezi referintele `Date!` -> `Vanzari!`, daca formulele raman coerente functional;
2. fie elimini / neutralizezi CONTROL_FINAL daca foaia este doar meta si nu este necesara C18.

Decizia trebuie justificata in raport.

## VERIFICARI DUPA REPARATIE
Verifica explicit:
1. nu mai exista referinte `Date!` sparte in Date_MASTER-C18;
2. workbook-ul se deschide corect;
3. formulele ramase sunt coerente cu foile existente;
4. nu ai introdus cifre business in HTML / FILM;
5. audit_sync ramane cel putin la statusul anterior, cu P0 imgclone deschis;
6. B2 gate ramane nerezolvat si nedeclarat PASS;
7. RELEASE ramane NU.

## LIMITA STRICTA
Nu inlocui imaginile.
Nu atinge B2 gate.
Nu modifica conceptual C18.
Nu reface artefactele.
Nu modifica HTML/FILM decat daca este absolut necesar pentru referinte, caz in care raportezi explicit.
Nu declara release.

## RAPORT
Scrie raport in _brain/c18/CLAUDE-TO-BRAIN.md cu:
- decizia luata;
- ce ai modificat;
- ce ai verificat;
- ce ramane P0;
- verdict: RELEASE = NU.
