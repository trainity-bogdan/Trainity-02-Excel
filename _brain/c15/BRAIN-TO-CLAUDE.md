# BRAIN -> CLAUDE C15

## STATUS
FREEZE_GENERATION_SPEC_MANDATE_READY

## CONTEXT
C15 SINTETIZAREA. T4 RAPORTARE. CUVANT LOCKED: SINTEZA. VERB LOCKED: SINTETIZEZ.

SPEC 11-slot C15 este inghetat conceptual v1.0.

Blueprint C15 v1.1 este aprobat conceptual de BRAIN.

Decizii BRAIN dupa BLUEPRINT_V1_1_PREPARED:
1. D-E5 = DA. E5 final este REFORMULARE - Mesajul se adapteaza la schimbare.
2. Pentru phase-tag, calea recomandata este (iii): phase-tag-ul intern poate ramane RECALCUL daca sistemul il cere, dar eticheta conceptuala si afisata pentru C15 trebuie sa fie REFORMULARE.
3. D-EXCEL = DA. Substratul Excel C15 este strat MESAJ, nu strat de calcul.
4. Regula substratului: mesajul citeste din pagina, nu produce pagina.

## SPEC 11 SLOT C15 LOCKED

1. HERO:
Cum transform o pagina intr-o singura fraza care conteaza?

2. BOMBA:
O pagina impecabila. Si niciun mesaj.

3. GRESEALA:
Oamenii rezuma tot. Profesionistii formuleaza ce conteaza.

4. AHA:
O pagina arata. O sinteza spune.

5. MANTRA:
Nu rezumam. Sintetizam.

6. WOW:
O pagina intreaga pe care trebuia s-o descifrezi. Acum o singura fraza iti spune ce conteaza, iar pagina o dovedeste.

7. MOTTO:
Dintr-o privire, mesajul.

8. CINE DEVII:
Nu mai prezinti tot ce ai. Sintetizezi singura fraza care conteaza.

9. PAYOFF:
O pagina coerenta a devenit un mesaj care conteaza.

10. MIZA:
Un director nu citeste toata pagina. O deschide si intreaba: si ce-i cu asta? Are zece rapoarte corecte pe masa si trei minute pentru fiecare. C15 e momentul in care o pagina intreaga capata o singura fraza care spune ce conteaza din ea, dintr-o privire. Nu o cifra noua, nu o cauza noua (acelea vin gata din analiza), ci mesajul: ce trebuie sa retii. Fara sinteza, pana si cel mai corect raport ramane mut: arata tot si nu spune nimic. Cu sinteza, decidentul stie in trei secunde ce conteaza si ce sa retina.

11. VERB-SEMNATURA:
SINTETIZEZ.

## BLUEPRINT C15 V1.1 LOCKED PENTRU FREEZE GENERATION SPEC

Axa:
SINTEZA, nu rezumat.

E5 final:
REFORMULARE - Mesajul se adapteaza la schimbare.

Cei 3 pasi E5 finali:
- PAS 13: Pagina se schimba, datele s-au actualizat in amonte, in model/T3, iar mesajul vechi nu mai este exact.
- PAS 14: Reformulezi headline-ul, refaci sinteza, NU recalculezi nimic; cifrele raman ale modelului.
- PAS 15: Noul mesaj ramane o singura afirmatie sustinuta de pagina, pe acelasi criteriu: ce conteaza.

Substrat Excel C15:
Date_MASTER-C15 = dashboard mostenit + strat MESAJ.

Stratul MESAJ contine:
- o celula headline, textul de o fraza formulat de cursant;
- o linie so-what, de ce conteaza, tot text;
- o legatura la pagina-dovada.

Stratul MESAJ face:
- enunta in cuvinte ce conteaza din pagina;
- leaga mesajul de dovada vizuala existenta;
- poate insera intr-o fraza-sablon o valoare deja calculata in amonte, ca plasare, nu calcul.

Stratul MESAJ nu face:
- nu calculeaza insight;
- nu descopera cauza;
- nu genereaza recomandare;
- nu rearanjeaza pagina;
- nu muta C15 in C14, C16 sau T3.

Regula de aur:
Mesajul citeste din pagina, nu produce pagina.

## MANDAT
Claude C15 executa exclusiv freeze-ul celor 9 elemente SPEC de generare pentru C15.

NU executa generarea efectiva.
NU creezi artefacte.
NU generezi c15/**.
NU creezi HTML, Excel, FILM, imagini sau fisiere livrabile.
NU modifici fisiere sistem.
NU modifici alte constructii.
NU intri in _brain/c13 sau alte foldere _brain/cYY.
NU repari nimic in afara acestui mandat.

Obiectiv:
1. marcheaza cele 9 elemente SPEC de generare C15 ca freeze-ready sau locked, dupa caz;
2. integreaza deciziile BRAIN: E5 = REFORMULARE, substrat Excel = strat MESAJ;
3. pastreaza SPEC 11-slot neatins;
4. consolideaza SLUG, INTRIGA, PROBLEMELE, FENOMENE, STEP-TITLES si celelalte elemente cerute de protocolul B1;
5. marcheaza explicit ce trebuie propagat ulterior de SYSTEM in registru, IDENTITATE_TEHNICA C15 si gate dict '15';
6. confirma ca dupa acest freeze conceptual se poate cere mandatul SYSTEM de inregistrare, nu generarea efectiva.

## CERINTE DE RAPORTARE
Raportul trebuie sa contina obligatoriu:

1. STATUS = GENERATION_SPEC_FREEZE_PREPARED
2. SPEC 11-SLOT RAMAS LOCKED
3. CELE 9 ELEMENTE SPEC DE GENERARE C15 FREEZE-READY
4. E5 FINAL INTEGRAT
5. SUBSTRAT EXCEL C15 FINAL INTEGRAT
6. STRUCTURA 6 ETAPE / 18 PASI FINALIZATA CONCEPTUAL
7. FENOMENE / VERIFICARI / PROMPTURI AI FINALIZATE CONCEPTUAL
8. CERERI SYSTEM NECESARE INAINTE DE GENERARE
9. DECIZII RAMASE PENTRU BRAIN, DACA EXISTA
10. CE NU AI FACUT

## CONDITII DE ACCEPTARE
Acceptabil doar daca:
- raportul are status GENERATION_SPEC_FREEZE_PREPARED;
- nu redeschizi SPEC 11-slot C15;
- nu modifici sloturile locked;
- E5 ramane REFORMULARE;
- substratul Excel ramane strat MESAJ, nu strat de analiza;
- nu generezi artefacte;
- raportul ramane freeze conceptual al SPEC-ului de generare, nu executie;
- marchezi clar ca urmatorul pas este SYSTEM registration, nu generare directa.

## RAPORT
Scrie raportul in _brain/c15/CLAUDE-TO-BRAIN.md si apoi commit descriptiv pe main + push.