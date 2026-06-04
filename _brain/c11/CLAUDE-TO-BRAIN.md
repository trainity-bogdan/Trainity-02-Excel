# CLAUDE → BRAIN · C11 COMPARAȚII / RANK

## STATUS
SPEC_FROZEN_ACK

## RAPORT SYNC (2026-06-04) · MANDAT C11-02

Sync executat în chat dedicat C11.

Pași:
1. `git fetch origin main` + rebase local pe `origin/main` (origin avansase cu C09 + freeze C11 + commit-uri system).
2. Citit `_brain/c11/CHAT-CONTEXT.md` + `_brain/c11/BRAIN-TO-CLAUDE.md` (MANDAT C11-02).
3. NU am generat artefacte. NU am atins fișiere sistem sau alte construcții.

---

## CONFIRMARE PRELUARE SPEC_FROZEN

Am preluat SPEC C11 ÎNGHEȚAT, integral. Confirm cele 5 decizii BRAIN:
1. SLUG `comparatii` — preluat.
2. 6 fenomene — preluat (clasament, diferență reală vs zgomot, contribuție/pondere, concentrare Pareto/ABC, comparabilitate, reper relativ).
3. Pareto/ABC rămâne în C11 ca fenomen de ierarhie și concentrare — preluat.
4. C12 primește doar cauza / „de ce" — delimitare acceptată.
5. MOTTO `Nu citi lista. Citește ierarhia.` — preluat.

Cele 9 elemente narrative + DELIMITĂRILE HARD + REGULA VOCABULAR/ADRESARE sunt înregistrate ca referință pentru faza de generare. Nu am modificat SPEC-ul înghețat.

---

## RISCURI DE VOCABULAR (de gestionat la generare)

Regula de adresare directă cu `tu` + lista de cuvinte interzise (`cursant`, `cursantul`, `participant`, `participantul`, `elev`, `student`) introduce un punct de atenție la `genereaza CNN`:

1. **Matrița `c01/`** (sursa de copy) e construcție T1 mai veche; poate conține formulări la persoana a III-a sau termenul `cursant` în HTML/FILM. La generarea C11 din copy, trebuie scanat și reformulat tot textul de experiență în adresare directă (`vezi`, `compari`, `confirmi`, `identifici`, `citești ierarhia`) ÎNAINTE de gate_v20. Notez asta ca pas obligatoriu de post-copy, nu las moștenirea de voce a lui C01.
2. **FILM:** `noi` permis punctual doar pentru ghidarea demonstrației, nu ca ton general. Voi păstra tonul business/operațional, nu școlar.
3. **Coerență cu SPEC-ul deja înghețat:** MIZA și PROBLEMELE din SPEC sunt deja la adresarea `tu` — voi propaga același registru în toate textele generate, fără să reintroduc persoana a III-a.

Nu e un blocaj, e o checklist de aplicat la mandatul de generare.

---

## DELIMITĂRI HARD (înregistrate pentru generare)
- C11 NU redefinește măsura (vine din C10).
- C11 NU explică „de ce" apare ierarhia (cauza = C12).
- C11 NU construiește dashboard (raportarea = T4).
- C11 compară actori agregați, NU etichetează rânduri individuale (vs C06).
- R-V02.14 sumă conservată (input C11 = output C10); R-V02.15 zero cifre business în HTML/FILM.

---

## CERERI SYSTEM
Nicio cerere SYSTEM deschisă.

Aștept mandat explicit separat de generare (`genereaza CNN`) ca să creez `c11/` din copy `c01/`. Nu generez artefacte până atunci.
