# Stare curentă Trainity · Pack 02 Excel

**Versiune sistem:** V61 (consolidat · marker SHA în `_system/VERSIUNI.md`)
**Ultima actualizare:** 2 iunie 2026

**Sesiunea V61 — sumar (audit adversarial C08 + închidere reziduuri non-imagine):**

1. **Audit adversarial C08 (production review, 10 axe A-J).** Premisa briefului (AHA „Cele mai importante date despre un rând nu sunt în rând", metodologie „localizăm nu aducem", MATCH) confirmată ca aliniată cu sistemul înghețat (06-MAP lock V58) ÎNAINTE de audit, nu coruptă (diferit de C05/L186). Structură PASS integral (6 etape / 18 pași / 5 fenomene / 8 verificări / 2 prompturi, dovedite empiric), identitate PASS (toate sloturile verbatim pe AHA, zero contradicții), garda T2 PASS (XLOOKUP/JOIN/MERGE = 0; „Data Model" 2× doar în handoff C09; întărire activă „nu am unit seturile"). GATE v20 PASS, em/en-dash = 0.
2. **R1 ÎNCHIS — AHA lock absent din FILM (master).** FILM C08 nu avea slot AHA (doar INTRIGA/MIZA/MANTRA/WOW/MOTTO). Inserat slotul „AHA (INSIGHT)" + linia lock verbatim cu diacritice între MIZA și MANTRA (clonare stil XML din paragraful MANTRA, re-zip docx). R-V46 FILM=master respectat.
3. **R3 ÎNCHIS — mismatch narativ/artefact (dinamic vs static).** Studiu pretindea „tabel viu / refresh → harta reflectă registrul" + mecanism COUNTIF/MATCH, dar `_ECOSISTEM`/`_CHEI` erau text static (0 formule). Adăugat recunoaștere LIVE în Date_MASTER: `randuri` prin `COUNTA`, coloană nouă `chei_recunoscute_live` prin `SUMPRODUCT(--ISNUMBER(MATCH(...)))` (recunoaștere pură, ZERO aducere de valori — garda T2 respectată). Verificat: PRODUSE 13/13, CLIENTI 15/15 recunoscute; suma `valoare_neta` conservată exact (7.986.019,38). PAS 13/14 reformulați: „tabel viu" → coloane vii care recalculează; „adaugă foaie nouă → apare automat" (imposibil cu formule legale T2, ar cere Power Query = C04) → „modifică date satelit → recalc → harta reflectă registrul". Onestitate tehnică.
4. **R4 ÎNCHIS — hero `alt=""` gol** → alt descriptiv (standard C01-C05), Studiu + Editor-Studiu.
5. **R2 RĂMÂNE (extern):** cele 6 exec-stage C08 sunt încă clone C01 (`R-V59.imgclone` XX). Prompturile ECOSISTEM refăcute; generarea Banana se face în altă sesiune, nu aici.

**C08 = ACCEPTAT CU WARNING la închiderea auditului → reziduurile non-imagine (R1/R3/R4) închise în V61.** Singurul rămas = R2 (imaginile, extern). GATE PASS, audit fără drift nou.

---

**Sesiunea V60 — DOUĂ fluxuri paralele consolidate: C05 RELEASE PASS real + C06 remediere MAMUT CLASIFICARE.**

---

### FLUX A · C05 (DICȚIONAR — RELEASE PASS real, 6/6 imagini dedicate)

**Sesiunea V60 — sumar (C05 remediere post-audit MAMUT: RELEASE PASS real, 6/6 imagini dedicate):**

