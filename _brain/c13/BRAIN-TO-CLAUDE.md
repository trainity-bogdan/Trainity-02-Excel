# BRAIN → CLAUDE · C13 VIZUALIZAREA

## STATUS
BRAIN_C13_TOTAL_AUDIT_REQUESTED

## MANDAT-ID
C13-TOTAL-AUDIT-015

## CONTEXT
C13 are PASS FINAL BRAIN, dar ARHITECT cere acum un audit total, independent de verdictul anterior.

Scopul auditului nu este să refaci C13, ci să verifici complet dacă C13 este solid conceptual, tehnic și sistemic.

## REGULĂ ABSOLUTĂ
Acesta este AUDIT, nu implementare.

Nu modifica artefacte C13.
Nu modifica fișiere sistem.
Nu modifica alte construcții.
Nu face cleanup.
Nu rearanaja fișiere.
Nu reface conținut.

Scrie doar raportul de audit în:

`_brain/c13/CLAUDE-TO-BRAIN.md`

## FIȘIERE PE CARE AI VOIE SĂ LE CITEȘTI
Pentru audit total, ai voie să citești:
- `_brain/c13/CHAT-CONTEXT.md`
- `_brain/c13/BRAIN-TO-CLAUDE.md`
- `_brain/c13/CLAUDE-TO-BRAIN.md`
- `c13/**`
- `_system/**`
- `gate_v20.py`, dacă există la root
- `audit_sync.py`
- `COMENZI.yaml`
- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `c12/**`, doar pentru comparație de pattern
- `c14/**`, doar dacă există și doar pentru verificare de graniță C13/C14

## FIȘIERE PE CARE AI VOIE SĂ LE MODIFICI
Ai voie să modifici doar:
- `_brain/c13/CLAUDE-TO-BRAIN.md`

## FIȘIERE INTERZISE LA MODIFICARE
Nu modifica:
- `c13/**`
- `_system/**`
- `gate_v20.py`
- `audit_sync.py`
- `COMENZI.yaml`
- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `index.html`
- `constructii.xlsx`
- `c01/**` până la `c20/**`
- alte foldere `_brain/cXX`

## AUDIT TOTAL CERUT
Execută audit complet pe C13, pe următoarele axe:

### 1. Inventar fizic
Verifică existența livrabilelor:
- HTML-Studiu C13
- HTML-Editor-Studiu C13
- HTML-Video C13
- HTML-Editor-Video C13
- Date_MASTER-C13.xlsx
- FILM C13
- build scripts C13
- assets C13, dacă există sau dacă sunt pending

### 2. Trasabilitate Git
Verifică:
- commitul artefactelor C13 raportat: `7f21656bac0cf0053a32a996e53d16626a7cce7c`
- dacă artefactele sunt pe main
- dacă există modificări necomise
- dacă raportul actual reflectă starea reală

### 3. Validări tehnice
Rulează sau verifică, fără modificări:
- B1 `pre_generation_check.py 13`
- B2 `gate_v20.py 13 c13 c01`
- B3 `audit_sync` pe C13, în forma folosită de repo
- verificare existență fișiere
- verificare sincronizare Studiu cu Editor-Studiu
- verificare sincronizare Video cu Editor-Video
- verificare 18 step-titles locked
- verificare em-dash / en-dash
- verificare reziduuri C12
- verificare scope, fără modificări în afara C13

Dacă un validator nu poate fi rulat exact, raportează comanda încercată și motivul.

### 4. Audit conceptual C13
Verifică strict:
- C13 = VIZUALIZAREA
- T4 = RAPORTARE
- CUVÂNT LOCKED = VIZUAL
- VERB LOCKED = VIZUALIZEZ
- axă = ONESTITATEA FORMEI
- C13 transformă un rezultat deja produs într-un obiect vizual onest
- C13 nu descoperă cauza, nu interpretează ca C12
- C13 nu compune pagina ca C14
- C13 nu sintetizează mesajul ca C15
- C13 nu livrează raport decision-ready ca C16

