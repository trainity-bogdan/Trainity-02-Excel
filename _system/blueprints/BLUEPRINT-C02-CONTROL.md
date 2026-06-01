# BLUEPRINT C02 · CONTROL — CORESPONDENȚA CU REALITATEA

> Spec de construcție, NU conținut final. Sloturile de copy (mantra/payoff/WOW/motto)
> se confirmă la implementare. Construit conform `TRAINITY_ARCHITECTURE_BIBLE §SHARED`
> + regulile T1. Identitate + 5 anomalii = LOCK (decizie ARHITECT V58). Treaptă: T1.

---

## 0. IDENTITATE (LOCK)
- **Nume:** C02 · CONTROL
- **Treaptă:** T1 STRUCTURĂ-CONTROL (a doua construcție)
- **Tema:** CORESPONDENȚA CU REALITATEA
- **AHA (lock S5):** „Valid nu înseamnă corect."
- **Regula oficială:** Excel acceptă valoarea. Business-ul trebuie să o investigheze.
- **Competență:** Identific valori pe care Excel le acceptă, dar care încalcă reguli ale lumii reale.
- **Filozofia:** C02 NU repară / NU șterge / NU modifică / NU decide / NU previne. **Semnalează** și **construiește dovezi** pentru o decizie de business.
- **Livrabil:** setul cu anomaliile de realitate **semnalate** (coloane `status_validare` + `motiv_anomalie`), valorile sursă neatinse.

