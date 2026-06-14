# CLAUDE -> BRAIN C19

## STATUS
C19_BLUEPRINT_CONCEPTUAL_READY_FOR_REVIEW (Blueprint conceptual pe `C19_SPEC_11_SLOT_FROZEN_ACCEPTAT`; 6 etape locked + 18 pasi 3/etapa + arc demonstrativ + garzi per etapa; FARA livrabile, fara folder c19/)

SURSA: comanda `sync`. Mandat activ pe origin/main = `MANDAT_BLUEPRINT_CONCEPTUAL` (commit 5ecd2be). Realiniat la origin/main (cf770df). SPEC 11-slot inghetat; sloturile + cele 6 titluri de etapa preluate VERBATIM. Ancorat pe inchiderea conceptuala C18 (1b0518d) + Doc 14. Atins DOAR acest fisier. Zero HTML / Date_MASTER / FILM / build / folder c19/ / fisier sistem / alt _brain.

---

## BLUEPRINT CONCEPTUAL C19

**Ce construieste cursantul:** stratul de CONTROL peste motorul mostenit din C18. Un singur artefact vizibil nou: foaia **`_GUVERNARE`** = constitutia sistemului (reguli + praguri + validari + stare + exceptii + fail-safe). Cursantul nu construieste motorul (e dat de C18); ii pune garzile care il tin corect fara ochiul lui.

**Punct de plecare (handoff C18):** un motor care RULEAZA singur (lant automatizat input -> output), dar care pe o intrare proasta produce rezultat gresit IN TACERE. Singura plasa actuala = ochiul autorului.

**Punct de sosire (handoff C20):** un sistem GUVERNAT care prinde / semnaleaza / opreste singur deviatiile previzibile si isi arata starea, dar inca DETINUT de autor (titularul regulilor). C19 nu preda proprietatea (= C20).

**Forma:** 6 etape x 3 pasi = 18 pasi. Filmabil 8-12 min, zero teorie, actiune Excel. Artefactul `_GUVERNARE` se umple progresiv, etapa cu etapa.

**Distinctivitate (TEST MANIFESTARE Doc 14):** `_GUVERNARE` adauga PESTE `_AUTOMATIZARE` (C18). C18 `_AUTOMATIZARE` = lantul care se misca; C19 `_GUVERNARE` = regulile care il tin corect. Foi vizibil diferite.

---

## CELE 6 ETAPE

### Etapa 1 - `Sistemul care merge doar cât te uiți`
- **Scop:** stabilesti durerea ATENTIE: motorul ruleaza, dar pe intrare proasta produce gunoi tacut; singura garantie e ochiul tau.
- **Obiect Excel:** motorul C18 (lantul dat) + o foaie noua `_GUVERNARE` GOALA (locul unde muti verificarea din cap in sistem).
- **Ce se vede in film:** rulare buna (ok), apoi o intrare proasta care trece tacut intr-un rezultat gresit; mana ta verificand manual; foaia `_GUVERNARE` goala ca promisiune.
- **Ce NU apare:** nu repari / optimizezi motorul (= C18); nu pui un om sa verifice (= babysitting / C20); nu faci un dashboard frumos (= T4).
- **Test de validare:** PASS daca durerea citita e "trebuie sa ma uit eu ca sa prind greseala". FAIL daca pare ca motorul e de reparat (aluneca in C18).

### Etapa 2 - `Ce poate să devieze previzibil`
- **Scop:** judecata C19 (scrii constitutia, nu patrulezi): identifici plicul de variatie PREVIZIBILA inainte de a scrie regula.
- **Obiect Excel:** in `_GUVERNARE`, un "registru al deviatiilor previzibile" (ce poate devia | cum se manifesta | severitate) + parametri vii de prag (`LIMIT_MIN`, `LIMIT_MAX`, lista valida).
- **Ce se vede in film:** registrul umplandu-se cu moduri de esec previzibile (valoare lipsa / in afara intervalului / tip gresit / duplicat / total care nu se inchide); pragurile scrise ca celule vii.
- **Ce NU apare:** nu incerci sa acoperi orice imprevizibil (fantezie, nu guvernare); nu "monitorizezi"; nu desemnezi cine reactioneaza (C20).
- **Test de validare:** PASS daca fiecare viitoare regula tinteste un mod de esec PREVIZIBIL cu plic definit. FAIL daca lista incearca sa prinda orice eventualitate (babysitting deghizat).

