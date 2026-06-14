# CLAUDE -> BRAIN C19

## STATUS
C19_SPEC_READY_FOR_REVIEW (SPEC 11-slot conceptual pe decizia `C19_SEED_CONCEPTUAL_ACCEPTAT_PROVIZORIU`; sloturile aprobate de BRAIN preluate VERBATIM; FARA livrabile; POATE FI INGHETAT PARALEL cu C18; MOTTO ramane slot CANDIDAT de treapta T5)

SURSA: comanda `sync`. Mandat activ pe origin/main = `MANDAT_SPEC_11_SLOT` (commit f7f1331). Realiniat la origin/main (0d8b7cb). Sloturi aprobate BRAIN preluate verbatim (intrebare centrala, HERO, BOMBA, MANTRA, artefact `_GUVERNARE`, obiect concret). Autorate aici: SLUG, INTRIGA (cadraj), PROBLEMELE, MIZA, WOW, MOTTO (instanta), FENOMENE, STEP-TITLES, GRESEALA (fara formula "Oameni/Profesionisti"), AHA (lock din Doc 14). Ancorat empiric pe: `_brain/c18/CLAUDE-TO-BRAIN.md` = `C18_SPEC_READY_FOR_REVIEW` (SPEC 11-slot AUTOMATIZAREA, aprobat, blueprint cerut), `_system/14-ARHITECTURA-CONCEPTUALA-T5.md`, Bible T5, NOMENCLATURA LOCKED V70. Atins DOAR acest fisier. Zero HTML / Date_MASTER / FILM / build / fisier sistem.

---

## SPEC 11-SLOT C19 PROPUS

### 1. SLUG
- Constructie: **C19 GUVERNAREA**. CUVANT LOCKED (brand): **CONTROL**. Verb LOCKED: **GUVERNEZ**. Iese din **ATENTIE**.
- Slug-token (fisier / asset, kebab fara diacritice, model c07 "datare" / c09 "relatii"): **`guvernare`**. Hero-poster: `hero-poster-excel-19-guvernare.jpg`.
- MIZA HERO (descriptor hov-object, gerunziu + obiect, model C01 "STRUCTURAREA TABELELOR" / C17 "SISTEMATIZAREA MUNCII RELUABILE" / C18 "AUTOMATIZAREA MUNCII RECURENTE"): **"GUVERNAREA SISTEMULUI PRIN REGULI"** (alternativa: "GUVERNAREA EXECUTIEI CORECTE"). Nota anti-contaminare: NU folosesc "motorul" ca obiect (cuvant C18).
- Axa (verbatim CHAT-CONTEXT): **DAI SISTEMULUI REGULI CARE IL TIN CORECT FARA SUPRAVEGHERE.**

### 2. INTRIGA (HERO + BOMBA, ambele aprobate BRAIN verbatim)
- **HERO (intrebare-hero):** "Cum se tine corect fara ochiul meu?"
- **BOMBA:** "Motorul tau ruleaza. Dar tot tu verifici ca n-a gresit, de fiecare data."
- Tensiunea ATENTIE: dupa C18 nu mai apesi butonul (efortul rezolvat), dar inca verifici fiecare rezultat. "Motorul tau" = callback la livrarea C18 (la fel cum BOMBA C18 "Sistemul tau e gata" face callback la C17), NU identitate C19. Izbeste in "se tine corect fara mine?".

### 3. PROBLEMELE
1. Motorul (C18) ruleaza, dar pe o intrare proasta produce rezultat gresit IN TACERE.
2. Un caz neprevazut trece nedetectat si curge in decizii ca si cum ar fi corect.
3. Autorul a scapat de efort, dar tot el verifica "a iesit bine?" la fiecare ciclu (atentia = gatuirea).
4. Greseala se vede tarziu, dupa ce a produs paguba, nu in momentul aparitiei.
5. Nicio regula nu spune sistemului unde sa se opreasca singur; se bazeaza pe ochiul omului.
6. "Merge" e confundat cu "merge corect" (vezi GRESEALA).

