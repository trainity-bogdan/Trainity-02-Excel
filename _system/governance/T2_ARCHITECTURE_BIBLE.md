# T2_ARCHITECTURE_BIBLE.md · Document normativ (ADN validat → reguli)

> **STATUT: NORMĂ.** Transformă ADN-ul din `T2_DNA.md` în reguli obligatorii.
> Orice construcție T2 (și T3-T5 prin moștenire) se evaluează contra acestor reguli.
> Format regulă: NUME · descriere · motiv · severitate · obligatorie/recomandată ·
> conform · neconform · unde · consecință.

---

## REGULI SACRE (nu se încalcă fără aprobarea arhitectului)

- **S1 · Un singur scop per construcție.** Fiecare construcție răspunde la O SINGURĂ
  întrebare. Dacă răspunde la două, e contaminată. (Sursă: C05-C08, fiecare o întrebare.)
- **S2 · Granița T2/T3.** T2 descrie/etichetează, NU interpretează/decide/modelează.
  Interzis: trend, performanță, prioritizare, decizie, join, Data Model, XLOOKUP/LOOKUP
  ca aducere, măsuri, BI/dashboard.
- **S3 · Invariant de valori sursă.** valoare_neta conservată cap-coadă (R-V02.14);
  zero cifre business în HTML/FILM (R-V02.15). Cifrele trăiesc în Excel.
- **S4 · Schelet fix.** 6 etape · 18 pași · 5 fenomene · 8 verificări finale · 2 prompturi.
  Nu se modifică fără decizie arhitecturală.
- **S5 · AHA locked.** AHA-ul oficial al fiecărei construcții (vezi T2_DNA §0) nu se
  schimbă fără aprobare.

---

## REGULI STRUCTURALE

**R-STR-1 · Cele 6 etape canonice.**
Descriere: ordinea și rolurile REALITATE→INVESTIGAȚIE→TRANSFORMARE→VERIFICARE→
STABILIZARE→CONFIRMARE sunt fixe. · Motiv: schelet comun = sistem, nu colecție. ·
Severitate: CRITICĂ · Obligatorie. · Conform: C05-C08. · Neconform: 5 sau 7 etape,
altă ordine. · Unde: Studiu + Editor-Studiu. · Consecință: FAIL structural.

**R-STR-2 · 3 pași per etapă (18 total).** Obligatorie · CRITICĂ. Neconform: etapă
cu 2 sau 4 pași. Consecință: FAIL.

**R-STR-3 · 5 fenomene SCENA.** Obligatorie. Neconform: 4 sau 6 carduri. FAIL minor.

**R-STR-4 · Meniu mobil fără bandă nav-brand (R-V03.73).** Side-nav începe cu
nav-progress, ca C01. Obligatorie · MEDIE.

---

## REGULI TERMINOLOGICE

**R-TERM-1 · Etapa 4 = „VERIFICAREA [obiect]".** Niciodată „AUDIT" (= ADN C03). ·
Motiv: auditul aparține C03; T2 verifică. · CRITICĂ · Obligatorie. ·
Conform: „VERIFICAREA CRONOLOGIEI" (C07). · Neconform: „AUDIT AL REGULILOR". ·
Unde: stage-label etapa 4. · Consecință: contaminare, se respinge.

**R-TERM-2 · phase-tag E5 = „RECALCUL".** Niciodată „RECALC". · MEDIE · Obligatorie.

**R-TERM-3 · „auditabil" permis.** Adjectivul (= verificabil) e vocabular T2 legitim,
prezent în toate 4. NU se confundă cu „AUDIT" (nume de etapă). · Clarificare.

