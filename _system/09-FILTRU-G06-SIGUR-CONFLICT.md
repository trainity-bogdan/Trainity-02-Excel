# 09 · FILTRUL SIGUR/CONFLICT (G-06) — procedură operațională

Versiune: V43 · Codificat ca document activ: 29 mai 2026
(anterior doar referențiat în CLAUDE.md + arhivă; acum document executabil în `_system/`)

Procedura prin care motorul tratează AUTOMAT orice feedback extern, fără să
ceară ARHITECTULUI cum să procedeze.

---

## 1. DEFINIȚIE
Orice feedback extern (alt model AI, ChatGPT, terți, articole, documente de
recomandare, sugestii din afara sistemului Trainity) este AUTOMAT clasificat
prin Filtrul Sigur/Conflict. Motorul NU întreabă „cum procedez cu feedbackul"
și NU pasează decizia înapoi. ARHITECT e arhitectul; clasificarea argumentată
e obligația motorului.

---

## 2. CELE TREI CLASE

### SIGUR
Aliniat cu: ADN-ul Trainity (vocabular, ton, identitate) · șablonul de aur
(C01 pilot) · SPEC-ul înghețat al construcției curente · sistemul (cele 7
artefacte, cele 3 invariante, regulile R-V*) · modelul operațional al
ARHITECTULUI (4h PC + 2h mobil, **versionare git**, etc.).
Include și corectarea erorilor reale semnalate de feedback.
ACȚIUNE: se APLICĂ direct, fără întrebare.

### CONFLICT
Rupe ADN-ul: vocabular interzis (em-dash, en-dash, anglicisme inutile) · ZERO
PDF (R-V03.15) · anti-clutter (R-V02.15 zero cifre business în HTML/FILM) ·
identitatea livrabilelor (cele 7 canonice) · modelul operațional declarat.
Abate de la: șablonul de aur · cele 22 funcții / 12 capabilități · SPEC-ul
înghețat · cifrele canonice (nicio cifră nu se repetă între construcții) ·
**granița între trepte** (ex. o construcție T2 care face muncă de T3).
Introduce: decorativ / dashboard fake / hype · dependențe externe care
contrazic modelul ARHITECTULUI · compromisuri pe confidențialitate fără mandat.
ACȚIUNE: se RESPINGE cu argument explicit documentat în răspuns.

### NEUTRU
Deja implementat în sistem, sau fără efect material asupra livrabilelor.
ACȚIUNE: se notează scurt, fără execuție.

---

## 3. PROCEDURA (pas cu pas)
1. **DETECȚIE** — mesajul conține feedback extern? (citează alt AI, lipește
   articol/recomandare, „ce zici de asta?" cu sursă externă, opțiune tehnică
   găsită aiurea).
2. **SPARGE PE PUNCTE** — fiecare sugestie se clasifică separat.
3. **CLASIFICĂ** — aliniat cu ADN+șablon+SPEC+sistem+model → SIGUR; rupe/abate/
   introduce conflict → CONFLICT (cu argument: ce rupe, de ce); deja făcut/fără
   efect → NEUTRU.
4. **LIVRARE** — format:
   ```
   FILTRU G-06 aplicat:
   Punct 1: [rezumat] → SIGUR/CONFLICT/NEUTRU
     [dacă CONFLICT: argumentul exact ce rupe]
   Punct 2: ...
   ```
5. **EXECUȚIE IMEDIATĂ** — SIGUR se aplică direct; CONFLICT se respinge în
   răspuns; NEUTRU se notează.
6. **REVIZUIRE OPȚIONALĂ** — dacă ARHITECT nu e de acord cu o clasificare, o
   spune; motor reanalizează ACEL punct, nu reia tot filtrul.

---

## 4. CE NU SE FACE
- NU se cere confirmare înainte de aplicarea părții SIGURE.
- NU se pasează decizia înapoi cu „ce zici?".
- NU se prezintă variante A/B/C la decizii evidente.
- NU se ezită din politețe față de sursa externă.
- NU se acceptă tăcut un CONFLICT pentru că „sună bine".
- NU se promovează soluții netestate ca SIGURE.

---

## 5. EXEMPLE
- CONFLICT: „GitHub Pages public ca să vezi HTML pe telefon" → expune produsul
  comercial confidențial. Respins. (Notă V42: Pages e activ DAR cu robots.txt +
  noindex; decizie explicită ARHITECT, nu feedback extern.)
- CONFLICT (graniță trepte): „C08 face join-uri și Data Model" → e muncă de T3
  (C09), rupe granița T2 descriptiv vs T3 relațional. Respins / redirecționat.
- SIGUR: „git privat ca punte PC↔mobil, commit/push gestionat de motor" →
  aliniat cu modelul, păstrează confidențialitatea. Aplicat.
- NEUTRU: „cere Remote Control la suport" → deja făcut, fără efect pe livrabile.

---

## 6. AUTO-APLICARE (meta)
G-06 se aplică AUTOMAT la fiecare feedback extern, fără cerere explicită. Semnal
de aplicare corectă: răspunsul conține „FILTRU G-06 aplicat:" + clasificare pe
puncte. Dacă motor scapă, ARHITECT poate cere „aplică G-06 retroactiv pe
ultimele N mesaje".

## 7. INTEGRARE CU CONSOLIDARE BRAIN
La fiecare `consolidează brain`: motor revede dacă au existat feedback-uri
externe netratate; dacă da, aplică retroactiv + documentează lecție; dacă apare
o clasă nouă de feedback, codifică sub-tip nou aici + crește versiunea.

---

FINAL: G-06 menține integritatea sistemului Trainity împotriva contaminării cu
sugestii externe nealiniate. Aplicare automată, argumentată, nereversibilă fără
mandat explicit al ARHITECTULUI.
