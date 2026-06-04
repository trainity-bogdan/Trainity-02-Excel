# BRAIN → CLAUDE · C10 MĂSURI

## STATUS
AUDIT_BRAIN_REFINEMENT_REQUIRED

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C10.

La comanda `sync`, citește:
- `_brain/c10/CHAT-CONTEXT.md`
- `_brain/c10/BRAIN-TO-CLAUDE.md`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

---

# AUDIT BRAIN C10

C10 este aprobat structural. Setul este generat complet și toate gate-urile trec.

Nu refacem arhitectura.
Nu schimbăm SPEC-ul.
Nu schimbăm cele 6 fenomene.
Nu introducem ranking, contribuție, comparație contextuală, ABC, Pareto, cauză sau dashboard.

Se cere doar polish pedagogic și operațional.

## VERDICT

C10 este bun, coerent, validat tehnic și aliniat pe axa:
- C10 = MĂSURI
- verb = a defini
- întrebare-mamă = Cât?
- C11 = comparații

Nota BRAIN actuală: 8.6 / 10.
Țintă după rafinare: 9.2 / 10.

---

# CE RĂMÂNE NESCHIMBAT

Păstrează:
- hero-ul: "Cât? Și cum definesc o măsură care răspunde corect de fiecare dată?"
- intriga: "Ai toate cifrele. Și nicio decizie."
- mantra: "Măsura corectă răspunde întrebării corecte."
- motto: "Nu calcula mai mult. Măsoară mai corect."
- cele 6 fenomene C10
- cele 8 verificări finale
- predarea explicită către C11
- zero cifre business în HTML/FILM

---

# CORECȚII CERUTE

## 1. Fă pașii 7-12 mai operaționali

În pașii 7, 8, 9, 10, 11, 12, adaugă micro-instrucțiuni concrete de lucru în Excel.

Nu te limita la principii. Cursantul trebuie să simtă că face efectiv ceva în fișier.

Direcție:
- deschide foaia Masuri
- identifică rândul măsurii
- completează/verifică întrebarea
- completează/verifică definiția
- completează/verifică baza
- completează/verifică reperul
- verifică semnalul
- verifică aceeași definiție în Masuri_Context

Nu introduce cifre business în HTML.

## 2. Întărește etapa 5

Etapa 5 este prea abstractă.

Păstrează ideea:
- definiția trăiește într-un singur loc
- rândul nou intră singur
- sursa nouă nu rupe măsura

Dar rescrie pașii 13-15 ca mini-demonstrație clară:
- înainte: măsură prinsă într-un calcul ad-hoc / interval / celule copiate
- după: măsură definită o singură dată peste model
- test: rând nou intră fără rescriere
- test: luna următoare nu schimbă definiția

## 3. Curăță etichetele moștenite

În Etapa 4, înlocuiește tagul:
"Funcții de validare"
cu:
"Controlul măsurii"

În Etapa 5, înlocuiește tagul:
"Tabel structurat"
cu:
"Definiție stabilă"
sau:
"Sursă unică"

Alege varianta cea mai coerentă în HTML.

## 4. Curăță Promptul 2 de drift spre C11

În Promptul 2, evită formularea cu:
"clasamentul și diferențele între felii"

Înlocuiește cu:
"Nu interpreta diferențele dintre felii. În această etapă verific doar definiția măsurii, baza, reperul și robustețea ei."

## 5. Întărește delimitarea C10-C11 în Pasul 10

După explicația despre context-awareness, adaugă ideea:

"Nu verificăm care felie este mai bună. Verificăm dacă aceeași măsură funcționează pe orice felie."

## 6. Întărește delimitarea C10-C12 în Pasul 12

Adaugă ideea:

"Semnalul nu spune încă de ce s-a întâmplat ceva. Semnalul spune doar că măsura este citibilă, explicabilă și pregătită pentru interpretare."

---

# LIVRABILE DE MODIFICAT

Modifică în principal:
- c10/HTML-Studiu-Excel-10-Masuri.html
- c10/HTML-Editor-Studiu-Excel-10-Masuri.html, dacă este companion 1:1 și trebuie sincronizat
- c10/HTML-Video-Excel-10-Masuri.html, doar dacă aceleași formulări apar și acolo
- c10/HTML-Editor-Video-Excel-10-Masuri.html, dacă este companion 1:1
- FILM-Excel-10-Masuri.docx, dacă scriptul video conține aceleași formulări afectate

Nu modifica Date_MASTER-C10.xlsx decât dacă descoperi inconsistență reală. Din auditul BRAIN, Date_MASTER pare validat și nu necesită schimbare.

---

# POST-CHECK OBLIGATORIU

După rafinare:
- rulează gate_v20 pentru C10
- rulează audit_sync
- rulează tier_guard_t3
- confirmă zero drift față de SPEC
- actualizează CLAUDE-TO-BRAIN.md cu raportul de rafinare

## STATUS AȘTEPTAT ÎN CLAUDE-TO-BRAIN

REFINED_AFTER_BRAIN_AUDIT · PASS
