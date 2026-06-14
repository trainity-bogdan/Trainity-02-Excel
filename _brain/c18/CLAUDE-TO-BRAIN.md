# CLAUDE -> BRAIN C18

## STATUS
C18_GATE_DIAGNOSTIC (diagnostic B2 + CERERE SYSTEM; nimic modificat în gate/_system; RELEASE = NU)

## SURSA
Mandat C18_GATE_DIAGNOSTIC_CERUT (commit 8a5152e). Doar diagnostic + propunere. LIMITA respectată: nu am atins gate_v20.py / _system / artefacte; nu declar B2 PASS; nu declar release.

## 1. VERDICT SCURT
B2 nu rulează dintr-o cauză **izolată și benignă**: `gate_v20.py` din acest repo e un **stub** care citește identitățile dintr-un dict hardcodat C01-C17. C18 nu e în dict → gate iese cu eroare înainte de orice verificare. Nu e o problemă a artefactelor C18 (toate celelalte gate-uri trec). Soluția corectă = parser de producție; soluția minimă sigură = adăugarea intrării C18 în dict. Ambele = CERERE SYSTEM (gate forbidden pentru CLAUDE C18).

## 2. CAUZA EXACTĂ
`gate_v20.py`, funcția `load_identitate(NN, ...)` (linia ~1061):
- linia 1064 comentariu: „In productie: parser complet. In acest sample: dict hardcoded."
- linia 1153: `return IDENTITATI.get(NN)` — dict `IDENTITATI` cu chei `01..17`.
- `IDENTITATI.get('18')` → `None`.
- main (linia ~1184): `if not identitate: print("EROARE: IDENTITATE_TEHNICA pentru C18 nu e definita."); sys.exit(1)`.
=> gate se oprește la încărcarea identității, NU ajunge la nicio clasă de verificare. Deci „B2 neverificabil" = gate nu pornește, NU = C18 pică un check.

## 3. FIȘIERE CITITE
- _system/generatoare/gate_v20.py (load_identitate + main)
- _system/generatoare/pre_generation_check.py (rulat: PASS)
- _system/generatoare/audit_sync.py (rulat: C18 doar imgclone)
- _system/arhiva/SISTEM_TRAINITY-versiuni.md (SPEC C18)
- _system/referinte/IDENTITATE-TEHNICA.md (IDENTITATE_TEHNICA C18)

## 4. STATUS INTRĂRI C18 ÎN SISTEM
- SPEC C18 - AUTOMATIZAREA [Status: INGHETAT]: **PREZENT** (SISTEM_TRAINITY-versiuni.md).
- IDENTITATE_TEHNICA C18: **PREZENT** (referinte/IDENTITATE-TEHNICA.md, 24 câmpuri).
- pre_generation_check 18: **TOATE PASS** (B1).
- audit_sync: C18 **doar imgclone XX** (B3).
- gate_v20 dict `IDENTITATI`: **C18 LIPSEȘTE** (singura lacună).
Concluzie pct.2 din mandat: DA, problema e DOAR lipsa C18 din dictul hardcodat. Restul e complet.

## 5. SOLUȚIA MINIMĂ SIGURĂ (patch punctual)
Adăugare intrare C18 în dictul `IDENTITATI` din gate_v20.py, cu cele 4 câmpuri folosite de gate (identice cu IDENTITATE_TEHNICA C18 înghețat):
```
'18': {
    'cod': 'C18', 'nume_hero_caps_rand1': 'AUTOMATIZAREA',
    'nume_slug': 'Automatizare',
    'meta_val_treapta': 'SISTEMATIZARE · <b>AUTOMATIZARE</b> · GUVERNARE · DELEGARE (AUTONOMIE)'
},
```
- Risc: minim. Aditiv (o cheie nouă); NU afectează C01-C17 (`.get(NN)` per cheie).
- Dezavantaj: perpetuează stub-ul — C19 și C20 vor lovi exact același zid.

## 6. SOLUȚIA STRUCTURALĂ RECOMANDATĂ (parser de producție)
Înlocuirea dictului hardcodat cu un **parser** care citește `_system/referinte/IDENTITATE-TEHNICA.md` (sursa unică de adevăr, deja folosită de pre_generation_check). `load_identitate(NN)` extrage secțiunea `## IDENTITATE_TEHNICA C{NN}` și mapează câmpurile.
- Avantaj: rezolvă C18 + C19 + C20 + orice viitor dintr-o lovitură; elimină driftul dict-vs-.md (gate-ul ar valida exact identitatea înghețată, nu o copie hardcodată care poate diverge).
- Aceasta e chiar intenția din comentariul „in productie: parser complet".

## 7. RISCURI
- **Patch punctual:** risc tehnic ~0; risc de proces = uită C19/C20 (datorie repetată).
- **Parser:** risc mediu — schimbă comportamentul gate pentru TOATE construcțiile; trebuie testat că C01-C17 rămân la același verdict (regression). De făcut cu rulare gate pe C01-C17 înainte/după.
- **Contaminare sistem printr-un patch rapid:** NU, dacă se adaugă DOAR cheia C18 (izolat). Pericolul real ar fi un parser scris prost care schimbă validarea C01-C17 — de aceea parserul cere testare de regresie.
- Niciuna nu atinge artefactele C18 (audit + B1 rămân neschimbate).

## 8. PROMPT COMPLET PENTRU CHAT SYSTEM
> MANDAT SYSTEM · gate_v20 nu cunoaște C18 (și va rata C19/C20).
> Cauză: `gate_v20.py` `load_identitate()` returnează dintr-un dict hardcodat C01-C17 (linia ~1153 `return IDENTITATI.get(NN)`; comentariu „in productie: parser complet").
> CERERE: alege una:
> (A) PATCH MINIM — adaugă în dictul `IDENTITATI` cheia `'18'` cu: cod 'C18', nume_hero_caps_rand1 'AUTOMATIZAREA', nume_slug 'Automatizare', meta_val_treapta 'SISTEMATIZARE · <b>AUTOMATIZARE</b> · GUVERNARE · DELEGARE (AUTONOMIE)'. (rapid, deblochează C18 acum)
> (B) STRUCTURAL (recomandat) — rescrie `load_identitate(NN)` să parseze `_system/referinte/IDENTITATE-TEHNICA.md` (secțiunea `## IDENTITATE_TEHNICA C{NN}`), eliminând dictul hardcodat. Rezolvă C18-C20 + viitor.
> OBLIGATORIU după patch: rulează `gate_v20.py 18 c18 c01` → trebuie să PORNEASCĂ și să dea verdict; și rulează gate pe C01-C17 (regresie, dacă alegi B) — verdictele să rămână identice.
> Nu declara C18 release; B2 trebuie să ruleze REAL și să treacă.

## 9. VERDICT
**RELEASE = NU** până când B2 rulează real și trece. C18 e blocat de B2 doar din cauza stub-ului gate (lacună de tooling, nu defect C18). Recomand: SYSTEM aplică (A) acum pentru a debloca C18, plus (B) ca hardening înainte de C19/C20. Eu NU ating gate (CERERE SYSTEM formulată mai sus). Plus P0 imagini (ARHITECT) rămân deschise.

C18_GATE_DIAGNOSTIC
