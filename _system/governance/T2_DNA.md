# T2_DNA.md · ADN-ul real al Treptei 2 (extras din C05-C08)

> **STATUT: EXTRACȚIE, NU NORMĂ.** Aici se descrie ce EXISTĂ empiric în C05-C08,
> nu ce ar trebui. Regulile derivate trăiesc în `TRAINITY_ARCHITECTURE_BIBLE.md`
> (§SHARED + §T2). Acest DNA alimentează §T2.
> Sursă: cele 4 construcții livrabile (Studiu) + observațiile auditului de treaptă.
> Ancorat la commit `ca23b05`.

---

## 0. CELE 4 CONSTRUCȚII (identitate de bază)

| | C05 | C06 | C07 | C08 |
|---|---|---|---|---|
| Nume | DICȚIONAR | CLASIFICARE | DATARE | CARTOGRAFIERE |
| Competență | vocabular | sens | calendar | context |
| Întrebare | „Din ce e făcut acest set?" | „Ce înseamnă fiecare rând?" | „Când se întâmplă fiecare rând?" | „Cu cine se leagă fiecare rând?" |
| Livrabil (sheet) | `_DICTIONAR` | `_CLASE/_SEGMENTE/_SCORURI` | `_TIMELINE/_CALENDAR/_SEZON` | `_ECOSISTEM/_CHEI/_ROLURI` |
| AHA (lock) | „Nu cunoști un set până nu-l poți enumera." | „Un rând nu are sens până nu primește o regulă." | „Un set fără poziție în timp e un set fără memorie." | „Cele mai importante date despre un rând nu sunt în rând." |

## 1. STRUCTURA COMUNĂ (prezentă în TOATE 4 — invariant de schelet)

- **6 ETAPE**, fixe ca rol și ordine: REALITATE → INVESTIGAȚIE → TRANSFORMARE → VERIFICARE → STABILIZARE → CONFIRMARE.
- **18 PAȘI** (3 pași / etapă, fără excepție).
- **5 FENOMENE** în secțiunea SCENA.
- **15 verificări** (final-check-btn), din care secțiunea „8 VERIFICĂRI FINALE canonice".
- **2 casete PROMPT AI** (Promptul 1 în etapa 2, Promptul 2 în etapa 3).
- **1 hero-obiect dedicat** (poză 3:2, watermark Gemini scos).

## 2. TIPARUL ETAPELOR (nume + faze + instrumente)

| Etapă | stage-name | phase-tag | type-tag | Rol |
|---|---|---|---|---|
| 1 | REALITATE | INPUT | Manual | deschide setul predat de C0(N-1) |
| 2 | INVESTIGAȚIE | AI | Copilot · Promptul 1 | interogare AI a setului |
| 3 | TRANSFORMARE | *[variabil local]* | Promptul 2 | construiește livrabilul |
| 4 | VERIFICARE | CONTROL | *[funcții pe axă]* | confruntă cu setul |
| 5 | STABILIZARE | RECALCUL | Tabel structurat | ancorare la sursă (tabel viu) |
| 6 | CONFIRMARE | PAYOFF | Cap-coadă | predă către C0(N+1) |

**Numele lung al etapei** urmează tiparul:
`ETAPA N · [DESCHIDERE-axă / INTEROGARE ASISTATĂ DE AI / [transformare-axă] / VERIFICAREA [obiect] / ANCORARE LA SURSĂ / PREDAREA [livrabil]]`.

## 3. TIPARUL SCENA (5 fenomene)

Secțiune „SCENA REALĂ · [hook axă]", 5 carduri numerotate 01-05, fiecare cu titlu
(majuscule) + descriere de o frază. Fenomenele sunt **specifice axei**, dar
formatul (num + titlu + desc) e identic. Exemple: C06 = CLASA ABC / SEGMENTE /
ETICHETĂ DERIVATĂ / REGULI COMPUSE / SCORING; C07 = PERIOADA REALĂ / GRANULARITATE /
GOLURI ÎN TIMP / CALENDAR OPERAȚIONAL / FIȘA TEMPORALĂ; C08 = SATELIȚI / CHEI /
ROLURI / CÂMPURI EXTERNE / LIMBI DIFERITE.

## 4. TIPARUL DOVADA (before/after)

Secțiune „DOVADA TRANSFORMĂRII", listă de 4-5 perechi ÎNAINTE → DUPĂ, fiecare cu
un indicator + valoare-înainte + valoare-după. Format identic; conținut pe axă.

## 5. TIPARUL VERIFICĂRILOR

