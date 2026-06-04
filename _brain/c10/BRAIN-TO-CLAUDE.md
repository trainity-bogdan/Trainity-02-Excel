# BRAIN → CLAUDE · C10 MĂSURI

## STATUS
HERO_NAME_FIX_REQUIRED

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C10.

La comanda `sync`, citește:
- `_brain/c10/CHAT-CONTEXT.md`
- `_brain/c10/BRAIN-TO-CLAUDE.md`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

---

# MANDAT BRAIN · FIX HERO NAME C10

C10 a fost aprobat structural, dar după fixul de eliminare a H1 duplicat a apărut o problemă vizuală nouă în pagina publicată.

## PROBLEMĂ

În header-ul principal / banda neagră de sus apare doar:

**MĂSURI**

Dar numele complet al obiectului construcției, stabilit și aprobat de BRAIN, este:

**MĂSURA POTRIVITĂ**

Această formulare trebuie să fie hero-ul vizual principal al construcției C10.

## CORECȚIE CERUTĂ

În `c10/HTML-Studiu-Excel-10-Masuri.html`:

1. în hero/header-ul principal, înlocuiește titlul mare `MĂSURI` cu `MĂSURA POTRIVITĂ`;
2. păstrează harta treptei cu `RELAȚII · MĂSURI · COMPARAȚII · INTERPRETARE`;
3. păstrează întrebarea de sub hero: `Cât? Și cum definesc o măsură care răspunde corect de fiecare dată?`;
4. nu reintroduce H1 duplicat;
5. aplică aceeași identitate în `HTML-Editor-Studiu`, dacă este companion 1:1;
6. verifică `HTML-Video`: acolo hero-title trebuie să rămână `MĂSURA POTRIVITĂ`;
7. nu modifica Date_MASTER;
8. nu modifica SPEC-ul.

## POST-CHECK

După corecție:
- rulează gate_v20 pentru C10;
- rulează audit_sync;
- rulează tier_guard_t3;
- confirmă vizual că hero-ul principal este `MĂSURA POTRIVITĂ` și că titlul-întrebare nu este dublat;
- actualizează `CLAUDE-TO-BRAIN.md`.

## STATUS AȘTEPTAT ÎN CLAUDE-TO-BRAIN

REFINED_AFTER_HERO_NAME_FIX · PASS
