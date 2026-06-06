# TRAINITY_ARCHITECTURE_BIBLE.md · Sursa UNICĂ de reguli (T2-T5)

> **STATUT: NORMĂ. SURSĂ UNICĂ DE ADEVĂR.** Orice regulă se enunță integral AICI.
> Detector și Release Gate o REFERĂ prin ID, nu o re-enunță.
> Structură: **§SHARED RULES** (toate treptele) + **§TIER RULES** (per treaptă).
> Pornirea unei trepte noi = moștenești §SHARED + scrii o secțiune §TIER nouă.

---

# §SHARED RULES (se aplică la TOATE treptele, T2-T5)

## REGULI SACRE (nu se încalcă fără aprobarea arhitectului)
- **S1 · Un singur scop per construcție.** O construcție răspunde la O SINGURĂ întrebare.
- **S2 · Garda de treaptă.** Fiecare construcție stă în competența treptei ei; nu predă
  competențe ale treptei următoare, nu reia treapta anterioară. *(Conținutul gărzii =
  în §TIER, pentru că diferă pe treaptă.)*
- **S3 · Invariant de valori sursă.** valoare_neta conservată cap-coadă (R-V02.14);
  zero cifre business în HTML/FILM (R-V02.15).
- **S4 · Schelet fix.** 6 etape · 18 pași · 5 fenomene · 8 verificări finale · 2 prompturi.
- **S5 · Identitate locked.** AHA + numele construcției nu se schimbă fără aprobare.

## REGULI DE PORNIRE A UNEI TREPTE (TIER SEED)
- **R-SEED-1 · Prima construcție = mod TIER SEED.** Moștenește §SHARED, definește §TIER
  (identitate + gardă), sare verificările cross-construction. · CRITICĂ · Obligatorie.
  · Procedura: vezi `TRAINITY_OPERATING_SYSTEM` §TIER SEED.
- **R-SEED-2 · DNA + Position Matrix = post-2-construcții.** Nu se forțează pe prima
  construcție a treptei; se creează retroactiv după a 2-a. · CRITICĂ · Obligatorie.
- **R-SEED-3 · Schelet moștenit, identitate diferită.** O treaptă nouă MOȘTENEȘTE
  scheletul (S4) dar IDENTITATEA ei DIFERĂ de treapta anterioară. Consistența
  structurală = cerută; consistența de identitate = INTERZISĂ. · CRITICĂ · Obligatorie.
- **R-TIER-PARAM · Detector și Gate sunt tier-aware.** Lista de „termeni interziși" e a
  treptei curente (din §TIER), nu hardcodată. Ce e contaminare într-o treaptă e
  competență în alta. · CRITICĂ · Obligatorie.

## REGULI STRUCTURALE (SHARED)
- **R-STR-1 · Cele 6 etape canonice.** REALITATE→INVESTIGAȚIE→TRANSFORMARE→VERIFICARE→
  STABILIZARE→CONFIRMARE, ordine și roluri fixe. · CRITICĂ. · Neconform: 5/7 etape.
- **R-STR-2 · 3 pași/etapă (18 total).** · CRITICĂ.
- **R-STR-3 · 5 fenomene SCENA.** · MEDIE.
- **R-STR-4 · Meniu mobil fără bandă nav-brand** (R-V03.73, automat). · MEDIE.

## REGULI TERMINOLOGICE (SHARED)
- **R-TERM-1 · Etapa 4 = „VERIFICAREA [obiect]".** Niciodată „AUDIT" (= ADN C03). ·
  CRITICĂ. · Conform: „VERIFICAREA CRONOLOGIEI". · Neconform: „AUDIT AL REGULILOR".
