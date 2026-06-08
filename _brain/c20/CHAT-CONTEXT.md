# CHAT-CONTEXT · ANDREI C20 / CLAUDE C20

Acest folder este dedicat exclusiv construcției C20 DELEGAREA.

## Comanda unică
sync

## Andrei C20 / BRAIN C20
La sync citește doar:
- _brain/c20/CHAT-CONTEXT.md
- _brain/c20/BRAIN-TO-CLAUDE.md
- _brain/c20/CLAUDE-TO-BRAIN.md

Scrie mandate doar în:
- _brain/c20/BRAIN-TO-CLAUDE.md

NU modifică fișiere sistem.
NU modifică alte construcții.
NU implementează artefacte.
Nevoie de sistem = CERERE SYSTEM pentru Chat Andrei SYSTEM.

La comanda Prompt, scrie direct mandatul în:
- _brain/c20/BRAIN-TO-CLAUDE.md
și confirmă doar fișierul + commit-ul. Nu afișa promptul în chat decât dacă ARHITECT cere explicit.

## Claude C20
La sync:
1. lucrează exclusiv pe main, fără branch-uri
2. citește _brain/c20/CHAT-CONTEXT.md
3. citește mandatul din _brain/c20/BRAIN-TO-CLAUDE.md
4. execută doar ce este permis în mandat
5. scrie raportul în _brain/c20/CLAUDE-TO-BRAIN.md
6. rulează validările cerute de mandat
7. commit descriptiv pe main + push

## Fișiere permise pentru Claude C20
- _brain/c20/CLAUDE-TO-BRAIN.md
- c20/** doar dacă mandatul BRAIN permite explicit generare / implementare

## Fișiere interzise pentru C20
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

## Context conceptual C20
C20 = DELEGAREA.
T5 = AUTONOMIE.
CUVÂNT LOCKED = AUTONOMIE.
Verb LOCKED = DELEG.
Axa C20 = PREDAI SISTEMUL CA SĂ LUCREZE FĂRĂ TINE (construcția semnătură, închide pack-ul).
Pilon T5 = T5 consumă raportul livrabil (T4) și îl face să funcționeze fără autor.

## Stare curentă C20
Obiectiv curent: SEED conceptual + SPEC 11-slot C20.
Nu executa nimic fără mandat în BRAIN-TO-CLAUDE.md.
