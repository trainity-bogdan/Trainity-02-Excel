# BRAIN -> CLAUDE C18

## STATUS
C18_REPARATIE_P2_FINALA_CERUTA

## CONTEXT
Auditul final monstru este finalizat.

Status actual:
- B1 = PASS;
- B2 = PASS;
- gate C01 = PASS;
- B3 = PASS mai putin imgclone;
- contaminare C04 / C17 / C19 / C20 = PASS;
- Date_MASTER = PASS;
- FILM = PASS;
- HTML-uri = PASS, cu exceptia celor 2 P2 raportate;
- RELEASE = NU.

Singurul P0 ramas:
- imaginile clone C01.

Auditul final a gasit 2 defecte P2 reale.

Acest mandat repara EXCLUSIV aceste 2 defecte.

## OBIECTIV
Inchide cele 2 P2 identificate de auditul final monstru.

## P2-1 DOWNLOAD FILENAME RAMAS C01
Fisiere:
- HTML-Editor-Studiu
- HTML-Editor-Video

Audit:
Editorul salveaza inca:
- HTML-Studiu-Excel-01-Structurare-Editat.html
- HTML-Video-Excel-01-Structurare-Editat.html

Trebuie sa devina:
- HTML-Studiu-Excel-18-Automatizare-Editat.html
- HTML-Video-Excel-18-Automatizare-Editat.html

Verifica toate referintele JS asociate.

## P2-2 VIDEO TITLE GRESIT
Audit:
Video title este:
- C18 · MOTOR · BROADCAST

Conform IDENTITATE_TEHNICA trebuie sa fie:
- C18 · AUTOMATIZARE · BROADCAST

Aplica in:
- HTML-Video
- HTML-Editor-Video

Verifica sa nu existe alte aparitii similare.

## VERIFICARI OBLIGATORII
Dupa reparatie ruleaza:
1. gate_v20 C18;
2. gate_v20 C01;
3. audit_sync;
4. pre_generation_check 18.

Verifica explicit:
- download filenames C01 = 0;
- title video MOTOR = 0;
- AUTOMATIZARE = corect;
- imgclone ramane singurul P0;
- nu apar regresii C01-C17.

## LIMITA STRICTA
Nu modifica imagini.
Nu modifica hero base64.
Nu modifica assets.
Nu modifica Date_MASTER.
Nu modifica FILM.
Nu modifica gate_v20.py.
Nu modifica _system.
Nu declara release.

## RAPORT
Scrie in _brain/c18/CLAUDE-TO-BRAIN.md si include:
1. fisiere modificate;
2. modificari efectuate;
3. rezultat gate C18;
4. rezultat gate C01;
5. rezultat audit_sync;
6. rezultat pre_generation_check 18;
7. confirmare ca P2-1 este inchis;
8. confirmare ca P2-2 este inchis;
9. lista P0 ramase;
10. verdict final.

## VERDICT ASTEPTAT
RELEASE = NU.

Singurul P0 permis dupa acest mandat:
- imgclone / imaginile C18.
