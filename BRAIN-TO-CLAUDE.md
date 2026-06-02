# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-004

## MANDAT
Construiește C09 RELAȚII ca prima construcție din T3.

## CONTEXT
Raportul BRAIN-003-CORRECTED spune că T3 este suficient de clară pentru start C09 și că C09 este PASS.

Suntem la TREAPTA 3, nu la Construcția 03.

T3:
- C09 Relații
- C10 Măsuri
- C11 Comparații
- C12 Interpretare

C09 = leagă.
C10 = măsoară.
C11 = compară.
C12 = explică.

## SURSE
Folosește:
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md
- _system/blueprints/BLUEPRINT-C09-RELATII.md
- c08 doar pentru handoff către C09
- structura tehnică deja existentă în proiect ca reper de formă

## IDENTITATE C09
HERO: Cum transform legăturile în răspunsuri?
BOMBĂ: Ai toate datele. Și niciun răspuns.
GREȘEALA: Oamenii copiază coloane dintr-un tabel în altul. Profesioniștii le leagă o dată.
AHA: Fără relații ai date. Cu relații ai răspunsuri.
MANTRA: Nu mutăm datele. Le legăm.
WOW: Tabele care stăteau alături fără să se cunoască. Acum răspund împreună la o singură întrebare.
MOTTO: Întrebi o dată. Modelul răspunde.
CINE DEVII: Nu mai vezi o rețea. O interoghezi.
PAYOFF: Un set cunoscut a devenit un model care răspunde.

## FIȘIERE PERMISE LA MODIFICARE
- c09/**
- fișiere noi pentru c09, dacă lipsesc
- index / registry / manifest doar dacă sistemul cere includerea C09
- CLAUDE-TO-BRAIN.md

## FIȘIERE INTERZISE LA MODIFICARE
- c01/** până la c08/**
- README.md
- CLAUDE.md
- STARE-CURENTA.md
- _system/governance/**

## REGULI
- Lucrează doar pe main.
- Nu crea branch.
- Nu crea PR.
- Respectă blueprint-ul C09.
- Nu schimba identitatea C09.
- Nu transforma C09 în C10, C11 sau C12.
- Nu transforma C09 în raportare vizuală sau decizie.
- Verifică reziduuri din construcțiile vechi.

## TESTE
Rulează testele / gate-urile disponibile pentru C09.
Raportează PASS / WARNING / FAIL.

## LIVRABIL
Scrie raportul complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere create
5. Fișiere modificate
6. Ce ai construit pentru C09
7. Teste rulate
8. Rezultate
9. Probleme rămase
10. Decizii cerute de la BRAIN
11. Commit / status Git

## MANDAT CURENT
Execută BRAIN-004.
