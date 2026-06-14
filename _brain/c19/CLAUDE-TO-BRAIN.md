# CLAUDE -> BRAIN C19

## STATUS
C19_READY_FOR_GENERATION_MANDATE (readiness conceptual PASS pe cele 3 niveluri: SEED + SPEC frozen + Blueprint acceptate; generarea efectiva NEINCEPUTA, asteapta mandat explicit + dependentele listate, in special cele 7 imagini si conservarea sumei)

SURSA: comanda `sync`. Mandat activ pe origin/main = `MANDAT_PREGATIRE_GENERARE` (commit 09c30a0). Realiniat la origin/main (09c30a0). Acesta NU e mandat de generare; raport de pregatire. Atins DOAR acest fisier. Zero folder c19/ / HTML / Date_MASTER / FILM / build / fisier sistem / alta constructie.

---

## READINESS GENERARE C19
Cele 3 niveluri conceptuale, cu dovada (status-urile de mandat de pe main):

- **Nivel 1 - SEED:** ACCEPTAT (`C19_SEED_CONCEPTUAL_ACCEPTAT_PROVIZORIU`, apoi consolidat). Dovada: mandat `MANDAT_SPEC_11_SLOT` (aprobari BRAIN).
- **Nivel 2 - SPEC 11-slot:** FROZEN ACCEPTAT (`C19_SPEC_11_SLOT_FROZEN_ACCEPTAT`). Cele **9 elemente SPEC obligatorii (regula B1)** sunt TOATE prezente, deci `pre_generation_check` e satisfiabil:
  SLUG (`guvernare`) · INTRIGA (HERO + BOMBA) · PROBLEMELE (6) · MIZA · MANTRA · WOW · MOTTO · FENOMENE (5) · STEP-TITLES (6). Plus AHA + GRESEALA (sloturi suplimentare).
- **Nivel 3 - Blueprint conceptual:** ACCEPTAT (`C19_BLUEPRINT_CONCEPTUAL_ACCEPTAT`). 6 etape locked / 18 pasi / arc demonstrativ.

**Verdict readiness:** C19 e **pregatit conceptual** pentru un mandat de generare. Cele 3 niveluri sunt inchise. NU raportez gate_v20 / audit_sync ca PASS acum, fiindca nu exista inca artefacte de validat; ele sunt pasi de rulat LA generare (vezi checklist). Readiness = pe conceptie, nu pe livrabile.

---

## CHECKLIST MANDAT GENERARE VIITOARE
(De inclus intr-un mandat viitor de generare; cele cerute de BRAIN + invariantele de sistem.)

**A. Setup**
- [ ] Creeaza folder `c19/` DOAR la mandat explicit de generare (COPY+MODIFY din `c01/` = referinta; `_template/` nu mai exista, V46).
- [ ] Cele **7 artefacte canonice livrate IMPREUNA** (R-V01.2): HTML-Studiu, HTML-Editor-Studiu, HTML-Video, HTML-Editor-Video, `Date_MASTER-C19.xlsx`, FILM, `assets/` (hero + 6 exec-stage).

**B. Identitatea C19 (din Blueprint)**
- [ ] `_GUVERNARE` distinct vizibil de `_AUTOMATIZARE` (C18).
- [ ] Include `STATUS` OK / ATENTIE / OPRIT (formula, nu manual).
- [ ] Include Data Validation la sursa (interval / lista / custom pe `LIMIT_`).
- [ ] Include praguri vii (`LIMIT_MIN` / `LIMIT_MAX`, formule).
- [ ] Include lista de exceptii (IFERROR / IFS + log).
- [ ] Include fail-safe automat (output legat de `STATUS=OPRIT`).
- [ ] Etapa 4 = semnal care SCHIMBA STAREA, nu dashboard decorativ.
- [ ] Etapa 5 = oprire AUTOMATA, fara interventie umana, **zero responsabil / owner / escaladare**.
- [ ] Arcul Excel: `input gresit -> regula -> prag / stare -> exceptie -> oprire controlata -> testul ochilor inchisi`.
- [ ] Titluri exec-stage SPECIFICE axei CONTROL (nu identice 8/8 - lectia L mostenita).

