# _brain · sistem multi-chat Trainity

Acest folder separă comunicarea BRAIN ↔ CLAUDE pe construcții și pe SYSTEM.

## Regula principală

- Chat Andrei C09 lucrează doar cu `_brain/c09/*`.
- Chat Claude C09 execută doar în `c09/**` și `_brain/c09/**`.
- Chat Andrei C10 lucrează doar cu `_brain/c10/*`.
- Chat Claude C10 execută doar în `c10/**` și `_brain/c10/**`.
- Chat Andrei SYSTEM lucrează doar cu `_brain/system/*` și fișiere comune.

## Comanda unică

În fiecare chat, comanda este doar:

```text
sync
```

Chat-ul își cunoaște rolul din `CHAT-CONTEXT.md`.

## Fișiere comune

Fișierele comune se modifică doar din Chat Andrei SYSTEM:

- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `index.html`
- `_system/**`
- `gate_v20.py`
- `audit_sync.py`
- `COMENZI.yaml`
- orice regulă / generator / document global

## Regulă de siguranță

Dacă o construcție are nevoie de fișier comun, Claude NU îl modifică. Scrie doar `CERERE SYSTEM` în raportul construcției.