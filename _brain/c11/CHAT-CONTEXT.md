# CHAT-CONTEXT · ANDREI C11 / CLAUDE C11

Acest folder este dedicat exclusiv construcției C11 COMPARAȚII / RANK.

## Comanda unică

În acest chat, comanda este doar:

```text
sync
```

Chat-ul știe singur că lucrează pe C11.

## Pentru Chat Andrei C11

La `sync`, Andrei citește doar:

- `_brain/c11/BRAIN-TO-CLAUDE.md`
- `_brain/c11/CLAUDE-TO-BRAIN.md`
- `_brain/c11/CHAT-CONTEXT.md`

Andrei scrie mandate doar în:

- `_brain/c11/BRAIN-TO-CLAUDE.md`

Andrei C11 NU modifică fișiere sistem.
Dacă apare nevoie de sistem, formulează `CERERE SYSTEM` pentru Chat Andrei SYSTEM.

## Pentru Chat Claude C11

La `sync`, Claude:

1. lucrează exclusiv pe `main`.
2. nu creează branch-uri.
3. citește mandatul din `_brain/c11/BRAIN-TO-CLAUDE.md`.
4. execută doar în:
   - `c11/**`
   - `_brain/c11/**`
5. scrie raportul doar în:
   - `_brain/c11/CLAUDE-TO-BRAIN.md`
6. rulează validările cerute de mandat.
7. face commit descriptiv direct pe `main` și push.

## Fișiere interzise pentru C11

Claude C11 și Andrei C11 nu modifică:

- `c09/**`
- `c10/**`
- `c12/**`
- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `index.html`
- `_system/**`
- `gate_v20.py`
- `audit_sync.py`
- `COMENZI.yaml`
- orice fișier global / sistem

## Dacă apare nevoie de fișier comun

Claude NU modifică fișierul comun.
Scrie în `_brain/c11/CLAUDE-TO-BRAIN.md`:

```text
CERERE SYSTEM
Construcție: C11
Fișier comun cerut: ...
Motiv: ...
Impact: ...
Propunere: ...
```

Apoi execuția C11 se oprește până la decizie SYSTEM.

## Stare curentă C11

C11 este construcția COMPARAȚII / RANK.
Nu executa nimic fără mandat explicit în `_brain/c11/BRAIN-TO-CLAUDE.md`.
