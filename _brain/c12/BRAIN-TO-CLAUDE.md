# BRAIN → CLAUDE · C12 INTERPRETARE

## STATUS
MANDAT_GENERARE_C12

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C12.

La comanda `sync`, citește:
- `_brain/c12/CHAT-CONTEXT.md`
- `_brain/c12/BRAIN-TO-CLAUDE.md`

Execută pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C12
C12 este construcția INTERPRETARE.

Conform hărții oficiale T3:
- C09 = RELAȚII, model interogabil, întrebarea „Ce pot întreba?”
- C10 = MĂSURI, întrebarea „Cât?”
- C11 = COMPARAȚII, întrebarea „Care?”
- C12 = INTERPRETARE, întrebarea „De ce?”

Verb-semnătură C12: a explica.
Rol C12: explică insight-ul verbal, cauza citită din model, interpretarea rezultatului după relații, măsuri și comparații.

Nu porni C12 ca „KPI / FILTER CONTEXT”. Aceasta nu mai este identitatea principală.

## MANDAT C12-04 · GENERARE C12

Claude, lucrează pe main.

Confirm raportul C12-03:
- `SYSTEM_SPEC_REGISTERED`
- SPEC C12 înscris în sistem
- `IDENTITATE_TEHNICA C12` înscrisă
- `pre_generation_check.py 12` PASS
- C12 este gata de generare

Nu alinia Bible §T3 acum.
Bible rămâne v1.0 în această etapă, deoarece nu blochează generarea.
Wording-ul operațional oficial pentru generare este cel din `SPEC_FROZEN` + registrul SPEC activ.

Generează C12 complet, conform sistemului activ și SPEC C12 înghețat.

Respectă:
- C12 = INTERPRETARE
- Hero vizual = DE CE-UL DIN DATE
- Verb-semnătură = a explica
- Întrebare-mamă = De ce?
- Mantra = Cifra spune cât. Explicația spune de ce.
- Motto = Nu citi rezultatul. Explică-l.
- AHA = Nu rezultatul contează. Contează de ce apare rezultatul.
- Formula finală = Rezultat numeric + cauză citită din model + frază verificabilă = insight care închide analiza.

Delimitări obligatorii:
- fără dashboard
- fără what-if
- fără scenarii
- fără predicție
- fără recomandări de acțiune
- fără re-ierarhizare C11
- C12 explică ce s-a întâmplat și de ce, pe baza modelului
- C12 închide T3 ANALIZA

Rulează procedurile obligatorii:
1. `pre_generation_check.py 12`
2. generare artefacte C12
3. `gate_v20.py` pentru C12
4. `audit_sync.py` dacă este cerut de sistem după generare

Raportează:
- fișiere generate/modificate
- PASS/FAIL pentru checks
- eventuale blocaje
- status final

Scrie raportul în:
`_brain/c12/CLAUDE-TO-BRAIN.md`

Status așteptat:
`C12_GENERATED`

## REGULĂ SYSTEM
Pentru acest mandat, ai permisiune explicită de generare C12 conform sistemului activ.
Nu modifica Bible §T3 în această etapă.