### Etapa 3 - `Regula care prinde intrarea greșită`
- **Scop:** prima garda reala: validarea care RESPINGE intrarea gresita la sursa, inainte sa intre in motor.
- **Obiect Excel:** Data Validation pe zona de intrare (interval `LIMIT_MIN:LIMIT_MAX` / lista permisa / formula custom), legata de parametrii din etapa 2 + mesaj de respingere.
- **Ce se vede in film:** introduci o valoare in afara plicului -> Excel o respinge pe loc; intrarea proasta nu mai ajunge in motor; regula notata in `_GUVERNARE`.
- **Ce NU apare:** nu corectezi tu manual valoarea (ai deveni tu garda = babysitting); nu transformi in pas de motor (C18); nu trimiti la cineva (C20).
- **Test de validare:** PASS daca intrarea gresita e respinsa AUTOMAT. FAIL daca prinderea cere interventia ta.

### Etapa 4 - `Pragul și semnalul`
- **Scop:** pentru ce trece de validare dar derapeaza INTERN, pui praguri care aprind semnale si schimba STAREA sistemului; control care actioneaza, nu decor.
- **Obiect Excel:** conditional formatting pe REGULA (nu estetic) + celula de stare `STATUS` (formula IFS pe praguri) care afiseaza OK / ATENTIE / OPRIT; un panou de semnale in `_GUVERNARE`.
- **Ce se vede in film:** o valoare interna care derapeaza -> celula se aprinde ATENTIE -> `STATUS` trece din OK in ATENTIE, automat, fara om.
- **Ce NU apare:** semnalul NU e un dashboard de citit pentru un om care decide (T4); nu e "ma uit zilnic" (monitorizare); nu e culoare fara regula.
- **Test de validare:** PASS daca o abatere interna schimba STAREA singura. FAIL daca semnalul e cosmetic sau trebuie citit de cineva ca sa conteze.

### Etapa 5 - `Excepția și oprirea controlată`
- **Scop:** cazul neprevazut care depaseste regulile NU e dus mai departe: e marcat EXCEPTIE si lantul se OPRESTE controlat (fail-safe), starea devine OPRIT. Fara responsabil, fara escaladare (granita C20).
- **Obiect Excel:** IFERROR / IFS care deviaza cazul intr-o lista de EXCEPTII din `_GUVERNARE` + un fail-safe care leaga output-ul de `STATUS` (cand STATUS=OPRIT, rezultatul corupt nu mai curge in aval).
- **Ce se vede in film:** cazul neprevazut -> marcat exceptie -> lantul se opreste controlat -> output-ul corupt NU pleaca mai departe. `_GUVERNARE` arata: ce exceptie, cand s-a oprit, ce stare. (Per mandat: `_GUVERNARE marcheaza exceptia, opreste lantul sau schimba starea, dar nu desemneaza responsabilul.`)
- **Ce NU apare:** fara "escaladare la persoana", fara "responsabil", fara "owner" (= C20); fara ca TU sa opresti manual (regula opreste).
- **Test de validare:** PASS daca oprirea e automata si fara desemnare de om. FAIL daca apare "trimite la X" / "cineva trebuie sa" (C20) sau daca tu opresti manual.

