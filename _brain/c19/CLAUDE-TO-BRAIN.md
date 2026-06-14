# CLAUDE -> BRAIN C19

## STATUS
C19_GENERARE_BLOCATA_B1_CERERE_SYSTEM (mandat de generare primit si acceptat; generarea NU a inceput; `pre_generation_check.py 19` da BLOCAJ B1 / R-V03.55 = SPEC C19 NEGENERAT in registrul de sistem; fisierul e `_system/**`, interzis chatului C19; ridic CERERE SYSTEM, nu fortez peste gate blocant)

SURSA: comanda `sync`. Mandat activ pe origin/main = `MANDAT_GENERARE_C19` (commit 168767e), cu interdictii operationale ridicate pentru `c19/`. Realiniat la origin/main (168767e). Am verificat tooling-ul + registrul inainte de generare. Atins DOAR acest fisier. Zero folder c19/ / artefacte / fisier sistem.

---

## ARTEFACTE GENERATE
**NICIUNUL.** Folder `c19/` NU creat. Cele 7 artefacte NU generate.
Motiv: gate-ul pre-flight B1 (regula BLOCANTA din CLAUDE.md) blocheaza generarea. B1: "Nu generezi o constructie fara SPEC inghetat. Daca lipseste -> BLOCHEAZA + cere ARHITECT sa inghete SPEC." Scriptul `pre_generation_check.py` cere explicit: "DUPA inghetare SPEC in SISTEM_TRAINITY.md, ruleaza din nou acest script". Precedent identic in aceasta sesiune: C18 a ridicat CERERE SYSTEM pe acelasi blocaj B1 (commit 975e563).

---

## SURSA COPY+MODIFY (identificata, raportata cum cere mandatul)
Am analizat sursele. **Sursa potrivita stabilita de sistem pentru constructiile T5 recente NU e HTML-ul raw `c01/`, ci pattern-ul build-script din `c17/`** (sibling T5 generat 6/6 azi):
- `c17/build_html_studiu_c17.py` (43 KB), `build_html_video_c17.py`, `build_html_editor_studiu_c17.py`, `build_html_editor_video_c17.py`, `build_date_master_c17.py`, `build_film_c17.py`.
- Motiv: C17 e T5, sora directa a C19, generata cu scripturi locale care injecteaza identitatea + cele 6 etape/18 pasi + foaia artefact (`_SISTEM` la C17 -> `_GUVERNARE` la C19). `c01/` ramane referinta canonica de fallback (HTML mare, model T1). C17-pattern = COPY+MODIFY corect pentru axa CONTROL.
- Plan: la deblocare B1, citesc scripturile c17, le adaptez la GUVERNARE (scriu `c19/build_*_c19.py`), le rulez, generez cele 7 artefacte. NU inventez structura noua.

---

## IDENTITATE C19 IMPLEMENTATA
Neimplementata inca (blocaj B1). Toate sloturile locked sunt pregatite verbatim (din mandat) si gata de injectat. **Completez aici cele 2 sub-elemente SPEC care lipseau** din cele 9 cerute de `pre_generation_check` (ca inghetul de sistem sa fie complet):

**PROMPTURI (2 Copilot, axa CONTROL, fara responsabil/escaladare):**
1. "Pentru coloana [X], listeaza valorile / intervalul permis si genereaza o regula de Data Validation care RESPINGE intrarile in afara plicului la sursa, fara sa corecteze automat valoarea."
2. "Pe baza [tabel], propune praguri (min / max) pentru [masura]; marcheaza ce abatere aprinde ATENTIE si ce eroare grava trece STATUS in OPRIT si opreste lantul, fara sa desemnezi un responsabil."

**FINAL-LABELS (8 ancore de retentie, axa CONTROL):**
1. "Regula prinde, nu ochiul."
2. "Prag, semnal, stare."
3. "OK / ATENTIE / OPRIT."
4. "Respins la sursa."
5. "Exceptia nu trece tacut."
6. "Fail-safe opreste lantul."
7. "Marcheaza, nu desemneaza."
8. "Testul ochilor inchisi."

Restul celor 9 elemente sunt deja in SPEC-ul frozen (versiunea FREEZE din istoricul acestui fisier): INTRIGA (HERO + BOMBA), PROBLEMELE (6), MIZA, MANTRA, MOTTO, STEP-TITLES (6 etape / 18 pasi), FENOMENE (5).

---

## DATE_MASTER / _GUVERNARE
Neconstruit inca (blocaj B1). Schema planificata (de implementat la deblocare, conform mandatului sectiunea 5):
- foaie `_GUVERNARE` distincta de `_AUTOMATIZARE` (C18);
- `STATUS` OK / ATENTIE / OPRIT (formula IFS pe praguri);
- Data Validation la sursa (interval / lista / custom pe `LIMIT_`);
- praguri vii `LIMIT_MIN` / `LIMIT_MAX`;
- lista de exceptii (IFERROR / IFS + log);
- fail-safe automat: output legat de `STATUS=OPRIT`, ca rezultatul corupt sa nu curga;
- R-V02.14: suma conservata fata de C18, verificata explicit la generare (citesc valoarea de iesire din `Date_MASTER-C18` cand exista; daca C18 nu are inca Date_MASTER, raportez si folosesc valoarea cap-coada din lant).

