# T2_POSITION_MATRIX.md · Matrice comparativă pe poziții structurale

> **PRINCIPIU: compari POZIȚII, nu fișiere.** Fiecare rând = o poziție structurală
> echivalentă în toate 4. Status: `uniform` / `variație acceptabilă` / `drift` /
> `contaminare` / `decizie arhitecturală`. Ancorat la `ca23b05` (post-uniformizare).

---

## A. NUMELE ETAPELOR (stage-label)

| Poziție | C05 | C06 | C07 | C08 | Regulă | Status |
|---|---|---|---|---|---|---|
| E1 | DESCHIDERE DESCRIPTIVĂ | DESCHIDERE A SENSULUI | DESCHIDERE TEMPORALĂ | DESCHIDERE RELAȚIONALĂ | „DESCHIDERE [axă]" | uniform |
| E2 | INTEROGARE ASISTATĂ DE AI | idem | idem | idem | fix | uniform |
| E3 | PROFILARE STRUCTURALĂ | CONSTRUIREA CLASELOR | PROFILARE TEMPORALĂ | CARTOGRAFIEREA ECOSISTEMULUI | „[transformare-axă]" | variație acceptabilă |
| E4 | VERIFICAREA DICȚIONARULUI | VERIFICAREA REGULILOR | VERIFICAREA CRONOLOGIEI | VERIFICAREA CHEILOR | R-TERM-1 „VERIFICAREA [obiect]" | uniform *(post-fix)* |
| E5 | ANCORARE LA SURSĂ | idem | idem | idem | fix | uniform |
| E6 | PREDAREA PROFILULUI | PREDAREA SETULUI CLASIFICAT | PREDAREA MEMORIEI | PREDAREA HĂRȚII | „PREDAREA [livrabil]" | uniform |

## B. PHASE-TAGS

| Poziție | C05 | C06 | C07 | C08 | Regulă | Status |
|---|---|---|---|---|---|---|
| E1 | INPUT | INPUT | INPUT | INPUT | R-PHASE-1 | uniform |
| E2 | AI | AI | AI | AI | R-PHASE-1 | uniform |
| **E3** | **POWER QUERY** | **FORMULE** | **POWER QUERY** | **HARTĂ** | R-PHASE-2 | **decizie arhitecturală** (Power Query trage spre C09) |
| E4 | CONTROL | CONTROL | CONTROL | CONTROL | R-PHASE-1 | uniform |
| E5 | RECALCUL | RECALCUL | RECALCUL | RECALCUL | R-TERM-2 | uniform *(post-fix RECALC→RECALCUL)* |
| E6 | PAYOFF | PAYOFF | PAYOFF | PAYOFF | R-PHASE-1 | uniform |

## C. TYPE-TAGS

| Poziție | C05 | C06 | C07 | C08 | Status |
|---|---|---|---|---|---|
| E2 | Copilot · Promptul 1 | idem | idem | idem | uniform |
| E3 | Promptul 2 | Promptul 2 | Promptul 2 | Promptul 2 | uniform *(post-fix C06)* |
| **E4** | UNIQUE/COUNTA/COUNTIF | **IFS/SWITCH/TEXT** | MIN/MAX/COUNTIFS | COUNTIF/MATCH | **decizie** (C06 = funcții de construcție, nu verificare) |
| E5 | Tabel structurat | idem | idem | idem | uniform |
| E6 | Cap-coadă | idem | idem | idem | uniform |

## D. HANDOFF (intrare, PAS 01)

| C05 | C06 | C07 | C08 | Status |
|---|---|---|---|---|
| „Setul predat de C04 este structural curat" | „Setul predat de C05 vine cu vocabular" | „Setul predat de C06 vine..." | „Setul predat de C07 are..." | uniform *(post-fix C06)* |

## E. PROMPT AI 1 (etapa 2)

| | Conținut | Status |
|---|---|---|
| C05 | inventar etichete distincte + frecvențe | uniform (interogare descriptivă) |
| C06 | interogare reguli/clase posibile | uniform |
| C07 | interogarea cronologiei (perioadă, goluri, count/lună) | uniform |
| C08 | interogarea ecosistemului (foi, chei, roluri) | uniform |