### 4. MIZA (director, fara cifre business, R-V02.15)
"Cata vreme cineva trebuie sa confirme de fiecare data ca rezultatul e corect, sistemul nu e autonom: atentia unui om e inca plafonul, iar o intrare gresita nedetectata intra in decizii ca si cum ar fi buna. Guvernarea prin reguli muta verificarea din mintea omului in sistem: deviatiile previzibile sunt prinse, semnalate sau blocate inainte sa produca paguba tacuta. Riscul ascuns inchis: sistemul nu mai produce gunoi in liniste cand nimeni nu se uita." (Director-test, fara "QA" / "SLA" / jargon.)

### 5. MANTRA (decizie BRAIN, verbatim)
**"Nu o supraveghez. O guvernez prin reguli."** (galben: **guvernez**)
("supraveghez" vs "guvernez prin reguli" = mutarea ochiului uman in reguli.)

### 6. WOW (autorat)
**"Un sistem care mergea doar cat stateai cu ochii pe el. Acum, pe o intrare gresita, se opreste singur si aprinde semnalul, fara tine."**
(before: mergea sub supraveghere / after: se prinde singur + semnaleaza + opreste. Anti-C18: nu doar "ruleaza", ci "se prinde cand greseste". Anti-C20: nicio proprietate, nimeni nu "raspunde", doar autocontrol prin reguli. Anti-babysitting: "fara tine". Anti-T4: actioneaza, nu doar afiseaza.)

### 7. MOTTO (slot de treapta T5, TEMPLATE CANDIDAT)
**"Pleci, si munca se tine singura."**
Progresia de treapta (confirmata din ambele parti): C17 "o reia altcineva" -> C18 "pleci din executie, lantul ramane in miscare" -> **C19 "se tine singura"** -> C20 "nu mai e a ta". Statut: instanta C19 e CONFIRMATA de SPEC C17 si SPEC C18 (ambele rezerva explicit "se tine singura" pentru C19); template-ul de treapta "Pleci, si munca [...]" ramane CANDIDAT pana la ratificarea formala (deschis de la C17, reluat de C18). "se tine singura" = reflexiv (ca C18 "ramane in miscare"), potrivit Doc 14 "se TINE corect singur".

### 8. FENOMENE (observabile in Excel, nu teorie)
1. **Intrarea respinsa la sursa:** o validare opreste o valoare gresita inainte sa intre in sistem (Data Validation).
2. **Pragul care aprinde semnalul:** o valoare iese din plicul asteptat si o celula devine ATENTIE (conditional formatting pe REGULA, nu decorativ).
3. **Starea care se schimba:** o celula de stare trece OK -> ATENTIE -> OPRIT dupa reguli.
4. **Exceptia prinsa:** un caz neprevazut cade intr-o lista de exceptii in loc sa treaca tacut (IFERROR / IFS + log de exceptii).
5. **Lantul oprit (fail-safe):** pe o conditie de eroare, lantul se opreste sau se marcheaza in loc sa duca eroarea mai departe.

### 9. STEP-TITLES (6 etape, specifice C19, NU generice)
1. "Sistemul care merge doar cat te uiti" (before, ATENTIE)
2. "Ce poate sa devieze previzibil" (judecata controlului: identifici plicul de variatie)
3. "Regula care prinde intrarea gresita" (validare la sursa)
4. "Pragul si semnalul" (prag -> stare OK / ATENTIE / OPRIT)
5. "Exceptia si fail-safe-ul" (`_GUVERNARE`: ce opreste lantul, ce cere atentie umana - granita C20)
6. "Testul ochilor inchisi" (bagi o intrare proasta, pleci; sistemul o prinde singur)
(18 pasi = 3/etapa, la blueprint. Titluri specifice axei - vezi lectia "titluri exec identice 8/8".)

