# BRAIN -> CLAUDE C15

## STATUS
C15_IMAGE_PACK_MANDATE_READY

## CONTEXT
C15 SINTETIZAREA a fost generat la nivel text.

Status raport anterior:
C15_GENERATED.

Rezultat anterior:
- 6 artefacte text canonice generate;
- gate_v20.py 15 c15 c01 = PASS;
- audit_sync.py = C15 OK, cu exceptia V39.assets = XX;
- assets / imagini = pending ARHITECT.

C15 nu se redeschide conceptual.
SPEC 11-slot ramane LOCKED.
Artefactele text generate raman neschimbate.

## OBIECTIV
Pregateste pachetul de prompturi / brief-uri pentru imaginile C15 necesare la inchiderea assets:

1. hero-poster C15;
2. 6 imagini exec-stage C15.

Nu genera imaginile aici.
Nu integra imagini.
Nu modifica HTML-urile.
Nu modifica Excel / FILM.
Nu modifica SYSTEM.

## AXA VIZUALA OBLIGATORIE
C15 = SINTEZA.

Imaginea trebuie sa transmita:
- pagina este deja compusa;
- problema este ca pagina nu spune inca mesajul;
- cursantul extrage/formuleaza mesajul esential;
- rezultatul este o singura fraza care conteaza;
- pagina devine dovada mesajului.

NU reprezenta:
- calcul;
- analiza cauzala;
- rearanjare vizuala;
- decizie / livrare;
- rezumat generic;
- dashboard generic fara mesaj.

## CERINTE PENTRU PACHET
Claude C15 trebuie sa propuna:

1. prompt pentru hero-poster C15;
2. prompt pentru imagine E1 INPUT - Pagina muta;
3. prompt pentru imagine E2 AI - Rezumatul automat;
4. prompt pentru imagine E3 SINTEZA - Mesajul esential;
5. prompt pentru imagine E4 CONTROL - Testul si ce-i cu asta?;
6. prompt pentru imagine E5 REFORMULARE - Mesajul se adapteaza la schimbare;
7. prompt pentru imagine E6 PAYOFF - O pagina a devenit un mesaj.

Pentru fiecare imagine include:
- titlu intern;
- scop vizual;
- descriere vizuala;
- elemente obligatorii;
- elemente interzise;
- text vizibil recomandat, daca este cazul;
- format recomandat;
- nota de coerenta cu C15.

## STIL
Pastreaza stilul vizual Trainity / T4:
- premium;
- clar;
- curat;
- business;
- alb / negru / galben;
- fara kitsch;
- fara metafore science-fiction;
- fara personaje exagerate;
- fara iconografie random.

## RAPORT
Scrie raport in:
_brain/c15/CLAUDE-TO-BRAIN.md

Raportul trebuie sa contina:

1. STATUS = C15_IMAGE_PROMPTS_PREPARED
2. CONTEXT GENERARE TEXT
3. PRINCIPIU VIZUAL C15
4. HERO-POSTER PROMPT
5. 6 EXEC-STAGE PROMPTS
6. ELEMENTE INTERZISE GLOBAL
7. CE RAMANE PENDING DUPA ACEST PAS
8. CE NU AI MODIFICAT
9. COMMIT

## CONDITII
- NU genera imagini;
- NU modifica c15/**;
- NU modifica artefactele text;
- NU modifica SYSTEM;
- NU intra in C14 sau C16;
- NU redeschide SPEC C15;
- doar pregateste prompturile pentru ARHITECT.

La final:
commit descriptiv pe main + push.