**C. Invariante de sistem (B2 / B3 + reguli)**
- [ ] `pre_generation_check.py 19` (cele 3 checks HARD) inainte de generare (B1).
- [ ] `gate_v20.py 19 ...` PASS pe canonic + editat (B2).
- [ ] `audit_sync.py` ZERO DRIFT post-generare (B3).
- [ ] R-V02.15: zero cifre business in HTML / FILM (cifrele traiesc in Excel; inclusiv foaia `_README` / meta, lectia L186).
- [ ] R-V02.14: suma conservata - valoarea de intrare in `Date_MASTER-C19` continua valoarea de iesire a C18.
- [ ] R-V59 imgclone: cele 7 imagini cu hash != c01 (nu clone).
- [ ] R-V03.72: zero em-dash / en-dash in toate textele.
- [ ] R-V49.1: watermark Gemini scos cu `strip_watermark.py` pe orice imagine.
- [ ] Model de afisare hero V69: MIZA HERO `GUVERNAREA SISTEMULUI PRIN REGULI` in `hov-object` (fara Hero Word mare central).
- [ ] Companion files (Editor-Studiu / Editor-Video) sincronizate DUPA stabilizarea bazei (BRAIN-016).
- [ ] LIVRARE HTML-Studiu catre ARHITECT (SendUserFile) ca ultima actiune.

---

## RISCURI DE GENERARE (de pazit in mandatul de generare)
- **Contaminare C18:** motor / executie / lant ca IDENTITATE C19. Garda: C19 pune garzi PESTE un motor DAT, nu-l construieste; `_AUTOMATIZARE` ramane al C18; "motor" doar callback.
- **Contaminare C20:** responsabil / owner / escaladare / RACI / "trimite la X". Garda etapa 5: `_GUVERNARE` marcheaza / opreste / schimba starea, NU desemneaza pe cine.
- **Contaminare T4 dashboard:** semnalul devine panou de citit pentru un om care decide. Garda etapa 4: semnalul ACTIONEAZA (schimba `STATUS`, opreste).
- **Contaminare C04 refresh:** "validez datele la actualizare / Apas Refresh". Garda: reguli care tin corect un SISTEM care ruleaza, nu actualizarea unui SET.
- **Babysitting / monitorizare zilnica:** "ma uit pe el zilnic". Garda: testul ochilor inchisi; regula prinde, nu ochiul.
- **QA generic / audit clasic:** lectie de proces uman de verificare. Garda: garzile sunt NATIVE Excel (Data Validation / praguri / fail-safe), nu un rol de QA.
- **`motor` ca identitate C19:** vezi C18. Garda: CUVANT LOCKED C19 = CONTROL, nu MOTOR.
- **(sistem) imgclone / cifre business / suma neconservata:** vezi checklist C.

---

## BLOCAJE / DEPENDENTE
1. **Cele 7 imagini C19** (hero `GUVERNARE` + 6 exec-stage pe axa CONTROL: input respins / prag-semnal / stare OK-ATENTIE-OPRIT / exceptie / oprire controlata / testul ochilor inchisi) = produse EXTERN de ARHITECT (Banana), procesate aici (watermark scos, base64 inline). **Dependenta reala pentru RELEASE PASS COMPLET** (precedent C06/C07/C08); fara ele, generarea pleaca cu imagini clonate c01 (L202) si nu e completa. NEBLOCANTA pentru a INCEPE generarea HTML/text, blocanta pentru inchidere.
2. **R-V02.14 suma conservata:** valoarea de intrare `Date_MASTER-C19` trebuie sa continue iesirea C18; de coordonat cu starea `Date_MASTER-C18` la generare (C18 e LOCKED conceptual, dar verific valoarea la generare).
3. **MOTTO template T5 = CANDIDAT.** Instanta C19 "Pleci, si munca se tine singura." e stabila pe CONTINUT si se poate genera asa; lock-ul template-ului de treapta T5 e decizie separata (CERERE SYSTEM pe Doc 14). NEBLOCANT pentru generarea C19.
4. **NU e blocaj:** C18 nefinalizat ca artefacte - handoff-ul C18 -> C19 e NARATIV; fiecare cNN e self-contained in folderul lui.

---

## CERERI CATRE BRAIN / SYSTEM
- **Catre BRAIN:** la mandatul de generare, ridica EXPLICIT interdictiile operationale curente (folder `c19/`, HTML, Excel, FILM, build) si confirma sursa COPY+MODIFY = `c01/`.
- **Catre ARHITECT:** cele 7 imagini `GUVERNARE` (hero + 6 exec-stage) - le produci extern; eu le procesez (watermark scos, base64 inline, hash != c01) in ciclul de generare.
- **Catre SYSTEM (semnalat):** ratificarea template-ului MOTTO T5 (Doc 14, CANDIDAT -> LOCKED) ramane deschisa la nivel de treapta; o duc ca CERERE SYSTEM cand se decide.
- **CERERE SYSTEM acum:** niciuna.

---

## COMMIT
Commit descriptiv pe `main`: `docs(c19): raport readiness generare GUVERNAREA (MANDAT_PREGATIRE_GENERARE) - checklist + riscuri + dependente`. SHA vizibil in `git log` pe main.

**C19_READY_FOR_GENERATION_MANDATE**
