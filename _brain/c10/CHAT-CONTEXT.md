# CHAT-CONTEXT · ANDREI C10 / CLAUDE C10

Acest folder este dedicat exclusiv construcției C10 MĂSURI.

## Comanda unică

În acest chat, comanda este doar:

```text
sync
```

Chat-ul știe singur că lucrează pe C10.

## Pentru Chat Andrei C10

La `sync`, Andrei citește doar:

- `_brain/c10/BRAIN-TO-CLAUDE.md`
- `_brain/c10/CLAUDE-TO-BRAIN.md`
- `_brain/c10/CHAT-CONTEXT.md`

Andrei scrie mandate doar în:

- `_brain/c10/BRAIN-TO-CLAUDE.md`

Andrei C10 NU modifică fișiere sistem.
Dacă apare nevoie de sistem, formulează `CERERE SYSTEM` pentru Chat Andrei SYSTEM.

## Pentru Chat Claude C10

La `sync`, Claude:

1. lucrează exclusiv pe `main`.
2. nu creează branch-uri.
3. citește mandatul din `_brain/c10/BRAIN-TO-CLAUDE.md`.
4. execută doar în:
   - `c10/**`
   - `_brain/c10/**`
5. scrie raportul doar în:
   - `_brain/c10/CLAUDE-TO-BRAIN.md`
6. rulează validările cerute de mandat.
7. face commit descriptiv direct pe `main` și push.

## Fișiere interzise pentru C10

Claude C10 și Andrei C10 nu modifică:

- `c09/**`
- `c11/**`
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
Scrie în `_brain/c10/CLAUDE-TO-BRAIN.md`:

```text
CERERE SYSTEM
Construcție: C10
Fișier comun cerut: ...
Motiv: ...
Impact: ...
Propunere: ...
```

Apoi execuția C10 se oprește până la decizie SYSTEM.
