# BRAIN -> CLAUDE C16

## STATUS
MANDAT_BRAIN_ACTIV

## CONTEXT
C16 LIVRAREA. T4 RAPORTARE. CUVÂNT LIVRARE. VERB LIVREZ.

Identitate blocată:
- C16 = LIVRAREA
- T4 = RAPORTARE
- CUVÂNT LOCKED = LIVRARE
- VERB LOCKED = LIVREZ
- Rol în T4: transformarea raportului într-un material decision-ready, predabil decidentului
- Graniță în jos: C15 = mesajul esențial sintetizat
- Graniță în sus: C17 = sistematizarea raportului în T5 AUTONOMIE

## MANDAT

Claude C16, la următorul sync:

1. Citește strict:
   - _brain/c16/CHAT-CONTEXT.md
   - _brain/c16/BRAIN-TO-CLAUDE.md
   - _brain/c16/CLAUDE-TO-BRAIN.md

2. Construiește SEED conceptual C16 pentru LIVRAREA, fără implementare de artefacte.

3. Construiește propunerea SPEC 11-slot C16 pentru slotul C16 din T4 RAPORTARE.

4. Respectă obligatoriu granițele:
   - C15 sintetizează mesajul esențial. C16 NU mai sintetizează.
   - C16 livrează raportul ca material decision-ready.
   - C17 sistematizează raportul în T5 AUTONOMIE. C16 NU creează sistem recurent, procedură autonomă, dashboard viu sau automatizare.

5. Evită explicit reducerea LIVRĂRII la logistică:
   - nu email
   - nu export
   - nu PDF ca simplă formă tehnică
   - nu share
   - nu trimitere
   - nu predare administrativă

6. Definește LIVRAREA ca transformarea raportului într-un obiect de decizie:
   - clar pentru decident
   - complet fără a fi aglomerat
   - predabil fără explicații suplimentare inutile
   - orientat spre decizie, risc, concluzie și următor pas

7. Raportează în _brain/c16/CLAUDE-TO-BRAIN.md cu:
   - SEED conceptual propus
   - SPEC 11-slot propus
   - riscuri conceptuale
   - granițe confirmate
   - eventuale întrebări strict necesare pentru BRAIN

8. Nu modifica:
   - c16/**
   - alte cNN/**
   - fișiere sistem
   - fișiere globale
   - alte foldere _brain/cYY/**

9. Dacă apare nevoie de sistem, scrie doar CERERE SYSTEM în _brain/c16/CLAUDE-TO-BRAIN.md și oprește execuția.

## RAPORT
Scrie raportul în _brain/c16/CLAUDE-TO-BRAIN.md.
