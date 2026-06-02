# BRAIN → CLAUDE

## STATUS
READY

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

## FORMAT MANDAT

Fiecare mandat viitor va avea această structură:

```md
# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-YYYY-MM-DD-XXX

## MANDAT
[ce trebuie executat]

## CONTEXT
[contextul arhitectural necesar]

## FIȘIERE PERMISE
- ...

## FIȘIERE INTERZISE
- ...

## REGULI
- Lucrează doar pe main.
- Nu crea branch nou.
- Nu crea PR.
- Nu modifica arhitectura locked fără mandat explicit.
- Nu redenumi concepte locked.
- Nu introduce termeni din trepte viitoare.
- Nu inventa conținut în afara mandatului.
- Raportează exact ce ai citit, ce ai schimbat și ce a rămas neschimbat.

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
10. Riscuri rămase
11. Decizii cerute de la BRAIN
12. Commit / status Git
```

## MANDAT CURENT
Nu există mandat de execuție activ.
Așteaptă următoarea actualizare de la BRAIN.
