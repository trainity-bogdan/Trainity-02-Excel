# 15 · PROTOCOL SYNC CONSTRUCȚII (BRAIN ↔ CLAUDE)

> **STATUT: PROCEDURĂ OFICIALĂ DE SISTEM.** Codifică modul de lucru multi-chat pentru orice construcție nouă C13-C20.
> Sursă a convenției live: `_brain/README.md` + `_brain/cXX/CHAT-CONTEXT.md`. Acest document e norma; folderele `_brain/cXX/` sunt implementarea.
> Domeniu: procesul de comunicare și execuție. NU atinge nomenclatura (LOCKED V70), Bible, cNN, HTML, Date_MASTER.

---

## 0. DE CE
O construcție nouă (C13-C20) se lucrează în DOUĂ chat-uri separate, una pentru gândire (BRAIN), una pentru execuție (CLAUDE), care comunică prin două fișiere versionate în git. Avantaj: BRAIN decide CE, CLAUDE execută CUM, fără ca cele două roluri să se amestece, și fără ca un chat de construcție să atingă din greșeală sistemul sau altă construcție.

---

## 1. STRUCTURA STANDARD

Pentru fiecare construcție CXX (XX = 13..20) există:

**Două chat-uri:**
- **Chat BRAIN CXX** (Andrei CXX) — rolul de arhitect al construcției. Decide, formulează mandate.
- **Chat CLAUDE CXX** — rolul de motor. Execută mandatul, raportează.

**Un folder dedicat `_brain/cXX/` cu trei fișiere:**

| Fișier | Cine scrie | Rol |
|---|---|---|
| `_brain/cXX/BRAIN-TO-CLAUDE.md` | BRAIN | mandatul curent (ce execută CLAUDE) |
| `_brain/cXX/CLAUDE-TO-BRAIN.md` | CLAUDE | raportul curent (ce a făcut + blocaje + CERERE SYSTEM) |
| `_brain/cXX/CHAT-CONTEXT.md` | SYSTEM (la creare) | identitatea chatului + regulile de scope (fix, nu se schimbă în lucru) |

**Folderul de livrabile `cXX/`** (cele 7 artefacte canonice) apare DOAR când CLAUDE generează construcția; până atunci munca trăiește în `_brain/cXX/`.

---

## 2. PROMPT STANDARD BRAIN

Se lipește la deschiderea unui chat BRAIN nou pentru CXX:

```text
Acest chat este BRAIN (Andrei) pentru construcția CXX <NUME> din Trainity-02-Excel.

Rolul tău:
- ești arhitectul construcției CXX
- decizi CE se face, nu CUM
- scrii mandate exclusiv în _brain/cXX/BRAIN-TO-CLAUDE.md
- citești rapoarte din _brain/cXX/CLAUDE-TO-BRAIN.md
- NU atingi fișiere sistem, alte construcții, nomenclatura, Bible
- dacă ai nevoie de un fișier comun, formulezi CERERE SYSTEM pentru Chat Andrei SYSTEM

La comanda "sync" citești DOAR:
- _brain/cXX/CHAT-CONTEXT.md
- _brain/cXX/BRAIN-TO-CLAUDE.md
- _brain/cXX/CLAUDE-TO-BRAIN.md

Respecti nomenclatura LOCKED V70 + doc 13/14 (autoritate conceptuală T4/T5).
Nu redeschizi decizii LOCKED.
```

---

## 3. PROMPT STANDARD CLAUDE

Se lipește la deschiderea unui chat CLAUDE nou pentru CXX:

```text
Acest chat este CLAUDE (motor) pentru construcția CXX <NUME> din Trainity-02-Excel.

Rolul tău:
- execuți mandatul curent, nu inventezi
- lucrezi exclusiv pe main, fără branch-uri
- execuți DOAR în cXX/** și _brain/cXX/**
- scrii raportul în _brain/cXX/CLAUDE-TO-BRAIN.md
- commit descriptiv direct pe main + push
- NU atingi fișiere sistem, alte construcții, HTML fără mandat
- orice nevoie de fișier comun = CERERE SYSTEM în raport, apoi te oprești

La comanda "sync":
1. git pull main
2. citești _brain/cXX/CHAT-CONTEXT.md + _brain/cXX/BRAIN-TO-CLAUDE.md
3. identifici mandatul curent
4. execuți strict fișierele permise din mandat
5. rulezi validările cerute (gate_v20, pre_generation_check, audit_sync)
6. scrii raportul în _brain/cXX/CLAUDE-TO-BRAIN.md
7. commit + push pe main
8. dacă nu poți executa, raportezi blocajul concret, nu te oprești după git status

Respecti nomenclatura LOCKED V70 + doc 13/14 + Bible §T4/§T5.
Regula B1: nu generezi construcția fără SPEC înghețat.
```

---

## 4. REGULA SYNC

**Comanda unică în orice chat de construcție = `sync`.**

La `sync`, fiecare chat citește DOAR fișierele propriei construcții (`_brain/cXX/*`), niciodată ale altei construcții și niciodată fișiere sistem. Chatul își cunoaște rolul (BRAIN sau CLAUDE) și construcția din `CHAT-CONTEXT.md`.

`sync` NU este doar git pull. Pentru CLAUDE înseamnă obligatoriu: pull -> citește mandat -> execută mandat -> validează -> raportează în CLAUDE-TO-BRAIN.md -> commit + push. Niciodată oprire după „working tree curat".

---

## 5. REGULI DE INTERDICȚIE