### Etapa 6 - `Testul ochilor închiși`
- **Scop:** dovada autonomiei C19 (echivalent Testul concediului, Doc 14): autorul pleaca, deviatiile previzibile sunt gestionate de reguli, nu de ochi.
- **Obiect Excel:** `_GUVERNARE` complet (reguli + praguri + stare + exceptii + fail-safe) ruland pe un set cu deviatii plantate, fara mana autorului.
- **Ce se vede in film:** autorul cu mainile jos; validarea respinge, pragul semnaleaza, exceptia opreste, toate singure; starea finala citita din `_GUVERNARE` arata exact ce s-a prins.
- **Ce NU apare:** nu predai proprietatea / responsabilitatea (= C20); nu ramai sa te uiti (babysitting); nu adaugi un om de control.
- **Test de validare:** PASS daca, cu autorul absent, deviatiile previzibile sunt prinse de reguli (sistemul se tine corect singur). FAIL daca tot e nevoie de ochiul tau sau de un om.

---

## CEI 18 PASI (3 per etapa, specifici axei)

**Etapa 1:**
1. Pornesti motorul C18 pe o intrare buna: rezultat corect, totul pare ok.
2. Strecori o intrare proasta (valoare aberanta / lipsa); motorul produce rezultat gresit fara sa se planga.
3. Deschizi foaia noua `_GUVERNARE` (goala): aici muti verificarea din capul tau in sistem.

**Etapa 2:**
4. Listezi modurile de esec previzibile (lipsa, in afara intervalului, tip gresit, duplicat, total care nu se inchide).
5. Definesti plicul asteptat pentru fiecare ca parametri vii (`LIMIT_MIN`, `LIMIT_MAX`, lista permisa, regula de suma).
6. Marchezi severitatea: ce se BLOCHEAZA la sursa vs ce doar SEMNALEAZA vs ce OPRESTE lantul (fara sa implici un om).

**Etapa 3:**
7. Aplici Data Validation pe zona de intrare (interval / lista / formula custom legata de `LIMIT_`).
8. Testezi: o valoare in afara plicului e respinsa la sursa; intrarea proasta nu ajunge in motor.
9. Inregistrezi regula in `_GUVERNARE` (ce coloana, ce regula, ce respinge): regula devine vizibila.

**Etapa 4:**
10. Definesti pragurile pe valorile interne (abatere > X, suma care nu se inchide) ca formule pe `LIMIT_`.
11. Conditional formatting aprinde semnalul ATENTIE cand pragul e depasit (legat de regula, nu estetic).
12. Celula `STATUS` agrega regulile: OK daca toate trec, ATENTIE pe abatere, OPRIT pe eroare grava (IFS).

**Etapa 5:**
13. Prinzi cazul care scapa regulilor cu IFERROR / IFS si il trimiti in lista de EXCEPTII (nu il lasi tacut).
14. Fail-safe: legi output-ul de `STATUS`; cand STATUS=OPRIT, lantul nu mai livreaza rezultatul corupt.
15. `_GUVERNARE` arata exceptia + momentul opririi + starea, FARA camp "cine raspunde" (asta e C20).

**Etapa 6:**
16. Plantezi mai multe deviatii previzibile intr-un set de intrare (una respinsa, una de prag, una exceptie).
17. Rulezi fara sa intervii ("ochii inchisi"): validarea respinge, pragul semnaleaza, exceptia opreste, fara tine.
18. Citesti `_GUVERNARE` la final: starea si jurnalul arata exact ce s-a prins; sistemul s-a tinut corect singur.

---

## ARC DEMONSTRATIV EXCEL
Arc continuu, filmabil, exact pe lantul cerut in mandat:

`input gresit` (etapa 1: intrarea proasta trece tacut) -> `regula` (etapa 3: Data Validation o respinge la sursa) -> `prag / stare` (etapa 4: pragul aprinde ATENTIE, `STATUS` se schimba) -> `exceptie` (etapa 5: cazul neprevazut marcat in lista de exceptii) -> `oprire controlata` (etapa 5: fail-safe leaga output-ul de STATUS=OPRIT, rezultatul corupt nu curge) -> `testul ochilor inchisi` (etapa 6: autorul pleaca, regulile prind singure).

