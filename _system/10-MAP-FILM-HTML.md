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
| **WOW (PAYOFF FINAL)** | — | — | **NU are slot single.** Zona `payoff-section` (Studiu) / `final-block` (Video) e o secvență narativă proprie (dim → accent → regular). WOW e seminţa conceptuală, nu o linie verbatim. Vezi nota WOW. |
| **MOTTO (SEMNĂTURĂ)** | `payoff-motto` | `final-motto` (data-frag 7) + `exec-closing-motto` (data-frag 2, ultima parte în `<span class="exec-closing-motto-yellow">`) | apare 3 locuri |

| Câmp FILM (SLIDES EXECUTIVE) | HTML-Video | 
|---|---|
| **STARE (exec-emotion)** ×6 | `exec-emotion` din slide-urile 1-6 (1:1 pe etapă) |
| **FRAZĂ DE IMPACT (exec-phrase)** ×6 | `exec-phrase` din slide-urile 1-6 (1:1 pe etapă) |

> NB: câmpul `hook:` din array-ul JS de etape NU e frază de impact — e hook-ul de scenă al etapei. NU se sincronizează din SLIDES EXECUTIVE.

---

## Nota WOW (gol de design)

FILM-ul are WOW (PAYOFF FINAL) ca punchline unic, dar HTML realizează payoff-ul ca secvență cinematică pe mai multe rânduri (`dim` × n → `accent` → `regular` → motto). Nu există slot verbatim pentru WOW.

Opțiuni de rezolvare (decizie ARHITECT, neîngheţată încă):
- **A.** Se lasă payoff-ul bespoke (WOW = seminţă conceptuală, expandată cinematic). Status quo.
- **B.** Se introduce o linie-climax verbatim cu WOW, înainte de motto, ca vârf al fluxului emoţional.

---

## Procedură „update html" (mecanic)

1. Citește valorile de identitate + SLIDES EXECUTIVE din FILM (.docx).
2. Pentru fiecare câmp, suprascrie slotul HTML corespunzător în toate cele 4 machete (Studiu + Editor-Studiu pentru sloturile Studiu; Video + Editor-Video pentru sloturile Video).
3. Split-uri: INTRIGA → hero-hook pe 2 propoziţii; MOTTO → final-motto / exec-closing-motto (ultima parte highlight).
4. Rulează `audit_sync.py` (ZERO DRIFT) + verifică vizual sloturile.
5. Commit + push.

---

## Status sincronizare per construcţie

| Cod | INTRIGA | MIZA | MANTRA | MOTTO | exec slides | WOW |
|---|---|---|---|---|---|---|
| C01 | parţial (hero ✓, cover-subtitle ≠) | ≠ (HTML propriu) | ≠ | ≠ | ✓ | gol |
| C02 | ✓ | ✓ | ✓ | ✓ | ✓ | gol (opţiune A/B pending) |

C01: identitatea HTML diferă de FILM (drift vechi, HTML mai şlefuit). Direcţie de reconciliere pending ARHITECT (sync HTML←FILM vs back-port HTML→FILM).