Într-un chat de construcție CXX (BRAIN sau CLAUDE):
1. **NU se ating fișiere sistem** din chat de construcție: `CLAUDE.md`, `README.md`, `STARE-CURENTA.md`, `index.html`, `_system/**`, `constructii.xlsx`, `gate_v20.py`, `audit_sync.py`, `COMENZI.yaml`, orice regulă/generator/document global.
2. **NU se ating alte construcții:** chat CXX execută strict în `cXX/**` și `_brain/cXX/**`.
3. **NU se modifică HTML fără mandat** explicit în `BRAIN-TO-CLAUDE.md`.
4. **NU se redeschide nomenclatura** (LOCKED V70) și nici deciziile LOCKED din Bible / doc 11-14.
5. **Cererile de sistem devin `CERERE SYSTEM`** (vezi formatul de mai jos), scrise în raport, nu executate.

### Format CERERE SYSTEM
Scris de CLAUDE în `_brain/cXX/CLAUDE-TO-BRAIN.md`, apoi execuția CXX se oprește până la decizie din Chat Andrei SYSTEM:
```text
CERERE SYSTEM
Construcție: CXX
Fișier comun cerut: <cale>
Motiv: <de ce e necesar>
Impact: <ce se schimbă în sistem>
Propunere: <modificarea exactă propusă>
```

---

## 6. PROCEDURA PENTRU CONSTRUCȚIE NOUĂ

Pasul de deschidere a unei construcții CXX (din Chat Andrei SYSTEM sau manual):
1. **Creează folder** `_brain/cXX/`.
2. **Creează cele trei fișiere** din template (secțiunea 7): `CHAT-CONTEXT.md`, `BRAIN-TO-CLAUDE.md` (gol/seed), `CLAUDE-TO-BRAIN.md` (gol).
3. **Pornește Chat BRAIN CXX** cu promptul standard (secțiunea 2).
4. **Pornește Chat CLAUDE CXX** cu promptul standard (secțiunea 3).
5. **Se lucrează exclusiv prin `sync`:** BRAIN scrie mandat -> CLAUDE face `sync` -> execută -> raportează -> commit. Repetă.
6. **Ordinea conceptuală obligatorie** (regula B1): SEED conceptual -> SPEC 11-slot înghețat -> blueprint -> generare cele 7 artefacte. Nu se generează fără SPEC înghețat.
7. **Folosirea fișierelor comune** trece prin `CERERE SYSTEM`, nu prin chatul de construcție.

---

## 7. TEMPLATE GENERIC CXX

### `_brain/cXX/CHAT-CONTEXT.md`
```text
# CHAT-CONTEXT · ANDREI CXX / CLAUDE CXX

Acest folder este dedicat exclusiv construcției CXX <NUME>.

## Comanda unică
sync

## Andrei CXX
La sync citește doar:
- _brain/cXX/BRAIN-TO-CLAUDE.md
- _brain/cXX/CLAUDE-TO-BRAIN.md
- _brain/cXX/CHAT-CONTEXT.md
Scrie mandate doar în _brain/cXX/BRAIN-TO-CLAUDE.md.
NU modifică fișiere sistem. Nevoie de sistem = CERERE SYSTEM.

## Claude CXX
La sync:
1. lucrează exclusiv pe main, fără branch-uri
2. citește mandatul din _brain/cXX/BRAIN-TO-CLAUDE.md
3. execută doar în cXX/** și _brain/cXX/**
4. scrie raportul în _brain/cXX/CLAUDE-TO-BRAIN.md
5. rulează validările cerute
6. commit descriptiv pe main + push

## Fișiere interzise pentru CXX
- toate celelalte cNN/**
- CLAUDE.md, README.md, STARE-CURENTA.md, index.html
- _system/**, constructii.xlsx, gate_v20.py, audit_sync.py, COMENZI.yaml
- orice fișier global / sistem

## Nevoie de fișier comun
Claude NU îl modifică. Scrie CERERE SYSTEM în CLAUDE-TO-BRAIN.md și oprește execuția până la decizie.

## Stare curentă CXX
CXX este construcția <NUME>. Nu executa nimic fără mandat în BRAIN-TO-CLAUDE.md.
```

### `_brain/cXX/BRAIN-TO-CLAUDE.md` (seed)
```text
# BRAIN → CLAUDE · CXX <NUME>

## STATUS
MANDAT_CXX_<ETAPA>

## CONTEXT
<cadru din doc 13/14 + nomenclatura LOCKED a CXX>

## MANDAT
Claude, lucrează pe main. Execută doar mai jos. Nu modifica altceva.
<pași concreți + fișiere permise + fișiere interzise>

## VERIFICĂRI
<lista de comenzi: gate_v20, pre_generation_check, audit_sync>

## RAPORT
Scrie raportul în _brain/cXX/CLAUDE-TO-BRAIN.md.
Status așteptat: MANDAT_CXX_<ETAPA>_DONE
```

### `_brain/cXX/CLAUDE-TO-BRAIN.md` (seed)
```text
# CLAUDE → BRAIN · CXX <NUME>

## STATUS
(gol până la primul sync)

## RAPORT
(fișiere modificate · ce s-a făcut · PASS/FAIL validări · CERERE SYSTEM dacă e cazul)
```

---

## RELAȚIA CU `sync`-ul global din CLAUDE.md
`sync`-ul global (rădăcina `BRAIN-TO-CLAUDE.md` / `CLAUDE-TO-BRAIN.md`) rămâne pentru mandate de SISTEM (Chat Andrei SYSTEM). Acest protocol scopează același mecanism PER CONSTRUCȚIE sub `_brain/cXX/`. Regula de bază: chat de construcție = fișiere de construcție; chat de sistem = fișiere comune. Niciodată invers.

---

Versiune document: V73 · procedură oficială multi-chat C13-C20.
