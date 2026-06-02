# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-003-CORRECTED

## MANDAT
Realiniere pe TREAPTA 3, nu pe Construcția 03.

Mandatul anterior BRAIN-003, despre sincronizarea C03 FILM ↔ HTML, este ANULAT.
Nu executa sincronizare C03.
Nu modifica artefacte C03.
Nu continua discuția pe T1 decât dacă BRAIN cere explicit.

## CONTEXT
Suntem în arhitectura T3, adică TREAPTA 3, nu Construcția 03.

T1 = ÎNCREDERE
C01 Structurare
C02 Control
C03 Auditare
C04 Normalizare / Automatizare

T2 = CUNOAȘTERE
C05 Dicționar
C06 Clasificare
C07 Datare
C08 Cartografiere

T3 = ANALIZĂ / INTERPRETARE
C09 Relații
C10 Măsuri
C11 Comparații
C12 Interpretare

Poziția reală a proiectului:
- T1 este PASS operațional după BRAIN-001 și BRAIN-002.
- Nu mai împingem micro-reziduuri T1 decât dacă sunt blocante.
- Următorul palier strategic este T3.
- Suntem la C09, prima construcție din T3.

## OBIECTIV
Fă un audit de realiniere pentru T3 înainte de implementarea C09.

Nu implementa C09.
Nu genera HTML.
Nu genera FILM.
Nu genera imagini.
Nu genera xlsx.
Nu modifica fișiere de conținut.

Trebuie să răspunzi la întrebarea:
Este T3 suficient de clară pentru a începe construcția C09?

## VERIFICĂRI CERUTE

### 1. Harta T3
Verifică dacă în repo există o hartă T3 coerentă pentru:
- C09 Relații
- C10 Măsuri
- C11 Comparații
- C12 Interpretare

Pentru fiecare, confirmă:
- întrebarea-mamă
- verbul-semnătură
- substantivul-semnătură
- competența-semnătură
- output-ul
- ce predă construcției următoare

### 2. Granița T2 → T3
Verifică dacă C08 predă corect către C09.

C08 trebuie să încheie T2 cu:
- context recunoscut
- chei / zone / tabele înțelese
- hartă descriptivă

C09 trebuie să înceapă T3 cu:
- relații active
- model interogabil
- legături transformate în răspunsuri

### 3. Diferențiere C09-C12
Verifică dacă aceste patru construcții sunt imposibil de confundat:
- C09 = leagă
- C10 = măsoară
- C11 = compară
- C12 = explică

Răspunde explicit:
- ce face C09 ce nu face C10?
- ce face C10 ce nu face C11?
- ce face C11 ce nu face C12?
- ce face C12 fără să intre în T4/T5?

### 4. C10 WARNING
În arhitectura T3, C10 a fost marcat ca punct mai slab decât C09/C11/C12.
Verifică dacă în repo există o versiune revizuită / mai puternică pentru C10.

Dacă există, citeaz-o în raport.
Dacă nu există, marchează C10 ca WARNING arhitectural și cere decizie BRAIN.

### 5. Granița T3 → T4 → T5
Verifică dacă există delimitare clară:
- T3 = analiză / interpretare
- T4 = raportare / comunicare vizuală
- T5 = decizie / acțiune

C12 trebuie să rămână insight verbal / explicație.
C12 nu are voie să devină dashboard, raport vizual, recomandare executată, alertă sau acțiune.

### 6. Recomandare de intrare în C09
La final, spune clar:
- putem începe C09?
- ce lipsește înainte de C09?
- ce trebuie înghețat înainte de C09?
- care este primul mandat corect pentru implementarea C09?

## FIȘIERE PERMISE LA CITIRE
Ai voie să citești:
- BRAIN-TO-CLAUDE.md
- CLAUDE-TO-BRAIN.md
- STARE-CURENTA.md
- README.md
- CLAUDE.md
- documente / blueprint-uri / arhitectură T3 existente în repo
- artefacte C08 dacă sunt necesare pentru handoff C08 → C09
- artefacte C09-C12 dacă există

## FIȘIERE PERMISE LA SCRIERE
- CLAUDE-TO-BRAIN.md

## FIȘIERE INTERZISE LA MODIFICARE
- orice FILM
- orice HTML
- orice xlsx
- orice imagine
- STARE-CURENTA.md
- README.md
- CLAUDE.md
- governance / Bible
- orice artefact C01-C12

## REGULI
- Lucrează doar pe main.
- Nu crea branch.
- Nu crea PR.
- Nu modifica fișiere de conținut.
- Nu implementa nimic.
- Nu repara nimic.
- Nu inventa arhitectură nouă dacă nu o găsești în repo, marchează lipsa ca NEEDS DECISION.
- Nu confunda T3 cu C03.
- Nu reveni la T1 decât ca status scurt.

## LIVRABIL
Scrie raportul complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Mandat executat
3. Rezumat executiv
4. Fișiere citite
5. T1 status scurt
6. Harta T3 găsită în repo
7. Verdict C09-C12
8. Handoff C08 → C09
9. Audit diferențiere C09-C12
10. Status C10 WARNING / PASS
11. Graniță T3 → T4 → T5
12. Putem începe C09? PASS / WARNING / FAIL
13. Ce lipsește
14. Recomandare pentru următorul mandat BRAIN
15. Riscuri
16. Decizii cerute de la BRAIN
17. Commit / status Git

## MANDAT CURENT
Execută BRAIN-003-CORRECTED.
Realiniere pe TREAPTA 3 și pregătire C09.
Audit pur.
Zero modificări de conținut.
