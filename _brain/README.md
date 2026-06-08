# _brain · sistem multi-chat Trainity

Acest folder separă comunicarea BRAIN ↔ CLAUDE pe construcții (C09-C20) și pe SYSTEM. Fiecare construcție are un chat BRAIN (Andrei) și un chat CLAUDE dedicate, care comunică prin fișiere, nu prin copy-paste.

## Acoperire protocol

Protocolul acoperă explicit **C09-C20**. Fiecare construcție `cXX` are folderul `_brain/cXX/` cu triada operațională proprie:

- `CHAT-CONTEXT.md` — rolul chat-ului: ce citește, ce scrie, ce nu are voie să atingă, contextul conceptual al construcției.
- `BRAIN-TO-CLAUDE.md` — mandatul curent scris de BRAIN (Andrei) pentru CLAUDE.
- `CLAUDE-TO-BRAIN.md` — raportul scris de CLAUDE după execuție.

Procedura oficială completă: `_system/15-PROTOCOL-SYNC-CONSTRUCTII.md`.

## Cele două comenzi

**`Prompt` (în chat BRAIN cXX):** BRAIN NU livrează textul în conversație pentru copy-paste. BRAIN scrie direct mandatul în `_brain/cXX/BRAIN-TO-CLAUDE.md` și confirmă doar fișierul + commit-ul. Promptul se afișează în chat doar dacă ARHITECT cere explicit.

**`sync` (în chat CLAUDE cXX):** CLAUDE
1. lucrează exclusiv pe `main`, fără branch-uri;
2. citește `_brain/cXX/CHAT-CONTEXT.md`;
3. citește mandatul din `_brain/cXX/BRAIN-TO-CLAUDE.md`;
4. execută doar ce permite mandatul;
5. scrie raportul în `_brain/cXX/CLAUDE-TO-BRAIN.md`;
6. rulează validările cerute;
7. commit descriptiv pe `main` + push.

**Copy-paste între chaturi NU mai este metoda principală.** Comunicarea trăiește în fișierele triadei; chat-urile se sincronizează prin `git` + `sync`.

## Scope per construcție

- Chat BRAIN cXX scrie doar în `_brain/cXX/BRAIN-TO-CLAUDE.md`.
- Chat CLAUDE cXX scrie doar în `_brain/cXX/CLAUDE-TO-BRAIN.md` și, dacă mandatul permite explicit implementare, în `cXX/**`.
- Un chat de construcție NU atinge alte construcții (`cYY/**`, `_brain/cYY/**`) și niciun fișier sistem.

## Fișiere comune (doar din Chat Andrei SYSTEM)

Fișierele comune se modifică EXCLUSIV din Chat Andrei SYSTEM:

- `CLAUDE.md`, `README.md`, `STARE-CURENTA.md`, `index.html`
- `_system/**`, `governance/**`
- `gate_v20.py`, `audit_sync.py`, `COMENZI.yaml`, `constructii.xlsx`
- orice regulă / generator / document global

## Regulă de siguranță (CERERE SYSTEM)

Dacă o construcție are nevoie de un fișier comun, CLAUDE NU îl modifică. Scrie `CERERE SYSTEM` în `_brain/cXX/CLAUDE-TO-BRAIN.md` (construcție, fișier cerut, motiv, impact, propunere) și oprește execuția până la o decizie din Chat Andrei SYSTEM.

## Stare triadă C09-C20

- **C09-C13:** triadă completă, cu mandate și rapoarte reale (lucru în curs / finalizat).
- **C14-C20:** triadă pregătită; `BRAIN-TO-CLAUDE.md` în `READY_FOR_BRAIN_MANDATE`, `CLAUDE-TO-BRAIN.md` în `EMPTY`, în așteptarea primului mandat BRAIN.