---

## VALIDARI RULATE
- **`pre_generation_check.py 19`: RULAT -> BLOCAJ.** R-V03.55: "SPEC C19 ESTE NEGENERAT". Cauza fizica: `_system/arhiva/SISTEM_TRAINITY-versiuni.md`, linia 2976: `## SPEC C19 - GUVERNAREA   [Status: NEGENERAT]` (la fel C17 si C18, toate NEGENERAT in acest fisier). Fix = `_system/**`, interzis chatului C19 -> CERERE SYSTEM.

---

## VALIDARI NERULATE / PROBLEME
Toate NU_RULAT, fiindca nu exista inca artefacte (blocate de B1 inainte de generare):
- `gate_v20.py 19 ...` = NU_RULAT (fara artefacte canonice).
- `audit_sync.py` post-generare = NU_RULAT.
- verificare zero em / en dash pe artefacte = NU_RULAT.
- `_GUVERNARE` distinct de `_AUTOMATIZARE` = NU_RULAT.
- `STATUS` OK/ATENTIE/OPRIT, Data Validation, fail-safe = NU_RULAT.
- R-V02.14 suma conservata = NU_RULAT.
- imagini hash != c01 = NU_RULAT (imaginile finale GUVERNARE nu exista; vezi RISCURI).
(Nu declar PASS pentru niciuna, conform mandatului.)

---

## RISCURI RAMASE
1. **B1 (blocant, activ):** SPEC C19 neinregistrat in registrul de sistem. Pana la deblocare, generarea nu poate trece pre-flight-ul.
2. **B2 anticipat:** chiar dupa B1, `gate_v20` ar putea cere ajustari de sistem (C17 a raportat B2 = CERERE SYSTEM). De verificat la prima rulare post-generare.
3. **Imagini:** cele 7 imagini finale `GUVERNARE` (hero + 6 exec-stage) sunt produse extern de ARHITECT. Fara ele, generarea ar folosi fallback draft (clone c01 / placeholder) = NU release complet (per mandat). De marcat draft explicit la generare.
4. **MOTTO template T5** = CANDIDAT (neblocant).
5. Branch de sesiune divergent fata de main; scris + commitat pe main aliniat, un singur fisier exclusiv C19.

---

## CERERI CATRE BRAIN / SYSTEM

CERERE SYSTEM
Constructie: C19
Fisier comun cerut: `_system/arhiva/SISTEM_TRAINITY-versiuni.md` (linia 2976; eventual oglinda in `constructii.xlsx` / `00-INDEX`, ca la freeze-ul C17).
Motiv: `pre_generation_check.py 19` (B1, R-V03.55) blocheaza generarea: `## SPEC C19 - GUVERNAREA [Status: NEGENERAT]`. SPEC-ul e inghetat si acceptat in `_brain/c19/` (SEED -> SPEC 11-slot FROZEN -> Blueprint -> readiness, toate acceptate de BRAIN), dar neinregistrat in registrul narativ de sistem pe care il citeste scriptul.
Impact: schimba statusul SPEC C19 din NEGENERAT in INGHETAT si adauga cele 9 elemente narative (INTRIGA, PROBLEMELE, MIZA, MANTRA, MOTTO, STEP-TITLES x18, PROMPTURI x2, FINAL-LABELS x8, FENOMENE), ca B1 sa treaca la re-rulare. NU atinge alte constructii.
Propunere: in sectiunea "## SPEC C19 - GUVERNAREA", aplica statusul + cele 9 elemente, toate disponibile gata-formulate in acest fisier (`_brain/c19/CLAUDE-TO-BRAIN.md`: versiunea FREEZE pentru sloturi + sectiunea IDENTITATE de mai sus pentru PROMPTURI / FINAL-LABELS). Mirror exact procedura de la C17 (commit FREEZE SPEC C17).

**Catre BRAIN (decizie ceruta):** aleg intre
- (a) **rezolvi CERERE SYSTEM** (chat SYSTEM inghetata SPEC C19 in registru) -> la urmatorul `sync` rulez `pre_generation_check 19` din nou, trece B1, si generez imediat cele 7 artefacte (build-pattern c17 adaptat); **recomandat** (respecta B1, consistent cu C18); SAU
- (b) **autorizezi explicit generarea draft peste B1** (precedent C17): generez artefactele cu pre_generation_check marcat BLOCAJ + imagini draft, fara declarare release complet. Spune clar daca vrei asta, fiindca incalca litera B1.

---

## COMMIT
Commit descriptiv pe `main`: `docs(c19): generare BLOCATA la B1 (SPEC C19 NEGENERAT in registru) - CERERE SYSTEM + sursa c17-pattern + PROMPTURI/FINAL-LABELS`. SHA vizibil in `git log` pe main.

**C19_GENERARE_BLOCATA_B1_CERERE_SYSTEM**
