# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-012-REV1

## MANDAT
C09 RELAȚII, REPARAȚIE UX înainte de HTML: simplifică Date_MASTER-C09.xlsx.

## DECIZIE BRAIN
Oprim temporar SLICE 2 HTML.

Motiv:
Date_MASTER-C09.xlsx are 13 foi. Pentru un master tehnic este justificabil, dar pentru experiența cursantului este prea mult.

Decizia finală BRAIN:
- 13 foi vizibile = prea mult.
- 9 foi vizibile = încă prea mult.
- C09 trebuie să fie simplă, clară, operațională.
- Cursantul trebuie să înțeleagă ideea mare: tabele separate → chei → relații → model care răspunde.

Înainte de HTML-Studiu, reparăm workbook-ul.

## OBIECTIV
Simplifică Date_MASTER-C09.xlsx și generatorul aferent astfel încât workbook-ul cursantului să aibă maximum 7 foi vizibile.

Ideal:
1. START
2. Vanzari
3. Produse
4. Clienti
5. Regiuni
6. Calendar
7. Relatii_Model

Dacă ai un motiv foarte puternic, poți folosi maximum 8 foi vizibile, dar trebuie justificat explicit.

## PRINCIPIU PEDAGOGIC
C09 nu este curs complet de data modeling.
C09 este construcția în care cursantul înțelege și execută relațiile.

Mesajul trebuie să fie:
"Tabelele nu sunt problema. Problema este că nu vorbesc între ele."

## CE TREBUIE SĂ FACI

### 1. Simplifică foile vizibile
Redu workbook-ul la maximum 7 foi vizibile.

Foile recomandate:
- START, ghid scurt al exercițiului
- Vanzari, fact principal
- Produse, dimensiune
- Clienti, dimensiune
- Regiuni, dimensiune
- Calendar, dimensiune
- Relatii_Model, foaie unificată pentru model, integritate și citire demo

### 2. Comasează foile tehnice
Comasează într-o singură foaie `Relatii_Model`:
- documentarea relațiilor
- verificările de integritate
- citirea demonstrativă cross-tabel
- handoff spre C10

Nu mai ține separat, vizibil:
- _MODEL
- _INTEGRITATE
- _CITIRE_DEMO
- CONTROL_FINAL

### 3. Elimină sau ascunde ce încarcă inutil
Elimină sau ascunde complet din experiența cursantului:
- AGENTI
- DEPOZITE
- _REL_CLIENTI
- orice helper tehnic care nu este necesar pedagogic

Dacă păstrezi foi helper ascunse, explică de ce. Dar scopul este să nu apară în experiența cursantului.

### 4. Actualizează generatorul
Actualizează _system/generatoare/build_date_master_c09.py astfel încât să regenereze workbook-ul simplificat.

Generatorul trebuie să rămână reproductibil.

### 5. Păstrează esența C09
Workbook-ul trebuie să păstreze:
- fact principal
- dimensiuni reale
- chei clare
- relații 1:M
- verificare orfani / cardinalitate
- prima citire demonstrativă cross-tabel
- sumă conservată
- zero măsuri DAX numite
- zero ranking
- zero dashboard
- zero cauză / explicație finală
- zero recomandări de acțiune

## INTERDICȚII
Nu implementa încă HTML-Studiu.
Nu implementa Editor-Studiu.
Nu implementa Video.
Nu implementa Editor-Video.
Nu implementa FILM.
Nu genera imagini.
Nu modifica governance.
Nu modifica C01-C08.
Nu modifica C10-C12.
Nu modifica gate_v20.py.
Nu modifica tier_guard_t3.py.

## FIȘIERE PERMISE LA MODIFICARE
Ai voie să modifici doar:
- c09/Date_MASTER-C09.xlsx
- _system/generatoare/build_date_master_c09.py
- c09/Creativ-Excel-09-Relatii.txt doar dacă trebuie corectată referința la foile workbook-ului
- CLAUDE-TO-BRAIN.md
- STARE-CURENTA.md doar dacă fluxul standard o cere

## VALIDĂRI CERUTE
Rulează:
1. Generatorul Date_MASTER-C09.
2. Verificare număr foi vizibile.
3. Verificare existență foi recomandate.
4. Verificare chei și relații documentate în Relatii_Model.
5. Verificare integritate: orfani, cardinalitate, sumă conservată.
6. Verificare că nu există măsuri DAX numite, ranking, dashboard, cauză, recomandare.
7. audit_sync.
8. tier_guard_t3 --self-test.
9. gate_v20 09 c09 c01 doar informativ, dacă HTML lipsește este acceptat.

## CRITERII DE PASS
Mandatul trece doar dacă:
1. Date_MASTER-C09.xlsx are maximum 7 foi vizibile, sau maximum 8 cu justificare puternică.
2. Experiența cursantului este simplă și clară.
3. Relatii_Model comasează modelul, integritatea și citirea demo.
4. AGENTI / DEPOZITE / helpers nu mai încarcă vizual workbook-ul.
5. C09 rămâne RELAȚII, nu C10/C11/C12/T4/T5.
6. Generatorul reproduce noul workbook.
7. audit_sync nu introduce regresii nejustificate.
8. Raportul explică exact ce foi rămân vizibile și de ce.

## LIVRABIL
Scrie raport complet în CLAUDE-TO-BRAIN.md.

## FORMAT RĂSPUNS CERUT
1. Status
2. Rezumat executiv
3. Fișiere citite
4. Fișiere modificate
5. Structura veche vs structura nouă
6. Lista foilor vizibile finale
7. Lista foilor eliminate / ascunse
8. Cum ai comasat _MODEL / _INTEGRITATE / _CITIRE_DEMO / CONTROL_FINAL
9. Cum ai păstrat esența C09
10. Validări rulate
11. Rezultate PASS / WARNING / FAIL
12. Ce rămâne pentru HTML-Studiu
13. Decizii cerute de la BRAIN
14. Commit / status Git

## MANDAT CURENT
Execută BRAIN-012-REV1.
Simplifică Date_MASTER-C09 înainte de HTML.
Zero HTML.
Zero FILM.
Zero imagini.
