# CLAUDE -> BRAIN C18

## STATUS
C18_SEED_PROPUS (SEED conceptual propus pe mandatul CORECTIE_C18; asteapta review / ratificare ARHITECT)

## SURSA
Comanda `sync` in chatul CLAUDE C18. Mandatul activ a fost gasit pe origin/main (commit 25f45ea, _brain/c18/BRAIN-TO-CLAUDE.md = CORECTIE_C18), NU pe branchul de sesiune (acolo era inca READY_FOR_BRAIN_MANDATE / "wait", stale). Mandat: "Propune SEED conceptual C18 pentru AUTOMATIZAREA", C18 autonom, C17 = reper conceptual (nu dependenta operationala). Citit ca reper: _system/14-ARHITECTURA-CONCEPTUALA-T5.md (sectiunea C18), _brain/c17/CLAUDE-TO-BRAIN.md (granita C17<->C18). Nomenclatura LOCKED V70: C18 AUTOMATIZAREA / CUVANT MOTOR / VERB AUTOMATIZEZ / iese din EFORT.

NOTA DE LIVRARE: branchul de sesiune (claude/bold-galileo-vt3cwd) e divergent fata de main (force-update 4176b5b->25f45ea, alte sesiuni paralele active). Raportul e scris aici si commitat pe branch; landingul pe main asteapta decizia ARHITECT (vezi intrebarea din chat). Am atins DOAR acest fisier (CLAUDE-TO-BRAIN.md), conform permisiunilor CLAUDE C18.

---

# SEED CONCEPTUAL C18 AUTOMATIZAREA

## 1. IDENTITATE C18
C18 AUTOMATIZAREA = **proiectarea retragerii omului din executia repetitiva**. NU configurarea unei unelte. Identitatea e o **judecata**: ce e destul de stabil si repetabil incat sa nu mai treaca prin mainile autorului la fiecare ciclu, si cum se construieste lantul care ruleaza fara ca vreun om sa faca pasii. Mecanismul tehnic (Power Query orchestrat, macro, trigger, secventa inlantuita) = **MIJLOC, nu identitate**.

Pozitia in lant: C18 primeste din C17 **forma reluabila** (sistemul exista, dar inca il porneste un om) si o transforma in **miscare** (lantul se executa singur). Preda la C19 un **motor care ruleaza, dar nu se autocontroleaza inca** (un esec inca cere omul).

Verb-semnatura: **a automatiza / AUTOMATIZEZ**. Axa: scoaterea autorului din EFORT.
MIZA HERO (descriptor hov-object, model C01 "STRUCTURAREA TABELELOR" / C17 "SISTEMATIZAREA MUNCII RELUABILE"): **"AUTOMATIZAREA EXECUTIEI REPETITIVE"** (alternativa: "AUTOMATIZAREA MUNCII RECURENTE").

## 2. MIZA C18 (director, fara jargon, fara cifre business - R-V02.15)
Cata vreme fiecare ciclu de munca cere mana autorului, timpul lui e consumat de repetitie, nu de judecata. Munca recurenta creste cu fiecare ciclu, iar omul devine plafonul. Automatizarea muta executia repetitiva pe un motor si elibereaza autorul pentru munca pe care doar el o poate face. Riscul ascuns inchis: procesul nu se mai opreste cand autorul e prins cu altceva. (Calitativ, fara "FTE"/"ROI"/jargon. Director-test.)

## 3. INTREBARE CENTRALA
**"Ce din munca asta poate rula fara sa o fac eu de fiecare data, si cum ma scot din bucla?"**
(Doc 14: C18 = "ruleaza fara ca vreun om sa faca pasii". Intrebarea e despre retragere, nu despre unealta.)

## 4. FORMULE (cerute in mandat)

### HERO
Intrebare-hero: **"Cum scot mana mea din ce se repeta?"**

### BOMBA
**"Sistemul tau e gata. Dar tot tu apesi pe buton, de fiecare data."**
(Tensiunea EFORT: forma reluabila din C17 exista, dar autorul e inca in bucla la fiecare ciclu. Izbeste direct in "se face singura?".)

