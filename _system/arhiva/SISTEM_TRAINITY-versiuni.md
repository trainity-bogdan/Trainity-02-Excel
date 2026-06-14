# SISTEM TRAINITY — V38 (27 mai 2026)

**V37 = V36 consolidat. Arhitectura canonic/+editat/ stabila.**

Toate constructiile T1 (C02-C05) migrate la noua structura. Gate v20
PASS pe ambele stari (canonic + editat). Pattern de patch confirmat
empiric pentru upgrade-uri KIT viitoare.

Cele 4 comenzi operationale canonice sub V37:
1. `genereaza constructia NN` - prima rulare, creeaza canonic/+editat/
2. `regenereaza CNN de la zero` - SUPRASCRIE ambele (cerere explicita)
3. `aplica upgrade KIT pe editat` - patch script pe editat/
4. `compara canonic vs editat CNN` - audit modificari manuale

C06+ vor genera AUTOMAT sub schema V36+ (canonic/+editat/ la prima
rulare).

================================================================================

**V36 = V35 + R-V03.62 (prima generare inghetata + patch over edited).**

ARHITECT a ridicat problema persistarii modificarilor de continut intre
regenerari. Solutia: model in DOUA STARI per constructie.

Fiecare livrabile_C{NN}/ are acum doua sub-foldere:
- `canonic/` - snapshot inghetat (V01 = prima generare). Imutabil.
- `editat/` - versiunea evolutiva (start identic cu canonic). Aici merg
  modificarile ARHITECT + patch-urile KIT.

C02 V26, C03 V26, C04 V27, C05 V28 migrate retroactiv prin
`init_canonic_editat.py`. Gate v20 PASS pe ambele stari, toate 4
constructii.

C06+ vor genera AUTOMAT sub schema V36+ (motorul scrie in canonic/ +
copie identica in editat/ la prima generare).

Lectie L154: persistarea editorilor prin non-regenerare. Pattern functional
deja confirmat empiric V32-V34 (cover-meta, buton lipit, highlighter).
V36 doar formalizeaza pattern-ul cu structura canonic/+editat/ + meta
markers.

================================================================================

**V35 = V34 consolidat. Matrita C01 V12 pilot are aplicate exhaustiv
toate modificarile V32+V33+V34:**

- **R-V03.60 (V32)** cover-meta curat (3 randuri: TREAPTA + CONSTRUCTIE
  + AI INTEGRAT)
- **V32 (fix)** referinte Date-Input/Date-Output → Date_MASTER-C01
- **R-V03.61 (V33)** `margin-top: auto` eliminat din `.nav-controls`
  (buton lipit responsive)
- **R-V03.59 V34** highlighter rafinat: fara buton, fara ESC, capture
  phase pentru preven advance, click pe text plain dupa toggle =
  avansare normala

Audit exhaustiv pe matrite C01: **18/18 verificari PASS** (Date-Output
0, cover-meta INPUT/OUTPUT 0, margin-top eliminat, buton hl-reset 0,
CSS .hl-reset 0, ESC handler absent, capture phase prezent, versiune
v34 marker).

Matrite gata pentru COPY+MODIFY la C06+. Toate fix-urile ereditate
automat.

================================================================================

**V32 = V31 + R-V03.60 (cover-meta HTML-Studiu fara INPUT/OUTPUT)
+ L151 (UI cleanup retroactiv prin script idempotent).**

ARHITECT a observat reziduuri din schema veche in cover-meta:
randurile INPUT + OUTPUT cu link la fisier Excel. Schema actuala
(R-V03.47) foloseste un singur Date_MASTER-CNN.xlsx - randurile
duplicate/obsolete.

Cover-meta acum minimalist: TREAPTA + CONSTRUCTIE + AI INTEGRAT.

Patch retroactiv aplicat pe C02, C03, C04 (HTML-Studiu + Editor-Studiu).
C05 era deja corect. Gate v20 PASS pe toate.

================================================================================

**V31 = V30 + R-V03.59 (Highlighter persistent HTML-Video) + L150
(feature consumer aditiv vs livrabil nucleu) + patch retroactiv T1
(C02-C05 HTML-Video au highlighter activ, gate v20 PASS pe toate).**

ARHITECT a cerut feature de evidentiere persistenta pentru text in
HTML-Video. Selectie text mouse -> marcaj galben Trainity + text negru.
Click pe marcaj -> toggle off. Reset prin buton stanga-jos + tasta ESC.
Persistenta in localStorage per constructie.

Pattern R-V03.59 stabileste sablonul pentru featuri consumer aditive:
CSS snippet + JS snippet + script `inject_*.py` + marker anti-duble-init.
Cele 6 livrabile canonice raman intact. Gate v20 PASS dupa injectare.

C06+ vor primi automat highlighter la generare HTML-Video.

================================================================================

**V30 = V29 + R-V03.58 (arhivare extinsa la `checkout constructie`:
folder `assets/` + document `FILM-Excel-NN.docx` adaugate aditiv
celor 6 livrabile canonice).**

ARHITECT a cerut reintroducerea aditiva pentru arhivare: pozele
raman base64 inline in HTML-Video (functionale), DAR si in folder
assets/ separat (pentru refolosire/backup). Plus FILM.docx cu script
cinematic procedural pentru arhivare narativa.

Cele 6 livrabile canonice raman NEMODIFICATE. La checkout constructie,
arhiva contine acum 8 artefacte (6 livrabile + assets/ + FILM.docx).

`referinte/assets_canonice/` adaugat ca asset perpetuu (12 fisiere
exec-stage-1..6 × jpg + png, 7.5MB). Acelasi set de imagini este
copiat in assets/ pentru fiecare constructie.

Aplicare retroactiva pentru C02-C05: NU regenerate, doar la urmatoarea
ad-hoc. C06+ genereaza automat sub schema V30+.

Lectie L149: deciziile arhitectura artefacte pot fi aditive. Cand un
livrabil eliminat anterior devine necesar din nou, reintroducerea
trebuie sa fie aditiva, NU inlocuire.

================================================================================

**V29 = V28 + C05 V28 LIVRABIL CANONIC (L144 fix complet) + L148
(verificare diagnostice motor inainte de decizie majora).**

T1 SCAN + C05 = 100% canonice. Lansabile catre cursanti. Toate 5
constructii cu sume conservate, identitate coerenta, brand respectat,
gate V20 PASS, R-V03.55 + L142 + L143 PASS.

Lectie L148: cand motorul face observatii diagnostice despre alte
constructii livrate, ARHITECT verifica empiric inainte de decizie.
In V29 motorul a observat fals ca "C03 a copiat label-uri pilot" -
verificare empirica a aratat ca C03 V26 are label-uri specifice.
Observatia falsa nu a influentat decizia in V29, dar putea cere
regenerare inutila a C03.

================================================================================

**V28 = V27 + L146 (gate v20 PQ whitelist extins) + L147 (path bug minor)
+ T1 SCAN COMPLET (C01-C05 toate validate).**

Consolidare dupa regenerare paralela C03 V26 + C04 V27. Treapta T1
SCAN este acum completa sub sistem V26+. Toate cele 5 constructii
(C01 pilot, C02 V26, C03 V26, C04 V27, C05 V25) au livrabile
canonice cu sume conservate si gate v20 PASS.

Fix L146: gate_v20.py acum accepta termeni tehnici Power Query
canonici (Promoted Headers, Filtered Rows, Removed Duplicates,
Normalized Diacritics, etc.) in context PQ explicit. C04 trece de
la 4 erori fals pozitive la 0 erori.

================================================================================

**V27 = V26 + script SELF-CHECK + schema REAL aplicata corect.**

Bug descoperit V26: am livrat OUT-V26.zip cu script `pre_generation_check.py`
care folosea denumiri INVENTATE pentru câmpurile IDENTITATE_TEHNICA
(cover_label, cover_title, localStorage_keys) care nu existau în
`referinte/IDENTITATE-TEHNICA.md` real. Am reparat scriptul ulterior
in V26 (schema reala: nume_hero_caps_rand1, localStorage_studiu,
localStorage_video) - dar chat-urile CONSTRUCTIE active sau arhive
intermediare au continuat sa foloseasca scriptul VECHE.

Solutie V27:
1. Script publica versiunea proprie ca prima linie de output:
   `[pre_generation_check V27.1 - schema REAL]`
2. PROMPT_CHAT_CONSTRUCTIE forteaza motorul sa verifice prima linie
   inainte sa interpreteze exit code. Daca vede `V26.X - schema INVENTED`
   sau lipsa header, OPRESTE si cere reatasare arhiva.

Asta previne situatia in care un chat CONSTRUCTIE ruleaza scriptul
buggy si raporteaza fals pozitiv L142 cand IDENTITATE_TEHNICA e
populata corect cu schema reala.

Lectie L145: REGULILE HARD TREBUIE SA PUBLICE VERSIUNEA. Nu e suficient
sa scriu cod functional. Codul critic trebuie sa-si declare versiunea
asa cum si tu cand atasezi un fisier dai dimensiunea/data.

================================================================================

**V24 = V23 + PROBLEMELE pe pozitia 2 din 9 elemente SPEC + script
pre_generation_check.py executabil HARD.**

Recodificata a treia regula veche pierduta intre V19-V23: PROBLEMELE
PE CARE LE REZOLVA CONSTRUCȚIA este al doilea element inghetat
(intre INTRIGA si MIZA). Lista incitanta, utila si de efect, 3-5
probleme scurte. Logica narativa: paradox -> probleme recunoscute ->
miza castig.

Plus script `generatoare/pre_generation_check.py` care VERIFICA hard
status SPEC C{NN} si returneaza exit code blocant. Motorul ruleaza
scriptul, nu citeste regula soft. Transforma R-V03.55 din regula
SOFT in regula HARD (executabila).

================================================================================

**V23 = V22 + R-V03.56 (SPEC FREEZING format grila cu 3 variante creative).**

Recodificata a doua regula veche pierduta intre V19-V22: motorul propune
3 variante creative la inghetare SPEC (INTRIGA/MIZA/MANTRA/etc.),
ARHITECT alege A/B/C sau cere "alte 3". Convenția folosita la C01-C04
inghetate, pierduta tacut la C05.

Descoperit empiric: motorul C05 a intrebat "care e INTRIGA TA?" -
inversare a principiului ARHITECT/CONSTRUCTOR. Motorul propune,
ARHITECT decide. R-V03.56 codifica acest format obligatoriu.

================================================================================

**V22 = V21 + R-V03.55 (SPEC inghetat blocant inainte de generare).**

Recodificata regula "veche" Trainity care s-a pierdut tacut intre V19-V21:
inainte de generarea unei constructii, SPEC C{NN} trebuie sa aiba
status INGHETAT in SISTEM. Motorul refuza generarea daca SPEC e
NEGENERAT. Improvizarea SPEC in chat CONSTRUCTIE strica unitatea
pedagogica.

Descoperit empiric: Bogdan a dat "Genereaza CONSTRUCTIA 05" cu SPEC C05
NEGENERAT, motorul a inceput sa improvizeze (a creat Date_MASTER-C05).
V22 codifica explicit BLOCANT: motorul verifica status SPEC inainte
de orice generare.

================================================================================
# SISTEM TRAINITY — V21 (25 mai 2026, STABIL EMPIRIC)

**V22 = V21 + R-V03.55 (SPEC inghetat blocant). V21 = V20 stabilizat empiric.** Validat pe 3 constructii consecutive
C02 + C03 + C04 cu GATE V20 PASS toate 6 clase. Nu sunt schimbari de
reguli fata de V20 - doar consolidare in brain a faptului ca cele
3 reguli critice (R-V03.52 livrare incrementala, R-V03.53 gate sheet
OUTPUT canonic, R-V03.54 lectura selectiva + COPY+MODIFY) functioneaza
empiric pentru construcții cu HTML-Video ~800KB.

Urmatoarele schimbari arhitecturale doar daca apare un esec REAL nou
in T2 sau T3.

================================================================================

# SISTEM TRAINITY — V11 (25 mai 2026)

================================================================================
## NOUTATI V11 FATA DE V10
================================================================================

### R-V03.19 PPT ELIMINAT DIN PRODUCTIE

PPT abrogat ca livrabil generat. FILM ramane artefact extern produs cu OBS
din HTML-VIDEO (nu generat de motorul Trainity).

SCHEMA CANONICA V11 = 7 LIVRABILE AUTOMAT (in loc de 8):
1. Date-Input-Excel-NN-NUME.xlsx
2. Date-Output-Excel-NN-NUME.xlsx
3. HTML-Studiu-Excel-NN-NUME.html
4. HTML-Editor-Studiu-Excel-NN-NUME.html
5. HTML-Video-Excel-NN-NUME.html
6. HTML-Editor-Video-Excel-NN-NUME.html
7. Creativ-Excel-NN-NUME.txt (prompturi Banana 2 pentru imagini exec)

Plus livrabil derivat OPT-IN:
- HTML-Video-Excel-NN-NUME-Autonom.html (single-file cu imagini base64,
  generat la cerere)

### R-V03.20 EXECUTIVE SHOW IMBEDDED IN HTML-VIDEO

HTML-VIDEO se incheie cu 8 slide-uri la finalul flow-ului:
- 1 slide tranzitie CONCLUZII (dupa Final motto)
- 6 slide-uri etape executive (imagine fundal cinematic Banana 2 cu Ken Burns
  9s, overlay gradient, cifra ghosted gigantica NN, label ETAPA, emotie, titlu
  monumental, fraza thriller-keynote memorabila)
- 1 slide closing apoteotic (negru pur, motto + semnatura Bogdan Tarla
  Dr.Excel pe 2 randuri verticale centrate)

### R-V03.21 CINEMATIC SHOW RULES

- safe center flexbox modern (fallback automat la flex-start cand continut
  depaseste)
- Ken Burns slow zoom 9s (transform scale 1.08 -> 1.0) cu clasa kb-go aplicata
  via requestAnimationFrame dupa force reflow
- Primele 3 fragmente exec apar automat la 350/630/910ms (cinematic intro)
- Fragmentul 4 (fraza memorabila) apare la prima sageata
- body.exec-mode ascunde topbar/panel/HUD/stage-nav-fixed pe exec (fullscreen
  cinematic pur)

### R-V03.22 VOCABULAR EXEC MINIMAL

Slide-uri exec etapa contin DOAR:
1. Label etapa (ex. "ETAPA 01")
2. Emotie (ex. "ADEVARUL BRUTAL")
3. Titlu monumental (ex. "REALITATE")
4. Fraza thriller-keynote memorabila

ZERO bullet-uri pe exec.

### R-V03.23 NAVIGARE BIDIRECTIONAL FRAGMENTE

- Inainte (sageata dreapta / tap / swipe): afiseaza fragment urmator. Cand
  fragmente epuizate -> trece la slide urmator
- Inapoi (sageata stanga): retrage fragment cu fragment in slide
- Pe exec: daca fragIdx <= 1 (doar label vizibil), trece la slide anterior cu
  toate fragmentele lui revealate

### R-V03.24 HUD ELIMINAT DIN HTML-VIDEO

Banda HUD (ETAPA N/6 + 00/18 + bara progres) eliminata din DOM. Panel-ul
lateral dreapta este unica sursa de progres.

### R-V03.25 ZERO SCROLL PE HTML-VIDEO

.screen { overflow: hidden }. Toate cele 53 slide-uri din FLOW incap pe un
singur ecran (1366x768 garantat). justify-content: safe center.

### R-V03.26 ETAPA #7 CONCLUZII IN PANEL

Adaugata manual in renderPanel ca etapa suplimentara dupa cele 6 STAGES.
Activa pe toate slide-urile final/conclusion/executive.

### R-V03.27 CLOSING EXEC APOTEOTIC

4 elemente verticale centrate:
- Motto: (galben mic, deasupra)
- Mai intai structura. Apoi orice. (alb + galben monumental)
- Divider galben 60px
- Semnatura pe 2 randuri:
  * TRAINITY · SISTEMUL 02 EXCEL (rand 1, gri)
  * BOGDAN TARLA (DR.EXCEL) (rand 2, alb + galben pe Dr.Excel)

### R-V03.28 HERO CA SLIDE COPERTA

Hero ramane slide separat in FLOW (state.flowIdx = -1) cu:
- Prelabel: CONSTRUC,TIA NN EXCEL (galben, 14-20px, letter-spacing 4.5px)
- Titlu monumental: NUME / CONSTRUCTIE (alb, clamp 44-110px)
- Hook frag 1 (thriller)
- Sub frag 2 (explicativ)
- Topbar ascuns complet prin body.hero-mode class (CSS: display: none)
- Buton sticky-jos stanga "Incepem constructia ->" apare DOAR cand toate
  fragmentele sunt expuse

### R-V03.29 CONVENTIE DENUMIRE LIVRABILE IN ROMANA

Toate fisierele livrate au denumiri romanesti standard:

```
Date-Input-Excel-NN-NUME.xlsx           (era INPUT-Excel)
Date-Output-Excel-NN-NUME.xlsx          (era OUTPUT-Excel)
HTML-Studiu-Excel-NN-NUME.html          (era HTML-STUDY-Excel)
HTML-Video-Excel-NN-NUME.html           (era HTML-VIDEO-Excel)
HTML-Video-Excel-NN-NUME-Autonom.html   (era STANDALONE)
HTML-Editor-Studiu-Excel-NN-NUME.html   (era HTML-EDIT-STUDY)
HTML-Editor-Video-Excel-NN-NUME.html    (era HTML-EDIT-VIDEO)
Creativ-Excel-NN-NUME.txt               (era CREATIVE-Excel)
assets/cover-yt-excel-NN-NUME.jpg       (thumbnail YouTube 1280x720)
assets/infografic-excel-NN-NUME.jpg     (infografic 10-sec 1920x1080)
assets/exec-stage-1..6.jpg              (6 imagini Banana 2 3:2 cinematic)
```

Link-urile interne (cover-meta, JS download) actualizate.

### R-V03.30 EDITOR PAGINA VIE V2.3

Overlay JS injectat in HTML-Studiu si HTML-Video care produce
HTML-Editor-Studiu-Excel-NN-NUME.html si HTML-Editor-Video-Excel-NN-NUME.html.

Caracteristici:
- Pagina ramane functionala normal (Hero, navigare, slide-uri dinamice, exec)
- contenteditable=true pe textele vorbite via selectori CSS din list
- Wrapper .edit-wrap cu buton x rosu SIBLING (NU copil) - evita aparitia in
  textContent
- Hover pe container (.anomaly-card, .inv-item, .final-block, slide exec) =>
  buton "ȘTERGE" rosu in colt sus-dreapta cu confirmare
- MutationObserver detecteaza render() dinamic si re-aplica editor pe
  elementele noi (Explain/Step/Prompt/Switch/Verify rendered runtime)
- Ctrl+Z = Undo nativ browser in contenteditable
- Capture phase blocheaza click-tap pe stage + keydown global cand cursor in
  contenteditable (altfel sageata sau Space ar avansa fragmentele)
- NO background change pe focus (pastram lizibilitatea textelor rosii pe
  fundal rosu)
- Toolbar slim 37px sticky-jos cu Export HTML + Reset
- Export filename: HTML-Editor-NN-NUME-Editat.html (curata toolbar +
  contenteditable + wrappers)

### R-V03.31 CHECKOUT BRAIN INTEGRITATE FORMAT

Checkout brain in chat BRAIN produce OUT-VNN.zip cu structura canonica
identica cu V10 si anterior:
- brain.md (regenerat COMPLET cu sesiunea noua la inceput + tot ce era)
- SISTEM_TRAINITY.md (regenerat cu modificari V11 integrate)
- PROMPT_CHAT_NOU.txt (updatat la VNN)
- generatoare/ (build_cNN_vM.py + gen_film_cNN.js + gen_ppt_cNN.js + test_cNN.js
  + verifica_cNN.py + README_VMM_PATTERN.md) - PASTRATE
- referinte/ (SABLON-HTML-Trainity.html + EDITOR-CSS.txt + EDITOR-JS.txt +
  RAPORT-VERIFICARE-CANONIC.md) - PASTRATE
- livrabile_C01..C20/ (cele 7 livrabile canonice V11 + assets/)

INTERZIS: kit-uri noi cu scripturi inventate ne-existente fizic in folder.
INTERZIS: snapshot one-shot in loc de matrita persistenta.
build_c01_v5.py ramane generatorul real prin COPY-MODIFY R-V02.6.

================================================================================
## END NOUTATI V11
================================================================================

# SISTEM_TRAINITY.md

Sistem operational de productie Trainity. Sursa unica de adevar tehnic.
Reconstruit de la zero pe arhitectura oficiala (mai 2026). Versiune 1.0.

Trainity NU preda aplicatii. Trainity construieste moduri de lucru,
mecanisme operationale, workflow-uri augmentate cu AI, sisteme de business
pregatite pentru 2030.

Viziunea centrala: NU predam aplicatii. Construim moduri de lucru.

================================================================================

# PARTEA I - ARHITECTURA SISTEMULUI

## A. CELE 5 TREPTE

Progresia sistemului acopera tot traseul de la date brute la sistem autonom.
Fiecare treapta maturizeaza operational ce a construit treapta anterioara.

### TREAPTA 1 - STRUCTURA (C01-C04)
- Ce construieste: transforma exporturile ERP in baze curate, continue,
  controlabile, BI-ready. Elimina ambalajul, haosul structural,
  contaminarea, instabilitatea.
- Rol: Excel trebuie mai intai sa inteleaga datele. Fara structura,
  formulele mint, dashboard-urile induc in eroare, automatizarea amplifica
  haosul.
- Tehnologie dominanta: Power Query (nu ca feature Excel, ci ca motor de
  maturizare operationala).
- Hook 1: "Datele nu sunt haos. Ambalajul este."
- Hook 2: "Arata ca tabel. Nu este tabel."
- Hook 3: "Excel nu poate calcula un export pe care nici macar nu il intelege."
- Mantra 1: "Nu schimbam fisierul. Maturizam acelasi set de date."
- Mantra 2: "Nu reconstruim tabelul. Il facem controlabil."
- Mantra 3: "SUM si AGGREGATE trebuie sa spuna aceeasi poveste."
- Emotii: eliberare din haos / control structural / stabilizare.
- Mize: automatizarea unui export instabil produce haos mai rapid; orice
  dashboard peste structura gresita produce incredere falsa; Excel nu poate
  analiza ce nu poate intelege structural.
- Rezultate: date curate continue BI-ready; structura stabila pentru calcul
  analiza dashboard automatizare; baza controlabila si refreshabila.

### TREAPTA 2 - CUNOASTERE (C05-C08)

REDENUMIRE V24 (25.05.2026, decizie Bogdan in chat SPEC C05): T2 CALCUL
->  T2 CUNOASTERE. Vezi L139. Numele vechi "CALCUL" a devenit invalid
dupa L136 (T2 = profilare/cunoastere descriptiva, NU KPI business).
Nume nou exact: "CUNOASTERE" (categoriala, numerica, temporala, relationala).

REASEZARE V24 (25.05.2026, decizie Bogdan in chat SPEC C05): T2 NU este
"atribuie semnificatie business" (aia e T3). T2 este PROFILAREA SETULUI -
operatorul face cunostinta cu datele la nivel macro, descriptiv,
multidimensional. Imagine din satelit, nu inspectie pe rand. Calculul din
T2 este calcul descriptiv (counts, sums, averages, distributions, profil
temporal), NU KPI executiv.

- Ce construieste: profilul complet al setului de date (continut, marime,
  cronologie, integrare). Operatorul iese din T2 cu fisa setului in mana,
  pregatit sa atribuie semnificatie decizionala in T3.
- Rol: operatorul descopera DIN CE e facut setul, CAT de mare e, CUM se
  distribuie in timp, CUM se leaga cu alte seturi. Nu inventeaza categorii
  business, descopera categoriile care exista deja in date si le numara.
- Tehnologie dominanta: Excel Formula Engine + AI Prompting (COUNTIF,
  COUNTIFS, COUNTA, UNIQUE, SORT, FILTER, FREQUENCY, SUM, AVERAGE, MEDIAN,
  MIN, MAX, STDEV, dynamic arrays, prompt natural pentru profilare rapida).
  AI accelereaza profilarea, operatorul valideaza profilul si il fixeaza
  ca livrabil auditabil.
- Hook 1: "Date corecte nu inseamna date cunoscute."
- Hook 2: "Excel are 3.300 de randuri. Operatorul nu stie cati clienti unici."
- Hook 3: "Inainte sa decizi pe set, fa-ti cunostinta cu setul."
- Mantra 1: "Cunoasterea setului inainte de interpretarea setului."
- Mantra 2: "Profilul descriptiv inainte de judecata decizionala."
- Mantra 3: "Nu inventam categorii. Le descoperim."
- Emotii: curiozitate metodica / claritate descriptiva / control prin
  cunoastere.
- Mize: fara profil, deciziile T3 se iau pe set necunoscut; analiza fara
  cunoastere descriptiva produce concluzii pe iluzii; categoriile inventate
  in cap sunt fragile, categoriile descoperite in date sunt auditabile.
- Rezultate: fisa completa a setului (profil de continut + masuratori +
  cronologie + consolidare); set cunoscut multidimensional; baza
  descriptiva pregatita pentru atribuire de semnificatie in T3.

INLANTUIREA CELOR 4 CONSTRUCTII T2 (intrebari-mama):
- C05 CLASIFICAREA DATELOR    -> "Din ce e facut setul?" (profil de continut)
- C06 KPI & CALCULE           -> "Cat de mare e setul?" (profil de marime)
- C07 LOGICA TEMPORALA        -> "Cum se distribuie in timp?" (profil temporal)
- C08 PREGATIREA PENTRU ANALIZA -> "Cum aduc mai multe seturi impreuna?"
                                   (consolidare pentru T3)

DIFERENTA T2 vs T3 (lectie L136 codificata):
T2 raspunde la "din ce e facut" / "cat masoara" / "cum se desfasoara
in timp" - intrebari DESCRIPTIVE. T3 raspunde la "ce inseamna" / "care
e prioritar" / "unde pierd / unde castig" - intrebari DECIZIONALE.
"Clasificare" in C05 = inventar de categorii existente, NU atribuire de
categorii noi. Atribuirea decizionala (segment A/B/C strategic,
prioritate executiva) traieste in T3-T4, cand exista obiectiv de
analiza.

### TREAPTA 3 - ANALIZA (C09-C12)
- Ce construieste: transforma datele, KPI-urile, modelele in insight,
  prioritizare, claritate, decizie.
- Rol: datele incep sa spuna povestea business-ului. Descoperim ce
  functioneaza, ce se degradeaza, unde pierdem, unde castigam, ce conteaza.
- Tehnologie dominanta: Power Pivot + Data Model (Pivot Tables,
  relationships, measures, dimensions, DAX controlat, model thinking).
- Hook 1: "Problema nu este lipsa datelor. Problema este zgomotul."
- Hook 2: "Datele nu decid. Operatorul decide."
- Hook 3: "Business-ul nu pierde din lipsa de rapoarte. Pierde din lipsa de claritate."
- Mantra 1: "Analiza buna reduce zgomotul."
- Mantra 2: "Pivotul nu decide. Operatorul decide."
- Mantra 3: "Fara context, toate rapoartele par corecte."
- Emotii: claritate strategica / descoperire / control intelectual.
- Mize: fara analiza dashboard-ul devine decor; datele fara prioritizare
  produc paralizie; business-ul pierde cand nu vede ce conteaza.
- Rezultate: date transformate in insight operational; probleme prioritizate
  si cuantificate; analiza pregatita pentru decizie executiva.

### TREAPTA 4 - RAPORTARE (C13-C16)
- Ce construieste: transforma analiza in dashboard-uri, cockpit-uri
  executive, control vizual, sisteme rapide de decizie.
- Rol: raportul inceteaza sa mai fie document. Devine interfata de comanda.
- Tehnologie dominanta: Dashboards + BI UX (charts, KPI panels, slicers,
  scorecards, executive dashboards, narrative BI, visual hierarchy).
- Hook 1: "Directorul nu citeste tabelul."
- Hook 2: "Raportul nu trebuie sa impresioneze. Trebuie sa decida."
- Hook 3: "Dashboard-ul bun reduce timpul de reactie."
- Mantra 1: "Vizualizarea trebuie sa accelereze decizia."
- Mantra 2: "Un dashboard frumos fara logica produce incredere falsa."
- Mantra 3: "Raportul devine cockpit."
- Emotii: control executiv / viteza / incredere operationala.
- Mize: managementul nu poate decide in haos vizual; dashboard-ul gresit
  produce prioritati gresite; controlul lent produce reactii lente.
- Rezultate: cockpit executiv clar si rapid; dashboard-uri orientate spre
  decizie; control operational vizual in timp real.

### TREAPTA 5 - AUTOMATIZARE (C17-C20)
- Ce construieste: transforma raportarea intr-un sistem autonom, repetabil,
  predictibil, scalabil.
- Rol: business-ul inceteaza sa mai depinda de copy-paste, versiuni
  multiple, panica operationala, reconstructie manuala.
- Tehnologie dominanta: Refresh Architecture + Operational Flows (Power
  Query refresh, reusable flows, standardizare operationala, orchestrare).
- Hook 1: "Daca trebuie sa repari din nou, nu ai construit sistemul."
- Hook 2: "Raportarea nu trebuie reconstruita in fiecare luni."
- Hook 3: "Datele intra. Sistemul ruleaza."
- Mantra 1: "Nu automatizam task-uri. Construim mecanisme."
- Mantra 2: "Refresh-ul trebuie sa fie predictibil."
- Mantra 3: "Raportarea trebuie sa urmeze sistemul, nu memoria operatorului."
- Emotii: stabilitate operationala / calm / putere.
- Mize: un proces manual nu poate sustine un business 2030; fragilitatea
  produce panica operationala; versiunile multiple distrug increderea.
- Rezultate: raportare predictibila si refreshabila; flux standardizat si
  repetabil; sistem Trainity pregatit pentru scalare si AI.

## B. MAPAREA CELOR 20 DE CONSTRUCTII (fixa, referinta pentru comenzi)

```
T1 STRUCTURA    C01 STRUCTURA TABELELOR
                C02 CONTROLUL DATELOR
                C03 AUDITAREA DATELOR
                C04 NORMALIZAREA DATELOR
T2 CUNOASTERE  C05 CLASIFICAREA DATELOR
                C06 KPI & CALCULE
                C07 LOGICA TEMPORALA
                C08 PREGATIREA PENTRU ANALIZA   [pod T2->T3, consolidare pentru modelare]
T3 ANALIZA      C09 EXPLORAREA DATELOR          [drill-down, slice, segmentare, descoperire]
                C10 ANALIZA PIVOT
                C11 DATA MODEL
                C12 PRIORITIZARE EXECUTIVA       [top probleme/clienti, Pareto, risc, focus]
T4 RAPORTARE    C13 VIZUALIZARE EXECUTIVA        [charts, comparare, visual hierarchy]
                C14 DASHBOARD EXECUTIV           [cockpit complet, interactivitate, slicers]
                C15 POVESTEA DATELOR             [narrative BI, insight, storytelling]
                C16 CONTROL INSTANT            [compresie operationala extrema]
T5 AUTOMATIZARE C17 RAPORTAREA DE LUNI DIMINEATA
                C18 ELIMINAREA VERSIUNILOR
                C19 PROCEDURA DE RAPORTARE
                C20 SISTEMUL TRAINITY            [asamblare completa: orchestration, handover]
```

## B-bis. REVIZUIRE GLOBALA PENTRU ECHILIBRU (Pasul 2, decizii Bogdan)

Cele 20 de constructii au fost revizuite global ca sistemul sa acopere
echilibrat toate zonele, fara teme suprareprezentate. Decizii:

1. C08 redefinit: din "CONSOLIDAREA DATELOR" (calcul pur, rupea ADN-ul T2)
   in "PREGATIREA PENTRU ANALIZA". Ramane ultima din T2 dar cu rol explicit
   de POD T2->T3: consolidare pentru modelare si analiza, nu calcul. Rezolva
   tensiunea fara sa lungeasca/PQ-greleze T1.

2. AI ramane TRANSVERSAL (infrastructura invizibila), NU constructie
   dedicata. O constructie "despre AI" ar distruge ADN-ul (tutorial AI,
   prompt engineering, hype). In schimb: capitol separat in SISTEM,
   "REGULILE AI TRAINITY" (PARTEA III) - AI codificat clar ca infrastructura,
   nu subiect.

3. C09 vs C12 separate prin ENERGIE, nu doar tema: C09 = EXPLORAREA DATELOR
   (explorare: drill-down, slice, segmentare, navigare, descoperire); C12 =
   PRIORITIZARE EXECUTIVA (decizie: top probleme, top clienti, Pareto, risc,
   focus management). Una exploreaza, cealalta decide.

4. T4 nu mai e dashboard x3. C16 schimbat din "CONTROL OPERATIONAL" (suna
   tot dashboard) in CONTROL INSTANT. CONCEPT documentat explicit (sa nu
   derive inapoi): C16 NU e raport de o pagina sau executive summary clasic.
   Este COMPRESIE OPERATIONALA EXTREMA - cockpit ultra-comprimat: zeci de
   taburi, dashboard-uri, grafice, KPI, filtre, surse multiple comprimate
   intr-o singura interfata clara, rapida, controlabila, fara zgomot.
   Anti-clutter, anti-BI-porn. Capcane de nume evitate constient: varianta
   "panou/tablou/control operational" = dashboard (coliziune C14); varianta
   "sinteza/rezumat de o pagina" = PDF corporate/consulting (rupe ADN).
   "Instant" muta accentul de la suprafata vizuala la viteza de reactie.
   Progresie T4 coerenta (4 acte cognitive, NU 4 dashboard-uri): C13 vezi ->
   C14 navighezi -> C15 intelegi -> C16 reactionezi instant.

5. C20 SISTEMUL TRAINITY pastrat ca payoff al sistemului, dar concretizat:
   "asamblarea sistemului complet" (refresh final, orchestration, cockpit
   complet, flow complet, integrare, simulare reala, handover operational).
   Constructie reala cu 8 livrabile, NU epilog filozofic.

Echilibru confirmat OK (nemodificat): T1 progresie curata structura->control
->audit->normalizare; T5 refresh/versiuni/procedura/sistem; repartitie
4+4+4+4+4 pe trepte.

## C. CELE 6 ETAPE STANDARD (schelet procedural macro, fix, obligatoriu)

Orice constructie Trainity contine EXACT aceste 6 etape, in aceasta ordine
obligatorie. Structura ramane identica procedural; emotia, tensiunea,
payoff-ul, tipul de risc si tipul de control se personalizeaza per
constructie.

### ETAPA 1 - REALITATE
- Rol procedural: expune problema reala, haosul, riscul, contaminarea,
  instabilitatea, situatia operationala curenta, fara cosmetizare.
- Rol psihologic: tensiune, expunere, disconfort, suspiciune, constientizare.
  Utilizatorul simte "Avem o problema reala."
- Contine: context operational, input real, risc concret, suma de referinta,
  volum, simptome, haos vizibil sau invizibil.
- Interzis: explicatii lungi, teorie, tutorial, setup plictisitor.

### ETAPA 2 - INVESTIGATIE
- Rol procedural: operatorul investigheaza realitatea ASISTAT DE AI, inainte
  de transformare. Pune intrebari, sondeaza datele, cauta deviatii, verifica
  ipoteze, cere explicatii, investigheaza riscuri, incearca sa inteleaga ce
  trebuie controlat sau transformat.
- Rol psihologic: control, autoritate, claritate dobandita prin intelegere.
  Utilizatorul simte "Incep sa inteleg ce se intampla cu adevarat."
- ADN CRITIC: promptul natural ramane central, dar rolul lui se schimba - NU
  mai e "comanda de executie", ci INSTRUMENT DE INVESTIGATIE OPERATIONALA. In
  aceasta etapa NU se transforma inca sistemul profund. Mai intai se intelege.
  Abia dupa INVESTIGATIE urmeaza TRANSFORMARE.
- Filozofie Trainity: NU transmitem "scrie prompt si AI face magie".
  Transmitem "operatorul investigheaza business-ul asistat de AI, apoi
  construieste control". Aproape de business intelligence real, operational
  thinking, forensic mindset, mod de lucru 2030.
- Interzis: prompt engineering complicat, AI hype, pseudo-cod, syntax dump,
  saltul direct la transformare fara intelegere.

### ETAPA 3 - TRANSFORMARE
- Rol procedural: sistemul opereaza. Power Query transforma, Excel
  calculeaza, AI genereaza, modelul ruleaza, dashboard-ul se construieste.
- Rol psihologic: putere, progres, acceleratie, satisfactie operationala.
  Utilizatorul simte "Haosul incepe sa se organizeze."
- Contine: transformari vizibile, diferente clare before/after, logica
  vizibila, progres masurabil, schimbare operationala reala.
- Interzis: pasi inutili, micro-click-uri, explicatii lungi, interactiuni
  repetitive.

### ETAPA 4 - VERIFICARE
- Rol procedural: validam integritatea, consistenta, logica, rezultatul,
  adevarul operational. Sistemul NU are incredere orbeste in AI sau formule.
- Rol psihologic: suspiciune controlata, tensiune, confirmare, incredere
  castigata. Utilizatorul simte "Putem avea incredere?"
- Contine: verificari vizibile, concrete, demonstrabile, operationale.
- Interzis: validari decorative, verificari fake, confirmari fara dovada.

### ETAPA 5 - STABILIZARE
- Rol procedural: eliminam fragilitatea, dependenta de interventii manuale,
  haosul repetitiv, instabilitatea. Sistemul devine predictibil, repetabil,
  robust.
- Rol psihologic: calm, control, stabilitate, siguranta operationala.
  Utilizatorul simte "Sistemul rezista."
- Contine: standardizare, reguli, fluxuri stabile, reutilizare, refresh
  predictibil, control operational.
- Interzis: improvizatie, solutii fragile, workaround-uri.

### ETAPA 6 - CONFIRMARE
- Rol procedural: certificam rezultatul, suma, integritatea, sistemul,
  controlul final. Constructia este validata operational.
- Rol psihologic: payoff, satisfactie, control, incredere finala.
  Utilizatorul simte "Sistemul functioneaza."
- Contine: rezultat final, before/after clar, validare, payoff vizual,
  concluzie operationala.
- Interzis: final slab, concluzie generica, ending fara impact.

## D. RITMUL CINEMATIC (ortogonal pe cele 6 etape, NU 1:1)

Cele 6 etape = scheletul procedural macro (progresia operationala,
maturizarea sistemului).

HOOK -> DEMO -> CONTROL -> REVEAL = ritmul cinematic si emotional care
trebuie sa existe IN INTERIORUL fiecarei etape (consum premium, tensiune,
payoff).

Cele doua sisteme NU se inlocuiesc si NU se mapeaza 1:1. Coexista. Exemplu
in etapa REALITATE: HOOK = expunerea riscului; DEMO = vedem problema in
date; CONTROL = fixam referinta; REVEAL = descoperim deviatia reala.
Acelasi ritm poate exista in INVESTIGATIE, TRANSFORMARE, VERIFICARE,
STABILIZARE, CONFIRMARE.

Regula ADN: NU tutorial liniar. Progres procedural (6 etape) + ritm
cinematic continuu (HOOK->DEMO->CONTROL->REVEAL in fiecare etapa) =
consumul premium, tensiunea si experienta cinematica Trainity.

## E. LIVRABILE (8, fix, ZERO PDF) [V05 - EXTINS prin R-V03.1 + R-V03.2 + R-V03.3 + R-V03.4 + R-V03.5]

Fiecare constructie produce EXACT 8 livrabile [V05 nomenclatura R-V03.5]:
1. INPUT-Excel-NN-Nume.xlsx
2. OUTPUT-Excel-NN-Nume.xlsx
3. HTML-STUDY-Excel-NN-Nume.html (study mode pentru cursant)
4. HTML-EDIT-STUDY-Excel-NN-Nume.html (study WYSIWYG editor)
5. HTML-VIDEO-Excel-NN-Nume.html (broadcast mode pentru filmare, R-V03.1)
6. HTML-EDIT-VIDEO-Excel-NN-Nume.html (video WYSIWYG editor, R-V03.3)
7. FILM-Excel-NN-Nume.docx
8. PPT-Excel-NN-Nume.pptx

HTML-STUDY este livrabilul central pentru invatare: document complet cu cele
6 etape, anomaly-grid, prompturi, verificari, MOTTO. Pentru cursant. Voce
narativa: persoana a 2-a singular (R-V03.4).

HTML-EDIT-STUDY adauga peste HTML-STUDY un strat WYSIWYG (bara TRAINITY
EDITOR, FAB, contenteditable, butoane sterge, undo/redo, export). Lifecycle
V01: generare AUTOMATA la `Genereaza CONSTRUCTIA NN`. Comanda
`Genereaza HTML-EDIT-STUDY` ramane doar pentru regenerare punctuala.
Test Playwright 5 viewporturi = blocant in Gate 1 extins. Storage key:
`trainity_cNN_study_edits_v1`.

HTML-VIDEO (broadcast mode) este destinat EXCLUSIV filmarii video a
constructiei. Distinct de HTML cockpit: ecrane scenice separate (nu scroll
lung), continut ancorat top + butoane prev/next fixe bottom, panel dreapta
cu lista etape clickabila + buton "Mergi la pas sărit" portocaliu in
topbar. Sapte ecrane: Hero / Explain / Step / Prompt / Switch / Verify /
Final. Cod culori canonic (vezi R-V03.1). Pilot validat:
livrabile_C01/HTML-VIDEO-Excel-01-Structura.html.

HTML-EDIT-VIDEO adauga peste HTML-VIDEO acelasi strat WYSIWYG universal
ca HTML-EDIT-STUDY (R-V03.3): bara TRAINITY EDITOR sus, FAB,
contenteditable pe elementele marcate `data-editable`, butoane sterge,
undo/redo, export HTML. Lifecycle AUTOMAT (paritate R-V01.3). Storage keys
izolate: `trainity_cNN_video_v1` (progres filmare, mostenit) +
`trainity_cNN_video_edits_v1` (continut editat) +
`trainity_cNN_video_deleted_v1` (ecrane sterse) (R-V02.5 extins).
Clasa `.editor-active` pe body suspenda regula video `user-select: none`
pe zonele editabile. Stage padding-top ajustat de la 64px la 114px
(50px bara editor + 64px ancorare originala). Butoanele prev/next raman
absolute bottom 40px (neafectate). Comanda `Genereaza HTML-EDIT-VIDEO`
pentru regenerare punctuala.

**R-V03.4 VOCE NARATIVA DIVERGENTA COCKPIT vs BROADCAST [V05]:** HTML
cockpit (study mode) si HTML-VIDEO (broadcast mode) folosesc voci narative
DIFERITE pentru aceeasi constructie. NU este eroare, este conventie:

- **HTML cockpit + HTML-EDITABIL:** persoana a 2-a singular (imperativ +
  indicativ). Cursantul face singur. Ex: `Deschide exportul ERP brut`,
  `Selectează coloana`, `Verifică pașii aplicați`. Voce de comanda directa
  catre cursant.

- **HTML-VIDEO + HTML-VIDEO-EDITABIL:** persoana a 3-a plural (noi).
  Naratorul/operatorul filmeaza vorbind in numele sistemului. Ex:
  `Deschidem exportul ERP brut`, `Selectăm coloana`, `Verificăm pașii
  aplicați`. Voce de ghid colectiv.

Aplicare obligatorie in HTML-VIDEO:
1. **Title-uri pasi** in `STAGES[].steps[].title` la persoana a 3-a plural
2. **Instr-uri** in `STAGES[].steps[].instr` la persoana a 3-a plural;
   formele reflexive reformulate (`asigură-te` -> `ne asigurăm`,
   `nu te uita` -> `nu ne uităm`, `lasă-l` -> `îl lăsăm`)
3. **Hook** (`STAGES[].hook`) cu verbe persoana 2 = transformat
4. **Next** (`STAGES[].next`) = deja la persoana 3 plural in conventia
   sistemului (`Deschidem`, `Predăm`)
5. **Hero hook + sub** cu verbe persoana 2 = transformate
6. **Switch titlu** = `Mergem în Excel` (NU `Mergi`)
7. **Switch sub** = `Demonstrăm rezultatul, apoi revenim`
8. **Step callout** = `Acum mergem în Excel`
9. **Verify sub nevalidat** = `Verificăm în Excel că toate cele trei
   intervenții s-au confirmat`
10. **Buton CTA Hero** = `Începem construcția →` (NU `Începe`)
11. **Buton topbar pas sărit** = `Mergem la pas sărit` (NU `Mergi`)

Exceptii admise (NU se transforma) in HTML-VIDEO:
- **PROMPTS[].text** (textul promptului Copilot) = destinatie tehnica AI,
  vorbesti cu AI-ul, persoana a 2-a corecta (`Analizează structura...`,
  `Construiește un flux...`)
- **PROMPTS[].meta** = descriere comportament AI, ramane la persoana 3
  singular (`AI investighează. Nu modifică. Nu decide.`)
- **Butoane UI Validează pasul / Validează etapa** = label de actiune UI
  pentru operator, NU narativ
- **Toast `Pasul X validat` / `Etapa X validată`** = feedback sistem
- **Final block** = persoana 1 plural (`Am separat realitatea de ambalaj`)
  = voce colectiva coerenta cu narativul a 3-a plural
- **Motto-uri si fraze-semnatura** = ramana ca atare (forma fixa de brand)

In HTML-EDITABIL si HTML-VIDEO-EDITABIL, textul ramane in vocea modului
parinte (cockpit a 2-a, broadcast a 3-a plural). Operatorul poate edita
WYSIWYG dar conventia ramane: nu transformi voce automatically la editare,
doar la generarea initiala.

## F. CONTINUITATE DATE: ZERO

Nicio continuitate intre constructii. Fiecare constructie are propriul set
de date, generat proaspat, niciodata mostenit (nici in interiorul treptei,
nici intre trepte). Continuitatea INPUT->OUTPUT exista DOAR in interiorul
unei constructii (OUTPUT deriva din INPUT prin transformarile constructiei).

## G. DESIGN (standardizat, obligatoriu)

Brutalist premium, enterprise, cinematic, control panel, curat, aerisit,
fara clutter, fara dashboard fake, fara AI hype, fara tutorial feeling.
Maximum per ecran: 1 accent galben major, 1 focus dominant, 1 payoff
principal. Interzis: wall text, clutter, dashboard fake, KPI fake, prea
multe boxuri, densitate excesiva.

================================================================================

## H. STRUCTURA DOCUMENTULUI (parti planificate)

- PARTEA I: Arhitectura (5 trepte, 20 constructii, 6 etape, ritm cinematic,
  livrabile, continuitate, design) - COMPLETA.
- PARTEA II: Definirea fiecarei trepte in detaliu (Pasul 3).
- PARTEA III: REGULILE AI TRAINITY (AI ca infrastructura invizibila
  transversala, NU subiect - decizia 2 din revizuirea globala). Se
  detaliaza la pasul potrivit.
- PARTEA IV: Definirea fiecarei constructii (Pasul 4).
- PARTEA V: Sablonul standard de constructie (Pasul 5).
- PARTEA VI-IX: Sabloane HTML / PPT / script video / INPUT-OUTPUT Excel
  (Pasii 6-9).
- PARTEA X: Prompturile finale pentru productia cu AI (Pasul 10).

SISTEM OPERATIONAL: Pasii 1-3+5-9 COMPLETI, motor minimal 5 comenzi +
standard estetic concret (tokeni C03 vechi). Pasul 4 absorbit in motor
(definire just-in-time). Identitatea celor 3 livrabile codificata definitiv.
Raman: Pasul 10 (prompturi finale), refacerea Catalogului. Sistemul poate
genera constructii.

================================================================================

# PARTEA II - DEFINIREA FIECAREI TREPTE (Pasul 3)

Fiecare treapta este un stadiu de maturizare operationala. Are criterii de
INTRARE (ce primeste), criterii de IESIRE (ce livreaza maturizat),
inlantuirea celor 4 constructii, rolul tehnologiei dominante si modul in
care cele 6 etape se manifesta specific pe treapta.

## TREAPTA 1 - STRUCTURA (C01-C04)

**Intrare:** export ERP brut - aparent tabel, real contaminat (subtotaluri,
anteturi multiple, blank-uri false, coloane ascunse, filtre mostenite,
ambalaj). Nimic nu e de incredere structural.

**Iesire:** baza curata, continua, controlabila, BI-ready. SUM = AGGREGATE.
Structura stabila pe care se pot construi calcul, analiza, dashboard,
automatizare fara ca ele sa amplifice haosul.

**Inlantuirea celor 4 constructii (maturizare progresiva):**
- C01 STRUCTURA TABELELOR - elimina ambalajul, reconstruieste continuitatea
  structurala. Excel incepe sa inteleaga datele.
- C02 CONTROLUL DATELOR - separa valid tehnic de corect operational.
  Marcheaza anomalii, NU repara, NU sterge.
- C03 AUDITAREA DATELOR - detecteaza contaminarea invizibila (whitespace,
  Unicode, false blanks, date ca text, entitati duble).
- C04 NORMALIZAREA DATELOR - transforma curatarea manuala in mecanism
  refreshabil. "Daca vine un export nou maine, sistemul rezista?"

**Rol tehnologie dominanta (Power Query):** nu ca feature Excel, ci ca
motor de maturizare structurala. Progresia: PQ transforma (C01) -> PQ +
logica detecteaza (C02) -> PQ audit engine (C03) -> PQ transformation
architecture refreshabila (C04).

**Cele 6 etape pe T1 (specific):**
- REALITATE: haos structural / logica falsa / contaminare invizibila /
  fragilitate operationala (dupa constructie).
- INVESTIGATIE: operatorul sondeaza exportul asistat de AI - "ce e ambalaj,
  ce e date reale?", "unde difera SUM de AGGREGATE?", "ce pare gol dar nu e?".
- TRANSFORMARE: reconstructie structurala / detectare anomalii /
  investigatie forensic / construirea mecanismului.
- VERIFICARE: SUM vs AGGREGATE / anomalii si exceptii / Unicode si
  contaminare / refresh si repetabilitate.
- STABILIZARE: structura stabila / reguli anti-recurenta / integritate
  auditabila / mecanism predictibil.
- CONFIRMARE: baza BI-ready, validata, pregatita pentru T2.

## TREAPTA 2 - CUNOASTERE (C05-C08)

**REDENUMIRE V24 (25.05.2026):** T2 CALCUL -> T2 CUNOASTERE. Vezi L139.

**REASEZARE V24 (decizie Bogdan 25.05.2026, chat SPEC C05):** T2 este
PROFILAREA SETULUI, NU atribuire de semnificatie business. Operatorul face
cunostinta cu datele la nivel macro: din ce sunt facute, cat masoara, cum
se desfasoara in timp, cum se integreaza cu alte surse. "Calcul" in
numele treptei se refera la calcul DESCRIPTIV (counts, sums, averages,
distributions), NU la KPI executiv. KPI executiv vine in T3-T4, cand
exista obiectiv de decizie.

**Intrare:** baza curata, continua, BI-ready de la T1. Date corecte
structural, dar necunoscute descriptiv - operatorul priveste 3.300 randuri
si nu poate spune cati clienti unici, cati distincti pe coloana,
care e granularitatea, care e intervalul temporal, care sunt extremele.
Datele exista, dar operatorul nu si-a facut cunostinta cu ele.

**Iesire:** fisa completa a setului - profil de continut (categorii
descoperite, frecvente, granularitate, valori rare) + profil de marime
(sume, medii, mediane, extreme, dispersie) + profil temporal (interval,
distributie lunara, varfuri, ritm) + set consolidat multi-sursa pregatit
pentru Data Model in T3. Operatorul iese cu setul CUNOSCUT
multidimensional, gata sa atribuie semnificatie decizionala.

**Inlantuirea celor 4 constructii (fiecare cu intrebarea-mama):**

- **C05 CLASIFICAREA DATELOR** -> "Din ce e facut setul?"
  Inventar de categorii existente, NU atribuire de categorii noi.
  Operatorul descopera cati unici per coloana, ce frecvente, ce
  granularitate, ce valori rare suspecte. Livrabil: fisa de profil de
  continut.
  Tehnologie: COUNTIF, COUNTIFS, COUNTA, UNIQUE, SORT, FILTER, FREQUENCY,
  prompt natural pentru profilare.

- **C06 KPI & CALCULE** -> "Cat de mare e setul?"
  Masuratori descriptive, NU KPI executiv. Sume, medii, mediane, intervale,
  extreme, deviatii, distributii. Operatorul afla forma numerica a setului.
  Livrabil: fisa de masuratori.
  Tehnologie: SUM, AVERAGE, MEDIAN, MIN, MAX, STDEV, SUMIFS, LARGE, SMALL,
  prompt natural pentru agregari descriptive.

- **C07 LOGICA TEMPORALA** -> "Cum se distribuie in timp?"
  Profil temporal descriptiv, NU trend analysis decizional. Interval de
  date, luni goale, varfuri, distributie pe zi a saptamanii, ritm. Nu
  raspunde "ce decid", raspunde "cum arata cronologic".
  Livrabil: fisa de profil temporal.
  Tehnologie: EOMONTH, EDATE, DATEDIF, WEEKDAY, ISOWEEKNUM, SUMIFS pe
  ferestre temporale, prompt natural pentru profil temporal.

- **C08 PREGATIREA PENTRU ANALIZA** -> "Cum aduc mai multe seturi impreuna?"
  POD T2->T3. Consolidare multi-sursa pentru modelare. Single source
  cunoscut multidimensional + structura comuna = baza pentru Data Model T3.
  Livrabil: set unic consolidat cu structura comuna.
  Tehnologie: Power Query reintrodus (dupa C04) pentru append/merge,
  standardizare keys, prompt natural pentru detectarea relatiilor.

**Rol tehnologie dominanta (Excel Formula Engine + AI Prompting):** AI
accelereaza profilarea (rapid, scalabil), operatorul valideaza profilul
(corect, util) si il fixeaza ca livrabil (auditabil, repetabil). Promptul
natural = accelerator procedural, NU gimmick AI. Pattern T2 uniform:
"intrebare descriptiva -> investigatie asistata AI -> validare critica
operator -> livrabil de profil auditabil".

**Cele 6 etape pe T2 (specific):**
- REALITATE: date corecte structural dar necunoscute descriptiv / operator
  in fata setului fara sa-l fi profilat niciodata / 3.300 randuri tac.
- INVESTIGATIE: operatorul interogheaza asistat de AI - "cati unici per
  coloana?", "care e granularitatea?", "care sunt extremele?", "cum se
  distribuie in timp?", "cum se leaga sursele?". Promptul natural =
  accelerator de profilare, NU comanda.
- TRANSFORMARE: profilare de continut (C05) / masurare descriptiva (C06) /
  profil temporal (C07) / consolidare multi-sursa (C08).
- VERIFICARE: profilul descopera ce e in date / masuratorile reflecta
  realitatea setului / profilul temporal respecta intervalul / consolidarea
  pastreaza totalurile.
- STABILIZARE: profil reutilizabil cu structured references, formule
  predictibile la refresh, profil auditabil, flux consolidat.
- CONFIRMARE: set cunoscut multidimensional, pregatit pentru atribuire de
  semnificatie in T3.

**Diferenta T2 vs T3 (lectie L136 codificata 25.05.2026):**
T2 raspunde la intrebari DESCRIPTIVE: "din ce e facut" / "cat masoara" /
"cum se desfasoara in timp" / "cum se integreaza".
T3 raspunde la intrebari DECIZIONALE: "ce inseamna" / "care e prioritar" /
"unde pierd" / "unde castig" / "ce decid".
"Clasificare" in C05 = inventar de categorii existente (descriptiv), NU
atribuire de categorii noi (decizional - aia e T3).
Atribuirea decizionala (segment A/B/C strategic, prioritate executiva,
canal valoros) traieste in T3-T4, cand exista obiectiv de analiza.
Confuzia T2-T3 a costat 3 iteratii in chat SPEC C05 (25.05.2026) -
codificata aici ca lectie permanenta de evitat la C06-C08 si T3.

## TREAPTA 3 - ANALIZA (C09-C12)

**Intrare:** baza consolidata cu KPI-uri stabile de la T2. Date corecte si
calculate, dar inca fara prioritizare - zgomot, nu insight.

**Iesire:** date transformate in insight operational, probleme prioritizate
si cuantificate, analiza pregatita pentru decizie executiva. Datele incep
sa spuna povestea business-ului.

**Inlantuirea celor 4 constructii:**
- C09 EXPLORAREA DATELOR - drill-down, slice, segmentare, navigare,
  descoperire. Energia: EXPLORARE.
- C10 ANALIZA PIVOT - Pivot Tables ca instrument de analiza reala, nu
  decor. Pivotul nu decide, operatorul decide.
- C11 DATA MODEL - relationships, measures, dimensions, DAX controlat,
  model thinking. Trecerea de la tabel la model.
- C12 PRIORITIZARE EXECUTIVA - top probleme, top clienti, Pareto, risc,
  focus management. Energia: DECIZIE.

**Rol tehnologie dominanta (Power Pivot + Data Model):** model thinking
controlat. C09 exploreaza pe pivot simplu, C10 aprofundeaza pivotul, C11
construieste modelul relational, C12 prioritizeaza pe model.

**Cele 6 etape pe T3 (specific):**
- REALITATE: zgomot / lipsa de claritate / rapoarte care par toate corecte
  fara context.
- INVESTIGATIE: operatorul exploreaza asistat de AI - "ce se degradeaza?",
  "unde pierdem?", "ce conteaza cu adevarat?". Investigatie, nu raport.
- TRANSFORMARE: explorare drill-down / analiza pivot / construire model /
  prioritizare Pareto.
- VERIFICARE: consistenta segmentarii / corectitudinea masurilor /
  integritatea relatiilor model / validitatea prioritizarii.
- STABILIZARE: model refreshabil, measures reutilizabile, prioritizare
  repetabila.
- CONFIRMARE: insight cuantificat, probleme prioritizate, pregatit pentru T4.

## TREAPTA 4 - RAPORTARE (C13-C16)

**Intrare:** insight prioritizat si cuantificat de la T3. Stim ce conteaza,
dar nu e inca comunicat in forma care accelereaza decizia.

**Iesire:** cockpit executiv clar si rapid, comunicare executiva in 4 forme
distincte, control operational vizual in timp real. Raportul devine
interfata de comanda.

**Inlantuirea celor 4 constructii (4 forme distincte de comunicare
executiva, NU dashboard x3):**
- C13 VIZUALIZARE EXECUTIVA - charts, comparare, visual hierarchy.
- C14 DASHBOARD EXECUTIV - cockpit complet, interactivitate, slicers,
  layout executive.
- C15 POVESTEA DATELOR - narrative BI, insight, concluzie, storytelling.
- C16 CONTROL INSTANT - compresie operationala extrema (cockpit
  ultra-comprimat, NU raport de o pagina). Zeci de surse comprimate intr-o
  interfata de control instant, fara zgomot. Energia: reactionezi instant.

**Rol tehnologie dominanta (Dashboards + BI UX):** vizualizarea trebuie sa
accelereze decizia, nu sa impresioneze. Progresie: vizual (C13) -> cockpit
interactiv (C14) -> naratiune (C15) -> sinteza pe o pagina (C16).

**Cele 6 etape pe T4 (specific):**
- REALITATE: directorul nu citeste tabelul / haos vizual / reactie lenta.
- INVESTIGATIE: operatorul investigheaza asistat de AI - "ce vede
  decidentul in 5 secunde?", "ce decizie trebuie sa declanseze acest
  ecran?".
- TRANSFORMARE: construire vizualizare / cockpit / naratiune / compresie
  de control instant.
- VERIFICARE: ierarhia vizuala accelereaza decizia? logica din spatele
  vizualului e corecta? sinteza nu pierde adevarul?
- STABILIZARE: layout reutilizabil, refreshabil, control vizual predictibil.
- CONFIRMARE: cockpit clar care declanseaza decizie, pregatit pentru T5.

## TREAPTA 5 - AUTOMATIZARE (C17-C20)

**Intrare:** raportare executiva clara de la T4. Functioneaza, dar inca
depinde de operator: reconstructie manuala, copy-paste, versiuni multiple.

**Iesire:** sistem autonom, repetabil, predictibil, scalabil. Datele intra,
sistemul ruleaza. Trainity asamblat complet.

**Inlantuirea celor 4 constructii:**
- C17 RAPORTAREA DE LUNI DIMINEATA - elimina reconstructia saptamanala.
- C18 ELIMINAREA VERSIUNILOR - sfarsitul haosului de versiuni multiple.
- C19 PROCEDURA DE RAPORTARE - raportarea urmeaza sistemul, nu memoria
  operatorului.
- C20 SISTEMUL TRAINITY - asamblarea sistemului complet: refresh final,
  orchestration, cockpit complet, flow complet, integrare, simulare reala,
  handover operational. Payoff-ul intregului sistem, constructie reala.

**Rol tehnologie dominanta (Refresh Architecture + Operational Flows):**
nu automatizam task-uri, construim mecanisme. C17-C19 elimina dependentele
manuale punctuale, C20 asambleaza tot intr-un sistem care ruleaza singur.

**Cele 6 etape pe T5 (specific):**
- REALITATE: reconstructie manuala / versiuni multiple / panica
  operationala / sistem neasamblat.
- INVESTIGATIE: operatorul investigheaza asistat de AI - "ce se reface
  manual de fiecare data?", "unde se rupe fluxul?", "ce trebuie orchestrat?".
- TRANSFORMARE: construire refresh / eliminare versiuni / standardizare
  procedura / asamblare sistem complet.
- VERIFICARE: refresh predictibil? versiuni eliminate? procedura
  reproductibila? sistemul ruleaza cap-coada singur?
- STABILIZARE: orchestrare robusta, flux standardizat, sistem scalabil.
- CONFIRMARE: sistem autonom validat, Trainity asamblat, handover
  operational.

## TASK PARALEL INREGISTRAT (nu se pierde)

10_Catalog_Constructii_Excel.docx trebuie REFACUT complet pe arhitectura
noua (decizia B a lui Bogdan): fara SCARA, INVESTIGATIE nu COMANDA, nume
noi (C08 Pregatirea pentru analiza, C09 Explorarea datelor, C12 Prioritizare
executiva, C16 One-page executiv). Dependenta logica: Catalogul detaliaza
constructiile, al caror continut se defineste la Pasul 4 (PARTEA IV). Decizie
de secventiere: Catalogul se reface DUPA Pasul 4, o singura data, aliniat -
altfel s-ar reface de doua ori. Inregistrat aici ca sa nu se piarda.

================================================================================

# PARTEA V - SABLONUL STANDARD DE CONSTRUCTIE (Pasul 5)

Acesta este PROTOCOLUL dupa care exista toate cele 20 de constructii.
Extras si formalizat din tiparul folosit consecvent in documentele oficiale
(C01-C08). Orice constructie C01-C20 se completeaza dupa acest sablon, in
aceasta ordine, cu aceleasi sectiuni. Nicio constructie nu inventeaza
structura proprie. Repetabil, scalabil, predictibil.

## STRUCTURA OBLIGATORIE (15 blocuri, in ordine)

NOTA: blocurile 6,7,8,9,10,11,13 (cele "Top 3") sunt PROPUNERI - la prima
rulare Claude propune 3, Bogdan alege 1 (vezi MECANISM ALEGERE + INGHETARE).

### BLOC 1 - IDENTITATEA CONSTRUCTIEI
Treapta de care apartine. Punctul de tranzitie pe care il marcheaza:
"C[NN] este punctul in care [X] inceteaza sa mai fie [stare veche] si
incepe sa devina [stare noua]". O frazare scurta, taioasa, cinematica.

### BLOC 2 - CE CONSTRUIESTE
Transforma [input] in [output]. Lista concreta a ce devine sistemul dupa
constructie. Verb la prezent, operational, fara teorie.

### BLOC 3 - ROL
Ce separa constructia (ex: valid tehnic de corect operational). Ce elimina
sau ce maturizeaza. O singura idee dominanta, formulata ca distinctie.

### BLOC 4 - TEHNOLOGIE DOMINANTA
Tehnologia principala + complementare. NU ca feature Excel, ci ca rol
operational (ex: Power Query ca motor de maturizare, nu ca buton).

### BLOC 5 - CE INVATA BUSINESS-UL
4-6 capacitati operationale dobandite. Formulare "cum [face X]", orientat
business, nu "cum se foloseste functia Y".

### BLOC 6 - DESCRIERI (3)
Trei descrieri scurte, cinematice, cu tensiune. Tipic: D1 expune iluzia
(pare corect, nu e), D2 muta in zona de constientizare/suspiciune, D3
generalizeaza miza (majoritatea firmelor fac asta gresit).

### BLOC 7 - TOP 3 HOOK-URI
Trei fraze-lovitura, scurte, memorabile, polarizante. Fara jargon. Test:
fiecare hook trebuie sa poata fi spus cu voce tare intr-un film si sa
ramana in minte.

### BLOC 8 - TOP 3 MANTRE
Trei principii operationale repetabile. Mantra = regula de mod-de-lucru,
nu slogan. Tipic una pleaca de la "nu facem X, facem Y".

### BLOC 9 - TOP 3 EMOTII
Trei stari pe care le produce constructia (ex: suspiciune controlata,
claritate logica, control). Definesc tonul emotional al filmului si HTML.

### BLOC 10 - TOP 3 MIZE
Trei consecinte reale daca problema nu e rezolvata. Orientate business,
concrete, nu abstracte.

### BLOC 11 - TOP 3 REZULTATE
Trei rezultate operationale concrete dupa constructie. Ultimul tipic:
"sistem pregatit pentru [constructia/treapta urmatoare]".

### BLOC 12 - STUDIU DE CAZ
Scenariu concret de firma, cu cifre. Structura: ce exporta/are firma,
ce pare corect, ce e de fapt gresit (cu cifre), ce face constructia
(cu cifre), rezultatul masurabil. Cifrele sunt canonice si traiesc
EXCLUSIV in INPUT.xlsx + OUTPUT.xlsx (R-V02.15). In HTML/HTML-VIDEO/
HTML-VIDEO-EDITABIL/FILM/PPT cifrele NU apar.

### BLOC 13 - WOW MOMENTS (3)
Trei momente de revelatie cu impact, cu cifra sau contrast vizibil
(ex: "X randuri devin Y tranzactii reale"; "suma A = suma B, suma ramane,
increderea nu"). Cifrele concrete se completeaza din livrabilele constructiei.

### BLOC 14 - FLOW OPERATIONAL (cele 6 etape, specific constructiei)
REALITATE / INVESTIGATIE / TRANSFORMARE / VERIFICARE / STABILIZARE /
CONFIRMARE - fiecare instantiata concret pentru aceasta constructie
(ce se vede, ce investigheaza operatorul asistat de AI, ce transforma,
ce verifica, ce stabilizeaza, ce confirma). In interiorul fiecarei etape
exista ritmul cinematic HOOK->DEMO->CONTROL->REVEAL.

### BLOC 15 - IDENTITATE FINALA
Trei linii de inchidere: Problema (o fraza) / Reframe (o fraza) /
Control (o fraza). Payoff conceptual al constructiei.

## REGULI DE CONTINUT (aplicabile fiecarei constructii)
- Vocabular ADN: mod de lucru / construim / sistem / operational /
  augmentat cu AI / control. INTERZIS: curs, cursant, lectie, modul,
  tutorial, masterclass, webinar, productivitate, AI hype.
- INVESTIGATIE inainte de TRANSFORMARE: promptul natural e instrument de
  investigatie, nu comanda de executie. NU "scrie prompt si AI face magie".
- Cifre canonice: aceeasi suma/volume identice in INPUT, OUTPUT, FILM,
  PPT, HTML. Zero divergenta.
- Zero continuitate intre constructii (date proaspete proprii).
- Fara em-dash sau en-dash retoric (semnal AI).

## REGULI DE DESIGN (aplicabile fiecarei constructii)
Brutalist premium, enterprise, cinematic, control panel, curat, aerisit.
Maximum per ecran: 1 accent galben major, 1 focus dominant, 1 payoff.
INTERZIS: dashboard fake, KPI fake, tutorial feeling, curs feeling, AI
hype, clutter, wall text, densitate excesiva.

## CELE 5 LIVRABILE (structura definita la Pasii 6-9)
INPUT.xlsx / OUTPUT.xlsx / FILM.docx / PPT.pptx / HTML.html. Structura
fiecaruia (HTML cockpit, PPT executive, script FILM, INPUT/OUTPUT Excel)
se defineste in PARTEA VI-IX. HTML = livrabil central (cockpit operational
live, NU document, NU pagina de curs).

## NOTA APLICARE
La Pasul 4 (definirea fiecarei constructii) fiecare C01-C20 se completeaza
EXACT pe aceste 15 blocuri + reguli. Pentru C01-C08 documentele oficiale au
material bogat (se structureaza, nu se inventeaza). Pentru C09-C20 (sumare
in documente) Claude semnaleaza explicit fiecare bloc unde lipseste
continut si cere decizia lui Bogdan - NU inventeaza identitate, hook-uri
sau mize.

## MECANISM ALEGERE + INGHETARE (regula de proces)

**REGULA INTREBARI-GRILA (permanenta, toate chat-urile):** ORICE alegere
ceruta lui Bogdan (selectie din Top 3, confirmari, optiuni de proces) se
pune ca INTREBARE-GRILA cu variante numerotate (1/2/3...), nu ca text liber.
Bogdan raspunde scurt cu numarul. Se aplica la mecanismul de alegere, la
clarificari de proces, la confirmari - in acest chat si in toate chat-urile
viitoare (regula intra in pachetul de checkin, se propaga). Exceptie: cifre
canonice sau decizii deschise unde nu exista variante discrete - acolo
Claude propune explicit si marcheaza ca propunere.

**REGULA REGENERARE TOP (permanenta, toate chat-urile):** FIECARE grila de
selectie din Top 3 (hook, mantra, emotie, miza, rezultat, descriere, wow)
contine OBLIGATORIU si optiunea suplimentara "Genereaza alte 3 optiuni".
MECANICA EXACTA (bucla, un bloc per grila): grilele de selectie din Top se
pun UNA CATE UNA (un singur bloc per tur), NICIODATA in seturi de mai multe
blocuri. Motiv tehnic: tool-ul de grila se rezolva in tururi discrete si nu
poate regenera in interiorul unui set; regenerarea pe loc functioneaza doar
daca fiecare bloc e o grila separata. Flux: Claude pune grila pentru blocul
curent. Daca Bogdan alege o varianta concreta, Claude o ingheata si trece
la blocul urmator (tur nou). Daca Bogdan alege "Genereaza alte 3 optiuni",
Claude NU trece mai departe; pune IMEDIAT, in turul urmator, o GRILA NOUA
pentru ACELASI bloc cu un set NOU de 3 variante (diferite de toate cele
propuse anterior la acel bloc, din acelasi material-sursa, fara a inventa
directia), plus din nou optiunea "Genereaza alte 3 optiuni". Bucla se
repeta ORICATE runde pana cand Bogdan alege o varianta concreta. Abia atunci blocul e
inghetat. Daca materialul-sursa se epuizeaza (nu mai exista variante noi
reale), Claude semnaleaza explicit acest lucru si cere directia lui Bogdan,
in loc sa repete sau sa inventeze. Se propaga prin checkin.

Blocurile cu "Top 3" (BLOC 6 descrieri, 7 hook-uri, 8 mantre, 9 emotii,
10 mize, 11 rezultate, 13 wow) sunt PROPUNERI. La PRIMA rulare a unei
constructii ("Genereaza CONSTRUCTIA NN"), prezentate ca INTREBARI-GRILA:
1. Claude propune cele 3 variante per bloc (numerotate).
2. Bogdan ALEGE 1 varianta per bloc (sau explicit mai multe daca cere).
   Restul cad. Bogdan e arhitectul.
3. Dupa ce toate blocurile Top sunt decise + restul sablonului confirmat,
   Claude INGHEATA automat alegerile in PARTEA VI - SPEC INGHETAT C[NN],
   o singura data, dupa confirmarea de ansamblu a lui Bogdan.
4. La ORICE re-rulare a aceleiasi constructii, Claude CITESTE SPEC-ul
   inghetat din PARTEA VI si APLICA alegerile FARA sa mai intrebe nimic.
   Re-genereaza doar livrabilele cu aceleasi decizii.
5. Modificarea unei alegeri inghetate: EXCLUSIV la cerere explicita Bogdan
   ("schimba hook-ul la C05"). Altfel SPEC-ul nu se atinge.

**BLOC 14 (regula permanenta, OBLIGATORIU la prima rulare) - FENOMENE / OPERATII
COOL "CE PARE DATA DAR ESTE AMBALAJ" / "anti-patterns de modernizat" (in T3):**

Inainte de a genera "anomaly-grid" (zona de fenomene/operatii din HTML),
Claude TREBUIE sa intrebe Bogdan ca grila separata:

  GRILA FENOMENE/OPERATII pentru CNN
  Rol: zona de revelatie post-deschidere - "uite ce ai in fisier dar nu vezi".
  Pozitie: dupa exec-hero, ca anomaly-grid 5 cards (titlu+cifra+descriere).
  Criteriu: fiecare item trebuie sa aiba HOOK (sa te socheze cand il auzi),
  sa fie real si frecvent intalnit in exporturile RO, sa fie util in
  practica (operatorul recunoaste imediat). NU lista exhaustiva tehnica.
  
  TOP 10 propuse (numerotate):
  1. [fenomen 1 cu cifra concreta]
  ...
  10. [fenomen 10 cu cifra concreta]
  
  ALEGE 5 (raspunzi cu numerele, ex: "2, 4, 5, 7, 9")
  [Genereaza alte 10] [Adauga manual]

Reguli pentru cele 10:
- Fiecare are titlu scurt (1-3 cuvinte CAPS) + cifra canonica/descriere
- Variatie de natura (structurale + de continut + de format + de logica),
  nu 10 variante ale aceluiasi tip
- Toate trebuie sa fie reale in fisierul construit (nu inventate)
- Cele 5 alese devin anomaly-grid-ul din HTML (grid 5 coloane sau 5×1)
- Cele 5 alese se INGHEATA in SPEC ca array FENOMENE_ALESE
- Restul 5 cad (nu se mentioneaza nicaieri)

Aceasta regula se propaga prin checkin la toate constructiile.

**BLOCUL 14 trebuie rulat DUPA HOOK/MANTRA/MIZA/WOW/MOTTO** (cele 5
elemente narative se aleg primele, dau directia), DAR INAINTE de
generarea livrabilelor (fenomenele influenteaza INPUT.xlsx, FILM-ul si
PPT-ul). Ordine corecta de chestionare la prima rulare:
1. Cele 5 elemente narative (HOOK/MANTRA/MIZA/WOW/MOTTO) - Top 3 each
2. BLOC 14 FENOMENE - Top 10 -> alege 5
3. Restul SPEC (descriere, rezultat, etape, cifre canonice)
4. INGHEATA tot in SPEC, apoi genereaza livrabilele.



PROPAGARE: SPEC-ul inghetat exista in SISTEM. La checkout se salveaza
starea (SISTEM cu SPEC actualizat intra in arhiva de tranzitie). Fiecare
chat de generare se incheie cu checkout, altfel SPEC-ul se pierde. Lucru
secvential, mereu arhiva cea mai noua.

Scop: Bogdan e intrebat O SINGURA DATA per constructie in viata ei.
Re-rulare = ZERO intrebari repetate.

================================================================================

# PARTEA VI - SPEC INGHETAT CONSTRUCTII

Aici traiesc alegerile de continut inghetate, per constructie. Se populeaza
la PRIMA rulare a fiecarei constructii (Bogdan alege din Top 3, Claude
ingheata aici). La re-rulare se citeste de aici, zero re-intrebari.
Modificare doar la cerere explicita Bogdan.

Format per constructie (completat la prima rulare): HOOK ales (1 din 3) /
MANTRA aleasa / MOTTO ales / EMOTIE aleasa / MIZA aleasa / REZULTAT ales /
DESCRIERE aleasa / WOW ales / cifre canonice + suma + etape / Status INGHETAT.

CELE 5 ELEMENTE NARATIVE CANONICE per constructie (regula permanenta):

| # | Element             | Rol psihologic + emotie inspirata        | Pozitie in flow narativ          |
|---|---------------------|------------------------------------------|----------------------------------|
| 1 | INTRIGA (vechi HOOK)| ATENTIE - paradox/socare/contradictie    | Deschidere (cover, sub titlu)    |
|   |                     | Te opreste din scroll. Emotie: curiozitate|                                 |
|   |                     | tensionata ("ce inseamna asta?")         |                                  |
| 2 | MIZA                | TENSIUNE - consecinta, de ce conteaza    | Sub INTRIGA, in cover (argument  |
|   |                     | Te face sa stai. Emotie: ingrijorare     | pentru decident)                 |
|   |                     | rationala ("asta ma costa daca ignor")   |                                  |
| 3 | MANTRA              | PROMISIUNE - formula sistemului,         | Bara galbena dupa hero, INAINTE  |
|   |                     | repetabila. Emotie: incredere operationala| de Etapa 1 (punct de cotitura) + |
|   |                     | ("am o regula clara de aplicat")         | leitmotiv in slogan-box etapa    |
|   |                     |                                          | STABILIZARE                       |
|   |                     | [Etapele 1-6 = demonstratia]                                            |
| 4 | WOW                 | ELIBERARE - dovada transformarii         | Payoff cinematic final (negru,   |
|   |                     | Recunoasterea ca s-a intamplat ceva real | gri estompat -> galben monument) |
|   |                     | Emotie: satisfactie ("a meritat")        |                                  |
| 5 | MOTTO               | SEMNATURA - regula interna a operatorului| Sub payoff-close ("C02 poate     |
|   |                     | dupa constructie. Emotie: convingere     | incepe"), separat prin linie     |
|   |                     | personala ("asta e regula mea de acum")  | gri, italic gri cu eticheta      |
|   |                     |                                          | galbena "MOTTO"                  |

TERMINOLOGIE HIBRIDA (regula permanenta): in CSS, in cod, in HTML pentru
clase si in tabelul de mai sus, denumirea OFICIALA este "INTRIGA" (vechi
HOOK). In grilele de inghetare SPEC din chat-urile CONSTRUCTIE NN, eticheta
afisata este "INTRIGA (HOOK)" la prima mentiune per grila, apoi doar
"INTRIGA". Motivatie: anglicism "HOOK" e inca prezent in documentele
sursa si in vorbirea operationala; pastram puntea de tranzitie pana cand
toata documentatia se aliniaza la INTRIGA. Vocabular Brand: INTRIGA e
romanesc, mai puternic narativ, aliniat la ADN-ul Trainity.

EXCEPTIE BRAND CONTROLATA - CASETA INTRIGA ROSIE (regula permanenta):
Caseta INTRIGA in HTML primeste o exceptie de la paleta canonica
galben/negru/alb. Tratament vizual:
- Fundal: #C00000 (rosu Trainity, IDENTIC cu butonul .pdf-download-btn)
- Text: alb #fff
- Border: 2px solid #000
- Box-shadow: 4px 4px 0 #000 (brutalist, IDENTIC cu PDF)
- Eticheta "INTRIGA · " micropunctata alba opacity .8
Motivatie: INTRIGA si butonul DESCARCA PDF formeaza pereche vizuala
coerenta - ambele "semnal de alarma" (atentie cinematica vs actiune
externa). Rosul iese in contrast puternic fata de galbenul cover-ului.
Aceasta exceptie e UNICA pe paleta - restul casetelor narative pastreaza
paleta canonica (MIZA neagra, MANTRA galbena, WOW negru cu galben, MOTTO
gri italic). Se propaga la toate constructiile C02-C20.

**REGULA OBLIGATORIE pentru grilele de inghetare SPEC (in chat CONSTRUCTIE NN,
la prima rulare):** orice grila care intreaba Bogdan sa aleaga unul din Top 3
pentru INTRIGA/MIZA/MANTRA/WOW/MOTTO TREBUIE sa includa la inceput, pe scurt:
- ROL PSIHOLOGIC al elementului (din tabel)
- EMOTIE INSPIRATA (ce simte privitorul/operatorul)
- POZITIE in flow narativ (unde apare in HTML)
- La prima mentiune per grila: parantezarea numelui vechi (ex. "INTRIGA (HOOK)"
  ca punte de tranzitie, pana la aliniere completa a vocabularului)

Asta ajuta Bogdan sa aleaga calibrat: nu doar "ce suna bine", ci "ce sluje
cel mai bine functiei narative" + "ce emotie declanseaza". Format scurt - 
3 randuri intro inainte de Top 3. NU se cere confirmare pentru aceasta 
regula; e automata.

Exemplu format grila (la negenerat, prima rulare):

  GRILA INTRIGA (HOOK) pentru CNN
  Rol: ATENTIE. Te opreste din scroll. Paradox/socare/contradictie.
  Emotie inspirata: curiozitate tensionata ("ce inseamna asta?")
  Pozitie: cover, sub titlu.
  
  1. "Optiunea A..."
  2. "Optiunea B..."
  3. "Optiunea C..."
  
  [Genereaza alte 3] [Alege manual]

Aceasta regula se propaga prin checkin in toate chat-urile CONSTRUCTIE NN.

**REGULA PERMANENTA - PROMPTURI COPILOT scrise din VOCEA OPERATORULUI, nu
din vocea expertului:**

Promptele Copilot din HTML-urile constructiilor (prompt-box) TREBUIE scrise
din perspectiva operatorului-care-NU-stie-taxonomia-tehnica, nu din
perspectiva expertului-care-deja-stie. AI investigheaza, AI clasifica, AI
propune solutia. Operatorul cere comportament dorit (verifica, transforma,
repetabil), NU dicteaza taxonomie tehnica (antet de raport / subtotal /
total general / blank-uri false / promoveaza rand ca antet / filtreaza
SUBTOTAL etc.). Daca operatorul ar sti deja taxonomia, n-ar mai avea
nevoie de AI.

Indicatori CONFORM (voce operator):
- "Ma uit la acest fisier si pare ... bănuiesc ca nu este"
- "Spune-mi ce nu ar trebui sa fie aici"
- "Vreau sa pot reaplica luna viitoare"
- "Verifica si raporteaza"
- "Construieste un flux care pastreaza doar ce e real"

Indicatori NECONFORM (voce expert, INTERZIS):
- "Identifica cate randuri sunt antet de raport"
- "Promoveaza randul curent ca antet"
- "Filtreaza randurile unde prima coloana incepe cu SUBTOTAL"
- "Elimina blank-urile false"

AI-ul produce raportul tehnic (cu taxonomia corecta) ca RAPORT, nu cerut de
operator. RAPORT_AI in tabelul de sub prompt foloseste vocabular tehnic;
PROMPTUL e simplu.

Lectie sursa (C01, mai 2026): P1 initial scris ca expert ("identifica
cate randuri sunt antet de raport, subtotaluri, total general...") - Bogdan
a respins corect: "de unde sa stie utilizatorul de antet de raport?".
Corectat la "Ma uit la acest fisier si pare un tabel normal, dar banuiesc
ca nu este. Verifica structura si spune-mi: ce nu ar trebui sa fie aici
daca ar fi un tabel curat?".

Aceasta regula se propaga prin checkin la toate constructiile C02-C20.

## SPEC C01 - STRUCTURA TABELELOR   [Status: INGHETAT]

Inghetat in chatul de reconstructie (mai 2026), prin motor cu grile.
Alegeri definitive (modificare doar la cerere explicita Bogdan):

ELEMENTE NARATIVE (5 inghetate):
- INTRIGA (vechi HOOK): "Arata ca tabel. Nu este tabel."
  Rol psihologic: ATENTIE (paradox). Emotie: curiozitate tensionata.
- MIZA: "O decizie corecta pe date structurate gresit ramane o decizie
  gresita." Rol: TENSIUNE. Emotie: ingrijorare rationala.
- MANTRA: "Nu reconstruim tabelul. Il facem controlabil."
  Rol: PROMISIUNE. Emotie: control structural.
- WOW: "Nimic sters. Nimic adaugat. Doar structura, eliberata."
  Rol: ELIBERARE. Emotie: satisfactie (a meritat).
- MOTTO: "Mai intai structura. Apoi orice." (semnatura mentala a
  operatorului dupa C01). Rol: SEMNATURA. Emotie: convingere personala.

EMOTIE DOMINANTA: ordine structurala.
TEHNOLOGIE DOMINANTA: Power Query (motor de transformare structurala).

CELE 5 FENOMENE ALESE (din BLOC 14):
1. ANTET RAPORT (randuri titlu raport inainte de antetul real al datelor)
2. SUBTOTALURI (randuri SUBTOTAL inserate intre tranzactii)
3. TOTAL GENERAL (rand TOTAL GENERAL la final)
4. BLANK FALS (randuri goale false in zona de date)
5. COLOANE ASCUNSE (coloane fizice ascunse: cod_filiala, cod_user)

Plasare cele 5: anomaly-grid AUTONOM dupa mantra-band, INAINTE de Etapa 1
(revelatia post-deschidere). NU in interiorul Etapei 1.

REGULI DE CALCUL SI CONTINUITATE (verificate fizic in livrabile):
- Suma valoare_neta CONSERVATA cap-coada INPUT = OUTPUT (toleranta 0).
- 14 coloane vizibile + 2 ascunse fizic (cod_filiala, cod_user) = 16 col
  INPUT. OUTPUT = 14 coloane (cele 2 ascunse eliminate prin Power Query).
- OUTPUT format Excel Table denumit `Vanzari_Curat`.
- Total ambalaj eliminat = randuri antet raport + SUBTOTAL + TOTAL GENERAL
  + BLANK FALS. Distinctie blank de format (separator antet raport) vs
  blank fals in zona date: separatorul NU se numara ca blank fals.

IDENTITATE FINALA:
- Problema: exportul ERP pare tabel, nu este
- Reframe: datele nu sunt haos, ambalajul este
- Control: nu reconstruim fisierul, il facem controlabil

PUNTE NEXT: C02 CONTROLUL DATELOR (T1 continua, marcheaza anomalii business).

VALIDARE: Gate 1 + Gate 2 + Gate 3 conforme. Cifrele reale traiesc in
livrabilele C01 din arhiva (livrabile_C01/), citite fizic la fiecare
verificare prin generatoare/verifica_c01.py.

## SPEC C02 - CONTROLUL DATELOR   [Status: INGHETAT]

Inghetat in chatul `CHECKIN CONSTRUCTIE 02` (20.05.2026), prin motor cu
grile + validat prin Gate 1 + Gate 2.

ELEMENTE NARATIVE (5 inghetate):
- INTRIGA (vechi HOOK): "Tabelul cu date pare curat. Datele insa mint."
  Rol psihologic: ATENTIE (paradox). Emotie: curiozitate tensionata.
- MIZA: "Un raport construit pe date care mint produce decizii care costa."
  Rol: TENSIUNE (consecinta). Emotie: ingrijorare rationala.
- MANTRA: "Marcam acum datele neconforme. Decidem dupa ce facem cu ele."
  Rol: PROMISIUNE (formula sistemului). Emotie: control.
- WOW: "Anomaliile nu mai trec neobservate. Si nici nu vor mai disparea
  fara urma." Rol: ELIBERARE. Emotie: satisfactie eliberatoare.
- MOTTO: "Datele neconforme se controleaza si se marcheaza, niciodata
  nu se ascund." (semnatura mentala a operatorului dupa C02).
  Rol: SEMNATURA. Emotie: convingere personala.

EMOTIE DOMINANTA: control suspicios constructiv.
TEHNOLOGIE DOMINANTA: Power Query (motor de marcare repetabila prin
reguli) + formule SUMIF/COUNTIF (verificare).

CELE 5 FENOMENE ALESE (din BLOC 14, anomalii business plantate):
1. DATA IN VIITOR (vanzari cu data ulterioara raportului)
2. CLIENT INEXISTENT (client_nume nereferentiat in nomenclatorul CLIENTI)
3. DUPLICAT EXACT (perechi identice factura+data+suma)
4. TRANZACTIE WEEK-END (vanzari sambata/duminica pe filiale L-V)
5. CAMP OBLIGATORIU GOL (client_nume sau cod_produs lipsa)

Plasare cele 5: anomaly-grid AUTONOM dupa mantra-band, INAINTE de Etapa 1.

REGULI DE CALCUL SI CONTINUITATE (verificate fizic in livrabile):
- C02 NU sterge, NU repara. MARCHEAZA prin doua coloane noi:
  status_validare (VALID / DE VERIFICAT / EXCLUS) + motiv_anomalie (text).
- INPUT C02 = OUTPUT C01 + randuri duplicate adaugate + modificari
  in-place pentru anomalii plantate. Continuitate cap-coada INTERIORUL
  treptei T1 (de la OUTPUT C01).
- OUTPUT C02 = INPUT C02 + 2 coloane noi (status_validare,
  motiv_anomalie). Numar randuri OUTPUT = numar randuri INPUT (zero
  pierderi, zero adaugari).
- OUTPUT format Excel Table denumit `Vanzari_Controlate`.
- Distributie status pe 3 nivele:
  * VALID = randuri fara anomalie
  * DE VERIFICAT = anomalie probabila, decizia la operator
    (regula: DATA IN VIITOR + TRANZACTIE WEEK-END)
  * EXCLUS = anomalie clara invalida
    (regula: COD CLIENT INEXISTENT + DUPLICAT EXACT + CAMP GOL)
- Conservare suma fizica INPUT = OUTPUT (toleranta 0). Suma raport oficial
  = SUMIF pe status_validare = "VALID".
- Foaie CONTROL_FINAL cu formule COUNTIF + SUMIF de validare cross-status.

MOTIVE EXACTE in coloana motiv_anomalie (texte canonice):
- "Data in viitor"
- "Client inexistent in nomenclator"
- "Duplicat exact (rand sursa)"
- "Duplicat exact (rand copie)"
- "Tranzactie in week-end pe filiala L-V"
- "Camp obligatoriu gol (client_nume sau cod_produs)"

CELE 6 ETAPE (schelet procedural macro):
- REALITATE - tabel pare curat
- INVESTIGATIE - suspiciuni AI (Prompt 1 = audit, raporteaza fara modificare)
- TRANSFORMARE - marcare Power Query (Prompt 2 = aplica reguli + status + motiv)
- VERIFICARE - SUMIF + COUNTIF (cross-check distributie + conservare)
- STABILIZARE - refresh + reguli reaplicabile
- CONFIRMARE - baza controlata predata catre C03

IDENTITATE FINALA:
- Problema: datele par curate, dar mint
- Reframe: separa VALID TEHNIC de CORECT OPERATIONAL
- Control: marcheaza si decide, nu sterge si nu ascunde

PUNTE NEXT: C03 AUDITAREA DATELOR (contaminare invizibila, dataset proaspat).

NOTA NARATIVA ONESTA: in baza C01 OUTPUT exista randuri week-end native
(date sintetice fara filtru filiale). Cele plantate ca anomalie in C02
sunt specifice regulii "filiale L-V". Restul week-end-urilor raman VALID.
Pentru consistenta narativa, formularea "vanzari sambata sau duminica pe
filiale cu program L-V" descrie regula de marcare, NU afirma ca toate
week-end-urile sunt suspecte.

VALIDARE: Gate 1 + Gate 2 + Gate 3 conforme. Cifrele reale traiesc in
livrabile_C02/, citite fizic la fiecare verificare.

## SPEC C03 - AUDITAREA DATELOR   [Status: INGHETAT]

Inghetat in chatul `CHECKIN CONSTRUCTIE 03` (20.05.2026), prin motor cu
grile + validat prin Gate 1 + Gate 2 + Gate 3.

ELEMENTE NARATIVE (5 inghetate):
- INTRIGA (vechi HOOK): "Cel mai periculos defect este cel care pare corect."
  Rol psihologic: ATENTIE (paradox vizibilitate). Emotie: vigilenta forensic.
- MIZA: "Cand defectul nu se vede, nu se cauta. Cand nu se cauta, intra
  in toate rapoartele." Rol: TENSIUNE. Emotie: ingrijorare metodica.
- MANTRA: "Datele nu se cred. Se demonstreaza."
  Rol: PROMISIUNE (metoda). Emotie: rigoare forensic.
- WOW: "Datele nu mai mint. Au fost demonstrate."
  Rol: ELIBERARE. Emotie: satisfactie de proba.
- MOTTO: "Defectele nu au disparut singure. Au fost detectate."
  (semnatura mentala a operatorului dupa C03, registru de raport/
  constatare, distinct de registrul imperativ C01).
  Rol: SEMNATURA. Emotie: convingere personala.

EMOTIE DOMINANTA: vigilenta forensic.
TEHNOLOGIE DOMINANTA: Power Query ca audit engine.

ROL IN TREAPTA: detecteaza contaminarea INVIZIBILA (dupa C01 structura si
C02 anomalii business). C03 NU repara, DEMONSTREAZA.

CELE 5 FENOMENE ALESE (BLOC 14, contaminare INVIZIBILA plantata disjunct):
1. SPATII ASCUNSE (trailing space in client_nume)
2. NUMERE CA TEXT (valori in valoare_neta stocate ca text)
3. DATE CA TEXT (valori data_factura stocate ca sir "DD.MM.YYYY")
4. CARACTERE INVIZIBILE (U+200B zero-width / U+00AD soft hyphen in
   client_nume)
5. TRAILING NEWLINE (CHAR(10)/CHAR(13) la final produs_nume)

Plasare cele 5: anomaly-grid AUTONOM dupa mantra-band, INAINTE de Etapa 1.

REGULI DE CALCUL SI CONTINUITATE (verificate fizic in livrabile):
- C03 NU sterge randuri. Curata VALORI tehnic, pastreaza valoarea
  semantica reala.
- INPUT C03 = dataset proaspat (NU continua din C02). Continuitate cap-coada
  intre constructii = ZERO (date proprii proaspete). Continuitate cap-coada
  INTERIORUL C03: INPUT = OUTPUT pe randuri si pe suma.
- Suma fizica conservata INPUT = OUTPUT. Calculul sumei INPUT necesita
  interpretare numerica a textului (numerele stocate ca text NU intra
  in SUM clasic; conversie explicita prin Power Query sau formula).
- OUTPUT: numere reale, date reale, text curat (zero spatii ascunse,
  zero caractere invizibile, zero trailing newline).

PROMPT 1 (audit forensic, voce operator): cere AI sa numere pe categorii
contaminari invizibile, fara modificare.

PROMPT 2 (curatare demonstrata, voce operator): cere AI sa construiasca
pasi Power Query reaplicabili care neutralizeaza tehnic fiecare categorie
fara sa modifice valoarea reala.

CELE 6 ETAPE:
- REALITATE (manual) - operatorul deschide fisierul, recunoaste ca
  aparenta de curatenie nu e dovada, fixeaza suma martor.
- INVESTIGATIE (Promptul 1) - AI auditeaza, raporteaza categoriile.
  Datele raman neatinse.
- TRANSFORMARE (Promptul 2 + Power Query) - flux PQ care neutralizeaza
  fiecare categorie. Zero randuri sterse, suma conservata.
- VERIFICARE (conservare) - dovedim numeric ca toate cele 5 categorii
  sunt la zero si suma e identica cu martorul.
- STABILIZARE (refresh) - fluxul de audit rezista la export nou.
- CONFIRMARE (cap-coada) - baza demonstrabila predata catre C04.

IDENTITATE FINALA:
- Problema: datele par curate, dar nu sunt
- Reframe: aparenta nu e dovada
- Control: C03 demonstreaza, nu repara silent

PUNTE NEXT: C04 NORMALIZAREA DATELOR (transformarea curatarii ad-hoc in
mecanism refreshabil documentat).

VALIDARE: Gate 1 + Gate 2 + Gate 3 conforme. Cifrele reale traiesc in
livrabile_C03/, citite fizic la fiecare verificare.

## SPEC C04 - NORMALIZAREA DATELOR   [Status: INGHETAT]

Inghetat in chatul `CHECKIN CONSTRUCTIE 04` (20.05.2026), prin motor cu
grile + validat prin Gate 1 + Gate 2 + Gate 3.

Pozitie: T1, ULTIMA constructie din TREAPTA 1 STRUCTURA (inchide treapta).

ELEMENTE NARATIVE (5 inghetate):
- INTRIGA (vechi HOOK): "Daca trebuie sa repari din nou, nu ai construit
  sistemul." Rol psihologic: ATENTIE (paradox). Emotie: curiozitate
  tensionata.
- MIZA: "Curatarea care depinde de tine nu este sistem. Este obicei."
  Rol: TENSIUNE (consecinta). Emotie: ingrijorare rationala.
- MANTRA: "Construim o singura data. Aplicam apasand un singur buton
  de refresh." Rol: PROMISIUNE (formula sistemului). Emotie: incredere
  operationala.
- WOW: "Export nou. Apesi refresh. Si gata." Rol: ELIBERARE (dovada
  transformarii). Emotie: satisfactie.
- MOTTO: "Construiesti manual o singura data. Apoi sistemul continua
  singur automat." (semnatura mentala a operatorului dupa C04).
  Rol: SEMNATURA. Emotie: convingere personala.

EMOTIE DOMINANTA: autonomie operationala.
TEHNOLOGIE DOMINANTA: Power Query ca TRANSFORMATION ARCHITECTURE
refreshabila (apex T1, distinct de C01 motor de transformare structurala).

CELE 10 OPERATII INGHETATE (anomaly-grid 5×2 fara separator, conform
R-V01.7 anomaly-grid parametrizat 3-12 cards):

Operatii in grid (10 cards, 5 coloane × 2 randuri desktop, 1 col mobile):
1. PROMOVARE ANTET (randul antet devine antet auto la fiecare refresh)
2. FILTRARE SUBTOTAL/TOTAL (randuri eliminate prin filtru text)
3. ELIMINARE BLANK FALS (randuri goale dispar singure)
4. DEDUPLICATION (dubluri fuzzy detectate si eliminate)
5. TABEL OUTPUT NUMIT (livrat ca Excel Table `Vanzari_Normalizat`)
6. ELIMINARE COLOANE ASCUNSE (cod_filiala + cod_user prin Remove Columns)
7. TIPIZARE COLOANE (tip explicit per coloana: date, numar, text)
8. TRIM + CLEAN UNICODE (valori cu spatii si caractere invizibile)
9. DATA DIN TEXT (valori DD/MM/YYYY convertite la data reala)
10. NORMALIZARE DIACRITICE (Bucuresti vs Bucuresti unificate)

Plasare cele 10: anomaly-grid AUTONOM dupa mantra-band, INAINTE de Etapa 1
(grid 5×2 desktop, stack vertical mobile). ZERO sectiuni separate
auxiliare gen "MECANISMUL COMPLET" intre randurile gridului - interzis
prin R-V01.7.

REGULI DE CALCUL SI CONTINUITATE (verificate fizic in livrabile):
- Suma valoare_neta CONSERVATA cap-coada INPUT = OUTPUT (toleranta 0).
- INPUT C04 = dataset proaspat cu perturbari celulare plantate (date
  proprii, NU continua din C03). Continuitate cap-coada intre constructii
  = ZERO. Continuitate cap-coada INTERIORUL C04: INPUT = OUTPUT pe suma.
- OUTPUT: 14 coloane finale. INPUT: 14 col vizibile + 2 ascunse fizic
  (cod_filiala col K, cod_user col O) = 16 col.
- Power Query expune Applied Steps refreshabili in ordine fixa, vizibili
  in panoul PQ Editor.
- OUTPUT format Excel Table denumit `Vanzari_Normalizat`.
- Seed determinist generator (parametru tehnic reproductibilitate).

IDENTITATE FINALA:
- Problema: ai curatat manual exporturi ERP de zece ori
- Reframe: curatarea este construibila, nu repetabila
- Control: nu repeti munca, construiesti mecanismul care o face

PUNTE NEXT: C05 CLASIFICAREA DATELOR (T2 CUNOASTERE incepe).

VOCABULAR ARHITECTURAL (R-V02.7): C04 inchide T1 cu vocabular de apex -
"transformation architecture refreshabila" cu Applied Steps in ordine
fixa, distinct de C01 "motor de transformare structurala". Pattern
permanent: la inchiderea unei trepte, ultima constructie capata vocabular
arhitectural.

VALIDARE: Gate 1 + Gate 2 + Gate 3 conforme. Cifrele reale traiesc in
livrabile_C04/, citite fizic la fiecare verificare.

## SPEC C05 - DICTIONAR (fost CLASIFICARE)A DATELOR   [Status: INGHETAT 25.05.2026]

Inceput in chat SPEC C05 (25.05.2026, motor V24). Inghetare progresiva
element cu element, ordinea narativa R-V03.56 V24 (modificata punctual
prin abatere constienta Bogdan: PROBLEMELE inghetate intai, INTRIGA dupa).

Pozitie: T2 CUNOASTERE, PRIMA constructie (deschide treapta dupa C04 inchide T1).

INTREBARE-MAMA C05 (decizie pe baza L136.A): "Ce contine setul?"
AXA: calitativa (categorial, taxonomic). NU cantitativa.
LIVRABIL: dictionarul setului (lista categoriilor existente, tipologia
randurilor, granularitatea atomica, anomalii de etichetare).
MARKER LINGVISTIC STRICT: cuvantul "ETICHETA" (vs "CIFRA" la C06).

ELEMENTE INGHETATE PROGRESIV:

### 1. INTRIGA   [Status: INGHETAT 25.05.2026, REFORMULAT 25.05.2026]

**"Setul are un dictionar. Excel il stie. Tu nu."**

Inghetata initial pe 25.05.2026 ca "Setul are un dictionar explicativ al
datelor. Excel il stie. Tu nu." Reformulata scurt la cererea Bogdan
(aceeasi zi): eliminat "explicativ al datelor" pentru ritm cinematic pur.

Structura tri-partita: setare + contrast 1 + contrast 2. Ritm cinematic
5/3/2 cuvinte (crescendo invers, ultimul cuvant "nu" lovitura curata).

Rol psihologic: ATENTIE prin paradox descriptiv (NU decizional - L136 R3
respectata).

Emotie: tensiune controlata + realizare ("Excel stie deja, eu nu am intrebat").

Mecanism pedagogic incapsulat: dictionarul setului = livrabilul C05 conform
L136.A. INTRIGA spune exact ce livreaza constructia.

Marker stilistic propagat in C07 (pattern T2): "Setul are X. Operatorul nu Y."
- C05: "Setul are un dictionar."
- C07: "Setul are memorie." (candidat)
Coerenta stilistica de treapta T2. Antropomorfizare cu actiune.

### 2. PROBLEMELE PE CARE LE REZOLVA   [Status: INGHETAT 25.05.2026]

Inghetate cele 5 din lista de 10 propuse de motor. Alese de Bogdan: 1, 2, 3, 5, 7.
Toate sunt intrebari descriptive pe axa calitativa (etichete, nu cifre).

**P1** - "Cati clienti unici am de fapt in set? Cate produse distincte?
Cate regiuni reale?"
*Cardinalitate categoriala per coloana. Inventarul de baza pe care
operatorul nu si-a pus-o niciodata.*

**P2** - "Care e granularitatea setului: un rand inseamna o tranzactie,
o factura sau o linie de produs?"
*Intrebarea atomicitatii. Fara raspuns aici, orice constructie urmatoare
e oarba.*

**P3** - "Care sunt cele mai frecvente cinci valori in fiecare coloana?"
*Topul frecventei categoriale. Dezvaluie ce domina setul fara sa
masoare nimic.*

**P5** - "Care coloane au valori distincte putine (cardinalitate mica)
si care au valori distincte multe (cardinalitate mare)?"
*Tipologia coloanelor. O coloana cu 3 etichete (status) e diferita
structural de una cu 800 (cod produs). Asta dicteaza cum o vei folosi.*

**P7** - "Care e dictionarul real al setului: toate etichetele care
exista in fiecare coloana categorica, cu frecventa lor?"
*Inventarul exhaustiv. Operatorul iese cu un dictionar al setului,
nu cu un mister.*

Logica grupului celor 5 (de propagat in HTML, FILM, PPT, prompturi):
P1 (cati unici) -> P2 (granularitate) -> P3 (top frecventa) ->
P5 (tipologie coloane) -> P7 (dictionar exhaustiv).
Progresie: cardinalitate -> nivel atomic -> domino -> tipologie ->
dictionar complet. De la intrebari simple la inventar exhaustiv.

### 3. MIZA   [Status: INGHETAT 25.05.2026]

**"Obtinem dictionarul complet al setului. Nu mai privim tabelul fara
sa stim ce contine."**

Inghetata de Bogdan ca reformulare a propunerii 1 (motor V24, runda 1):
- Schimbat "Operatorul iese cu" -> "Obtinem" (persoana intaia plural,
  inclusiv operatorul + sistemul + AI augmentat)
- Schimbat "3.300 de randuri orb" -> "tabelul fara sa stim ce contine"
  (generalizare, miza valabila la orice set, nu doar la cel de 3.300 randuri)

Rol psihologic: DORINTA. Operatorul stie ce castiga concret la final.

Emotie: claritate operationala anticipata + control prin cunoastere.

Livrabil incapsulat in miza: dictionarul complet al setului. Marker C05
respectat (L136.A): "dictionar" e cuvant-cheie axa calitativa.

Construit pe pattern oglinda fata de INTRIGA:
- INTRIGA C05: "Setul are un dictionar. Excel il stie. Tu nu." (lipsa)
- MIZA C05: "Obtinem dictionarul complet... Nu mai privim tabelul fara
  sa stim ce contine." (cucerire)
Lipsa -> cucerire. Pattern narativ TRAINITY clasic.

Persoana intaia plural ("obtinem", "privim") = identificare cu operatorul,
nu observator extern. Echo MANTRA C04 ("construim o singura data").

### 4. MANTRA   [Status: INGHETAT 25.05.2026]

**"Nu privim tabelul. Il interogam."**

Inghetata de Bogdan ca propunerea 3 (motor V24, runda 1), fara modificari.

Structura: contrast verb-verb scurt. Ritm 4/3 cuvinte. Memorabila instant.

Mecanism pedagogic incapsulat: "interogam" = exact verbul promptului
natural ca instrument de investigatie (canon SISTEM, prompt ca accelerator
procedural, NU comanda AI hype). MANTRA contine tehnica.

Contrast operational:
- "privim" = pasiv, vechi mod 2015, operatorul observa orb
- "interogam" = activ, augmentat AI 2030, operatorul intreaba sistemul

Persoana intaia plural ("privim", "interogam") consistenta cu MIZA
("obtinem", "privim"). Coerenta T2 mentinuta.

Pattern de propagare in FILM, PPT, HTML, prompturi: repetare in puncte
de inflexiune narativa (deschidere, mijloc, final). Repetabila in orice
context (intalniri, ziduri post-it, slide-uri).

### 5. MOTTO   [Status: INGHETAT 25.05.2026]

**"Un set cunoscut. Apoi orice decizie."**

Inghetat de Bogdan ca propunerea 5 (motor V24, runda 2 dupa corectie
definitie MOTTO).

Rol psihologic: SEMNATURA - regula interna a operatorului DUPA C05.
Emotie: convingere personala ("asta e regula mea de acum").

Pozitie in flow narativ: sub payoff-close ("C06 poate incepe"), separat
prin linie gri, italic gri cu eticheta galbena "MOTTO" (canonic R-V03.x).

Pattern stilistic: respecta exact C01 ("Mai intai structura. Apoi
orice.") - doua batai scurte, "X. Apoi orice Y." Coerenta cap-coada
SCARA pe linia MOTTO.

Mecanism codificat: encapsuleaza L136 ca regula interna (NU enunt
filosofic). Operatorul iese din C05 cu jurat: nu mai decide pe set
necunoscut. T2 inainte de T3 devine principiu personal.

Cinci cuvinte total. Ritm punch maxim. Aliniabila vizual sub payoff-close
in HTML-STUDY si HTML-VIDEO.

NOTA istorica: la prima propunere motorul a generat "MOTTO" gresit
(filozofie universala Trainity tip "Cunoasterea descriptiva vine
inaintea judecatii"). Bogdan a corectat: "motto nu era fraza de la
final?" Motorul a verificat SISTEM, a confirmat definitia (SEMNATURA
post-constructie, NU filozofie generala) si a regenerat. Lectie L137
codificata mai jos.

### 6. STEP-TITLES (18)   [Status: NEINGHETAT]
### 6. STEP-TITLES (18)   [Status: INGHETAT 25.05.2026]

Inghetate de Bogdan ca propunerea unica a motorului V24 (runda 1 acceptata
integral). Vocabular L136.A respectat (etichete, dictionar, profilare
descriptiva). Pattern C01 validat. Voce persoana a 2-a singular
(R-V03.4 HTML-STUDY cockpit).

**REALITATE (pasi 1-3)** - operatorul deschide setul curat si recunoaste
orbirea descriptiva:
01. Deschide tabelul curat predat de C04
02. Priveste setul si recunoaste necunoasterea
03. Fixeaza lista coloanelor de profilat

**INVESTIGATIE (pasi 4-5)** - operatorul activeaza Copilot, ruleaza
Promptul 1 (inventarul etichetelor):
04. Activeaza Copilot pe foaia Date
05. Ruleaza Promptul 1 de inventar al etichetelor

**CITIRE RAPORT + INCARCARE (pasi 6-7)** - operatorul citeste dictionarul
propus si-l confrunta cu setul:
06. Citeste dictionarul propus de sistem
07. Incarca dictionarul ca foaie de profil

**TRANSFORMARE (pasi 8-9)** - operatorul ruleaza Promptul 2 (granularitate
+ tipologie + anomalii):
08. Ruleaza Promptul 2 de profilare structurala
09. Aplica granularitatea atomica pe set

**VERIFICARE (pasi 10-12)** - operatorul confrunta cardinalitatea,
frecventele si valorile rare:
10. Confrunta cardinalitatea cu COUNTUNIQUE
11. Verifica top frecvente pe fiecare coloana
12. Marcheaza etichetele rare suspecte

**STABILIZARE (pasi 13-15)** - operatorul leaga dictionarul la sursa,
testeaza, documenteaza:
13. Leaga dictionarul la sursa ca tabel viu
14. Testeaza un refresh simulat pe profil
15. Documenteaza regula anti-deriva a etichetelor

**CONFIRMARE + PUNTE (pasi 16-18)** - operatorul confirma dictionarul
cap-coada si preda la C06:
16. Verifica profilul cap-coada cu setul
17. Confirma dictionarul complet auditabil
18. Preda catre C06

NOTE de coerenta:
- Cuvinte-cheie C05 propagate: "dictionar" x5, "eticheta" x3, "profil" x3,
  "cardinalitate" x1, "frecvente" x1, "granularitate" x1.
- Zero "suma", "medie", "total", "agregat" (teritoriu C06 protejat).
- Pasi 4+8 = doua prompturi Copilot (canon numar prompturi = numar
  SHORT-uri in FILM-Excel).
- Pas 14 "refresh simulat" preluat din C01 (pas 14 acolo) - stabilitatea
  regulii la refresh ca verificare canonica T1+T2.
- Pas 18 formula identica cu C01 pas 18 ("Preda catre C02") - coerenta
  cap-coada SCARA.

Echo elemente narative in step-titles:
- INTRIGA ("Tu nu") -> pas 02 ("recunoaste necunoasterea")
- MIZA ("dictionarul complet") -> pasi 6, 7, 13, 17
- MANTRA ("interogam") -> pasi 5, 8 (rulare prompturi)
- MOTTO ("Un set cunoscut. Apoi orice decizie.") -> pasi 16, 17, 18
  (confirma profil cap-coada + preda)

### 7. PROMPTURI Copilot (2)   [Status: INGHETAT 25.05.2026]

Inghetate de Bogdan ca rafinare a propunerilor motorului V24 (runda 1).
Rafinarea = descoperire critica codificata ca L138 (vezi mai jos).

**PROMPTUL 1 - INVENTAR ETICHETE** (corespunde STEP 05, raspunde P1 + P7)

> "Analizeaza acest set de date. Pentru fiecare coloana categorica,
> spune-mi cate valori distincte exista si listeaza etichetele impreuna
> cu frecventa lor. Identifica separat coloanele cu valori aproape unice,
> coloanele repetitive si coloanele cu valori libere. Returneaza
> rezultatul ca dictionar complet al setului, in format tabel."

Construct:
- "valori distincte" (NU "valori unice") - terminologic corect:
  COUNTDISTINCT vs COUNTUNIQUE diferentiate.
- "aproape unice" (NU "identificatori unici") - observatie descriptiva
  pura (cardinalitate ~ 1), NU termen semantic-business. L136 respectat.
- "dictionar complet al setului in format tabel" - livrabil concret,
  copy-paste in Excel ca foaie de profil (echo STEP 07).

**PROMPTUL 2 - PROFILARE STRUCTURALA** (corespunde STEP 08, raspunde
P2 + P3 + P5 + anomalii etichetare)

> "Pentru acelasi set, descrie structura datelor mai profund. Estimeaza
> granularitatea atomica a randurilor pe baza coloanelor si a repetitiilor
> observate. Pentru fiecare coloana, listeaza cele mai frecvente 5 valori
> si clasifica nivelul de cardinalitate: mic, mediu sau mare. Marcheaza
> separat etichetele rare care apar izolat in coloane predominant
> repetitive."

Construct:
- "Estimeaza pe baza structurii si repetitiilor observate" (NU "spune-mi
  ce este: tranzactie / factura / linie produs") - lista business
  invita modelul sa aleaga din optiuni semantice; "estimeaza pe baza
  structurii" il tine descriptiv. ANTI-HALLUCINATION critic.
- "Estimeaza" (NU "spune-mi ce este") - implica incertitudine onesta
  si bazare pe observabile, NU certitudine ontologica.
- "Clasifica in niveluri mic/mediu/mare" (NU "putine vs multe") -
  ordinala cu 3 niveluri, mai utila operational, mai usor de auditat.
- "Predominant repetitive" (NU "unde ar trebui sa se repete") -
  observatie de pattern detectat, NU judecata externa de expectatie
  business.

NOTA structurala: cele 2 prompturi sunt secventiale. Promptul 2 incepe
cu "Pentru acelasi set" - presupune ca Promptul 1 a fost rulat in
sesiunea anterioara Copilot. Operatorul nu redeschide context.

ECHO PROMPT-uri in alte livrabile:
- HTML-STUDY: PROMPTS-text caseta cu cele 2 prompturi copy-paste.
- HTML-VIDEO: PROMPTS-text in modul broadcast persoana a 3-a plural.
- FILM-Excel: 2 SHORT-uri (canon numar prompturi = numar SHORT-uri).
- PPT: slide PROMPTURI cu cele 2 prompturi formatate.

### 8. FINAL-LABELS (8)   [Status: NEINGHETAT]
### 8. FINAL-LABELS (8)   [Status: INGHETAT 25.05.2026]

Inghetate de Bogdan ca propunerea unica motor V24 (runda 1 acceptata
integral). Vocabular L136.A strict (zero business semantic).

```
01. CONTROL          (echo C01 pilot - operatorul stapaneste setul)
02. UNICI            (cardinalitate pe coloane categorice cunoscuta)
03. DICTIONAR        (inventarul exhaustiv al etichetelor)
04. GRANULARITATE    (nivelul atomic al randurilor stabilit)
05. FRECVENTE        (topul valorilor dominante per coloana mapate)
06. TIPOLOGIE        (coloanele clasificate pe cardinalitate)
07. RARE             (etichetele izolate marcate ca anomalii)
08. PROFIL           (fisa cap-coada a setului livrata)
```

Aliniere step-titles -> FINAL-LABELS:
- CONTROL <- STEP 01, 02 (deschide, recunoaste)
- UNICI <- STEP 05, 10 (Prompt 1, COUNTUNIQUE)
- DICTIONAR <- STEP 06, 07, 17 (citeste, incarca, confirma)
- GRANULARITATE <- STEP 08, 09 (Prompt 2, aplica)
- FRECVENTE <- STEP 11 (verifica top frecvente)
- TIPOLOGIE <- STEP 08 (clasificare cardinalitate)
- RARE <- STEP 12 (marcheaza etichete rare)
- PROFIL <- STEP 16, 17, 18 (verifica cap-coada, confirma, preda)

Pattern stilistic: CAPS, telegrafic, 1-3 cuvinte. Apar in payoff-block-ul
HTML-STUDY si HTML-VIDEO ca recapitulare vizuala cap-coada. Cursantul
pleaca cu 8 cuvinte-cheie indexate.

### 9. FENOMENE / OPERATII   [Status: INGHETAT 25.05.2026, RECALIBRAT 26.05.2026]

RECALIBRARE 26.05.2026 (in chat CONSTRUCTIE C05, motor V25 cu acceptul
ARHITECT): FENOMENELE originale presupuneau o schema fizica diferita
(cod_client × 47, status_factura, regiune_business cu variante diacritice,
canal_vanzare). Verificarea cross asset fizic Date_MASTER-initial.xlsx
(L138 aplicat retroactiv) a aratat schema reala: client_nume × 15, judet × 8,
categorie × 4, fara status sau canal. FENOMENELE au fost realiniate la
asset fizic pastrand variatia de natura. Elementele narative (INTRIGA,
MIZA, MANTRA, MOTTO, STEP-TITLES, PROMPTURI, FINAL-LABELS) raman
neschimbate - sunt independente de schema fizica.

CELE 5 FENOMENE ALESE C05 (RECALIBRATE):

**1. 15 CLIENTI** - cardinalitate mica pe coloana client_nume
(fiecare client apare in medie ~133 de ori in set, raport unici/total 0.0075)
*Tip: cardinalitate mica concentrata. Adreseaza P1 (cati clienti unici)
+ P5 (tipologie coloane).*

**2. 4 CATEGORII** - cardinalitate foarte mica pe coloana categorie
(Hardware, Software, Consumabile, Servicii)
*Tip: cardinalitate minima. Adreseaza P5 (tipologie coloane - 4 categorii
e tipic dimensiune de business, NU detaliu operational).*

**3. 12 CANTITATI** - cardinalitate discreta pe coloana cantitate
(1, 2, 3, 4, 5, 8, 10, 16, 20, 25, 50, 100 - pattern de pachet operational,
NU valori continue libere)
*Tip: tipologie discreta. Adreseaza P3 (top frecvente: cantitate 1 domina
cu 542 aparitii) + P5 (cantitate e cantitativa NUMERIC dar are pattern
categorial).*

**4. 2.000 RANDURI = 2.000 FACTURI** - granularitatea atomica inferata:
o linie = o factura completa (nr_factura unic per rand)
*Tip: granularitate. Adreseaza P2 (granularitate atomica - intelegerea
ca un rand inseamna o factura, NU o linie de produs intr-o factura).*

**5. TOP-3 97.5%** - concentrare categoriala extrema: primele 3 valori
din coloana categorie acopera 97.5% din randuri
(Hardware 47.9%, Consumabile 26.1%, Software 23.6%, Servicii doar 2.5%)
*Tip: distributie 80/20 extrema. Adreseaza P3 (top frecvente) extins la
distributie. Servicii e categoria reziduala vizibila numai prin frecventa.*

VARIATIE DE NATURA (criteriu canonic BLOC 14 R-V01.x):
- Cardinalitate mica concentrata: F1 (15 valori)
- Cardinalitate minima: F2 (4 valori)
- Tipologie discreta pe coloana numerica: F3 (12 valori cantitate)
- Granularitate: F4
- Concentrare distributiva extrema: F5

NU sunt 5 variante ale aceluiasi tip. Variatie corecta validata.

CIFRE CANONICE C05 (de propagat in livrabile, aliniate la
Date_MASTER-initial.xlsx fizic):
- Set: 2.000 tranzactii, anul 2025 (data_factura), B2B RO sintetic
- 14 coloane Vanzari (predate de C04 neschimbate)
- 15 client_nume unice (medie 133 randuri/client)
- 13 cod_produs unice
- 4 categorie etichete (Hardware, Software, Consumabile, Servicii)
- 8 judet etichete (Bucuresti, Cluj, Timis, Iasi, Constanta, Brasov,
  Sibiu, Mures)
- 12 cantitate valori distincte (1, 2, 3, 4, 5, 8, 10, 16, 20, 25, 50, 100)
- 3 cota_tva valori (0.19, 0.05, 0.09)
- 3 moneda valori (RON, EUR, USD)
- Suma valoare_neta canonica: 7.986.019,38 lei (conservata din initial)
- Continuitate: Date_MASTER-C05.xlsx pleaca de la Date_MASTER-initial.xlsx
  (R-V03.49 constructii independente), suma valoare_neta conservata

PLASARE IN HTML: anomaly-grid 5 cards (titlu CAPS + cifra + descriere),
dupa exec-hero, INAINTE de Etapa 1. Pozitie identica cu C01-C04.

FENOMENE RESPINSE (din top 10 motor V24) si motiv:
- F2 12 PRODUSE: redundant cu F1 (alta cardinalitate aproape unica)
- F4 8 REGIUNI: redundant cu F2 status-uri (cardinalitate mica/medie)
- F5 1 REGIUNE IZOLATA: redundant conceptual cu F3 (ambele anomalii
  etichetare); F3 mai concreta vizual prin diacritice
- F9 0 NULURI: confirma livrabilul T1 (pozitiv), dar nu ofera revelatie
  C05; mai potrivit pentru carouselul cap-coada
- F10 5 LUNI: pod spre C07, mai potrivit ca pre-MIZA C07

---

## SPEC C05 - STATUS FINAL: COMPLET INGHETAT 25.05.2026

Toate 9 elemente narative inghetate. SPEC poate trece exit 0 la
pre_generation_check.py 05. Generarea celor 6 livrabile poate porni
(HTML-STUDY, HTML-EDIT-STUDY, HTML-VIDEO, HTML-EDIT-VIDEO, FILM, PPT,
plus INPUT.xlsx + OUTPUT.xlsx).

REZUMAT INGHETARE C05:
1. INTRIGA: "Setul are un dictionar. Excel il stie. Tu nu."
2. PROBLEMELE: P1+P2+P3+P5+P7 (5 din 10)
3. MIZA: "Obtinem dictionarul complet al setului. Nu mai privim
   tabelul fara sa stim ce contine."
4. MANTRA: "Nu privim tabelul. Il interogam."
5. MOTTO: "Un set cunoscut. Apoi orice decizie."
6. STEP-TITLES (18): cap-coada validate cu vocabular L136.A
7. PROMPTURI (2): inventar etichete + profilare structurala (L138 OK)
8. FINAL-LABELS (8): CONTROL/UNICI/DICTIONAR/GRANULARITATE/FRECVENTE/
   TIPOLOGIE/RARE/PROFIL
9. FENOMENE (5): 47 CLIENTI + 5 STATUS-URI + 3 BUCURESTI + 2.000 RANDURI
   + TOP-3 80%

---

---

## SPEC C06 - CLASIFICARE (rebuild, fost CUANTIFICARE: reguli IFS/SWITCH/XLOOKUP/scor)   [Status: INGHETAT 29.05.2026]

Treapta T2 CUNOASTERE · Axa CANTITATIVA (numeric, statistic) · pozitie 2/4.
Marker lingvistic strict: cuvantul "cifra" (cum C05 a fost "eticheta").
Separare obsesiva C05/C06 (RAFINARE L136.A): C05 = ETICHETE, C06 = CIFRE.
Intrebare-mama: "Cum arata numeric setul?" (descriptiv, NU decizional).

### 1. INTRIGA
Setul are cifre. Excel le stie. Tu nu.

### 2. PROBLEMELE (profilare, incep cu Cat/Care/Cum)
- Cat insumeaza setul, total si pe categorie?
- Care e media si mediana per factura?
- Cat de intins e setul (minim, maxim, amplitudine)?
- Cum se concentreaza valoarea (Pareto numeric, nu de frecventa)?
- Care sunt extremele numerice (top-N si bottom-N)?

### 3. MIZA
Operatorul iese cu fisa de profil NUMERIC a setului (intervale, medii,
distributii, agregate). NU strategie, NU prioritizare (acelea vin la T3).

### 4. MANTRA
Nu privim tabelul. Il interogam. (voce T2 partajata)
Accent de separare pe slide-uri: C06 = CIFRE.

### 5. MOTTO
O cifra cunoscuta. Apoi orice decizie.

### 6. STEP-TITLES (6 etape macro)
- ETAPA 1 · DESCHIDERE NUMERICA
- ETAPA 2 · INTEROGARE ASISTATA DE AI
- ETAPA 3 · PROFILARE CANTITATIVA
- ETAPA 4 · AUDIT AL AGREGATELOR
- ETAPA 5 · ANCORARE LA SURSA
- ETAPA 6 · PREDAREA PROFILULUI NUMERIC

### 7. PROMPTURI (2 Copilot)
P1 (ETAPA 2 interogare agregate): "Calculeaza pentru coloana valoare_neta:
suma totala, media, mediana, minimul si maximul. Apoi suma pe fiecare
categorie de produs."
P2 (ETAPA 3 profilare distributii): "Arata-mi cum se distribuie valoarea
pe categorii: ce procent din total aduce fiecare categorie si care sunt
primele si ultimele facturi dupa valoare_neta."

### 8. FINAL-LABELS (8 ancore de retentie)
- SUMA TOTALA
- MEDIE SI MEDIANA
- AMPLITUDINE
- DISPERSIE
- CONCENTRARE
- TOP-N / BOTTOM-N
- PROFIL NUMERIC
- O CIFRA CUNOSCUTA

### 9. FENOMENE / OPS

CELE 5 FENOMENE ALESE (axa cantitativa, COLOANE REALE din asset):

**1. Suma totala si pe categorie** — SUM, SUMIFS pe valoare_neta grupat
pe categorie. Setul are o dimensiune.

**2. Medie si mediana per factura** — AVERAGE, MEDIAN pe valoare_neta;
contrastul medie-vs-mediana arata asimetria.

**3. Amplitudine** — MIN, MAX pe valoare_neta; intinderea setului.

**4. Dispersie** — STDEV pe valoare_neta; cat de imprastiate sunt cifrele.

**5. Concentrare numerica** — proportii % pe categorie, LARGE/SMALL pentru
top-N si bottom-N facturi dupa valoare_neta (Pareto numeric, distinct de
Pareto-frecventa din C05).

Operatii: SUM, SUMIFS, AVERAGE, AVERAGEIFS, MEDIAN, MIN, MAX, STDEV,
LARGE, SMALL, proportii procentuale.

DATE (Date_MASTER-C06.xlsx): NU planteaza anomalii. Porneste din output-ul
curat conservat, adauga coloana derivata marja_estimata (procent sintetic
pe categorie) si sheet KPI_GENERAL cu agregatele descriptive.
Suma conservata: 7.986.019,38 lei (DELTA 0).
Coloane reale folosite: valoare_neta, categorie, cantitate, pret_unitar,
client_nume, nr_factura.

---

## SPEC C07 - DATARE (MEMORIA SETULUI)   [Status: INGHETAT 29.05.2026]

Treapta T2 CUNOASTERE · Axa TEMPORALA (unica pe treapta) · pozitie 3/4.
Obiect: memoria. Marker lingvistic strict: cuvantul "memorie" (+ vocabular
temporal: luna, perioada, evolutie, ritm, sezon). Separare obsesiva: C07 =
TIMP (cum se misca setul), C08 = ECOSISTEM (cu cine vorbeste setul).
Intrebare-mama: "Cum se comporta setul in timp?"

### 1. INTRIGA
Setul are memorie. Excel o tine minte. Tu nu.

### 2. PROBLEMELE (profilare temporala, incep cu Pe ce / Care / Cum / Exista)
- Pe ce perioada reala se intind tranzactiile?
- Exista luni care lipsesc din timeline?
- Care e ritmul natural al setului (volum pe luna)?
- Care e luna dominanta si care cea minima?
- Setul accelereaza sau incetineste?
- Exista sezonalitate recurenta si o saptamana tipica?

### 3. MIZA
Operatorul iese cu memoria temporala a setului (perioada, ritm, trend, sezon).
Nu mai presupune cand s-a intamplat. NU strategie, NU prognoza (acelea vin la T3).

### 4. MANTRA
Nu privim tabelul. Il interogam. (voce T2 partajata)
Accent de separare: C07 = MEMORIE (timpul setului).

### 5. MOTTO
O memorie citita. Apoi orice decizie.

### 6. STEP-TITLES (6 etape macro)
- ETAPA 1 · DESCHIDERE TEMPORALA
- ETAPA 2 · INTEROGARE ASISTATA DE AI
- ETAPA 3 · PROFILARE TEMPORALA
- ETAPA 4 · AUDIT AL CRONOLOGIEI
- ETAPA 5 · ANCORARE LA SURSA
- ETAPA 6 · PREDAREA MEMORIEI

### 7. PROMPTURI (2 Copilot)
P1 (ETAPA 2 interogare cronologie): "Pentru coloana data_factura spune-mi
perioada acoperita (prima si ultima data), cate luni distincte exista si daca
lipseste vreo luna din secventa. Apoi numara tranzactiile pe fiecare luna."
P2 (ETAPA 3 profilare ritm): "Pentru acelasi set arata-mi cum evolueaza volumul
lunar (creste sau scade), care luna are cel mai mare si cel mai mic volum, si ce
zi a saptamanii concentreaza cele mai multe tranzactii."

### 8. FINAL-LABELS (8 ancore de retentie)
- PERIOADA
- TIMELINE
- GOLURI
- RITM
- LUNA-VARF
- TREND
- SEZON
- MEMORIE

### 9. FENOMENE / OPS

CELE 5 FENOMENE ALESE (axa temporala, COLOANE REALE din asset):

**1. Perioada acoperita** — MIN si MAX pe data_factura; prima si ultima luna,
intinderea reala a setului in timp.

**2. Goluri in timp** — secventa lunilor; ce luni lipsesc din timeline.

**3. Ritm lunar** — COUNT pe data_factura grupat pe luna; volumul tipic/luna.

**4. Trend** — directia volumului luna-la-luna (creste/scade/stationar).

**5. Sezonalitate si saptamana tipica** — grupare pe luna-din-an si pe ziua
saptamanii (extrase din data_factura); recurente si zi predilecta.

Operatii: MIN, MAX pe date, COUNT/COUNTIFS pe luna, grupare cronologica,
delta luna-la-luna, extragere componente (luna-din-an, zi-din-saptamana).

DATE (Date_MASTER-C07.xlsx): NU planteaza anomalii. Porneste din output-ul C06,
adauga sheet-uri temporale (_TIMELINE, _TREND, _RITM, _SEZON, CONTROL_FINAL).
Suma conservata: 7.986.019,38 lei (DELTA 0).
Coloane reale folosite: data_factura, valoare_neta, nr_factura.

---

## SPEC C08 - CARTOGRAFIERE (HARTA ECOSISTEMULUI)   [Status: INGHETAT 29.05.2026]

Treapta T2 CUNOASTERE · Axa RELATIONALA DESCRIPTIVA · pozitie 4/4 (inchide T2).
Obiect: ecosistemul. Marker strict: "ecosistem" (+ satelit, cheie, rol, camp extern).
SEPARARE OBSESIVA C08 vs C09: C08 CARTOGRAFIAZA (recunoaste relatiile posibile,
descriptiv). C09 (T3) CONSTRUIESTE relatiile reale (merge, 1:M, Data Model,
masuri). C08 NU uneste, NU modeleaza, NU analizeaza prin relatii.
Intrebare-mama: "Cu cine vorbeste setul?"

### 1. INTRIGA
Setul are un ecosistem. Excel il vede. Tu nu.

### 2. PROBLEMELE (recunoastere, incep cu Ce / Care / Cu cine)
- Ce alte seturi descriu setul principal?
- Care e cheia comuna cu fiecare satelit?
- Ce rol are fiecare set: fapt sau descriere?
- Ce campuri lipsesc din setul principal dar exista in sateliti?
- Ce conventii difera si trebuie aliniate inainte de modelare?

### 3. MIZA
Operatorul iese cu harta ecosistemului de date din jurul setului: stie cu cine
vorbeste, prin ce chei, cu ce roluri. NU uneste, NU construieste model (acelea
sunt C09/T3). Doar cartografiaza inainte de a lega.

### 4. MANTRA
Nu privim tabelul. Il interogam. (voce T2 partajata)
Accent de separare: C08 CARTOGRAFIAZA. Nu uneste.

### 5. MOTTO
Un ecosistem cunoscut. Apoi orice decizie.

### 6. STEP-TITLES (6 etape macro)
- ETAPA 1 · DESCHIDERE RELATIONALA
- ETAPA 2 · INTEROGARE ASISTATA DE AI
- ETAPA 3 · CARTOGRAFIEREA ECOSISTEMULUI
- ETAPA 4 · AUDIT AL CHEILOR
- ETAPA 5 · ANCORARE LA SURSA
- ETAPA 6 · PREDAREA HARTII

### 7. PROMPTURI (2 Copilot)
P1 (ETAPA 2 interogare ecosistem): "Pe langa foaia Vanzari, ce alte foi exista in
acest registru? Pentru fiecare spune-mi ce coloana-cheie o leaga de Vanzari si ce
rol are: fapt sau descriere."
P2 (ETAPA 3 campuri externe + conventii): "Ce campuri descriptive exista in foile
satelit dar lipsesc din Vanzari? Si ce conventii de cod sau format difera intre foi
si ar trebui aliniate inainte de a construi relatii?"

### 8. FINAL-LABELS (8 ancore de retentie)
- SATELITI
- CHEI
- ROLURI
- FAPT
- DESCRIERE
- CAMP EXTERN
- CONVENTII
- ECOSISTEM

### 9. FENOMENE / OPS

CELE 5 FENOMENE ALESE (axa relationala descriptiva, structuri REALE din registru):

**1. Setiele-satelit** — pe langa Vanzari, registrul contine foile CLIENTI,
PRODUSE, AGENTI, DEPOZITE. Setul nu e singur.

**2. Cheile comune** — coloana cod_produs leaga Vanzari de PRODUSE; client_nume si
judet trimit catre CLIENTI; fiecare satelit are cheia lui de legatura.

**3. Rolul fiecarui set** — Vanzari = fapt (tranzactiile); CLIENTI/PRODUSE/AGENTI/
DEPOZITE = descriere (lookup). Faptul masoara, descrierea explica.

**4. Campuri externe** — atribute descriptive care exista doar in sateliti, absente
din Vanzari (ex. descrierea produsului in PRODUSE dincolo de produs_nume).

**5. Conventii de aliniat** — formate de cod si denumiri care difera intre foi si
trebuie RECUNOSCUTE inainte de modelare (alinierea efectiva = C09).

Operatii: inspectie foi registru, identificare chei (cod_produs, client_nume),
clasificare fapt/descriere, listare campuri externe. NU merge, NU join, NU
Data Model (acelea sunt C09).

DATE (Date_MASTER-C08.xlsx): NU planteaza anomalii. Porneste din output-ul C07,
adauga sheet-uri de cartografiere (_ECOSISTEM, _CHEI, _ROLURI, _CAMPURI_EXTERNE,
CONTROL_FINAL). Suma conservata: 7.986.019,38 lei (DELTA 0).
Coloane reale folosite: cod_produs, produs_nume, client_nume, judet, categorie.

---

## SPEC C09 - RELAȚII   [Status: INGHETAT 04.06.2026]

> Sincronizare retroactivă registru (mandat T3-02, reparația M-2). C09 e livrat integral
> (gate_v20 PASS); registrul era stale (nume vechi „EXPLORAREA DATELOR", status NEGENERAT).
> Identitate neschimbată. Autoritate conceptuală: Bible §T3 (C09 RELAȚII LOCKED v1.0).

- Identitate: RELAȚII · verb-semnătură `a lega` · întrebare-mamă „Ce pot întreba?"
- Hero: RELAȚIILE DINTRE DATE
- Rol: activează ecosistemul recunoscut în C08 (merge / 1:M / Data Model); model interogabil.

### 1. SLUG
relatii

### 2. INTRIGA
Ai cinci tabele corecte. Și niciun răspuns care să le traverseze. Datele sunt ordonate, dar
stau separate: fiecare tabel răspunde doar despre el însuși. Intriga C09 este trecerea de la
date corecte la un model care răspunde la o întrebare ce trăiește în mai multe tabele deodată.

### 3. PROBLEMELE
- un tabel singur nu poate răspunde la o întrebare care traversează setul
- se copiază coloane dintr-un tabel în altul în loc să se lege o dată
- cheile nu sunt verificate: rămân orfani care strică răspunsul
- un Inner Join ascunde tăcut rândurile care nu se potrivesc
- se confundă unirea tabelelor diferite (join) cu adunarea tabelelor de același fel (union)
- relații greșite produc concluzii false, care par corecte

### 4. MIZA
Cursantul transformă un set cunoscut într-un model interogabil: relații corecte, verificate,
care răspund împreună la o întrebare de business. Un set cunoscut devine un model care răspunde.

### 5. MANTRA
Nu mutăm datele. Le legăm.

### 6. WOW
Tabele care stăteau alături fără să se cunoască. Acum răspund împreună la o singură întrebare.

### 7. MOTTO
Un model care răspunde. Apoi măsura stabilă.

### 8. FENOMENE C09 (5)
1. TABEL ORB — un tabel singur nu duce o întrebare care traversează setul.
2. CHEIA NEVERIFICATĂ — o legătură pe o cheie cu orfani dă răspunsuri incomplete.
3. INNER ASCUNDE — Inner Join elimină tăcut ce nu se potrivește.
4. CE NU SE POTRIVEȘTE — Left/Right ca audit al orfanilor, înainte de analiză.
5. UNION NU E RELAȚIE — a adăuga tabele de același fel nu e tot una cu a lega tabele diferite.

### 9. STEP-TITLES (6 etape)
1. Pornești de la setul cunoscut și întrebarea pe care un tabel nu o duce singur
2. Identifici relațiile cu AI (Promptul 1)
3. Activezi relațiile 1:M și alegi operația (Join vs Union, Promptul 2)
4. Verifici cu Left/Right ca audit al orfanilor (zero chei orfane)
5. Ancorezi la sursă, regula anti-derivă
6. Faci prima citire cross-tabel și predai modelul către C10

### AHA
Fără relații ai date. Cu relații ai răspunsuri.

## SPEC C10 - MĂSURI   [Status: FROZEN]

### 1. SLUG
`masuri`

### 2. INTRIGA
Relațiile sunt corecte, tabelele comunică, modelul este interogabil. Totuși, simpla existență a datelor legate nu produce decizii. Apar totaluri, medii și procente, dar ele pot induce în eroare dacă nu sunt definite ca măsuri clare, ancorate într-o întrebare reală. Intriga C10 este trecerea de la "avem cifre" la "știm exact ce măsurăm și de ce".

### 3. PROBLEMELE
- se calculează totaluri fără întrebare clară
- se folosesc medii care ascund realitatea
- se confundă cifra brută cu indicatorul util
- se folosesc procente fără bază de raportare clară
- aceeași cifră este recalculată diferit în locuri diferite
- măsura se rupe când se schimbă tăietura sau filtrul
- se trag concluzii din calcule izolate
- nu există criteriu stabil pentru ce merită măsurat

### 4. MIZA
Cursantul transformă datele legate corect în măsuri utile, controlabile, explicabile.

**O măsură bună reduce haosul, nu îl amplifică.**

### 5. MANTRA
**Măsura corectă răspunde întrebării corecte.**

### 6. WOW
Același set de date poate susține concluzii complet diferite în funcție de măsura aleasă. Problema nu este lipsa cifrelor, ci alegerea greșită a cifrei care primește autoritate.

### 7. MOTTO
**Nu calcula mai mult. Măsoară mai corect.**

### 8. FENOMENE C10
1. Măsura ca definiție unică, single source of truth.
2. Baza de raportare, procentul sau raportul își declară numitorul.
3. Reperul / pragul, măsura capătă sens raportată la o țintă sau limită definită.
4. Context-awareness, aceeași definiție produce rezultat corect pe orice tăietură sau filtru.
5. Cifra utilă vs cifra decorativă, criteriul prin care alegi ce merită promovat la rang de măsură.
6. Semnalul controlabil, măsura produce un semnal explicabil, nu doar o cifră.

### 9. STEP-TITLES FINALE
1. Confirmă că datele sunt legate corect
2. Formulează întrebarea de business, "Cât?"
3. Alege măsura potrivită întrebării
4. Definește baza de raportare a măsurii
5. Ancorează măsura într-un reper
6. Separă cifra utilă de cifra decorativă
7. Verifică robustețea măsurii
8. Confirmă setul de măsuri controlabile

---

### AHA C10
**Nu cifra contează. Contează ce întrebare răspunde cifra.**

### Schimbare mentală urmărită
De la: **Ce pot calcula?**
La: **Ce trebuie să măsor ca să pot decide?**

### Formula finală C10
**Date legate corect + întrebare clară + măsură potrivită = decizie controlabilă.**

---

# MANDAT CĂTRE CLAUDE C10

La următorul `sync`, Claude C10 trebuie să:

1. trateze acest SPEC ca final și înghețat,
2. genereze C10 dacă regulile locale permit,
3. păstreze C10 strict pe `a defini`, nu pe `a compara`,
4. nu includă ranking, contribuție, comparație contextuală, ABC sau Pareto,
5. nu modifice fișiere sistem,
6. nu modifice alte construcții,
7. raporteze rezultatul în `_brain/c10/CLAUDE-TO-BRAIN.md`.
## SPEC C11 - COMPARATII / RANK   [Status: INGHETAT 04.06.2026]

> Realiniere BRAIN-006 + îngheț construcție (mandat C11-02). Identitatea veche
> „DATA MODEL" abandonată (acum teritoriu C09 RELAȚII). Sursa canonică:
> `_brain/c11/BRAIN-TO-CLAUDE.md` (SPEC_FROZEN). Autoritate conceptuală:
> Bible §T3 (C11 COMPARAȚII LOCKED). Înscriere sistem prin mandat C11-04.

- Identitate: COMPARAȚII / RANK · verb-semnătură `a compara` · întrebare-mamă „Care?"
- Hero: COMPARAȚII
- Rol: așază măsurile definite în clasament, diferență, contribuție și concentrare;
  transformă lista plată în ierarhie decizională. Vine DUPĂ C10 MĂSURI și ÎNAINTEA
  C12 INTERPRETARE în lanțul T3 (model -> măsură -> clasament -> explicație).

### 1. SLUG
comparatii

### 2. INTRIGA
Datele sunt legate corect și măsurate corect. Totuși o listă de măsuri, oricât de
corectă, rămâne o masă plată. Ochiul nu poate ierarhiza singur o coloană lungă de
numere, iar „mare în listă" este confundat cu „important pentru rezultat". C11 face
trecerea de la „avem măsuri corecte" la „știm cine contează", de la listă plată la
ierarhie clară.

### 3. PROBLEMELE
- citești lista fără să vezi cine conduce rezultatul
- compari valori care nu sunt comparabile
- confunzi „mare în listă" cu „important pentru rezultat"
- tratezi toate elementele ca egale, fără ierarhie
- reacționezi la diferențe minuscule, unde zgomotul pare semnal
- nu vezi concentrarea, adică puțini actori duc majoritatea rezultatului
- ignori contribuția în total
- decizi pe baza ordinii brute, fără reper relativ

### 4. MIZA
Transformi măsurile corecte într-o ierarhie decizională. Vezi cine duce rezultatul și
cine doar apare în listă. Fără comparație, analiza rămâne plată. Cu comparație, datele
capătă ierarhie.

### 5. MANTRA
Nu toate valorile sunt egale. Unele conduc rezultatul.

### 6. WOW
Într-un set cu multe elemente, de obicei o mână duce majoritatea rezultatului.
Comparația corectă arată că „mult" și „important" nu sunt același lucru. Lista plată
ascunde o ierarhie dură, în care câțiva actori decid totul.

### 7. MOTTO
Nu citi lista. Citește ierarhia.

### 8. FENOMENE C11 (6)
1. Clasamentul, ordonarea actorilor după o măsură; cine e sus, cine e jos, instant.
2. Diferența reală vs zgomotul, contează gap-ul dintre poziții, nu doar ordinea.
3. Contribuția / ponderea în total, cât duce fiecare actor din rezultatul global.
4. Concentrarea Pareto / ABC, puțini actori duc majoritatea rezultatului.
5. Comparabilitatea, compari doar ce are aceeași bază, unitate, perioadă și numitor.
6. Reperul relativ, poziția capătă sens raportată la lider, mediană sau grup.

### 9. STEP-TITLES (8)
1. Confirmă măsura pe care compari
2. Asigură comparabilitatea
3. Așază actorii în clasament
4. Citește diferențele reale
5. Calculează contribuția în total
6. Identifică concentrarea
7. Raportează poziția la reper
8. Confirmă ierarhia decizională

### DELIMITĂRI (gardă de treaptă)
C11 NU redefinește măsura (vine din C10). C11 NU explică de ce apare ierarhia (cauza =
C12). C11 NU construiește dashboard (raportarea = T4). C11 compară actori agregați, nu
etichetează rânduri individuale (vs C06). R-V02.14 sumă conservată (input C11 = output
C10); R-V02.15 zero cifre business în HTML/FILM.

### AHA
Nu volumul contează, ci ierarhia. Puțini actori duc rezultatul.

### FORMULA FINALĂ
Măsuri comparabile + clasament + contribuție = ierarhie decizională.

## SPEC C12 - INTERPRETARE   [Status: INGHETAT 04.06.2026]

> Realiniere BRAIN-006 + îngheț construcție (mandat C12-02). Identitatea veche
> „PRIORITIZARE EXECUTIVA" abandonată. Sursa canonică: `_brain/c12/CLAUDE-TO-BRAIN.md`
> (SPEC_FROZEN). Autoritate conceptuală: Bible §T3 (C12 INTERPRETARE LOCKED).

- Identitate: INTERPRETARE · verb-semnătură `a explica` · întrebare-mamă „De ce?"
- Hero: DE CE-UL DIN DATE
- Rol: explică insight-ul verbal, cauza citită din model, interpretarea rezultatului
  după relații, măsuri și comparații. ÎNCHIDE treapta T3 ANALIZA.

### 1. SLUG
interpretare

### 2. INTRIGA
Modelul răspunde, măsurile sunt definite, clasamentul este clar. Știm cine conduce și
cu cât diferă. Și totuși rămâne întrebarea care contează cel mai mult pentru decizie:
de ce? Un clasament arată CARE, dar nu spune DE CE. Intriga C12 este trecerea de la
rezultatul numeric corect la explicația verbală pe care un om o poate înțelege, contesta
și folosi.

### 3. PROBLEMELE
- se citește clasamentul, dar nu se explică ce îl produce
- se confundă ce apare împreună cu ce produce rezultatul
- se construiește o poveste plauzibilă pe care datele nu o susțin
- rezultatul se atribuie unei singure cauze când lucrează mai mulți factori
- aceeași cifră primește explicații diferite de la oameni diferiți
- un total ascunde cauza reală care apare doar pe tăietură
- explicația nu poate fi verificată înapoi în model
- insight-ul rămâne în capul analistului, netranscris într-o frază clară

### 4. MIZA
Cursantul transformă rezultatul numeric în explicație verbală ancorată în model, pe care
o poate apăra și verifica. O explicație bună spune de ce, nu doar cât.

### 5. MANTRA
Cifra spune cât. Explicația spune de ce.

### 6. WOW
Același clasament poate avea două explicații opuse, și doar una se verifică în date.
Diferența dintre un analist și un povestitor nu este cifra, ci capacitatea de a arăta în
model de unde vine cifra.

### 7. MOTTO
Nu citi rezultatul. Explică-l.

### 8. FENOMENE C12 (6)
1. Insight-ul verbal, traducerea rezultatului numeric într-o frază pe care un decident o înțelege.
2. Cauza citită din model, explicația ancorată în relații, măsuri și comparații, nu în presupunere.
3. Ce apare împreună nu explică automat ce produce rezultatul, coincidență vs cauză efectivă.
4. Cauza multiplă, rezultatul rar are o singură cauză; identifici factorii principali, nu forțezi o explicație unică.
5. Cauza ascunsă de agregare, explicația reală apare doar când cobori sub total, pe tăietura potrivită.
6. Explicația verificabilă, orice „de ce" trebuie arătat înapoi în model; povestea pe care datele nu o susțin se respinge.

### 9. STEP-TITLES (8)
1. Confirmă că ai model, măsuri și clasament
2. Formulează întrebarea de business, „De ce?"
3. Citește cauza din model, nu din presupunere
4. Verifică dacă ce apare împreună chiar produce rezultatul
5. Identifică factorii principali, nu o cauză unică
6. Coboară sub total ca să găsești cauza ascunsă
7. Scrie insight-ul într-o frază verificabilă
8. Închide analiza: treapta T3 finalizată

### DELIMITĂRI (gardă de treaptă)
C12 NU face: dashboard (T4), what-if, scenarii, predicție, recomandare de acțiune (T5),
re-ierarhizare (C11). C12 explică ce s-a întâmplat și de ce, pe baza modelului. Închide T3 (R-V02.7).

### AHA
Nu rezultatul contează. Contează de ce apare rezultatul.

### FORMULA FINALĂ
Rezultat numeric + cauză citită din model + frază verificabilă = insight care închide analiza.

## SPEC C13 - VIZUALIZAREA   [Status: INGHETAT 08.06.2026]

Axă: ONESTITATEA FORMEI. Pilon T4: T4 consumă răspunsul produs de T3, nu îl naște.
Decizie locked: C13 = obiect vizual onest, NU dashboard (dashboard = C14).

### 1. INTRIGA
"Cifra e corectă. Graficul minte."

### 2. PROBLEMELE
- aceeași cifră produce concluzii diferite prin forme diferite
- graficul pare obiectiv, dar forma e aleasă de autor
- ochiul crede forma înainte să verifice cifra
- AI generează graficul, dar nu garantează onestitatea lui
- decidentul crede că vede datele, dar vede o formă vizuală prost aleasă

### 3. MIZA
"O decizie este luată cu încredere pe o imagine falsă construită peste date corecte."

### 4. MANTRA / AHA
MANTRA: "Nu desenez frumos. Desenez adevărat."
AHA: "Forma greșită minte cu cifra corectă."

### 5. MOTTO
"Forma nu se nimerește. Se alege."

### 6. STEP-TITLES (18, în 6 etape x 3 pași)
ETAPA 1 REALITATE
1. Răspunsul corect, dar invizibil
2. Nimeni nu decide privind un model
3. Aceeași cifră, încă fără formă
ETAPA 2 INVESTIGAȚIE
4. O cifră, mai multe forme posibile
5. Promptul 1: ce formă cere rezultatul
6. Aceeași cifră, două grafice, două concluzii
ETAPA 3 TRANSFORMARE
7. Tipul de grafic urmează natura rezultatului
8. Promptul 2: generezi vizualul, corectezi axa și scala
9. Scoți codarea care sugerează fals
ETAPA 4 VERIFICARE
10. Vizualul față de cifra brută: aceeași concluzie?
11. Testul celui de-al doilea ochi
12. Marchezi forma care spune mai mult decât cifra
ETAPA 5 STABILIZARE
13. Cele șase reguli de onestitate a formei
14. Eticheta, unitatea, contextul: nimic de ghicit
15. Un obiect vizual onest, repetabil
ETAPA 6 CONFIRMARE
16. Forma onestă repară percepția
17. Devii garantul a ceea ce vede altcineva
18. Predai către C14: obiectul, gata de așezat în pagină

### 7. PROMPTURI Copilot (2)
- Promptul 1, E2 INVESTIGAȚIE: ce formă cere rezultatul (AI propune, omul judecă)
- Promptul 2, E3 TRANSFORMARE: generezi vizualul, corectezi axa și scala (omul corectează)

### 8. FINAL-LABELS (8)
- Cifra corectă nu garantează grafic corect.
- Forma este o decizie.
- Axa poate exagera adevărul.
- Tipul de grafic urmează natura rezultatului.
- Scala trebuie să fie declarată.
- Codarea vizuală spune un singur lucru.
- Eticheta, unitatea și contextul elimină ghicitul.
- Vizualul corect produce aceeași concluzie ca cifra brută.

### 9. FENOMENE / OPERATII (6 perechi: deformare -> corecție onestă)
- Axa care exagerează -> axa pleacă de la zero, sau abaterea e declarată explicit.
- Tipul de grafic nepotrivit -> tipul urmează natura rezultatului.
- Scala care inventează relații -> o singură scală liniară, declarată.
- Codarea care sugerează fals -> o singură dimensiune codată coerent.
- Agregarea care ascunde variația -> arăți distribuția / variația, nu doar media.
- Eticheta / unitatea / contextul lipsă -> fiecare vizual poartă unitate, etichetă și context.

### GRANIȚE
C12 = interpretarea rezultatului. C13 = forma vizuală onestă a unui rezultat deja produs. C14 = organizarea spațială (pagină / dashboard). C15 = sinteza mesajului. C16 = livrarea decision-ready. Handoff: "C13 face obiectul adevărat. C14 îl așază în pagină."

## SPEC C14 - COMPUNEREA   [Status: INGHETAT 08.06.2026]

Axă: ORGANIZAREA SPAȚIALĂ A ELEMENTELOR VIZUALE. Pilon T4: T4 consumă răspunsul produs de T3, nu îl naște.
Decizie locked: C14 = organizarea spațială a mai multor obiecte vizuale într-o pagină cu ierarhie. Dashboard = substrat tehnic posibil, NICIODATĂ identitate conceptuală. Numele vechi "DASHBOARD EXECUTIV" e SUPERSEDAT (NOMENCLATURA-LOCKED-SCARA V70: C14 COMPUNEREA, cuvânt COMPOZIȚIE, verb COMPUN).
Întrebarea-ax: "Ce vede ochiul întâi?"

### 1. INTRIGA
"Aceleași grafice corecte pot produce decizii diferite prin așezare."

### 2. PROBLEMELE
- pagina nu are un "întâi": ochiul nu știe unde să înceapă, decizia întârzie
- esențialul stă la fel de tare ca detaliul: nicio ierarhie, totul concurează
- ordinea de pe pagină este ordinea de producție, nu ordinea pentru decizie
- proximitate greșită: lucruri legate stau departe, nelegate stau lipite
- pagina prost compusă pare profesională și eșuează silențios

### 3. MIZA
"Eșecul silențios al paginii prost compuse: o decizie lentă sau greșită luată pe o pagină care pare completă, iar vina cade pe cititor, nu pe autor."

### 4. MANTRA / AHA
MANTRA: "Compun privirea, nu pagina."
AHA: "Aceleași grafice, altă ordine, altă decizie."

### 5. MOTTO
"Ce vede ochiul întâi schimbă decizia."

### 6. STEP-TITLES (11, conceptual LOCKED de BRAIN; scaffold HTML mapează la generare)
1. Pagina fără "întâi"
2. Primul punct de contact al ochiului
3. Poziția ca semnal de importanță
4. Focarul vizual
5. Traseul de citire
6. Retrogradarea elementelor secundare
7. Ierarhia vizuală pentru decizie
8. Gruparea elementelor legate
9. Spațiul gol ca instrument de ierarhie
10. Compunerea guvernată de răspunsul venit din T3
11. Testul celui de-al doilea ochi
OUTPUT C14: pagină de raportare coerentă, cu ordine vizuală, ierarhie și flux, pregătită pentru extragerea mesajului esențial în C15.
NOTĂ TEHNICĂ 11 vs 18: SPEC-ul conceptual C14 rămâne la 11 step-titles (decizie BRAIN). Cele 18 din mesajul generic pre_generation_check sunt text-instrucțiune, NU un check hard; B1 nu numără step-titles. La generare, scaffold-ul HTML (etape) mapează cele 11 fără a modifica SPEC-ul.

### 7. PROMPTURI Copilot (2)
- Promptul 1, ierarhie și ordine de citire: dă-i AI-ului obiectele vizuale deja produse și cere-i să propună ce vede ochiul întâi, ce după și ce se retrogradează. Nu redesenează obiectele, nu formulează mesajul.
- Promptul 2, compoziția paginii: cere-i o variantă de poziționare, grupare, spațiu și focar pentru pagina de raport, pe care o corectezi după criteriul "se vede întâi ce decide", nu după estetică. Nu adaugă concluzie, nu pregătește livrarea.

### 8. FINAL-LABELS (8)
- Aceleași obiecte, altă ordine, altă decizie.
- Poziția pe pagină este un argument despre importanță.
- O pagină are un singur focar.
- Ce vede ochiul întâi guvernează decizia.
- Ierarhia se face cu mărime, poziție, contrast și spațiu.
- Proximitatea spune adevărul despre relații.
- Spațiul gol este instrument, nu lipsă.
- Compoziția servește răspunsul venit din T3, nu estetica.

### 9. FENOMENE / OPERATII (6 perechi: dezordine -> compoziție pentru decizie)
- Pagina-zid fără focar -> stabilești un singur focar, atins primul.
- Esențialul îngropat în colț -> esențialul urcă în primul punct de contact al ochiului.
- Ordinea de producție pe pagină -> ordinea de citire guvernată de răspuns.
- Greutate egală la lucruri inegale -> ierarhie prin mărime, poziție, contrast, spațiu.
- Proximitate care minte despre relații -> grupare spațială a obiectelor legate.
- Horror vacui, umpli orice gol -> spațiul gol folosit ca instrument de ierarhie.

### GRANIȚE
C13 = obiectul vizual onest (atomul). C14 = organizarea spațială a mai multor obiecte într-o pagină cu ierarhie (ansamblul). C15 = sinteza mesajului esențial. C16 = livrarea decision-ready. Handoff: "C13 face obiectul adevărat. C14 îl așază în pagină. C14 predă pagina coerentă către C15." C14 NU desenează obiectul (C13), NU formulează mesajul (C15), NU livrează raportul (C16), NU face estetică, NU se autorizează ca dashboard.

## SPEC C15 - SINTETIZAREA   [Status: INGHETAT 08.06.2026]

Axă: SINTEZA — extragerea și formularea mesajului ESENȚIAL al paginii. Pilon T4: T4 consumă răspunsul produs de T3, nu îl naște.
Decizie locked: C15 = formularea mesajului esențial (headline / so-what) pe care pagina o dovedește. SINTEZA NU ESTE REZUMAT. C15 nu descoperă mesajul, îl formulează. Output = o propoziție, NU layout (C14), NU decizie (C16), NU analiză nouă (T3). SLUG: sintetizarea. SPEC 11-slot conceptual = autoritate governance/TRAINITY_ARCHITECTURE_BIBLE.md §T4 SPEC C15 (verbatim, neatins).
Întrebarea-ax (HERO): "Cum transform o pagină într-o singură frază care contează?"

### 1. INTRIGA
"Un raport corect, complet, frumos aranjat. Îl deschizi și nu știi ce să reții. Cu cât e mai plin, cu atât spune mai puțin." (ancoră scurtă, BOMBĂ LOCKED: "O pagină impecabilă. Și niciun mesaj.")

### 2. PROBLEMELE
- Rapoarte corecte pe care nimeni nu le citește până la capăt.
- Decidentul întreabă "și ce-i cu asta?" după o pagină întreagă.
- Fiecare reține altceva din aceeași pagină (sau nimic).
- Confuzia rezumat (scurtez tot) vs sinteză (spun ce contează).
- Mesajul există în date, dar nu e formulat nicăieri.

### 3. MIZA
"Un director nu citește toată pagina. O deschide și întreabă: «și ce-i cu asta?». Are zece rapoarte corecte pe masă și trei minute pentru fiecare. C15 e momentul în care o pagină întreagă capătă o singură frază care spune ce contează din ea, dintr-o privire. Nu o cifră nouă, nu o cauză nouă (acelea vin gata din analiză), ci mesajul: ce trebuie să reții. Fără sinteză, până și cel mai corect raport rămâne mut: arată tot și nu spune nimic. Cu sinteză, decidentul știe în trei secunde ce contează și ce să rețină."

### 4. MANTRA / AHA
MANTRA: "Nu rezumăm. Sintetizăm."
AHA: "O pagină arată. O sinteză spune."

### 5. WOW
"O pagină întreagă pe care trebuia s-o descifrezi. Acum o singură frază îți spune ce contează, iar pagina o dovedește."

### 6. MOTTO
"Dintr-o privire, mesajul."

### 7. STEP-TITLES (18, pe 6 etape; phase-tags E1-E6, E5 etichetă C15 = REFORMULARE)
E1 INPUT — Pagina mută:
1. Primești pagina coerentă de la C14
2. Testul celor 3 secunde: ce reține un decident? (încă nimic)
3. De ce o pagină corectă poate fi mută
E2 AI — Rezumatul automat:
4. AI propune un rezumat draft al paginii
5. Formula: "Rezumatul scurtează tot. Sinteza spune ce contează."
6. De ce rezumatul nu e încă mesajul
E3 SINTEZĂ — Mesajul esențial:
7. Care e singura afirmație pe care pagina o dovedește?
8. Formulezi headline-ul (so-what) într-o singură frază
9. Mesajul pentru ACEASTĂ decizie și audiență
E4 CONTROL — Testul "și ce-i cu asta?":
10. Filtrul "fără asta, decidentul hotărăște la fel?"
11. Indicativ, nu decizional (≠C16)
12. Formulat, nu descoperit (nicio cifră/cauză nouă, ≠T3)
E5 REFORMULARE — Mesajul se adaptează la schimbare:
13. Pagina se schimbă (datele s-au actualizat în amonte, în model/T3) → mesajul vechi nu mai e exact
14. Reformulezi headline-ul, refaci sinteza, NU recalculezi nimic; cifrele rămân ale modelului
15. Noul mesaj rămâne o singură afirmație susținută de pagină, pe același criteriu: ce contează
E6 PAYOFF — O pagină a devenit un mesaj:
16. O pagină coerentă a devenit un mesaj care contează
17. Mesajul + pagina-dovadă, împreună
18. Predare către C16 (care îl va încadra pentru decizie)
OUTPUT C15: o pagină de raport care spune, într-o singură frază, ce contează (mesajul esențial, dovedit de pagină), predată către C16 pentru încadrare de decizie.

### 8. PROMPTURI Copilot (2)
- Promptul 1 (DRAFT, E2): pe baza raportului, AI propune 3 titluri candidate de o singură frază care spun ce contează pentru decizia/audiența dată. Nu calculează cifre noi, nu explică de ce — formulează din ce e deja în raport. Omul alege și ascute.
- Promptul 2 (TEST, E4): pentru titlul ales, AI verifică: o singură afirmație? indicativ (nu spune ce să faci)? nu introduce cifră/cauză absentă din raport? trece "fără asta, decidentul hotărăște la fel?". Omul decide forma finală.

### 9. FENOMENE / OPERATII (5: pagină mută -> mesaj esențial)
- Rezumat vs sinteză: același raport, două ieșiri (scurtare proporțională vs afirmația-cheie).
- Mesaj dependent de audiență/decizie: aceeași pagină -> mesaj diferit pentru CFO vs operațiuni.
- Testul "și ce-i cu asta?": o frază care mută decizia vs una care e zgomot.
- Headline-ul ancorează citirea: aceeași pagină, două headline-uri -> ochiul reține altceva.
- Mesaj susținut de pagină (pagina îl dovedește) vs afirmație nesusținută.

### 10. VERIFICĂRI (8)
1. O singură propoziție. 2. Indicativ, nu decizional (≠C16). 3. Nicio cifră/cauză nouă (≠T3). 4. Trece "fără asta, decidentul hotărăște la fel?". 5. Sinteză, nu rezumat. 6. Pagina îl dovedește. 7. Nu rearanjează pagina (≠C14). 8. Verb SINTETIZEZ.

### SUBSTRAT EXCEL (strat MESAJ)
Date_MASTER-C15 = dashboard moștenit (C13/C14) + strat MESAJ: celulă headline (text formulat de cursant) + linie so-what + legătură la pagina-dovadă. FACE: enunță în cuvinte ce contează; leagă mesajul de dovadă; cel mult inserează într-o frază-șablon o valoare deja calculată în amonte (plasare, nu calcul). NU FACE: nu calculează insight, nu descoperă cauză, nu generează recomandare, nu rearanjează pagina, nu mută C15 în C14/C16/T3. Regula de aur: mesajul citește din pagină, nu produce pagina.

### FORMULA LOCKED
"Rezumatul scurtează tot. Sinteza spune ce contează."

### GRANIȚE
C14 = organizarea spațială a paginii (layout). C15 = sinteza mesajului esențial (propoziție). C16 = livrarea decision-ready. Handoff: "C14 predă pagina coerentă. C15 formulează mesajul esențial. C15 predă mesajul + pagina-dovadă către C16." C15 NU organizează pagina (C14), NU numește decizia / nu predă pentru decident (C16), NU descoperă cauză / nu calculează (T3/C12), NU rezumă (rezumat != sinteză).
## SPEC C16 - LIVRAREA   [Status: INGHETAT 08.06.2026]

Axă: RAPORT DECISION-READY. Pilon T4: T4 consumă răspunsul produs de T3, nu îl naște.
Decizie locked: C16 = foaie-raport de decizie (raportul devine obiect de decizie), NU logistică (email/export/PDF/share/trimitere = logistică, nu livrare), NU sinteză (C15), NU layout vizual (C14), NU sistem recurent (C17).
Nomenclatură LOCKED (NOMENCLATURA-LOCKED-SCARA V70): C16 LIVRAREA, cuvânt LIVRARE, verb LIVREZ. Numele vechi "CONTROL INSTANT" e superseded.
Nota: SPEC narativ M-A (revizuit) aprobat de BRAIN 08.06.2026; înlocuiește blocul SEED 11-slot. IDENTITATE_TEHNICA C16 populată (L142). Hero descriptor (IDENTITATE-TEHNICA) = "DECIZIA GATA" PROVIZORIU, de confirmat BRAIN.

### 1. INTRIGA
Ai răspunsul, e și sintetizat (C15), dar decidentul tot nu decide: cere clarificări, amână, "se mai gândește". Raportul bun care nu mișcă nimic. Distanța dintre "am terminat analiza" și "s-a luat decizia".

### 2. PROBLEMELE
- mesajul esențial (de la C15) e îngropat, nu stă în capul foii ca decizie cerută;
- complet, dar aglomerat: decidentul se îneacă în detaliu fără relevanță pentru decizie;
- raportul are nevoie de autor lângă el ca să fie înțeles (nu se susține singur);
- lipsește cadrul de decizie (decizie, risc, concluzie, pas următor): e informație, nu ramă de decizie;
- livrarea tratată ca logistică ("am trimis"), nu ca obiect de decizie.

### 3. MIZA
Valoarea întregului lanț T1-T4 se realizează sau se pierde în momentul livrării. O decizie amânată sau greșită pentru că raportul nu a livrat decizia = analiză irosită. Livrarea e locul unde analiza devine (sau nu) acțiune.

### 4. MANTRA / AHA
MANTRA: "Nu livrez informație. Livrez o decizie gata de luat."
AHA: "Raportul nu se trimite, se predă ca obiect de decizie."

### 5. MOTTO
"Raportul care decide."

### 6. STEP-TITLES (18, în 6 etape x 3 pași)
ETAPA 1 REALITATE
1. Mesajul sintetizat, dar încă nu o decizie
2. Raportul plin, iar decidentul tot întreabă
3. Aceeași informație, încă fără cadru de decizie
ETAPA 2 INVESTIGAȚIE
4. Ce decizie se cere, de fapt, din acest raport
5. Promptul 1: ce-i trebuie decidentului ca să decidă (AI propune, omul judecă)
6. Ce e semnal pentru decizie, ce e zgomot
ETAPA 3 TRANSFORMARE
7. Concluzia urcă în capul foii
8. Promptul 2: construiești cadrul decizie / risc / concluzie / pas următor (omul corectează)
9. Detaliul exhaustiv coboară în anexă
ETAPA 4 VERIFICARE
10. Poate decidentul hotărî doar din foaie?
11. Testul fără autor: întrebările inevitabile, nu întrebările de bază
12. Riscul și pasul următor, scrise explicit, nu deduse
ETAPA 5 STABILIZARE
13. Cele șase reguli ale foii-raport de decizie
14. Complet pentru decizie, fără surplus
15. O foaie-raport de decizie care stă în picioare singură
ETAPA 6 CONFIRMARE
16. Forma de decizie scurtează drumul spre hotărâre
17. Devii cel care predă o decizie, nu un teanc de date
18. Raportul-decizie este gata, T5 îl poate sistematiza

### 7. PROMPTURI Copilot (2)
- Promptul 1, E2 INVESTIGAȚIE: ceri Copilot să identifice, pentru un decident concret, ce decizie se cere din raport, ce risc o însoțește și ce informație e relevantă pentru decizie vs zgomot. AI propune lista, omul judecă. NU re-sintetizează mesajul (C15), îl încadrează pentru decizie.
- Promptul 2, E3 TRANSFORMARE: ceri Copilot să structureze foaia-raport cu cadrul de decizie în cap (decizie, risc, concluzie, pas următor) și detaliul în anexă, pornind de la agregatul relevant. Omul corectează formularea și pragul de risc. NU aranjează vizual (C14), NU automatizează (C17).

### 8. FINAL-LABELS (8)
- Un raport care nu produce o decizie nu e livrat, e doar trimis.
- Decizia se citește din capul foii, nu se caută la pagina 14.
- Cadrul de decizie: decizie, risc, concluzie, pas următor.
- Complet înseamnă cât îi trebuie decidentului, nu tot ce ai.
- Un raport bun se susține singur, fără autorul lângă el.
- Riscul și pasul următor se scriu, nu se deduc.
- Ce nu intră în decizie coboară în anexă, nu dispare.
- Nu livrezi informație, livrezi o decizie gata de luat.

### 9. FENOMENE / OPERATII (6 perechi: problemă de livrare -> corecție decision-ready)
Concepte reale Date_MASTER (valoarea netă, cantitatea, data facturii, categoria, clientul, județul); cifrele rămân în Excel (R-V02.15).
- Concluzia relevantă (ex. valoarea netă pe o categorie) îngropată în tabel -> urcă în capul foii ca decizie cerută.
- Detaliul brut listat linie cu linie (fiecare factură, fiecare dată) -> coboară în anexă; sus rămâne agregatul de decizie.
- Doar cifre, fără ramă de decizie -> se adaugă cadrul (decizie/risc/concluzie/pas următor) peste agregatul pe categorie, client sau județ.
- Riscul lăsat implicit (decidentul îl deduce din valoarea netă față de cantitate) -> riscul scris explicit, cu pragul lui.
- Raportul se termină în constatare -> se scrie pasul următor (acțiunea propusă), ancorat în datele care o susțin.
- Foaia are nevoie de autor -> fiecare cifră poartă unitate, perioadă (data facturii) și referință, ca foaia să se susțină singură.

### GRANIȚE
- vs C12 (T3): C12 interpretează (de ce); C16 nu re-interpretează, primește răspunsul și îl livrează ca decizie.
- vs C15 (jos): C15 sintetizează mesajul esențial (enunț); C16 NU sintetizează, livrează mesajul deja sintetizat dându-i forma de decizie (decizie-cadru).
- vs C14: C14 face compunerea vizuală / layout-ul paginii (spațiu); C16 NU aranjează vizual, lucrează cadrul de decizie al raportului.
- vs C17 (sus): C17 sistematizează raportul în T5 AUTONOMIE (recurent, dashboard viu, automatizare); C16 livrează o dată un raport finit, nu construiește mecanismul. Handoff: "C16 predă decizia gata; C17 o face să ruleze singură."

## SPEC C17 - SISTEMATIZAREA   [Status: NEGENERAT]
## SPEC C18 - AUTOMATIZAREA   [Status: INGHETAT 14.06.2026]

Axă: RETRAGEREA OMULUI DIN EXECUȚIA REPETITIVĂ printr-un lanț care rămâne în mișcare. Pilon T5: T5 consumă raportul livrabil (T4) și îl face să funcționeze fără autor; C18 = mișcarea (motorul), nu forma.
Decizie locked: C18 = judecata retragerii (ce e destul de stabil/repetabil încât să nu mai treacă prin mâinile autorului la fiecare ciclu) materializată într-un lanț pornit dintr-un singur declanșator. NU tutorial de unealtă, NU refresh (C04), NU buton-ca-identitate, NU autocontrol (C19), NU ownership (C20).
Nomenclatură LOCKED (NOMENCLATURA-LOCKED-SCARA V70): C18 AUTOMATIZAREA, cuvânt MOTOR, verb AUTOMATIZEZ. Iese din EFORT.
Nota: pachet conceptual aprobat de BRAIN 14.06.2026 (SEED + SPEC 11-slot + SLUG Automatizare + blueprint 6x3 + artefact _AUTOMATIZARE), mandat C18_CONCEPTUAL_INCHIS_CONFIRMAT_BRAIN. IDENTITATE_TEHNICA C18 populată (L142).

### 1. INTRIGA
Ți-ai construit sistemul (C17): munca are o formă reluabilă, există în workbook. Și totuși, la fiecare ciclu, tot tu o pornești, pas cu pas. Paradoxul: ai un sistem și ești încă veriga manuală. „Am sistem" nu înseamnă „nu mai execut".

### 2. PROBLEMELE
- același lanț de pași se reface manual la fiecare ciclu;
- autorul e gâtuirea: când e ocupat, ciclul așteaptă;
- pașii manuali introduc variație și erori între cicluri;
- timpul de judecată e mâncat de timpul de execuție;
- forma reluabilă (C17) există, dar nimic nu se mișcă fără mâna omului.

### 3. MIZA
Câtă vreme fiecare ciclu trece prin mâinile autorului, omul devine plafonul: cât poate el executa, atât se face. Automatizarea mută execuția repetitivă pe un motor și eliberează omul pentru ce doar el poate face. Procesul nu se mai oprește când autorul e prins cu altceva.

### 4. MANTRA / AHA
MANTRA: "Nu o execut. O las să ruleze."
AHA: "Ce repeți manual la fiecare ciclu nu e o sarcină. E un motor care încă merge pe mâna ta."

### 5. MOTTO
"Tu pleci din execuție, lanțul rămâne în mișcare."

### 6. STEP-TITLES (18, în 6 etape x 3 pași)
ETAPA 1 REALITATE
1. Ai un sistem, dar tot tu îl pornești
2. Același lanț de pași, refăcut cu mâna la fiecare ciclu
3. „Am sistem" nu înseamnă „nu mai execut"
ETAPA 2 INVESTIGAȚIE
4. Care pași sunt destul de stabili ca să iasă din mâinile tale
5. Promptul 1: ce merită automatizat și ce cere judecată (AI propune, omul decide)
6. Ce e repetiție mecanică, ce rămâne decizie umană
ETAPA 3 TRANSFORMARE
7. Pașii stabili, legați într-un lanț
8. Promptul 2: construiești declanșatorul unic al lanțului (omul corectează)
9. O singură atingere pornește ce făceai în mulți pași
ETAPA 4 VERIFICARE
10. Un pas manual dispare, rezultatul rămâne corect
11. Testul anti-refresh: ai eliminat un pas, nu doar ai adus date la zi
12. Contorul de atingeri scade, ciclu după ciclu
ETAPA 5 STABILIZARE
13. Ce rămâne mâna omului, marcat explicit
14. Lanțul rulează, dar nu se autocontrolează: aici intri tu
15. Un motor care merge fără tine, cu un singur punct de intervenție
ETAPA 6 CONFIRMARE
16. Testul mâinile jos: declanșezi și nu mai atingi nimic
17. Devii cel care pune în mișcare, nu cel care execută
18. Motorul rulează; C19 îl poate guverna

### 7. PROMPTURI Copilot (2)
- Promptul 1, E2 INVESTIGAȚIE: ceri Copilot să clasifice pașii ciclului în „stabili și repetabili" (candidați de automatizare) vs „cer judecată umană", pe criteriul „se face la fel de fiecare dată?". AI propune lista, omul decide. NU configurează unealta, NU stabilește praguri (C19).
- Promptul 2, E3 TRANSFORMARE: ceri Copilot să propună cum se leagă pașii stabili într-un lanț pornit dintr-un singur declanșator (secvență end-to-end). Omul corectează ordinea și ce rămâne manual. NU adaugă validări/alerte (C19), NU se rezumă la un refresh (C04).

### 8. FINAL-LABELS (8)
- „Am un sistem" nu e același lucru cu „nu mai execut".
- Ce repeți manual la fiecare ciclu e un motor care încă merge pe mâna ta.
- Automatizezi mișcarea, nu forma: forma e C17.
- Un pas eliminat nu mai trece prin tine; un refresh doar aduce date la zi.
- Lanțul pornește dintr-o singură atingere și se duce până la capăt fără tine.
- Ce rămâne mâna omului se marchează, nu se ascunde.
- C18 rulează, dar nu se autocontrolează: un eșec încă te cheamă.
- Nu o execut. O las să ruleze.

### 9. FENOMENE / OPERATII (6 perechi: execuție manuală -> retragere în lanț)
Concepte reale Date_MASTER (valoarea netă, cantitatea, data facturii, categoria); cifrele rămân în Excel (R-V02.15).
- Recalcularea agregatului pe categorie, refăcută manual la fiecare ciclu -> pasul intră în lanț și se execută la declanșare, fără mâna ta.
- Importul și curățarea aceluiași set, repetate identic -> legate în lanț; un pas manual dispare, valoarea netă rămâne identică.
- Reîmprospătarea datelor confundată cu automatizarea -> testul: ai eliminat un pas din lanț, nu doar ai adus la zi data facturii (refresh = C04).
- Pasul care cere judecată (ex. o alegere pe cantitate) -> marcat ca intervenție minimă, rămâne mâna omului (granița C19).
- Numărul de atingeri pe ciclu -> scade vizibil între ciclul 1 și ciclul 2, dovada retragerii.
- Lanțul pornit dintr-o singură atingere -> se duce până la capăt fără intervenție, mai puțin punctul minim marcat.

### GRANIȚE
- vs C04: C04 = refresh/actualizarea unui set; C18 = elimină pași din lanțul end-to-end ca să iasă omul din execuție. Refresh poate fi un pas-mijloc, nu identitatea.
- vs C17 (jos): C17 = forma reluabilă pornită de om; C18 = mișcarea fără om. C18 nu definește structura, o pune în mișcare. Handoff: „C17 predă forma reluabilă; C18 o face să ruleze fără mâini."
- vs C19 (sus): C19 = autocontrol (praguri, validări, excepții); C18 rulează, dar nu se autoguvernează: un eșec încă cheamă omul. Handoff: „C18 predă motorul care rulează; C19 îl face să se țină singur."
- vs C20: C20 = ownership/predarea controlului; C18 = mișcare tehnică, nu desemnare de proprietar.
## SPEC C19 - GUVERNAREA   [Status: NEGENERAT]
## SPEC C20 - DELEGAREA   [Status: NEGENERAT]

================================================================================

# PARTEA VII - SABLONUL HTML REPLICABIL (Pasul 6, arhitectura de sistem)

ATENTIE DOMENIU: aceasta parte defineste DOAR arhitectura de sistem a
HTML-ului. NU contine cod, NU layout vizual final, NU conatinut C01-C20.
HTML-ul este CONTAINER GOL replicabil: orice constructie se toarna identic
in el. Daca o constructie nu are inca SPEC inghetat (PARTEA VI), HTML-ul
foloseste placeholdere standard pana la alegerea finala.

REGULA DE AUR: HTML-ul foloseste DOAR elementele alese si inghetate in
SPEC-ul constructiei (1 hook ales, 1 mantra aleasa, etc.), NICIODATA toate
variantele Top 3. Top 3 traieste in sablonul de constructie (PARTEA V);
in HTML intra doar varianta inghetata.

## A. NATURA HTML-ULUI

Cockpit operational live. NU document, NU pagina de curs, NU tutorial.
Folosit dual: in invatare SI in filmare. Livrabilul central al sistemului.

## B. STRUCTURA COCKPIT-ULUI (sectiuni, in ordine obligatorie)

1. COVER / IDENTITATE - numele constructiei, treapta, hook-ul ales
   (din SPEC), tensiunea de deschidere. Un singur focus.
2. SIDEBAR DE NAVIGARE - cele 6 etape ca ancore fixe (REALITATE,
   INVESTIGATIE, TRANSFORMARE, VERIFICARE, STABILIZARE, CONFIRMARE) +
   progres vizibil.
3. ETAPA 1 REALITATE - sectiune.
4. ETAPA 2 INVESTIGATIE - sectiune.
5. ETAPA 3 TRANSFORMARE - sectiune.
6. ETAPA 4 VERIFICARE - sectiune.
7. ETAPA 5 STABILIZARE - sectiune.
8. ETAPA 6 CONFIRMARE - sectiune.
9. IDENTITATE FINALA - Problema / Reframe / Control (din SPEC) + MOTTO
   ca semnatura mentala finala. FARA payoff-numeric, FARA wow-strip cu
   cifre (R-V02.15). Wow-strip ramane ca slogan unic + bara galbena.

Cele 6 etape sunt scheletul macro (sectiuni principale). In INTERIORUL
fiecarei etape exista ritmul cinematic HOOK -> DEMO -> CONTROL -> REVEAL.

## C. CE SE INJECTEAZA IN FIECARE ETAPA (blocuri obligatorii)

Fiecare din cele 6 sectiuni-etapa contine, in ordine:
- HOOK LOCAL - micro-tensiunea de intrare a etapei (din ritmul cinematic).
- CONTINUT DEMO - ce se vede/se intampla in etapa (specific etapei).
- BLOC INVESTIGATIE / AI - unde apare promptul natural ca INSTRUMENT DE
  INVESTIGATIE (vizibil mai ales in ETAPA 2, dar poate aparea in oricare:
  operatorul investigheaza asistat de AI). NU "AI face magie".
- BLOC TRANSFORMARE - unde se vede schimbarea procedurala (vizibil mai
  ales in ETAPA 3). Descriere narativa a transformarii, FARA grid
  before/after cu cifre concrete (R-V02.15).
- BLOC VERIFICARE - unde apar verificarile concrete, demonstrabile
  (vizibil mai ales in ETAPA 4). Verifica efectul, nu prezenta. Verificarile
  sunt PROCEDURI ("ruleaza COUNTIF pe motiv_anomalie"), NU cifre afisate.
- CAPCANA - avertismentul operational al etapei (unde gresesc altii).
- REVEAL PROCEDURAL - momentul de claritate al etapei (slogan/insight,
  NU cifra). Inlocuieste vechiul "WOW MOMENT cu cifra/contrast".
- PROGRES - confirmarea vizuala ca etapa s-a maturizat.

Nu toate blocurile apar in fiecare etapa; apar unde au sens operational
(ex: BLOC INVESTIGATIE domina ETAPA 2, BLOC VERIFICARE domina ETAPA 4).
Placeholder standard daca SPEC-ul nu e inca inghetat.

INTERZIS V03 (R-V02.15): block "WOW MOMENT cu cifra/contrast", block
"REZULTAT MASURABIL cifra", block "before/after grid cu cifre".

## D. UNDE APARE FIECARE ELEMENT (maparea ceruta)

- Hook ales (din SPEC): COVER + hook local la intrarea fiecarei etape.
- Mantra aleasa (din SPEC): accent recurent, tipic la CONTROL in ritmul
  cinematic si la inchidere de etapa.
- Tensiunea: ETAPA 1 REALITATE (expunere) + hook local fiecare etapa.
- Investigatia / prompt natural: BLOC INVESTIGATIE, dominant ETAPA 2.
- Transformarile: BLOC TRANSFORMARE (narativ, fara before/after cu cifre),
  dominant ETAPA 3.
- Verificarile: BLOC VERIFICARE (proceduri, nu cifre afisate), dominant
  ETAPA 4.
- WOW din SPEC: slogan UNIC la final (banda wow-strip), FARA cifre.
- Capcanele: bloc CAPCANA per etapa relevanta.
- Reveal procedural: insight/slogan la iesirea etapelor, FARA cifre.
- Confirmarea finala: ETAPA 6 CONFIRMARE + IDENTITATE FINALA + MOTTO ca
  semnatura unica de inchidere, FARA payoff-numeric.

## E. PARITATE FUNCTIONALA OBLIGATORIE (standard absolut, nenegociabil)

REFERINTA DE STANDARD: `referinte/SABLON-HTML-Trainity.html` (SABLONUL HTML
OFICIAL TRAINITY, derivat din HTML-ul C03 vechi validat la filmare, ~91KB,
22 functii JS, 25 pasi, 8 verificari finale, 5 etape). NU e doar referinta
estetica (tokeni F-bis), ci si referinta FUNCTIONALA. Orice HTML nou trebuie
sa atinga PARITATE FUNCTIONALA cu sablonul oficial - adaptata la arhitectura
noua (6 etape, INVESTIGATIE). Un cockpit cu mai putine functionalitati decat
sablonul este RESPINS. Cockpit, NU mockup procedural.

LECTIE DE FUNDATIE (eroare reala C01, prinsa de Bogdan): primul HTML C01
generat avea ~17KB, 3 functii JS, 6 toggle-uri grosiere per etapa intreaga,
zero persistenta, zero pasi granulari, zero verificari finale, zero
highlight, zero reset, zero nav mobila. Sub 20% din functionalitatea C03.
Cauza: PARTEA VII E era vaga ("interactive, demonstreaza efectul") fara
inventar concret obligatoriu. CORECTAT prin acest inventar exhaustiv.

### CELE 12 CAPABILITATI OBLIGATORII (toate, fara exceptie)

Fiecare HTML de constructie TREBUIE sa contina, functional si testat:

1. **PERSISTENTA STARE (localStorage).** loadState/saveState. Cheie unica
   per constructie (ex. STORAGE_KEY = 'trainity-c01'). Stare = { steps:{},
   verif:{}, final:{}, activeStage:N }. La refresh pagina, TOT progresul
   (pasi bifati, verificari, etapa activa, highlights) se pastreaza. Fara
   persistenta = RESPINS.

2. **PASI GRANULARI per etapa (step-check, toggle real).** Fiecare etapa
   contine MAI MULTI pasi operationali concreti, fiecare cu propriul
   step-check toggle (nu un singur buget grosier per etapa intreaga).
   toggleStep(id) -> schimba state.steps[id] -> persista -> re-render.
   Numar de pasi per etapa: derivat din continutul real al etapei (C03
   vechi avea 4-6 pasi per etapa). Minimum credibil, nu decorativ.

3. **VERIFICARI FINALE separate (zona dedicata, final-check-btn).** Zona
   distincta de verificari finale canonice (C03 vechi: 8). Fiecare cu
   final-check-btn toggle real, confirmFinal(id) -> state.final[id] ->
   persista -> render. Verificarile finale = ritualul Trainity din
   CONTROL_FINAL Excel, reflectat in cockpit (suma control, before/after,
   integritate, volume). Numar derivat din CONTROL_FINAL al constructiei.

4. **COLAPSARE / EXPANDARE etape (stage-toggle, accordion).** toggleStage(id)
   -> activeStage comuta -> renderStages -> scroll smooth la etapa. O etapa
   activa expandata, restul colapsabile. Stare activeStage persistata.

5. **CONTOR DUBLU in progres.** nav-progress arata DOUA contoare separate:
   "X / N pasi" SI "Y / M verificari finale" (C03 vechi: "0 / 25 pasi ·
   0 / 8 final"). Bara de progres = procent global pe (pasi + finale), nu
   pe 6 etape grosier. navStepDone + navFinalDone actualizate la render.

6. **BARA PROGRES per etapa (stage-progress).** Fiecare etapa are propria
   bara de progres care reflecta procentul de pasi bifati DIN acea etapa
   (data-stage-progress). Se umple pe masura ce pasii etapei sunt bifati.

7. **FLOATING-NEXT INTELIGENT.** Nu doar scroll la urmatoarea sectiune.
   goToNextStep(): gaseste PRIMUL pas nebifat din ordinea ALL_STEPS,
   comuta la etapa lui daca e nevoie, scroll smooth + highlight temporar
   (box-shadow 3px #FFD400, 1.5s). Dupa ce toti pasii sunt bifati, trece
   la prima verificare finala nebifata. Eticheta dinamica ("PAS 07" /
   "VERIF 03"). Se ascunde cand totul e complet.

8. **HIGHLIGHT / ADNOTARE TEXT (selectie persistenta).** mouseup ->
   processSelection -> wrapTextNodeRange in <mark class="persist">. Click
   pe mark -> removeMark (scoate evidentierea). Buton "STERGE EVIDENTIERILE"
   -> clearHighlights (cu confirm). Functii complete: collectTextNodesInRange,
   nodeIntersectsRange, wrapTextNodeRange, removeMark. Doar in zona de
   continut (.main-content), exclus pe butoane/controale. Selectia ramane
   copiabila (Ctrl+C) dupa wrap.

9. **RESET PROGRES.** resetProgress() cu confirm(). Sterge steps/verif/final,
   activeStage=1, persista, re-render. Buton vizibil in sidebar.

10. **NAVIGATIE MOBILA reala.** Hamburger (mobile-nav-toggle) + overlay
    (nav-overlay) + sidebar care gliseaza (transform translateX). toggleMobileNav()
    comuta clasele open/show. La navigare, sidebar se inchide automat. NU
    doar "display:none pe sidebar la max-width" - meniu mobil functional.

11. **RENDER DINAMIC SIDEBAR.** renderStages + render: fiecare nav-item
    reflecta starea reala (active = etapa curenta, done = verificarea etapei
    confirmata, culoare verde #1F7A1F). nav-final-dot-uri reflecta finalele
    bifate. Sidebar = oglinda live a progresului, nu lista statica.

12. **COPIERE PROMPT ROBUSTA (cu fallback).** copyPrompt: incearca
    navigator.clipboard.writeText; la esec sau absenta API -> fallbackCopy
    (textarea ascuns + execCommand('copy')). Feedback vizual "COPIAT ✓"
    2s apoi revine. Buton OBLIGATORIU galben #FFD400 fundal + text negru,
    la FIECARE instanta (lectia bug-ului C03 vechi - vezi sectiunea 5 brain).

### REGULI DE STARE (toate capabilitatile care au stare)

- O singura sursa de adevar: obiectul `state`. Orice toggle muta state,
  persista (saveState), apoi re-randeaza din state (render). NU se
  manipuleaza DOM-ul direct fara a trece prin state.
- render() recalculeaza TOT din state: clase done, texte butoane
  (VERIFICA/VERIFICAT), bare de progres, contoare, vizibilitate
  floating-next, oglindire sidebar.
- Verifica EFECTUL, nu prezenta: testul unui toggle = click programatic +
  verificare schimbare clasa/text + verificare update contor/bara + (daca
  e cazul) verificare persistenta dupa reload. Lectia C01 eroare #2.

### CE RAMANE (logica de baza, neschimbata)

- SIDEBAR: cele 6 etape ancore fixe + zona verificari finale; indica etapa
  curenta; navigare directa; oglindeste progresul (vezi cap. 11).
- BLOCURI AI / INVESTIGATIE: promptul natural ca investigatie operationala;
  NU terminal feeling, NU prompt engineering, NU AI hype.
- LOGICA FINALULUI: ETAPA 6 + IDENTITATE FINALA inchid cu payoff (Problema
  / Reframe / Control din SPEC); sistem validat, nu "ending" decorativ.

## F. REGULI DE DENSITATE, RITM, PROGRES, DESIGN, UX

- DENSITATE: maximum per ecran 1 accent galben major, 1 focus dominant,
  1 payoff principal. Interzis: wall text, clutter, prea multe boxuri,
  densitate excesiva, dashboard fake, KPI fake.
- RITM: fiecare etapa respecta HOOK -> DEMO -> CONTROL -> REVEAL. Tensiune
  -> payoff continuu. NU tutorial liniar.
- PROGRES: progres psihologic vizibil (utilizatorul simte maturizarea
  sistemului etapa cu etapa), reflectat in sidebar + progress bar.
- DESIGN: brutalist premium, enterprise, cinematic, control panel, curat,
  aerisit. Interzis: tutorial feeling, curs feeling, AI hype.
- UX: whitespace premium, focus dominant per ecran, navigare clara,
  actiune de avans mereu accesibila, zero clutter.

## F-bis. STANDARD ESTETIC CONCRET (extras din HTML C03 vechi validat)

Referinta estetica: HTML-ul vechi C03 (cockpit validat la filmare). Decizia
Bogdan: se pastreaza LIMBAJUL VIZUAL (design tokens), se ignora continutul
si logica veche (5 etape/SCARA - abandonate). Acesti tokeni sunt standardul
estetic al tuturor HTML-urilor noi, adaptati la arhitectura noua (6 etape,
INVESTIGATIE, identitatea livrabilelor).

**PALETA (exacta):**
- Galben accent dominant: #FFD400 (semnatura Trainity, cel mai folosit).
- Negru: #000 (text major, casete monumentale).
- Alb: #fff (fundal).
- Verde confirmare/succes: #1F7A1F (accente de validare), inchis #155515.
- Rosu risc/eroare: #C00000.
- Portocaliu semnal: #E8A800.
- Galben-pal fundal pill: #FFFAE0.
- Griuri text: #333333 (corp), #444444, #888888 (muted), #CCCCCC
  (divider slab), #F0F0F0 (fundal bloc slab).
- Soft-black: #1a1a1a.

**TIPOGRAFIE:**
- Font stack: -apple-system, BlinkMacSystemFont, (sistem, fara webfont).
- Dimensiuni uzuale: 10-11px micro/etichete UPPERCASE, 12-14px corp,
  15-18px subtitlu, 21-26px titluri sectiune (H1 mare la cover).
- Weight: 500 corp, 700 accente, 800-900 titluri/cover.
- Letter-spacing: negativ pe titluri mari (-1px..-2px), usor pozitiv pe
  etichete UPPERCASE (0.2..0.5px).

**COMPONENTE (limbaj vizual validat, denumiri din C03):**
- COVER: cover-label (eticheta sus), cover-title (titlu masiv), subtitlu,
  microline, cover-meta-row (metadate constructie/treapta).
- SIDEBAR navigare: nav-item / nav-item-row / nav-item-num + progres mini
  (nav-progress-track / fill / stat).
- STAGE (sectiune-etapa): stage-header + stage-header-quote (mantra),
  stage-number, stage-info, stage-toggle (colapsare), stage-progress,
  stage-body, stage-exec-summary.
- STEP (pas in etapa): step-head / step-num / step-title / step-check
  (toggle interactiv) / step-body / step-action.
- ANOMALY-CARD: card de anomalie/risc (rosu/galben dupa severitate).
- PROMPT-BOX: prompt-label / prompt-text / prompt-copy (buton copiere) -
  pentru blocul INVESTIGATIE (prompt natural). SPEC EXACT INGHETAT (din
  C03 vechi validat, vezi captura Bogdan poza 2):
  - `.prompt-box`: background #000, border 1px #000, padding 22px 24px,
    margin-bottom 14px, position relative.
  - `.prompt-label`: 11px, weight 500, letter-spacing 1.4px, color #FFD400,
    margin-bottom 14px.
  - `.prompt-text`: background #1a1a1a, border 1px #333333, padding 16px
    18px, font-family "SF Mono",Consolas,"Courier New",monospace, 13px,
    line-height 1.65, color #ffffff, margin-bottom 14px, white-space
    pre-wrap, user-select text, cursor text. ::selection background
    #FFD400 color #000 (si -moz-selection).
  - **BUTON COPIERE (`.copy-btn`, OBLIGATORIU exact asa, fiecare instanta):**
    background #FFD400, color #000, border none, padding 11px 20px,
    font-size 12px, font-weight 500, letter-spacing 1px, cursor pointer,
    font-family inherit, transition all 0.15s. `:hover` background #fff.
    `.copied` (dupa copiere reusita) background #1F7A1F color #fff, text
    "COPIAT ✓" 2s apoi revine la "COPIAZĂ PROMPTUL". NICIODATA buton plat
    fara stare hover/copied. NICIODATA alt fundal decat #FFD400 in repaus.
  Acest spec e nenegociabil: butonul plat din primul C01 (fara :hover,
  fara .copied) a fost RESPINS de Bogdan. Frumos = exact stilul de mai sus.
- CAPCANA: capcana-label / capcana-text (avertisment operational).
- VERIFICATION: verif-label / verif-list / verification-btn (interactiv).
- FINAL: final-card / final-content / final-label / final-check-btn +
  nav-final-dot (identitate finala + MOTTO). FARA final-num (cifre
  monumentale eliminate prin R-V02.15). Wow-strip = banda galbena 6px +
  slogan unic + bara galbena, fara cifre afisate.
- FLOATING-NEXT: actiune persistenta de avans.

**FORME / UMBRE (brutalist premium):**
- box-shadow caracteristic: offset dur fara blur, ex. 3px 3px 0 #000;
  3px 3px 0 0 #FFD400; 2px 2px 0 0 #000; 0 4px 0 #000.
- border-radius minim (2-4px) sau deloc - estetica brutalist, colturi dure.
- Bara galbena 6px #FFD400 ca separator intre sectiuni.

**LAYOUT / SPATIERE:**
- Container max-width: 1180px (cockpit), benzi de text 780-980px.
- Sidebar ingust (coloana de navigare/progres).
- Gap-uri 4-18px (ritm dens dar aerisit); padding scalat 4-18px.
- Whitespace premium: aer in jurul focusului dominant, zero clutter.

**INTERACTIVITATE (logica vizuala, nu implementare aici):**
- step-check / verification-btn / final-check-btn = toggle-uri reale
  (schimba stare + persista). C03 vechi folosea localStorage si onclick;
  logica de implementare se decide la generare/implementare, NU aici.
- Verifica EFECTUL (schimbare stare), nu prezenta (regula PARTEA VII E).

**REGULA:** acesti tokeni sunt standardul vizual obligatoriu. Adaptarea la
arhitectura noua = aceiasi tokeni aplicati pe cele 6 etape noi (REALITATE
.. CONFIRMARE), pe blocul INVESTIGATIE (prompt-box ca instrument de
investigatie, nu comanda), pe identitatea livrabilelor. Estetica veche
pastrata; continut/logica veche IGNORATE.

### F-bis EXTENSII V01 (mai 2026) - reguli aditionale propagabile C01-C20:

**F-bis.V01.1 ANOMALY-GRID PARAMETRIZAT (numar variabil de fenomene)**

Toate fenomenele unei constructii traiesc intr-un SINGUR anomaly-grid, sub
UN SINGUR section-marker `SCENA REALA · [descriptor]`. Niciodata nu se
imparte in 2 sectiuni.

Layout responsive in functie de numar (parametrizat):
- 3-5 cards: 1 rand (3, 4 sau 5 coloane desktop)
- 6-10 cards: 2 randuri (5×2 grid - 5 col desktop, 2 randuri)
- 11-12 cards: 3 randuri (4×3 sau 6×2 - decizie chat CONSTRUCTIE)
- Mobile (≤768px): mereu 1 coloana stack vertical, indiferent de numar.

Zero separatoare intre randuri: niciun section-marker, paragraf descriptiv,
banda, text intermediar, divider, intre cards. Card-urile curg continuu in
grid (gap: 24px desktop, 16px mobile).

Card dimensiune fixa, identica pentru toate: numar (yellow box) + titlu
(caps bold) + descriere. Toate tratate vizual identic, indiferent de pozitia
in grid. Numerele curg 01-N continuu.

Plasare cronologica: anomaly-grid AUTONOM dupa mantra-band, INAINTE de
Etapa 1 (revelatie post-deschidere).

**INTERZICERI EXPLICITE (parte din regula F-bis):**
- Spargerea fenomenelor in "principale" + "complementare/suport" - toate
  fenomenele sunt egale, indiferent de complexitate operationala
- Sectiunile auxiliare gen "MECANISMUL COMPLET", "DETALII", "OPERATII
  SUPORT" intre randurile gridului
- Numerotare 01-05 + 06-10 cu narativ intre (numerotare continua 01-N)
- Section-marker dublu sub anomaly-grid

**Cauza root documentata (lectie 23):** chatul CONSTRUCTIE C04 a inventat
Cale 3 (spargere) cand a intalnit regula "5 cards" hardcoded. G-06 trebuie
sa respinga inventarea de structuri noi care nu sunt in SISTEM. Regula
F-bis cu numere hardcoded = periculoasa.

**F-bis.V01.2 SECTION-MARKER `SCENA REALA` CENTRAT**

Doar pentru banda `SCENA REALA · [descriptor]` (titlul de deasupra
anomaly-grid), textul se centreaza orizontal: `text-align: center`.
Toate celelalte section-marker-uri (etape, payoff, verificari) raman
aliniate stanga.

Implementare CSS: clasa modificator `.section-marker.scena-reala` cu
`text-align: center`. Nu modifica regula generala `.section-marker`.

**F-bis.V01.3 BUTON `VERIFICA ETAPA` POST-CLICK**

Comportament: dupa click pe `VERIFICĂ ETAPA N` (verde #1F7A1F, text alb
bold), textul se inlocuieste cu `✓ ETAPĂ N VALIDATĂ` (check emoji ✓ + caps
+ diacritice romane).

Stil pastrat: fond verde #1F7A1F, text alb bold, padding identic.

Click pe `ETAPĂ N VALIDATĂ` (deja validata) deschide confirmare scurta
"Anulezi validarea?" -> revine la `VERIFICĂ ETAPA N`. Persistenta in
localStorage (mecanismul 3-stari existent: NEINCEPUT/IN LUCRU/VALIDAT).

Implementare in JS din generatorul `build_cNN.py` + SABLON.

**F-bis.V01.4 GATE 2 INVERSAT V03 - ZERO CIFRE BUSINESS IN HTML/HTML-VIDEO/HTML-VIDEO-EDITABIL/FILM/PPT**

V03 INVERSEAZA Gate 2. In V01-V02 verifica paritate cross-livrabil pe
cifre afisate identic in 5 livrabile. In V03 (R-V02.15), HTML/FILM/PPT
NU mai contin cifre business - deci Gate 2 verifica TOCMAI ABSENTA lor.
V04 extinde la HTML-VIDEO. V05 extinde la HTML-VIDEO-EDITABIL.

Verificarile blocante:

1. **INPUT.xlsx + OUTPUT.xlsx** (sursa unica de adevar):
   - Suma valoare_neta calculata cu openpyxl
   - Numar randuri brute (max_row), numar randuri curate
   - Categorii anomalii (count per categorie din OUTPUT)
   - Conservare INPUT = OUTPUT (semantica per R-V02.14 daca exista
     deduplicare)
   - Aceste cifre ramaneau in Excel ca adevar fizic. NU se exporta in
     text livrabil.

2. **HTML.html, HTML-VIDEO.html, HTML-VIDEO-EDITABIL.html** - parse DOM,
   verifica ZERO cifre business:
   - Zero ocurente `[0-9]\.[0-9]{3}` (format RO mii) ca text afisat
   - Zero ocurente `[0-9]{4,}` ca text business (toleranta: ID-uri
     tehnice, numere de versiune, dimensiuni px in style inline)
   - Zero clase decorative `.wow-number`, `.pn-v`, `.pn-k`,
     `.payoff-numeric` cu continut
   - Lista albe (exceptii didactice): exemplul format `1.234.567,89`
     daca apare ca demonstratie pedagogica, ID-uri Excel, dimensiuni CSS

3. **FILM.docx** - parse XML, verifica ZERO cifre business in paragrafe
   (aceleasi reguli ca HTML).

4. **PPT.pptx** - parse XML slides + text frames, verifica ZERO cifre
   business.

NECONFORM blocant la prima cifra business detectata. Raport per livrabil
cu pozitia exacta + textul gasit + sugestia generica de inlocuire
("suma conservata" / "randuri curate" / etc).

Implementare in `verifica_cNN.py` cu pattern regex strict + lista alba
configurabila per constructie.

Motivul inversarii (R-V02.15 + lectia META V03): cifrele Excel n-au ce
cauta in HTML/FILM/PPT. Box-urile decorative care le contineau au
disparut. Daca o cifra apare, e bug de regresie sau decor accidental -
gate o prinde.

**F-bis.V01.5 GATE 3 V03 - COERENTA BRAND FILM+PPT + PARITATE EDITOR**

Gate 3 V03 acopera DOUA verificari blocante combinate:

A) **COERENTA BRAND FILM+PPT** (R-V02.3 originar V02):
   - ZERO em-dash / en-dash in FILM.docx si PPT.pptx
   - ZERO cuvinte interzise brand cu context awareness (R-V02.11)
   - Diacritice romanesti virgula, NU sedila (R-V02.2)
   - Numarul de prompturi Copilot in meta-box = count fizic .prompt-box
     in HTML (R-V02.9)

B) **PARITATE EDITOR <-> COCKPIT** (originar identificat V01):
   La fiecare generare HTML cockpit, script verifica:
   - TOATE elementele cu text vizibil (h1-h6, p, span, div, li, td, th
     cu text non-empty) au CLASA lor sau parent-ul in SEL+BLOCKS din
     EDITOR-JS.
   - Orice element editorial fara cale de editare = NECONFORM blocant.

Lista selectori editori actuali V03 (componente vii in HTML):
- `.hook-local` (hookuri pe etape)
- `.cover-label-pill` (eticheta cu numarul constructiei)
- `.phase-tag` (tag "INPUT" / "TRANSFORMARE")
- `.footer-brand` ("TRAINITY" in footer)
- `.cover-title`, `.cover-subtitle`, `.cover-microline`
- `.stage-header`, `.stage-header-quote`, `.step-title`, `.step-body`
- `.capcana-text`, `.verif-list`, `.final-content`, `.final-label`
- `.intriga-text` (caseta INTRIGA rosie cover)
- `.miza-text`, `.mantra-band`, `.motto-text`, `.wow-strip-slogan`

Selectori OBSOLETI V03 (componente eliminate prin R-V02.15, NU mai apar
in HTML, deci NU trebuie in SEL):
- `.wow-number` (cifre mari monumentale) - ELIMINAT
- `.wow-title` (titlu wow-strip cu numar) - ELIMINAT
- `.wow-sub` (subtext wow-strip cu numar) - ELIMINAT
- `.pn-v` (valori payoff numeric) - ELIMINAT
- `.pn-k` (etichete payoff numeric) - ELIMINAT
- `.data-table th` + `.data-table td` (tabele before/after cu cifre) -
  ELIMINATE

Wow-strip ramane ca BANDA GALBENA + SLOGAN UNIC (clasa noua
`.wow-strip-slogan` text fix, editabil). FARA cifre.

Categorii corect EXCLUSE (raman non-editabile):
- Butoane functionale: `.copy-btn`, `.verification-btn`, `.pdf-download-btn`,
  `.final-check-btn`, `.scroll-top-btn`, `.nav-ctrl-btn`, `.nav-next-btn`
- Simboluri: ☰ ▾ ↓ ↑
- Status dinamic: `.stage-badge` (schimba programatic)
- Script: `.book-app`
- Navigatie sidebar (editarea ar strica routing)

## F-ter. SABLON HTML TRAINITY (fisier fizic in arhiva)

Fisierul `referinte/SABLON-HTML-Trainity.html` (~91KB, derivat din HTML-ul
C03 vechi validat la filmare) este pastrat permanent in arhiva de la
`checkout brain`. Acesta este SABLONUL HTML OFICIAL TRAINITY. Rol DUBLU,
codificat definitiv:

- **Referinta ESTETICA:** tokenii F-bis sunt extrasi din el.
- **Referinta FUNCTIONALA:** cele 12 capabilitati obligatorii din PARTEA
  VII.E sunt extrase din el. Este standardul de paritate. La generarea
  oricarui HTML nou, Claude DESCHIDE acest fisier, extrage scheletul
  functional (cele 22 functii JS: loadState, saveState, toggleStage,
  toggleStep, confirmVerification, confirmFinal, copyPrompt, fallbackCopy,
  navigateStage, navigateFinal, goToNextStep, resetProgress, toggleMobileNav,
  renderStages, render, processSelection, collectTextNodesInRange,
  nodeIntersectsRange, wrapTextNodeRange, removeMark, clearHighlights,
  scrollToTopTrainity) si il PORTEAZA pe arhitectura noua (6 etape,
  INVESTIGATIE, SPEC inghetat al constructiei curente). NU se reinventeaza
  logica de la zero; se porteaza scheletul validat, se schimba doar
  CONTINUTUL (6 etape noi, SPEC constructie) si numarul de pasi/finale
  (derivat din continutul real al constructiei). Continutul/logica veche
  C03 (5 etape SCARA, audit) IGNORATE; SCHELETUL FUNCTIONAL pastrat.

REGULA DE AUR EXTINSA: HTML nou = (schelet functional C03 referinta) +
(tokeni estetici F-bis) + (continut din SPEC inghetat al constructiei).
Trei surse, zero improvizatie sub standardul C03.

## G. STARE PLACEHOLDER (constructie fara SPEC inghetat)

Daca SPEC-ul C[NN] din PARTEA VI e [Status: NEGENERAT], HTML-ul foloseste
placeholdere standard etichetate clar (ex: "[HOOK ALES - de inghetat]")
pentru fiecare element din SPEC. Structura cockpit-ului ramane completa si
replicabila; doar continutul ales lipseste pana la prima rulare. La
inghetarea SPEC-ului, placeholderele se inlocuiesc cu alegerile reale.

## NOTA DOMENIU (limita respectata)

Aceasta parte este STRICT arhitectura de sistem. Codul HTML real, layout-ul
vizual final si structura tehnica de implementare se definesc ulterior, la
pasul de implementare, NU aici. Aici: ce sectiuni, ce ordine, ce blocuri
obligatorii, ce se injecteaza unde, cum se mapeaza cele 6 etape, logica
componentelor. Container gol replicabil.

================================================================================

# PARTEA VIII - SABLON PPT (Pasul 7) [VALIDAT de Bogdan]

STATUS: VALIDAT. Structura corectata si confirmata de Bogdan.

ROL: PPT = STRAT CINEMATIC DE IMPACT, amplificatorul emotional al filmarii.
NU urmeaza cele 6 etape procedural (acela e rolul HTML-ului - procedural).
PPT urmeaza RITMUL CINEMATIC. PPT comprima: tensiunea, reveal-urile,
verificarile, wow moments, contrastul, payoff-ul. Apare rar, puternic,
memorabil. Sursa: SPEC inghetat.

DISTINCTIE ADN CRITICA: HTML = procedural (cele 6 etape complet). PPT =
impact (ritm cinematic comprimat). PPT NU reproduce: toate etapele, toti
pasii, toate explicatiile, toate verificarile. Acela e rolul HTML.

## STRUCTURA PPT (6 slide-uri tip, ritm cinematic, NU cele 6 etape)

1. COVER - constructie, treapta, hook ales, identitate vizuala dominanta.
2. TENSIUNE - problema reala, risc, contrast, miza operationala.
3. DEMONSTRATIE / INVESTIGATIE - inainte, anomalie, contradictie,
   suspiciune, elementul care produce tensiune.
4. REVEAL / CONTROL - verificare, before/after, diferenta, control numeric,
   payoff logic.
5. WOW MOMENT - moment memorabil, cinematic, simplu, foarte vizual, foarte
   comprimat.
6. CONFIRMARE FINALA - Problema, Reframe, Control, mantra finala, payoff
   Trainity.

## REGULI PPT (validate)
- 5-8 slide-uri foarte puternice, NU 20 descriptive. Cantitate mica,
  impact mare.
- Whitespace mare; UN singur mesaj dominant per slide; maximum 1 wow
  vizual; maximum 1 idee majora; foarte putin text; foarte mult contrast
  si focus.
- PPT NU reproduce toate etapele/pasii/explicatiile/verificarile (rol HTML).
- Cifre canonice identice cu SPEC/HTML/FILM/Excel.
- Foloseste DOAR elementele inghetate in SPEC, nu Top 3.
- Design: brutalist premium, accent galben, contrast, focus. NU deck
  corporatist, NU deck de curs, NU slide-uri explicative. Strat cinematic
  de impact.

================================================================================

# PARTEA IX - SABLON FILM / SCRIPT VIDEO (Pasul 8) [VALIDAT de Bogdan]

STATUS: VALIDAT. Structura corectata si confirmata de Bogdan.

ROL: FILM = PROCEDURAL CINEMATIC. Stratul de ritm, tensiune, demonstratie,
pacing, energie, interventie umana. NU "citirea HTML-ului cu voce". NU "PPT
animat". Operator care conduce spectatorul prin sistem. Sursa: SPEC inghetat.

IDENTITATEA CELOR 3 LIVRABILE (ADN, codificat definitiv):
- HTML = procedural complet (cele 6 etape, integral).
- PPT = impact comprimat (ritm cinematic, NU cele 6 etape).
- FILM = procedural cinematic (cele 6 etape, DAR cu ritm cinematic
  HOOK->DEMO->CONTROL->REVEAL in interiorul fiecarei etape).

## STRUCTURA SCRIPT FILM (cele 6 etape; 8 componente per etapa)

- COVER / SETUP FILMARE - cadru de deschidere, hook ales rostit, tonul.
- Pentru FIECARE din cele 6 etape (REALITATE, INVESTIGATIE, TRANSFORMARE,
  VERIFICARE, STABILIZARE, CONFIRMARE), scriptul contine explicit, in
  ordine, cele 8 componente (in interiorul lor traieste ritmul cinematic
  HOOK->DEMO->CONTROL->REVEAL):
  1. OBIECTIVUL ETAPEI - ce incercam sa demonstram.
  2. STAREA EMOTIONALA - tensiune / suspiciune / claritate / control /
     payoff (dupa etapa).
  3. VOCEA TRAINERULUI - calm / alert / forensic / executiv / accelerat
     (registrul vocal al etapei).
  4. DEMONSTRATIA - ce vede utilizatorul efectiv pe ecran.
  5. INTERVENTIA AI - unde investigheaza, explica, accelereaza, genereaza,
     valideaza (INVESTIGATIE inainte de TRANSFORMARE respectata in voce).
  6. MOMENTUL DE CONTROL - verificare numerica / confirmare logica /
     before-after / contradictie / risc / payoff.
  7. REVEAL - concluzia locala a etapei.
  8. TRANZITIA - de ce mergem in etapa urmatoare.
- INCHIDERE - Identitate finala rostita (Problema/Reframe/Control din SPEC).

## REGULI FILM (validate)
- FILM controleaza: energia, ritmul, pauzele, reveal-urile, tacerile,
  accelerarile. Acestea sunt parte din script, nu optionale.
- Mai putin text, mai multa intentie si ritm. Replici SCURTE: hook-uri,
  payoff-uri, tensiune, control, claritate. NU paragrafe lungi de
  voice-over. NU script explicativ. Ghid cinematic procedural.
- Narativ, nu tutorial: NU enumera pasi Excel ca in 2015.
- INVESTIGATIE inainte de TRANSFORMARE respectata in voce: trainerul
  investigheaza asistat de AI, nu "scrie prompt si arata magie".
- Cifre canonice identice cu SPEC/HTML/PPT/Excel.
- Doar elementele inghetate in SPEC, nu Top 3.
- [CONTEXT INSUFICIENT]: durata tinta per film, nivel de detaliu al
  indicatiilor de voce (cuvant cu cuvant vs ghidaj) - de decis la Pasul 4
  sau prima rulare.

================================================================================

# PARTEA X - SABLON INPUT/OUTPUT EXCEL (Pasul 9) [VALIDAT de Bogdan]

STATUS: VALIDAT. Structura corectata si confirmata de Bogdan.

ROL (ADN): Excel INPUT/OUTPUT NU este "fisier suport" sau anexa. Este SCENA
REALA a constructiei: sursa tensiunii, dovada transformarii, terenul pe care
se intampla tot sistemul. Excel = REALITATEA OPERATIONALA. Feeling de
business real, NU exercitiu scolar Excel. Sursa: SPEC inghetat.

## STRUCTURA INPUT.xlsx (validata)
1. DATE_BRUTE - realitate operationala: zgomot, riscuri, anomalii,
   inconsistente. Exact contextul care produce tensiunea constructiei.
2. NOMENCLATOARE - ALL CAPS, separate clar, curate, tratate ca sursa
   oficiala de adevar.
3. REGULI / REFERINTE (optional, unde constructia cere) - praguri,
   clasificari, mapping, reguli business, exceptii controlate.
4. ANOMALII PLANTATE - NU "exercitii de curs". Erori REALE de business:
   subtile, credibile, periculoase, uneori chiar valide tehnic. Acesta e
   ADN-ul Trainity. INPUT = realitatea, contine problema, nu solutia.

## STRUCTURA OUTPUT.xlsx (validata)
1. DATE_MATURIZATE - NU "date curate", ci date CONTROLABILE OPERATIONAL.
2. MARCAJE / DECIZII / STATUS - aici se vede ce a fost separat, validat,
   ce cere decizie, ce a fost investigat, ce a fost stabilizat.
3. CONTROL_FINAL - zona STANDARDIZATA (ritual Trainity): suma control,
   totaluri, before/after, verificari canonice, confirmari, semnale de
   integritate. Aceeasi zona, mereu, la fiecare constructie.
4. TRASABILITATE - OUTPUT pastreaza trasabilitate, continuitate, dovada
   transformarii. NU "fisier nou magic": se vede CLAR ce s-a maturizat.

## REGULI EXCEL (validate)
- INPUT si OUTPUT spun ACEEASI poveste numerica, cu nivel diferit de
  control. Cifre canonice identice in INPUT, OUTPUT si toate livrabilele;
  zero divergenta; suma de control conservata conform SPEC.
- FEELING DE BUSINESS REAL: denumiri credibile, distributii credibile,
  zgomot realist, pattern-uri reale, riscuri reale, valori imperfecte. NU
  dataset artificial, NU exercitiu scolar.
- ANOMALIILE: declarate in SPEC, exacte numeric, verificabile,
  reproductibile (numarul real pe date = numarul declarat). NU anomalii
  inventate haotic.
- Continuitate INPUT->OUTPUT doar in interiorul constructiei. Zero
  mostenire intre constructii (date proaspete proprii).
- Formatare romana (data DD.MM.YYYY, virgula decimala).
- [CONTEXT INSUFICIENT]: numarul de coloane/randuri standard si structura
  exacta a foilor per tip de constructie - variaza pe treapta (T1
  structura vs T3 model); de detaliat la Pasul 4 per constructie.

## NOTA DOMENIU (toate cele 3 sabloane)
Propuneri de structura de sistem. Cod, formule reale, layout vizual final,
continut C01-C20 - NU aici, ci la implementare/Pasul 4. Bogdan valideaza
fiecare bloc; ce nu e validat ramane PROPUNERE, nu regula.

================================================================================

# PARTEA XI - MOTORUL DE GENERARE (motor minimal, 5 comenzi)

Motor MINIMAL (decizia Bogdan: optiunea B). Fluxul esential de productie.
Verificarea e minimala (NU cele 7 gate-uri stratificate vechi); stratul de
blindaj complet se adauga deliberat ulterior, ca strat asumat, nu reactiv.
Pasul 4 (definirea constructiei) este ABSORBIT in motor: definire
just-in-time per constructie la prima rulare (decizia Bogdan: optiunea A).

## COMENZILE MOTORULUI

Doua comenzi de PORNIRE (prima comanda intr-un chat nou, dupa atasarea
arhivei ZIP de la `checkout brain`):

### `CHECKIN BRAIN`
Chat nou de CONTINUARE GENERALA. Bogdan ataseaza arhiva ZIP si da
`CHECKIN BRAIN`. Claude: extrage arhiva, citeste INTEGRAL brain.md +
SISTEM_TRAINITY.md, intra in context maxim, confirma pe scurt stadiul
(ce e gata, ce urmeaza). Nu porneste o constructie anume - continua de
unde s-a ramas conform brain.md.

Livrabilele existente in arhiva (livrabile_C[NN]/) sunt disponibile ca
referinta: cele 5 canonice (INPUT/OUTPUT/HTML/FILM/PPT) + editabilul daca
exista (`HTML-EDITABIL-Excel-NN-Nume.html`). Claude le citeste daca sunt
relevante pentru sarcina curenta. Editabilul nu se regenereaza la checkin
- daca trebuie reactualizat, Bogdan da explicit `Genereaza HTML-EDITABIL`.

### `CHECKIN CONSTRUCTIE NN`
Chat nou DEDICAT constructiei NN. UNICA comanda de pornire pentru
generarea unei constructii (inlocuieste vechiul `Genereaza CONSTRUCTIA
NN` ca punct de intrare). Bogdan ataseaza arhiva ZIP si da
`CHECKIN CONSTRUCTIE NN`. Claude face TOT, in ordine:
A. Extrage arhiva, citeste brain.md + SISTEM_TRAINITY.md (context).
B. Apoi ruleaza motorul de generare pentru constructia NN:
1. Citeste SPEC C[NN] din PARTEA VI.
2. Daca [Status: NEGENERAT]: defineste constructia just-in-time pe sablonul
   de 15 blocuri (PARTEA V). Pentru blocurile Top 3 (descrieri, hook-uri,
   mantre, emotii, mize, rezultate, wow) Claude propune 3 variante, Bogdan
   alege 1. Pentru C01-C08 materialul vine din documentele oficiale; pentru
   C09-C20 Claude semnaleaza explicit fiecare bloc fara context si cere
   decizia Bogdan (NU inventeaza identitate/hook/mize). Dupa confirmarea de
   ansamblu, Claude INGHEATA alegerile in SPEC C[NN] (Status: INGHETAT).
3. Daca [Status: INGHETAT]: aplica direct, ZERO re-intrebari.
4. Produce cele **8 livrabile** [V05 prin R-V03.2 + R-V03.3 + R-V03.4] pe
   sabloanele validate, respectand identitatea:
   - HTML-STUDY.html = procedural complet pentru cursant (6 etape, PARTEA
     VII + standard estetic F-bis). PARITATE FUNCTIONALA OBLIGATORIE: toate
     cele 12 capabilitati din PARTEA VII.E. Referinta de standard =
     `referinte/SABLON-HTML-Trainity.html`. ZERO cifre business (R-V02.15).
     **Voce narativa: persoana a 2-a singular (R-V03.4)**.
   - HTML-EDIT-STUDY.html = HTML-STUDY complet + strat WYSIWYG editor
     universal. **AUTOMAT** [V01], nu mai la cerere. Test Playwright 5
     viewporturi blocant. **Voce narativa mostenita: persoana a 2-a
     singular**. Storage: `trainity_cNN_study_edits_v1`.
   - HTML-VIDEO.html = broadcast mode pentru filmare (R-V03.1, 7 ecrane
     scenice, butoane prev/next fixe bottom, panel dreapta cu lista etape
     clickabila + buton pas sarit). ZERO cifre business. Pilot validat
     C01. **Voce narativa: persoana a 3-a plural (R-V03.4)**. Exceptii:
     prompt text Copilot (persoana 2 catre AI), butoane UI Validează,
     toast feedback sistem, motto-uri fixe.
   - HTML-EDIT-VIDEO.html = HTML-VIDEO + strat WYSIWYG editor universal
     (R-V03.3). **AUTOMAT**. Acelasi pattern editor ca HTML-EDIT-STUDY,
     injectat peste matrita video. **Voce narativa mostenita: persoana a
     3-a plural**. Storage: `trainity_cNN_video_edits_v1` +
     `trainity_cNN_video_deleted_v1`.
   - PPT.pptx = impact comprimat (PARTEA VIII, 6 slide-uri ritm cinematic).
     ZERO cifre business (R-V02.15).
   - FILM.docx = procedural cinematic (PARTEA IX, 6 etape x 8 componente).
     ZERO cifre business (R-V02.15).
   - INPUT.xlsx + OUTPUT.xlsx = scena reala (PARTEA X, DATE_BRUTE ..
     CONTROL_FINAL, anomalii din SPEC). UNICA SURSA FIZICA DE CIFRE.
5. Cifrele traiesc EXCLUSIV in INPUT.xlsx + OUTPUT.xlsx (R-V02.15). Zero
   continuitate intre constructii. Vocabular ADN. 0 em-dash/en-dash.
   Voce narativa per livrabil: R-V03.4.

**R-V01.2 LIVRARE TOATE ODATA (regula permanenta) [V04 EXTINS LA 8
LIVRABILE prin R-V03.2 + R-V03.3]:** cele 8 livrabile + gate-uri se livreaza
intr-un singur `present_files` la finalul chatului. Niciodata pe rand.
Niciodata cu intrebare prealabila despre ordine sau mod de livrare. Singura
intrebare permisa in chatul de constructie = grilele de inghetare SPEC (cand
NEGENERAT). Restul = executie curata.

### `Verifica CONSTRUCTIA NN` (in interiorul chatului)
Verificare MINIMALA (NU cele 7 gate-uri vechi). Verifica esentialul:
- Cele 8 livrabile exista (8/8).
- SPEC C[NN] respectat (hook/mantra/etc. inghetate = cele din livrabile).
- Cifrele traiesc EXCLUSIV in INPUT.xlsx + OUTPUT.xlsx (R-V02.15). Gate 2
  INVERSAT verifica ABSENTA cifrelor business in HTML / HTML-VIDEO /
  HTML-EDIT-VIDEO / FILM / PPT.
- Anomaliile din SPEC prezente si numeric corecte in Excel.
- 0 em-dash/en-dash, 0 cuvinte interzise (vocabular ADN).
- Identitatea livrabilelor respectata (HTML cockpit procedural / HTML-VIDEO
  broadcast scenic / PPT impact / FILM procedural cinematic / Excel scena
  reala; editabilele = strat WYSIWYG injectat peste sursa).
- **GATE PARITATE FUNCTIONALA HTML (obligatoriu, blocant).** HTML-ul are
  TOATE cele 12 capabilitati din PARTEA VII.E, verificate functional, nu
  doar prezente in cod:
  1. localStorage loadState/saveState (cheie unica; reload pastreaza tot).
  2. step-check granulari (mai multi pasi per etapa, toggle real persistat).
  3. zona verificari finale separata (final-check-btn, toggle persistat).
  4. stage-toggle colapsare/expandare (activeStage persistat).
  5. contor dublu in progres ("X / N pasi" + "Y / M finale").
  6. bara progres per etapa (data-stage-progress, se umple din pasii etapei).
  7. floating-next inteligent (primul pas nebifat + highlight, nu scroll orb).
  8. highlight text persistent (mark.persist, click sterge, buton clear).
  9. resetProgress (cu confirm, sterge tot, persista).
  10. navigatie mobila reala (hamburger + overlay + slide, nu display:none).
  11. render dinamic sidebar (nav-item active/done din state).
  12. copyPrompt cu fallback (clipboard API + textarea fallback; buton
      OBLIGATORIU galben #FFD400 fundal + negru, fiecare instanta).
  PROBA: numara functiile JS si capabilitatile; compara cu standardul C03
  vechi (referinta). Daca lipseste ORICARE din cele 12, sau e doar
  decorativa (fara state/persistenta/efect real), HTML = RESPINS, se
  regenereaza. Test EFECT nu prezenta: click programatic + verificare
  schimbare stare/clasa/text + update contor + persistenta dupa reload.

- **GATE COERENTA CROSS-LIVRABIL (obligatoriu, blocant).** HTML-ul si
  fisierele Excel TREBUIE sa fie coerente cap-coada. Fiecare afirmatie
  numerica din HTML se confirma fizic in INPUT.xlsx si OUTPUT.xlsx.
  Nu poate HTML-ul sa spuna "54 blank" daca Excel are 53. Nu poate sa
  spuna "62 ambalaj" daca calculul (antet + subtot + total + blank) e 61.
  Verifica EFECT, nu doar prezenta textuala:
  
  INPUT.xlsx - se verifica fizic:
  - max_row = cifra "total randuri" mentionata in HTML
  - max_col = cifra "coloane fizice" (vizibile + ascunse) din HTML
  - column_dimensions hidden = numarul de coloane ascunse afirmat
  - antet real pe randul cu numarul mentionat in HTML
  - numar randuri SUBTOTAL = cifra HTML
  - numar randuri TOTAL GENERAL = cifra HTML
  - numar randuri BLANK FALS = cifra HTML
  - ambalaj total (suma componentelor) = cifra HTML
  - suma valoare_neta (sau coloana cheie) = SUMA canonica din SPEC
  
  OUTPUT.xlsx - se verifica fizic:
  - max_row = 1 (antet) + numarul de tranzactii afirmat in HTML
  - max_col = numarul de coloane utile afirmat in HTML
  - antet pe randul 1 (curatat)
  - 0 randuri blank
  - 0 randuri SUBTOTAL/TOTAL
  - suma valoare_neta = SUMA canonica (CONSERVATA din INPUT, neschimbata)
  - NU contine coloanele ascunse declarate ca "eliminate"
  - contine Excel Table cu numele canonic (ex. Vanzari_Curat)
  
  Daca ORICE cifra din HTML nu se confirma fizic in Excel, gate-ul =
  NECONFORM. HTML sau Excel se aliniaza pana la coerenta. Niciodata se
  raporteaza ca "CONFORM" daca exista o singura discrepanta numerica.
  
  Lectie sursa (C01, mai 2026): primul gate cross-livrabil rulat a prins
  o discrepanta reala: HTML zicea "54 blank / 62 ambalaj" dar Excel avea
  53 blank / 61 ambalaj (din 3+4+1+53). Discrepanta era invizibila pentru
  gate-ul de paritate functionala HTML, fiindca acolo "62" e doar text
  prezent. Coerenta cap-coada e gate distinct OBLIGATORIU.

Raport scurt: CONFORM / lista abateri pentru AMBELE gate-uri. Blindajul
complet (gate-uri + proba numerica stratificata) se adauga ulterior,
deliberat, NU acum.

### `Genereaza HTML-EDITABIL` (in interiorul chatului)
Comanda de **REGENERARE PUNCTUALA** [V01] a editabilului, cand SPEC e
deja inghetat si vrei doar refresh editabil (de exemplu dupa o modificare
la HTML cockpit). Acelasi standard estetic F-bis, structura PARTEA VII.

**LIFECYCLE EDITABIL V01 (regula permanenta, SCHIMBATA):**

1. **Generare = AUTOMATA in CHECKIN CONSTRUCTIE NN.** Editabilele se
   genereaza AUTOMAT ca parte din `CHECKIN CONSTRUCTIE NN`. Cele 8 livrabile
   [V05] includ HTML-EDIT-STUDY si HTML-EDIT-VIDEO ca standard, nu ca
   optionale. Motivatie: ambele editabile sunt necesare de fiecare data
   pentru ajustari pre-filmare (cockpit pentru recapitulare, broadcast
   pentru filmare propriu-zisa), asadar livrabile canonice.

2. **Regenerare punctuala = LA CERERE EXPLICITA prin `Genereaza
   HTML-EDIT-STUDY` (study) sau `Genereaza HTML-EDIT-VIDEO` (video).**
   Comenzi pastrate pentru cazul cand HTML-STUDY / HTML-VIDEO sursa s-a
   modificat si editabilul trebuie reactualizat fara a regenera intreaga
   constructie.

3. **Persistenta in arhiva.** La `checkout brain`, ambele editabile intra
   OBLIGATORIU in arhiva ZIP (existand prin V05 ca livrabile canonice).

4. **Disponibilitate la CHECKIN.** Editabilele din arhiva sunt disponibile
   ca referinta in context, alaturi de celelalte 6 livrabile canonice.

CONVENTIE DE NUME (regula permanenta): fisierul editabil incepe
OBLIGATORIU cu "HTML". Format exact: `HTML-EDITABIL-Excel-NN-Nume.html`.
NU "BOOK-...", NU "HTML-Excel-NN-Nume-EDITABIL.html", NU alt prefix.
"BOOK" nu apare niciodata in output. Editabilul = cockpit-ul complet
(toate cele 12 capabilitati, neatins) + strat WYSIWYG de editare (toggle
contenteditable, buton sterge element/bloc, undo/redo, salvare localStorage
cheie izolata, restaurare, export HTML curat, export PDF prin print
browser). Stratul de editare e generic, atasat prin selectori CSS
(SEL/BLOCKS) la clasele sistemului; la fiecare constructie SEL/BLOCKS se
aliniaza la clasele HTML-ului curent. Export PDF prin window.print NU
incalca ZERO PDF (e print al utilizatorului, nu export DOCX->PDF al lui
Claude).

**Bara editor SUPREMA (regula vizuala, lectie C01 mai 2026):** stratul de
editare (#tr-bar) e sticky sus cu z-index 999999, deasupra TUTUROR
elementelor documentului. Body primeste padding-top: 50px MEREU (nu doar
la editing) ca sa lase loc barii. Sidebar (.side-nav), butonul PDF
(.pdf-download-btn), hamburger (.mobile-nav-toggle) primesc top: 50/58px
cand bara e prezenta. Cand utilizatorul apasa "Ascunde", body primeste
clasa `tr-hide-bar` care reseteaza padding-ul si pozitiile la originale.

### `checkout brain` (UNICA comanda de iesire, motor perpetuu)
Inlocuieste complet `checkout chat`. La aceasta comanda Claude produce O
SINGURA arhiva ZIP care contine TOT ce ii trebuie chatului urmator:
1. **brain.md** - contextul curent COMPLET in detaliu.
2. **SISTEM_TRAINITY.md** - sursa unica de adevar (cu SPEC-urile la zi).
3. **Toate fisierele sistem si livrabilele**. Include OBLIGATORIU cele
   8 livrabile [V05] (INPUT/OUTPUT/HTML/HTML-EDITABIL/HTML-VIDEO/
   HTML-VIDEO-EDITABIL/FILM/PPT).
4. **PROMPT_CHAT_NOU.txt** - promptul exact pe care Bogdan il da in
   chatul nou.

**R-V01.1 NUMIRE ARHIVA (regula permanenta):** numele arhivei =
`OUT-VNN.zip` (NN incremental, 2 cifre, zero-padded). V01, V02,
V03... Format vechi (`CHECKOUT_BRAIN_TRAINITY_DATE.zip`) abandonat.

Toate intr-un SINGUR fisier ZIP. PERPETUU: regula `checkout brain` traieste
in SISTEM_TRAINITY.md, care intra in ZIP, care se deschide in chatul nou,
care are din nou comanda `checkout brain`. OBLIGATORIU la finalul fiecarui
chat BRAIN - fara el, starea se pierde.

### `scurt checkout` (in chat CONSTRUCTIE, alternativa la checkout brain) [V01]

Comanda dedicata pentru chatul CHECKIN CONSTRUCTIE NN. Cand Bogdan vrea sa
ia DOAR cele 8 livrabile fara a regenera arhiva ZIP completa cu sistemul:

Claude livreaza ca text in chat:
1. **SPEC C[NN] inghetat** ca text intr-un singur paragraf (alegerile
   facute prin grile: INTRIGA / MIZA / MANTRA / WOW / MOTTO + fenomene
   + cifre canonice + identitate finala).
2. **Lectii noi din chat** (daca exista) intr-un al doilea paragraf
   (cazuri ce ar trebui adresate ca regula/gate nou in sistem).

Bogdan le copiaza in chat CHECKIN BRAIN urmator. Captureaza 90% din
valoarea checkout-ului fara overheadul arhivei complete.

Util cand lucrezi rapid in paralel si vrei doar livrabilele fara sa
amani timpul cu regenerarea sistemului.

### WORKFLOW PARALEL + MERGE SPEC [V01]

**R-V01.5:** chat-urile `CHECKIN CONSTRUCTIE NN` ruleaza simultan
(C02, C03, C04...). Bogdan se uita la rezultate, detecteaza probleme,
le aduce in chatul `CHECKIN BRAIN`. Aici se consolideaza regula/gate.
`checkout brain` produce sistemul nou. Sistemul nou se foloseste la
chat-uri CONSTRUCTIE viitoare.

Implicatie: chat-urile CONSTRUCTIE in paralel pot folosi versiuni
diferite de sistem (C02 a inceput cu V01, C03 a inceput cu V02 dupa o
consolidare BRAIN). Asta e acceptat - sistemul se imbunatateste continuu,
constructiile vechi raman valide cu sistemul lor de pornire.

**Merge SPEC-uri (necontroversat):** SPEC-urile inghetate ale fiecarei
constructii se compileaza in PARTEA VI a SISTEM_TRAINITY.md, sectiuni
distincte. Conflicte de SPEC nu exista (fiecare CNN are sectiunea lui).

**Merge livrabile + generatoare:** livrabilele si generatoarele se
copiaza in arhiva noua (livrabile_CNN/, generatoare/build_cNN.py etc.).

**Merge lectii brain.md (potential conflictual):** Claude compara
lectiile noi din fiecare brain.md cu sistemul curent. Conflicte raportate
inainte sa decida:
- Doua chat-uri au aplicat aceeasi regula diferit
- O lectie dintr-un chat contrazice o regula consolidata
- Numerotare lectii brain.md continua
Decizia Bogdan pentru fiecare conflict, nu Claude inventeaza autonom.

**Bonus check Gate 2 retrospectiv:** cifrele canonice din fiecare SPEC
sunt unice si nu se ciocnesc (M-1 din SISTEM: nicio cifra/metrica nu se
repeta intre constructii).

Output merge: arhiva `OUT-VNN.zip` (NN = next incremental) cu sistem
consolidat + raport scurt: "C02, C03, C04 inghetate. X lectii noi
adaugate. Y conflicte rezolvate prin decizia ta."

## REGULI MOTOR

**G-06 FILTRUL SIGUR/CONFLICT PENTRU FEEDBACK EXTERN (regula permanenta,
toate chat-urile, AUTOMATA, NU se cere confirmare):**

Orice feedback extern (alt model AI, ChatGPT, terti, documente de
recomandare, sugestii din afara) este AUTOMAT clasificat prin Filtrul
Sigur/Conflict. Claude NU intreaba niciodata pe Bogdan "cum procedez cu
feedbackul" si NU paseaza decizia inapoi. Bogdan e arhitectul; clasificarea
argumentata e obligatia lui Claude. Procedura fixa:

1. **SIGUR** = aliniat cu ADN-ul Trainity, cu sablonul de aur
   (referinta functionala/estetica), cu SPEC-ul inghetat si cu sistemul.
   Include si corectarea erorilor reale semnalate de feedback. Se APLICA
   direct, fara intrebare.
2. **CONFLICT** = rupe ADN-ul (vocabular interzis, ZERO PDF, anti-clutter,
   identitatea livrabilelor), abate de la sablonul de aur / cele 22 functii
   / cele 12 capabilitati, contrazice SPEC-ul inghetat sau cifrele canonice,
   sau introduce elemente decorative/dashboard fake/hype. Se RESPINGE cu
   argument explicit documentat in raspuns.
3. **NEUTRU** = deja implementat sau fara efect. Se noteaza scurt.

Claude livreaza clasificarea (SIGUR/CONFLICT/NEUTRU, punct cu punct, cu
argument pentru fiecare CONFLICT), apoi EXECUTA direct: aplica tot ce e
SIGUR, respinge tot ce e CONFLICT. Fara grila de confirmare, fara
"confirmi sa procedez". Singura interventie a lui Bogdan e ulterioara si
optionala: daca nu e de acord cu o clasificare, o spune explicit si Claude
reanalizeaza acel punct. Implicit insa, totul curge automat prin filtru.

Exceptie unica: daca feedbackul atinge o decizie deschisa fara varianta
discreta evidenta (ex. o cifra canonica nevalidata), Claude marcheaza
explicit ca [PROPUNERE de validat], nu o aplica tacit ca adevar.

Se propaga prin checkin in toate chat-urile (BRAIN si CONSTRUCTIE).

---

**SEPARARE STRICTA A CELOR DOUA TIPURI DE CHAT (regula de comportament):**

- Chat `CHECKIN BRAIN` = chat de SISTEM / ARHITECTURA / CONSOLIDARE. Aici
  se discuta sistemul, se adauga reguli si gate-uri, se consolideaza
  arhitectura, se iau decizii. INTERZIS sa genereze livrabile de
  constructie aici.

- Chat `CHECKIN CONSTRUCTIE NN` = chat de PRODUCTIE PURA. Genereaza DOAR
  constructia NN (livrabilele) pe sistemul existent. INTERZIS sa modifice
  sistemul/regulile/arhitectura. NU discuta despre sistem. NU se
  auto-evalueaza pentru erori de sistem si NU intrerupe ca sa trimita
  Bogdan la BRAIN. Executie curata: produce livrabilele, atat. Fara
  meta-comentarii de tip "asta ar trebui reparat in sistem".

- ERORILE LE RAPORTEAZA BOGDAN. Claude in chatul de constructie NU judeca
  daca o eroare e "de sistem" si NU redirectioneaza. Bogdan se uita la
  rezultat, Bogdan detecteaza eroarea, Bogdan decide consolidarea.

- BUCLA DE EROARE: Bogdan detecteaza o problema -> Bogdan revine in ultimul
  chat `CHECKIN BRAIN` -> consolideaza sistemul acolo (adauga regula/gate
  care prinde eroarea) -> `checkout brain` -> reia constructia intr-un chat
  `CHECKIN CONSTRUCTIE NN` nou cu sistemul imbunatatit. Sistemul se schimba
  DOAR in BRAIN; constructiile se produc DOAR in CONSTRUCTIE. Erorile
  devin combustibil pentru consolidarea sistemului, nu petice ad-hoc.

- Un chat incepe prin a atasa arhiva ZIP + a da fie `CHECKIN BRAIN`, fie
  `CHECKIN CONSTRUCTIE NN`. Se incheie OBLIGATORIU cu `checkout brain`
  (produce arhiva ZIP unica perpetua). Promptul din ZIP
  (PROMPT_CHAT_NOU.txt) ramane plasa de siguranta daca un chat nou nu
  prinde comanda direct.
- SPEC-ul inghetat este sursa de adevar; modificare doar la cerere
  explicita Bogdan.
- Mecanica completa a comenzilor (format arhiva, continut exact checkout,
  blindaj verificare) se detaliaza ca pas dedicat ulterior - aici doar
  principiul de functionare (motor minimal).
- Pasul 4 NU mai e pas separat (absorbit in `Genereaza CONSTRUCTIA NN`).
  Raman: Pasul 10 (prompturi finale productie), refacerea Catalogului
  (dupa ce primele constructii sunt definite prin motor).

---

## REGULI NOI V15 (25 mai 2026, dupa audit C03)

**R-V03.38 PROMPTURI BANANA 2 = ASSET PERPETUU IN BRAIN [V15]:**
Folder `creative_banana2/` in brain este EXCEPTIE controlata la
R-V03.37 (brain lightweight). Contine Creativ-Excel-NN-*.txt per
constructie ca asset arhitectural perpetuu. La CHECKIN CONSTRUCTIE
NN: primul pas dupa citirea kit-ului = verificare existenta in
arhiva. Daca exista, SE FOLOSESC ca atare. Daca lipseste, motorul
genereaza nou si livreaza pentru consolidare la urmatorul checkout
brain. Marime totala maxima ~500 KB (25 KB x 20 constructii),
insignifianta vs ~5 MB brain total.

**R-V03.39 POST-FLIGHT GATE CROSS-CONTAMINATION (BLOCANT) [V15]:**
Inainte de `present_files` la `Genereaza CONSTRUCTIA NN`, motorul
ruleaza automat `generatoare/gate_cross_contamination.py`. Daca
oricare verificare picătură, livrabilul NU iese din chat, se cere
regenerare. Verifica 6 dimensiuni: (1) niciun cod CXX vizibil
!= CNN curent in text HTML, (2) cover-label exact "CONSTRUCȚIA
C{NN}" si cover-title contine nume_hero_caps, (3) meta-val toate
CAPS R-V03.43, (4) niciun cuvant englez forbidden (Normalize,
Tutorial, Lesson, Quiz, Module, Course, Webinar, Masterclass),
(5) localStorage keys = trainity_c{NN}_*, (6) similarity step-titles
cu pilot C01 V12 < 30% daca CNN != C01 (R-V03.41).

Acest gate ar fi prins eroarea C03 din V14 (17/18 step-titles
identice cu pilot, 4 violatii cover-label, "Normalize" engleza).

**R-V03.40 BLOC IDENTITATE_TEHNICA PER CONSTRUCTIE [V15]:**
Document `referinte/IDENTITATE-TEHNICA.md` cu bloc explicit per
C01-C20. Generatorul citeste DIRECT, nu interpreteaza. Contine 20
campuri obligatorii: cod, treapta_nr, treapta_nume, treapta_pozitie,
nume_hero_caps (rand1, rand2, combinat), nume_title_case, nume_slug,
input_filename, output_filename, creativ_filename, meta_val_treapta
cu bold corect, next_cod, next_nume_title, next_label, footer_text,
topbar_text, mobile_topbar, nav_brand_label, nav_brand_title,
title_studiu, title_video, localStorage_studiu, localStorage_video.
Daca un camp lipseste, motorul OPRESTE generarea cu eroare
explicita, NU continua cu approximare.

C01-C04 sunt complete in V15. C05-C20 completate la inghetarea
SPEC T2-T5.

**R-V03.41 SIMILARITY CHECK STEP-TITLES CU PILOT C01 V12 [V15]:**
Pentru constructie CNN unde NN != C01, step-titles in HTML-Studiu
si HTML-Video NU pot avea >= 30% identitate cu pilotul C01 V12.
Threshold derivat empiric din audit C03: 17/18 step-titles
identice (94%) = COMPLET INACCEPTABIL. Verificarea ruleaza in
cadrul R-V03.39 si semnaleaza ALERTA CLONA PASIVA cu numarul
exact de step-titles identice. Sub 30% = constructia e regenerata
onest. Peste 30% = constructia e clona pasiva, blocata la livrare.

**R-V03.42 CHECKLIST EXPLICIT COVER-HEADER [V15]:**
Document `referinte/COVER-CHECKLIST.md` cu lista de 20 puncte
atomice care SE SCHIMBA obligatoriu la COPY-MODIFY pe pilot C01
V12. Acopera: cover-label, cover-title rand1+rand2, cover-subtitle,
cover-miza, meta-val TREAPTA cu bold corect, meta-val CONSTRUCTIE,
INPUT filename link, OUTPUT filename link, AI INTEGRAT descriere,
next-label, next-title, next-desc, footer, nav-brand-label,
nav-brand-title, mobile-topbar, <title> pagina, topbar-brand,
localStorage_studiu, localStorage_video. Folosit ca ghid prescriptiv
in chat CHECKIN CONSTRUCTIE NN.

**R-V03.43 CAPITALIZARE META-VAL TREAPTA = TOATE CAPS [V15]:**
Decizie ARHITECT Bogdan in V15. Format final inghetat universal:
- C01: `<b>STRUCTURA</b> · CONTROL · AUDIT · NORMALIZARE (SCAN)`
- C02: `STRUCTURA · <b>CONTROL</b> · AUDIT · NORMALIZARE (SCAN)`
- C03: `STRUCTURA · CONTROL · <b>AUDIT</b> · NORMALIZARE (SCAN)`
- C04: `STRUCTURA · CONTROL · AUDIT · <b>NORMALIZARE</b> (SCAN)`

Pentru T2-T5 lista de treapta se schimba per IDENTITATE_TEHNICA.
Aplicat retroactiv pe pilot C01 V12 + livrabile_C01 in V15.

---

## NOTA SPECIALA C03 V14

HTML-Studiu si HTML-Editor-Studiu C03 din arhiva
OUT-03-V14-20260525_125341.zip sunt INVALIDATE
in V15 dupa audit exhaustiv. Erori descoperite:
- 17/18 step-titles identice cu pilot C01 V12 (CLONA PASIVA)
- 8/8 final-labels identice cu pilot C01 V12
- 2/2 prompturi text identice cu pilot C01 (limbaj C01 "exportul ERP",
  "Power Query", "SUM vs AGGREGATE")
- cover-label "CONSTRUCȚIA C01" in loc de "CONSTRUCȚIA C03"
- bold pe STRUCTURA in cover-meta-val in loc de Audit (treapta curenta)
- "Normalize" engleza in cover-meta-val

HTML-Video, HTML-Editor-Video, Date-Input.xlsx, Date-Output.xlsx,
Creativ-Excel-03-Auditare.txt din aceeasi arhiva sunt VALIDE si
PASTRATE.

Regenerarea HTML-Studiu + HTML-Editor-Studiu C03 se va face intr-un
chat CHECKIN CONSTRUCTIE 03 NOU, cu noile reguli V15 active si
gate-ul R-V03.39 verificand livrarea.

---

## REGULI NOI V16 (25 mai 2026, dupa audit C02+C03+C04 V15)

## REGULI NOI V19 (25 mai 2026, schimbare arhitecturala majora dupa V18)

**R-V03.49 DATE_MASTER-INITIAL ASSET CANONIC + CONSTRUCTII INDEPENDENTE [V19]:**

Schimbare arhitecturala MAJORA care inverseaza decizia V18:

**Decizia V18 (deprecat V19):** Date_MASTER progresiv cap-coada - C05
depindea de Date_MASTER-dupa-C04, care depindea de C03, etc.

**Problema V18:** sistemul devenea secvential obligatoriu. C05 nu putea
fi generat fara sa termine C04. Chat-urile CONSTRUCTIE paralele
imposibile. Asta contrazicea R-V01.5 care explicit cerea chat-uri
paralele.

**Decizia V19:** un singur `Date_MASTER-initial.xlsx` ca asset
perpetuu inghetat in arhiva (`referinte/Date_MASTER-initial.xlsx`).
Toate constructiile C01-C08 pleaca de la acest fisier identic, aplica
modificari specifice SPEC C{NN}, livreaza `Date_MASTER-C{NN}.xlsx`.

Constructiile sunt **INDEPENDENTE**. C05 NU dependa de C04. C03 NU
dependa de C02. Fiecare poate fi generata in chat propriu paralel.

**Continut Date_MASTER-initial:**
- 2000 facturi sintetice pe 12 luni (iun 2025 - mai 2026)
- Schema canonica 14 coloane sheet Vanzari (R-V03.47 pastrat)
- Sheets auxiliare: CLIENTI (15), PRODUSE (13), AGENTI (6), DEPOZITE (5)
- Pattern sezonier realist (varf nov-dec, valle iul-aug)
- Suma valoare_neta ~7,986,000 lei
- Date sintetice generate determinist (seed=42)
- Nume firmelor fictive (SC AROMET TRADING SRL, SC DACTECH SOLUTIONS,
  etc.) - fara coincidente cu companii reale

**Document principal: `referinte/DATA-INSTRUCTIUNI.md`**

Acest document inghetat detaliaza pentru fiecare constructie C01-C08
EXACT ce trebuie facut pe Date_MASTER-initial:
- C01 STRUCTURA: adauga antet ERP brut, subtotale, blank-uri false
- C02 CONTROL: planteaza 5 categorii anomalii logice
- C03 AUDIT: planteaza 550 contaminari invizibile
- C04 NORMALIZARE: aplica toate T1 cumulativ + 3 perturbari noi
- C05 CLASIFICARE: nu planteaza, adauga coloane segment/prioritate
- C06 KPI: nu planteaza, adauga marja_estimata si sheet KPI_GENERAL
- C07 LOGICA TEMPORALA: nu planteaza, adauga sheets agregari lunare/YoY
- C08: TBD la inghetarea SPEC

**Nomenclatura noua fisiere:**
- Asset perpetuu: `referinte/Date_MASTER-initial.xlsx`
- Livrabil per constructie: `Date_MASTER-C{NN}.xlsx`
  (V18 `Date_MASTER-dupa-C{NN}.xlsx` deprecated)

**R-V03.62 PRIMA GENERARE INGHETATA + PATCH OVER EDITED [V36]:**

**Decizie ARHITECT V36 (27 mai 2026):** persistarea modificarilor de continut
intre regenerari se realizeaza prin model in DOUA STARI:

1. **CANONIC INGHETAT** - prima generare a unei constructii. Imutabil ca
   snapshot de referinta. Niciodata suprascris.
2. **EDITAT EVOLUTIV** - copia activa pe care ARHITECT face modificari de
   continut (in Editor HTML) si pe care motorul aplica patch-uri venite
   din upgrade-uri KIT.

**Cele doua stari coexista permanent in arhiva constructiei:**

```
livrabile_C02/
├── canonic/                    # CANONIC INGHETAT (V01 = prima generare)
│   ├── HTML-Studiu-Excel-02-Control.html
│   ├── HTML-Editor-Studiu-Excel-02-Control.html
│   ├── HTML-Video-Excel-02-Control.html
│   ├── HTML-Editor-Video-Excel-02-Control.html
│   ├── Date_MASTER-C02.xlsx
│   ├── Creativ-Excel-02-Control.txt
│   ├── FILM-Excel-02-Control.docx
│   └── assets/
│
└── editat/                     # EDITAT EVOLUTIV (versiunea activa)
    ├── HTML-Studiu-Excel-02-Control.html       # cu modificarile ARHITECT
    ├── HTML-Editor-Studiu-Excel-02-Control.html
    ├── HTML-Video-Excel-02-Control.html
    ├── HTML-Editor-Video-Excel-02-Control.html
    ├── Date_MASTER-C02.xlsx
    ├── Creativ-Excel-02-Control.txt
    ├── FILM-Excel-02-Control.docx
    └── assets/
```

**Workflow operational complet:**

**Faza 1 - Prima generare (CANONIC INGHETAT):**

1. Motorul genereaza C02 conform SPEC + matrita C01 V12 + KIT V36
2. Cele 8 artefacte sunt scrise in `livrabile_C02/canonic/`
3. La acelasi moment, motorul COPIAZA cele 8 artefacte si in
   `livrabile_C02/editat/` (start identic cu canonic)
4. Marker meta `<meta name="trainity-snapshot" content="canonic-V01">`
   adaugat in toate HTML-urile din `canonic/`
5. Marker meta `<meta name="trainity-snapshot" content="editat">`
   adaugat in HTML-urile din `editat/`

**Faza 2 - ARHITECT editeaza in browser:**

1. Deschide `editat/HTML-Editor-Studiu-Excel-02-Control.html` in Chrome
2. Click pe text -> editeaza inline
3. Apasa EXPORT -> primeste fisier descarcat cu numele
   `HTML-Studiu-Excel-02-Control-Editat.html`
4. Inlocuieste manual fisierul din `editat/` cu versiunea exportata
   (sau motorul automat la urmatoarea sesiune)
5. Restul fisierelor din `editat/` raman neschimbate

**Faza 3 - Upgrade KIT (Patch over Edited):**

1. Apare modificare in KIT (ex. R-V03.65 introduce un nou stil vizual)
2. Motorul scrie scriptul de patch ca pattern L151:
   - Regex strict pentru zona specifica
   - Idempotent (re-run nu face nimic)
   - Anti-duble-inject prin marker
3. Scriptul ruleaza pe TOATE constructiile, in folder `editat/`:
   ```bash
   for nn in 02 03 04 05 06...; do
     python3 generatoare/patch_NEW.py livrabile_C$nn/editat/HTML-*.html
   done
   ```
4. Folder `canonic/` ramane IMUTABIL (nu se patchaza)
5. ARHITECT primeste folder `editat/` cu modificarile sale + upgrade-ul KIT
6. Gate v20 PASS pe `editat/` (cu KIT-ul nou)

**Faza 4 - Re-generare la cerere explicita:**

Daca ARHITECT vrea sa restarteze de la zero (de exemplu dupa schimbare
masiva SPEC):
1. Comanda explicita: `regenereaza C02 de la zero`
2. Motorul SUPRASCRIE `canonic/` cu generarea noua (CANONIC V02)
3. Motorul SUPRASCRIE `editat/` cu copia canonicului V02
4. Modificarile vechi sunt PIERDUTE (era cererea explicita)

**De ce DOUA stari, nu doar editat:**

- `canonic/` e snapshot-ul de referinta pentru audit, debug, restore
- ARHITECT poate compara oricand `canonic/` vs `editat/` ca sa vada
  ce s-a schimbat (`diff canonic/HTML-Studiu.html editat/HTML-Studiu.html`)
- Daca patch-ul KIT strica accidental ceva in `editat/`, `canonic/`
  ramane intact ca fallback
- La regenerare full, snapshot-ul vechi din `canonic/` poate fi
  arhivat pentru istorie (optional: `canonic-V01-ARHIVA/`,
  `canonic-V02/`)

**Aplicabilitate:**

- **C06+ (viitoare)**: genereaza AUTOMAT sub schema V36+ cu cele doua
  stari `canonic/` + `editat/` la prima generare.
- **C02-C05 (deja livrate)**: arhivele canonice deja livrate sunt
  promovate la `canonic/` (snapshot de referinta) + creata copia
  initiala in `editat/`. Migrare retroactiva idempotenta.
- **C01 pilot**: NU primeste cele doua stari - este referinta perpetua
  (matrita), nu artefact livrabil.

**Fisier nou V36:**

- `generatoare/init_canonic_editat.py` (~2 KB) - script care promoveaza
  un folder `livrabile_C{NN}/` plat la structura `livrabile_C{NN}/canonic/`
  + `livrabile_C{NN}/editat/`. Idempotent (skip daca structura deja
  exista).

**Lectie L154 codificata:** PERSISTAREA EDITORILOR PRIN NON-REGENERARE
estetichetabila ca strategie. In loc sa separam content de template
si sa regeneram din JSON (complicat, fragil), pastram HTML-urile editate
ca surse de adevar live. Upgrade-urile KIT vin ca patch-uri izolate
aplicate peste editat. Snapshot-ul canonic e tinut pentru reference.

Pattern functional confirmat empiric V32-V34: cover-meta cleanup, buton
lipit responsive, highlighter V34 - toate au fost aplicate ca patch-uri
pe HTML-uri canonice existente, fara regenerare. Gate v20 PASS pe toate.

Asta inseamna ca daca patch-urile sunt scrise corect (pattern L151:
regex strict + idempotent + anti-duble-inject), ele se aplica cu acelasi
succes peste HTML-uri editate cu continut diferit. Continutul TAU e
intangibil de patch-ul KIT, pentru ca patch-ul tinteste DOAR zona
specifica.

---

**R-V03.61 BUTON RESET PROGRES LIPIT DE MENIU (RESPONSIVE FIX) [V33]:**

**Decizie ARHITECT V33 (27 mai 2026):** butonul "RESETEAZA PROGRES"
din `.nav-controls` trebuie sa fie LIPIT imediat sub meniul cu 8
verificari finale (`.nav-finals`), NU forfat la baza side-nav prin
`margin-top: auto`.

**Bug descoperit empiric pe tableta Samsung landscape (~1600x1000):**

CSS original `.nav-controls { margin-top: auto; }` impingea butonul
la baza coloanei side-nav. Pe desktop normal (1920x1080+), continutul
side-nav (brand + progres + 6 etape + 8 verificari) umple inaltimea
disponibila, butonul ajunge natural lipit de ultim element. Pe
tableta landscape cu inaltime mai mica (1000-1024px), continutul NU
umple inaltimea, gap-ul `margin-top: auto` produce 315-339px spatiu
gol intre meniu si buton - inestetic, vizual deconectat.

Verificare empirica Playwright:
- Samsung Tab landscape (1600x1000): gap 315px → 0px dupa fix
- iPad landscape (1366x1024): gap 339px → 0px dupa fix
- Laptop standard (1440x900): gap 215px → 0px dupa fix
- Desktop FullHD (1920x1080): gap 395px → 0px dupa fix

Pe TOATE viewport-urile, butonul ramane lipit perfect sub meniu.
Spatiul nefolosit (315-395px) ramane jos in side-nav (fundal negru
continuu, estetic acceptabil).

**Fix tehnic:**

Eliminam `margin-top: auto;` din regula CSS `.nav-controls`. Restul
proprietatilor (padding, border-top, flex direction) raman.

Inainte:
```css
.nav-controls {
  padding: 12px 18px 18px;
  border-top: 1px solid #222;
  margin-top: auto;            /* <-- ELIMINATE */
  display: flex; flex-direction: column; gap: 6px;
}
```

Dupa:
```css
.nav-controls {
  padding: 12px 18px 18px;
  border-top: 1px solid #222;
  display: flex; flex-direction: column; gap: 6px;
}
```

**Aplicabilitate:**

- Constructiile noi (C06+) genereaza HTML-Studiu + Editor-Studiu fara
  `margin-top: auto` in .nav-controls.
- Constructiile existente (C01 pilot, C02-C05) patchate via
  `generatoare/fix_reset_button_position.py` (idempotent).

**Fisier nou V33:**

- `generatoare/fix_reset_button_position.py` (~1.5 KB) - script patch
  cu regex strict pentru eliminare `margin-top: auto` doar din regula
  `.nav-controls` (NU din alte locuri unde ar putea aparea pattern-ul).

**Patch retroactiv aplicat:**

- C01 pilot HTML-Studiu + Editor-Studiu: patchat
- C02 V26 HTML-Studiu + Editor-Studiu: patchat
- C03 V26 HTML-Studiu + Editor-Studiu: patchat
- C04 V27 HTML-Studiu + Editor-Studiu: patchat
- C05 V28 HTML-Studiu + Editor-Studiu: patchat
- Gate v20 PASS pe toate dupa patch

**Lectie L152 codificata:** REGULILE CSS "margin-top: auto" PENTRU
"PUSH TO BOTTOM" FUNCTIONEAZA DOAR DACA CONTINUTUL ARE INALTIME FIXA
SI CONTAINER-UL E STRICT MAI MIC. In cazul contrar (continut variabil,
container cu height calc(100vh-...) pe viewport-uri diferite), produce
gap-uri vizuale inestetice.

Solutie: pentru elemente UI care trebuie sa fie "imediat dupa precedent",
foloseste pozitionare naturala (NU margin-top: auto), accepta ca poate
ramane spatiu nefolosit la baza container-ului. Estetic, e mai bine
decat un buton plutind la mijlocul fundalului negru.

Pattern similar cu L151 (UI cleanup retroactiv): script izolat in
`generatoare/`, regex strict, idempotent, aplicat batch, gate v20 PASS
post-patch.

---

**R-V03.60 COVER-META FARA INPUT/OUTPUT IN HTML-STUDIU [V32]:**

**Decizie ARHITECT V32 (26 mai 2026):** cover-meta din HTML-Studiu si
HTML-Editor-Studiu trebuie sa contina DOAR cele 3 randuri canonice:
- TREAPTA
- CONSTRUCTIE (NN din 20 · Pack 02 Excel)
- AI INTEGRAT (descrierea prompturilor Copilot)

Randurile "INPUT" si "OUTPUT" (care indicau fisierul Excel) sunt
ELIMINATE din cover-meta. Sunt reziduuri din schema veche pre-R-V03.47
(Date-Input + Date-Output separate) si nu mai sunt de actualitate.
Sistemul actual foloseste un singur Date_MASTER-CNN.xlsx per
constructie.

**De ce eliminate:**

1. Sub schema actuala (R-V03.47/R-V03.49), exista un singur fisier
   Date_MASTER-CNN.xlsx care contine si input si output (input pe
   sheet "Vanzari", output pe sheet specific constructiei). Cele
   doua randuri INPUT + OUTPUT din cover-meta arata acelasi fisier
   - redundanta vizuala.
2. Informatia despre fisier nu trebuie sa fie pe primul ecran al
   cursantului - el ajunge la fisier prin contextul construcției,
   nu prin link direct la metadate.
3. Cover-meta trebuie sa fie minimalist: trei date esentiale (treapta,
   pozitia in pack, AI integrat). Restul e zgomot.

**Aplicabilitate:**

- Constructiile noi (C06+) genereaza HTML-Studiu si Editor-Studiu
  DEFAULT fara randurile INPUT/OUTPUT in cover-meta.
- Constructiile existente (C02 V26, C03 V26, C04 V27) sunt patchate
  retroactiv via `generatoare/remove_input_output_meta.py` care
  detecteaza si elimina cele 2 randuri. Idempotent (skip silentios
  daca patch-ul a fost deja aplicat).
- C05 V28 era deja corect (motorul C05 V28 a omis randurile la
  generare).

**Fisier nou V32:**

- `generatoare/remove_input_output_meta.py` (~2 KB) - script patch
  idempotent. Pattern-uri regex pentru detectare + eliminare cele
  doua randuri din cover-meta.

**Modificari livrabile T1:**

- C02 V26 HTML-Studiu si Editor-Studiu: -497 bytes fiecare (8 randuri
  HTML eliminate)
- C03 V26 HTML-Studiu si Editor-Studiu: -447 bytes fiecare
- C04 V27 HTML-Studiu si Editor-Studiu: -490 bytes fiecare
- Gate v20 PASS pe toate 4 dupa patch

**Lectie L151 codificata:** UI cleanup retroactiv prin script idempotent.
Cand un element vizual devine obsolete dintr-o schimbare de arhitectura
(aici R-V03.47 a unificat input+output intr-un singur fisier dar UI
nu a fost curatat sincronizat), eliminarea retroactiva se face printr-un
script de patch izolat:
- Pattern regex strict (anti-fals-pozitive)
- Idempotent (re-run nu face nimic)
- Anti-orphan whitespace (elimina si linia goala lasata in urma)
- Verificat post-patch cu gate v20 PASS

Pattern similar cu R-V03.59 (highlighter): snippet izolat in
`generatoare/`, script reutilizabil, aplicabil batch.

---

**R-V03.59 HIGHLIGHTER PERSISTENT HTML-VIDEO [V31 → V34 refinat]:**

**Update V34 (27 mai 2026):** comportament rafinat dupa feedback ARHITECT.

**Decizia V34:**

1. **ELIMINAT** buton "Reseteaza evidentieri" din colt stanga-jos
2. **ELIMINAT** keybind ESC pentru reset
3. **Click pe text evidentiat** = toggle off (revine textul), **DAR**
   previne advance la urmatorul slide/frag
4. **Click ulterior pe acelasi loc** (text plain dupa toggle) = merge
   inainte normal

**Cum se realizeaza tehnic:**

Click handler pe document foloseste **CAPTURE PHASE** (`addEventListener('click', onClickCapture, true)`), care intercepteaza click-ul INAINTE de handler-ul stage element (`nextFrag()` pe bubble phase). Daca click-ul e pe un `.trainity-highlight`, handler-ul apeleaza:
- `e.preventDefault()`
- `e.stopPropagation()`
- `e.stopImmediatePropagation()`
- `removeHighlight(span)` + `saveHighlights()`

Si **return-eaza** fara sa lase event-ul sa ajunga la stage handler. Click-ul nu produce advance.

Daca click-ul e pe text plain (NU highlight), handler-ul NU face nimic - event-ul propaga normal la stage handler care apeleaza `nextFrag()`.

**Decizie ARHITECT V31 (26 mai 2026):** HTML-Video are nevoie de
feature de evidentiere persistenta pentru text - cursantul poate
marca pasaje cheie cu fond galben Trainity in timpul vizualizarii
filmului, marcajele raman intre sesiuni (persistente in localStorage).

**Comportament functional:**

1. **Selectie text cu mouse-ul** -> la `mouseup`, daca selectia
   contine cel putin un caracter non-whitespace, textul este invelit
   intr-un `<span class="trainity-highlight">` cu:
   - background `#FFD400` (galben Trainity canonic)
   - color `#000` (text negru)
   - cursor pointer
2. **Click pe text deja marcat** -> toggle off: elimina `<span>`-ul,
   pastreaza text plain, salveaza state.
3. **Buton "Resetează evidențieri"** in colt stanga-jos (`fixed`
   bottom 18px, left 18px), brand Trainity (galben + border negru
   + shadow). Apare DOAR cand exista marcaje, dispare cand 0.
4. **Tasta ESC** -> sterge toate marcajele (echivalent click pe buton).
5. **Persistenta:** marcajele salvate in `localStorage` cu key
   `trainity_c{NN}_video_highlights_v1`. La incarcare pagina,
   marcajele sunt restorate automat.

**Constrangeri tehnice:**

- Refuz wrap pentru selectii care:
  * Au lungime 0 (whitespace doar)
  * Traverseaza deja un highlight existent (anti-nesting)
  * Traverseaza elemente blocate: `IMG`, `BUTTON`, `INPUT`, `IFRAME`,
    `VIDEO`, `AUDIO`, `CANVAS`, `SVG`
- Pentru selectii care traverseaza limite de noduri (span partial),
  fallback la `extractContents()` + wrap manual.
- Anti-duble-init prin marker `<meta id="trainity-highlighter-v1">`.

**Stocare persistenta:**

Format JSON in localStorage:
```json
[
  {
    "id": "1716750000000-123",
    "text": "textul evidentiat",
    "parentPath": "0/3/1/5",  // path indecsi catre parintele span
    "siblingIdx": 7
  },
  ...
]
```

La restore, algoritmul cauta textul exact in parintele indicat (prin
path-ul indecsilor) si reaplica wrap-ul. Daca text-ul nu mai exista
(improbabil pentru pagina statica), marcajul respectiv e ignorat
silentios.

**Aplicabilitate:**

- Constructiile noi (C06+) primesc AUTOMAT highlighter la generare:
  motorul injecteaza CSS + JS in HTML-Video la step-ul final inainte
  de checkout.
- Constructiile existente (C02 V26, C03 V26, C04 V27, C05 V28) sunt
  patchate via `generatoare/inject_highlighter.py` care detecteaza
  anti-duble-inject si poate fi rulat la nivel batch peste toate
  livrabilele canonice T1.

**Fisiere noi V31:**

- `referinte/highlighter-snippet.css` (asset perpetuu, ~1.2 KB)
- `referinte/highlighter-snippet.js` (asset perpetuu, ~7.4 KB)
- `generatoare/inject_highlighter.py` (script patch, ~3 KB)

**Cost performance:**

Marime HTML-Video creste cu ~12.6 KB (de la ~796 KB la ~809 KB,
+1.6%). Acceptabil pentru un fisier deja mare cu base64 inline.

**Doar pe HTML-Video, NU pe HTML-Studiu sau Editor:**

Highlighter-ul e specific HTML-Video unde cursantul urmareste pasiv
filmul si marcheaza cu mouse-ul. HTML-Studiu are deja interactivitate
proprie (next step, copy prompt, etc.), unde highlighting-ul ar
interfera. Editor-urile sunt versiuni de editare DOM care nu au
nevoie de feature consumer.

**Lectie L150 codificata:** featuri consumer "soft" (highlighter,
bookmark, etc.) pot fi adaugate AUDITIV peste schema livrabile
canonice fara a sparge gate v20. Diferenta intre LIVRABIL NUCLEU
(verificat de gate exhaustiv) si FEATURE CONSUMER (injectat aditiv,
opt-in vizual): nucleul e imutabil cap-coada, feature-ul se poate
itera independent.

R-V03.59 stabileste pattern-ul: snippet izolat in `referinte/`,
script `inject_*.py` care patcheaza, anti-duble-inject prin marker,
fara modificare la livrabilele canonice ale R-V03.47.

---

**R-V03.58 ARHIVARE EXTINSA - ASSETS/ + FILM.DOCX IN ARHIVA LIVRABILELOR [V30]:**

**Decizie ARHITECT V30 (26 mai 2026):** alaturi de cele 6 livrabile
canonice per constructie, motorul de generare adauga in arhiva
checkout-ului DOUA artefacte suplimentare pentru arhivare:

1. **Folder `assets/`** continand imaginile cinematice ca fisiere
   separate (.jpg + .png variante).
2. **Document `FILM-Excel-{NN}-{slug}.docx`** continand scriptul video
   procedural cinematic.

**Important:** cele 6 livrabile canonice raman NEMODIFICATE - HTML-Video
continua sa contina imaginile inline ca base64 (R-V03.33). Pozele in
folder `assets/` sunt DUPLICAT pentru arhivare, NU inlocuiesc base64-ul
din HTML-Video.

**Schema arhiva checkout constructie V30 (8 artefacte):**

```
livrabile_C{NN}/
├── HTML-Studiu-Excel-{NN}-{slug}.html               (livrabil 1)
├── HTML-Editor-Studiu-Excel-{NN}-{slug}.html        (livrabil 2)
├── HTML-Video-Excel-{NN}-{slug}.html                (livrabil 3, base64 inline)
├── HTML-Editor-Video-Excel-{NN}-{slug}.html         (livrabil 4)
├── Date_MASTER-C{NN}.xlsx                           (livrabil 5)
├── Creativ-Excel-{NN}-{slug}.txt                    (livrabil 6)
├── FILM-Excel-{NN}-{slug}.docx                      (arhivare 7) [V30+]
└── assets/                                           (arhivare 8) [V30+]
    ├── exec-stage-1.jpg
    ├── exec-stage-1.png
    ├── exec-stage-2.jpg
    ├── exec-stage-2.png
    ├── exec-stage-3.jpg
    ├── exec-stage-3.png
    ├── exec-stage-4.jpg
    ├── exec-stage-4.png
    ├── exec-stage-5.jpg
    ├── exec-stage-5.png
    ├── exec-stage-6.jpg
    └── exec-stage-6.png
```

**De ce DOUA artefacte de arhivare:**

- `assets/`: pentru arhivare separata, refolosire in alte contexte
  (presentare, blog, social media), reeditare imagini fara a sparge
  HTML-ul, backup independent.
- `FILM-Excel-NN.docx`: pentru arhivare narativa scriptata, refolosire
  in training trainer, recapitulare cinematica, document de referinta
  pentru OBS Studio recording (decorul mental al inregistrarii video).

**Continut FILM-Excel-{NN}-{slug}.docx:**

Document de tip script video procedural cinematic, ~150 paragrafe,
structurat:
1. Header: titlu, treapta, pozitia constructiei in pack
2. IDENTITATE CINEMATICA: INTRIGA (HOOK), MIZA, MANTRA, WOW (PAYOFF),
   MOTTO
3. DESCHIDERE: de ce constructia, context narrativ
4. ROLURI: AI / Power Query / Operatorul - cine face ce
5. SCENA REALA: fenomenele/anomalii/operatii concret
6. CELE 6 ETAPE cinematic detaliate (HOOK → DEMO → CONTROL → REVEAL
   pe fiecare etapa)
7. VERIFY: dovada finala
8. FINAL: payoff + tranzitie catre constructia urmatoare

**Cele 6 imagini cinematic (exec-stage-1..6):**

Imagini Banana 2 (asset Trainity perpetuu), proportii 3:2 cinematic,
folosite ca fundal Ken Burns in Executive Show embedded in HTML-Video
final (slide tranzitie CONCLUZII + 6 slide-uri cinematic 9s pe fiecare
imagine + closing apoteotic).

**Sursa imagini:** asset perpetuu Trainity, deja inglobat in
`creative_banana2/` din arhiva sistem. NU se regenereaza per constructie.
Aceleasi 6 imagini sunt copiate in `assets/` pentru fiecare constructie.

**Conditii la `checkout constructie`:**

Motorul de generare in chat CONSTRUCTIE NN, la primirea comenzii
`checkout constructie`, impacheteaza in arhiva:
- Cele 6 livrabile canonice (R-V03.47 neschimbat)
- Folder `assets/` cu cele 12 fisiere (6 exec-stage × jpg + png)
- Document `FILM-Excel-{NN}-{slug}.docx`

Total: 6 livrabile + 1 folder cu 12 fisiere + 1 document = 8 artefacte
in arhiva, sub `livrabile_C{NN}/`.

**Aplicabilitate retroactiva:**

Pentru constructiile T1 deja livrate (C02 V26, C03 V26, C04 V27, C05 V28),
arhivele canonice NU sunt regenerate retroactiv. La urmatoarea utilizare/
regenerare a unei constructii, se aplica R-V03.58. Constructiile noi
(C06+) genereaza automat sub schema V30+.

**Lectie L149 codificata:** decizii de arhitectura artefacte se pot
schimba in timp pe baza necesitatilor operationale. Cand un livrabil
util a fost eliminat anterior (R-V03.19 a sters PPT + FILM separat,
R-V03.33 a inlocuit assets cu base64 inline) si apoi devine necesar
din nou pentru un caz de uz specific (arhivare independenta, refolosire
in alte contexte), reintroducerea trebuie facuta ADITIV (NU inlocuieste
livrabile canonice existente). 

R-V03.58 este aditiva: cele 6 livrabile canonice raman, assets/ +
FILM.docx se adauga ca artefacte arhivare. Cursantul primeste tot
ce primea inainte plus DOUA artefacte suplimentare.

---

**R-V03.56 SPEC FREEZING - FORMAT GRILA CU 3 VARIANTE CREATIVE [V23]:**

**Problema descoperita V22->V23:** la inghetare SPEC C05 in chat
CONSTRUCTIE 05, motorul a folosit format conversational deschis:
- "INTRIGA este ... la C04 era X. Care e INTRIGA ta pentru C05?
   Cateva directii posibile: A, B, C. Care e INTRIGA ta?"

Asta forteaza ARHITECT-ul Bogdan sa GENEREZE creativ pe loc, ceea
ce este obositor si genereaza inconsistente intre sesiuni.

Format-ul corect (folosit V14-V17, **pierdut** in V19-V22): motorul
propune 3 variante creative concrete, ARHITECT-ul alege una sau cere
inca 3 noi.

**Format obligatoriu V24 pentru INGHETARE SPEC (toate cele 9 elemente):**

Pentru fiecare element din SPEC C{NN}, in ordinea NARATIVA stricta:

```
Intrebarea N din 9: [NUMELE_ELEMENTULUI]

[Scurta explicatie 1-2 randuri ce rol are elementul]

La C04 [NUMELE_ELEMENTULUI] era: "[exemplu din C04 inghetat]"

Pentru C{NN} ({nume_constructie}), iata 3 propuneri creative:

A. "[varianta 1 creativa]"
B. "[varianta 2 creativa]"
C. "[varianta 3 creativa]"

Alege A, B sau C. Daca niciuna nu te convinge, scrie "alte 3" si
generez alte propuneri pe alta directie.
```

**Cele 9 elemente in ordinea OBLIGATORIE (decizie ARHITECT, recodificare
V24 dupa pierdere convenție veche):**

1. **INTRIGA** - paradoxul/provocarea care deschide constructia
2. **PROBLEMELE PE CARE LE REZOLVA** - lista incitanta, utila si de
   efect a problemelor concrete pe care constructia le rezolva.
   Format: 3-5 probleme scurte (1 propozitie fiecare), in formulare
   directa, fara jargon, care pun cursantul sa zica "da, am asta".
3. **MIZA** - ce castiga cursantul concret la final
4. **MANTRA** - fraza-semnatura care ramane cu cursantul
5. **MOTTO** - sub-hook complementar mantrei
6. **STEP-TITLES (18)** - progresia narativa pas cu pas (rafala in
   format grila, motorul propune 3 seturi A/B/C de 18 step-titles
   coerente, ARHITECT alege un set sau face merge)
7. **PROMPTURI Copilot (2)** - instrumentele AI ale constructiei
   (format grila pentru fiecare prompt: 3 variante creative cu
   diferenta de unghi de atac)
8. **FINAL-LABELS (8)** - ancorele de retentie (rafala in format
   grila, motor propune 3 seturi A/B/C, ARHITECT alege)
9. **FENOMENE/OPERATII** specifice constructiei (anomaly-grid 5 cards
   in HTML, BLOC 14 canonic R-V01.x). Format: titlu CAPS 1-3 cuvinte +
   cifra concreta + descriere scurta. Real in fisier, NU inventate.
   Cele 5 alese influenteaza INPUT.xlsx (datele se construiesc sa le
   contina). Motorul propune 10, ARHITECT alege 5.

   **CRITIC - L140 anti-confuzie cu PROBLEMELE (pozitia 2):**
   - PROBLEMELE = intrebari pe care si le pune operatorul ("Cati / Care")
   - FENOMENE = anomalii / observatii FIZICE in fisier cu cifre concrete
     (ex: "47 CLIENTI", "3 BUCURESTI", "2.000 RANDURI")
   Cele doua sunt COMPLEMENTARE, NU substituibile. Vezi L140 pentru
   regula completa si tabel cuvinte-cheie anti-confuzie.

   Tipologie variabila per treapta:
   - T1 STRUCTURA: contaminari fizice (ANTET RAPORT, SUBTOTAL, BLANK FALS)
   - T2 CUNOASTERE: observatii descriptive (cardinalitati, anomalii etichetare,
     granularitate, distributii) - vocabular L136.A strict
   - T3 ANALIZA: motoare / anti-patterns de modernizat (VLOOKUP->XLOOKUP etc)
   - T4 RAPORTARE: elemente vizuale problematice (cifre fara context,
     grafice gresite)
   - T5 AUTOMATIZARE: bottleneck-uri / interventii manuale repetate

**Logica ordinii narative:**

INTRIGA deschide paradoxul (ATENTIE). PROBLEMELE listeaza concret ce
rezolva (RECUNOASTERE - "da, eu am asta"). MIZA promite castigul
concret (DORINTA). MANTRA + MOTTO fixeaza identitatea constructiei
(RETENTIE). Step-titles + prompturi + final-labels detaliaza executia.
Fenomene/operatii incheie cu specificul tehnic.

**Lectie L133 codificata:** PROBLEMELE pe care le rezolva constructia
e elementul cheie pentru ATRACTIE EMOTIONALA. Fara el, INTRIGA ramane
abstracta si MIZA ramane neclara. Cursantul are nevoie sa se
recunoasca in lista de probleme inainte sa accepte miza. Ordinea
narativa: paradox -> probleme concrete recunoscute -> miza castig
concret -> mantra identitate. Era convenția C01-C04, pierduta in
V19-V23, recodificata V24.

**Lectie L136 codificata (25.05.2026, chat SPEC C05):** Confuzia
TREAPTA-TREAPTA produce SPEC eronate. T2 CUNOASTERE (fost T2 CALCUL pana
la 25.05.2026, vezi L139) nu inseamna "KPI
business" sau "atribuie semnificatie" - aia e T3 ANALIZA. T2 inseamna
PROFILAREA SETULUI (descriptiv, cunoastere de set, imagine din satelit).

Test rapid pentru motor inainte de SPEC pe T2:
- Intrebari T2 corecte: "din ce e facut", "cat masoara", "cum se
  distribuie in timp", "cum se integreaza" (DESCRIPTIVE).
- Intrebari T3 (de evitat in SPEC T2): "ce inseamna", "care e prioritar",
  "unde pierd", "ce decid" (DECIZIONALE).

Cuvant marker T2: "profil", "cunoastem", "descoperim", "masuram",
"interval", "frecventa", "distributie", "granularitate", "extreme".
Cuvant marker T3 (de evitat in T2): "strategic", "prioritar", "decizie",
"semnificatie business", "categorie A/B/C", "valoare reala", "important".

"Clasificare" in C05 = inventar de categorii existente (descriptiv),
NU atribuire de categorii noi (decizional - aia e T3 si T4).

Aceasta confuzie a costat 3 iteratii in chat SPEC C05 (25.05.2026).
Cel mai important: a aratat ca motorul propune SPEC business strategy
prematur cand numele constructiei contine cuvinte care suna business
("clasificare", "calcul", "KPI"). Solutia: motorul confirma intai
intrebarea-mama a constructiei pe schema profilare descriptiva
inainte sa propuna elemente SPEC.

Reguli derivate pentru SPEC C06-C08:
1. Inainte de SPEC FREEZING C{NN} pe T2, motorul confirma cu ARHITECT
   intrebarea-mama a constructiei (descriptiv, NU decizional).
2. PROBLEMELE C{NN} pe T2 incep cu "Cati / Care / Cat / Cum / Exista" -
   intrebari de profilare, NU "Care e strategic / prioritar / valoros".
3. INTRIGA C{NN} pe T2 ataca orbirea descriptiva ("ai date dar nu le
   cunosti"), NU orbirea decizionala ("ai date dar nu decizi pe ele").
4. MIZA C{NN} pe T2 = "operatorul iese cu fisa de profil [tip]", NU
   "operatorul iese cu strategie / prioritizare / decizie".

**RAFINARE L136.A (25.05.2026, decizie Bogdan): separare obsesiva
C05 vs C06.**

Problema descoperita: C05 si C06 erau prea apropiate. Ambele foloseau
COUNT, ambele raspundeau la "cate", granita se topea cand venea cursantul.

Solutie: separare pe DOUA AXE COMPLET DIFERITE, NU pe nuante.

C05 = AXA CALITATIVA (categorial, taxonomic)
- Intrebare-mama: "Ce contine setul?"
- Raspuns sub forma de: ETICHETE, enumerari, liste, dictionar
- Verb dominant: descopera, identifica, enumera, distinge
- Operatii: UNIQUE, FILTER, SORT, COUNTIF per categorie, tabla de frecvente
- Livrabil: dictionarul setului (lista categoriilor existente, tipologia
  randurilor, granularitatea atomica)
- Cuvant marker strict: "eticheta"

C06 = AXA CANTITATIVA (numeric, statistic)
- Intrebare-mama: "Cum arata numeric setul?"
- Raspuns sub forma de: CIFRE, agregate, intervale, procente
- Verb dominant: masoara, calculeaza, agregheaza, compara numeric
- Operatii: SUM, AVERAGE, MEDIAN, MIN, MAX, STDEV, LARGE, SMALL, proportii
- Livrabil: profilul numeric al setului (intervale, medii, distributii)
- Cuvant marker strict: "cifra"

Test de delimitare codificat:
- "Cati clienti unici am?"       -> C05 (cardinalitate categoriala)
- "Care e suma medie per client?" -> C06 (masuratoare numerica)
- "Cate produse distincte?"       -> C05 (inventar categorial)
- "Care produs are valoarea cea mai mare?" -> C06 (clasament numeric)
- "Cate randuri pe luna?"         -> C07 (profil temporal)

Mantra de separare obsesiva (de propagat in SPEC C05 si SPEC C06):
**C05 = ETICHETE.** Raspunsuri in cuvinte si liste.
**C06 = CIFRE.** Raspunsuri in numere si agregate.

Cuvantul "eticheta" in C05 si cuvantul "cifra" in C06 devin marker-i
lingvistici stricti propagati in step-titles, prompturi, final-labels.

**RAFINARE L136.B (25.05.2026, decizie Bogdan): C07 e constructia
CINEMATICA a T2.**

Problema descoperita: pe formulare functionala (YOY, MOM, rolling,
sezonalitate), C07 era cea mai slaba a treptei T2. Suna a Power BI
tutorial, nu a Trainity.

Solutie: reformulare cinematica radicala. C07 nu mai e "logica temporala
functionala", e povestea memoriei setului.

C07 LOGICA TEMPORALA - constructia poetica a T2:
- Intrebare-mama: "Ce-si aminteste setul?"
- Verb dominant: isi aminteste, povesteste, dezvaluie, retine
- Livrabil: harta memoriei setului (calendarul vietii setului, lunile cu
  greutate vs fara, varfurile uitate, ritmul ascuns)
- Operatii: EOMONTH, DATEDIF, WEEKDAY, SUMIFS pe ferestre, distributie
  temporala

INTRIGA C07 candidat (de validat in SPEC FREEZING C07): "Setul are memorie."
Putere triplata:
- Strat 1 PARADOX: setul e static, cum poate avea memorie?
- Strat 2 ADEVAR ASCUNS: setul chiar are memorie (datele inlantuie
  cronologia), operatorul a ignorat-o.
- Strat 3 ANTROPOMORFIZARE CALDA: personifica setul fara AI hype.

MANTRA C07 candidat: "Setul are memorie. Operatorul invata sa o citeasca."

PERICOL CODIFICAT: antropomorfizarea trebuie sa creeze imediat ACTIUNE
("interoghez memoria"), NU VIBRATIE ("oh, ce frumos"). Lipim imediat o
ancora operationala. Exemplu: "Setul are memorie. Excel n-o citeste singur.
Operatorul ii cere."

INTERZIS in C07: "datele vorbesc cu noi", "AI inteligent intelege istoria",
"insighturi temporale magice" - astea ar fi AI hype-light si decorativism.
Permis: "setul isi aminteste / povesteste / pastreaza / retine".

REGISTRU T2 COMPLET (variatie pedagogica intentionata):
- C05 + C06 = constructii PRAGMATICE (etichete + cifre)
- C07 = constructie CINEMATICA (memoria setului)
- C08 = constructie de POD (consolidare multi-sursa pentru T3)

Asta da ritm pedagogic T2 sanatos: nu 4 constructii uniforme functionale,
ci 2 pragmatice + 1 poetica + 1 de pod.

**Lectie L137 codificata (25.05.2026, chat SPEC C05): definitiile celor
5 elemente narative trebuie verificate in SISTEM la FIECARE inghetare,
NU asumate din memorie.**

Problema descoperita: motorul a propus la SPEC FREEZING MOTTO C05
"Cunoasterea descriptiva vine inaintea judecatii" - filozofie universala
Trainity, NU semnatura post-constructie. Bogdan a corectat: "motto nu
era fraza de la final?"

Definitiile corecte (canonice SISTEM linia 1142-1159, de verificat
inainte de orice propunere):

| # | Element  | Rol psihologic | Emotie inspirata | Continut |
|---|----------|----------------|------------------|----------|
| 1 | INTRIGA  | ATENTIE        | curiozitate      | paradox initial |
| 2 | MIZA     | TENSIUNE       | ingrijorare rationala | consecinta lipsei |
| 3 | MANTRA   | PROMISIUNE     | incredere operationala| formula sistemului, repetabila |
| 4 | WOW      | ELIBERARE      | satisfactie ("a meritat")| eliberare post-actiune |
| 5 | MOTTO    | SEMNATURA      | convingere personala  | regula INTERNA a operatorului DUPA constructie |

MOTTO NU e:
- Filozofie universala Trainity ("Cunoasterea X vine inaintea Y")
- Principiu de companie ("Profilul setului e o forma de respect")
- Slogan abstract ("Cunoasterea descriptiva vine inaintea judecatii")

MOTTO ESTE:
- Semnatura mentala a operatorului DUPA construcția
- "Asta e regula mea de acum"
- Pattern C01: "Mai intai X. Apoi orice."
- Pattern C02: "X se Y si se Z, niciodata nu se W."
- Pattern C03: "X nu au disparut singure. Au fost Y."
- Pattern C04: "X manual o singura data. Apoi sistemul Y singur."
- Pattern C05: "Un X cunoscut. Apoi orice Y."

Regula derivata pentru motor (aplicare la SPEC C06-C20):
**Inainte de orice grila SPEC FREEZING pentru element narativ
INTRIGA/MIZA/MANTRA/WOW/MOTTO, motorul citeste definitia canonica
din SISTEM linia 1142-1159 si genereaza pe baza ei. NU genereaza
din memorie semantica.**

Aceasta lectie costa 1 iteratie in chat SPEC C05 (25.05.2026).
Codificata aici ca lectie permanenta de evitat la C06-C20.

**Lectie L138 codificata (25.05.2026, chat SPEC C05, decizie Bogdan):
ANTI-HALLUCINATION GUARD pentru prompturile Copilot in TOATE constructiile
C05-C20.**

Descoperita la rafinarea prompturilor C05. Bogdan a observat ca
prompturile vechi tipice "AI demo" / "prompt engineering gimmick"
deschid usa hallucinatiei consultant: modelul interpreteaza, propune
roluri business, alege din optiuni semantice. Trainity NU vrea consultant
AI. Trainity vrea investigator descriptiv augmentat.

REGULA UNIVERSALA (aplicabila la TOATE prompturile Copilot din SCARA):

Prompturile trebuie sa fie:
1. **DESCRIPTIVE**, NU interpretative
   - DA: "estimeaza granularitatea pe baza structurii"
   - NU: "spune-mi ce este: tranzactie / factura / linie produs"

2. **CONTROLABILE**, NU deschise
   - DA: "clasifica in 3 niveluri: mic, mediu, mare"
   - NU: "spune-mi care e cardinalitatea"

3. **OBSERVATIONALE** semantic (cuvinte ancorate in observabile),
   NU semantic-business
   - DA: "aproape unice" (observatie: cardinalitate apropiata de 1)
   - NU: "identificatori unici" (rol functional business)
   - DA: "predominant repetitive" (pattern observat in set)
   - NU: "unde ar trebui sa se repete" (expectatie externa business)

4. **BAZATE PE OBSERVABILE** (verbe care implica incertitudine onesta),
   NU pe interpretare ontologica
   - DA: "estimeaza", "marcheaza", "clasifica in niveluri", "listeaza"
   - NU: "spune-mi ce este", "identifica rolul", "explica de ce"

5. **CU OPTIUNI STRUCTURALE** (cand se ofera optiuni, ele sa fie pe
   axa structurala observabila), NU pe axa business semantica
   - DA: "nivel de cardinalitate: mic/mediu/mare"
   - NU: "tip: tranzactie/factura/linie produs"

6. **FLUIDE SPOKEN** (limbaj natural conversational), NU brief de
   consultant cu 3-4 imperative succesive
   - DA: "analizeaza, spune-mi X, identifica separat Y, returneaza Z"
   - NU: "Identifica A. Identifica B. Identifica C. Returneaza."

Capcana protejata: AI consultant hallucination. Modelele LLM moderne
sunt antrenate sa "ajute" cu interpretari business cand sunt rugate
sa identifice "tipuri" sau "roluri". Daca prompturile Trainity invita
explicit la interpretare, modelul va inventa categorii business
plauzibile dar nedovedite. Operatorul valideaza inventiile, ramane
fara dictionar real.

Solutia codificata: prompturile descriu STRUCTURI OBSERVABILE
(cardinalitate, frecventa, repetitivitate, izolare), NU SEMNIFICATII
BUSINESS (tipuri, roluri, importante). Modelul observa si raporteaza;
operatorul interpreteaza intr-o etapa ulterioara, in T3 ANALIZA, cand
exista obiectiv de decizie.

Test rapid pentru validare prompt inainte de inghetare in SPEC C{NN}:
- Contine optiuni business explicite ca lista? (tranzactie/factura/...)
  -> REJECT, reformuleaza ca "estimeaza pe baza structurii".
- Contine verbe interpretative? (identifica rolul / spune-mi ce e)
  -> REJECT, inlocuieste cu "estimeaza / clasifica / marcheaza".
- Contine cuvinte semantic-business? (identificatori, importanti,
  strategici, relevanti, valorosi)
  -> REJECT, inlocuieste cu observatie descriptiva ("aproape unice",
     "predominant repetitive", "izolate").
- Suna ca brief de consultant cu imperative succesive?
  -> REJECT, fluidizeaza spoken.

Aceasta lectie a fost descoperita la C05 si codificata aici ca regula
permanenta. Aplicabila la TOATE prompturile Copilot din C05-C20,
inclusiv T3, T4, T5. In T3 ANALIZA, cand intra inevitabil semantica
business, prompturile vor avea ANCORE OBSERVATIONALE explicite (date
care sustin decizia, NU decizie inventata) - dar regula L138 ramane
canonic la T2.

**Lectie L139 codificata (25.05.2026, chat SPEC C05, decizie Bogdan):
REDENUMIRE PERMANENTA T2 CALCUL -> T2 CUNOASTERE. Decizie de
identitate SCARA.**

SCARA noua oficiala:
- T1 STRUCTURA       (datele exista corect)
- T2 CUNOASTERE      (operatorul intelege ce este setul)  <-- NOU
- T3 ANALIZA         (operatorul interpreteaza ce spune setul)
- T4 RAPORTARE       (operatorul transmite ce spune setul)
- T5 AUTOMATIZARE    (operatorul orchestreaza setul autonom)

Acronim SCARA pastrat (S-C-A-R-A). Litera C ramane neschimbata. Numai
denumirea completa schimbata: "CALCUL" -> "CUNOASTERE".

Motivatie cumulativa:
1. L136 a invalidat denumirea "CALCUL" pentru T2: continutul treptei e
   PROFILARE/CUNOASTERE DESCRIPTIVA, NU calcul KPI executiv. Discrepanta
   nume-continut era activa.
2. "CUNOASTERE" capteaza exact functia pedagogica (operatorul cunoaste
   setul multidimensional).
3. C05-C08 devin perfect logice: cunoastere categoriala (C05) +
   numerica (C06) + temporala (C07) + relationala (C08).
4. Coerenta cap-coada SCARA: progresie de maturizare cognitiva a
   operatorului (datele exista -> operatorul intelege -> interpreteaza ->
   transmite -> orchestreaza). Fiecare treapta are identitate cognitiva
   distincta.
5. Brand-fit superior:
   - B2C: "Dupa Trainity, CUNOSTI ce ai in date" >> "CALCULEZI ce ai".
   - B2B: precizie semantica, vocabular brand existent ("operatorul cunoaste
     setul" deja apare in vocabular brand §4).
   - Marketing: aliniere cu "construim sistem", "operam augmentat",
     "deciziile vin din date cunoscute".
6. MOTTO C05 "Un set cunoscut. Apoi orice decizie." se leaga PERFECT cu
   numele nou T2 CUNOASTERE. Coerenta interna.

Alternative C respinse (cu motivatie):
- CARTOGRAFIERE: poetic, dar parțial (T2 e mai mult decat harta).
- CATALOGARE: prea ingust (doar C05).
- CLARIFICARE: slab conceptual.
- CARACTERIZARE: academic, greoi.
- CONTEXTUALIZARE: corporate, gresit (T2 nu pune in context, descopera).
- CONSTATARE: pasiv (operatorul activ in T2, nu constata).
- CITIRE: prea usor (T2 nu e doar citire, e profilare).
- CALIBRARE: metoda, nu continut.

PROPAGARE OBLIGATORIE (de Bogdan, dupa chat SPEC C05):

A. In SISTEM_TRAINITY.md: actualizate 6 referinte T2 CALCUL la
   T2 CUNOASTERE (in acest chat). Mentiuni istorice de redenumire
   pastrate intentionat in 3 locuri (L139 + 2 note "fost T2 CALCUL").

B. In project knowledge (de actualizat de Bogdan):
   - 01_Brand_Trainity.docx (vocabular brand §4, mentiuni SCARA)
   - 05_Sistem_Excel_Trainity.docx (pricing grid B2B, structura SCARA)
   - 06_Pack_Excel_Trainity.docx (B2C structura)
   - Toate documente strategice care mentioneaza SCARA

C. In landing pages live:
   - trainity.ro/excel-sistem (B2B): textul care prezinta SCARA
   - trainity.ro/excel-pack (B2C): idem

D. In livrabile C01 existente (puntea NEXT C05 / lista trepte):
   - HTML-Studiu-Excel-01-Structura.html: pas 18 caseta NEXT
   - HTML-Video-Excel-01-Structura.html: idem ecran final
   - PPT-Excel-01-Structura.pptx: slide finale
   - FILM-Excel-01-Structura.docx: scenariu final
   NOTA: "INAINTE DE ORICE CALCUL" din hero C01 RAMANE (e substantiv comun
   "calcul" = operatie tehnica, NU numele treptei).

E. In viitoarele livrabile C02-C20: scrise direct cu T2 CUNOASTERE,
   nu necesita modificari.

F. In motorul de generare livrabile: brain.md + generatoare/ - verificat
   dupa C05, daca exista hardcode "T2 CALCUL" se inlocuieste cu
   "T2 CUNOASTERE".

Decizia se aplica de la data 25.05.2026 incolo. Toate livrabilele
generate dupa aceasta data folosesc denumirea noua.

**Lectie L140 codificata (25.05.2026, chat SPEC C05, decizie Bogdan):
ORDINEA NARATIVA FLOW SPEC FREEZING - regula permanenta, OBLIGATORIE,
verificata la fiecare SPEC FREEZING C{NN} pentru C05-C20.**

Problema descoperita: la SPEC C05 motorul a propus elementul 9 FENOMENE
amestecat conceptual cu elementul 2 PROBLEMELE. A tratat FENOMENE
semantic ("ce se intampla in set"), in loc de operational ("ce vede
operatorul cu cifre concrete in fisier"). Confuzia s-a clarificat doar
cand Bogdan a intrebat "nu am ales deja cele 5 probleme?".

REGULA L140 OFICIALA:

ORDINEA EXACTA a celor 9 elemente SPEC C{NN} (NU se ocoleste, NU se
inverseaza fara abatere constienta documentata):

```
1. INTRIGA          (paradox initial, ATENTIE)
2. PROBLEMELE       (5 din 10 intrebari concrete, RECUNOASTERE)
3. MIZA             (consecinta lipsei, TENSIUNE)
4. MANTRA           (formula sistemului, PROMISIUNE)
5. MOTTO            (regula interna post-constructie, SEMNATURA)
6. STEP-TITLES      (18 pasi cap-coada, schelet operational)
7. PROMPTURI        (2 prompturi Copilot, accelerator procedural)
8. FINAL-LABELS     (8 etichete payoff-block CAPS, memorabilitate)
9. FENOMENE         (5 din 10 anomalii/observatii FIZICE cu cifre
                    concrete in fisier, anomaly-grid HTML)
```

DEFINITII DISTINCTE (cele mai des confundate):

PROBLEMELE (pozitia 2) =
- Intrebari pe care si le pune operatorul
- Formulate ca text complet ("Cati clienti unici am?")
- Recunoastere emotionala ("da, am asta")
- Pozitionate dupa INTRIGA in flow narativ
- Sunt 5 alese din 10 propuse de motor

FENOMENE (pozitia 9, BLOC 14 canonic R-V01.x) =
- Anomalii / observatii FIZICE plantate / descoperite in setul de date
- Formulate ca titlu scurt CAPS + cifra concreta ("47 CLIENTI", "3 BUCURESTI")
- Influenteaza generarea INPUT.xlsx (datele se construiesc sa le contina)
- Devin anomaly-grid 5 cards in HTML dupa exec-hero
- Sunt 5 alese din 10 propuse de motor, cu variatie de natura

Cele doua sunt COMPLEMENTARE, NU substituibile:
- PROBLEMELE creeaza recunoasterea ("am intrebari fara raspuns")
- FENOMENE creeaza revelatia ("uite ce e in fisier dar nu vezi")

ABATERI CONSTIENTE POSIBILE (cu documentare explicita):

L140.A - SPEC C05 chat 25.05.2026: PROBLEMELE inghetate INAINTEA INTRIGEI
(pozitia 2 inainte de pozitia 1). Motiv: Bogdan a cerut explicit "lucram
PROBLEMELE intai, INTRIGA dupa, 10 propuneri individuale acceptat".
Motorul a confirmat cu Bogdan abaterea inainte de executie. Documentata
ca abatere unica, NU regula.

In general: motorul propune ordinea oficiala. Daca ARHITECT cere alt
order, motorul confirma explicit "aceasta e abatere de la R-V03.56,
confirmi?" inainte sa execute.

REGULA DE VERIFICARE MOTOR (anti-confuzie):

Inainte de a propune grila SPEC FREEZING pentru elementul N (1-9):
1. Motorul citeste DEFINITIA elementului N din SISTEM_TRAINITY.md
   (linia 1142-1159 pentru INTRIGA-MIZA-MANTRA-WOW-MOTTO,
    linia 1081-1115 pentru BLOC 14 FENOMENE,
    linia 2754-2780 pentru PROBLEMELE / V24 recodificare)
2. Motorul verifica ca propunerea respecta DEFINITIA elementului N,
   NU este preluata din alt element.
3. Daca propunerea seamana cu un alt element deja inghetat, motorul
   recheamă atentia ARHITECTului: "asta seamana cu PROBLEMELE deja
   inghetate, sigur vrei FENOMENE diferite?"

CUVINTE-CHEIE care semnaleaza CONFUZIE elemente:

| Element | Cuvinte tipice (corecte) | Cuvinte tipice (gresite, semnal confuzie) |
|---------|--------------------------|-------------------------------------------|
| PROBLEMELE | "Cati / Care / Cum / Exista" intrebari | titlu CAPS, cifra, anomaly-grid |
| FENOMENE | titlu CAPS 1-3 cuv + cifra concreta | "Cati / Care" intrebari |
| INTRIGA | propozitie paradoxala scurta | listă, schemă |
| MIZA | propozitie consecinta / castig | titlu CAPS, formula |
| MANTRA | propozitie formula repetabila | listă verbe |
| MOTTO | semnatura mentala post-constructie | filosofie universala |
| STEP-TITLES | 18 verbe imperative scurte | propozitii descriptive lungi |
| PROMPTURI | text natural conversational | comenzi imperative tehnice |
| FINAL-LABELS | 8 cuvinte CAPS telegrafice | propozitii intregi |

Aceasta lectie a costat 1 iteratie de confuzie in chat SPEC C05
(25.05.2026). Codificata aici ca regula permanenta de prevenire
pentru C06-C20.

---

**Reguli pentru cele 3 variante (neschimbat fata de V23):**

1. **Toate trei TREBUIE sa fie creative**, nu generice. Una poate fi
   mai abstract, una mai concreta, una mai poetic - dar toate trei
   sa fie *propuneri reale*, nu placeholders.

2. **Toate trei TREBUIE sa respecte brand Trainity** §4: vocabular
   permis, zero em-dash, ritm punch, fara productivitate, fara hype AI.

3. **Toate trei TREBUIE sa fie diferite ca abordare**. Daca toate
   propun acelasi unghi, nu sunt variante - sunt clone. Asigura
   diversitate REALA:
   - A: o directie pedagogica/conceptuala
   - B: o directie emotional/concreta
   - C: o directie poetica/aforistica

4. **Daca ARHITECT scrie "alte 3"**, motorul genereaza 3 noi variante,
   diferite ca abordare fata de prima rundă. Maxim 3 runde - dupa
   9 variante, ARHITECT alege sau formuleaza singur.

5. **ARHITECT poate combina:** "vreau A dar cu finalul din B". Motorul
   reformuleaza pe loc si confirma.

6. **ARHITECT poate edita:** "varianta A, dar 'paseaza' inlocuit cu
   'pasueaza'". Motorul accepta modificarea.

**Comportament motor:**

Dupa fiecare element inghetat, motorul confirma SCURT:
> "INGHETAT [ELEMENT]: '[textul ales/editat]'. Trec la intrebarea
> {N+1}/8: [URMATORUL_ELEMENT]."

La final (toate 8 elemente inghetate), motorul consolideaza intr-un
bloc SPEC formatat ca C04, gata de inserat in SISTEM_TRAINITY.md.

**Exemplu concret (intrebarea 1 din 8 pentru C05 INTRIGA):**

```
Intrebarea 1 din 8: INTRIGA

INTRIGA este paradoxul/provocarea care deschide constructia. Are rol
psihologic de ATENTIE - trezeste curiozitate tensionata.

La C04 INTRIGA era: "Daca trebuie sa repari din nou, nu ai construit
sistemul."

Pentru C05 (Clasificarea datelor), iata 3 propuneri creative:

A. "Cu date curate dar fara clase, totul pare la fel de important.
    Adica nimic nu este."
    [Pedagogic: paradoxul egalitatii anuleaza importanta]

B. "Datele tale sunt curate. Acum gandeste cine iti plateste chiria."
    [Concret/emotional: forteaza recunoasterea ca nu toti clientii
     sunt egali]

C. "2000 de randuri perfecte. Si nici unul nu spune ce conteaza."
    [Aforistic: contrast volum/lipsa de directie]

Alege A, B sau C. Daca niciuna nu te convinge, scrie "alte 3".
```

**Lectie L131 codificata:** Convenția SPEC FREEZING V14-V17 (3 variante
creative) era buna empiric dar nu codificata BLOCANT in SISTEM. S-a
pierdut tacut cand motorul a fost retrainat pe versiunile V19-V22.
Solutie aceeasi ca L129: regulile evidente trebuie codificate
explicit cu format exemplificat (nu doar text). 

Aceasta lectie e a treia oara (L129 SPEC INGHETAT, L131 FORMAT GRILA)
cand o regula veche se pierde. Trebuie un mecanism de "ARHEOLOGIE
TRAINITY" - cand un user observa "asa era inainte, s-a pierdut",
regula veche e codificata IMEDIAT cu blocaj/format explicit, nu doar
text descriptiv.

**Lectie L132 codificata:** Motorul propune, ARHITECT-ul decide. Asta
e principiul fundamental ARHITECT/CONSTRUCTOR. Cand motorul intreaba
"care e INTRIGA ta?" forteaza ARHITECT-ul sa fie creator pe loc - inverseaza
rolurile. Motorul ar trebui sa fie creator (propune), ARHITECT-ul
selector (alege/respinge). Variantele in grila respecta acest principiu.

---

**R-V03.55 SPEC INGHETAT BLOCANT INAINTE DE GENERARE [V22]:**

**Problema descoperita V21->V22:** Bogdan a deschis chat CONSTRUCTIE 05
cu OUT-V21.zip si a dat comanda "Genereaza CONSTRUCTIA 05". Motorul
a inceput sa genereze - sa creeze Date_MASTER-C05.xlsx - fara ca
SPEC C05 sa fie inghetat. SPEC C05 are status `NEGENERAT` in
SISTEM_TRAINITY.md.

R-V03.51 (CHECKIN implicit la generare) spune "motorul citeste SPEC
C{NN}" dar nu spune ce se intampla cand SPEC nu exista. Motorul a
improvizat - eroare grava care strica regula veche a sistemului
Trainity.

**Regula corecta (acum codificata explicit BLOCANT):**

Inainte de orice generare (fie completa, fie partiala, fie doar pe
Date_MASTER), motorul VERIFICA daca SPEC C{NN} are status INGHETAT
in SISTEM_TRAINITY.md.

**Daca SPEC C{NN} are status:**
- `[Status: INGHETAT]` sau echivalent -> procedeaza la generare
- `[Status: NEGENERAT]` -> SE OPRESTE si raspunde:

  > "SPEC C{NN} are status NEGENERAT in SISTEM_TRAINITY.md. NU pot
  > genera constructia fara SPEC inghetat (R-V03.55).
  >
  > Inainte de generare trebuie inghetate impreuna cu ARHITECT:
  > 1. INTRIGA (provocarea naratiunii)
  > 2. MIZA (ce castiga cursantul)
  > 3. MANTRA (fraza-semnatura, raman cu cursantul)
  > 4. MOTTO (sub-hook)
  > 5. Cele 18 step-titles
  > 6. 2 prompturi Copilot
  > 7. 8 final-labels
  > 8. Eventuale fenomene/operatii specifice (planted contaminations
  >    pentru T1, coloane noi pentru T2-T5)
  >
  > Te rog deschide chat BRAIN dedicat SPEC C{NN} sau dam SPEC aici
  > impreuna inainte sa procedam la generare."

**Acest blocaj se aplica si daca Bogdan insista** ("genereaza chiar daca
nu ai SPEC"). Motorul refuza cu acelasi mesaj. NU se improvizeaza SPEC
in chat CONSTRUCTIE - asta strica unitatea pedagogica si genereaza
inconsistente intre constructii.

**Exceptie unica:** daca Bogdan scrie explicit "definim SPEC C{NN}
acum in acest chat", atunci motorul trece la modul SPEC FREEZING
(intrebari structurate pentru inghetare SPEC), apoi la generare. Dar
nu sare peste SPEC tacut.

**Lectie L129 codificata:** Regulile care sunt "evidente pentru
toata lumea" trebuie totusi codificate EXPLICIT cu mecanism de
verificare. R-V03.51 spunea "citeste SPEC C{NN}" - prea slab.
R-V03.55 spune "verifica status SPEC C{NN} si OPRESTE-TE daca e
NEGENERAT" - explicit blocant. Diferenta intre "stii sa faci" si
"esti fortat sa faci" e diferenta intre regula respectata 80% si
regula respectata 100%.

**Lectie L130 codificata:** Motorul cunoaste regulile sistemului
Trainity prin lectura WORKFLOW + SISTEM + KIT. Dar in stress (chat
nou, comanda directa, presiune de productie), motorul "uita"
regulile soft si urmeaza comanda literal. Solutie: regulile critice
nu pot fi soft. Trebuie sa aibe MECANISM DE VERIFICARE - script,
checklist, blocaj explicit. Asta inseamna sa pui regula in gate
sau in cod, nu doar in documentatie.

---

**R-V03.54 STRATEGIE LECTURA SELECTIVA PILOT VIDEO + COPY+MODIFY
PENTRU HTML-VIDEO (ANTI-CONTEXT-EXCEEDED) [V20]:**

**Problema descoperita V20:** chiar cu R-V03.52 (livrare incrementala),
chat-ul CONSTRUCTIE 02 V20 a esuat REPETAT cu "context window
exceeded". Cauza root: motorul citeste pilot HTML-Video (~800KB) +
HTML-Editor-Video (~800KB) la inceputul chat-ului pentru a le clone-a.
Plus CHECKIN integral (brain ~180KB, WORKFLOW, SISTEM, KIT, DATA-INSTR,
SCHEMA, Date_MASTER-initial ~165KB). Total context lectura: ~2.5MB
inainte de generare. Saturare fereastra inevitabila.

**Solutie V20:** strategia lectura selectiva + COPY+MODIFY:

1. **NU citi pilot Video integral.** Foloseste extragere selectiva:
   - Doar STRUCTURA JS STAGES (head -200 lines)
   - Doar CSS-ul de baza (.stage, .video-card)
   - Imagini base64: pre-citite din fisier direct prin bash, nu in context

2. **Pentru HTML-Video si HTML-Editor-Video, foloseste COPY+MODIFY:**
   - Bash `cp pilot/HTML-Video.html /tmp/HTML-Video-CNN.html`
   - Str_replace TARGETED pentru cele 18 step-titles, 6 stage-quotes,
     cover-title, footer, localStorage keys
   - Fisierul rezultat e ~99% pilot + ~1% identitate constructie noua
   - Costul de context = scriem ~18 str_replace-uri scurte, nu un fisier
     de 800KB

3. **Lectura selectiva la inceput chat CONSTRUCTIE:**
   - Pilot Studiu (~80KB): citeste integral
   - Pilot Editor-Studiu (~90KB): citeste integral
   - Pilot Video (~800KB): NU citi integral, doar primele 200 linii
   - Pilot Editor-Video (~800KB): NU citi integral
   - brain.md sectiunea PROMPT_CHAT_CONSTRUCTIE: citeste prima

**Document nou: `PROMPT_CHAT_CONSTRUCTIE.txt`** in radacina arhivei.

Acest fisier contine instructiuni IMPERATIVE pentru motor in chat
CONSTRUCTIE NN. Lectura PRIMA, inainte de orice altceva. Defineste:
- Strategia lectura selectiva pilot
- Livrarea incrementala obligatorie
- Strategia COPY+MODIFY pentru HTML-Video/Editor-Video
- Recovery la esec
- Comenzi acceptate

**Mecanism integrare:**

PROMPT_CHAT_NOU.txt (existent) include la inceput un bloc CRITICAL V20
care redirectioneaza motorul la PROMPT_CHAT_CONSTRUCTIE.txt cand chat
este pentru constructie.

**Lectie L126 codificata:** R-V03.52 (livrare incrementala) e necesara
dar nu suficienta. Cauza esuarii e DUBLA: livrare atomica + lectura
neselectiva pilot. R-V03.52 rezolva prima cauza, R-V03.54 rezolva a
doua. Sistemele care esueaza tehnic au de obicei mai multe cauze
suprapuse. Solutia nu e o singura regula, e un set de reguli
complementare.

**Lectie L127 codificata:** COPY+MODIFY e mai eficienta decat generare
de la zero pentru fisiere mari (>500KB) cu modificari mici (<5%
diferenta). Pentru Pack 02 Excel, HTML-Video difera intre constructii
prin: 18 step-titles, 6 stage-quotes, cover-title, footer, localStorage
keys. Total ~30 punctuale. COPY pilot + 30 str_replace = ~100KB context
in loc de 800KB.

---

**R-V03.53 GATE V20 — DISTINCTIE SHEET INPUT CONTAMINAT vs SHEET
OUTPUT CURAT pentru CONSERVARE SEMANTICA [V20]:**

**Problema descoperita V19:** la audit C03 V19, gate v19 a raportat
delta 7.61% pe sheet `Vanzari` (input contaminat). Bogdan a primit
alarmare falsa - delta era cauzata de 150 valori stocate ca text in
INPUT (lectia C03), care nu intra in SUM clasic. Conservarea semantica
era PERFECTA pe sheet `Vanzari_AUDIT` (output curat).

**Solutie V20:** gate v20 verifica conservarea valorii_neta vs
Date_MASTER-initial pe **sheet-ul OUTPUT corect**, nu pe sheet
`Vanzari` (care poate fi intentionat contaminat).

**Logica:**

Per constructie, gate v20 cunoaste numele sheet-ului OUTPUT canonic:
- C01 STRUCTURA: `Vanzari` (curatat de antet/subtotale)
- C02 CONTROL: `Vanzari` (marcaj, fara modificari valori)
- C03 AUDIT: `Vanzari_AUDIT` (curatat de contaminari invizibile)
- C04 NORMALIZARE: `Vanzari_Normalizat` (output dupa 10 Applied Steps)
- C05 CLASIFICARE: `Vanzari` (cu coloane noi adaugate)
- C06 KPI: `Vanzari` (cu marja adaugata)
- C07 LOGICA TEMPORALA: `Vanzari` (neschimbat) + sheets agregate
- C08: TBD

**Mecanism:**

Fisierul `referinte/DATA-INSTRUCTIUNI.md` extins cu o sectiune
**"SHEET OUTPUT CANONIC PER CONSTRUCTIE"** care contine maparea:

```
C01 -> Vanzari
C02 -> Vanzari
C03 -> Vanzari_AUDIT
C04 -> Vanzari_Normalizat
C05 -> Vanzari
C06 -> Vanzari
C07 -> Vanzari
C08 -> TBD
```

Gate v20 citeste aceasta mapare si verifica suma valoare_neta pe
sheet-ul OUTPUT, NU pe sheet `Vanzari` cand acestea difera.

**Daca sheet OUTPUT lipseste** (ex: constructia n-a livrat
Vanzari_AUDIT pentru C03), gate v20 raporteaza ERROR explicit:
"Sheet OUTPUT canonic pentru C{NN} ('Vanzari_AUDIT') LIPSA in
Date_MASTER-C{NN}.xlsx. Construc,tia nu poate demonstra
conservare semantica."

**Tolerante:**

- Delta < 0.01 lei (rotunjire) - automatic OK
- Delta 0.01 - 1% - OK (mici variatii tehnice)
- Delta 1% - 15% - OK doar daca declarat in DATA-INSTRUCTIUNI
  (ex: C04 elimina subtotale, delta declarat ~5%)
- Delta > 15% - FAIL automat

**Lectie L125 codificata:** Gate-ul prea strict pe input contaminat
poate genera alarme false care eroda increderea in sistem. Solutia
nu e relaxarea threshold-ului (asta mascheaza erori reale), ci
verificarea pe sheet-ul corect (output, nu input). Gate v20
distinge intre "ce a primit" si "ce livreaza" constructia.

---

**R-V03.52 LIVRARE INCREMENTALA OBLIGATORIE IN CHAT CONSTRUCTIE
(ANTI-CONTEXT-EXCEEDED) [V20]:**

**Problema descoperita V19→V20:** in chat CONSTRUCTIE NN, livrarea
atomica a celor 6 livrabile intr-o singura runda produce DOUA tipuri
de erori tehnice frecvente:

1. **"Claude's response could not be fully generated"** - limita
   tokens per raspuns depasita (HTML-Video cu base64 embed ~800KB,
   HTML-Editor-Video ~800KB)
2. **"Prompt is too long: context window exceeded"** - intreaga
   fereastra de context (200K tokens Opus 4.7) depasita dupa CHECKIN
   integral + retry-uri intermediare + generare livrabile

Empiric in sesiunea V19: C02 V19 a esuat REPETAT cu eroarea 2,
blocand complet generarea. C03 V19 si C04 V19 au reusit dar la limita.

**REGULA OBLIGATORIE V20:** motorul in chat CONSTRUCTIE NN livreaza
**CATE UN LIVRABIL PER MESAJ**, NU atomic toate 6.

**Ordinea OBLIGATORIE (de la mic la mare ca size in context):**

1. **MESAJ 1: Date_MASTER-C{NN}.xlsx** (cel mai mic, ~170KB binar
   dar redus in context)
2. **MESAJ 2: Creativ-Excel-{NN}-{slug}.txt** (~25KB text pur)
3. **MESAJ 3: HTML-Studiu-Excel-{NN}-{slug}.html** (~80KB)
4. **MESAJ 4: HTML-Editor-Studiu-Excel-{NN}-{slug}.html** (~90KB)
5. **MESAJ 5: HTML-Video-Excel-{NN}-{slug}.html** (~800KB, base64
   imagini)
6. **MESAJ 6: HTML-Editor-Video-Excel-{NN}-{slug}.html** (~800KB)
7. **MESAJ 7: gate_v19.py rulat + verdict + offer checkout
   constructie**

**Comportament motor:**

- Dupa fiecare livrare, motor confirma SCURT: "Livrat: {nume_fisier}.
  Continui cu livrabilul {N+1}/6 ({nume_urmator})."
- Procedeaza AUTOMAT la urmatorul fara sa astepte comanda Bogdan
- Daca un mesaj iese cu "could not be fully generated", motor retry
  AUTOMAT acel mesaj o singura data
- Daca al doilea fail consecutiv, **opreste** generarea si raporteaza:
  "Livrabil X esuat la generare. Restul livrabilelor pana acum: [lista].
  Cere comanda 'continua cu X' sau 'continua de la urmatorul'."

**Beneficii masurate:**

- Elimina 99% din eseu tehnic context-exceeded
- Permite recovery partial (daca pica HTML-Video, ai deja Excel +
  Creativ + 2 HTML-uri sigure)
- Reduce stres asupra Bogdan (nu mai trebuie sa salveze din retry-uri
  frenetice)

**Comportament Bogdan:**

- Nu mai trebuie sa scrie "livreaza fisier cu fisier" - e implicit V20
- Daca vrea pauza, scrie "asteapta" intre mesaje (motor opreste)
- Daca vrea sa sara peste un livrabil (ex: doar Studiu, fara Video),
  scrie comanda explicita inainte de generare:
  "Genereaza C05 doar HTML-Studiu si Date_MASTER"

**Lectie L124 codificata:** Context window al modelului (200K tokens)
e o limita REALA care nu se vede pana o atingi. Sistemele care
ignora aceasta limita esueaza tacut sau zgomotos in productie. R-V03.52
e o adaptare la realitatea infrastructurii Anthropic, nu o decizie
arhitecturala Trainity.

---

**R-V03.51 CHECKIN IMPLICIT LA GENERARE DIRECTA + ACCEPTARE VARIANTE
LINGVISTICE [V19]:**

Decizie ARHITECT Bogdan: la deschiderea unui chat nou CONSTRUCTIE cu
arhiva OUT-V{NN}.zip atasata, daca primul mesaj de la Bogdan este
direct **"Genereaza CONSTRUCTIA NN"** (fara CHECKIN explicit anterior),
motorul SE COMPORTĂ astfel:

1. Recunoaste comanda Genereaza ca implicand CHECKIN integral
2. Citeste TOATE documentele canonice din arhiva (brain.md, WORKFLOW,
   SISTEM, KIT-V19, DATA-INSTRUCTIUNI, SCHEMA-MASTER, pilot, IDENTITATE,
   COVER-CHECKLIST, creative_banana2, Date_MASTER-initial)
3. Confirma SCURT (1-2 randuri): "Am citit toate documentele si SPEC
   C{NN}. Procedez la generare."
4. Procedeaza imediat la generare (4 HTML + 1 Creativ + 1 Date_MASTER-C{NN})
5. Ruleaza gate_v19 automat (R-V03.45)
6. Daca PASS, ofera checkout constructie cu arhiva OUT-{NN}-V19-{TS}.zip

**VARIANTE LINGVISTICE ACCEPTATE (toate echivalente):**

Motorul recunoaste si trateaza identic orice formulare care contine
intentia "generare constructie NN":

- `Genereaza CONSTRUCTIA NN`
- `Genereaza CONSTRUCTIȚIA NN` (autocorrect mobil)
- `Genereaza constructia NN` (lowercase)
- `Generează construcția NN` (cu diacritice complete)
- `genereaza c{NN}`
- `genereaza C05` / `genereaza C{NN}`
- `genereaza constructia 5` / `genereaza constructia 05`
- Orice combinatie a celor de mai sus

**NN poate fi format:**
- `05` (cu zero leading)
- `5` (fara zero leading)
- `c05` / `C05`

Motorul **NU cere clarificare** pentru variante de scriere. Daca exista
ambiguitate reala (ex: "Genereaza constructia" fara numar), atunci cere
clarificare. Altfel, executa direct.

**Acelasi principiu pentru toate comenzile sistemului:**
- `CHECKIN CONSTRUCTIE NN` / `CHECKIN CONSTRUCȚIE NN` / `checkin constructie NN`
- `checkout constructie` / `checkout construcție`
- `checkout brain` / `CHECKOUT BRAIN`
- `CHECKIN BRAIN` / `checkin brain`

Cazul ortografic, diacriticele si autocorrect-ul mobil NU sunt
obstacole. Motorul recunoaste intentia, nu sintaxa stricta.

**Comanda `CHECKIN CONSTRUCTIE NN` ramane disponibila** ca prim mesaj
SEPARAT in chat, pentru cazurile in care Bogdan vrea sa:
- Modifice SPEC inainte de generare (ex: "schimba un step-title")
- Verifice manual ce documente au fost citite
- Cerere modificari speciale (ex: "Genereaza C05 fara HTML-Video")

**Implicit: Genereaza CONSTRUCTIA NN = CHECKIN + Genereaza** atomic.

Justificare: in 99% din cazuri Bogdan deschide chat doar pentru
generare. Confirmarea CHECKIN explicit era overhead inutil. Comanda
"Genereaza CONSTRUCTIA NN" se citeste mai natural si elimina 1 pas.

**Aplicabilitate similara pentru chat BRAIN:**

- **Daca chat BRAIN curent CONTINE deja o arhiva produsa (OUT-V{N}.zip
  livrata anterior in acelasi chat):** context-ul brain traieste in
  istoricul chat-ului. Bogdan NU trebuie sa re-atasaze OUT-V{N}.zip.
  Atasaza doar arhivele CONSTRUCTIE noi care necesita consolidare,
  apoi scrie `checkout brain`. Motorul:
  1. Foloseste brain-ul curent din context (NU re-citeste arhiva)
  2. Audit arhivele CONSTRUCTIE atasate cu gate_v19
  3. Codifica reguli noi / lectii noi
  4. Livreaza OUT-V{N+1}.zip incrementat

- **Daca chat BRAIN e NOU** (sesiune proaspata, context gol):
  Bogdan atasaza OUT-V{N}.zip (brain-ul ultim) + opțional arhive
  CONSTRUCTIE. Motorul citeste brain-ul integral (CHECKIN BRAIN
  implicit) si procedeaza la consolidare.

- **Comanda `CHECKIN BRAIN`** ramane disponibila explicit pentru
  investigare fara checkout (cand vrei sa vezi doar ce am inteles
  din arhive, fara sa generez o noua versiune).

**Lectie L122 codificata:** NU cere user-ului sa furnizeze context pe
care-l ai deja. Daca brain.md a fost livrat in acelasi chat ca
OUT-V{N}.zip, contextul e disponibil. A cere re-atașare e fricțiune
inutila si semn ca workflow-ul nu respecta principiul "userul nu
trebuie sa repete intentia care e oricum implicita" (L121).

---

**R-V03.50 GATE V19 SIMPLIFICAT CLASA 6 [V19]:**

Gate V18 verifica continuitate stricta cap-coada (suma valoare_neta vs
construc,tia precedenta). V19 simplifica:

CLASA 6 DATA-CONTINUITY verifica acum:
1. Sheet principal `Vanzari` exista
2. Schema canonica 14 coloane prezenta
3. Sheets auxiliare CLIENTI, PRODUSE, AGENTI, DEPOZITE prezente
4. **Nomenclatoarele IDENTICE cu Date_MASTER-initial** (count rows)
5. **Suma valoare_neta in range conservare semantica** vs initial
   (delta < 15% sau declarat in SPEC C{NN})

ELIMINAT din gate V19:
- Verificare ordine stricta coloane (acceptam coloane noi adaugate la
  capatul listei)
- Verificare cap-coada vs C{NN-1} (constructiile sunt independente acum)

**Lectie L117 codificata:** Cand o decizie arhitecturala (V18 cap-coada
strict) intra in conflict cu o decizie anterioara mai veche (R-V01.5
chat-uri paralele), trebuie revazuta. Onestitatea cere recunoasterea ca
V18 a fost o decizie buna in intentie dar gresita in implementare.
V19 corecteaza prin Date_MASTER-initial + independenta.

**Lectie L118 codificata:** Cele 3 optiuni propuse de Brain (DATA-PATTERN
script, OPT 2 hibrid, OPT 1 renuntare totala) au fost toate inferioare
fata de ce a propus ARHITECT-ul (Bogdan): "un set generic + modificari
specifice per constructie". Lectie pentru Brain: cand ARHITECT spune
ceva simplu, sa nu inteleg ca "naive" - de obicei simpla e mai buna.

---

**R-V03.47 SCHEMA CANONICĂ DATE_MASTER + DATE_MASTER PROGRESIV CAP-COADĂ [V18]:**

Schimbare arhitecturală majoră a Excel-urilor in sistemul Pack 02:
**eliminare pereche Input/Output duplicat, introducere Date_MASTER
progresiv unic per construcție.**

**Cauza schimbării:**

Auditul exhaustiv C02+C03+C04 V17 a relevat două probleme structurale:
1. **Schema diferită între construcții**: C02 folosea `data, cod_client,
   nume_client, ...` (14 col), C03 folosea `nr_factura, data_factura,
   client_nume, judet, ..., valoare_tva, moneda` (14 col diferite),
   C04 revenea la schema C02 ignorând C03. Sistemul nu era cap-coadă
   real, era un colaj.
2. **Inflație de duplicat**: fiecare construcție livra Date-Input +
   Date-Output cu ~90% conținut duplicat (sheets CLIENTI, PRODUSE,
   AGENTI, DEPOZITE copiate identic). Diferența reală: 1-2 sheets
   suplimentare + 2 coloane noi (C02), sau 0 schimbări de schema (C03).

**Soluția V18:**

1. **Schema înghețată** prin `referinte/SCHEMA-MASTER.md` (14 coloane
   canonice, sheet `Vanzari` invariant, sheets auxiliare CLIENTI/
   PRODUSE/AGENTI/DEPOZITE consistente). Toate construcțiile C02-C20
   folosesc aceeași schemă.

2. **Date_MASTER progresiv unic**: fiecare construcție livrează exact
   un fișier Excel `Date_MASTER-dupa-C{NN}.xlsx` care reprezintă
   starea universului de date după trecerea construcției NN.

3. **Continuitate cap-coadă reală**: Date_MASTER-dupa-C{NN-1} servește
   ca INPUT pentru construcția NN. Chat-ul CONSTRUCTIE NN primește în
   arhiva atașată fișierul produs de construcția precedentă.

4. **Cele 7 livrabile devin 6**: 4 HTML + 1 Creativ + 1 Date_MASTER.
   Eliminate: Date-Input-Excel-{NN}-{slug}.xlsx și Date-Output-Excel-
   {NN}-{slug}.xlsx (deprecated V18).

**Gate V18 CLASA 6 nouă: DATA-CONTINUITY**
Verifică schema canonică, sheets auxiliare prezente, ordine coloane,
schema cap-coadă vs precedentă (coloane se păstrează doar se adaugă),
conservare semantică suma valoare_neta (delta < 0.01 lei sau declarat
in SPEC).

**Impact construcții existente C02 V17, C03 V17, C04 V17:**
Aceste arhive rămân valide la nivel intern (HTML curate, livrabile
funcționale), dar NU sunt cap-coadă. Pot fi regenerate cu schema
canonică la nevoie pentru integrare reală în Date_MASTER progresiv.

**Lectie L113 codificată:** "Sistemul Trainity nu poate fi construit
ca o secvență de construcții independente." Fiecare construcție
trăiește într-un univers de date partajat. Verificarea integrității
unei construcții izolate este necesară dar nu suficientă. Gate-ul V16
verifica integritatea izolată; gate-ul V18 verifică și continuitatea
cap-coadă (gradele de libertate față de construcțiile vecine).

**R-V03.48 GATE V18 FILTRE ANTI-FALS-POZITIV [V18]:**

Gate V16 avea fals pozitive recurente care consumau timp de audit
manual. V18 codifică filtrele explicit:

- **CSS values whitelist**: valori în context `opacity:`, `transform:`,
  `scale()`, `translate()`, `rotate()` NU se raportează ca cifre business
  (R-V02.15)
- **Power Query whitelist**: termeni Microsoft canonici (Refresh All,
  Refresh, Applied Steps, Power Query, Power BI, Pivot Table,
  Architecture în context PQ, Text.Trim, Text.Clean, Text.Replace,
  Number.FromText, Date.From) NU se raportează ca engleză forbidden
- **Template literals JS**: `${...}` în HTML-Video render exclus din
  scanare similarity step-titles
- **Versionare pilot**: hash MD5 al pilotului raportat în output gate.
  Dacă pilotul se modifică tăcut, hash-ul se schimbă și apare în raport.

**Lectie L114 codificată:** Filtrele anti-fals-pozitiv nu pot trăi în
memoria audit-orului (în acest caz, în mintea Brain). Trebuie codificate
în gate, altfel se repetă la fiecare verificare.

---

**R-V03.46 NOMENCLATURĂ ARHIVE OUT-* (DECIZIE ARHITECT V17) [V17]:**

Toate arhivele produse de chat BRAIN sau chat CONSTRUCȚIE folosesc
prefixul `OUT-` (output). Formatele exacte:

**Chat BRAIN (`checkout brain`):**
```
OUT-V{NN}.zip
```
NN = versiunea brain (V01, V02, ..., V17, V18, ...).
Exemplu: `OUT-V17.zip`.

**Chat CONSTRUCȚIE (`checkout constructie`):**
```
OUT-{CC}-V{NN}-{YYYYMMDD_HHMMSS}.zip
```
- CC = numărul construcției (01-20)
- NN = versiunea brain de la care a plecat (citită din numele OUT-V{NN}.zip atașat)
- YYYYMMDD_HHMMSS = timestamp generare (data + ora) pentru unicitate

Exemplu: `OUT-04-V17-20260525_143055.zip` = construcția 04, generată cu
brain V17 ca sursă, la 25 mai 2026 14:30:55.

**Justificare timestamp:** Bogdan poate rula chat-uri CONSTRUCȚIE
paralele pentru aceeași construcție (testare, regenerare). Două arhive
cu același CC și V_N pot coexista; timestamp-ul distinge varianta
canonică și permite sortare cronologică alfabetică.

**Format vechi (DEPRECATED V17):**
- `CHECKOUT_VNN.zip` → înlocuit cu `OUT-V{NN}.zip`
- `CHECKOUT_FROM_VNN_CMM_TIMESTAMP.zip` → înlocuit cu
  `OUT-{CC}-V{NN}-{YYYYMMDD_HHMMSS}.zip`

Această nomenclatură e codificată ca prim element în WORKFLOW-CAP-COADA.md
(secțiunea "NOMENCLATURĂ ARHIVE"). Toate documentele V17+ folosesc
exclusiv formatul nou.

---

**R-V03.44 PROMPT-TEXT CLONE CHECK (TOLERANTA ZERO) [V16]:**
Pentru HTML-Studiu si HTML-Editor-Studiu, daca CNN != C01, prompt-text
(elementele cu class="prompt-text") NU pot fi identice cu pilot C01.
Toleranta ZERO: un singur prompt-text identic = eroare BLOCANTA.

Cauza codificarii: in C03 V14 si C04 V15, generatoarele au schimbat
prompt-LABEL dar au pastrat textul propriu-zis al promptului catre AI
din pilot C01. Aceasta zona e "invizibil vulnerabila la COPY-MODIFY"
pentru ca pare schelet tehnic reutilizabil, dar in realitate e cea
mai importanta zona didactica (acolo se demonstreaza ce intreaba
utilizatorul AI-ul, specific per constructie).

Verificarea ruleaza in cadrul R-V03.45 (gate v16), in CLASA 1
NO-CLONE GENERIC, cu threshold 0% pe zona prompt-text.

**R-V03.45 GATE V18 BLOCANT SI OBLIGATORIU INAINTE DE PRESENT_FILES [V16]:**

Inainte de orice present_files in chat CONSTRUCTIE NN, motorul DEVE
rula:

```bash
python3 generatoare/gate_v18.py NN livrabile_CNN/ pilot_C01_V12/
```

Exit code 0 = PASS, 1 = FAIL. Daca FAIL, motorul NU livreaza
fisierele, raporteaza erorile la Bogdan, cere regenerare in chat
curent. Repeat pana PASS.

**Aceasta regula NU admite exceptii.** Daca un chat CONSTRUCTIE
livreaza fara sa fi rulat gate-ul, Bogdan refuza arhiva si cere
refacere. Aceasta e diferenta fundamentala intre V15 (gate scris,
fisier in arhiva) si V16 (gate executat obligatoriu prin proces).

Gate v16 verifica 5 CLASE de erori (nu cazuri specifice):

1. **NO-CLONE GENERIC** — pentru fiecare zona textuala din lista
   TEXTUAL_ZONES (step-title, step-action, prompt-text, prompt-label,
   final-label, anomaly-card-desc, payoff-line, stage-quote,
   cover-subtitle, cover-miza), verifica similarity cu pilot C01 V12.
   Threshold per zona. La descoperirea unei zone noi vulnerabile,
   se adauga in TEXTUAL_ZONES, NU se codifica regula separata.

2. **IDENTITY** — cover-label, cover-title, meta-val-treapta, footer,
   topbar, localStorage, <title> conform IDENTITATE_TEHNICA C{NN}.

3. **BRAND** — zero em-dash, en-dash, engleza forbidden, vocab brand
   forbidden in text vizibil.

4. **CROSS-CONTAMINATION** — niciun cod CXX vizibil != CNN, cu
   exceptii legitime (next-section, predare).

5. **VOCE** — Studiu = persoana 2 sg, Video = persoana 3 plural.

R-V03.45 INLOCUIESTE R-V03.39 (gate_cross_contamination.py V15
deprecated, sters din arhiva V16).

**Filosofia V16 (lectia L108):** acoperim CLASE de erori, nu CAZURI
specifice. La descoperirea unei erori noi, intrebam "din ce CLASA
face parte?" si extindem verificatorul existent. Fix de cauza, nu
fix de simptom. Acest principiu transformeaza sistemul din "lista
de patch-uri" in "framework rezistent" pe masura ce ajungem spre C20.

---

## DOCUMENT PRINCIPAL: WORKFLOW-CAP-COADA.md

In radacina arhivei V16+ exista WORKFLOW-CAP-COADA.md. Acesta e
documentul principal al sistemului. Explica arhitectura BRAIN ↔
CONSTRUCTIE, comenzile, cele 7 livrabile, regula absoluta R-V03.45,
si ciclul de invatare DESPRE clase de erori (nu DIN cazuri).

Citeste-l la deschiderea oricarui chat BRAIN sau CONSTRUCTIE, INAINTE
de orice alta actiune. Daca exista conflict intre WORKFLOW si alte
documente, WORKFLOW castiga.

---

**SFARSIT SISTEM_TRAINITY.md (V06, 23 mai 2026: + R-V03.5 NOMENCLATURA UNIFICATA STUDY/VIDEO + EDIT (HTML-STUDY-Excel-NN-Nume.html + HTML-EDIT-STUDY-Excel-NN-Nume.html + HTML-VIDEO-Excel-NN-Nume.html + HTML-EDIT-VIDEO-Excel-NN-Nume.html). Storage keys aliniate: trainity_cNN_study_v1 + trainity_cNN_study_edits_v1 + trainity_cNN_video_v1 + trainity_cNN_video_edits_v1 + trainity_cNN_video_deleted_v1. Aplicat pilot C01: HTML-Excel.html -> HTML-STUDY-Excel.html, HTML-VIDEO-EDITABIL.html -> HTML-EDIT-VIDEO.html. HTML-EDIT-STUDY pentru C01 va fi creat ca pas urmator. Toate referintele in SISTEM + brain + comenzi + lifecycle EDITABIL actualizate la noua nomenclatura.) + + R-V03.4 VOCE NARATIVA DIVERGENTA COCKPIT vs BROADCAST (HTML cockpit + HTML-EDITABIL = persoana a 2-a singular catre cursant; HTML-VIDEO + HTML-VIDEO-EDITABIL = persoana a 3-a plural ca ghid colectiv. Aplicare obligatorie in HTML-VIDEO la title-uri pasi, instr-uri, hook, hero hook+sub, Switch title/sub, Step callout, Verify sub, butoane CTA Hero "Începem construcția →" si topbar "Mergem la pas sărit". Exceptii admise: PROMPTS.text si meta, butoane UI Validează, toast feedback, Final block persoana 1 plural, motto-uri fixe brand. La reformulari reflexive: asigură-te -> ne asigurăm; nu te uita -> nu ne uităm; lasă-l -> îl lăsăm. Aplicat pilot C01 cu 41 modificari atomice, pattern COPY-MODIFY R-V02.6 pentru C02-C20. R-V03.4 documentat in PARTEA E LIVRABILE + PARTEA XI motor pasul 4.) + HTML-VIDEO-EDITABIL al 8-LEA LIVRABIL CANONIC (paritate EDITABIL aplicata pe ambele moduri study si broadcast) + R-V03.3 EDITOR UNIVERSAL PE HTML-VIDEO (acelasi pattern WYSIWYG ca HTML-EDITABIL cockpit) + R-V03.2 EXTINS la 8 LIVRABILE + R-V01.2 EXTINS la 8 livrabile in present_files + SECTIUNEA E LIVRABILE actualizata la 8 fix ZERO PDF. Baza V04 pastrata: R-V03.1 matrita HTML-VIDEO broadcast (7 ecrane scenice, cod culori canonic, pas sarit, butoane fixe). Baza V03 pastrata: R-V02.14 + R-V02.15 + Gate 2 INVERSAT + livrabile C01-C04 INVALIDATE (regenerare necesara). Baza V02: SPEC C01-C04 inghetate, R-V02.0-R-V02.13. Baza V01: R-V01.2-R-V01.9, ANOMALY-GRID parametrizat, INTRIGA, EDITABIL automat, workflow paralel.)**