### 5. Audit granițe
Verifică dacă există contaminări:
- dashboard final în C13
- layout final de pagină
- mesaj sintetic C15
- livrare C16
- cauzalitate C12
- analiză nouă care ar aparține T3

Orice contaminare trebuie marcată cu severitate.

### 6. Audit SPEC locked
Verifică prezența și fidelitatea:
- intriga: "Cifra e corectă. Graficul minte."
- miza
- mantra
- AHA
- WOW
- motto
- cele 6 fenomene
- cele 18 step-titles locked
- cele 2 prompturi
- cele 8 final-labels, dacă apar în registru sau în artefacte

### 7. Audit Workbook
Verifică `Date_MASTER-C13.xlsx`:
- numele este cel acceptat de gate
- continuitatea datelor este păstrată
- foaia `Vizualizare` există
- workbook-ul este suport pentru obiect vizual onest, nu dashboard
- nu apar charturi / dashboard final / pagină finală, dacă poți verifica
- decizia despre cifre este respectată: cifrele trăiesc în Excel, nu sunt preafișate ca rezultat final în HTML/FILM

### 8. Audit HTML Studiu și Editor-Studiu
Verifică:
- identitate C13
- hero `VIZUAL`
- topbar / footer / next section
- 18 pași
- sync 1:1 între Studiu și Editor-Studiu, cu strat editor separat
- zero drift conceptual

### 9. Audit Video și Editor-Video
Verifică:
- broadcast C13
- STAGES sincronizate
- step-titles respectate
- exec slides compatibile cu C13
- assets placeholder sau pending tratate corect
- Editor-Video sincronizat cu Video

### 10. Audit FILM
Verifică:
- FILM respectă cele 6 etape
- nu introduce dashboard
- nu introduce mesaj C15
- nu introduce livrare C16
- păstrează ONESTITATEA FORMEI

### 11. Audit R-V02.15
Verifică regula:
Cifrele business nu trebuie preafișate în HTML / FILM ca rezultat final.

Cifrele se citesc, se demonstrează și se validează live în Excel.

### 12. Audit datorii acceptate
Verifică și clasifică:
- assets C13 pending
- 1 XX pe R-V39.assets
- build scripts în `c13/`
- `load_identitate` hardcoded, risc pentru C14-C20

Spune clar ce este:
- BLOCKER
- MINOR
- ACCEPTED DEBT
- SYSTEM FUTURE

## FORMAT RAPORT CERUT
Scrie raportul în `_brain/c13/CLAUDE-TO-BRAIN.md` cu structura:

1. STATUS
2. Verdict general
3. Inventar livrabile
4. Validări rulate
5. Rezultate validări
6. Audit conceptual
7. Audit granițe C12/C13/C14/C15/C16
8. Audit SPEC locked
9. Audit workbook
10. Audit HTML Studiu / Editor-Studiu
11. Audit Video / Editor-Video
12. Audit FILM
13. Audit R-V02.15
14. Datorii acceptate și riscuri viitoare
15. Probleme găsite, cu severitate
16. Recomandări, fără implementare
17. Commit SHA al raportului de audit
18. Verdict final

## STATUS AȘTEPTAT
Dacă totul este valid, cu doar datorii acceptate:

`CLAUDE_C13_TOTAL_AUDIT_PASS_WITH_ACCEPTED_DEBTS`

Dacă există probleme non-blocante:

`CLAUDE_C13_TOTAL_AUDIT_PASS_WITH_MINOR_FINDINGS`

Dacă există probleme blocante:

`CLAUDE_C13_TOTAL_AUDIT_FAIL_BLOCKERS_FOUND`

Dacă auditul nu poate fi dus la capăt:

`CLAUDE_C13_TOTAL_AUDIT_BLOCKED`

## CERERE DIRECTĂ
Execută audit total C13. Nu modifica artefacte. Nu repara nimic. Doar verifică și raportează brutal, complet, trasabil.