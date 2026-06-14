# CLAUDE -> BRAIN C17

## STATUS
C17_BLUEPRINT_READY_FOR_REVIEW (SLUG + Blueprint propuse; SPEC 11-slot înghețat ca referință)

## SURSA
Mandat BRAIN `MANDAT_SLUG_BLUEPRINT_C17` (via sync). Pregătire SLUG + Blueprint, fără HTML / Date_MASTER / build / FILM / folder c17 / artefacte / fișiere sistem / C18. Doar design conceptual pentru review.

SPEC 11-slot înghețat (V76, commit 1438789, oglindit în Doc 14): HERO „Cum transform munca pe care doar eu o știu într-un sistem pe care altcineva îl pornește?" · BOMBĂ „Munca ta merge perfect. Până pleci tu." · GREȘEALA „Nu ai un proces. Ai o memorie personală care ține un Excel în viață." · AHA „O muncă făcută de două ori nu mai e o livrare. E un sistem ascuns în workbook." · MANTRA „Nu o fac din nou. O fac sistem." · WOW „...o hartă vie în workbook, pe care altcineva o pornește fără tine." · MOTTO „Pleci, și munca o reia altcineva." · CINE DEVII „...Ești omul care o face sistem." · PAYOFF „Acum poți lipsi o săptămână, și munca are cine s-o reia." · MIZA (director) · VERB a sistematiza.

---

## 1. SLUG FINAL PROPUS
- **Slug:** `Sistematizare` (din gerunziul canonic SISTEMATIZAREA).
- **Nume folder:** `c17/`
- **Nume fișiere (model C16/C09):**
  - `c17/HTML-Studiu-Excel-17-Sistematizare.html`
  - `c17/HTML-Editor-Studiu-Excel-17-Sistematizare.html`
  - `c17/HTML-Video-Excel-17-Sistematizare.html`
  - `c17/HTML-Editor-Video-Excel-17-Sistematizare.html`
  - `c17/Date_MASTER-C17.xlsx`
  - `c17/FILM-Excel-17-Sistematizare.docx`
  - `c17/assets/hero-poster-excel-17-sistematizare.jpg` + `exec-stage-1..6.jpg`
