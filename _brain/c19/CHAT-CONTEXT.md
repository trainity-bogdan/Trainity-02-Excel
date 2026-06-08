# CHAT-CONTEXT · ANDREI C19 / CLAUDE C19

Acest folder este dedicat exclusiv construcției C19 GUVERNAREA.

## Comanda unică
sync

## Andrei C19 / BRAIN C19
La sync citește doar:
- _brain/c19/CHAT-CONTEXT.md
- _brain/c19/BRAIN-TO-CLAUDE.md
- _brain/c19/CLAUDE-TO-BRAIN.md

Scrie mandate doar în:
- _brain/c19/BRAIN-TO-CLAUDE.md

NU modifică fișiere sistem.
NU modifică alte construcții.
NU implementează artefacte.
Nevoie de sistem = CERERE SYSTEM pentru Chat Andrei SYSTEM.

La comanda Prompt, scrie direct mandatul în:
- _brain/c19/BRAIN-TO-CLAUDE.md
și confirmă doar fișierul + commit-ul. Nu afișa promptul în chat decât dacă ARHITECT cere explicit.

## Claude C19
La sync:
1. lucrează exclusiv pe main, fără branch-uri
2. citește _brain/c19/CHAT-CONTEXT.md
3. citește mandatul din _brain/c19/BRAIN-TO-CLAUDE.md
4. execută doar ce este permis în mandat
5. scrie raportul în _brain/c19/CLAUDE-TO-BRAIN.md
6. rulează validările cerute de mandat
7. commit descriptiv pe main + push

## Fișiere permise pentru Claude C19
- _brain/c19/CLAUDE-TO-BRAIN.md
- c19/** doar dacă mandatul BRAIN permite explicit generare / implementare

## Fișiere interzise pentru C19
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

## Context conceptual C19
C19 = GUVERNAREA.
T5 = AUTONOMIE.
CUVÂNT LOCKED = CONTROL.
Verb LOCKED = GUVERNEZ.
Axa C19 = DAI SISTEMULUI REGULI CARE ÎL ȚIN CORECT FĂRĂ SUPRAVEGHERE.
Pilon T5 = T5 consumă raportul livrabil (T4) și îl face să funcționeze fără autor.

## Stare curentă C19
Obiectiv curent: SEED conceptual + SPEC 11-slot C19.
Nu executa nimic fără mandat în BRAIN-TO-CLAUDE.md.
