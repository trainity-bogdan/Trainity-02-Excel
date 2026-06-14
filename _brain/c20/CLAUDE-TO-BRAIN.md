# CLAUDE -> BRAIN C20

## STATUS
SEED_C20_CONSOLIDAT_DUPA_AUDIT (M1 inchis prin test de predare VIU; M2 inchis pe `_DELEGARE` + formule romanesti; 11-slot canonic propus; gata de SPEC dupa confirmarea formularilor de identitate)

## SURSA
Comanda `sync`. Mandat activ pe origin/main: `_brain/c20/BRAIN-TO-CLAUDE.md` = `CONSOLIDEAZA_SEED_C20_DUPA_AUDIT` (commit 3e159c1). Lucrez direct pe main (permisiune ARHITECT "commite pe main"). Versiunile anterioare (seed `0d8b7cb`, audit `8b85b3d`) raman in istoricul git. Citit ca reper, doar fisiere permise: Doc 14 (T5), NOMENCLATURA-LOCKED-SCARA, mandatul C20 curent. Am scris DOAR acest fisier; zero artefacte de constructie generate.

---

## 1. VERDICT SCURT

SEED C20 consolidat dupa audit. Cele doua finding-uri MAJORE inchise:
- **M1 (manifestare filmabila):** inlocuit DEMO-ul de tip tabel pasiv cu un **TEST DE PREDARE VIU** in workbook - un comutator "scoate autorul" care declanseaza o baterie de verificari prin formule si un STATUS calculat automat (nepredat / partial / delegat / autonom). Echivalentul C20 al testului C19 "bagi o intrare proasta, sistemul o prinde singur": aici "scoti autorul, sistemul dovedeste singur ca se tine fara el".
- **M2 (nomenclatura):** artefact LOCKED pe **`_DELEGARE`** (conform deciziei BRAIN), "proprietate operationala" ramane concept intern, zero mix romana-engleza in formule.

Identitatea ramane curata pe axa PROPRIETATE, verb-semnatura DELEG, granita C19|C20 = control vs transfer. 11-slot remapat pe schema canonica. Singura poarta ramasa inainte de SPEC: BRAIN alege formularile finale de identitate (MANTRA / AHA / MOTTO) dintre variantele testate mai jos.

---

## 2. INCHIDERE M1 - TEST DE PREDARE VIU (nu tabel pasiv)

Problema din audit: DEMO-ul vechi era completarea unui tabel, adica documentare pasiva (interzisa). Lipsea dovada LIVE, filmabila, ca proprietatea S-A TRANSFERAT, nu doar s-a descris.

**Mecanismul propus: TESTUL DE PREDARE in foaia `_DELEGARE`.**

Doua controale care misca tot:
- **`AUTOR_ACTIV`** = comutator DA / NU. Pus pe NU, simuleaza autorul scos din sistem.
- **`ROL_DELEGAT`** = lista de validare cu ROLURI (nu persoane). Rolul care preia.

Cand `AUTOR_ACTIV = NU`, o baterie de verificari prin formule recalculeaza singura si raspunde OK / FAIL. Cele 7 componente cerute de mandat, fiecare ca verificare vie:

| # | Verificare | Ce dovedeste LIVE | OK cand |
|---|---|---|---|
| stare autor scos | `AUTOR_ACTIV = NU` | autorul nu mai e in lant | comutatorul e pe NU si sistemul ramane verde |
| rol nou activ | `ROL_DELEGAT` setat + zona + backup | exista cine preia | rol ales, zona definita, backup-rol prezent |
| V1 zero dependenta author-only | scan referinte critice catre "author-only" | nimic nu se rupe cand pleaca autorul | COUNTIF(referinte author-only in lantul critic) = 0 (altfel #REF! / gol -> FAIL) |
| V2 acces validat | harta de acces a rolului acopera zona de operare | rolul poate opera | rolul vede/modifica tot ce-i trebuie, nimic in plus |
| V3 zone interzise blocate | limitele declarate = ranges chiar blocate | rolul nu poate strica | protectie reala pe zonele "limite", nu doar declarata |
| V4 escaladare functionala | escaladarea tinteste un ROL, cu declansator | problema are unde sa urce | rand escaladare complet, tinta = rol (nu persoana, nu gol) |
| STATUS FINAL (calculat) | agrega tot, formula | unde e predarea acum | vezi mai jos |

**STATUS FINAL = celula calculata prin formula (NU bifata manual):**
- `NEPREDAT` - autor inca activ sau harta goala
- `PARTIAL` - unele verificari OK, altele FAIL
- `DELEGAT` - toate verificarile operationale OK, dar inca sub titulatura autorului
- `AUTONOM` - toate OK + autor scos + zero dependenta author-only + escaladare functionala

**Momentul filmabil (8-12 min, zero teorie):** trainerul completeaza harta rolului, apoi apasa `AUTOR_ACTIV = NU`. Doua finaluri dramatice posibile, ambele pe viu:
1. o dependenta author-only ascunsa se aprinde FAIL (V1), STATUS cade la PARTIAL - "credeai ca ai delegat, dar tu erai cheia"; muti dependenta pe rol, STATUS urca la AUTONOM.
2. nimic nu se rupe, STATUS devine AUTONOM singur - dovada ca sistemul chiar e al rolului.

Asta e transferul DEMONSTRAT, nu documentat. Inchide M1 si capcana RACI/fisa-de-post (m4): tabelul exista, dar VIU-l e statusul care se calculeaza, nu casutele bifate.

---

## 3. INCHIDERE M2 - NOMENCLATURA

Decizie BRAIN adoptata integral:
- **Artefact = `_DELEGARE`.** `_OWNERSHIP` abandonat ca nume principal. "Proprietate operationala" ramane CONCEPT explicat in interior, niciodata nume de foaie/zona.
- **Verb-semnatura LOCKED = DELEG**, ancorat in toate sloturile (hero, mantra, aha, step-titles).
- **Fara formule mixte romana-engleza.** "Ownership" scos din mantra.

Testarea formulelor romanesti pentru MANTRA (ceruta de BRAIN). Gramatica de mantra a pachetului = "Nu [actiune respinsa]. [verb-semnatura] [obiect]." (model C19 "Nu o supraveghez. O guvernez prin reguli."), cu verbul-semnatura DOAR in partea a doua si evidentiat galben:

| Candidat | Verdict |
|---|---|
| "Nu deleg sarcini. Deleg proprietatea sistemului." (BRAIN) | semantic corect, dar pune verbul DELEG in ambele jumatati (rupe tiparul) si e lung |
| "Nu deleg munca. Deleg sistemul." (BRAIN) | acelasi defect (deleg in ambele) + "deleg munca" suna ca delegare normala de task |
| "Nu predau explicatii. Deleg continuitatea." (BRAIN) | respecta tiparul (predau vs Deleg), inchide anti-documentare; bun |
| **"Nu impart sarcini. Deleg sistemul." (propunere CLAUDE)** | **respecta tiparul exact (impart vs Deleg), punchy, inchide anti-impartire-de-taskuri - RECOMANDAT** |

**MANTRA recomandata: "Nu impart sarcini. Deleg sistemul."** (galben: **Deleg**). Alternativa puternica daca BRAIN vrea accent anti-documentare: "Nu predau explicatii. Deleg continuitatea."

---

## 4. 11-SLOT CANONIC PROPUS

1. **SLUG:** `Delegare` (fisier: `Excel-20-Delegare`). MIZA HERO (descriptor hov-object, model C17 "SISTEMATIZAREA MUNCII RELUABILE" / C18 "AUTOMATIZAREA EXECUTIEI REPETITIVE" / C19 "GUVERNAREA SISTEMULUI PRIN REGULI"): **"DELEGAREA SISTEMULUI DE LUCRU"** (alternativa: "DELEGAREA PROPRIETATII OPERATIONALE").

2. **INTRIGA (hero):** **"Cum deleg sistemul, ca sa mearga fara mine?"** (ancoreaza verbul DELEG + axa "fara mine"). Alternativa: "Cum predau cheia, fara sa raman eu cheia?" (mai vizual, dar foloseste "predau", nu verbul locked).

3. **PROBLEMELE:**
- sistemul exista, dar autorul ramane punctul central;
- responsabilitatea nu e transferata explicit;
- drepturile de acces sunt neclare;
- rolul nou nu stie unde poate interveni;
- escaladarea ramane verbala;
- predarea nu poate fi verificata;
- continuitatea depinde de disponibilitatea autorului.

4. **MIZA (director, fara cifre business - R-V02.15):** Cat timp sistemul ramane proprietatea informala a autorului, autonomia e falsa: merge doar cat autorul e disponibil, iar la plecarea lui devine orfan - nimeni nu-l detine, toti il intreaba. Delegarea muta proprietatea de la o persoana la un ROL, verificabil in workbook, ca munca sa aiba cine s-o continue fara autor. Riscul inchis: sistemul bun care moare pentru ca a ramas legat de o singura persoana.

5. **MANTRA:** **"Nu impart sarcini. Deleg sistemul."** (galben: **Deleg**). Vezi sectiunea 3 pentru variante testate.

6. **WOW:** **"Apesi «scoate autorul», si sistemul nu se rupe: workbook-ul confirma singur ca alt rol il poate continua."** (legat direct de testul de predare viu - momentul in care STATUS devine AUTONOM singur).

7. **MOTTO (slot de treapta T5, template "Pleci, si munca [...]"):** **"Pleci, si munca nu mai e a ta."** (candidat BRAIN, confirmat). Inchide progresia: C17 "o reia altcineva" -> C18 "se face singura / ramane in miscare" -> C19 "se tine singura" -> **C20 "nu mai e a ta"**. Ramane TEMPLATE CANDIDAT pana la ratificarea comuna de treapta T5.

8. **FENOMENE:**
- ownership implicit ramas la autor;
- rol operational nedefinit;
- responsabilitate transferata partial;
- acces insuficient sau excesiv;
- interventie fara limita clara;
- escaladare verbala;
- predare imposibil de verificat;
- sistem orfan dupa plecarea autorului.

9. **STEP-TITLES** (8 pasi, ultimii doi ancorati pe testul viu):
1. Identifica rolul care preia sistemul (rol, nu persoana).
2. Stabileste responsabilitatea care se transfera.
3. Mapeaza accesul necesar pentru operare.
4. Defineste punctele unde rolul poate interveni.
5. Blocheaza zonele care nu trebuie atinse.
6. Stabileste escaladarea (catre ce rol, cu ce declansator).
7. Ruleaza testul de predare: scoate autorul, vezi daca sistemul se tine.
8. Citeste statusul calculat: nepredat / partial / delegat / autonom.

10. **GRESEALA** (diversificata, FARA formula saturata "Oamenii / Profesionistii" - R8): **"Crezi ca ai delegat cand ai explicat. Dar explicatia nu muta proprietatea: la prima problema, tot pe tine te suna."** (inchide anti-documentare; verbul DELEG prezent). Varianta cu formula de treapta, daca BRAIN vrea consistenta: "Oamenii predau instructiuni. Profesionistii deleg proprietatea." - dar recomand varianta diversificata.

11. **AHA** (candidat lock S5). BRAIN a cerut testarea verbului locked pe "Nu o tin. O predau." (Doc 14, linia 118):
- "Nu o tin. O predau." - original Doc 14, dar "predau" nu e verbul locked;
- "Nu o tin. O deleg." - verb locked, curat;
- **"Nu o pastrez. O deleg."** - verb locked + antonim mai ascutit (pastrez vs deleg) - RECOMANDAT ca forma scurta.

Pentru a NU suprapune AHA peste MANTRA (ambele "Nu X. deleg Y"), propun ca AHA sa fie reframe-ul, nu stance-ul: **AHA primar = "Un sistem nu e autonom pentru ca merge singur. E autonom cand il poate detine altcineva."** (redefineste autonomia, distinge de C18 "merge fara efort", inchide pachetul). Forma scurta "Nu o pastrez. O deleg." ramane disponibila daca BRAIN prefera un AHA-mantra. **BRAIN alege: reframe lung sau forma scurta cu verb locked.**

---

## 5. ARTEFACT `_DELEGARE` WORKBOOK-NATIVE

Foaie / zona `_DELEGARE`, nativ-Excel, distincta de `_GUVERNARE` (C19). Trei straturi:

**A. CONTROALE (motorul testului viu)**
- `AUTOR_ACTIV` (DA / NU) - comutatorul de predare;
- `ROL_DELEGAT` (validare de lista, ROLURI) - cine preia.

**B. HARTA DE PREDARE** (ce se transfera - inputul rolului):
- Rol operational: rol, zona detinuta, backup-rol (regula: nume de persoana NU e identitate; persoana se ataseaza temporar, proprietatea e a rolului);
- Responsabilitate transferata: proces preluat, decizii permise, actualizari permise, livrare asigurata;
- Acces si drepturi: ce vede, ce modifica, ce e protejat, ce surse actualizeaza, ce cere aprobare;
- Puncte de interventie: unde, cand, ce declanseaza, ce rezultat;
- Limite: ce nu poate schimba / sterge / recalibra (mapate la ranges chiar blocate);
- Escaladare: catre ce rol, cu ce declansator, cu ce dovada, in ce termen.

**C. VERIFICARE VIE + STATUS** (output-ul, calculat din A + B):
- V1-V4 (zero dependenta author-only / acces validat / zone blocate / escaladare functionala) - formule OK/FAIL;
- `STATUS FINAL` (formula): NEPREDAT / PARTIAL / DELEGAT / AUTONOM.

**Distinctivitate vs `_GUVERNARE` (inchide m5):** `_GUVERNARE` (C19) = reguli care prind un INPUT GRESIT (validare, prag, semnal, fail-safe); subiectul = corectitudinea datelor. `_DELEGARE` (C20) = predarea PROPRIETATII, testata prin scoaterea AUTORULUI; subiectul = cine detine sistemul. Test de manifestare Doc 14: cele doua foi sunt vizibil diferite (C19 reactioneaza la date, C20 reactioneaza la disparitia omului).

---

## 6. RISCURI RAMASE

- **Proximitate RACI / fisa de post (m4):** atenuata de STATUS-ul calculat (viu, nu bifat), dar la SPEC harta de predare nu trebuie sa devina o organigrama. Garda: tot ce e in `_DELEGARE` exista ca sa alimenteze testul viu, nu ca lista de citit.
- **"Rol nu persoana"** trebuie tinut peste tot (acces, escaladare, backup) ca sa nu alunece in HR.
- **Granita la "escaladare":** escaladarea C20 = catre un ROL care preia proprietatea, nu semnalul de control C19. De pazit la SPEC sa nu recada in C19.
- **Filmabilitate reala:** testul de predare e filmabil, dar cere scenariu (drama FAIL ascuns -> reparare -> AUTONOM), altfel devine demo plat.
- **MOTTO / AHA cu verb locked = inca CANDIDATE** (cer lock S5 la confirmarea BRAIN). Template de treapta T5 inca neratificat global.
- **Granita jos (C19/C18)** se sprijina pe SPEC-uri inca neratificate final (C18 blueprint, C19 SPEC propus); de reconfirmat cand se inghetata.

---

## 7. RECOMANDARE

Cu M1 inchis (test de predare viu) si M2 inchis (`_DELEGARE` + formule romanesti), SEED-ul C20 e consolidat si pregatit pentru SPEC. Mai ramane O SINGURA poarta: BRAIN confirma formularile finale de identitate, ca sa le pot ingheta la SPEC (lock S5):
- MANTRA: "Nu impart sarcini. Deleg sistemul." (recomandat) sau "Nu predau explicatii. Deleg continuitatea."?
- AHA: reframe lung ("Un sistem nu e autonom pentru ca merge singur...") sau forma scurta cu verb locked ("Nu o pastrez. O deleg.")?
- MIZA HERO: "DELEGAREA SISTEMULUI DE LUCRU" sau "DELEGAREA PROPRIETATII OPERATIONALE"?

La confirmarea acestor trei -> emit **SLUG + SPEC 11-slot C20** (cerere explicita). Daca BRAIN vrea, mai e loc de o micro-runda doar pe formulari; altfel, **gata de SPEC**.

**SEED_C20_CONSOLIDAT_DUPA_AUDIT - M1 + M2 INCHISE.**