- **R-TERM-2 · phase-tag E5 = „RECALCUL".** Niciodată „RECALC". · MEDIE.
- **R-TERM-3 · „auditabil" permis** (adjectiv = verificabil; nu se confundă cu „AUDIT").
- **R-TERM-5 · Fără ecouri C04** („Suma rămâne conservată/martorul de sumă") în copy;
  conservarea trăiește în Excel (S3). · MEDIE.
- **R-TERM-6 · Fără em/en-dash** (R-V03.72, automat). · MEDIE.
- **R-NAME-1 · Nume construcție = LOCK.** Numele istorice (TIPIZARE etc.) abandonate. · CRITICĂ.
- **R-TEASER-1 · Teaserul poate numi construcția+treapta următoare**, inclusiv termeni ai
  treptei superioare, dacă e explicit „C0(N+1) deschide...". NU contaminează. · Clarificare.

> **NOTĂ:** interdicțiile terminologice CONCRETE (ce termeni sunt interziși) trăiesc în
> §TIER, pentru că diferă pe treaptă (R-TIER-PARAM). §SHARED stabilește doar disciplina.

## REGULI PEDAGOGICE (SHARED)
- **R-PED-1 · Etapa 3 e AI-assisted.** type-tag E3 = „Promptul 2"; formula = output-ul
  promptului, nu muncă manuală. · MAJORĂ.
- **R-PED-2 · Două prompturi AI/construcție** (Promptul 1 etapa 2, Promptul 2 etapa 3). · MEDIE.
- **R-PED-3 · Promptul = interogare, nu execuție.** · Recomandată.

## REGULI METODOLOGICE (SHARED)
- **R-MET-1 · Etapa 4 verifică, nu construiește.** Pașii E4 CONFRUNTĂ/VERIFICĂ/MARCHEAZĂ;
  nu construiesc livrabilul. · MAJORĂ. · *Încălcată azi de C06 (E4 construiește) → decizie
  arhitecturală deschisă.*
- **R-MET-2 · Verificare prin confruntare cu setul** („Nu avem încredere oarbă..."). · MEDIE.
- **R-MET-3 · Funcții de verificare pe axă = variație acceptabilă** (UNIQUE vs MIN/MAX vs
  COUNTIF, după tipul de date). · Clarificare.

## REGULI DE HANDOFF (SHARED)
- **R-HAND-1 · Intrare explicită.** PAS 01: „Setul predat de C0(N-1) [stare]". · MAJORĂ.
- **R-HAND-2 · Ieșire + teaser.** „Predă către C0(N+1)... C0(N+1) deschide [axa]." · MEDIE.
- **R-HAND-3 · Stare moștenită corectă.** · Obligatorie.

## REGULI PHASE-TAG / COMPLETION (SHARED)
- **R-PHASE-1 · Phase-tags fixe:** E1=INPUT, E2=AI, E4=CONTROL, E5=RECALCUL, E6=PAYOFF. · MEDIE.
- **R-PHASE-2 · E3 phase-tag variabil pe axă** (din familia transformării). · *decizie deschisă:
  Power Query trage spre treaptă superioară.*
- **R-COMP-1 · completion-title = „[Livrabil] validat"**, fără adjective suplimentare. · MEDIE.

---

# §TIER RULES

## §T2 — CUNOAȘTERE (descrie, nu interpretează)
- **Axă:** setul devine CUNOSCUT. C05 vocabular · C06 sens · C07 calendar · C08 context.
- **Întrebări:** „Ce există?" / „Ce înseamnă fiecare rând?" / „Când se întâmplă?" / „Cu cine se leagă?"
- **GARDA T2/T3 (lista de interziși pentru R-TIER-PARAM):** trend, performanță, prioritizare,
  decizie, comparație, „cel mai mare/mic", dominant, prioritar/strategic/critic, join, Data
  Model, XLOOKUP/LOOKUP ca aducere, „conectat/conexiune", Power Query (ca operațiune),
  BI-ready, KPI. Toate = T3/T4. · Excepție: teaser explicit (R-TEASER-1).
- **AHA locked:** C05 „Nu cunoști un set până nu-l poți enumera." · C06 „Un rând nu are
  sens până nu primește o regulă." · C07 „Un set fără poziție în timp e un set fără
  memorie." · C08 „Cele mai importante date despre un rând nu sunt în rând."
- **Detaliu complet:** `_system/11-ARHITECTURA-CONCEPTUALA-T2.md` (autoritate conceptuală T2).

## §T3 — ANALIZĂ (inițiată prin TIER SEED la C09 · aprobat ARHITECT V58)
- **Axă:** setul cunoscut (T2) devine INTERPRETAT. T3 = ANALIZĂ.
- **Ce produce T3:** relații reale, măsuri, comparații, interpretare; răspuns la „de ce /
  cât / care e mai mare / care e mai bun".
- **Ce NU produce T3:** vizualizare/dashboard/raport (= T4 RAPORTARE), sistem care rulează
  și se autoguvernează fără autor (= T5 AUTONOMIE).
- **Lanț (LOCKED la îngheț C09, V66):** C09 RELAȚII · C10 MĂSURI · C11 COMPARAȚII · C12 INTERPRETARE.
- **Întrebări (verbul de treaptă, LOCKED):** C09 răspunde · C10 măsoară · C11 compară · C12 explică.
  Forma narativă: C09 „Ce pot întreba?" · C10 „Cât?" · C11 „Care?" · C12 „De ce?"
- **GARDA T3/T4-T5 (lista pentru R-TIER-PARAM):**
  - **PERMIS** (competența T3, era INTERZIS în T2): join, Data Model, relații 1:M, merge,
    măsuri/agregări peste model, comparații, trend, performanță, „cel mai mare/mic",
    „care e mai bun", interpretare, citire cross-tabel.
  - **INTERZIS** (= T4/T5): dashboard, vizualizare, grafic publicabil, raport (T4); decizie
    automată, alertă, acțiune, recomandare executată (T5).
- **AHA locked (S5):** C09 „Fără relații ai date. Cu relații ai răspunsuri."
- **NOTĂ inversiune:** termenii din garda §T2 (join/Data Model/trend/„cel mai mare") sunt
  AICI competență, nu contaminare. Detectorul tier-aware (R-TIER-PARAM) îi tratează corect.

### §T3 · GRAMATICA DE TREAPTĂ (LOCKED la îngheț C09, V66)
Regula care ține cele 4 construcții T3 coerente și ne-contaminate. Două categorii de slot:
- **SLOT DE TREAPTĂ (generic, identic ca formă la toate 4):** MOTTO = template
  „Întrebi [WH]. Modelul [verb]." → C09 „Întrebi o dată. Modelul răspunde." ·
  C10 „Întrebi cât. Modelul măsoară." · C11 „Întrebi care. Modelul compară." ·
  C12 „Întrebi de ce. Modelul explică." Verbul de treaptă (întreb/răspund) trăiește AICI.
- **SLOT DE CONSTRUCȚIE (poartă diferențierea, substantiv/verb propriu axei):** HERO,
  GREȘEALA, MANTRA, WOW, CINE DEVII. Aici verbul de treaptă e INTERZIS ca ancoră;
  fiecare construcție își pune verbul propriu: C09 **a lega** · C10 **a defini** ·
  C11 **a compara** · C12 **a explica**. *(C10: motto = verbul de treaptă „măsoară";
  verbul de construcție = „a defini" — BRAIN-006.)*
- **Regula anti-contaminare:** verbul-semnătură al unei construcții T3 NU apare ca ancoră
  în slotturile de construcție ale alteia. „Compar" e al C11, nu intră în WOW/mantra C09;
  „măsor/cât" e al C10; „de ce/explic" e al C12. (Detectorul tier-aware le scopează.)

### §T3 · SPEC C09 RELAȚII — LOCKED v1.0 (V66, confirmat ARHITECT)
- **HERO:** „Cum transform legăturile în răspunsuri?"
- **BOMBĂ:** „Ai toate datele. Și niciun răspuns."
- **GREȘEALA:** „Oamenii copiază coloane dintr-un tabel în altul. Profesioniștii le leagă o dată."
- **AHA (lock S5):** „Fără relații ai date. Cu relații ai răspunsuri."
- **MANTRA:** „Nu mutăm datele. Le legăm." (cuvânt-cheie galben: *legăm*)
- **WOW:** „Tabele care stăteau alături fără să se cunoască. Acum răspund împreună la o singură întrebare."
- **MOTTO:** „Întrebi o dată. Modelul răspunde." (slot de treaptă, vezi gramatica)
- **CINE DEVII:** „Nu mai vezi o rețea. O interoghezi."
- **PAYOFF:** „Un set cunoscut a devenit un model care răspunde."
- **MIZA:** „Un director nu întreabă ce conține tabelul. Întreabă care client, ce produs, ce
  perioadă. Răspunsul la întrebarea lui trăiește în mai multe tabele deodată. C09 este
  momentul în care datele încep să răspundă la întrebări de business, nu doar să fie corecte
  și ordonate."
- **Verb-semnătură C09:** *a lega* (ancoră în hero/greșeală/mantra). Verbul de treaptă
  (întreb/răspund) rezervat mottoului. Slotturile NU se mai redeschid: sunt LOCKED.

### §T3 · SPEC C10 MĂSURI — LOCKED v1.0 (BRAIN-006, varianta revizuită)
- **Problema:** ai un model, dar fiecare calculează altă cifră pentru aceeași întrebare; o cifră bună pentru o felie e greșită pentru alta.
- **Output:** o măsură stabilă (măsura vie) — o cifră care înseamnă același lucru pentru toți, corectă în orice context.
- **Instrumente:** măsuri, agregări, DAX de bază, context de filtrare, Power Pivot, single source of truth.
- **HERO:** „Cum scriu o cifră o dată și răspunde corect oriunde?"
- **BOMBĂ:** „O cifră bună pentru un client. Greșită pentru toți ceilalți."
- **GREȘEALA:** „Oamenii scriu un total pentru fiecare felie. Profesioniștii scriu o măsură pentru toate."
- **AHA (lock):** „Un număr stă în tabel. O măsură trăiește în întrebare."
- **MANTRA:** „Nu scriem cifra. O definim." (cuvânt-cheie galben: *definim*)
- **WOW:** „Înainte, o cifră bună pentru o singură felie. Acum, o măsură care răspunde corect pentru orice felie."
- **MOTTO:** „Întrebi cât. Modelul măsoară." (slot de treaptă)
- **CINE DEVII:** „Nu mai scrii un total. Definești o măsură care răspunde singură."
- **PAYOFF:** „Un model care răspunde a devenit un model care măsoară."
- **MIZA:** „Un director trăiește cu rapoarte care nu se potrivesc: trei oameni, trei totaluri pentru aceeași întrebare. C10 e momentul în care o cifră se definește o singură dată și răspunde corect oriunde: pentru orice client, lună sau produs. Nu mai e numărul cuiva. E măsura în care toți au încredere, fiindcă e una singură."
- **Verb-semnătură:** *a defini* (ancoră în hero/greșeală/mantra/cine-devii). Motto = verbul de treaptă „măsoară".
- **Identitate:** măsura vie · define once · context-aware · single source of truth.
- **NU are voie:** ranking/top/bottom/comparații (C11), explicații cauzale (C12), dashboard (T4), acțiune (T5).
- **Gardă anti-contaminare:** „compar/care" (C11) și „de ce/explic" (C12) INTERZISE ca ancoră în slotturile C10.

### §T3 · SPEC C11 COMPARAȚII — LOCKED v1.0 (BRAIN-006)
- **Problema:** ai măsuri corecte, dar nu știi care contează; toate arată bine.
- **Output:** clasament / diferență / contribuție (care e mai mare, și cu cât).
- **Instrumente:** ranking, top/bottom, diferențe, contribuții (% din total), sortare analitică, ABC/Pareto *ca instrumente de comparație* (nu ca identitate).
- **HERO:** „Cum transform măsurile într-un clasament?"
- **BOMBĂ:** „Zece cifre corecte. Și tot nu știi care contează."
- **GREȘEALA:** „Oamenii privesc cifrele una câte una. Profesioniștii le compară."
- **AHA (lock):** „Un număr nu e mare sau mic. E mare sau mic față de altul."
- **MANTRA:** „Nu citim cifrele. Le comparăm." (cuvânt-cheie galben: *comparăm*)
- **WOW:** „Zece rapoarte, fiecare cu cifra lui. Acum un singur clasament care spune care contează."
- **MOTTO:** „Întrebi care. Modelul compară." (slot de treaptă)
- **CINE DEVII:** „Nu mai citești cifre. Vezi care contează."
- **PAYOFF:** „Un model care măsoară a devenit un model care compară."
- **MIZA:** „Un director nu vrea o listă de cifre. Vrea să știe care client, care produs, care lună contează cel mai mult, și cu cât. C11 e momentul în care cifrele se așază într-un clasament: nu doar cât, ci care, ca să știi unde să te uiți întâi. Fără el, ai măsuri corecte și tot nu știi pe ce să te concentrezi."
- **Verb-semnătură:** *a compara*. Motto = verbul de treaptă „compară".
- **NU are voie:** explicații cauzale (C12), dashboard/grafic publicabil (T4), decizie automată (T5).
- **Gardă anti-contaminare:** „de ce/explic" (C12) și „a defini/măsoară" (C10) INTERZISE ca ancoră în slotturile C11.

### §T3 · SPEC C12 INTERPRETARE — LOCKED v1.0 (BRAIN-006 · închide T3)
- **Problema:** știi care a crescut/scăzut, dar nu de ce; un clasament fără cauză nu e o decizie.
- **Output:** insight verbal / cauză / înțeles (citit din model). ÎNCHIDE treapta T3.
- **Instrumente:** citire din model, drill-down ANALITIC (citire, nu widget interactiv = T4), explicație, cauză, insight verbal, citire cross-tabel.
- **HERO:** „Cum transform clasamentul în înțeles?"
- **BOMBĂ:** „Știi care a crescut. Nu știi de ce."
- **GREȘEALA:** „Oamenii ghicesc de ce. Profesioniștii citesc de ce, în date."
- **AHA (lock):** „Cifrele spun ce. Numai interpretarea spune de ce."
- **MANTRA:** „Nu ghicim de ce. Explicăm." (cuvânt-cheie galben: *Explicăm*)
- **WOW:** „Un clasament care arăta că ceva a crescut. Acum și motivul pentru care a crescut."
- **MOTTO:** „Întrebi de ce. Modelul explică." (slot de treaptă)
- **CINE DEVII:** „Nu mai vezi un clasament. Înțelegi de ce arată așa."
- **PAYOFF:** „Un model care compară a devenit un model care explică. Setul nu mai e doar cunoscut, e interpretat."
- **MIZA:** „Un director nu se oprește la «care a scăzut». Întreabă imediat «de ce». C12 e momentul în care datele nu doar arată ce s-a întâmplat, ci explică de ce: ce client, ce produs, ce perioadă a tras cifra în jos sau în sus. E diferența dintre un raport care constată și o analiză care lămurește. Cu C12, setul a parcurs tot drumul: corect (T1), înțeles (T2), interpretat (T3)."
- **Verb-semnătură:** *a explica*. Motto = verbul de treaptă „explică".
- **Identitate LOCK:** INTERPRETARE / „de ce". Tema veche „What-if / scenarii business" RETRASĂ din identitate (BRAIN-006); poate rămâne, cel mult, instrument marginal, niciodată identitate.
- **NU are voie:** dashboard / grafic / raport vizual (T4); decizie / alertă / acțiune / recomandare executată (T5). C12 explică verbal, nu vizualizează și nu acționează.
- **Gardă anti-contaminare:** „a compara/care" (C11) INTERZIS ca ancoră; orice fugă spre vizual = T4, orice fugă spre acțiune = T5.

## §T4 — RAPORTARE · §T5 — AUTONOMIE (granițe LOCKED; identitatea completă se seedează la C13/C17)
**Formula de treaptă (LOCKED):** T3 produce răspunsul · T4 îl face vizibil · T5 îl face să funcționeze fără autor.

### §T4 — RAPORTARE / COMUNICARE VIZUALĂ
- **Întrebarea treptei:** „Cum vede altcineva, dintr-o privire?"
- **Output:** interfața vizuală — vizualizare / compoziție de pagină / sinteză de mesaj / raport livrat pentru decizie.
- **Lanț (LOCKED V70):** C13 VIZUALIZARE · C14 COMPUNERE · C15 SINTETIZARE · C16 LIVRARE.
- **Permis:** a face răspunsul (produs de T3) vizibil și comunicabil pentru o audiență; ierarhie vizuală, compunere de pagină, distilarea mesajului, predarea raportului pentru decizie.
- **Interzis:** a inventa răspunsuri/măsuri/cauze NOI (= T3, se consumă, nu se nasc la T4); a transforma munca într-un sistem care rulează fără autor (= T5).
- **Unde începe T5:** când livrarea nu mai e un act unic al autorului, ci devine un sistem care se reface, rulează și se ține singur, fără autor.

### §T5 — AUTONOMIE / FUNCȚIONARE FĂRĂ AUTOR
- **Întrebarea treptei:** „Cum funcționează fără mine?"
- **Output:** sistemul autonom — o livrare unică devine un lanț operațional end-to-end care rulează, se autocorectează prin reguli și funcționează fără autor.
- **Lanț (LOCKED V70):** C17 SISTEMATIZARE · C18 AUTOMATIZARE · C19 GUVERNARE · C20 DELEGARE.
- **Verbe de treaptă:** sistematizez · automatizez · guvernez · deleg.
- **Permis:** a transforma o livrare unică într-un sistem repetabil (C17); a-l face să ruleze fără efortul autorului (C18); a-i da reguli care îl țin corect fără supraveghere (C19); a preda responsabilitatea ca sistemul să lucreze fără autor (C20).
- **Interzis:** a reface analiza T3 sau designul vizual T4 ca lecție nouă; T5 industrializează ce există, nu naște conținut nou.
- **Delimitare C18 vs C04 (LOCKED):** C04 NORMALIZARE = automatizarea curățării/refacerii unui SET de date prin flux (teritoriul „Apăs Refresh"). C18 AUTOMATIZARE = automatizarea LANȚULUI operațional end-to-end, ca întregul sistem să ruleze fără autor. „Apăs Refresh" NU e identitate T5; e teritoriu C04.

**Nuanța deciziei (LOCKED):** decizia UMANĂ stă între T4 și T5 (omul citește raportul T4 și hotărăște = consumatorul pachetului, în afara construcțiilor). Sistemul care rulează și se autoguvernează fără autor = T5 AUTONOMIE.

---

# BACKLOG DECIZII (reguli candidate, ÎNCĂ NEDECISE — NU sunt norme)
> Aici trăiesc regulile propuse dar nedecise. NU se aplică la audit până nu sunt aprobate
> și mutate sus. Se decid în runda DEZAMBIGUIZARE.
- **(pending) Payoff specific, nereutilizabil** între construcții. *(Neverificabil mecanic;
  decizie DEZAMBIGUIZARE.)*
- **(pending) WOW cu deschidere distinctă** între construcții. *(idem.)*
- **(pending) Motto cu terminație distinctă** (C05↔C06 „Apoi orice decizie").