### 10. GRESEALA (autorat, FARA formula "Oameni/Profesionisti" - in spiritul diversificarii C18)
**"Confunzi «merge» cu «merge corect». Crezi ca ai controlul pentru ca te uiti; dar daca trebuie sa te uiti, nu sistemul se tine singur - tu il tii."**
(Confuzia specifica C19: supravegherea pare control, dar tine omul prezent. "te uiti" = babysitting (respins, Doc 14); "se tine singura prin reguli" = guvernare. Oglinda confuziei C18 "am sistem vs nu mai execut", la nivelul C19 "ma uit vs se tine singur".)

### 11. AHA (lock S5; din Doc 14, aliniat BRAIN)
**"Un sistem in care ai incredere nu e cel pe care il urmaresti. E cel care se prinde singur cand greseste."**
(Candidat confirmat in Doc 14, linia 72. Lock la SPEC. Anti-babysitting in chiar formularea AHA.)

### VERB-SEMNATURA (slot de sprijin)
**a guverna / GUVERNEZ.** Anti-contaminare: a sistematiza (C17), a automatiza (C18), a delega (C20) INTERZISE ca ancora in C19. Verbe-satelit permise: a valida, a semnaliza, a bloca, a marca abaterea, a prinde (deviatia), a opri (fail-safe), a tine corect.

---

## GRANITE SI GARZI

**Formula de paza (mandat):** C18 = **ruleaza** · C19 = **se tine corect** · C20 = **preda responsabilitatea**.

- **C17 <-> C19:** forma reluabila pornita de om vs reguli de corectitudine peste forma care deja ruleaza automat. Garda OGLINDA a C17 (afiseaza starea, NU o judeca) se opreste exact unde incepe C19 (judeca praguri, semnaleaza, blocheaza).
- **C18 <-> C19:** motorul RULEAZA (miscare) vs ruleaza CONTROLAT si isi semnaleaza abaterea. Confirmat din partea C18: SPEC C18 (artefact `_AUTOMATIZARE`, "ce nu este: nu praguri / validari / alerte autocorectate (C19)") + WOW C18 ("nu spune «se controleaza singur»"). C19 NU construieste motorul; primeste un motor care ruleaza si ii pune garzile. Test: daca doar face pasii = C18; daca verifica / semnaleaza / blocheaza / marcheaza abaterea = C19.
- **C19 <-> C20:** PASTREAZA controlul prin reguli (autorul ramane titularul regulilor, iese din atentie, NU din proprietate) vs PREDA titularitatea (iese din proprietate). Semnalul C19 striga "atentie"; CUI striga si CINE raspunde (ownership, rol, escaladare la persoana) = C20. C19 nu desemneaza niciodata un responsabil.
- **C19 <-> C04:** reguli care tin corect un SISTEM care ruleaza vs actualizarea unui SET (Refresh). Output C19 = motor guvernat; output C04 = set reimprospatat.
- **Garzi anti-interdictii (mandat):** SPEC-ul evita management / responsabil / escaladare umana / dashboard decorativ / monitorizare zilnica / QA generic / audit clasic / "motor" ca identitate C19 / ownership / delegare / persoana care verifica. Unde apar termeni de pe lista (GRESEALA "te uiti", BOMBA / INTRIGA "motorul tau"), sunt ANTI-PATTERN (supravegherea respinsa) sau CALLBACK la livrarea C18, NU identitate C19. Marcat explicit slot cu slot.
- **Artefact `_GUVERNARE`** (confirmat Doc 14 linia 91 + decizie BRAIN): reguli / praguri / validari / exceptii / semnale de control / stare a sistemului + ce se intampla la input gresit (respins / blocat / semnalat) + cand se opreste (fail-safe) + cand cere atentie umana (exceptia peste reguli) + unde se opreste inainte de ownership C20 (semnaleaza, nu desemneaza). Adauga PESTE `_AUTOMATIZARE` (C18 = lantul care se misca; C19 = regulile care il tin corect). Distinctivitate vizibila obligatorie (TEST MANIFESTARE Doc 14).

---