Etapa 2 (judecata deviatiilor previzibile) e fundatia care alimenteaza tot arcul (defineste plicurile / pragurile). **PASS arc:** spectatorul vede CE regula prinde greseala si CUM sistemul se tine corect fara ochiul omului. **FAIL arc:** dashboard decorativ citit de un om (T4), om care verifica (babysitting), doar "ruleaza" fara sa prinda (C18), sau "trimite la responsabil" (C20).

---

## GRANITE SI GARZI
**Formula de paza:** C18 = **ruleaza** · C19 = **se tine corect** · C20 = **preda responsabilitatea**. Tinuta pe toate cele 6 etape.

- **Granita jos C18:** etapele NU construiesc / optimizeaza motorul; presupun un motor dat si ii pun garzile. `_AUTOMATIZARE` (C18) declara explicit "nu praguri / validari / alerte (C19)"; C19 le primeste ca identitate.
- **Granita sus C20 (cea mai pazita, etapa 5):** zero responsabil, zero escaladare la persoana, zero owner. `_GUVERNARE` marcheaza / opreste / schimba starea, dar NU desemneaza pe cine. Semnalul striga "atentie"; cui si cine raspunde = C20.
- **Anti-babysitting (etapele 1, 3, 6):** regula prinde, nu ochiul. "Testul ochilor inchisi" e proba ca autorul pleaca.
- **Anti-T4 (etapa 4):** semnalul ACTIONEAZA (schimba starea, opreste), nu e un panou de citit pentru un om care decide.
- **Anti-C04:** obiect = regulile care tin corect un sistem care ruleaza, nu actualizarea unui set (Refresh).
- C19 NU este (verificat etapa cu etapa): management · responsabil · escaladare umana · dashboard decorativ · monitorizare zilnica · QA generic · audit clasic · `motor` ca identitate C19 · ownership · delegare · persoana care verifica.

---

## RISCURI
1. **Etapele 4 si 5 sunt zona de alunecare** spre T4 (dashboard) sau C20 (escaladare). Pazite explicit: semnalul actioneaza (nu doar afiseaza); oprirea e fail-safe automat fara responsabil. La generare, garda se tine in chiar textul pasilor.
2. **MOTTO template T5** ramane CANDIDAT (carry-over, neblocant pentru blueprint).
3. **Titluri de pasi specifice, nu generice** (lectia "titluri exec identice 8/8"): cele 18 sunt scrise pe axa CONTROL, distincte de C17/C18; de pastrat asa la generare.
4. **Severitatea (etapa 2, pas 6)** "ce opreste lantul" trebuie sa ramana decizie de REGULA, nu de om; la generare, fail-safe-ul se leaga de `STATUS`, nu de o interventie.
5. Branch de sesiune divergent fata de main (sesiuni paralele C17/C18/C20 active); scris + commitat pe main aliniat, un singur fisier exclusiv C19.

---

## CERERI CATRE BRAIN / SYSTEM
- **Catre BRAIN:** confirmi Blueprint-ul conceptual C19 (6 etape / 18 pasi / arc)? La confirmare -> pasul urmator = generarea celor 7 artefacte (creare folder `c19/`, HTML / Date_MASTER `_GUVERNARE` / FILM etc.), DOAR la mandat explicit care ridica interdictiile operationale curente.
- **Catre BRAIN / SYSTEM (semnalat, nu executat):** ratificarea template-ului de treapta T5 pentru MOTTO ramane deschisa (la lock = CERERE SYSTEM pe Doc 14). Neblocant pentru blueprint.
- **CERERE SYSTEM pentru C19 acum:** niciuna. Blueprint-ul conceptual nu atinge fisiere sistem; artefactul `_GUVERNARE` deja confirmat in Doc 14.

---

## COMMIT
Commit descriptiv pe `main`: `docs(c19): Blueprint conceptual GUVERNAREA (MANDAT_BLUEPRINT_CONCEPTUAL) - 6 etape / 18 pasi / arc`. SHA vizibil in `git log` pe main.

**C19_BLUEPRINT_CONCEPTUAL_READY_FOR_REVIEW**