## F. PROMPT AI 2 (etapa 3)

Toate 4: adâncire pe axă, copiat într-un sheet de profil. **uniform** ca mecanică.

## G. ETAPA 3 (mecanică)

| | Pași-cheie | Status |
|---|---|---|
| C05 | profilare structurală via Promptul 2 | uniform |
| C06 | Construiește clasă (IFS) + Rulează Promptul 2 + segment (SWITCH) | variație acceptabilă *(are Promptul 2)* |
| C07 | încarcă timeline + Promptul 2 + granularitate | uniform |
| C08 | hartă via Promptul 2 + chei/roluri | uniform |

## H. ETAPA 4 (mecanică — punct critic)

| | stage-quote | pași | Status |
|---|---|---|---|
| C05 | confruntă cu setul | UNIQUE/COUNTA (numără) | uniform |
| **C06** | „Confruntăm... Marcăm rândurile fără clasă" | **Compune etichetă / Construiește regulă / Calculează scor** | **decizie arhitecturală** (verifică prin construire) |
| C07 | confruntă cu setul | MIN/MAX/COUNTIFS (numără/confruntă) | uniform |
| C08 | confruntă cu setul | COUNTIF/MATCH (verifică existență) | uniform |

## I. VERIFICĂRI FINALE (8 carduri)

Toate 4: card 1 = CONTROL (fișier există/Vanzari neschimbată); card final = livrabil +
valori sursă neatinse. **uniform** ca structură.

## J. COMPLETION

| C05 | C06 | C07 | C08 | Status |
|---|---|---|---|---|
| Dicționar validat | Set clasificat validat | Cronologie validată | Hartă a ecosistemului validată | uniform *(post-fix C05 „auditabil")* |

## K. PAYOFF (accent)

| C05 | C06 | C07 | C08 | Status |
|---|---|---|---|---|
| Am inventariat dicționarul setului. | Setul nu mai are rânduri anonime. Fiecare rând are sens scris. | Setul nu mai plutește în timp. Fiecare rând are poziție temporală. | Nu mai ai rânduri suspendate. Știi unde trăiește contextul fiecăruia. | **drift** (C06↔C07 același tipar; C05 slab) → DEZAMBIGUIZARE |

## L. WOW

| C05 | C06 | C07 | C08 | Status |
|---|---|---|---|---|
| ...acum are hartă. | Dintr-o listă de tranzacții, am construit... | Dintr-o listă de tranzacții, am construit... | Un tabel izolat... începe să vorbească. | **drift** (C06↔C07 aceeași deschidere) → DEZAMBIGUIZARE |

## M. MOTTO / TEASER

| | MOTTO | Teaser | Status |
|---|---|---|---|
| C05 | Un set cunoscut. Apoi orice **decizie**. | → C06 CLASIFICARE | drift motto C05↔C06 |
| C06 | Un sens construit. Apoi orice **decizie**. | → C07 Datare | drift |
| C07 | Un set datat. Apoi orice analiză în timp. | → C08 Cartografiere | uniform-ish |
| C08 | Un set cartografiat. Apoi orice analiză de context. | → C09 Relații | uniform-ish |

## N. TERMINOLOGIE SENSIBILĂ (post-uniformizare)

| Termen | C05 | C06 | C07 | C08 | Status |
|---|---|---|---|---|---|
| AUDIT (nume etapă) | scos | scos | n/a | n/a | uniform (eliminat) |
| conectat la sursă | ancorat | ancorat | ancorat | ancorat | uniform |
| ecou „sumă" | scos | scos | scos | scos | uniform |
| RECALC | RECALCUL | — | — | — | uniform |
| Power Query (phase) | **prezent** | — | **prezent** | — | decizie (D1) |

## O. FORMULE RETORICE (semnături)

Mantra / greșeala / promise / motto / completion = **tipar comun intenționat** în toate
4 (semnătură de treaptă). Status: **uniform by design**. Singurul drift = conținutul
payoff/WOW (K, L) și terminația motto (M).
