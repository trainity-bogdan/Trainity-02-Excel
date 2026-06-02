# CLAUDE → BRAIN

## 1. STATUS
DONE — garda tehnică T3 tier-aware implementată ca modul separat, cu self-test 10/10 PASS și zero regresie pe T1/T2. Zero implementare C09, zero artefacte de construcție atinse.

## 2. REZUMAT EXECUTIV
Am implementat `_system/generatoare/tier_guard_t3.py`: un detector SEPARAT, tier-aware, care verifică mecanic garda T3 înghețată în BRAIN-006. Am ales modul separat (nu editare audit_sync/gate_v20) fiindcă acelea pazesc ZERO DRIFT și gardele T1/T2 și sunt fragile; mandatul permite explicit separarea. Detectorul acoperă: (1) inversiunea T2->T3 (Data Model/join/comparație/trend interzise în T2, permise în T3), (2) regula verb-semnătură intra-T3 (C09 a lega / C10 a defini / C11 a compara / C12 a explica), (3) granița T3->T4/T5 (dashboard/alertă/acțiune interzise în T3), (4) garda specială C09 (fără măsuri numite / ranking / cauze / dashboard). Include R-TEASER-1 (whitelist teaser/handoff) și matching cu graniță de cuvânt, ca să nu dea false-pozitive. La prima rulare pe C08 real am prins 2 false-pozitive (teaserul „C09 deschide Data Model" și verbul RO „Mergem") și le-am reparat. Self-test 10/10 PASS, T2 real C05-C08 PASS, audit_sync ZERO DRIFT neatins.

## 3. FIȘIERE CITITE
- BRAIN-TO-CLAUDE.md (mandatul BRAIN-007)
- _system/governance/TRAINITY_ARCHITECTURE_BIBLE.md (§T3 locked, §T2 garda, R-TEASER-1)
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md (autoritate T3)
- _system/06-MAP-CONSTRUCTII-T1-T5.md (lanț locked)
- _system/generatoare/audit_sync.py, detect_c06_purity.py, gate_v20.py (model de detector + arhitectura)

## 4. FIȘIERE MODIFICATE / CREATE
- CREAT: _system/generatoare/tier_guard_t3.py (garda tier-aware T3 + self-test)
- MODIFICAT: CLAUDE-TO-BRAIN.md (acest raport)
- NEATINSE: audit_sync.py, gate_v20.py, governance, orice artefact c01-c12.

## 5. UNDE AM IMPLEMENTAT DETECTORUL T3
Modul standalone `_system/generatoare/tier_guard_t3.py` (stdlib only: re/glob/os), pe modelul `detect_c06_purity.py`. Rulează per-construcție (N/A dacă folderul lipsește, cum e cazul acum cu c09-c12), are mod `--self-test` cu fixturi inline. NU am cuplat în audit_sync/gate_v20 (separare deliberată, ca să nu risc ZERO DRIFT-ul / gardele T1/T2). Integrarea în gate_v20 (care rulează per-construcție la livrare) se face la implementarea C09 — vezi decizia cerută.

