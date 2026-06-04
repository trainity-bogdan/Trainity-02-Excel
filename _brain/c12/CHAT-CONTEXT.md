# CHAT-CONTEXT · ANDREI C12 / CLAUDE C12

Acest folder este dedicat exclusiv construcției C12 INTERPRETARE.

## Comanda unică

În acest chat, comanda este doar:

```text
sync
```

Chat-ul știe singur că lucrează pe C12.

## Pentru Chat Andrei C12

La `sync`, Andrei citește doar:

- `_brain/c12/BRAIN-TO-CLAUDE.md`
- `_brain/c12/CLAUDE-TO-BRAIN.md`
- `_brain/c12/CHAT-CONTEXT.md`

Andrei scrie mandate doar în:

- `_brain/c12/BRAIN-TO-CLAUDE.md`

Andrei C12 NU modifică fișiere sistem.
Dacă apare nevoie de sistem, formulează `CERERE SYSTEM` pentru Chat Andrei SYSTEM.

## Pentru Chat Claude C12

La `sync`, Claude:

1. lucrează exclusiv pe `main`.
2. nu creează branch-uri.
3. citește mandatul din `_brain/c12/BRAIN-TO-CLAUDE.md`.
4. execută doar în:
   - `c12/**`
   - `_brain/c12/**`
5. scrie raportul doar în:
   - `_brain/c12/CLAUDE-TO-BRAIN.md`
6. rulează validările cerute de mandat.
7. face commit descriptiv direct pe `main` și push.

## Fișiere interzise pentru C12

Claude C12 și Andrei C12 nu modifică:

- `c09/**`
- `c10/**`
- `c11/**`
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
Scrie în `_brain/c12/CLAUDE-TO-BRAIN.md`:

```text
CERERE SYSTEM
Construcție: C12
Fișier comun cerut: ...
Motiv: ...
Impact: ...
Propunere: ...
```

Apoi execuția C12 se oprește până la decizie SYSTEM.

## Stare curentă C12

C12 este construcția INTERPRETARE.
Nu executa nimic fără mandat explicit în `_brain/c12/BRAIN-TO-CLAUDE.md`.
