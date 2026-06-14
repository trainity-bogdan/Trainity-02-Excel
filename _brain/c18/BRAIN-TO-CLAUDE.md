# BRAIN -> CLAUDE C18

## STATUS
C18_GATE_CONTENT_FIX_CERUT

## CONTEXT
C18 AUTOMATIZAREA. T5 AUTONOMIE. CUVANT MOTOR. VERB AUTOMATIZEZ.

Gate-ul a fost reparat structural in SYSTEM mode si ruleaza acum pe C18.

C18 ramane RELEASE = NU.

B2 inca este FAIL, dar acum din 3 defecte reale de continut C18, nu din config gate.

## DEFECTE DE REPARAT
Repara strict cele 3 defecte de continut raportate de gate:

1. IDENTITY
- `mobile-topbar = "C18 · MOTOR"`
- trebuie sa devina `C18 · Automatizare`
- aplica in HTML-Studiu si HTML-Editor-Studiu.

2. NO-CLONE GENERIC
- `prompt-label` este 100% identic cu C01.
- diferentiaza-l semantic C18, fara sa schimbi structura inutil.
- trebuie sa comunice automatizare / lant / executie recurenta / motor, nu structurare C01.

3. BRAND
- inlocuieste anomaly-title `TUTORIAL DE UNEALTA` sau orice forma cu `tutorial`.
- foloseste o formula brand-safe C18.
- propunere: `BUTON FARA MOTOR` sau `UNEALTA FARA LANT`.
- aplica in HTML-Studiu si HTML-Editor-Studiu.

## LIMITA STRICTA
Nu modifica imagini.
Nu modifica hero base64.
Nu modifica assets.
Nu modifica Date_MASTER.
Nu modifica FILM.
Nu modifica gate_v20.py.
Nu modifica _system.
Nu reface artefactele de la zero.
Nu declara release.

## VERIFICARI DUPA REPARATIE
Verifica explicit:
1. gate_v20 C18;
2. gate_v20 C01;
3. audit_sync;
4. pre_generation_check 18;
5. ca cele 3 defecte de continut au disparut;
6. ca P0 imgclone ramane deschis;
7. ca RELEASE ramane NU.

## RAPORT
Scrie raport in _brain/c18/CLAUDE-TO-BRAIN.md cu:
- ce ai modificat;
- fisiere modificate;
- rezultatul gate C18;
- rezultatul gate C01;
- status audit_sync;
- status pre_generation_check 18;
- ce P0 raman;
- verdict: RELEASE = NU.
