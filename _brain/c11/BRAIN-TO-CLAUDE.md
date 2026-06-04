# BRAIN → CLAUDE · C11 COMPARAȚII / RANK

## STATUS
MANDAT_GENERARE_ACTIV

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C11.

La comanda `sync`, citește:
- `_brain/c11/CHAT-CONTEXT.md`
- `_brain/c11/BRAIN-TO-CLAUDE.md`

Execută doar în:
- `c11/**`
- `_brain/c11/**`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C11
C11 este construcția COMPARAȚII / RANK.
SPEC C11 este înghețat.
SYSTEM fix pentru C11 a fost recepționat de Claude, iar C11 așteaptă mandat de generare.
Este activ mandatul de generare C11.

## MANDAT C11-05 · CONFIRMARE DECIZII MICI + GENERARE C11

### STATUS
MANDAT_GENERARE_ACTIV

### DECIZII BRAIN CONFIRMATE
1. Hero C11 se face pe 2 rânduri:

`CINE CONDUCE`
`IERARHIA DIN DATE`

2. `nume_slug` se confirmă cu majusculă inițială, conform convenției C10:

`Comparatii`

### OBIECTIV
Pornește COPY+MODIFY din `c01/` pentru generarea C11.

Generează construcția C11 COMPARAȚII / RANK pe baza SPEC C11 înghețat și a deciziilor BRAIN de mai sus.

C11 trebuie să livreze ideea centrală:
`Nu citi lista. Citește ierarhia.`

### SPEC C11 ÎNGHEȚAT

#### 1. SLUG
`comparatii`

#### 2. INTRIGA
Datele sunt legate corect și măsurate corect. Totuși o listă de măsuri, oricât de corectă, rămâne o masă plată. Ochiul nu poate ierarhiza singur o coloană lungă de numere, iar `mare în listă` este confundat cu `important pentru rezultat`.

C11 face trecerea de la `avem măsuri corecte` la `știm cine contează`, de la listă plată la ierarhie clară.

#### 3. PROBLEMELE
- citești lista fără să vezi cine conduce rezultatul
- compari valori care nu sunt comparabile
- confunzi `mare în listă` cu `important pentru rezultat`
- tratezi toate elementele ca egale, fără ierarhie
- reacționezi la diferențe minuscule, unde zgomotul pare semnal
- nu vezi concentrarea, adică puțini actori duc majoritatea rezultatului
- ignori contribuția în total
- decizi pe baza ordinii brute, fără reper relativ

#### 4. MIZA
Transformi măsurile corecte într-o ierarhie decizională. Vezi cine duce rezultatul și cine doar apare în listă.

Fără comparație, analiza rămâne plată. Cu comparație, datele capătă ierarhie.

#### 5. MANTRA
Nu toate valorile sunt egale. Unele conduc rezultatul.

#### 6. WOW
Într-un set cu multe elemente, de obicei o mână duce majoritatea rezultatului. Comparația corectă arată că `mult` și `important` nu sunt același lucru. Lista plată ascunde o ierarhie dură, în care câțiva actori decid totul.

#### 7. MOTTO
Nu citi lista. Citește ierarhia.

#### 8. FENOMENE
1. Clasamentul: ordonarea actorilor după o măsură.
2. Diferența reală vs zgomotul: contează gap-ul dintre poziții, nu doar ordinea.
3. Contribuția / ponderea în total: vezi cât duce fiecare actor din rezultatul global.
4. Concentrarea Pareto / ABC: puțini actori duc majoritatea rezultatului.
5. Comparabilitatea: compari doar ce are aceeași bază, unitate, perioadă și numitor.
6. Reperul relativ: poziția capătă sens raportată la lider, mediană sau grup.

#### 9. STEP-TITLES
1. Confirmă măsura pe care compari
2. Asigură comparabilitatea
3. Așază actorii în clasament
4. Citește diferențele reale
5. Calculează contribuția în total
6. Identifică concentrarea
7. Raportează poziția la reper
8. Confirmă ierarhia decizională

### REGULĂ VOCABULAR ȘI ADRESARE C11
În HTML-Studiu și în textele de experiență se folosește adresarea directă cu `tu`.

Cuvinte interzise:
- `cursant`
- `cursantul`
- `participant`
- `participantul`
- `elev`
- `student`

Nu se folosesc formule de tip:
- `cursantul vede`
- `participantul înțelege`
- `utilizatorul descoperă`

Se reformulează direct:
- `vezi`
- `compari`
- `confirmi`
- `construiești`
- `identifici`
- `citești ierarhia`

În FILM se poate folosi punctual `noi`, doar pentru ghidarea demonstrației, dar nu ca ton general de training.

C11 trebuie să sune business, operațional, direct, nu școlar.

### DELIMITĂRI HARD
C11 NU redefinește măsura. Măsura vine din C10.
C11 NU explică de ce apare ierarhia. Cauza rămâne pentru C12.
C11 NU construiește dashboard. Raportarea rămâne pentru T4.
C11 compară actori agregați, nu etichetează rânduri individuale.

### INSTRUCȚIUNI DE GENERARE
Generează `c11/` respectând arhitectura curentă a construcțiilor.
Folosește COPY+MODIFY din `c01/`.
Nu modifica matrița `c01/`.
Nu modifica alte construcții.

După generare, aplică obligatoriu un post-copy/post-generation pass pentru:
- eliminarea completă a cuvintelor interzise
- adresare directă cu `tu` în HTML-Studiu și textele de experiență
- folosirea controlată a lui `noi` doar în FILM
- eliminarea oricărei formulări școlare
- păstrarea delimitării C11 față de C10 și C12

### VALIDĂRI OBLIGATORII
După generare:
1. Scanează toate fișierele C11 pentru cuvintele interzise:
   - `cursant`
   - `cursantul`
   - `participant`
   - `participantul`
   - `elev`
   - `student`
2. Scanează pentru adresare indirectă de tip `utilizatorul`, `persoana`, `cel care` și reformulează direct cu `tu`, unde apare în text de experiență.
3. Verifică să nu existe `de ce`, `explică`, `cauză`, `motiv` ca axă narativă C11. Acestea aparțin C12.
4. Verifică să nu existe dashboard sau raportare T4 ca livrare C11.
5. Rulează validările permise de sistem pentru C11.

### RESTRICȚII
Nu modifica `CLAUDE.md`.
Nu modifica `README.md`.
Nu modifica `STARE-CURENTA.md`.
Nu modifica `index.html`.
Nu modifica `_system/generatoare/**`.
Nu modifica alte construcții.
Nu executa nimic în afara:
- `c11/**`
- `_brain/c11/**`

Dacă apare nevoie de sistem, scrie CERERE SYSTEM în `_brain/c11/CLAUDE-TO-BRAIN.md` și oprește acea parte.

### LIVRARE CERUTĂ
Actualizează `_brain/c11/CLAUDE-TO-BRAIN.md` cu:
- status generare
- lista fișierelor C11 create/modificate
- rezultat scan vocabular interzis
- rezultat delimitări C10/C12/T4
- rezultat validări
- eventuale CERERI SYSTEM