1. **Audit senior C05 (8 niveluri) + remediere.** Întâi am respins premisa coruptă a brief-ului de audit („C05 = CLASIFICARE") — contrazicea sistemul înghețat (C05=DICȚIONAR, C06=CLASIFICARE), verificat în 06-MAP + deliverabilul construit + decizia ARHITECT (L186). Apoi remediere cap-coadă pe identitatea corectă DICȚIONAR.
2. **H-2 + M-1 + L-1 + L-2 + mecanism Video:** „AUDIT FORENSIC AL DICȚIONARULUI" → „VERIFICAREA DICȚIONARULUI" (C03 contaminare scoasă); ETAPA 3 phase-tag „POWER QUERY" → „PROFILARE" (aliniat cu Video „Power Query nu intră"); FILM diacritice + roluri „audit"→„interogare"; „auditabil"→„verificabil"; Video frame 13/14 Format-as-Table/Refresh → formule dinamice, „alertă în C06"→„de dicționar"; Creativ COUNTUNIQUE→COUNTA(UNIQUE()). Terminologic C05 = CURAT (forensic/PQ/auditabil/KPI/COUNTUNIQUE = 0).
3. **H-1 REZOLVAT — 6/6 imagini exec-stage dedicate DICȚIONAR.** ARHITECT a generat cele 6 imagini Banana (din prompturile Creativ S3); procesate singur (extras din transcript jsonl, watermark Gemini scos — img5 = caz greu L179 pe card alb+amber, patch țintit), salvate în `c05/assets/exec-stage-1..6.jpg` + base64 inline (resize 1200/q82) în HTML-Video + HTML-Editor-Video. Toate 6 = hash ≠ C01 (înainte erau clone byte-identice C01).
4. **Merge cu munca paralelă aprobată:** la push am găsit pe main o sesiune paralelă care rescrisese C05 cu texte aprobate de ARHITECT (payoff/motto, „C05 nu enumeră C06", nav-brand scos) + fixase H-2 identic. Am adoptat main ca bază și am re-aplicat DOAR deltele mele unice (M-1, Video, FILM diacritice, R-V59, Creativ) — fără a suprascrie conținutul aprobat.
5. **L196 (nou) — detector anti-clonă imagine `R-V59.imgclone`:** o construcție PREMIUM (hero-visual-overlay) nu poate avea imagini exec-stage byte-identice cu C01 (parazitare moștenite COPY-from-C01), decât cu excepție în `EXEC_CLONE_EXCEPTIONS`. Doar stdlib (`hashlib`/`md5`), fără dependență. A prins corect C05 (rezolvat acum) + **C06/C07/C08** (premium-izate de uniformizarea paralelă dar rămase cu imagini clone — de tratat separat). Audit 104→**120** verificări (15 detectoare × 8).

**C05 = RELEASE PASS real** (toate 8 axe audit PASS): premium + axă DICȚIONAR curată cap-coadă + 6/6 imagini dedicate + zero contaminare C03/C04/C06 + FILM sync. Cele 2 HIGH din audit (H-1 imagini, H-2 forensic) închise. **Rămas în afara C05:** C06/C07/C08 au nevoie de 6×3 imagini dedicate (R-V59 le flaghează); img5 are un ghost minuscul în colț (opțional regenerat).

---

### FLUX B · C06 (CLASIFICARE pură — RELEASE PASS, mai puțin imagini PENDING BANANA)

**Sesiunea V60 — sumar (C06 remediere MAMUT: CLASIFICARE pură, RELEASE PASS mai puțin imagini PENDING BANANA):**

1. **MEGA AUDIT C06 (2 runde, AUDITOR ȘEF) → IMPLEMENTARE MAMUT.** Cauză-rădăcină: C06 finalizat ca COPY din C05 fără a duce toate artefactele la rigoarea C01-C04. Reparat cap-coadă pe 8 fișiere + detector nou.
2. **CRIT-1 Creativ era C05 DICȚIONAR:** SECȚIUNEA 2 (infografic) + SECȚIUNEA 3 (6 prompturi exec) rescrise integral pe axa CLASIFICARE. Eliminat dicționar (×17)/profilare/cardinalitate/granularitate/COUNTUNIQUE/„taxonomy hidden"/„C05 stamp STRUCTURE OK"/refresh. Footer C05→C06.
3. **CRIT-3 Scor = cuantificare (regresie identitate V45):** min-max `(valoare_neta-MIN)/(MAX-MIN)*100` → **punctaj pe reguli** `IFS(clasă 40/25/10)+SWITCH(segment 25/20/15/10)+cantitate(20/10/5)+regulă compusă(15)`, max 100. Propagat 4 HTML + FILM + Date_MASTER (recalculat 2000 rânduri, scor 25-100) + `_SCORURI`. Cuvântul „normalizare" eliminat.
4. **HIGH-2 XLOOKUP reintrodus** (era dropat, înlocuit cu TEXT): coloană `eticheta_externa` + sheet `_NOMENCLATOR` (categorie→linie business) în Date_MASTER; pas/card/SCENA REALĂ/final-card în HTML; cele 3 funcții-semnătură IFS/SWITCH/XLOOKUP complete (06-MAP respectat).
5. **HIGH-1 refresh/automatizare scos** din HTML/FILM/Creativ (recalculare automată a formulelor, fără refresh/Power Query/flux). Whitelist: comentariul editor „hard refresh cache-bust" (infrastructură partajată, nu conținut C06).
6. **HIGH-3 transformare-section gated** (DUPĂ C06 POȚI + DE ACUM ÎNAINTE) adăugat Studiu+Editor (CSS display:none + .visible + JS reveal, ca C01/C02). **HIGH-4 FILM:** back-port ARC TRANSFORMARE/CINE DEVII/DE ACUM ÎNAINTE.
7. **MED:** em-dash scos din Date_MASTER (CONTROL_FINAL). `_README` avea harta T2 **pre-V45** (C06=„KPI & CALCULE", C05=CLASIFICARE, T2=„CALCUL") → corectată la CUNOAȘTERE (C06=CLASIFICARE, C05=DICȚIONAR, C07=DATARE, C08=CARTOGRAFIERE). prioritate/KPI scoase (limbaj T3 interzis). **LOW:** auditabil→trasabil; „recunoaște necunoașterea"→„marchează rândurile fără clasă"; emotion „Audit"→„Verificare".
8. **L197 (nou) — BUG CRITIC JS reparat:** ghilimele neescapate `"A_Licențe"` într-un string JS rupeau **întreg blocul `<script>` STAGES** din HTML-Video + Editor-Video (PARSE ERROR → show executiv + nav etape nu se încărcau). Reparat (`\"A_Licențe\"`). **Regulă durabilă:** orice string în array-uri JS (steps/stages) cu ghilimele interioare se validează cu `new Function(block)` — gate/audit nu prind JS rupt, doar nesting HTML.
9. **L198 (nou) — Creativ-ul e artefact de drift de prim rang:** contaminarea C05 trăia în Creativ (brief imagini) deși HTML/xlsx fuseseră rebuild-uite pe clasificare; de aici imaginile clone. **Regulă durabilă:** la COPY+MODIFY o construcție, Creativ-ul (SECȚIUNEA 2+3) se rescrie OBLIGATORIU pe axa proprie, altfel imaginile generate sunt ale construcției-sursă.
10. **L199 (nou) — openpyxl instalabil în container Web** (`pip install openpyxl`): deblochează editarea sigură a xlsx ȘI rularea reală a gate-ului (DATA-CONTINUITY pica pe dependență lipsă, nu pe conținut). De instalat la orice sesiune care atinge Date_MASTER.
11. **Detector nou `_system/generatoare/detect_c06_purity.py` (D1-D7):** refresh în corp T2, scor min-max/normalizare, em-dash în xlsx, funcții-semnătură IFS/SWITCH/XLOOKUP, Creativ contaminat cu termeni C05, limbaj T3 (prioritar/strategic), exec-stage clone C01 (R-V59). Acoperă găurile pe care gate/audit_sync nu le prind (xlsx dash, JS, Creativ).
12. **Stare:** C06 GATE PASS, audit_sync 14/15 (doar imgclone XX), detect 6/7 (doar D7), sumă conservată DELTA 0, JS parse OK ×4, render desktop+mobil OK. **PENDING BANANA (necosmetizat, fără fake fix):** cele 6 imagini exec-stage rămân clone C01 (R-V59 FAIL) până la generarea din Creativ-ul corectat → atunci C06 = RELEASE PASS complet.


---

**Sesiunea V59 — sumar (C03 refactor MAMUT: graniță AUDITARE/NORMALIZARE absolută, GATE PASS):**

1. **Cauză-rădăcină reparată: confuzia AUDITARE vs NORMALIZARE.** Auditul senior pe 6 niveluri a arătat că C03 etapele 3-5 executau curățare Power Query (teritoriul C04), deghizată în „demonstrație". Refactor cap-coadă: C03 = detectează + cuantifică + dovedește recuperabilitatea + confirmă; C04 = construiește mecanismul. **Power Query eliminat complet ca unealtă activă din corpul C03** (toate 4 machete): zero PQ / Refresh All / Text.Trim / Number.From / Date.From / neutralizare / AGGREGATE / dashboard în machetele learner-facing.
2. **Etapa 3 = „DEMONSTRAȚIA RECUPERABILITĂȚII"**: coloane martor cu formule (TRIM, CLEAN, SUBSTITUTE, VALUE, DATEVALUE) lângă sursa intactă; nu se produce foaie curată, se dovedește recuperabilitatea. Etapa 4 = „VERIFICAREA DOVEZII" (reconciliere detectat==explicat + sumă martor). Etapa 5 = „AUDIT REPETABIL" (aceeași metodă → aceeași dovadă; phase-tag REFRESH/Power Query Refresh → METODĂ/Audit repetabil).
3. **Video JSON era integral C01/C04** (subtotaluri, antet promovat, „flux Power Query", AGGREGATE) — STAGES+PROMPTS rescrise complet pe axa forensic, aliniate la Studiu. Overlay slide 3 forensic.
4. **transformare-section reintrodusă** (gated, CSS+JS reveal reparate) cu identitate proprie de auditor. Secțiuni 18→**19** (paritate C01/C02). **Bombă diferențiată de C02**: „Invizibil cu ochiul. Vizibil sub audit." Nav-meta corectate (AGGREGATE→Reconciliere, Power Query Refresh→Audit repetabil). **FILM rescris** (bombă, slide exec 3, narațiune boilerplate 6×3 specializată forensic, zero PQ/Refresh/AGGREGATE). Creativ etapa 3 reframe.
5. **Stare:** C03 **GATE PASS**, audit_sync **ZERO DRIFT 112/112**, zero em/en-dash, randat-verificat desktop+mobil. Index cache-bust C03 v5/v4 + titlu reparat („Cum auditezi ce nu se vede în date", închide observația V51). **Rest minor:** xlsx `Vanzari_AUDIT` rămâne copie pe schemă (gate o cere), tratată narativ ca foaie-dovadă; rebuild cu coloane martor = follow-up gate-aware.

---

**Sesiunea V58 — sumar (C02 reconstruită cap-coadă CONTROL + audituri T1/T2 + remedieri C01 + excepție gate C01):**

1. **C02 = LIVRABILĂ, reconstruită integral pe identitatea LOCK CONTROL** („CORESPONDENȚA CU REALITATEA", AHA „Valid nu înseamnă corect."). Lanț de execuție documentat: blueprint → spec → D1 nomenclatoare → D2 Vanzari curat → D3 realitate → D4 build. **Date_MASTER-C02 rescris** prin generator determinist (`build_date_master_c02.py`, seed 42): realitate coerentă (Vanzari 2010 + CONTACTE 50 cu CNP construit corect + 4 nomenclatoare) + **5 anomalii LOCK injectate controlat** (orașe 50 / TVA 47 / scadență 25 / NETWORKDAYS 20 / CNP 25) + semnalizare live (COUNTIF/XLOOKUP/NETWORKDAYS.INTL/SUMPRODUCT cifra control) + `_SEMNALIZARE`. **Reconciliere plantate==detectate, zero fals pozitiv/negativ.** Sumă `valoare_neta` conservată exact (8.018.087,99). Foi auxiliare CLIENTI/PRODUSE/AGENTI/DEPOZITE păstrate (gate).
2. **C02 HTML/FILM/Creativ MARCARE→CONTROL** prin transformatoare deterministe (`transform_c02_{control,video,film}.py`): cele 4 HTML rescrise (E3 FORMULE, E4 VERIFICAREA CORESPONDENȚEI, AF/CF, status OK/DE INVESTIGAT, prompturi interogare+semnalizare), FILM 49 paragrafe, Creativ. Redenumite `02-Control`; `gate_v20.py` nume_slug C02='Control'. Eliminat: Power Query, SUMIF, EXCLUS, week-end, duplicat, suma martor, „valid nu înseamnă adevărat".
3. **C02 călită prin audit reviewer senior** (3 runde): M1-M7 (H1 „Valid pentru Excel. Greșit pentru realitate."; regula oficială în cover-miza; mantra „Nu luăm valorile de bune…"; competență fără reziduu MARCARE; WOW „Excel acceptă orice. De acum, tu nu."; ts-block „Marchezi"→„Semnalizezi cu dovada" + întrebarea inversată reparată; ba-indicator „Sumă fizică/raport oficial"→„Valori sursă/Neconcordanțe semnalate"; alt-text status vechi). **Hero nou** (de la ARHITECT): metafora „≠" confruntare cu realitatea (nu ștampila de marcare), watermark Gemini scos, base64 + assets. Promptul Hero din Creativ refăcut.
4. **C01 — remedieri punctuale (anti-drift T1):** M1-M5 (elimină „BI-ready"→structură controlabilă/bază structurală validată; „calcul, analiză, dashboard"→„calcul și verificare"; „suma de referință/martor"→„control de conservare"; handoff „marchează anomaliile"→„semnalizează anomaliile"; alt hero descriptiv) + 3 label/frază („martorul fixat"→„valoarea de control fixată"; verificări finale „SUMĂ/SUMĂ"→„CONSERVARE/AGGREGATE"). Arhitectură neatinsă.
5. **L191 (nou) — base64 contaminează scanările lexicale:** scanul de termeni interziși (KPI/Scor) a dat 5-14 false pozitive fiindcă șirurile apar aleator în base64-ul hero-ului. **Regulă durabilă:** orice scan lexical de drift strip-uiește întâi `data:image;base64,...` (și style/script) — altfel numeri zgomot, nu conținut.
6. **L192 (nou) — audit comparativ valid cere adâncime egală:** primul ranking T1+T2 a scorat C02 pe disecție profundă și restul pe ~7 metadate → scoruri cosmetice, ranking liniar fals (meta-auditul adversarial l-a demontat). **Regulă durabilă:** nu se compară/ranchează construcții auditate la adâncimi diferite; ori disecție egală pe toate, ori tiere („dovedit / neinspectat"), niciodată precizie inventată.
7. **L193 (nou) — C01 e scenariu-pilot propriu, nu derivat:** investigația gate FAIL DATA-CONTINUITY a arătat că C01 are schemă proprie (`cod_client/cod_agent/cod_depozit` pentru lecția de integritate referențială la 4 nomenclatoare), sumă proprie (~1.25M vs ~8M), nomenclatoare proprii — NU derivă din `Date_MASTER-initial`. Output curat în `Vanzari_Curat` (gate citea greșit `Vanzari`=banner input). **Fix detector (verdict B+C):** excepție explicită C01 în `gate_v20.py` (validează `Vanzari_Curat` pe schema EI + nomenclatoare, fără comparație cu initial), scoped strict `NN=='01'`. **Regulă durabilă:** contractul de date C02-C08 (schemă canonică + initial-reference) NU se aplică pe C01-pilot; gate-ul e per-construcție pe foaia de output (ca la C03 Vanzari_AUDIT / C04 Vanzari_Normalizat). Forțarea schemei canonice ar rupe scenariul C01 = interzis.
8. **L194 (CORECTAT) — C03 gate FAIL a fost confirmat ca REAL după audit N1-N6.** Detectorul nu over-flaghează simplu handoff-ul, ci semnalează o contaminare metodologică reală: Power Query / Refresh erau folosite activ în corpul C03, ceea ce muta construcția din AUDITARE în NORMALIZARE. C03 trebuia refactorizat prin scoaterea Power Query din corp, reconstruirea etapei 3 ca demonstrație de recuperabilitate pe formule-martor, reintroducerea transformare-section și repararea nav-meta. **Formularea V58 anterioară („FAIL fals / over-flag handoff") e INVALIDĂ.** **REZOLVAT în V59** (refactor MAMUT C03, exact acest plan): PQ scos din corp, etapa 3 = DEMONSTRAȚIA RECUPERABILITĂȚII (formule-martor), transformare-section reintrodusă, nav-meta reparate → C03 GATE PASS.
9. **L195 (decizie deschisă) — phase-tag E3 neuniform în serie:** C05/C07 au phase-tag `POWER QUERY` peste corp 100% formule (UNIQUE/MIN/MAX); contrazice corpul + zona gri a gărzii T2 (R-PHASE-2 = decizie deschisă). C06=FORMULE, C08=HARTĂ (corecte). De decis (nu reparat orb).

**Stare gate/audit la închidere V58:** C01 GATE PASS (după excepție), C02/C04/C05/C06/C07/C08 PASS, **C03 = FAIL REAL la V58** (contaminare metodologică Power Query/Refresh în corp → muta AUDITARE spre NORMALIZARE; confirmat audit N1-N6; NU fals pozitiv) — **rezolvat ulterior în V59 prin refactor → C03 GATE PASS** (vezi sumar V59 + L194). audit_sync ZERO DRIFT 112/112.

---

**Sesiunea V57 — sumar (C05 LIVRABILĂ: premium + ascuțire G-06 + curățare drift SPEC + 3 runde feedback extern):**

1. **C05 ascuțită prin G-06** (feedback extern, confirmat ARHITECT): hook „Tabelul este curat. Dar știm ce conține?"; WOW nou cu slot `payoff-wow`+`data-wow` „Setul nu mai este o masă de date. Acum are hartă."; MIZA reframe spre teritoriu enumerabil + notă poziționare în 06-MAP (C05 = „știu ce există?" vs C01-04 „pot avea încredere?"); exec-slide 1/4/6 (slide 4 fără nume de funcții); fix drift `payoff-motto` (era „Mai întâi structura" din C01). Mantra/motto/slide 2/3/5 = NEUTRU. FILM (master) → 4 machete.
2. **C05 = model PREMIUM** (grefă L175 pe Studiu + Editor-Studiu, Video neatins): hero cockpit cu imagine-obiect DICȚIONAR dedicată (generată de ARHITECT din prompt Creativ SECȚIUNEA 1, watermark Gemini scos, base64) + overlay + system-map T2 + hero-question „Din ce este făcut acest set?"; arc TU (BOMBA → SUNĂ CUNOSCUT → GREȘEALA „Profesioniștii îl enumeră." → AHA „Nu cunoști un set până nu îl poți enumera." → CINE DEVII „Vezi un teritoriu.") + before/after + outcomes; cover-miza card; scos exec-hero + cover-meta. CSS premium scoped din C01. FILM + secțiune ARC TRANSFORMARE. Hero salvat `c05/assets/hero-poster-excel-05-dictionar.jpg`. **Verificat randat** 393px + 1280px.
3. **Curățare drift SPEC C05** (3 runde feedback extern G-06, toate verificate empiric înainte de aplicare): (a) DOVADA TRANSFORMĂRII rescrisă din probă de normalizare C04 (volum/subtotaluri/SUM-AGGREGATE/Refresh) în probă de dicționar; (b) mecanism dicționar Format-as-Table+Refresh → **formule dinamice UNIQUE / COUNTA(UNIQUE()) / COUNTIF** (afirmația „apare automat la valoare nouă" devine corectă tehnic); (c) alertă C06 → alertă de dicționar; (d) suma 7.986.019,38 lei scoasă (R-V02.15) în Studiu+Video; „Media ~133" scos; (e) tag AGGREGATE (C01/C04) → funcții reale Excel (header + side-nav); (f) nav Etapa 5 Power Query Refresh → Formule dinamice; (g) final check 8 + completion-title curățate de sumă/generic; (h) „TOP-3 97.5%" headline → „TOP-3 DOMINĂ" (cifra rămâne doar în pasul de calcul, ca martor); (i) `next-label` TREAPTA 1 → 2.
4. **Bug HTML propriu reparat:** grefa premium crease `<style id=c05-premium-graft><style>` imbricat (CSS-ul copiat din C01 începea cu propriul `<style>`). Scos wrapper-ul redundant; `<style>` balansat 8/8.
5. **Două fix-uri gate (conștiente de redesign, stil L176):** (a) cover-title liber post-V42 — checkul legacy nu mai cere slug-ul caps în titlu (deblochează C05-C08); (b) **`fold_diac()`** — premium topbar comparat cu slug-ul modulo diacritice (`Dictionar` ASCII vs `Dicționar` display). C05 GATE PASS premium.
6. **L186 (nou) — C06 = CLASIFICARE, respins de 3 ori „profil numeric/KPI":** un feedback extern a insistat repetat (citând un „HDMR" inexistent în repo) că C06 e profil numeric. Verificat empiric: `c06/` e construit ca CLASIFICARE (fișiere `...06-Clasificare`, label „C06 · CLASIFICARE", titlu „Cum dăm sens fiecărui rând", 71 markeri IFS/SWITCH/scor), rebuild V45 documentat, confirmat ARHITECT. **Regulă durabilă:** identitatea unei construcții se verifică în deliverabilul construit + 06-MAP + confirmarea ARHITECT, NU dintr-un document citat extern dar inexistent. Autorul feedback-ului lucra pe harta T2 pre-V45 (C06=CUANTIFICARE). Restul observațiilor lui (bug style, AGGREGATE) au fost utile și aplicate.
7. **L187 (nou) — G-06 verifică ÎNAINTE de a aplica:** fiecare punct de feedback extern a fost confruntat cu HTML-ul real + 06-MAP + deliverabilele construite înainte de clasificare. A separat driftul real (aplicat) de soluțiile greșite-pentru-sistem (respinse: „profil numeric", eliminarea Pareto care e fenomen C05). Intelligent honesty > aplicare oarbă SAU apărare oarbă (L167 în practică, de 3 ori).
9. **L189 (nou) — paritate componente-semnătură + detector permanent:** C05 ratase upgrade-ul V56 al mantra-band (rămas pe scala veche 20-28px), pentru că grefa premium copiază blocurile `<style>` premium APENDATE din C01, NU blocul `<style>` MAIN unde trăiesc mantra-band/componentele-semnătură; iar V56 modificase mantra în main-style-ul C01-C04 în paralel. Gate/audit nu l-au prins fiindcă verificau structură/identitate/anti-clonă-text/dash, NU paritatea tipografică a componentelor-semnătură între construcții (textul mantrei era corect, doar scala diferea). **Fix:** aliniat C05 la C01 (4 reguli: container/main/mark/sub) + **detector nou `R-V57.parity` în audit_sync** care verifică pe construcțiile PREMIUM mantra-band scala V56 (clamp 30-64 + weight 900 + box-decoration-break:clone) + cover-miza card (box-shadow); legacy = N/A vacuos. Rulat: C01-C05 PASS (confirmă că DOAR C05 era gaura, C02-C04 erau ok), C06-C08 N/A. Audit 88→96. **Regulă durabilă:** la propagarea premium / finalizarea unei construcții, componentele-semnătură (mantra, miza, bombă) se verifică contra referinței C01 — grefa nu cară schimbările din main-style făcute paralel; detectorul de paritate face asta automat de acum.

10. **L190 (nou) — nume FILM == identitate HTML, detector permanent:** la verificarea sync FILM↔HTML C05 am găsit că FILM-ul C05 avea încă numele vechi „CLASIFICAREA DATELOR" (rename V44 CLASIFICARE→DICȚIONAR a atins filename-ul + HTML, dar NU titlul din .docx) — coliziune cu C06 care e acum CLASIFICARE. Sincronizat FILM (nume în 3 locuri + ETAPA 4 AGGREGATE→COUNTA(UNIQUE())/COUNTIF + ETAPA 5 Power Query→formule dinamice + fenomen Pareto softat). **Detector nou `R-V58.filmname`** (audit_sync, doar stdlib `zipfile` — fără dependență python-docx, degradare grațioasă): stem-ul numelui din titlul FILM `.docx` trebuie să apară în identitatea HTML (topbar+footer+cover-title), modulo diacritice. Numele narative legitime (C07 MEMORIA, C08 ECOSISTEM) trec fiindcă apar în cover-title. Validat: toate 8 PASS, C05-vechi „CLASIFICAREA" ar fi picat. Audit 96→**104**. **Regulă durabilă:** orice rename de construcție trebuie să atingă ȘI conținutul FILM (titlu/deschidere/final), nu doar filename-ul; detectorul prinde automat dacă scapă.

8. **L188 (nou) — acuratețe funcții Excel:** `COUNTUNIQUE` NU există în Excel (e funcție Google Sheets); a trăit în C05 de la generarea inițială și am propagat-o din greșeală în fix-urile de mecanism. Corect Excel 365: `COUNTA(UNIQUE(range))` pentru cardinalitate, `COUNTIF` pentru frecvență, `UNIQUE` pentru listă distinctă. Curățat în toate 4 machetele (8+1 apariții). **Regulă durabilă:** orice funcție Excel scrisă într-un livrabil se verifică contra setului real de funcții Excel 365 (nu Google Sheets / nu inventată) — e curs de Excel, acuratețea funcțiilor e parte din corectitudine.

**C05 = LIVRABILĂ** (a treia construcție model finalizat după C01, C02): premium + axă DICȚIONAR curată cap-coadă + zero contaminare C04/C06/KPI + hero dedicat + FILM sync + verificat randat. Cache-bust `?v=4` pe link-urile C05 din index (L185). Audit ZERO DRIFT 88/88, gate C05-C08 PASS.

---

**Sesiunea V56 — sumar (mantra-band la scala tipografică de bombă, propagat C01-C04 + lecție cache-bust):**

1. **Mantra-band ridicată la scala bombei** (cerere ARHITECT: „arăta prea mic și prea neimportant"). Din `clamp(20px, 2.6vw, 28px)` weight 800 → `clamp(30px, 7vw, 64px)` weight 900, letter-spacing `-1.5px`, line-height `1.02`. Mapat exact ca BOMBA premium: linia-setup în **gri masiv** (`#a6a6a6`) + cuvântul-cheie în **caseta galbenă** (`<mark>`), cu `box-decoration-break: clone` ca highlight-ul să rămână casetă curată dacă se rupe pe două rânduri (ex. C03 „auditul tehnic"). Bandă mai aerisită (padding vertical până la 84px) + eticheta sub puțin mai distanțată. Limbaj unitar cu bomba: gri = afirmația, galben = lovitura.
2. **Propagat C01-C04** (Studiu + Editor-Studiu, 8 fișiere), păstrând textul propriu al fiecărei mantre: C01 „Înainte de orice calcul, structura.", C02 „Înainte de orice raport, controlul.", C03 „Înainte de orice analiză, auditul tehnic.", C04 „O dată construit. De fiecare dată identic." Întâi doar C04 (validat de ARHITECT), apoi propagat la 1/2/3 la OK. **Verificat randat** (L178) desktop 1280px + mobil 393px pe toate 4; C03 (cel mai lung, highlight pe 2 cuvinte) confirmat fără overflow.
3. **L185 (nou) — disciplină cache-bust:** când un livrabil HTML se modifică dar link-ul din `index.html` păstrează același `?v=N`, browserul servește copia VECHE din cache (URL identic → zero refetch). Asta a fost bug-ul „nu văd în html" raportat de ARHITECT (vedea mantra veche neagră deși fișierul de pe main era corect gri). **Regulă durabilă:** orice modificare a unui HTML dintr-o construcție livrată → bump `?v=` pe link-urile ei din `index.html` în același commit. Aplicat: C01/C02/C03/C04 link-uri Studiu+Editor-Studiu `?v=3` → `?v=4`.
4. **L181 reconfirmat în practică:** `main` local era încă pe lineage-ul orfan V45; `origin/main` real avansase V51 → V55 prin sesiuni paralele. Aliniat pe `origin/main` (fetch) + cherry-pick al singurului commit unic (mantra C04) → fișiere disjuncte, fără conflict. **ARHITECT a cerut explicit „lucrează doar pe main"** — starea pe care o vede el = `origin/main` (sursa Pages); push-ul pe branch nu era vizibil.
5. ⚠️ **Observație (neatinsă, out of scope):** `index.html` card-title C03 = „Cum construim un audit valoric" (titlul vechi pre-V51); rename-ul V51 la „Cum auditezi ce nu se vede în date" nu a ajuns în dashboard. De aliniat la o sesiune C03.
6. **Sync FILM↔Studiu C01-C04 (cerere ARHITECT „în film să regăsim informațiile din studiu"):** verificat slot cu slot — MANTRA/WOW/MOTTO erau deja sincrone pe toate 4; MIZA sincronă C01/C02. Drift real: modelul premium V47+ a adăugat în Studiu **arcul TU** (BOMBA + SUNĂ CUNOSCUT + GREȘEALA + AHA + CINE DEVII), dar doar C04 FILM îl avea back-portat. **Back-portat secțiunea `ARC TRANSFORMARE` completă în FILM la C02 + C03** (clonând formatarea XML din C04, texte din Studiu) + completat fraza a 2-a din MIZA C04. C01 are arcul în format Biblia v2.0. Docx editate prin manipulare directă `word/document.xml` (python-docx absent) + re-zip; integritate verificată. Maparea `10-MAP-FILM-HTML.md` actualizată (era stale: `cover-subtitle` ← BOMBĂ la premium, nu INTRIGA). Rămâne intenționat doar voce C03 MIZA („noi" în FILM vs „C03" în Studiu, aceeași informație).

Audit ZERO DRIFT 88/88. Gate v20 C04 PASS. Zero em/en-dash. Toate pe `main`.

---

**Sesiunea V55 — sumar (C03 imagini exec COMPLET 6/6 + tooling cleanup branch-uri):**

1. **C03 = MODEL FINALIZAT (a treia construcție 100% gata, după C01+C02+C04).** Cele 6 imagini exec-stage forensic dedicate generate de ARHITECT, procesate singur (extras transcript jsonl → strip watermark → recomprimate ~120-200KB, normă C02 → base64 în Video + Editor-Video). Toate 7 imaginile C03 (hero + 6 exec) sunt acum proprii, zero clone C01. Video 1.31MB. Render-verificat (data URI valid + tabel forensic se vede în player). C03 complet: premium + rescope C03/C04 + hero + 6/6 exec + FILM sync.
2. **L183 (nou) — rafinare `strip_watermark`:** `detect_sparkle` SUPRA-detectează când colțul dreapta-jos e ADIACENT unei zone luminoase (marginea unei pagini albe lângă steluță) → prinde o casetă mare (164px) și clonează din zona deschisă = pată vizibilă. Fix aplicat la exec-stage 3-6 C03: casetă mică fixă (~95px) în colț + **clonă verticală din banda întunecată direct deasupra**. Completează L179 (acolo colțul ERA pe fundal deschis; aici colțul e pe întuneric dar adiacent luminii). De integrat ca mod în `strip_watermark.py`.
3. **Tooling nou — `_system/generatoare/cleanup_branches.sh`:** șterge toate branch-urile în afară de `main`. Safe by default (dry-run; `main` protejat; comută pe main înainte de a șterge branch-ul curent). Flags: `--local`/`--remote`/`--all` + `--force`.
4. **Curățat branch-urile:** local → doar `main`; remote → 2/3 șterse (`admiring-babbage`, `dreamy-keller`). `vigilant-goldberg` BLOCAT (403/disconnect — sesiune paralelă activă). **L184:** proxy-ul Web blochează `git push origin --delete` pentru branch-uri de sesiuni ÎNCĂ ACTIVE (403, ca la tag-uri); GitHub MCP n-are tool de delete-branch. Ștergerea remote a unei sesiuni active se face de pe mașina ARHITECT (`git push origin --delete`) sau din GitHub UI, ori după ce sesiunea se închide.

---

**Sesiunea V54 — sumar (C05 copy ascuțit prin G-06 + fix gate cover-title legacy):**

1. **Feedback extern pe C05 → G-06 → aplicat** (confirmat ARHITECT): hook „Tabelul este curat. Dar știm ce conține?" (tensiune, callback C01-04 „curat"); **WOW nou cu slot `payoff-wow` + `data-wow`** „Setul nu mai este o masă de date. Acum are hartă." (C05 nu avea slot WOW vizibil în modelul V44; l-am adăugat cu CSS din C01, badge verde); MIZA reframe spre teritoriu enumerabil; exec-slide 1/4/6 reformulate (slide 4 fără nume de funcții: COUNTUNIQUE/COUNTIF → „Sistemul decide"); fix drift `payoff-motto` (zicea „Mai întâi structura. Apoi orice." din C01) → motto corect C05 în slot. Mantra/motto/slide 2/3/5 = NEUTRU, păstrate. Propagat FILM (master) → 4 machete, round-trip consistent.
2. **Notă poziționare C05 în `06-MAP`:** C01-04 răspund „pot avea încredere în set?"; C05 răspunde „știu ce există în el?" (poarta T2, teritoriu cartografiat, nu etichete izolate).
3. **Fix `gate_v20.py` (stil L176 — detector conștient de redesign):** checkul legacy IDENTITY cerea slug-ul caps articulat (DICȚIONARUL etc.) în `cover-title`, dar V42 a făcut titlurile descriptive libere („Cum construim X" / „Cum dăm sens fiecărui rând" — C06 nici nu conține slug-ul). Identitatea rămâne garantată de `cover-label` (CONSTRUCȚIA CNN) + footer + meta; anti-clonă narativă = audit_sync R-V03.69. Acum verificăm doar că `cover-title` există și nu e gol. **Deblochează GATE PASS pe C05-C08** (aveau toate aceeași presupunere stale de la V42). Premium C01-C04 neatins (ramura hero-overlay separată).
4. **Git (L174 în practică):** „unrelated histories" la merge era cu `main` LOCAL (lineage orfan V45, rămas după un force-push pe remote), NU cu `origin/main` real. `origin/main` (10aef81) împărțea strămoșul `57be5d2` cu branch-ul de sesiune. Merge cu munca paralelă (C04 exec-stage-1, zero conflicte — foldere disjuncte) → FF pe main `10aef81..b805920`. **L181:** după force-push pe remote, `main` local poate rămâne pe un lineage orfan; ținta corectă de merge e `origin/main` (post-fetch), nu `main` local.
5. **L182:** verificarea anti-regresie după un fix de script (am rulat gate pe C01-C04 ca să confirm că fix-ul legacy nu rupe premium) e OK; săparea în cauzele unor FAIL-uri pre-existente, neînrudite de task, și raportarea lor = scope creep. Confirm doar „nu vine din schimbarea mea", apoi mă opresc.

6. **Propagare model PREMIUM pe C05** (grefă L175, după ascuțirea G-06): hero cockpit cu imagine-obiect DICȚIONAR dedicată (generată de ARHITECT din promptul Creativ SECȚIUNEA 1, watermark Gemini scos, base64 inline) + overlay „DICȚIONAR" + system-map T2 (DICȚIONAR activ) + hero-question „Din ce este făcut acest set?"; arc TU (BOMBA „Tabelul este curat. Dar știm ce conține?" → SUNĂ CUNOSCUT → GREȘEALA „Oamenii presupun ce conține setul. Profesioniștii îl enumeră." → AHA „Nu cunoști un set până nu îl poți enumera." → CINE DEVII „Nu mai vezi coloane. Vezi un teritoriu.") + before/after + outcomes; cover-miza upgradat la card (V53 propagat acum și pe C05). Scos exec-hero „DE CE C05" + cover-meta. Doar Studiu + Editor-Studiu (Video neatins, per L175). CSS premium grefat scoped din C01 (fix L173 inclus). **Verificat randat** (L178): mobil 393px + desktop 1280px, hero + arc + card miza corecte. FILM (master) + secțiune „ARC TRANSFORMARE" (format C04). hero salvat `c05/assets/hero-poster-excel-05-dictionar.jpg`.
7. **Fix gate (#2 azi): premium topbar diacritic-insensitive.** Checkul premium cerea slug-ul ASCII (`Dictionar`) în topbar, dar topbar afișează diacritic (`Dicționar`) → C05 pica doar pe asta. Adăugat `fold_diac()` (pliază diacriticele românești) la compararea slug↔topbar. C05 GATE PASS premium. **L183:** slug-ul = stem filename ASCII, display-ul = diacritic; comparațiile de identitate între ele se fac modulo diacritice.

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
| **C03** | AUDITARE (cum auditezi ce nu se vede în date) | V51 MODEL FINALIZAT: premium + rescope C03/C04 + hero-poster + 6/6 exec-stage forensic dedicate + FILM sync | versiune unica + assets/ + hero | ✓ ZERO DRIFT |
| **C04** | NORMALIZARE (model PREMIUM V50: hero cockpit + arc TU) | V50 premium · 6/6 exec dedicate + hero | versiune unica + assets/ + hero | ✓ ZERO DRIFT · GATE PASS |
| **C05** | DICȚIONAR (ce reprezintă datele — inventar categorii) | **V57 LIVRABILĂ** model PREMIUM (hero cockpit DICȚIONAR + arc TU + before/after + outcomes) + G-06 + curățare drift SPEC cap-coadă (zero contaminare C04/C06/KPI; mecanism dinamic UNIQUE / COUNTA(UNIQUE()) / COUNTIF) | versiune unica + assets/ + hero dedicat | ✓ ZERO DRIFT · GATE PASS |
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

1. ✓ **C03 COMPLET** — 6/6 exec-stage forensic dedicate + hero + premium + rescope. (opțional rămas: infografic + cover-yt C03, neesențiale)
2. ✓ **C04 COMPLET 100%** — toate 6 exec-stage + hero dedicate. Nimic rămas pe C04.
3. **Propagare model premium C06-C08** (C01-C05 făcute) — grefă hero+arc+CSS scoped + imagine-obiect per construcție + sync FILM. Gate v20 deja conștient de premium. Necesită hero imagine-obiect dedicat per construcție (generat de ARHITECT din prompt Creativ).
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