- **Titlu intern:** „C17 SISTEMATIZAREA"
- **Topbar label:** `C17 · SISTEM` (model `C{NN} · CUVÂNT`, CUVÂNT LOCKED = SISTEM)
- **hov-object (MIZA HERO afișat):** „SISTEMATIZAREA MUNCII RELUABILE"
- **hero-question:** „Cum transform munca pe care doar eu o știu într-un sistem pe care altcineva îl pornește?"
- **cover-title (titlu articol „Cum să..."):** „Cum să transformi o muncă pe care o repeți într-un sistem pe care altcineva îl poate relua"
- **Compatibilitate nomenclatură LOCKED V70:** slug derivă din SISTEMATIZAREA; CUVÂNT SISTEM (topbar); verb SISTEMATIZEZ; iese din OCAZIE. Aliniat 100%, zero deviație.

## 2. BLUEPRINT C17 (6 etape, 18 pași, 3/etapă)
Context: workbook-ul muncii „făcute o dată" (handoff C16) are foi-sursă (ex `Vanzari`, `Clienti`, `Calendar`), foi de lucru și o foaie-raport. Munca = procesul de a reproduce raportul din surse. C17 scrie foaia `_SISTEM` care cartografiază funcțional acest workbook ca proces reluabil.

### ETAPA 1 · „Munca pe care o știi doar tu" (REALITATE / before, OCAZIE)
Obiectiv: arăți că workbook-ul merge, dar reluarea trăiește în capul autorului. Ce se vede: foi împrăștiate, fără punct de intrare. Ce dovedește `_SISTEM`: încă nimic (stabilește problema author-only).
- 1.1 Deschizi workbook-ul; observi foile (surse/lucru/raport) fără ghid de pornire.
- 1.2 Încerci reluarea fără autor și te blochezi (care foaie prima? ce sursă? ce pas?) = dovada gâtuirii (OCAZIE).
- 1.3 Creezi foaia `_SISTEM` (goală), o fixezi ca prima filă; declari intenția: harta reluabilă. Workbook: apare foaia `_SISTEM`.

### ETAPA 2 · „Inventarul componentelor reale"
Obiectiv: cartografiezi componentele reale ca referințe vii. Ce se vede: blocul A, index cu hyperlink-uri + dimensiune live. Dovedește: componentele sunt navigabile (click -> foaia reală).
- 2.1 Construiești blocul A COMPONENTE: pentru fiecare foaie/tabel, `=HYPERLINK("#'Vanzari'!A1","Vanzari")`.
- 2.2 Adaugi oglinda dimensiunii: `=ROWS(TblVanzari)` / `=COUNTA('Vanzari'!A:A)` -> componenta se numără singură.
- 2.3 Marchezi rolul fiecărei componente (sursă / lucru / ieșire). Workbook: blocul A populat cu linkuri + oglinzi.

### ETAPA 3 · „O singură sursă pentru fiecare intrare"
Obiectiv: fixezi o singură sursă de adevăr per intrare. Ce se vede: blocul B, named ranges `SRC_` + oglindă rânduri. Dovedește: reluarea nu mai întreabă „care fișier?".
- 3.1 Pentru fiecare intrare, named range `SRC_<nume>` pe zona reală a sursei.
- 3.2 Oglinda `=ROWS(SRC_<nume>)` -> câte rânduri are sursa, live.
- 3.3 Elimini dublura: declari UNA canonică (anti-ambiguitate). Workbook: named ranges SRC_ create, bloc B populat.

### ETAPA 4 · „Ordinea de reluare, legată de obiecte"
Obiectiv: scrii secvența ca lanț navigabil legat de obiecte reale. Ce se vede: blocul C, pași cu hyperlink + OBJ_ + rezultat live. Dovedește: fiecare pas duce la obiectul real.
- 4.1 Numerotezi pașii; fiecare = `=HYPERLINK("#...")` la zona pasului.
- 4.2 Legi obiectul atins: named range `OBJ_<pas>` pe celula-cheie; opțional `=FORMULATEXT(OBJ_<pas>)` arată transformarea (fără s-o execute).
- 4.3 Legi rezultatul vizibil: referință live la celula de rezultat (oglindă, NU validare). Workbook: blocul C = lanțul de navigare, named ranges OBJ_.

### ETAPA 5 · „Cunoașterea scoasă din cap"
Obiectiv: externalizezi convențiile autorului ca parametri vii + definești cine poate relua. Ce se vede: blocul E (`PARAM_`) + blocul D (profil). Dovedește: reluarea nu mai depinde de memoria autorului.
- 5.1 Deciziile author-only (praguri de proces, convenții de denumire, alegeri) -> named ranges `PARAM_<nume>` cu valoarea în celulă.
- 5.2 Legi pașii de parametri: unde era „cum știu eu", acum referă `PARAM_x` (oglindă, nu regulă activă).
- 5.3 Scrii blocul D „CINE POATE RELUA": rol / competență minimă (ex „știe tabele structurate + XLOOKUP"), NU numele autorului. Workbook: named ranges PARAM_, blocuri D + E.

### ETAPA 6 · „Testul substitutului"
Obiectiv: confirmi reluabilitatea + marchezi granița C17->C18. Ce se vede: START AICI + punct de reluare + zona test anti-SOP. Dovedește: reluabil fără autor; harta moare scoasă din workbook.
- 6.1 Construiești zona START AICI (hyperlink la primul pas) + punctul de reluare (unde reintri dacă te-ai oprit).
- 6.2 Testul substitutului pe viu: altcineva pornește din `_SISTEM`, parcurge lanțul, reia munca fără autor.
- 6.3 Marchezi granița C17->C18: pașii repetitivi etichetați „candidat C18" (NEautomatizați); zona test anti-SOP. Workbook: zone START/reluare/graniță finalizate.

## 3. ARTEFACT `_SISTEM` (structură concretă)
Foaie `_SISTEM`, prima filă a workbook-ului. Antet: titlu + „START AICI" (hyperlink la primul pas).

| Bloc | Coloane | Formule vii / obiecte |
|---|---|---|
| **A · COMPONENTE** | Componentă (link) · Rol în proces · Dimensiune live | `HYPERLINK` intern · `ROWS`/`COUNTA` |
| **B · SURSE** | Intrare · Sursă unică · Există/rânduri | named range `SRC_*` · `ROWS(SRC_*)` |
| **C · PAȘI (ordine reluare)** | # Pas · Acțiune (link) · Obiect atins · Transformare · Rezultat vizibil · Candidat C18? | `HYPERLINK` -> `OBJ_*` · `FORMULATEXT(OBJ_*)` · referință live (oglindă) |
| **D · CINE POATE RELUA** | Rol · Competență minimă | text (profil, NU nume) |
| **E · PARAMETRI** | Parametru · Valoare live · Folosit la pasul | named range `PARAM_*` |
| **F · PORNIRE / RELUARE + GRANIȚA** | START AICI · Punct de reluare · Listă „candidat C18" · Test anti-SOP | `HYPERLINK` · etichete |

