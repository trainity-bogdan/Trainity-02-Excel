# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-019-REV2

## CORECȚIE DIRECȚIE
Anulează interpretarea BRAIN-019-REV1 ca mandat de cleanup Creative dacă ai primit deja direct de la BRAIN instrucțiuni despre:
- eliminarea fișierului Creativ / prompturi.
- hero C09.
- prompt Banana.

BRAIN spune acum clar:
- acele lucruri ți-au fost date deja separat.
- continuarea trebuie să plece din auditul Editor-Studiu C09, exact mandatul primit înainte de discuția despre poză / hero / Banana.

## CONTEXT AUDIT VALID
Ultimul raport relevant este BRAIN-018-REV1, audit Editor-Studiu C09.

Verdict audit:
- `HTML-Editor-Studiu-Excel-09-Relatii.html` = PASS CU FIXURI.
- 0 BLOCKER.
- companion sincronizat 1:1 cu baza.
- export curat.
- zone LOCKED funcționale.
- fără contaminare C10/C11/C12/T4/T5.
- fără clonă C08.

Probleme rămase din audit:
1. MINOR-1: MANTRA, MOTTO, hero-question-text sunt sigure, dar nu au badge LOCKED vizibil.
2. MINOR-2: formula Join/Union în corp este non-canonică față de forma locked.
3. MINOR-3: over-locking pe PAS 01 și PAS 09.
4. MINOR-4: panoul companion este înalt pe mobil.
5. WARN: lock-by-phrase este fragil, ar trebui înlocuit cu lock-by-attribute.
6. MAJOR UX hero: rezolvat sau în curs de rezolvare prin instrucțiunile primite direct de la BRAIN, nu prin fișierul Creativ.

## MANDAT ACTUAL
Aplică fixurile de editor rezultate din auditul BRAIN-018, fără să atingi problema hero / Banana / Creative.

Scop:
- întărește companionul Editor-Studiu C09.
- treci de la lock-by-phrase fragil la lock-by-attribute, unde este realist.
- marchează vizual LOCKED sloturile care erau sigure dar fără badge.
- aliniază formula Join/Union la forma canonică.
- redu over-locking-ul pe PAS 01 și PAS 09.
- fă panoul companion mai ergonomic, ideal colapsabil pe mobil.

## FIXURI CERUTE

### FIX 1, LOCK vizual complet
Asigură că următoarele primesc badge vizibil LOCKED și nu sunt editabile:
- hero-question-text.
- mantra-band-main.
- payoff-motto.
- toate sloturile deja locked.

### FIX 2, Join vs Union canonic
În corp, aliniază formula la forma canonică:
"Join leagă tabele diferite. Union adună tabele de același fel."

Actualizează și mecanismul de lock ca să prindă forma canonică.

### FIX 3, lock granular
Nu bloca integral PAS 01 și PAS 09 dacă doar o propoziție din pas este canonică.

Soluție preferată:
- marchează frazele canonice cu `data-locked="1"` sau span dedicat `.locked-slot`.
- editorul blochează prin atribut / clasă stabilă, nu doar prin substring.
- păstrează restul microcopy-ului editabil unde este sigur.

### FIX 4, companion panel UX
Fă panoul companion mai ergonomic:
- colapsabil sau compact pe mobil.
- să nu împingă inutil conținutul real foarte jos.
- să păstreze lista de LOCKED / editabile / gărzi.

### FIX 5, robusteză editor
Actualizează JS-ul editorului astfel încât:
- lock-by-attribute să fie prioritar.
- lock-by-phrase să rămână doar fallback, nu mecanism principal.
- exportul curat elimină toate atributele și clasele de editor fără să rupă HTML-ul final.

## FIȘIERE PERMISE
Ai voie să modifici doar:
- `c09/HTML-Studiu-Excel-09-Relatii.html`, doar dacă este necesar pentru markeri `data-locked` / span locked și formula Join/Union canonică.
- `c09/HTML-Editor-Studiu-Excel-09-Relatii.html`.
- `CLAUDE-TO-BRAIN.md`.
- `STARE-CURENTA.md`, doar dacă fluxul standard cere actualizare.

Nu modifica:
- Video.
- Editor-Video.
- FILM.
- assets.
- index.html.
- Date_MASTER-C09.xlsx.
- fișiere Creative / prompturi.
- gate / audit / governance.

## SINCRONIZARE OBLIGATORIE
Dacă atingi baza HTML-Studiu, companionul Editor-Studiu trebuie sincronizat în același ciclu.

După modificări:
- Editor-Studiu strip-uit de stratul editor trebuie să fie identic cu HTML-Studiu, exceptând doar whitespace irelevant.
- nu livra baza fără companion sincronizat.

## VALIDĂRI CERUTE
Rulează:
1. `gate_v20 09 c09 c01`.
2. `tier_guard_t3` pentru C09.
3. `audit_sync`.
4. comparație Editor curățat vs HTML-Studiu.
5. verificare 18 pași, 8 verificări, 5 fenomene, 2 prompturi.
6. verificare că toate zonele LOCKED au badge și nu sunt editabile.
7. verificare că PAS 01 și PAS 09 nu mai sunt blocate integral inutil.
8. verificare export curat.
9. verificare că nu ai modificat index.html, Video, FILM, assets, Creative.
10. git diff sumar.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet:
1. Status.
2. Rezumat executiv.
3. Fișiere citite.
4. Fișiere modificate.
5. Fix LOCK vizual complet.
6. Fix Join vs Union canonic.
7. Fix lock granular.
8. Fix panel UX.
9. Fix robusteză editor.
10. Sincronizare bază / companion.
11. Validări rulate.
12. PASS / WARNING / FAIL.
13. Ce nu ai modificat.
14. Ce rămâne pentru pasul următor.
15. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-019-REV2.
Refă direcția către fixurile rezultate din auditul Editor-Studiu C09.
