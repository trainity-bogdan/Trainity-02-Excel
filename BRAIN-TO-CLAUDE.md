# BRAIN → CLAUDE

## STATUS
PENDING

## CUVÂNT CHEIE

SYNC

Când Bogdan scrie `SYNC` către Claude Code, Claude trebuie să citească acest fișier, să execute mandatul curent și să scrie raportul complet în `CLAUDE-TO-BRAIN.md`.

Când Bogdan scrie `SYNC` către BRAIN, BRAIN va citi `CLAUDE-TO-BRAIN.md`, va da verdictul și va pregăti următorul mandat în `BRAIN-TO-CLAUDE.md`, dacă este cazul.

## PROTOCOL
Acest fișier este canalul oficial prin care BRAIN, ChatGPT / Andrei, transmite mandate către Claude Code.

Regula de lucru:
- BRAIN definește arhitectura, auditul, decizia pedagogică și mandatul.
- Claude Code execută în repository.
- Claude Code nu schimbă arhitectura fără mandat explicit.
- Claude Code lucrează doar pe `main`, conform instrucțiunii lui Bogdan.
- Claude Code scrie răspunsul complet în `CLAUDE-TO-BRAIN.md`.
- Claude Code nu folosește conversația ca raport principal, ci fișierul `CLAUDE-TO-BRAIN.md`.

## FIȘIERE DE COMUNICARE

- `BRAIN-TO-CLAUDE.md` = instrucțiunile de la BRAIN către Claude.
- `CLAUDE-TO-BRAIN.md` = raportul de la Claude către BRAIN.

## REGULA DE AUR

Claude execută exact mandatul curent din acest fișier.
Dacă mandatul este ambiguu, Claude oprește execuția și scrie `NEEDS DECISION` în `CLAUDE-TO-BRAIN.md`.

## MANDAT-ID
BRAIN-001

## MANDAT
Audit adversarial final T1 după reparațiile FILM.

## CONTEXT
Auditul Monstruos a semnalat riscuri și FAIL-uri de formă în T1, în special pe FILM C02, C03 și C04:

- C02 și C04 aveau risc de boilerplate.
- C03 avea risc de template / voce neutră.
- C02 și C03 aveau risc de canibalizare conceptuală.
- T1 trebuie să rămână clar: C01 STRUCTURARE, C02 CONTROL, C03 AUDIT, C04 NORMALIZARE / AUTOMATIZARE.

Acest mandat este AUDIT PUR.
Nu modifica nimic.
Nu rescrie nimic.
Nu face commit-uri de conținut.
Doar citește, verifică și raportează.

## OBIECTIV
Verifică dacă FAIL-urile identificate în Auditul Monstruos pentru C02, C03 și C04 au fost închise efectiv.

## FIȘIERE PERMISE
Ai voie să citești toate artefactele necesare auditului T1, inclusiv:

- artefacte C01-C04
- fișiere FILM C01-C04
- HTML-Studiu C01-C04
- documente de guvernanță relevante
- STARE-CURENTA.md
- README.md
- CLAUDE.md
- orice audit intern relevant existent în repo

## FIȘIERE INTERZISE
- Nu modifica niciun fișier de conținut.
- Nu modifica HTML.
- Nu modifica FILM.
- Nu modifica xlsx.
- Nu modifica imagini.
- Nu modifica governance.

Singurul fișier pe care ai voie să îl scrii este:

- CLAUDE-TO-BRAIN.md

## AUDIT CERUT

### 1. C02 FILM
Verifică:
- mai există boilerplate?
- mai există câmpuri identice între etape?
- mai există voce generică?
- este C02 clar CONTROL, nu AUDIT?

### 2. C03 FILM
Verifică:
- mai există secțiuni template?
- mai există voce neutră?
- este diferențiat complet?
- este C03 clar AUDIT, nu CONTROL?

### 3. C04 FILM
Verifică:
- mai există boilerplate?
- este specific axei NORMALIZARE / AUTOMATIZARE?
- este clar diferit de C02/C03?

### 4. Diferențiere C02 vs C03
Răspunde explicit:
- poate un auditor extern să distingă instant C02 de C03?
- ce face C02 ce nu face C03?
- ce face C03 ce nu face C02?
- scor diferențiere 0-10

### 5. Reaudit T1
Dă verdict separat:

- C01: PASS / WARNING / FAIL
- C02: PASS / WARNING / FAIL
- C03: PASS / WARNING / FAIL
- C04: PASS / WARNING / FAIL
- T1 global: PASS / WARNING / FAIL

### 6. Probleme sistemice rămase
Verifică dacă mai există probleme deschise din Auditul Monstruos:
- boilerplate
- template drift
- form-drift
- canibalizare C02/C03
- voce generică
- contaminare cu trepte viitoare
- lipsă diferențiere între construcții

### 7. Listă finală
Produce trei liste clare:

- Probleme închise
- Probleme rămase
- Probleme noi descoperite

## REGULI
- Lucrează doar pe main.
- Nu crea branch nou.
- Nu crea PR.
- Nu modifica arhitectura locked fără mandat explicit.
- Nu redenumi concepte locked.
- Nu introduce termeni din trepte viitoare.
- Nu inventa conținut în afara mandatului.
- Raportează exact ce ai citit, ce ai verificat și ce verdict dai.
- Nu face rescrieri.
- Nu face reparații.
- Nu face commit-uri de conținut.

## LIVRABIL
Scrie răspunsul complet în `CLAUDE-TO-BRAIN.md`.

## FORMAT RĂSPUNS CERUT
1. Status
2. Mandat executat
3. Rezumat executiv
4. Fișiere citite
5. Fișiere modificate
6. Schimbări efectuate
7. Schimbări nefăcute
8. Teste / audituri rulate
9. Rezultate
10. Verdict C01-C04
11. Verdict T1 global
12. Probleme închise
13. Probleme rămase
14. Probleme noi descoperite
15. Riscuri rămase
16. Decizii cerute de la BRAIN
17. Commit / status Git

## MANDAT CURENT
Execută BRAIN-001.
Audit pur.
Zero modificări de conținut.
Raport complet în `CLAUDE-TO-BRAIN.md`.
