# CHAT-CONTEXT · ANDREI C14 / CLAUDE C14

Acest folder este dedicat exclusiv construcției C14 COMPUNEREA.

## Comanda unică
sync

## Andrei C14 / BRAIN C14
La sync citește doar:
- _brain/c14/CHAT-CONTEXT.md
- _brain/c14/BRAIN-TO-CLAUDE.md
- _brain/c14/CLAUDE-TO-BRAIN.md

Scrie mandate doar în:
- _brain/c14/BRAIN-TO-CLAUDE.md

NU modifică fișiere sistem.
NU modifică alte construcții.
NU implementează artefacte.
Nevoie de sistem = CERERE SYSTEM pentru Chat Andrei SYSTEM.

La comanda Prompt, scrie direct mandatul în:
- _brain/c14/BRAIN-TO-CLAUDE.md
și confirmă doar fișierul + commit-ul. Nu afișa promptul în chat decât dacă ARHITECT cere explicit.

## Claude C14
La sync:
1. lucrează exclusiv pe main, fără branch-uri
2. citește _brain/c14/CHAT-CONTEXT.md
3. citește mandatul din _brain/c14/BRAIN-TO-CLAUDE.md
4. execută doar ce este permis în mandat
5. scrie raportul în _brain/c14/CLAUDE-TO-BRAIN.md
6. rulează validările cerute de mandat
7. commit descriptiv pe main + push

## Fișiere permise pentru Claude C14
- _brain/c14/CLAUDE-TO-BRAIN.md
- c14/** doar dacă mandatul BRAIN permite explicit generare / implementare

## Fișiere interzise pentru C14
- toate celelalte cNN/**
- alte _brain/cYY/**
- CLAUDE.md
- README.md
- STARE-CURENTA.md
- index.html
- _system/**
- governance/**
- constructii.xlsx
- gate_v20.py
- audit_sync.py
- COMENZI.yaml
- orice fișier global / sistem

## Nevoie de fișier comun
Claude NU îl modifică. Scrie CERERE SYSTEM în CLAUDE-TO-BRAIN.md și oprește execuția până la decizie.

## Context conceptual C14
C14 = COMPUNEREA.
T4 = RAPORTARE.
CUVÂNT LOCKED = COMPOZIȚIE.
Verb LOCKED = COMPUN.
Axa C14 = ORGANIZAREA SPAȚIALĂ A ELEMENTELOR VIZUALE.
Pilon T4 = T4 consumă răspunsul produs de T3. Nu îl naște.

## Stare curentă C14
Obiectiv curent: SEED conceptual + SPEC 11-slot C14.
Nu executa nimic fără mandat în BRAIN-TO-CLAUDE.md.
