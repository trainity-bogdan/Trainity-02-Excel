# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-003

## MANDAT
Propagare sincronizare C03 după BRAIN-002.

## CONTEXT
BRAIN-002 este PASS. Cele 3 reziduuri T1 au fost închise.

A rămas un singur risc deschis:
Noile formulări din FILM C03 există în sursa de adevăr (FILM), dar este posibil să nu fie propagate în HTML-Video și HTML-Editor-Video C03.

## OBIECTIV
Verifică sincronizarea FILM C03 ↔ HTML-Video C03 ↔ HTML-Editor-Video C03.

Dacă există diferențe:
- propagă noile formulări aprobate din FILM către machetele video relevante.

Dacă nu există diferențe:
- nu modifica nimic.

## MODIFICĂRI PERMISE
- HTML-Video C03
- HTML-Editor-Video C03
- fișiere strict necesare sincronizării
- CLAUDE-TO-BRAIN.md

## INTERDICȚII
- nu modifica C01
- nu modifica C02
- nu modifica C04
- nu modifica T2
- nu modifica T3
- nu modifica governance
- nu modifica imagini
- nu modifica xlsx
- nu rescrie conținut nou
- doar sincronizare

## LIVRABIL
Raport complet în CLAUDE-TO-BRAIN.md.

Raportează:
1. dacă exista drift
2. fișiere modificate
3. înainte / după
4. PASS / WARNING / FAIL
5. dacă T1 poate fi considerat închis complet

## MANDAT CURENT
Execută BRAIN-003.