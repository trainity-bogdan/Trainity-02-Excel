# CLAUDE -> BRAIN C18

## STATUS
CERERE_SYSTEM_BLOCAJ_B1 (mandat ARHITECT "genereaza tot" primit; generare BLOCATA de dependenta de sistem; opresc executia, astept decizie)

## SURSA
ARHITECT a dat mandat direct in chat: "genereaza tot" = cele 7 artefacte C18. Pachet conceptual = LOCKED (SEED + SPEC 11-slot + SLUG Automatizare + blueprint 6x3 + _AUTOMATIZARE, confirmat C18_LOCKED). La pasul B1 (pre_generation_check.py 18) generarea e BLOCATA.

## BLOCAJ B1 - toate dependentele sunt in _system/** (in afara scope-ului CLAUDE C18)
1. **R-V03.55:** `_system/arhiva/SISTEM_TRAINITY-versiuni.md` linia 2975 = `## SPEC C18 - AUTOMATIZAREA [Status: NEGENERAT]`. Generatorul cere [Status: INGHETAT] cu cele 9 elemente narative (INTRIGA / PROBLEME / MIZA / MANTRA / MOTTO / STEP-TITLES / PROMPTURI / FINAL-LABELS / FENOMENE). SPEC-ul nostru e aprobat in CANALUL BRAIN, dar generatorul citeste REGISTRUL de sistem.
2. **L142:** `_system/referinte/IDENTITATE-TEHNICA.md` -> sectiunea `## IDENTITATE_TEHNICA C18` LIPSESTE (C01-C16 exista; C17-C20 nu). Necesita ~20 campuri tehnice (cod, treapta_nr, nume_slug, nume_hero_caps_rand1, meta_val_treapta, footer_text, topbar_text, localStorage_studiu, localStorage_video, next_cod=C19, next_nume_title etc.), consistente cu C01-C17.
3. **L143:** FENOMENE C18 verificate empiric vs `_system/referinte/Date_MASTER-initial.xlsx` (coloane reale).

## DE CE E CERERE SYSTEM
CHAT-CONTEXT C18: `_system/**` = INTERZIS pentru CLAUDE C18. Regula: "nevoie de fisier comun -> Claude NU il modifica -> CERERE SYSTEM + opreste executia pana la decizie." Cele 3 fisiere sunt partajate de TOATE constructiile (C01-C20). B1 e regula blocanta (CLAUDE.md), nu se ignora.

## NOTA SISTEMICA
Si C17 (acum "in generare", Date_MASTER _SISTEM facut) are in registru SPEC C17 [Status: NEGENERAT] + IDENTITATE_TEHNICA C17 lipsa. Deci freeze-ul in registru e un gap deschis pentru intreg T5 (C17-C20), nu doar C18.

## OPTIUNI PENTRU ARHITECT
**A (recomandat):** autorizezi CLAUDE C18 sa scrie DOAR intrarile C18 in cele 3 fisiere `_system` (inghet SPEC C18 in registru cu cele 9 elemente din pachetul aprobat + IDENTITATE_TEHNICA C18 consistent cu C01-C17 + verificare FENOMENE), apoi rulez B1 -> PASS si generez cele 7 artefacte (COPY+MODIFY din c01/), cu B2 gate v20 + B3 audit_sync dupa. Am pachetul complet aprobat, pot face freeze-ul corect.
**B:** freeze-ul SPEC + IDENTITATE_TEHNICA C18 se face intr-un chat SYSTEM dedicat; eu astept si apoi rulez doar generarea.

## RECOMANDARE
A - autorizatie punctuala sa ating `_system/**` exclusiv pentru intrarile C18 (nu ating alte constructii), cu gate + audit dupa. E cel mai rapid drum la "genereaza tot".

CERERE_SYSTEM_BLOCAJ_B1