### MANTRA
**"Nu o execut. O las sa ruleze."** (galben: **ruleze**)
(Verbatim linia C18 din Doc 14. "execut" vs "las sa ruleze" = exact mutarea omului din lant.)

### MOTTO (slot de treapta T5)
**"Pleci, si munca se face singura."**
(Instantiaza template-ul de treapta propus la C17 "Pleci, si munca [se retrage autorul, gradat]". Progresia: C17 "o reia altcineva" -> **C18 "se face singura"** -> C19 "se tine singura" -> C20 "nu mai e a ta". Subiectul marcheaza granita: C17 = altcineva-OM porneste; C18 = singura, fara om. CERE ratificarea template-ului de treapta, ramasa deschisa de la C17.)

## 5. RISCURI DE CONTAMINARE (cu garda fiecare)
- **R1 -> C04 (cel mai periculos):** "Apas Refresh" / actualizez un set de date ca IDENTITATE. C04 = actualizarea unui set printr-un flux; C18 = scoaterea omului din LANTUL end-to-end. Garda: Refresh/Power Query = mijloc permis DOAR daca serveste retragerea omului din lant; nu devine identitatea. C18 elimina PASI din lant, nu doar reimprospateaza date.
- **R2 -> mecanism-ca-identitate:** aluneca in "configurez Power Automate / scriu o macro". Garda: identitatea = judecata retragerii. Filmul arata DECIZIA (ce las sa ruleze) + lantul, nu un tutorial de unealta.
- **R3 -> C17 (forma):** redescrie "cum se reia munca" / "definesc structura". Garda: C17 = forma reluabila pornita de om; C18 = miscarea fara om. C18 nu spune niciodata "definesc structura".
- **R4 -> C19 (autocontrol):** apar praguri / validari / alerte / exceptii autocorectate. Garda: C18 RULEAZA, dar NU se autoguverneaza; un esec inca cere omul. Autocontrolul = C19.
- **R5 -> C20 (ownership):** apare "cine raspunde / cine detine / escaladare". Garda: C18 = miscare tehnica, nu desemnare de proprietate.
- **R6 -> "se face singur" prematur:** pretinde autonomie totala (zero om) cand inca exista un hand-off manual. Garda: artefactul _AUTOMATIZARE declara EXPLICIT ce ramane interventie umana minima.
- **R7 -> saturatie "Oamenii/Profesionistii":** formula de treapta e saturata 100% (mostenit din C17). De diversificat daca ARHITECT cere.

## 6. CRITERIU DE FILMABILITATE (Excel, 8-12 min, zero teorie)
Arc:
1. **before:** autorul face manual lantul la fiecare ciclu (deschide, copiaza, reimprospateaza, lipeste, formateaza) - vizibil obositor, pas cu pas.
2. **construiesti motorul:** legi pasii intr-un lant declansat de o singura actiune; externalizezi ce era manual.
3. **_AUTOMATIZARE (artefactul vizibil, Doc 14):** o foaie/zona care arata LANTUL: ce pasi manuali au fost ELIMINATI (taiati vizibil), CE declanseaza lantul, CE ramane interventie umana minima (marcat explicit).
4. **testul retragerii pe viu:** declansezi o data, autorul isi ia mainile de pe tastatura, lantul merge pana la capat singur; ciclul urmator ruleaza fara pasii manuali.

**Criteriu PASS:** spectatorul vede CE munca a iesit din mainile autorului si CE ramane (interventia minima). **FAIL:** filmul e "cum configurez unealta X" (R2) sau doar "apas Refresh" (R1/C04).

**Distinctivitate artefact (TEST DE MANIFESTARE Doc 14):** _AUTOMATIZARE adauga PESTE _SISTEM (C17), nu il reboteaza. C17 _SISTEM = harta functionala, navighezi/oglindesti, un OM porneste. C18 _AUTOMATIZARE = lant de executie, se misca fara om.