- **Named ranges:** `SRC_*` (surse) · `INPUT_*` (zone introduse de operator) · `PARAM_*` (convenții) · `OBJ_*` (obiecte atinse).
- **Formule vii:** `HYPERLINK` (navigare) · `ROWS`/`COUNTA` (oglinzi dimensiune) · `FORMULATEXT` (oglindă transformare) · referințe directe (oglindă rezultat).
- **Zona START AICI:** hyperlink la primul pas. **Punct de reluare:** hyperlink la pasul curent. **Zona test anti-SOP:** oglindă care depinde de celelalte foi (se rupe dacă le ștergi).
- **Ce NU are voie să conțină `_SISTEM`:** macro / Power Query / Refresh / butoane care EXECUTĂ pașii (= C18) · reguli / praguri / validări / conditional formatting de alertă / IF de eroare care JUDECĂ (= C19) · ownership / responsabil / escaladare / RACI (= C20) · proză de procedură independentă de obiectele reale (= SOP) · descrierea raportului / dashboard-ului (= T4) · cifre business statice fără sursă (cifrele trăiesc în surse, oglindite).

## 4. TESTE
- **Anti-SOP:** șterge celelalte foi -> `_SISTEM` se umple de `#REF!` / `#NAME?` / linkuri moarte (HYPERLINK moarte, `ROWS(SRC_*)` -> #REF!, `FORMULATEXT` -> #REF!). PASS = inutilizabil scos din workbook. FAIL = util copiat în Word.
- **Substitut:** rol instruit pornește din START AICI, navighează lanțul, reia munca fără autor.
- **Anti-C18:** zero macro/Refresh/Power Query; pașii cer un OM; „candidat C18" = doar etichetă.
- **Anti-C19:** zero praguri/validări/alerte; oglinzile DOAR afișează starea, nu o judecă.
- **Anti-C20:** zero ownership/escaladare; doar profil de capabilitate (bloc D).
- **Filmabilitate 8-12 min:** before (etapa 1) -> construiești blocurile A-F live, named ranges + linkuri + oglinzi care se aprind (etapele 2-5) -> substitut pe viu (etapa 6). Acțiune Excel, zero teorie.

## 5. CONTINUITATE
- **Primește din C16:** procesul care a produs raportul (pași, surse, decizii), ca act author-only.
- **Predă la C18:** harta `_SISTEM` cu pași etichetați „candidat C18"; C18 ia pașii repetitivi și-i scoate din execuția umană.
- **Unde se oprește înainte de automatizare:** `_SISTEM` descrie pașii ca acțiuni de OM; NU automatizează niciun pas (eticheta „candidat C18" e limita).
- **Granița C19:** `_SISTEM` nu pune reguli care prind erori (oglindă, nu gardian). **Granița C20:** spune cine POATE relua, nu cine DEȚINE.

## 6. RISCURI
- **SOP:** blocurile devin proză. Mitigare: totul legat prin HYPERLINK/named ranges/formule vii + test anti-SOP.
- **C18:** apare execuție. Mitigare: garda OGLINDĂ + „candidat C18" doar etichetă.
- **C19:** oglinzile devin validări. Mitigare: oglindă afișează, nu judecă; zero conditional alert.
- **C20:** apare ownership. Mitigare: bloc D = capabilitate, nu desemnare.
- **T4:** descrie raportul. Mitigare: obiect = procesul, niciun slot despre raport.
- **Ecou C08 prin „hartă":** folosesc „hartă reluabilă a muncii/workbook-ului", NU verbul „a cartografia" ca identitate. C08 = ecosistem de date; C17 = proces de muncă. Context disjunct.
- **Generic:** step-titles + blocuri specifice C17 (SRC_/OBJ_/PARAM_), nu titluri generice; lecția „titluri exec identice 8/8" respectată.
- **Film static:** filmezi CONSTRUIREA live (named ranges, linkuri care se aprind) + substitut pe viu, nu tastare de procedură.

## 7. VERDICT
SLUG aliniat 100% la nomenclatura LOCKED. Blueprint 6 etape / 18 pași, fiecare cu acțiune Excel proprie (non-generic), ancorat în `_SISTEM` nativ-Excel. Artefact `_SISTEM` definit la nivel de blocuri/coloane/formule/named ranges, cu lista „ce NU are voie" (anti C18/C19/C20/SOP/T4). Teste + continuitate + riscuri acoperite. Garda OGLINDĂ + OCAZIE + anti-SOP la fiecare nivel.

**C17_BLUEPRINT_READY_FOR_REVIEW**

## SPEC 11-slot (înghețat, referință)
Vezi V76 / Doc 14 STARE DE IMPLEMENTARE / BRAIN-TO-CLAUDE. MOTTO: template de treaptă T5 „Pleci, și munca [...]" = CANDIDAT (nu LOCKED), se retestează la C18/C19/C20.