## 1. HANDOFF (R-HAND-1/2/3)
- **Preia de la C01:** setul **structural curat** (un tabel real, fără ambalaj). „Setul predat de C01 este structural curat."
- **PAS 01 (tipar):** „Setul predat de C01 e structural curat. Dar valorile pot fi valide tehnic și totuși greșite față de realitate."
- **Predă către (R-HAND-2):** C03 · AUDIT („vezi ce nu se vede" — contaminarea invizibilă). Teaser → „C03 caută defectele pe care nici ochiul, nici verificarea de realitate nu le văd: cele tehnice, invizibile."

## 2. SCHELET (S4 — moștenit din §SHARED)
6 etape · 18 pași (3/etapă) · 5 fenomene SCENA · 8 verificări finale · 2 prompturi AI · 1 hero dedicat.

## 3. ETAPE (R-STR-1, R-TERM-1, R-PED-1, R-MET-1, R-PHASE-1)

| # | Nume etapă | phase-tag | type-tag | Conținut (axă CORESPONDENȚA CU REALITATEA) |
|---|---|---|---|---|
| 1 REALITATE | DESCHIDERE A SUSPICIUNII | INPUT | Manual | deschide setul curat predat de C01; recunoaște că valorile valide pot minți operațional |
| 2 INVESTIGAȚIE | INTEROGARE ASISTATĂ DE AI | AI | Copilot · Promptul 1 | interoghează ce valori par valide dar suspecte față de realitate |
| 3 TRANSFORMARE | CONSTRUIREA SEMNALIZĂRII | FORMULE | Promptul 2 | construiește aparatul de semnalizare: nomenclatoare, tabele de reguli, comparații (NU modifică datele) |
| 4 VERIFICARE | VERIFICAREA CORESPONDENȚEI | CONTROL | *funcții de verificare pe axă* | confruntă semnalările cu setul, cuantifică, marchează ce necesită decizie |
| 5 STABILIZARE | ANCORARE LA SURSĂ | RECALCUL | Tabel structurat | semnalări reaplicabile (tabel viu), regulă anti-derivă |
| 6 CONFIRMARE | PREDAREA SETULUI CONTROLAT | PAYOFF | Cap-coadă | predă către C03 setul cu anomaliile de realitate semnalate |

## 4. SCENA · 5 FENOMENE = cele 5 anomalii (ordine LOCK)

> Progresie: de la problema vizibilă la contradicția cea mai ascunsă.

| # | Fenomen (card SCENA) | Teritoriu | Cine reclamă | Ce vezi |
|---|---|---|---|---|
| **01** | **ORAȘE NEALINIATE** | nomenclator | omul (geografia) | aceeași localitate scrisă în mai multe feluri (Cluj/CJ/Cluj-Napoca) |
| **02** | **TVA GREȘIT** | regulă externă/fiscală | omul (regula fiscală) | cotă validă ca număr, greșită fiscal pentru categorie |
| **03** | **SCADENȚĂ < FACTURĂ** | cronologie / ordine logică | omul (logica) | ambele date valide, ordinea imposibilă |
| **04** | **ZI NELUCRĂTOARE (NETWORKDAYS)** | calendar operațional | omul (calendarul firmei) | dată validă, dar firma nu opera (sărbătoare legală) |
| **05** | **CNP CONTRADICTORIU** *(ICONIC)* | consistență între câmpuri | omul (contradicția) | CNP+Sex+Județ+Data_Nașterii par corecte separat, se contrazic împreună |

## 5. INSTRUMENTE per anomalie (din spec LOCK)
- **C02.01 Orașe:** Advanced Filter (valori unice → nomenclator) · Conditional Formatting (marchează abaterile) · Data Validation (FORMALIZARE marginală a nomenclatorului, DOAR după decizia business — nu temă, nu competență).
- **C02.02 TVA:** Conditional Formatting · tabel reguli TVA per categorie.
- **C02.03 Scadență:** formulă de comparație (`data_scadenței < data_factura`) · Conditional Formatting.
- **C02.04 Zi nelucrătoare:** NETWORKDAYS / NETWORKDAYS.INTL · tabel sărbători legale · Conditional Formatting.
- **C02.05 CNP:** formule (extragere componente + interpretare sex/județ/dată + cifră de control) · Conditional Formatting (marchează inconsistențele) · nomenclator cod-județ.
- **Roluri (R-PED/§SHARED):** AF = DESCOPERIRE · CF = SEMNALIZARE · DV = FORMALIZARE marginală.

## 6. PROMPTURI AI (R-PED-1/2/3)
- **Promptul 1 (etapa 2):** interogare descriptivă — „ce valori par valide dar suspecte față de realitate (orașe inconsistente, cote, date, identificatori)?". Instrument de interogare, nu de execuție.
- **Promptul 2 (etapa 3):** adâncire — construirea semnalizării (nomenclatoare, reguli, comparații), copiată într-o foaie de profil.

## 7. VERIFICARE (R-MET-1 — etapa 4 VERIFICĂ, nu repară)
8 verificări finale canonice; card 1 = CONTROL (`Date_MASTER-C02.xlsx` există, foaia Vanzari neschimbată); card final = livrabil (set cu anomalii semnalate) + valori sursă neatinse (S3). Pașii E4: confruntă fiecare semnalare cu setul, cuantifică (COUNTIF), **marchează — nu corectează.**

## 8. GARDA T1 (delimitări — ce poate / ce NU poate C02)
- **POATE:** semnalează valori greșite față de realitate; construiește dovezi pentru decizia de business.
- **NU POATE (= C03):** semnale tehnice — spații ascunse, text vs număr, Unicode, caractere invizibile (greșit față de MOTOR). Criteriu: dacă reclamantul e motorul Excel → C03.
- **NU POATE (= T5):** prevenție / Data Validation în cascadă / gardian permanent. C02 detectează+semnalează, NU închide poarta viitoare.
- **NU POATE:** repară / șterge / modifică / decide (decizia rămâne a business-ului).

## 9. SLOTURI DE IDENTITATE (copy final la implementare — NU acum)
- obiect: CONTROL · întrebare: [slot] · titlu: [slot] · AHA: LOCK „Valid nu înseamnă corect."
- mantra/payoff/WOW/motto: [sloturi — se confirmă la implementare; nu se scriu în blueprint].

## 10. DATE_MASTER · cerințe la implementare (target)
Setul actual (`Vanzari`) are: `judet`, `cota_tva`, `data_factura`, `client_nume` etc.
**Adăugări necesare pentru cele 5 anomalii:**
- C02.01 → coloană `oras` + nomenclator `tbl_Localitati` (oraș↔județ).
- C02.02 → tabel `tbl_RegulriTVA` (categorie → cotă legală). *(`cota_tva` există.)*
- C02.03 → coloană `data_scadentei`.
- C02.04 → tabel `tbl_SarbatoriLegale`.
- C02.05 → coloane `CNP`, `Sex`, `Data_Nasterii` (`judet` există) + nomenclator `tbl_CodJudetCNP`. *(CNP = iconic, injectat conștient — setul e B2B.)*
- Anomalii plantate per fenomen, în proporții realiste; `status_validare` + `motiv_anomalie` ca output.

## 11. ARTEFACTE LA IMPLEMENTARE (nu acum)
4 HTML (Studiu/Editor-Studiu/Video/Editor-Video) · FILM · Date_MASTER-C02 (rescris cu cele 5 anomalii) · hero dedicat (prompt Banana) · 6 exec-stage · Creativ.

---

## OBSERVAȚII (notate separat — NU redeschid arhitectura)
*(Conform regulii „orice observație nouă se notează separat".)*
1. **Tensiune de ordine E3↔E4 vs dificultate (audit anterior):** ordinea anomaliilor 03 (Scadență, relațional) → 04 (NETWORKDAYS, context extern) e pe axa „distanța sursei de adevăr" (LOCK), nu pe „dificultate cognitivă crescătoare" (care ar cere 04→03). Decizie ARHITECT: ordinea LOCK rămâne. Notat, nu redeschis.
2. **CNP în set B2B:** rămâne exemplu iconic injectat conștient (decizie V58). Anti-drift: doar registrul „arată perfect, totuși fals" (contradicție multi-câmp + cifră de control), niciodată format/lungime (= C03).
3. **DV (C02.01):** marginală, doar formalizare după decizie. DV în cascadă (oraș filtrat după județ) = T5 — **interzis în corpul C02**.
4. **Aliniere nume fișier:** construcția = „C02 · CONTROL"; fișierul/HTML încă poartă „02-Marcare" + identitatea veche MARCARE. Se aliniază la implementarea efectivă.
5. **Implementare HTML + Date_MASTER:** PENDING. Acest blueprint = target LOCK; corpul c02/ e încă versiunea veche MARCARE (36 anomalii structurale).
