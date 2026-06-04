# CLAUDE → BRAIN · C09 RELAȚII

## STATUS FINAL
CERERE_SYSTEM_INDEX_C09_READY

## MANDAT EXECUTAT
C09-M024-CERERE-SYSTEM-INDEX — formulare CERERE SYSTEM pentru `index.html`. Nu am modificat `index.html`, `STARE-CURENTA.md` sau orice fișier sistem. Doar am scris cererea aici.

## OBSERVAȚIE LA PREMISA MANDATULUI (corecție de acuratețe)
Premisa mandatului spune că „C09 nu apare în `index.html` preview live". Verificat empiric (read-only): **C09 APARE deja** în `index.html`, în zona „T3 ANALIZĂ", dar cardul este **STALE / parțial**:
- linkează DOAR `c09/HTML-Studiu-Excel-09-Relatii.html?v=1`;
- textul cardului spune „… deschide treapta. Video, Editor și film urmează." (scris când exista doar Studiu).

Deci cererea corectă este de **ACTUALIZARE a cardului C09 existent** (nu de adăugare de la zero), ca să reflecte starea finală: 4 HTML + FILM + 6 imagini, toate prezente.

---

## CERERE SYSTEM
```
CERERE SYSTEM
Construcție: C09 RELAȚII
Status: FINAL după MONSTER AUDIT
Status tehnic: READY_FINAL_C09_MONSTER_PASS_AFTER_FIX
Fișier comun cerut: index.html
```

### MOTIV
C09 este finală în folderul `c09/` (GATE PASS, ZERO DRIFT, 6/6 imagini, FILM valid), dar cardul ei din `index.html` este stale: oferă doar linkul către Studiu și anunță că „Video, Editor și film urmează", ceea ce nu mai e adevărat. Preview-ul live nu reflectă construcția completă.

### IMPACT
- Vizitatorul preview-ului live vede C09 ca incompletă (doar Studiu), deși toate cele 4 HTML + FILM + imaginile sunt livrate.
- Fără actualizare, C09 pare „în lucru" în loc de „finală T3".
- Risc zero pe conținutul C09 (cererea atinge doar `index.html`, fișier comun, în afara scope-ului meu).

### PROPUNERE CONCRETĂ (pentru Chat SYSTEM / ARHITECT)
Actualizați cardul C09 din secțiunea „T3 ANALIZĂ" a `index.html` astfel:
1. Linkuri către toate cele 4 livrabile HTML:
   - `c09/HTML-Studiu-Excel-09-Relatii.html`
   - `c09/HTML-Editor-Studiu-Excel-09-Relatii.html`
   - `c09/HTML-Video-Excel-09-Relatii.html`
   - `c09/HTML-Editor-Video-Excel-09-Relatii.html`
2. Bump cache-bust pe linkul Studiu: `?v=1` → `?v=2` (Studiu s-a schimbat după index: hero real + markeri `data-locked`).
3. Actualizați textul cardului (scoateți „Video, Editor și film urmează"):
   - Cod: C09
   - Titlu: Cum legăm tabelele prin relații corecte
   - Descriere: „Ai toate datele. Și niciun răspuns. T3 ANALIZĂ · construcția 9 · relații."
4. Poziționare: rămâne în „T3 ANALIZĂ", înainte de C10/C11/C12, ca prima construcție finală T3 (deja e acolo).

### MENȚIUNI
- Creativ C09 este **absent corect** (Creativ abandonat V68); NU trebuie listat în card.
- C10 are drift propriu (e parțial în repo, în afara scope-ului C09); statusul C09 NU trebuie amestecat cu C10. C09 = ZERO DRIFT pe rândul ei.
- FILM-ul C09 nu se linkează din index (e artefact de filmare .docx, nu pagină web preview) — conform patternului celorlalte construcții.

## STATUS FINAL
CERERE_SYSTEM_INDEX_C09_READY
