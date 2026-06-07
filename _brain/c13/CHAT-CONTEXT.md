# CHAT-CONTEXT · ANDREI C13 / CLAUDE C13

Acest folder este dedicat exclusiv construcției C13 VIZUALIZAREA.

## Comanda unică
sync

## Andrei C13 / BRAIN C13
La sync citește doar:
- _brain/c13/CHAT-CONTEXT.md
- _brain/c13/BRAIN-TO-CLAUDE.md
- _brain/c13/CLAUDE-TO-BRAIN.md

Scrie mandate doar în:
- _brain/c13/BRAIN-TO-CLAUDE.md

NU modifică fișiere sistem.
NU modifică alte construcții.
NU implementează artefacte.
Nevoie de sistem = CERERE SYSTEM pentru Chat Andrei SYSTEM.

La comanda Prompt, scrie direct mandatul în:
- _brain/c13/BRAIN-TO-CLAUDE.md
și confirmă doar fișierul + commit-ul. Nu afișa promptul în chat decât dacă ARHITECT cere explicit.

## Claude C13
La sync:
1. lucrează exclusiv pe main, fără branch-uri
2. citește _brain/c13/CHAT-CONTEXT.md
3. citește mandatul din _brain/c13/BRAIN-TO-CLAUDE.md
4. execută doar ce este permis în mandat
5. scrie raportul în _brain/c13/CLAUDE-TO-BRAIN.md
6. rulează validările cerute de mandat
7. commit descriptiv pe main + push

## Fișiere permise pentru Claude C13
- _brain/c13/CLAUDE-TO-BRAIN.md
- c13/** doar dacă mandatul BRAIN permite explicit generare / implementare

## Fișiere interzise pentru C13
- toate celelalte cNN/**
- CLAUDE.md
- README.md
- STARE-CURENTA.md
- index.html
- _system/**
- constructii.xlsx
- gate_v20.py
- audit_sync.py
- COMENZI.yaml
- orice fișier global / sistem

## Nevoie de fișier comun
Claude NU îl modifică. Scrie CERERE SYSTEM în CLAUDE-TO-BRAIN.md și oprește execuția până la decizie.

## Context conceptual C13
C13 = VIZUALIZAREA.
T4 = RAPORTARE.
CUVÂNT LOCKED = VIZUAL.
Verb LOCKED = VIZUALIZEZ.
Axa C13 = ONESTITATEA FORMEI.
Pilon T4 = T4 consumă răspunsul produs de T3. Nu îl naște.

## Stare curentă C13
Obiectiv curent: SPEC 11 SLOT C13.
Nu executa nimic fără mandat în BRAIN-TO-CLAUDE.md.