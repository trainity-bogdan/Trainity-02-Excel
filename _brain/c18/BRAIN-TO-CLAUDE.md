# BRAIN -> CLAUDE C18

## STATUS
C18_AUDIT_FINAL_MONSTRU_CERUT

## CONTEXT
C18 AUTOMATIZAREA. T5 AUTONOMIE. CUVANT MOTOR. VERB AUTOMATIZEZ.

Ultimul status raportat de Claude:
- B1 pre_generation_check 18 = PASS;
- B2 gate C18 = PASS;
- gate C01 = PASS;
- audit_sync = PASS mai putin imgclone;
- P2 reparat;
- CONTROL_FINAL reparat;
- defectele gate de continut reparate;
- RELEASE = NU deoarece imaginile raman clone C01.

BRAIN cere acum audit final monstru, mod adversarial, fara reparatii.

## OBIECTIV
Auditeaza complet C18 ca si cum ar fi gresit.

Scopul nu este sa confirmi rapoartele anterioare, ci sa gasesti orice defect ramas inainte de release.

## LIMITA STRICTA
Nu modifica fisiere.
Nu repara nimic.
Nu inlocui imagini.
Nu modifica gate.
Nu modifica _system.
Nu modifica artefacte.
Nu declara release.
Doar audit.

## SURSE OBLIGATORII
Verifica empiric:
1. toate fisierele din c18/;
2. HTML-Studiu C18;
3. HTML-Editor-Studiu C18;
4. HTML-Video C18;
5. HTML-Editor-Video C18;
6. FILM C18;
7. Date_MASTER-C18.xlsx;
8. assets C18;
9. _brain/c18/BRAIN-TO-CLAUDE.md;
10. _brain/c18/CLAUDE-TO-BRAIN.md;
11. _system/SISTEM_TRAINITY-versiuni.md pentru C18;
12. _system/referinte/IDENTITATE-TEHNICA.md pentru C18;
13. gate_v20.py doar pentru citire;
14. rezultatele gate / audit_sync / pre_generation_check;
15. c01 doar pentru comparatie anti-clona.

## AUDIT OBLIGATORIU
Verifica punctual:
1. existenta celor 7 artefacte canonice;
2. numele si locatia fiecarui artefact;
3. sincronizarea Studiu vs Editor-Studiu;
4. sincronizarea Video vs Editor-Video;
5. sincronizarea HTML-uri vs FILM;
6. sincronizarea HTML-uri vs Date_MASTER;
7. respectarea SEED C18;
8. respectarea SPEC 11-slot C18;
9. respectarea blueprint 6 x 3;
10. existenta si distinctia _AUTOMATIZARE vs _SISTEM;
11. daca declansatorul a devenit buton-identitate;
12. daca MOTOR este folosit corect ca brand/cuvant si nu ca slug gresit;
13. daca AUTOMATIZARE este folosit corect ca slug;
14. daca AUTOMATIZEZ apare corect ca verb-semnatura;
15. daca hero, topbar, meta, title, mobile-topbar sunt coerente;
16. daca prompt-label-urile sunt diferentiate de C01;
17. daca anomaly-title-urile sunt brand-safe;
18. daca exista cuvantul tutorial sau alte cuvinte brand-interzise;
19. daca exista em-dash sau caractere interzise;
20. daca exista cifre business in HTML / FILM;
21. daca exista contaminare C04: refresh / actualizare in loc de lant;
22. daca exista contaminare C17: sistem / structura in loc de miscare;
23. daca exista contaminare C19: praguri / validari / alerte / semafor / autocontrol;
24. daca exista contaminare C20: ownership / responsabil / escaladare / predare proprietate;
25. daca exista contaminare C01 prin copy-modify;
26. daca exista texte C01 ramase: structura, structurare, ambalaj, realitate, datare, cartografiere, etc.;
27. daca exista assets cu nume C01;
28. daca hero base64 este inca clona C01;
29. daca exec-stage images sunt inca clone C01;
30. daca imgclone este singurul detector audit_sync care pica;
31. daca gate C18 este PASS real;
32. daca gate C01 ramane PASS;
33. daca pre_generation_check 18 este PASS;
34. daca Date_MASTER are formule sparte;
35. daca Date_MASTER are foi meta C01 ramase;
36. daca CONTROL_FINAL este coerent dupa reparatie;
37. daca STARE-CURENTA este consolidat sau ramane datorie SYSTEM;
38. daca C18 poate intra in release dupa imagini;
39. ce blocheaza release acum;
40. daca exista orice defect neraportat anterior.

## FORMAT PROBLEME
Pentru fiecare problema gasita scrie:
- ID;
- severitate: P0 / P1 / P2 / P3;
- fisier;
- locatie;
- dovada;
- regula incalcata;
- de ce conteaza;
- remediere recomandata;
- blocheaza release: DA / NU.

## SEVERITATI
- P0 = blocheaza release.
- P1 = compromite identitatea C18 sau validarea.
- P2 = problema reala reparabila fara risc arhitectural.
- P3 = curatare cosmetica.

## RAPORT FINAL
Raportul trebuie sa contina:
1. verdict executiv;
2. tabel artefacte gasite;
3. status B1 / B2 / B3;
4. status imgclone;
5. status gate C18 / gate C01;
6. status pre_generation_check 18;
7. status STARE-CURENTA;
8. lista P0;
9. lista P1;
10. lista P2;
11. lista P3;
12. audit contaminare C04 / C17 / C19 / C20;
13. audit copy-modify C01;
14. audit imagini / assets;
15. audit Date_MASTER;
16. audit FILM;
17. audit HTML-uri;
18. verdict RELEASE DA / NU;
19. lista minima de actiuni pentru release complet.

## REGULA FINALA
Daca exista macar un P0, verdictul este RELEASE = NU.
Daca singurul P0 ramas este imgclone / imagini, spune explicit.
Nu cosmetiza raportul.
Nu ascunde defecte.
Nu raporta PASS fara dovada.

## RAPORT
Scrie auditul final monstru in _brain/c18/CLAUDE-TO-BRAIN.md.