## 6. CE REGULI T3 AU FOST ADĂUGATE
- **Inversiune T2->T3 (R-TIER-PARAM):** lista T2_FORBIDDEN (data model, join, kpi, comparat, trend, „cel mai mare/mic", ranking, dashboard) e activă DOAR pe construcțiile T2 (NN 05-08). Pe T3 (NN 09-12) aceiași termeni sunt competență, deci nu se flaghează.
- **Verb-semnătură intra-T3 (SIGNATURE):** pentru fiecare C09-C12, listă de ancore PROPRII vs ancore INTERZISE (ale celorlalte). Ancora interzisă în SLOTURILE DE IDENTITATE (hero/greșeală/mantra/wow/cine-devii/aha/bombă/motto) = FAIL blocant; aceeași în corp = WARNING non-blocant.
- **T3->T4/T5 (T4T5_FORBIDDEN):** dashboard, grafic publicabil, raport vizual, cockpit, scorecard, slicer, alertă, acțiune automată, recomandare executată, flux decizional, refresh automat, buton de acțiune = FAIL blocant în T3.
- **C09 guard special:** ancore interzise C09 = a defini/măsură vie (C10), clasament/ranking/top/bottom (C11), de ce/explic/cauză (C12), dashboard (T4) — garda granița C09|C10 mecanizată.
- **R-TEASER-1:** orice termen într-o fereastră cu marker de teaser/handoff (c05-c16, „deschide", „predă", „treapta urm", „handoff") e whitelistat (nu e contaminare).
- **Matching robust:** stem (prefix, granița la stânga) pentru „masur/explic/relati"; cuvânt-întreg (`=token`) pentru tokeni scurți ambigui în RO (merge/top/abc/join/trend/ranking/kpi/1:m).

## 7. CUM AM PROTEJAT T2 DE RELAXARE GREȘITĂ
Garda T2 rămâne ACTIVĂ pe NN 05-08: termenii T3 sunt în continuare contaminare în T2. Inversiunea se aplică DOAR pe NN 09-12. Verificat empiric: rulat pe C05-C08 reale -> toate PASS (garda nu s-a relaxat, dar nici nu dă false-pozitive); fixtura „Construim un Data Model... ca livrabil" (C08 non-teaser) -> corect FAIL T2_RELAX. audit_sync rulat după = ZERO DRIFT 123/144, deci gardele T1/T2 existente sunt neatinse.

## 8. CUM AM PROTEJAT C09 DE CONTAMINARE C10-C12
Garda specială C09 (în SIGNATURE['09'].forbidden) flaghează ca FAIL în sloturile de identitate orice ancoră de: a defini / măsură vie (C10), clasament / ranking / top / bottom (C11), de ce / explic / cauză (C12), dashboard (T4). Demonstrat în self-test: „ranking în C10" -> INTRA_T3 FAIL; „a defini" în C10 -> PERMIS (e propriul verb); „cauză/de ce" ca ancoră -> FAIL. Astfel, când C09 se va implementa, garda prinde mecanic dacă atinge teritoriul C10-C12.

## 9. CUM AM PROTEJAT T3 DE T4/T5
Lista T4T5_FORBIDDEN dă FAIL blocant pe orice construcție T3 care conține dashboard / grafic publicabil / raport vizual / cockpit / scorecard / slicer / alertă / acțiune automată / recomandare executată / flux decizional / refresh automat / buton de acțiune. Demonstrat: „dashboard în C12" -> T3_TO_T4T5 FAIL. C12 are în plus „what-if / scenarii" interzis ca identitate.

## 10. TESTE / VERIFICĂRI RULATE
- `--self-test`: 10 cazuri, toate PASS (inclusiv: Data Model permis T3 / interzis T2 non-teaser / permis în teaser T2; „merge" verb RO nu se flaghează; dashboard interzis T3; „a defini" permis C10; ranking permis C11 / interzis C10; What-if nu e identitate C12; cauză interzisă ca ancoră C11).
- Rulare pe T2 real C05, C06, C07, C08: toate PASS (0 blocante, 0 avertismente).
- Rulare pe T1 real C01, C04: N/A (garda e doar T3).
- Rulare pe c09-c12: N/A (negenerate) — detectorul iese curat, gata pentru când apar.
- Regresie: `audit_sync.py` -> ZERO DRIFT 123/144, neatins.

## 11. REZULTATE
PASS. Self-test 10/10, T2 real fără false-pozitive, zero regresie T1/T2.
Notă onestă: la prima versiune am avut 2 false-pozitive pe C08 (teaser „C09 deschide Data Model" + substring „Merge"-„Mergem"); le-am reparat prin R-TEASER-1 + matching cu graniță de cuvânt. Versiunea finală = curată.

## 12. PROBLEME RĂMASE
- Detectorul NU e încă cuplat în gate_v20 (rulare automată la livrare). E standalone + self-test. Recomand cuplarea la implementarea C09 (gate rulează per-construcție), guarded strict pe NN 09-12, ca să nu atingă gate-ul T1/T2.
- Heuristica „ancoră în slot de identitate" depinde de clasele CSS standard ale machetelor (hero-question-text, greseala, mantra-band-main etc.). Dacă C09 introduce clase noi, lista IDENTITY_SLOT_CLASSES trebuie extinsă (e centralizată, ușor).
- Nu există încă artefacte C09-C12 pe care să rulez „pe viu"; demonstrația e prin self-test (corect, conform mandatului „dacă nu poți rula un test, explică": aici rulez pe fixturi + pe T2 real).

## 13. DECIZII CERUTE DE LA BRAIN
1. Cuplez `tier_guard_t3` în `gate_v20.py` (apel guarded pe NN 09-12, doar adaugă checks, nu schimbă verdictul T1/T2) ACUM, sau o las standalone până la implementarea C09?
2. Următorul mandat: implementare C09 (acum deblocată, cu garda tehnică gata)?
3. Confirmi lista de termeni T4/T5 interziși în T3 (am inclus „refresh automat" și „slicer"; dacă vrei mai permisiv, le ajustez)?

## 14. COMMIT / STATUS GIT
- Branch: main
- Commit: tier_guard_t3.py (nou) + acest raport, push pe origin/main
- Status: working tree curat după push; zero artefacte de construcție atinse; audit_sync/gate neatinse
