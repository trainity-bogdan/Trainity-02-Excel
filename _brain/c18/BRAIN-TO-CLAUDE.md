# BRAIN -> CLAUDE C18

## STATUS
C18_AUDIT_TOTAL_CERUT

## CONTEXT
C18 AUTOMATIZAREA. T5 AUTONOMIE. CUVANT MOTOR. VERB AUTOMATIZEZ.

C18 este inchis conceptual, dar generarea raportata ca C18_GENERAT nu este release complet.

BRAIN cere audit total pe C18 generat.

## OBIECTIV
Auditeaza integral C18 generat, fara modificari si fara reparatii.

Scopul auditului este sa stabilesti daca pachetul C18 generat respecta:
- SEED C18 aprobat;
- SPEC 11-slot C18 aprobat;
- blueprint 6 x 3 aprobat;
- artefactul _AUTOMATIZARE;
- granitele C04 / C17 / C19 / C20;
- regulile canonice de release.

## SURSE OBLIGATORII
Citeste si verifica explicit:
1. _brain/c18/BRAIN-TO-CLAUDE.md
2. _brain/c18/CLAUDE-TO-BRAIN.md
3. toate fisierele din c18/
4. intrarile C18 din _system/SISTEM_TRAINITY-versiuni.md
5. intrarile C18 din _system/referinte/IDENTITATE-TEHNICA.md
6. orice fisier Date_MASTER-C18 existent
7. orice FILM C18 existent
8. orice HTML-Studiu / HTML-Editor-Studiu / HTML-Video / HTML-Editor-Video C18 existent
9. orice assets C18 existente
10. referinta c01 doar pentru comparatie anti-clona si COPY+MODIFY, nu pentru contaminare conceptuala.

## AUDIT OBLIGATORIU
Verifica punctual:
1. existenta celor 7 artefacte canonice;
2. numele si locatia fiecarui artefact;
3. daca fiecare artefact respecta SPEC 11-slot C18;
4. daca fiecare artefact respecta blueprint 6 x 3;
5. daca exista drift fata de SEED C18;
6. daca exista contaminare C04: refresh / actualizare in loc de lant;
7. daca exista contaminare C17: sistem / structura / reluare de om in loc de miscare;
8. daca exista contaminare C19: semafor, praguri, validari, alerte, autocontrol, rosu/verde, coduri de alarma;
9. daca exista contaminare C20: ownership, responsabil, escaladare, predare de proprietate;
10. daca exista contaminare C01 prin COPY+MODIFY;
11. daca _AUTOMATIZARE este distinct empiric de _SISTEM;
12. daca declansatorul a devenit buton-identitate;
13. daca imgclone blocheaza release;
14. daca B2 gate blocheaza release;
15. daca exista cifre business in HTML / FILM;
16. daca Date_MASTER respecta R-V02.15;
17. daca FILM respecta axa C18 si predarea catre C19;
18. daca HTML-Video si HTML-Editor-Video sunt sincronizate cu HTML-Studiu;
19. daca Editor-Studiu este sincronizat cu Studiu;
20. daca exista em-dash sau caractere interzise;
21. daca exista texte, clase CSS, imagini sau componente ramase din C01 care slabesc identitatea C18;
22. daca audit_sync este PASS sau ce detectori pica;
23. daca gate_v20 este PASS sau de ce nu poate rula;
24. daca STARE-CURENTA.md este sau nu consolidat;
25. daca C18 poate fi declarat release complet.

## SEVERITATI
Clasifica fiecare problema astfel:
- P0 BLOCKER = blocheaza release;
- P1 GRAV = nu blocheaza tehnic, dar compromite identitatea C18 sau sincronizarea;
- P2 MEDIU = problema reala, dar reparabila fara risc de arhitectura;
- P3 COSMETIC = stil, curatare, mici ramasite fara impact conceptual.

## FORMAT PENTRU FIECARE PROBLEMA
Pentru fiecare problema gasita scrie:
- ID problema;
- severitate;
- fisier;
- locatie exacta sau aproximativa;
- regula incalcata;
- dovada;
- de ce conteaza;
- remediere recomandata;
- blocheaza release: DA / NU.

## FORMAT RAPORT FINAL
Raportul trebuie sa contina:
1. verdict executiv;
2. tabel artefacte gasite / lipsa;
3. status B1 / B2 / B3;
4. status imgclone;
5. status STARE-CURENTA;
6. lista P0;
7. lista P1;
8. lista P2;
9. lista P3;
10. audit contaminare C04 / C17 / C19 / C20;
11. audit _AUTOMATIZARE vs _SISTEM;
12. audit COPY+MODIFY fata de c01;
13. audit HTML-uri;
14. audit Date_MASTER;
15. audit FILM;
16. audit assets;
17. concluzie: RELEASE DA / NU;
18. lista minima de actiuni pentru release complet.

## LIMITA STRICTA
Nu modifica fisiere.
Nu repara nimic.
Nu genera artefacte.
Nu face commit de reparatie.
Nu declara release daca exista P0.
Nu ascunde problemele sub formulari optimiste.

## RAPORT
Scrie auditul complet in _brain/c18/CLAUDE-TO-BRAIN.md.