## 7. GRANITE (compact)
- **C17 <-> C18:** forma (sistem pornit de om) vs miscare (lant fara om).
- **C18 <-> C04:** lant end-to-end fara om vs Refresh/actualizare set. Refresh = mijloc, nu identitate.
- **C18 <-> C19:** ruleaza vs se autocontroleaza (praguri/validari/exceptii = C19).
- **C18 <-> C20:** miscare tehnica vs ownership/escaladare.

## 8. PROBLEMELE C18 (sustin MIZA)
1. Acelasi lant de pasi se reface manual la fiecare ciclu.
2. Autorul e gatuirea: cand e ocupat, ciclul se opreste.
3. Pasii manuali introduc variatie si erori intre cicluri.
4. Timpul de judecata e mancat de timpul de executie.
5. Forma reluabila (C17) exista, dar nimic nu se misca fara mana omului.

## 9. FENOMENE OBSERVABILE (Excel, nu teorie)
1. **Lantul intr-un singur declansator:** o actiune porneste o secventa care inainte cerea N pasi manuali.
2. **Pasul eliminat:** un pas manual dispare din flux si rezultatul ramane corect.
3. **Mainile jos:** dupa declansare, executia continua fara interventie pana la capat.
4. **Interventia minima ramasa:** un singur punct unde omul mai atinge procesul, marcat explicit (granita catre C19).
5. **Ciclul urmator gratis:** al doilea ciclu ruleaza fara sa reconstruiesti nimic.

## 10. STEP-TITLES CANDIDATE (6 etape, specifice C18)
1. "Lantul pe care il faci de fiecare data" (before, EFORT)
2. "Ce merita scos din mainile tale" (judecata retragerii)
3. "Pasii legati intr-un singur declansator" (construirea motorului)
4. "Pasul manual care dispare" (eliminare, nu doar Refresh - granita C04)
5. "Ce ramane mana omului" (_AUTOMATIZARE: interventia minima explicita, granita C19)
6. "Testul retragerii" (mainile jos, lantul merge singur)
(18 pasi = 3/etapa, se detaliaza la blueprint. Titluri specifice axei, nu generice.)

## 11. VERB-SEMNATURA
**a automatiza / AUTOMATIZEZ.** Anti-contaminare: a sistematiza (C17), a guverna (C19), a delega (C20) INTERZISE ca ancora in C18. Verbe-satelit permise: a inlantui, a declansa, a rula, a elimina (pasi), a se retrage, a externaliza executia.

## TESTE DE PAZA
- **Testul retragerii:** opreste autorul (mainile jos) dupa declansare. PASS = ciclul se duce la capat fara el. FAIL = se blocheaza la un pas manual neeliminat -> e inca C17 (forma), nu C18 (miscare).
- **Testul anti-C04:** daca tot ce face artefactul e "actualizeaza un set la apasare", e C04. C18 trebuie sa ELIMINE pasi din lant.

## VERDICT
SEED conceptual C18 pe axa "judecata retragerii / scoaterea autorului din EFORT", verb-semnatura "a automatiza", ancorat in artefactul _AUTOMATIZARE (Excel-native, distinct de _SISTEM al C17). Toate cele 7 elemente cerute in mandat sunt acoperite (identitate, miza, intrebare centrala, riscuri de contaminare, formule HERO/BOMBA/MANTRA/MOTTO, criteriu de filmabilitate) + granite, problemele, fenomene, step-titles, verb, teste de paza. Zero contaminare C04/C17/C19/C20 (verificat punct cu punct).

Doua puncte care cer decizie ARHITECT la review:
(a) ratificarea template-ului de treapta T5 pentru MOTTO "Pleci, si munca [...]" (ramas deschis de la C17);
(b) daca diversifica GRESEALA / formula "Oamenii/Profesionistii" (R7, saturatie 100%).

Pasul urmator dupa review: SLUG + SPEC 11-slot C18 (la cerere explicita), apoi blueprint + cele 7 artefacte. Nu am generat SPEC/HTML/Date_MASTER/FILM (nu erau in mandat).

C18_SEED_PROPUS