**R-TERM-4 · Interdicții T3/viitor.** Niciun: XLOOKUP/LOOKUP ca aducere, join, Data
Model, „conectat/conectează/conexiune", Power Query (ca operațiune), BI-ready, KPI,
trend, performanță, „cel mai mare/mic", dominant, prioritar/strategic/critic. ·
CRITICĂ · Obligatorie. · Consecință: FAIL de identitate. · Excepție: teaser explicit
către construcția următoare („C09 deschide Data Model") = legitim.

**R-TERM-5 · Fără ecouri C04.** Fără „Suma rămâne conservată / martorul de sumă" în
copy. Conservarea trăiește în Excel (S3); în HTML = „valorile sursă rămân neatinse". ·
MEDIE · Obligatorie.

**R-TERM-6 · Fără em/en-dash (R-V03.72).** Zero `—`/`–` în text vizibil. · MEDIE.

---

## REGULI PEDAGOGICE

**R-PED-1 · Etapa 3 e AI-assisted.** type-tag E3 = „Promptul 2"; transformarea e
rezultatul unui prompt, nu muncă manuală. Formulele (IFS/SWITCH etc.) sunt output-ul
promptului. · Motiv: filozofia Trainity = AI-driven, nu 2015 manual. · MAJORĂ ·
Obligatorie. · Conform: C05/C07/C08 (acum C06). · Neconform: E3 etichetată „IFS/SWITCH"
ca muncă manuală.

**R-PED-2 · Două prompturi AI per construcție.** Promptul 1 (interogare, etapa 2),
Promptul 2 (adâncire, etapa 3). · Obligatorie · MEDIE.

**R-PED-3 · Promptul = interogare, nu execuție.** Limbaj „instrument de interogare
[axă], nu de execuție". · Recomandată.

---

## REGULI METODOLOGICE

**R-MET-1 · Etapa 4 verifică, nu construiește.** Pașii etapei 4 CONFRUNTĂ/VERIFICĂ/
MARCHEAZĂ (funcții de numărare/potrivire: COUNTIF, MIN/MAX, MATCH, COUNTA), NU
construiesc livrabilul. · Motiv: verificarea ≠ reconstrucție. · MAJORĂ · Obligatorie. ·
Conform: C07 („Confruntă perioada cu MIN/MAX", „Marchează golurile"). · Neconform: C06
E4 („Compune eticheta", „Construiește regulă", „Calculează scorul"). · Unde: step-titles
etapa 4. · Consecință: NECESITĂ DECIZIE ARHITECTURALĂ (reziduu structural C06, vezi
T2_DNA D3). *Această regulă e încălcată azi de C06 — flag deschis.*

**R-MET-2 · Verificare prin confruntare cu setul.** Stage-quote E4: „Nu avem încredere
oarbă... Confruntăm fiecare [X] cu setul însuși." · Obligatorie · MEDIE.

**R-MET-3 · Funcții de verificare pe axă = variație acceptabilă.** UNIQUE/COUNTA (C05),
MIN/MAX/COUNTIFS (C07), COUNTIF/MATCH (C08) diferă justificat (tip de date diferit). ·
Clarificare (NU drift).

---

## REGULI DE HANDOFF

**R-HAND-1 · Intrare explicită.** Etapa 1 PAS 01: „Setul predat de C0(N-1) [stare]". ·
Motiv: lanț coerent, nu construcție orfană. · MAJORĂ · Obligatorie. · Conform: „Setul
predat de C06 vine..." (C07). · Neconform: „Setul vine cu vocabular" (fără „predat de").

**R-HAND-2 · Ieșire explicită + teaser.** Etapa 6 + teaser: „Predă către C0(N+1)... 
C0(N+1) deschide [axa]." · Obligatorie · MEDIE.

**R-HAND-3 · Stare moștenită corectă.** C0N preia starea reală a lui C0(N-1) (C06
primește „vocabular", C07 „set clasificat", C08 „set datat"). · Obligatorie.

---

## REGULI PENTRU PHASE-TAGS

**R-PHASE-1 · Phase-tags fixe pe poziție:** E1=INPUT, E2=AI, E4=CONTROL, E5=RECALCUL,
E6=PAYOFF. · Obligatorie · MEDIE.
**R-PHASE-2 · E3 phase-tag = variabil pe axă, dar din familia transformării.** Observat:
FORMULE/POWER QUERY/HARTĂ. · NECESITĂ DECIZIE: se uniformizează sau rămâne pe axă?
(Power Query trage spre C09 — vezi T2_DNA D1.)

---

## REGULI PENTRU COMPLETION / PAYOFF / TEASER / NAMING

**R-COMP-1 · completion-title = „[Livrabil] validat".** Fără adjective suplimentare
(„auditabil"). · MEDIE · Obligatorie. · Conform: „Cronologie validată". · Neconform:
„Dicționar auditabil validat".

**R-PAY-1 · Payoff specific, nu reutilizabil.** Un payoff nu trebuie să poată fi mutat
la altă construcție. · MAJORĂ · Recomandată (intră în DEZAMBIGUIZARE). · Neconform:
payoff C06↔C07 cu același tipar „Setul nu mai X. Fiecare rând are Y".

**R-WOW-1 · WOW cu deschidere distinctă.** Două WOW-uri nu încep identic. · Recomandată. ·
Neconform: C06↔C07 „Dintr-o listă de tranzacții...".

**R-NAME-1 · Nume construcție = LOCK.** DICȚIONAR/CLASIFICARE/DATARE/CARTOGRAFIERE.
Numele istorice (TIPIZARE etc.) abandonate. · CRITICĂ · Obligatorie.

**R-TEASER-1 · Teaserul poate numi construcția următoare și treapta ei**, inclusiv
termeni T3 (Data Model) ca descriere a ce URMEAZĂ. NU contaminează dacă e explicit
„C0(N+1) deschide...". · Clarificare.