„RITUAL TRAINITY · CONTROL FINAL" → „8 verificări finale canonice" → carduri
[ETICHETĂ] + text + buton VERIFICĂ. Prima verificare e mereu CONTROL
(„Date_MASTER-C0N.xlsx există, se deschide, conține foaia Vanzari neschimbată").
Ultima e livrabilul + invariantul de valori sursă.

## 6. FORMULE RETORICE RECURENTE (semnături de treaptă)

| Element | Tipar | C05 | C06 | C07 | C08 |
|---|---|---|---|---|---|
| MANTRA | „Nu [verb-operațional]. [Îl/Le] [verb-C0N]." | Nu privim tabelul. Îl interogăm. | Nu citim rândurile. Le clasificăm prin reguli. | Nu interpretăm timpul. Îl structurăm. | Nu aducem contextul. Îl localizăm. |
| GREȘEALA | „Oamenii [X]. Profesioniștii [Y]." | presupun ce conține / îl enumeră | citesc rândurile / le clasifică | presupun când / citesc cronologia | citesc ca pe o insulă / îl leagă de ecosistem |
| PROMISE (CINE DEVII) | „Nu mai vezi [X]. Vezi [Y]." | coloane / teritoriu | rânduri / clase | o listă / un calendar | un tabel singur / o rețea |
| MOTTO | „Un [livrabil]. Apoi orice [Y]." | Un set cunoscut. Apoi orice decizie. | Un sens construit. Apoi orice decizie. | Un set datat. Apoi orice analiză în timp. | Un set cartografiat. Apoi orice analiză de context. |
| COMPLETION | „[Livrabil] validat." | Dicționar validat. | Set clasificat validat. | Cronologie validată. | Hartă a ecosistemului validată. |

## 7. TIPARUL PAYOFF / WOW (variabil, NU semnătură strictă)

Secțiune payoff: 3 linii „dim" (Nu am modificat/rescris/alterat...) + 1 linie
„accent" + linii „regular" + slot WOW (verde) + motto. WOW antropomorfizează
transformarea. **Observație: payoff/WOW NU au tipar unic** — vezi §11 driftul.

## 8. TIPARUL PROMPTURILOR AI

- **Promptul 1** (etapa 2): interogare descriptivă a setului („Pentru coloana X
  spune-mi..."). Output = harta/raportul de bază.
- **Promptul 2** (etapa 3): adâncire pe axă, copiat într-un sheet de profil.
- Ambele: instrument de **interogare**, nu de execuție. „Promptul natural devine
  instrument de interogare [axă], nu de execuție."

## 9. TIPARUL HANDOFF

- **Intrare (etapa 1):** „Dublu-click pe Date_MASTER-C0N.xlsx... Setul predat de
  C0(N-1) [stare]..."
- **Ieșire (etapa 6 + teaser):** „Predă către C0(N+1)... C0(N+1) deschide [axa
  următoare]." + completion „C0N e pregătit pentru C0(N+1) [nume]."
- Lanțul: C04→C05→C06→C07→C08→C09.

## 10. ELEMENTE PE NIVELURI DE PREZENȚĂ

- **În TOATE 4 (invariant):** scheletul (6/18/5/15/2), tiparul etapelor, mantra-
  semnătură, greșeala, promise, motto, completion, handoff, hero dedicat, garda
  T2/T3, invariant sumă conservată (7.986.019,38 lei), R-V02.15 (zero cifre
  business în HTML).
- **În MAJORITATE (3/4):** type-tag E3 = „Promptul 2" (acum uniform după
  uniformizare); phase-tag E5 = RECALCUL.
- **LOCAL (justificat de axă):** fenomenele SCENA, funcțiile de verificare E4
  (UNIQUE/COUNTA vs IFS vs MIN/MAX vs COUNTIF/MATCH), phase-tag E3
  (FORMULE/POWER QUERY/HARTĂ), hero-obiectul.

## 11. POSIBILE DRIFTURI (observate, NU încă reguli)

- **D1 phase-tag E3 neuniform:** FORMULE (C06) / POWER QUERY (C05, C07) / HARTĂ (C08).
- **D2 funcții E4** diferă pe axă — *variație acceptabilă* (verifici alt tip de date),
  DAR C06 E4 folosește funcții de **construcție** (IFS/SWITCH/TEXT), nu de verificare.
- **D3 mecanică E4 C06:** stage-quote promite verificare, pașii construiesc
  (etichetă/regulă/scor). Reziduu **structural** (C06 are 5 sub-produse).
- **D4 payoff/WOW/motto:** tipare duplicate C06↔C07 (payoff „Setul nu mai X.
  Fiecare rând are Y", WOW „Dintr-o listă de tranzacții..."), motto C05↔C06
  („Apoi orice decizie"). Payoff C05 slab (descriptiv).

## 12. CONTAMINĂRI DIN ALTE TREPTE (observate istoric, curățate)

- **C03 (audit):** „AUDIT" ca nume de etapă 4 (era în C05/C06, scos → VERIFICAREA).
  „auditabil" (adjectiv) = vocabular legitim, păstrat.
- **C04 (normalizare/sumă):** ecouri „Suma rămâne conservată", „martorul de sumă"
  (curățate → „valorile sursă neatinse").
- **C09/T3 (Data Model/join/lookup):** XLOOKUP/LOOKUP/„aduse cu XLOOKUP" (C06),
  „conectat/conexiune", Power Query, „BI-ready" — curățate pe axa CARTOGRAFIERE.
- **POWER QUERY phase-tag** (C05/C07) — suspendat de arhitect ca observație.
