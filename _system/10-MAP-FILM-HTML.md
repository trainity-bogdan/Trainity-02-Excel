# 10 · MAPARE FILM → HTML (frazele de impact)

**Scop:** sursă de adevăr pentru ce text din FILM (.docx) se sincronizează în cele 4 machete HTML. La comanda „update html / sincronizează FILM", motorul aplică maparea de mai jos mecanic, în toate cele 4 fișiere relevante.

**Principiu:** FILM = MASTER. HTML urmează FILM. Dacă HTML are o formulare mai bună decât FILM, se BACK-PORTEAZĂ în FILM întâi (FILM rămâne master), apoi se sincronizează.

---

## Cele 4 machete

| Machetă | Conține sloturi de impact |
|---|---|
| HTML-Studiu | cover-subtitle, cover-miza, mantra-band-main, payoff-motto |
| HTML-Editor-Studiu | (idem Studiu) |
| HTML-Video | hero-hook, final-motto, exec-closing-motto, exec-emotion×6, exec-phrase×6 |
| HTML-Editor-Video | (idem Video) |

---

## Maparea câmp FILM → slot HTML

Rolul slotului e dat de eticheta proprie din HTML (`mantra-band-sub` = „MANTRA · TRAINITY", `exec-closing-prelabel` = „Motto:").

| Câmp FILM (IDENTITATE) | HTML-Studiu | HTML-Video | Observații |
|---|---|---|---|
| **INTRIGA (HOOK)** | `cover-subtitle` (text integral) | `hero-hook` (split pe cele 2 propoziții: prop.1 + `<span class="hero-hook-twist">`prop.2`</span>`) | — |
| **MIZA** | `cover-miza` | — | doar Studiu |
| **MANTRA · TRAINITY** | `mantra-band-main` (cuvânt-cheie în `<mark>`) | — | doar Studiu |
| **WOW (PAYOFF FINAL)** | linie-climax `[data-wow="1"]` (`.payoff-line.accent`) chiar înainte de `payoff-motto` | frag `[data-wow="1"]` (`.accent`) chiar înainte de `final-motto` (renumerotează motto + bump `data-frag-total`) | vârful fluxului emoţional, înainte de semnătură |
| **MOTTO (SEMNĂTURĂ)** | `payoff-motto` | `final-motto` (ultimul frag) + `exec-closing-motto` (ultima parte în `<span class="exec-closing-motto-yellow">`) | apare 3 locuri |
| **CONTRACT (DESTINAȚIE)** *(element nou)* | bloc `<section class="exec-hero" data-contract="1">` în cusătura SCENA REALĂ → primul pas | (Studiu only; în Video rolul e jucat de `hero-sub`) | promisiune privită înainte; copy DRAFT, de formalizat în FILM după ce ARHITECT fixează wording-ul |

| Câmp FILM (SLIDES EXECUTIVE) | HTML-Video | 
|---|---|
| **STARE (exec-emotion)** ×6 | `exec-emotion` din slide-urile 1-6 (1:1 pe etapă) |
| **FRAZĂ DE IMPACT (exec-phrase)** ×6 | `exec-phrase` din slide-urile 1-6 (1:1 pe etapă) |

> NB: câmpul `hook:` din array-ul JS de etape NU e frază de impact — e hook-ul de scenă al etapei. NU se sincronizează din SLIDES EXECUTIVE.

---

## WOW (rezolvat — opţiunea B)

WOW are acum slot dedicat: linie-climax verbatim chiar înainte de motto, ca vârf al fluxului emoţional. Ancorat pe `[data-wow="1"]`, reutilizează stilul `.accent` (galben, bold) — fără CSS nou. În Video e frag propriu (renumerotează motto-ul + creşte `data-frag-total` cu 1).

## CONTRACT (element nou — copy DRAFT)

Cusătura SCENA REALĂ → primul pas primeşte un „contract de destinaţie": o promisiune privită înainte de călătorie (timp prezent-viitor). Bloc `exec-hero` ancorat `[data-contract="1"]`, Studiu only. Copy-ul curent e DRAFT, scris de motor; se formalizează ca element SPEC în FILM după ce ARHITECT fixează wording-ul, apoi se masterizează ca restul.

---

## Procedură „update html" (mecanic)

1. Citește valorile de identitate + SLIDES EXECUTIVE din FILM (.docx).
2. Pentru fiecare câmp, suprascrie slotul HTML corespunzător în toate cele 4 machete (Studiu + Editor-Studiu pentru sloturile Studiu; Video + Editor-Video pentru sloturile Video).
3. Split-uri: INTRIGA → hero-hook pe 2 propoziţii; MOTTO → final-motto / exec-closing-motto (ultima parte highlight).
4. Rulează `audit_sync.py` (ZERO DRIFT) + verifică vizual sloturile.
5. Commit + push.

---

## Status sincronizare per construcţie

| Cod | INTRIGA | MIZA | MANTRA | MOTTO | exec slides | WOW | CONTRACT |
|---|---|---|---|---|---|---|---|
| C01 | parţial (hero ✓, cover-subtitle ≠) | ≠ (HTML propriu) | ≠ | ≠ | ✓ | ✓ slot nou | ✓ draft |
| C02 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ slot nou | ✓ draft |

C01: identitatea HTML (MIZA/MANTRA/MOTTO) încă diferă de FILM (drift vechi, HTML mai şlefuit). Direcţie de reconciliere pending ARHITECT (sync HTML←FILM vs back-port HTML→FILM). WOW + CONTRACT însă au fost adăugate la ambele.
