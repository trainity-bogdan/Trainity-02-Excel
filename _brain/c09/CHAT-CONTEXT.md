# CHAT-CONTEXT · ANDREI C09 / CLAUDE C09

Acest folder este dedicat exclusiv construcției C09 RELAȚII.

## Comanda unică

În acest chat, comanda este doar:

```text
sync
```

Chat-ul știe singur că lucrează pe C09.

## Pentru Chat Andrei C09

La `sync`, Andrei citește doar:

- `_brain/c09/BRAIN-TO-CLAUDE.md`
- `_brain/c09/CLAUDE-TO-BRAIN.md`
- `_brain/c09/CHAT-CONTEXT.md`

Andrei scrie mandate doar în:

- `_brain/c09/BRAIN-TO-CLAUDE.md`

Andrei C09 NU modifică fișiere sistem.
Dacă apare nevoie de sistem, formulează `CERERE SYSTEM` pentru Chat Andrei SYSTEM.

## Pentru Chat Claude C09

La `sync`, Claude:

1. lucrează exclusiv pe `main`.
2. nu creează branch-uri.
3. citește mandatul din `_brain/c09/BRAIN-TO-CLAUDE.md`.
4. execută doar în:
   - `c09/**`
   - `_brain/c09/**`
5. scrie raportul doar în:
   - `_brain/c09/CLAUDE-TO-BRAIN.md`
6. rulează validările cerute de mandat.
7. face commit descriptiv direct pe `main` și push.

## Fișiere interzise pentru C09

Claude C09 și Andrei C09 nu modifică:

- `c10/**`
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
Scrie în `_brain/c09/CLAUDE-TO-BRAIN.md`:

```text
CERERE SYSTEM
Construcție: C09
Fișier comun cerut: ...
Motiv: ...
Impact: ...
Propunere: ...
```

Apoi execuția C09 se oprește până la decizie SYSTEM.

## Stare curentă C09

BRAIN-019-REV2 a fost executat cu PASS.
Editor-Studiu C09 este reparat.
Rămân mandate separate pentru:

- HTML-Video C09
- Editor-Video C09
- FILM C09