## FILMABILITATE EXCEL (din mandat, 8-12 min, zero teorie)
Arc:
1. **before:** sistemul ruleaza, dar tu verifici fiecare rezultat (ochiul prins).
2. **input gresit:** bagi intentionat o valoare proasta.
3. **regula care il prinde:** validarea o respinge la sursa SAU pragul o semnaleaza.
4. **pragul care semnalizeaza + starea care se schimba:** celula OK -> ATENTIE / OPRIT (conditional formatting pe regula).
5. **lantul care se opreste / se marcheaza:** fail-safe opreste secventa inainte sa duca eroarea mai departe; exceptia merge in lista de exceptii.
6. **testul ochilor inchisi:** pleci, sistemul prinde singur deviatia.

**PASS:** spectatorul vede CE regula prinde greseala si CUM sistemul se tine corect fara ochiul omului. **FAIL:** dashboard decorativ citit de un om (T4), SAU un om care verifica (babysitting), SAU doar "ruleaza" fara sa prinda nimic (C18).

---

## DEPENDENTA C18
- C18 = `C18_SPEC_READY_FOR_REVIEW`: SPEC 11-slot AUTOMATIZAREA aprobat, blueprint cerut (commit 6e7d75c). Granita jos C18 e acum ancorata in **SPEC C18**, nu doar in seed.
- **Verdict: SPEC C19 POATE FI INGHETAT PARALEL cu C18.** Motiv: granita C18 <-> C19 e confirmata din AMBELE parti (SPEC C18 rezerva explicit "se controleaza singur", "se tine singura" si praguri / validari / alerte pentru C19; C19 le primeste ca identitate). Cele 10 sloturi non-MOTTO nu depind de finalizarea C18.
- **Singura dependenta reala = MOTTO** (slot de treapta T5): ramane CANDIDAT pana la ratificarea formala a template-ului "Pleci, si munca [...]" (deschis de la C17, reluat de C18). Instanta C19 "se tine singura" e deja folosita verbatim de progresia din SPEC C17 si SPEC C18, deci e stabila pe CONTINUT; doar statutul de "template LOCKED de treapta" ramane de ratificat la nivel T5.
- Daca SPEC C18 s-ar schimba material la review (improbabil, e aprobat), s-ar reverifica DOAR nota de granita jos, nu sloturile C19.

---

## RISCURI
1. Template MOTTO de treapta inca neratificat formal: instanta C19 stabila pe continut (confirmata de C17/C18), dar statutul "template LOCKED" cere o decizie comuna de treapta T5.
2. GRESEALA diversificata (fara "Oameni/Profesionisti"), aliniata la precedentul C18; daca BRAIN vrea alta directie, se ajusteaza un singur slot.
3. WOW / AHA ating zona "incredere / se prinde singur"; tinute strict pe autocontrol prin reguli (NU ownership C20, NU dashboard T4) prin garzile de mai sus.
4. Branch de sesiune divergent fata de main (sesiuni paralele C17 / C18 / C20 active); scris + commitat pe main aliniat, un singur fisier exclusiv C19.

---

## CERERI CATRE BRAIN / SYSTEM
- **Catre BRAIN:** confirmi SPEC 11-slot C19 (inghet PARALEL cu C18)? La confirmare -> SLUG final + blueprint + cele 7 artefacte (doar la mandat explicit).
- **Catre BRAIN:** ratifici instanta MOTTO C19 "se tine singura" sub template CANDIDAT, sau o lasi candidat pana la decizia de treapta T5 comuna (C17-C20)?
- **Catre BRAIN:** confirmi GRESEALA propusa (confuzia "merge vs merge corect" / supraveghere vs control) sau dai alta directie?
- **CERERE SYSTEM:** niciuna. Artefactul `_GUVERNARE` e deja confirmat in Doc 14; nu a fost nevoie sa ating niciun fisier sistem.

---

## COMMIT
Commit descriptiv pe `main`: `docs(c19): SPEC 11-slot GUVERNAREA propus (MANDAT_SPEC_11_SLOT) + ancorare granita pe SPEC C18`. SHA vizibil in `git log` pe main.

**C19_SPEC_READY_FOR_REVIEW**
