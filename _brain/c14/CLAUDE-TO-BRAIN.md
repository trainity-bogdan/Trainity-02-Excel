# CLAUDE -> BRAIN · C14 READY FOR GENERATION CHECK

## STATUS
CLAUDE_C14_READY_FOR_GENERATION_CHECK_READY
Conceptual / planificare exclusiv. Zero implementare, zero artefacte, zero c14/**, generare NEPORNITĂ. Nu am accesat în acest pas: c01/, generatoare/gate, niciun fișier de sistem; nicio CERERE SYSTEM ridicată. Răspuns la `MANDAT_READY_FOR_GENERATION_CHECK`.

## STARE APROBATĂ (preluată din mandat, nu reinventată)
SEED + SPEC 11 SLOT + BLUEPRINT + SPEC COMPLET = aprobate. SLUG provizoriu `compunerea`. MOTTO final: "Ce vede ochiul întâi schimbă decizia." AHA "Aceleași grafice, altă ordine, altă decizie." Mantra "Compun privirea, nu pagina." STEP-TITLES = cele 11 sloturi.

Acest raport spune CE trebuie autorizat înainte de generare. Baza de cunoaștere = CLAUDE.md + Doc 13 T4 (citite). Ce nu am citit încă e marcat explicit (necesar la generare).

---

## 1. Fișiere / foldere care trebuie citite înainte de generare
**Deja citite în sesiune:** CLAUDE.md; `_brain/c14/CHAT-CONTEXT.md`; `_brain/c14/BRAIN-TO-CLAUDE.md`; `_system/NOMENCLATURA-LOCKED-SCARA.md`; `_system/13-ARHITECTURA-CONCEPTUALA-T4.md` (în special §STARE: livrabil per construcție + dashboard XLSX la C13); `_system/governance/TRAINITY_ARCHITECTURE_BIBLE.md` §T4; SPEC COMPLET C14 (în CLAUDE-TO-BRAIN.md).
**NECITITE încă, necesare la generare (de autorizat):**
- `_system/04-ARHITECTURA-LIVRABILE.md` (schema exactă a celor 7 artefacte)
- `_system/05-WORKFLOW-PER-SCENARIU.md` (workflow generare pas cu pas)
- `_system/08-PROCEDURA-GENERARE-VALIDARE.md` (procedura + validări)
- `_system/10-MAP-FILM-HTML.md` (maparea FILM <-> HTML)
- `_system/COMENZI.yaml` (intrarea `genereaza_constructie`)
- `c01/` integral (referință COPY+MODIFY)

## 2. Ce se poate folosi din `c01/` ca COPY+MODIFY
Per CLAUDE.md, c01 = construcția-cobai, referința unică de COPY+MODIFY. La generare se copiază SCHELETUL, nu conținutul:
- structura celor 4 HTML: `HTML-Studiu`, `HTML-Editor-Studiu`, `HTML-Video`, `HTML-Editor-Video` (base64 inline)
- structura `Date_MASTER-CNN.xlsx` (schema, nu cifrele)
- structura `FILM`
- convenția `assets/`: `hero-poster-excel-14-{slug}.jpg` + `exec-stage-1..6.jpg` (jpg, 3:2 cinematic)
- modelul de afișare pe 2 straturi (NOMENCLATURA): topbar `C14 · COMPOZIȚIE`, hero `COMPUNEREA`, navigare cuvinte T4, titlu articol „Cum să…"
NU se copiază: cifrele, textul, imaginile C01 (imaginile sunt DIFERITE per construcție). Conținutul vine din SPEC COMPLET C14.
Flag: nu am accesat `c01/` (interzis acum), deci descriu din CLAUDE.md; structura empirică se confirmă la generare.

## 3. Ce generatoare / gate-uri trebuie accesate
- `_system/generatoare/pre_generation_check.py 14` (B1: cele 3 checks HARD pre-generare)
- `_system/generatoare/gate_v20.py 14 <dir> <pilot_dir>` (B2: GATE V20 PASS pe canonic + editat, pre-livrare)
- `_system/generatoare/audit_sync.py` (B3: AUDIT ZERO DRIFT post-modificare)
- `_system/generatoare/strip_watermark.py` (R-V49.1: curățare watermark Gemini înainte de a pune imaginile în assets/)
- eventual `_system/generatoare/patch_runner.py` (doar dacă se aplică patch-uri prin rețetă)
Acestea se RULEAZĂ și se CITESC, NU se modifică. Nu le-am accesat în acest pas (interzis).

## 4. Ce fișiere se vor putea modifica la generare
Doar `c14/**`, cele 7 artefacte canonice (R-V01.2 LIVRARE TOATE ODATĂ):
1. `c14/HTML-Studiu`
2. `c14/HTML-Editor-Studiu`
3. `c14/HTML-Video`
4. `c14/HTML-Editor-Video`
5. `c14/Date_MASTER-C14.xlsx`
6. `c14/FILM`
7. `c14/assets/` (`hero-poster-excel-14-{slug}.jpg` + `exec-stage-1..6.jpg`)
Plus, ca raportare: `_brain/c14/CLAUDE-TO-BRAIN.md`.

## 5. Ce fișiere sunt interzise
Per CHAT-CONTEXT C14, NU se modifică: toate celelalte `cNN/**`; alte `_brain/cYY/**`; `CLAUDE.md`; `README.md`; `STARE-CURENTA.md`; `index.html`; `_system/**`; `governance/**`; `constructii.xlsx`; codul generatoarelor/gate; `COMENZI.yaml`; orice fișier global/sistem.
Nuanță: `_system/generatoare/*.py` și `c01/` se CITESC/RULEAZĂ la generare (cu autorizare în mandatul de generare), dar NU se MODIFICĂ.

## 6. Este sau nu nevoie de CERERE SYSTEM?
- Pentru **generarea artefactelor `c14/**`** (COPY+MODIFY din c01, rulare generatoare existente): **NU e nevoie de CERERE SYSTEM** — nu se modifică niciun fișier comun/sistem.
- Pentru **integrarea globală post-generare** (înregistrarea C14 în `index.html`, `constructii.xlsx`, `STARE-CURENTA.md`, eventual un doc `_system`): **DA, CERERE SYSTEM separată** către chat-ul SYSTEM. C14 produce doar `c14/**` + raport; integrarea globală nu e treaba C14.
- Caz posibil de CERERE SYSTEM și la generare: dacă `Date_MASTER-C14.xlsx` cere o schemă de dashboard XLSX care depinde de o decizie de sistem sau de output-ul C13 (vezi riscul de la pct. 7).

## 7. Riscuri finale înainte de generare
- **B1 (SPEC înghețat):** SPEC complet C14 aprobat (9 elemente). De confirmat HARD prin `pre_generation_check.py 14` la generare.
- **Suprapunere C13/C14 pe XLSX:** Doc 13 §STARE spune că dashboard XLSX se introduce la C13. De clarificat ce conține `Date_MASTER-C14`: moștenește dashboard-ul C13? îl extinde cu compoziția/ierarhia? doar îl referențiază? Risc real de suprapunere de substrat. DE DECIS înainte de generare.
- **Dependența de output C13:** obiectele vizuale oneste vin de la C13. C13 e „pre-generation ready" (per commit-urile recente), dar NU generat. Dacă C13 nu e generat/stabil, C14 nu are input vizual coerent. De confirmat ordinea.
- **Garduri la autorarea HTML/FILM:** dashboard doar substrat (nu identitate); fără mesaj (C15); fără livrare decision-ready (C16); fără estetică; fără redesenarea obiectului (C13).
- **R-V02.15 ZERO CIFRE BUSINESS:** în HTML/FILM doar referințe generice; cifrele trăiesc în Excel.
- **R-V02.14 SUMĂ CONSERVATĂ:** valoarea netă cap-coadă; `Date_MASTER-C14` trebuie să continue lanțul (input de la C13).
- **Imagini:** hero + 6 exec-stage se produc extern (ARHITECT); watermark Gemini curățat cu `strip_watermark.py`. Dacă imaginile nu sunt furnizate la generare, generarea vizuală e blocată parțial. Flag.
- **SLUG provizoriu `compunerea`:** de confirmat definitiv înainte de a fixa numele fișierelor din assets.

---

## CERERE DE DECIZIE PENTRU BRAIN
- Confirmi lista de autorizări (pct. 1-4) pentru mandatul de generare?
- Decizia pe `Date_MASTER-C14` vs dashboard-ul C13 (pct. 7, suprapunere XLSX) — esențială înainte de generare.
- Confirmi ordinea: C13 generat înainte de C14 (input vizual), sau C14 se generează cu obiecte-placeholder?
- La aprobare, mandatul de generare trebuie să ridice explicit interdicțiile din acest pas: acces citire `c01/` + `_system/04,05,08,10` + `COMENZI.yaml`, rulare `pre_generation_check / gate_v20 / audit_sync / strip_watermark`.
