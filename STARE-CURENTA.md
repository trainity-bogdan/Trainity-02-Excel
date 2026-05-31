# Stare curentă Trainity · Pack 02 Excel

**Versiune sistem:** V54 (consolidat · marker SHA în `_system/VERSIUNI.md`)
**Ultima actualizare:** 31 mai 2026

**Sesiunea V54 — sumar (C05 copy ascuțit prin G-06 + fix gate cover-title legacy):**

1. **Feedback extern pe C05 → G-06 → aplicat** (confirmat ARHITECT): hook „Tabelul este curat. Dar știm ce conține?" (tensiune, callback C01-04 „curat"); **WOW nou cu slot `payoff-wow` + `data-wow`** „Setul nu mai este o masă de date. Acum are hartă." (C05 nu avea slot WOW vizibil în modelul V44; l-am adăugat cu CSS din C01, badge verde); MIZA reframe spre teritoriu enumerabil; exec-slide 1/4/6 reformulate (slide 4 fără nume de funcții: COUNTUNIQUE/COUNTIF → „Sistemul decide"); fix drift `payoff-motto` (zicea „Mai întâi structura. Apoi orice." din C01) → motto corect C05 în slot. Mantra/motto/slide 2/3/5 = NEUTRU, păstrate. Propagat FILM (master) → 4 machete, round-trip consistent.
2. **Notă poziționare C05 în `06-MAP`:** C01-04 răspund „pot avea încredere în set?"; C05 răspunde „știu ce există în el?" (poarta T2, teritoriu cartografiat, nu etichete izolate).
3. **Fix `gate_v20.py` (stil L176 — detector conștient de redesign):** checkul legacy IDENTITY cerea slug-ul caps articulat (DICȚIONARUL etc.) în `cover-title`, dar V42 a făcut titlurile descriptive libere („Cum construim X" / „Cum dăm sens fiecărui rând" — C06 nici nu conține slug-ul). Identitatea rămâne garantată de `cover-label` (CONSTRUCȚIA CNN) + footer + meta; anti-clonă narativă = audit_sync R-V03.69. Acum verificăm doar că `cover-title` există și nu e gol. **Deblochează GATE PASS pe C05-C08** (aveau toate aceeași presupunere stale de la V42). Premium C01-C04 neatins (ramura hero-overlay separată).
4. **Git (L174 în practică):** „unrelated histories" la merge era cu `main` LOCAL (lineage orfan V45, rămas după un force-push pe remote), NU cu `origin/main` real. `origin/main` (10aef81) împărțea strămoșul `57be5d2` cu branch-ul de sesiune. Merge cu munca paralelă (C04 exec-stage-1, zero conflicte — foldere disjuncte) → FF pe main `10aef81..b805920`. **L181:** după force-push pe remote, `main` local poate rămâne pe un lineage orfan; ținta corectă de merge e `origin/main` (post-fetch), nu `main` local.
5. **L182:** verificarea anti-regresie după un fix de script (am rulat gate pe C01-C04 ca să confirm că fix-ul legacy nu rupe premium) e OK; săparea în cauzele unor FAIL-uri pre-existente, neînrudite de task, și raportarea lor = scope creep. Confirm doar „nu vine din schimbarea mea", apoi mă opresc.

Audit ZERO DRIFT 88/88. Gate C05-C08 PASS. Zero em/en-dash, nesting balansat.

---

**Sesiunea V53 — sumar (card MIZA cu chenar + shadow, propagat C01-C04):**

1. **Card `.cover-miza`** (cerere ARHITECT): textul MIZA din modelul premium HTML-Studiu, transformat din linie cu border-top (V47) în **card alb cu chenar + colțuri rotunjite 10px + accent galben Trainity 4px pe stânga + shadow dublu**. Îl ridică de pe pagină ca element-cheie. Aplicat **C01-C04** (Studiu + Editor-Studiu, 8 fișiere). Verificat randat (C01 + C03). Audit ZERO DRIFT 88/88.
2. **Documentat** în `_system/07-BRAND-OPERATIONAL.md` → „Componente vizuale signature" (specificația CSS completă + notă propagare C05-C08).
3. De propagat la C05-C08 odată cu modelul premium (T2 încă pe model vechi).

---

**Sesiunea V52 — sumar (C02 finalizat: premium + business G-06 + imagini exec + FILM sync + verificat randat):**

1. **C02 = model premium complet** (Studiu + Editor-Studiu): hero cockpit imagine-obiect CONTROL + system-map MARCARE activ + arc TU (bombă „Pare curat. Datele mint." → SUNĂ CUNOSCUT → GREȘEALA „marchează întâi" → AHA → CINE DEVII) + before/after + outcomes + transformare gated. Eliminat exec-hero DE CE + CONTRACT.
2. **Tensiune business (feedback extern → G-06 SIGUR, confirmat ARHITECT):** MIZA strategică (risc KPI/dashboard/decizie), „Minciuna produsă" calitativ pe cele 5 anomalii (fără cifre — garda R-V02.15 + granița C02/C03 respectată), AHA „Valid nu înseamnă adevărat", WOW „Raportul nu mai înghite minciuna. O marchează." Aplicat pe 4 machete (WOW slot data-wow) + FILM sync.
3. **TOATE cele 6 imagini exec-stage C02 dedicate** generate de ARHITECT (REALITATE/INVESTIGAȚIE/TRANSFORMARE/VERIFICARE/STABILIZARE/CONFIRMARE), procesate singur: extras din transcript jsonl, watermark Gemini scos (exec-1/2/3/6 reparate prin clonare verticală — colțul lor e pe fundal deschis, `strip_watermark` presupune fundal întunecat: L179), integrate base64 în HTML-Video (verificat: a N-a imagine == fișierul exec-stage-N). exec-6 = folder CONTROLAT + VALIDAT + handoff la C03. **C02 = 6/6 imagini exec proprii + hero-poster dedicate.**
4. **FILM C02 sync** (R-V46 FILM=master): MIZA + WOW vechi → noi în .docx (text într-un singur run, înlocuire sigură).
5. **`PROMPTURI-SLIDES-EXEC-C02.txt`** creat (cele 6 verbatim din Creativ) + livrat ARHITECT.
6. **VERIFICAT RANDAT** (L178 aplicat): C02 Studiu randat 393px + 1280px — hero, arc TU, „minciuna produsă", outcomes, mantra toate corecte. Audit ZERO DRIFT 88/88, nesting 0 pe toate 4 machete.
7. **L179 (nou):** `strip_watermark.py` eșuează când colțul dreapta-jos al imaginii e pe fundal DESCHIS (hârtie/lumină), nu întunecat — `detect_sparkle` prinde o casetă prea mare și lasă o pată gri. Fix: clonare verticală dintr-o bandă imediat deasupra casetei steluței (textură continuă), casetă fixă. De integrat în strip_watermark ca fallback când zona-țintă e luminoasă.

**C02 = MODEL FINALIZAT COMPLET** (a doua construcție 100% gata după C01): premium + business G-06 + 6/6 imagini exec dedicate + hero + FILM sync + verificat randat. Nimic deschis pe C02. **L180:** consolidarea pe STARE-CURENTA poate fi suprascrisă de un merge paralel — verific persistența post-merge și re-aplic dacă a fost înlocuită.

---

**Sesiunea V51 — sumar (C03 model premium + hero forensic + rescope C03/C04 + bullet canonic + prompturi exec):**

1. **C03 = model premium propagat** (Studiu + Editor-Studiu): hero cockpit cu imagine-obiect forensic dedicată + overlay „AUDIT" + system-map (AUDIT activ); arc TU pe axa forensic — bombă „Arată curat. Nu este." → SUNĂ CUNOSCUT → GREȘEALA „Oamenii curăță ce se vede. Profesioniștii auditează ce nu se vede." → AHA → CINE DEVII „Nu mai vezi date curate. Vezi date neauditate." → before/after + outcomes. Video/Editor-Video neatinse (modelul premium NU atinge Video — confirmat empiric: C01 și C03 Video structural identice, zero markeri premium). Eliminat exec-hero DE CE + CONTRACT (paritate C01).
2. **L178 — RANDAREA FUNCȚIONEAZĂ în containerul Web** (corectează presupunerea V47/V48/L175 că „Playwright nu e instalat"). Chromium + Playwright trăiesc în `/opt/node22/lib/node_modules/playwright`; rulez `node` cu `require(PW+'/index.js')` → screenshot la 393px (mobil) + 1280px (desktop). „NEVERIFICAT randat" nu mai e scuză — verific ÎNTOTDEAUNA înainte de livrare. C03 premium verificat randat integral.
3. **R-V03.72 nou (detector + regulă):** zero em/en-dash ORIUNDE (text, CSS `content:`, comentarii JS/CSS) + bullet `.tu-list` canonic `\2022` (•) IDENTIC în toate construcțiile. Curățat C01 (en-dash bullet + comentariu CSS) + 4× Editor-Video (em-dash în comentariu JS: c01,c02,c03,c05). C01 = C02 = C03 bullet `•`. **Audit 80 → 88** (11 detectoare × 8).
4. **Hero-poster forensic C03** generat de ARHITECT, procesat singur (extras din transcript jsonl, watermark Gemini scos cu `strip_watermark.py` per R-V49.1, base64) și integrat în hero Studiu+Editor-Studiu. Salvat `c03/assets/hero-poster-excel-03-auditare.jpg`. Numere lizibile în poză = textură fotografică (precedent C02 aprobat de ARHITECT; R-V02.15 vizează callout-uri de date HTML, nu fotografii).
5. **Feedback extern → G-06 → ascuțire C03** (confirmat ARHITECT: rescope + titlu + da FILM): titlu „Cum auditezi ce nu se vede în date" (era „audit valoric", contabil/vag); miză mai dură („formulele, rapoartele și AI-ul lucrează pe o minciună tehnică"); „Datele nu mai mint" → „nu mai ascund defecte" (diferențiere de C02 operațional); prompt 1 scurtat pentru cursant.
6. **RESCOPE C03/C04 (cel mai important):** C03 revendica „flux refreshabil... la fiecare export nou" (etapa 3 TRANSFORMARE, etapa 5 STABILIZARE pașii 13-15, prompt 2, outcomes, exec-slide 5 Video, prompturile imagine) = teritoriul C04. Corectat: **C03 = demonstrează + audit + dovadă + conservare; auditul = repetabil ca VERIFICARE** (îl re-rulezi pe export nou ca să confirmi); **C04 = mecanismul permanent refreshabil**. Toate mențiunile „refreshabil" rămase atribuie EXPLICIT mecanismul lui C04. Propagat în 4 machete + FILM (sursă) + Creativ (prompturi imagine etapa 3+5) + notă graniță anti-redrift în 06-MAP.
7. **`PROMPTURI-SLIDES-EXEC-C03.txt`** creat (cele 6 prompturi exec-stage într-un singur fișier, format ca C02, aliniate rescope) + livrat ARHITECT.
8. ⚠️ **PENDING — POZELE C03 NEGENERATE:** cele 6 imagini **exec-stage C03 sunt încă clone byte-identice cu C01** (scenă generică „monitor + Excel + legendă forme" + watermark Gemini) — NU universul forensic C03. Prompturile sunt gata (fișierul de la pct. 7). De generat în Banana → strip watermark → integrare base64 în HTML-Video + Editor-Video → salvare assets. Opțional negenerate: `infografic` (nefolosit în modelul premium, 0 referințe în Studiu) + `cover-yt` (thumbnail YouTube, extern HTML). **Singura imagine C03 dedicată generată până acum = hero-poster.**

---

**Sesiunea V50 — sumar (propagare model premium C01 → C04 cap-coadă):**

1. **C04 = a doua construcție cu model premium V47** (după C01). Grefat pe HTML-Studiu + HTML-Editor-Studiu: hero cockpit (imagine-obiect NORMALIZARE inline base64 + cuvânt overlay + întrebare + hartă treaptă), arcul TU (BOMBA „Fișierul curat nu e rezultatul. Fluxul este." → RECUNOAȘTERE → GREȘEALA → AHA → CINE DEVII), before/after, outcomes. Scos `exec-hero DE CE` + `CONTRACT` (ca la C01 V47). CSS premium injectat scoped (L173). Paritate structurală cu C01.
2. **Metodă propagare premium (L175):** grefă, nu COPY+MODIFY. Delta premium = doar regiunea hero+arc + CSS (~5KB markup; restul „greutate" C01 = imaginea hero base64). Stadii/scenă/final/payoff C04 păstrate. Video + Editor-Video NU primesc premium (V47 = doar Studiu, verificat: C01 Video are 0 clase premium).
3. **Imagini Banana dedicate C04 — COMPLET (6/6):** hero-normalizare.jpg (buclă conducte flux) + cele 6 exec-stage (etape 01-06, toate dedicate, zero clone C01). Watermark Gemini scos automat (R-V49.1, `strip_watermark.py` cu auto-detecție corner-only).
4. **FILM C04** dus spre Biblia: + ARC TRANSFORMARE + FORMULA finală + notă video Prompt 2.
5. **Feedback extern G-06 (tot SIGUR) aplicat:** marker „CEI 10 PAȘI...", precizie dedup (scos „fuzzy" — Table.Distinct = dedup exact), final „Refresh. Aceeași ordine.", framing „activ".
6. **Fix sistem — gate v20 conștient de premium (L176):** checkul IDENTITY cerea cover-label + slug în titlu, ambele eliminate de V47 → C01 ȘI C04 picau. Acum: detectează hero-overlay (premium) → verifică identitatea în hero-overlay + topbar + footer; altfel legacy (cover-label) pentru C05-C08. C04 GATE PASS complet.
7. **Lecție L177 — imaginile lipite în chat SUNT accesibile** prin transcriptul sesiunii (`~/.claude/projects/.../<session>.jsonl`, bloc `type:"image"`, `source.data`). Nu mai spun „nu pot accesa imaginea". Procedat la fel ca sesiunea C02.
8. **Audit ZERO DRIFT 88/88 · Gate v20 C04 PASS.** Toate pe `main`.

---

**Sesiunea V49 — sumar (reguli git workflow + start lucru paralel multi-sesiune):**

1. **Regulă nouă — MERGE ÎN MAIN = MEREU MOTORUL, NICIODATĂ ARHITECT.** Codificată în 3 locuri în CLAUDE.md (regula absolută din cap + G1 + „consolideaza brain"). La finalul fiecărei sesiuni / fiecărui set de modificări, motorul face OBLIGATORIU `fetch → merge --ff-only (sau normal) → push origin main`, fără să întrebe. Permisiune durabilă.
2. **Regulă nouă — FĂRĂ TAG-URI GIT (G3 rescris, ABANDONAT).** Push de tag dă 403 din proxy-ul Web. Nu mai folosesc tag-uri, nu mai scriu NICIODATĂ despre ele ARHITECTULUI, nu dau comenzi de push tag. Versionarea oficială = commit descriptiv pe `main` + STARE-CURENTA. Curățat tot CLAUDE.md (comanda `tag V{N}` ștearsă, restore fără `v{N}`, sumar disciplină actualizat).
3. **Context nou — LUCRU PARALEL MULTI-SESIUNE.** ARHITECT va deschide mai multe construcții simultan pe sesiuni Claude Code on Web diferite (branch-uri `claude/<task>` paralele). Fiecare sesiune face merge în `main` la final. Construcțiile trăiesc în foldere separate `cNN/` → conflicte de merge rare (doar pe fișiere partajate: STARE-CURENTA, CLAUDE.md, `_system/`, `index.html`). Vezi L174.
4. **Propagat modelul premium C01 → C02** (prima din seria C02-C08), pe machetele **Studiu + Editor-Studiu** (Video/Editor-Video au structură frag, NU primesc modelul premium — confirmat empiric pe C01). Aplicat: hero cockpit (imagine-obiect `hero-poster-excel-02-control.jpg` cu overlay „CONTROL" + system-map MARCARE activ), intro-top, bombă „Pare curat. / Datele mint.", arc TU (SUNĂ CUNOSCUT → GREȘEALA „marchează întâi" → AHA „o anomalie ștearsă e o dovadă pierdută" → CINE DEVII „le pui sub control"), before/after, outcomes, transformare-section gated „DUPĂ C02 POȚI + DE ACUM ÎNAINTE". Eliminat exec-hero „DE CE" + CONTRACT (redundante, ca la C01). Nesting valid, audit ZERO DRIFT 80/80. NEVERIFICAT randat (container web fără browser — vezi L175).

---

**Sesiunea V48 — sumar (fix CSS leak C01 = box DUPĂ negru cu text invizibil):**

1. **Bug raportat de ARHITECT:** în secțiunea „DOVADA TRANSFORMĂRII" (pasul 9, lista ÎNAINTE→DUPĂ), box-urile DUPĂ apăreau negre cu text invizibil pe HTML-Studiu C01.
2. **Cauza:** la redesignul hero V47, regulile blocului `.hero-beforeafter` au fost scrise cu selectori BARE (`.ba-after{background:#0a0a0a}`, `.ba-before{background:#fff}`, `.ba-arrow{...}`, `.ba-*  .ba-label{...}`) în loc de scoped `.hero-beforeafter .ba-*`. Clasa `.ba-after`/`.ba-before` e refolosită și de lista DOVADA din pași → fundalul devenea negru, dar textul `.ba-val` rămânea `color:var(--k)` (negru) → invizibil.
3. **Fix:** încadrat toate regulile leak în `.hero-beforeafter` (backgrounds, `.ba-label` colors, `.ba-arrow` + `::after`). Aplicat în ambele machete afectate: `HTML-Studiu` + `HTML-Editor-Studiu`. DOVADA revine la verde/roșu-deschis (liniile 773/1266) cu text negru vizibil; săgeata revine la galben simplu.
4. **Audit ZERO DRIFT** menținut (80/80 PASS). Playwright nu e instalat în containerul Web — verificare prin analiza cascadei CSS (nu randată).
5. **L173 (nou):** vezi mai jos.

**Notă propagare:** același pattern de leak ar apărea în C02-C08 DOAR dacă moștenesc blocul hero V47 — dar redesignul premium e încă nepropagat (doar C01 model finalizat). La propagare C02-C08 se folosește varianta corectată (scoped).

---

**Sesiunea V47 — sumar (redesign experiență C01 = model premium validat):**

1. **HERO COCKPIT** (poster + cockpit coexistă în ecranul 1): imagine-obiect generată (schelă STRUCTURĂ) cu cuvântul-obiect uriaș overlay + întrebarea construcției + bandă cockpit (hartă simplificată pe cele 4 din T1). Topbar păstrat. Fără buton/cover-meta în poster (orientarea rămâne în topbar+hartă).
2. **ARC DE TRANSFORMARE A CURSANTULUI, cu DOUĂ VOCI simțite (fără etichete):** voce TU (fundal închis, persoana a II-a) vs voce DATE (deschis, tehnic). Ordine: titlu+micro-brief+miză → **BOMBA „Arată ca tabel. Nu este unul."** (memoria de 24h) → RECUNOAȘTERE → GREȘEALA → AHA (vârf) → CINE DEVII → demonstrația (date+pași) → DUPĂ C01 POȚI + DE ACUM ÎNAINTE (gated).
3. **Bookend identitate:** CINE DEVII (promisiune vizibilă, după AHA) + DE ACUM ÎNAINTE (confirmare gated la final), ecou pe prima frază.
4. **Ierarhie 3-1-1:** o singură idee dominantă (bomba) + un singur vârf intelectual (AHA). Restul = suport.
5. **FILM C01 = Biblia (SPEC v2.0, 4 secțiuni)** completă: IDENTITATE / ARSENAL / BRIEF / TRANSFORMARE + CINE DEVII.
6. **Metodă nouă (L171):** instalat **randator headless (Chromium/Playwright)** — orice schimbare vizuală se verifică randată mobil (393px) + desktop (1280px) ÎNAINTE de livrare. Gata cu „lucrul orb" care a spart mobilul de 2 ori.
7. **L172:** designul se face prin **scădere + concentrare** (3-1-1: o idee, o memorie), nu prin adăugare de carduri. Două transformări (date vs cursant) separate prin fundal/ton/persoană, NU prin etichete textuale.

**C01 = MODEL FINALIZAT (V47):** coerență (eliminat `exec-hero „DE CE"` + `CONTRACT`, redundante cu arcul) + cleanup CSS mort complet (**99 reguli orfane** eliminate: exec-hero*, arsenal vechi, cover-meta*, hero-competency, hero-start, cover-label* etc., ~6KB/fișier), detecție JS-aware (clasele runtime `.visible`/`.done`/`.frag-in` păstrate), verificat randat 2 stări (fresh pixel-identic + completat identic). C01 e curat și gata de propagare. **Rămas deschis:** (a) propagare model C02-C08 (copy per beat + imagine-obiect per construcție); (b) sync FILM↔HTML C05-C08; (c) opțional cosmetic: unire blocuri `<style>`.

---

**Sesiunea V46 — sumar (sincronizare FILM↔HTML + sloturi noi):**

1. **Mapare canonică FILM → HTML codificată** în `_system/10-MAP-FILM-HTML.md` (nu exista document care să spună ce frază de impact din FILM merge în ce slot HTML). FILM = MASTER. „update html" devine mecanic: INTRIGA→cover-subtitle+hero-hook · MIZA→cover-miza · MANTRA→mantra-band-main · MOTTO→payoff-motto+final-motto+exec-closing · STARE/FRAZĂ exec→exec-emotion/exec-phrase ×6.
2. **Slot nou WOW**: linie-climax verbatim înainte de motto, highlight VERDE `.payoff-wow` (#18843e) + etichetă `WOW:`. Fraza în `<span data-wow>` (sync atinge doar fraza). Video = frag propriu + renumerotare motto. Adăugat C01-C04.
3. **Slot nou CONTRACT (DESTINAȚIE)** în cusătura SCENA REALĂ → primul pas (`exec-hero [data-contract]`, Studiu). Element NOU în SPEC, copy DRAFT (de formalizat în FILM + propagat în C02-C20).
4. **Sincronizări complete C01-C04** (identitate + 6 exec slides + WOW + CONTRACT, 4 machete fiecare). C01 rezolvat prin sync HTML←FILM (a reparat și confuzia de rol mantra/motto). C03+C04 FILM repo = docx reparat (voce „noi", fără conflict V45).
5. **Diacritice reparate** în FILM C02 + C03 + C04 (docx returnate ARHITECT): typo „.." + ~160-180 corecturi fiecare.
6. **Lecție L169:** C01 nu era „special" tehnic — era singura construcție fără FILM proaspăt trimis de ARHITECT, deci FILM-repo (vechi) ≠ HTML (șlefuit) fără arbitru. Rezolvare: aplici regula FILM=master uniform.
7. **C01 VALIDAT (închidere fir):** ARHITECT a trimis ulterior FILM-ul C01 → **byte-identic** cu cel din repo + identitatea confirmă fix valorile sincronizate (MOTTO „Nu reconstruim tabelul. Îl facem controlabil." etc.). Sync-ul HTML←FILM a fost corect, zero pierderi. Diacritice curate. **L170:** când sync-ul precede primirea FILM-ului, validarea ulterioară (diff FILM↔HTML) confirmă corectitudinea fără re-muncă.

**Deschis:** (a) formalizare copy CONTRACT în FILM-SPEC + propagare în C05-C20; (b) sync FILM↔HTML pentru C05-C08 (la primirea FILM-urilor sau la cerere).

---

**Ultima sesiune V45 — sumar:**

Re-arhitectură T2 (după feedback extern trecut prin G-06) + rafinări ARHITECT:

1. **Re-arhitectura C05/C06** (suprapunere rezolvată): **C05 CLASIFICARE → DICȚIONAR** (rename + fișiere Clasificare→Dictionar; conținut = inventar categorii) și **C06 CUANTIFICARE → CLASIFICARE** (REBUILD complet: dă sens fiecărui rând prin reguli — clasa ABC cu IFS, segment cu SWITCH, etichetă externă cu XLOOKUP, regulă compusă, scor 0-100). Aici apare Excel-ul de construit care lipsea din T2. Date_MASTER-C06 cu coloane derivate clasa_valoare/segment_produs/scor.
2. **Cele 4 obiecte T2 acum complet distincte:** DICȚIONAR (ce reprezintă) · CLASIFICARE (cum capătă sens) · MEMORIE (cum evoluează) · ECOSISTEM (cum se conectează). Patru întrebări diferite.
3. **Garda T2/T3:** C06 atribuie etichete descriptiv; prioritizarea strategică pe segmente rămâne C11/T3.
4. **Rafinări** (filtru motor + ARHITECT): C07 voce impersonală „noi" + slide5 + fenomen TREND + F5 MEMORIA CICLICĂ + „Suma DELTA 0" scoasă din identitate; C08 MIZA cinematică + WOW „nu mai este singur" + F5 „LIMBI DIFERITE"; rol „CONTROL UMAN" (eliminat „operatorul") în toate 8 FILM-urile.
5. **Naming C08:** TIPIZARE → CARTOGRAFIERE. **G-06** codificat ca doc 09.
6. Meta-list `DICȚIONAR · CLASIFICARE · DATARE · CARTOGRAFIERE` propagată C05-C08. Audit **80/80 ZERO DRIFT**.

**Progresie pedagogică validată:** C05 descoperi → C06 construiești sens → C07 citești timpul → C08 citești relațiile.

---

**Sesiunea anterioară V44 — sumar:**

Sesiune T2 încheiat (C07 + C08) + procedură FILM-ca-sursă în practică + G-06 codificat:

1. **C07 DATARE / MEMORIA SETULUI generat** (T2, axa TEMPORALĂ unică, marker „memorie"). Date_MASTER-C07 cu _TIMELINE/_TREND/_RITM/_SEZON. Perioada iun 2025-mai 2026, 12 luni. Rafinat cu ARHITECT (voce impersonală „noi" în loc de „operatorul", slide 5 memorie↔refresh, fenomen TREND separat). Purge C06 din FILM (deschidere+fenomene+etape).
2. **C08 CARTOGRAFIERE / HARTA ECOSISTEMULUI generat** (T2, axa RELAȚIONALĂ DESCRIPTIVĂ, marker „ecosistem"). RECUNOAȘTERE, nu modelare (join/Data Model = C09). Date_MASTER-C08 cu _ECOSISTEM/_CHEI/_ROLURI/_CAMPURI_EXTERNE. Cartografiere reală: PRODUSE prin cod_produs, CLIENTI prin nume, AGENTI/DEPOZITE neconectate. Rafinat: motto „O hartă completă", F5 „LIMBI DIFERITE".
3. **Naming C08: TIPIZARE → CARTOGRAFIERE** (se potrivește cu obiectul ecosistem). Meta-list propagată C05-C08.
4. **Delimitare obsesivă C07/C08** lock în 06-MAP (după G-06): C07 = MEMORIA (timp), C08 = ECOSISTEM (recunoaștere). C08↔C09: C08 vezi relațiile posibile / C09 construiești relațiile reale. Cele 4 obiecte T2: dicționar/profil/memorie/ecosistem.
5. **G-06 FILTRU SIGUR/CONFLICT codificat** ca document activ `_system/09-FILTRU-G06-SIGUR-CONFLICT.md` (era doar referențiat în arhivă).
6. **T2 CUNOAȘTERE COMPLET** (C05-C08). Audit **10 detectoare × 8 = 80 PASS**. Toate live în index.html.

**T2 SCARA — cele 4 obiecte narative:** dicționar (C05) · profil numeric (C06) · memorie (C07) · ecosistem (C08).

---

**Sesiunea anterioară V43 — sumar:**

Sesiune C06 + control de calitate pe machete + procedură FILM-ca-sursă:

1. **C06 CUANTIFICARE generat** (T2 CUNOAȘTERE, axa CANTITATIVĂ, marker „cifră"). 7 artefacte + assets. SPEC înghețat + IDENTITATE_TEHNICA populată (pre_generation_check 3/3). Date_MASTER-C06 cu coloana marja_estimata + sheet-uri KPI_GENERAL/_AGREGATE/_DISTRIBUTIE/_EXTREME/CONTROL_FINAL, sumă conservată 7.986.019,38 (DELTA 0). Live în index.html.
2. **Fix layout buton** continue-btn + scroll-top: erau ancorate la viewport (`right:var(--gutter)`), dar `.book-app` e max-width:1280px centrat → se desprindeau de sub side-nav la zoom/ecran lat. Fix: `right: calc((100% - min(100%,1280px))/2 + var(--gutter))`. Aplicat matriță + C01-C06 (Studiu+Editor-Studiu).
3. **Drift exec video reparat la sursă**: C03/C05 aveau exec-emotion = clonă C01; C05/C06 și exec-phrase = clonă C01 (moștenit prin COPY+MODIFY, neprins de R-V03.69 care citea doar Studiu). Rescrise pe axa fiecărei construcții.
4. **Detector nou R-V03.71 ANTI-CLONĂ EXEC VIDEO** (exec-phrase / exec-emotion / hero-sub, comparație pe tuplu complet). Audit acum **10 detectoare × 6 = 60 PASS**.
5. **Procedură nouă** `_system/08-PROCEDURA-GENERARE-VALIDARE.md`: manifest de conținut + injectare în matriță + pipeline 4 gate-uri + **workflow FILM-ca-sursă** (FILM = sursa de adevăr textuală; propagare în machete cu verificare round-trip).
6. **Secțiune SLIDES EXECUTIVE** adăugată în toate FILM-urile (matriță + C01-C06), după MOTTO: cele 6 slide-uri exec (STARE + FRAZĂ DE IMPACT).
7. **Set texte C06 rafinat** (ARHITECT + filtru motor): INTRIGA, MIZA (formă de dorință), WOW, MOTTO („Un profil cunoscut. Apoi orice decizie."), exec-phrase S2-S6. Aplicat FILM → 4 machete, round-trip PASS.

---

**Sesiunea anterioară V42 — sumar:**

Refactor masiv naming + UX editor + audit narativ + deploy live Pages:

1. **Naming -ARE peste tot** (T1+T2): denumiri scurte unifilament în filenames + titluri lungi „Cum construim X" în Hero. Schimbări vizibile:
   - C01 STRUCTURA → STRUCTURARE
   - C02 CONTROL → MARCARE (era CONTROL, descris corect ce face: marchează anomalii fără șterge)
   - C03 AUDIT → AUDITARE
   - C04 NORMALIZARE (rămâne)
   - C05 CLASIFICARE (rămâne)
   - Treaptele: SCAN → SCANARE; CARE → CUNOAȘTERE; ANALIZA → ANALIZARE
   - T2 plan: C06 CUANTIFICARE / C07 DATARE / C08 TIPIZARE (înlocuiește KPI/MEMORIA SETULUI/TIPARE TEMPORALE)
2. **Cover-meta restructurat în 4 rânduri**: DENUMIRE TREAPTĂ / CONSTRUCȚIILE TREPTEI (cu bold pe curentă) / CONSTRUCȚIE CURENTĂ / AI INTEGRAT. Aplicat în matriță Studiu+Editor-Studiu + propagat la c01-c05.
3. **Editor live editabil EXTINS** (V42 EDITABLE_SELECTORS): acum și mantra-band-main, cover-label, cover-subtitle, cover-meta-key/val, exec-hero-label/sharp, section-marker/sublabel, stage-label/quote, next-label/title/desc, payoff-line/motto, completion-title/subtitle. Aplicat matriță + c01-c05 Editor-Studiu.
4. **Video navigation tableta**: click stânga = prevFrag, click dreapta = nextFrag (split L/R). Combinat cu: click pe text = edit (browser default), click între texte = nav. Eliminat IIFE blockStageInteractions (era piedică pentru background clicks).
5. **Editor-Video tastatură fix critic** (V42 R-V03.70): Enter în mod edit crea newline (nu nextFrag), ArrowKeys mută cursor în text (nu schimbă slide). Folosit `stopImmediatePropagation` în CAPTURE phase pe document.keydown (stopPropagation simplu nu era suficient — nu oprește alte listeneri pe ACELAȘI nod). Plus walk manual prin parentNode pentru Text nodes fără closest. Aplicat matriță + propagat c01-c05.
6. **Reset video = hard refresh + cleanup**: `editorReset()` acum șterge cheile localStorage `trainity_*`, sessionStorage similar, apoi `location.replace(pathname + '?_=' + timestamp + hash)` cu cache-bust + entry curat în history. Plus recuperare c04 (lipseau editorExport + editorReset complet — drift preexistent).
7. **GitHub Pages activ**: repo trecut la public, workflow `.github/workflows/pages.yml` deploy automat la fiecare push pe main. URL live: `https://trainity-bogdan.github.io/Trainity-02-Excel/`. Dashboard index.html cu link-uri direct, toate cu `?v=2` cache-bust. Privacy: robots.txt + noindex meta pe toate paginile (nu sunt indexate Google).
8. **Audit narativ R-V03.69 ANTI-CLONĂ NARATIVĂ**: detector nou care prinde cazul când două cNN au liste titlare identice literal (inv-item-label, anomaly-title, final-label). Descoperit empiric drift c05 inv-list = clonă C01 (din generarea V28, neprins în 7 sesiuni). Fixat + detector permanent în audit_sync.py. Total audit: 9 detectori × 5 cNN = 45 verificări PASS.
9. **Assets PNG eliminate** (~40 MB economisit): doar JPG rămâne (lossless PNG inutil pentru fotografii foto-realistice Banana 2). Detector V39.assets actualizat la 6 jpg per folder.
10. **Banana 2 exec-stage C02**: aplicate primele 2 imagini dedicate (REALITATE, INVESTIGAȚIE) + fix prompt „future date" → „4 OCT 2036" (independent de când vede cursantul cursul).

**Regulile noi în CLAUDE.md** (V42):
- ⚠️ **REGULĂ ABSOLUTĂ:** LUCREZI MEREU PE `main`. NU CREEZI BRANCH-URI NOI. Excepție: ARHITECT cere EXPLICIT.
- **Întrebări în text liber**, NU în grile A/B/C cu AskUserQuestion.

**Reguli noi în 01-REGULI-ACTIVE.md**:
- **R-V03.69 ANTI-CLONĂ NARATIVĂ**: detector permanent în audit_sync
- **R-V03.70 STOP IMMEDIATE KEYDOWN ÎN EDIT**: pattern blockKeyboardInEditor (capture + stopImmediatePropagation)

---

**Ultima actualizare V41:** Fix responsive complet pe matrița HTML-Studiu (safe-area iPhone, breakpoint-uri 380px/landscape, a11y aria-expanded/keyboard) + **refactor invers OneDrive → git** (V40 a fost OneDrive, V41 revine la git ca singura sursă de versionare; reguli G1-G5 noi în CLAUDE.md)

---

## Construcții — status complet

| Cod | Nume | Versiune | Stare | Audit |
|-----|------|----------|-------|-------|
| **C01** | STRUCTURARE (cum construim o structură tabelară corectă) | V12 → V42 nume | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C02** | MARCARE (cum construim controlul anomaliilor de date) | V52 MODEL FINALIZAT (premium + business G-06 + 6/6 exec-stage dedicate + hero + FILM sync + verificat randat) | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C03** | AUDITARE (cum auditezi ce nu se vede în date) | V51: model premium + hero-poster forensic dedicat + rescope C03/C04 (audit≠mecanism permanent) | versiune unica · hero-poster generat; ⚠️ exec-stage 1-6 = clone C01 (forensic NEGENERAT) | ✓ ZERO DRIFT |
| **C04** | NORMALIZARE (model PREMIUM V50: hero cockpit + arc TU) | V50 premium · 6/6 exec dedicate + hero | versiune unica + assets/ + hero | ✓ ZERO DRIFT · GATE PASS |
| **C05** | DICȚIONAR (ce reprezintă datele — inventar categorii) | V54 (copy ascuțit G-06: hook/WOW/MIZA reframe + slot payoff-wow + exec-slides) | versiune unica + assets/ | ✓ ZERO DRIFT · GATE PASS |
| **C06** | CLASIFICARE (cum capătă sens datele — reguli IFS/SWITCH/XLOOKUP/scor) | V44 (rebuild din CUANTIFICARE) | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C07** | DATARE — MEMORIA SETULUI (axă temporală) | V44 | versiune unica + assets/ | ✓ ZERO DRIFT |
| **C08** | CARTOGRAFIERE — HARTA ECOSISTEMULUI (axă relațională descriptivă; închide T2) | V44 | versiune unica + assets/ | ✓ ZERO DRIFT |
| C09-C12 | (T3 ANALIZARE: CORELARE / COMPARARE / SEGMENTARE / PROIECTARE — draft) | — | NESTAR | — |
| C13-C16 | (T4 RAPORTARE: VIZUALIZARE / SINTETIZARE / NARARE / PUBLICARE — draft) | — | NESTAR | — |
| C17-C20 | (T5 AUTOMATIZARE: DECLANȘARE / PROGRAMARE / INTEGRARE / STANDARDIZARE — draft) | — | NESTAR | — |

**Progres: 8/20 (40%) livrate. T1 SCANARE complet + T2 CUNOAȘTERE complet (C05-C08).**

---

## Audit empiric (rulează `_system/generatoare/audit_sync.py`)

```
✓ 11 detectoare empirice × 8 construcții = 88 verificări PASS (R-V03.72 nou: anti em/en-dash + bullet canonic)
✓ ZERO DRIFT (versiune unică per cNN — git ține istoricul complet via log/tags/branches)
✓ Toate cele 7 artefacte + assets/ prezente per construcție
```

Detectori activi (V40):
- R-V03.60 cover-meta fără INPUT/OUTPUT
- R-V03.61 buton lipit responsive (`.nav-controls` fără `margin-top:auto`)
- R-V03.59 highlighter V34 (capture phase, fără buton, fără ESC)
- V32-fix zero referințe Date-Output/Input
- R-V03.33 imagini base64 inline în Video
- R-V03.47 cele 6 livrabile canonice
- R-V03.58 FILM.docx prezent
- R-V39.assets folder `assets/` cu 6 imagini exec-stage jpg (V41 update: eliminat PNG duplicate wasteful)
- R-V03.72 zero em/en-dash oriunde (text/CSS content/comentarii) + bullet `.tu-list` canonic `\2022` uniform în toate construcțiile (V50)

---

## Pe agenda imediată

1. ⚠️ **POZE C03 exec-stage 1-6 NEGENERATE** — clone C01 + watermark; prompturi gata în `c03/PROMPTURI-SLIDES-EXEC-C03.txt`. ARHITECT generează în Banana → motor strip watermark + base64 în Video/Editor-Video. (opțional: infografic + cover-yt C03)
2. ✓ **C04 COMPLET 100%** — exec-stage-1 (etapa 01 REALITATE) generat, watermark scos, re-inline în Video/Editor-Video. Toate 6 exec-stage + hero dedicate. Nimic rămas pe C04.
3. **Propagare model premium C05-C08** (C01-C04 făcute) — grefă hero+arc+CSS scoped + imagine-obiect per construcție + sync FILM. Gate v20 deja conștient de premium.
4. **Sync FILM↔HTML C05-C08** (la primirea/cererea FILM-urilor)
5. **Setup B2C landing pages live** (paralel)

---

## Sesiunea V41 (28 mai 2026) — Responsive matriță + refactor git

**Lucrări:**
1. **Fix responsive complet pe `_template/HTML-Studiu`** (matriță, NU propagat la C01-C05):
   - Critical: safe-area iPhone (notch + home indicator) pe mobile-topbar/side-nav/continue-btn/scroll-top, padding-uri intermediare 641-1024px (exec-hero, payoff-section), cover-meta-row tabletă (150px gutter), inv-item-status mobile pill, prompt-box mobile padding + `word-break: break-word`, stage-number `clamp(56-96px)` unificat
   - Medium: breakpoint `≤380px` (iPhone SE / Android budget) + continue-btn condensat sub 380px + landscape phone drawer
   - A11y: `aria-expanded` dinamic pe mobile-toggle + `aria-hidden` pe overlay + Escape închide drawer + focus management + `role=button` / `tabindex=0` / `aria-label` pe `.step-check` + keyboard support (Space/Enter)
   - Commit: `2a31f46` pe branch `claude/status-7j30w`, push reușit pe origin
2. **Refactor invers OneDrive → git** (V40 a fost greșit înțeles — ARHITECT folosește git, nu OneDrive):
   - CLAUDE.md: secțiunea „VERSIONARE ONEDRIVE + BACKUP DISCIPLINE" rescrisă ca „VERSIONARE GIT" cu regulile G1-G5
   - STARE-CURENTA, README, COMENZI.yaml, 00-INDEX, 01-REGULI, 02-GLOSAR, 03-COMENZI-OPERATIONALE, 04-ARHITECTURA-LIVRABILE, 05-WORKFLOW-PER-SCENARIU: rescrise referințele OneDrive
   - Reguli noi git (G1 branch-per-task, G2 commit descriptiv, G3 tag V{N} la increment, G4 restore git, G5 PR pentru schimbări sistemice) — au înlocuit V1/V2/V3 OneDrive

**L159 (nou):** Sistemul a oscilat două sesiuni la rând între GitHub și OneDrive (V40 a refactorizat spre OneDrive bazat pe presupunere; V41 revine la git pe confirmare directă din partea ARHITECT). **Regulă durabilă:** orice schimbare a workflow-ului de versionare se face DOAR pe confirmare scrisă explicită din partea ARHITECT, nu pe deducție din artefacte existente.

---

## Sesiunea de audit V40 (28 mai 2026)

Audit exhaustiv din partea ARHITECT. Findings prioritizate (14 total, 4 critical), fix-uri aplicate în Sesiunea 2.

**CRITICAL fixate:**
- **#1 audit_sync.py encoding bug** — `open(f)` fără `encoding='utf-8'` arunca `UnicodeDecodeError` pe HTML cu base64, captat silent de `except Exception` generic. 5/8 detectoare silent-fail-uiau pe Windows. Raport spunea "ZERO DRIFT" fals. **FIX:** adăugat `encoding='utf-8'`, raportare ERR explicită pe stderr, tracking distinct OK/XX/ERR în output.
- **#2 STARE-CURENTA cifre false** — "9 detectoare × 10 zone = 80 verificări PASS" era inventat. **FIX:** corectat la "8 × 5 = 40 verificări PASS" (real măsurat).
- **#3 pre_generation_check.py** — căuta `SISTEM_TRAINITY.md` eliminat la refactor V38. **FIX:** adăugate candidate paths pentru `_system/arhiva/SISTEM_TRAINITY-versiuni.md`.
- **#4 gate_v20.py print crash** — `'✓' (✓)` nu putea fi printat în cp1252 Windows console. **FIX:** `sys.stdout.reconfigure(encoding='utf-8')` la pornire.

**HIGH fixate:**
- **#5 04-ARHITECTURA-LIVRABILE.md** rewrite complet pentru V39 versiune unică (eliminat canonic/editat).
- **#6 COMENZI.yaml** rewrite — eliminate comenzile fără sens (refa_canonic, aplica_si_pe_canonic), simplificate restul.
- **#7 assets_canonice/** — eliminate referințele din 04-ARHITECTURA, 07-BRAND-OPERATIONAL, COMENZI.yaml (per construcție în V39, nu partajat).
- **#8 IDENTITATE-TEHNICA.md schema** — C01-C04 actualizate la `Date_MASTER-initial.xlsx` + `Date_MASTER-CNN.xlsx` (schema R-V03.47), aliniate cu C05.

**MEDIUM/LOW fixate:**
- **#9 c04/RAPORT-CONSTRUCTIE-C04.md** mutat în `_system/arhiva/RAPORT-CONSTRUCTIE-C04-V27.md`.
- **#11 README.md** data sincronizată.
- **#12 STARE-CURENTA detectori** — eliminat R-V03.62-c/e marker (nu se mai folosesc).
- **#13 .gitignore** — eliminat `*-Editat.html.bak` (convenție nume veche).

**Finding adițional V40 (REVOCAT în V41):**
- **#15 V40 a presupus că ARHITECT folosește OneDrive.** Presupunerea greșită — ARHITECT lucrează doar cu git. V41 a rescris înapoi toate docurile spre workflow git (vezi sesiunea V41 mai sus).

**Confirmate empiric PASS:**
- Zero em-dash (—), zero en-dash (–), zero vocab interzis în HTML-uri C01-C05
- 40/40 verificări audit_sync REAL PASS (post-fix)
- Gate v20 PASS pe C02 (testat post-fix)

---

## Reguli noi de la ultima sesiune (V38)

- **R-V03.62** PRIMA GENERARE ÎNGHEȚATĂ + PATCH OVER EDITED (V36 consolidat V37) — **ABSORBITĂ V39:** versiune unică, fără meta marker
- **R-V03.63** AUDIT EMPIRIC PERMANENT (V38)

Reguli existente, statusuri actuale: vezi `_system/01-REGULI-ACTIVE.md`.

---

## Lecții noi V36-V40

- **L154** Persistarea editorilor prin non-regenerare (V36)
- **L155** Punctarea permanentă a sincronizării prin audit empiric (V38)
- **L156** Audit infrastructure poate ascunde drift real prin exception silent capture — orice `except Exception:` fără raportare pe stderr e suspect. Toate scripturile de validare TREBUIE să raporteze ERR explicit, nu doar PASS/FAIL.
- **L157** Documentația sistemului poate diverge silent de realitatea pe disk la refactor (V38→V39 a lăsat 4 docs stale). La fiecare refactor structural, audit sync docs-vs-disk e obligatoriu.
- **L158** [REVOCAT în V41] V40 a presupus OneDrive bazat pe artefacte istorice (foldere `OUT-V{N}.zip`, lipsa `.gitignore` clar). Confirmare directă V41: ARHITECT folosește exclusiv git.
- **L159** Workflow-ul de versionare nu se schimbă pe deducție din artefacte. Doar pe confirmare scrisă explicită din partea ARHITECT. Două sesiuni consecutive au oscilat între GitHub și OneDrive pentru că am inferat în loc să întreb. **Regulă durabilă:** la orice schimbare de model (versionare, structură repo, convenție livrabile), motor întreabă ARHITECT direct înainte de a refactoriza docs.
- **L160** (V42) Drift narativ poate trăi luni în repo fără detectare dacă audit verifică doar structură + prezență CSS. Cazul empiric: c05 inv-list era clonă C01 literal de la V28 (7 sesiuni nedetectat). audit_sync.py verifica „6 jpg present", „CSS class X există", dar nu „lista titlară A == lista titlară B → DRIFT". **Regulă durabilă:** detectorii noi trebuie să acopere și COERENȚĂ SEMANTICĂ (nu doar prezență tehnică). Detector R-V03.69 ANTI-CLONĂ NARATIVĂ adăugat ca prevenție viitoare.
- **L161** (V42) `e.stopPropagation()` NU oprește alte event listenere de pe ACELAȘI nod. Doar oprește propagarea spre alte noduri (DOM tree). Pentru a opri și listener-ele bubble pe același nod (document) când e capture, folosesc `e.stopImmediatePropagation()`. Cauza descoperită empiric: blockKeyboardInEditor cu stopPropagation simplu nu opera Enter→nextFrag pentru că bubble handler-ul global pe document rula oricum. **Regulă durabilă:** când vrei blocare totală a unui event în fază capture pe nod cu multipli listenere (document), foloseşte stopImmediatePropagation, nu stopPropagation.

- **L162** (V43) Detectorii de coerență trebuie să acopere TOATE machetele, nu doar Studiu. Driftul exec video (C03/C05 exec-emotion = clonă C01, C05/C06 și exec-phrase) a trăit nedetectat pentru că R-V03.69 citea doar HTML-Studiu. **Regulă durabilă:** orice zonă de conținut construcție-specific (în oricare din cele 4 machete) primește detector de anti-clonă pe tuplu complet la introducere. R-V03.71 a extins acoperirea pe Video.
- **L163** (V43) COPY+MODIFY cu înlocuiri de string e fundamental leaky — moștenește literal orice zonă nemapată. **Regulă durabilă:** FILM-ul (.docx) e sursa de adevăr textuală; generarea = injectare manifest în matriță + propagare FILM→machete cu verificare round-trip, NU editare directă în 4 machete. Vezi `_system/08-PROCEDURA-GENERARE-VALIDARE.md`.

- **L164** (V44) Propagarea FILM trebuie să acopere TOT documentul, nu doar identitatea + creativ + slides exec. La C07, DESCHIDERE + SCENA REALĂ (fenomene) + OBIECTIVELE etapelor au rămas în axa veche (C06 numeric) după transform parțial. **Regulă durabilă:** transformul FILM include explicit DESCHIDERE, SCENA REALĂ (cele 5 fenomene), OBIECTIVE etape + scan final de markeri pe axa veche.
- **L165** (V44) `open(f,'w').write(open(f).read())` în Python TRUNCHIAZĂ fișierul (modul 'w') ÎNAINTE ca `open(f).read()` să citească → scrie gol. A golit 3 fișiere C08 (raportate „done", scanate „CLEAN" fiindcă erau goale). **Regulă durabilă:** CITEȘTE întâi într-o variabilă, apoi scrie; verifică dimensiunea fișierului (>0) după orice transform în masă.
- **L166** (V44) Coliziuni de ordine la înlocuiri: o regulă scurtă („Setul are memorie.") rulată înaintea uneia lungi care o conține îi sparge match-ul (instr18 a devenit Frankenstein). Plus numerele bare („Construcția 0X") nu sunt prinse de shift-ul de cod C0x. **Regulă durabilă:** înlocuirile lungi înaintea celor scurte (sau placeholdere); numerele bare de construcție se tratează explicit.

- **L167** (V45) G-06 nu înseamnă apărare rigidă a oricărei reguli înghețate. Când feedback-ul extern identifică un defect REAL într-o decizie înghețată de ARHITECT (ex. suprapunerea C05/C06 + nume/conținut nepotrivit la C05), clasificarea corectă e CONFLICT-condiționat: resping soluția care contrazice sistemul, dar prezint onest defectul și las ARHITECT să-și dezghețe propria regulă. Intelectual honesty > consistență. (Mi-am schimbat verdictul între două mesaje pe baza unui argument nou, nu a presiunii repetate.)
- **L168** (V45) Procedura de redenumire construcție: (a) replace stem filename repo-wide `Excel-NN-Vechi`→`Excel-NN-Nou` în toate fișierele text, (b) `git mv` fișierele, (c) rename DISPLAY separat (nume afișat în hero/meta/nav/title — atenție la protejarea meta-listei cu placeholder), (d) update C(N-1) next-pointer + index + IDENTITATE + gate dict. Verifică `git status` arată R (rename), nu D+A.

- **L173** (V48) CSS cu selectori BARE într-un bloc copiat/redesignat se scurge peste alte secțiuni care refolosesc aceleași clase. Cazul empiric: redesignul hero V47 a definit `.ba-after{background:#0a0a0a}` neîncadrat, iar lista DOVADA din pași (pasul 9) folosește aceeași clasă `.ba-after` → box negru cu text negru invizibil. A trăit o sesiune nedetectat (audit verifică structură+prezență, nu contrast/cascadă). **Regulă durabilă:** orice CSS component-specific se scrie ÎNTOTDEAUNA scoped la containerul lui (`.hero-beforeafter .ba-after`, nu `.ba-after`), mai ales când numele de clasă (ba-before/ba-after/ba-val/ba-arrow) sunt generice și refolosite în alte secțiuni. La redesign de bloc, verifică dacă clasele atinse mai apar în altă parte din document înainte de a scrie reguli bare.

- **L175** (V50) Propagarea modelului premium = GREFĂ chirurgicală, nu COPY+MODIFY. Delta premium real (hero+arc+CSS scoped) e ~5KB markup; restul „greutății" C01 e imaginea hero base64. Procedeu sigur: păstrezi conținutul de domeniu al construcției (stadii, scenă, pași, final, payoff), grefezi DOAR regiunea hero+arc din C01 cu text propriu + injectezi blocul CSS premium (cu maparea variabilelor lipsă, ex. `var(--tr-y)`→`var(--y)`). Premium V47 = doar Studiu/Editor-Studiu; Video nu se atinge (verifică: 0 clase premium în C01 Video).
- **L176** (V50) Gate/detectoarele trebuie făcute conștiente de redesign, altfel chiar construcția-model pică. Gate v20 cerea `cover-label` + slug în titlu (eliminate de V47) → C01 ÎNSUȘI pica IDENTITY. Fix: ramură premium (detectează `hero-visual-overlay` → verifică identitatea în hero-overlay+topbar+footer), păstrând legacy pentru construcțiile nepropagate. **Regulă durabilă:** când redesignul mută unde trăiește o informație (identitate), actualizează detectorul în aceeași mișcare, nu mai târziu.
- **L177** (V50) Imaginile lipite de ARHITECT în chat SUNT accesibile motorului prin transcriptul sesiunii (`~/.claude/projects/.../<session>.jsonl`, bloc `type:"image"` → `source.data` base64). Nu se spune niciodată „nu pot accesa imaginea". Le extrag, scot watermark-ul (R-V49.1) și le salvez singur. Mapez 1:1 cu prompturile după conținut (verificare vizuală pe cele ambigue) și confirm înainte de salvare când lipsesc/dublează.
- **L174** (V49) La lucru paralel pe sesiuni multiple (branch-uri `claude/<task>` simultane care fac toate merge în `main`), riscul de conflict e izolat la fișierele PARTAJATE, nu la construcții. Construcțiile `cNN/` sunt foldere disjuncte → merge curat. Punctele de conflict: `STARE-CURENTA.md` (toți scriu sumar sesiune), `CLAUDE.md` (reguli), `_system/*` (detectori, docs), `index.html` (dashboard cu link-uri). **Regulă durabilă:** înainte de merge în main, `git fetch origin main` + merge main în branch întâi (rezolv conflictele pe fișierele partajate local), apoi push. La STARE-CURENTA, fiecare sesiune adaugă propria secțiune V{N} — dacă două sesiuni incrementează simultan, a doua care face merge ajustează numărul V și fuzionează sumarele, nu suprascrie. Pentru `index.html`, fiecare construcție își are propriul rând → merge aditiv.

- **L175** (V49) Containerul Claude Code on Web NU are browser/Playwright instalat → randarea de verificare (L171) nu e posibilă aici. Compensare: validare structurală programatică (parser HTML pentru nesting balansat + decode base64 imagine + audit_sync + grep prezență/absență elemente). **Regulă durabilă:** când randarea nu e disponibilă, declar explicit „NEVERIFICAT randat" în raport și STARE-CURENTA, NU pretind verificare vizuală pe care n-am făcut-o; ARHITECT face check-ul vizual final sau îl fac la o sesiune cu browser.

Toate lecțiile cumulate (L01-L168) în `_system/arhiva/brain-evolutia-V01-V38.md` (până V41) + STARE-CURENTA (V42+).

---

## Modificări sistem aplicate V38

**Refactor documentație** (de la 580 KB împrăștiată la 84 KB în 8 fișiere):
- `_system/00-INDEX.md` (punctul de intrare)
- `_system/01-REGULI-ACTIVE.md` (reguli distilate)
- `_system/02-GLOSAR.md` (termenii cheie)
- `_system/03-COMENZI-OPERATIONALE.md` (FAQ)
- `_system/04-ARHITECTURA-LIVRABILE.md` (schema 7 artefacte)
- `_system/05-WORKFLOW-PER-SCENARIU.md` (5 scenarii)
- `_system/06-MAP-CONSTRUCTII-T1-T5.md` (cele 20 mapate)
- `_system/07-BRAND-OPERATIONAL.md` (brand, voce, colors)

**Setup definitiv (V38 extins):**
- `CLAUDE.md` la rădăcină (boot rapid)
- `STARE-CURENTA.md` la rădăcină (acest fișier)
- `_system/COMENZI.yaml` (catalog machine-readable)
- `_system/INDEX-CAUTARE.md` (search index)
- `_system/generatoare/patch_runner.py` (motor patch unificat)
- `_system/patch_recipes/` (rețete YAML)

**Migrare retroactivă R-V03.58:** generat FILM.docx + copiere assets/ pentru C02-C05 (drift detectat și reparat).

**Restructurare repo:** eliminat `_pilot/`, mutat în `c01/canonic/+editat/` ca celelalte construcții.

---

## Asset-uri perpetue verificate (V40)

| Asset | Locație | Stare |
|---|---|---|
| Date_MASTER-initial.xlsx | `_system/referinte/` | ✓ (2000 facturi, sumă 7.986.019,38) |
| IDENTITATE-TEHNICA.md | `_system/referinte/` | ✓ schema R-V03.47 |
| DATA-INSTRUCTIUNI.md | `_system/referinte/` | ✓ |
| SCHEMA-MASTER.md | `_system/referinte/` | ✓ |
| COVER-CHECKLIST.md | `_system/referinte/` | ✓ |
| PROTOCOL-FILM-OBS.md | `_system/referinte/` | ✓ |
| highlighter-snippet.{css,js} | `_system/referinte/` | ✓ |
| 6 imagini exec-stage per cNN | `cNN/assets/` | ✓ jpg 3:2 cinematic (diferite per construcție; PNG eliminat V41) |
| c01/ = construcția de referință (cobai) | rădăcină | ✓ (V46: `_template/` eliminat) |

---

## Cum se actualizează acest fișier

**Cine îl scrie:** Claude (motor) la fiecare modificare semnificativă.

**Când îl scrie:**
- După `genereaza CNN` cu PASS → update tabel construcții
- După `aplica fix` → update reguli noi
- După `consolideaza brain` → update sumar sesiune
- La fiecare incrementare V → update versiune + data

**Cum îl citește ARHITECT:** la fiecare sesiune nouă, primul lucru. 2 minute pentru a fi orientat.

---

## Următorul checkpoint așteptat

**V41 — generare C06**

Trigger: ARHITECT îngheaţă SPEC C06 (cele 9 elemente narrative) în `_system/arhiva/SISTEM_TRAINITY-versiuni.md` → comandă `genereaza C06` → motor rulează `pre_generation_check.py 06` → PASS → execută → V41 marcat aici cu C06 LIVRABIL.
