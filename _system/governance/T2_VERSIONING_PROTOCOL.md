# T2_VERSIONING_PROTOCOL.md · Control de versiuni

> Aliniat la disciplina git existentă a proiectului (commit descriptiv pe `main`,
> FĂRĂ tag-uri git — vezi CLAUDE.md G3). Acest document adaugă stratul de
> guvernanță: leagă fiecare modificare de poziția structurală + regula Bible.

---

## CONVENȚIE DE VERSIUNI (semantic, pe treaptă)

`T2 vMAJOR.MINOR.PATCH`

- **PATCH** (vX.Y.+1): corecție într-o singură construcție, fără impact transversal
  (element local — vezi T2_DNA §10). Ex: fix typo, ajustare poză.
- **MINOR** (vX.+1.0): modificare de poziție structurală **propagată transversal** pe
  toate construcțiile afectate. Ex: AUDIT→VERIFICARE pe C05+C06. Schimbă suprafața, nu
  arhitectura.
- **MAJOR** (v+1.0.0): schimbare de regulă în Bible, de schelet, de identitate locked,
  sau decizie arhitecturală structurală (ex: rezolvarea C06 E4). Necesită aprobare arhitect.

## MARCAREA UNEI MODIFICĂRI TRANSVERSALE
Orice MINOR/MAJOR transversal se notează în commit cu:
- poziția structurală atinsă (din T2_POSITION_MATRIX);
- regula Bible afectată (din T2_ARCHITECTURE_BIBLE);
- lista construcțiilor în care s-a propagat.

## LEGAREA DE BIBLE
Când o regulă din Bible se schimbă/adaugă → MAJOR + actualizare Bible + notare în
changelog + actualizare T2_DRIFT_DETECTOR (dacă regula e detectabilă).

## ISTORIC DE DECIZIE
Deciziile arhitecturale (cele din T2 + viitoare) se păstrează în changelog cu „Aprobat
de" + motiv. Nu se șterg; o decizie inversată = nouă linie, nu editare.

---

## FORMAT CHANGELOG (recomandat)

```
| Data | Fișier(e) | Poziție structurală | Regulă afectată | Tip (PATCH/MINOR/MAJOR) | Motiv | Propagat în | Aprobat de |
```

**Exemple reale (retroactiv, din sesiunea T2):**
```
| 2026-05-31 | c05,c06 Studiu+Editor | E4 nume etapă | R-TERM-1 | MINOR | scoate AUDIT (ADN C03) | C05,C06 | ARHITECT |
| 2026-05-31 | c05 Studiu+Editor | E5 phase-tag | R-TERM-2 | MINOR | RECALC→RECALCUL | C05 | motor |
| 2026-05-31 | c05,c06,c07 | confirmare E6 | R-TERM-4 | MINOR | conectat→ancorat | C05,C06,C07 | ARHITECT |
| 2026-05-31 | c06 4 machete | fenomen 03 | R-TERM-4 | MAJOR | XLOOKUP-aducere → etichetă derivată | C06 | ARHITECT |
| 2026-05-31 | 06-MAP | C08 secțiune | R-NAME-1 | MINOR | TIPIZARE→CARTOGRAFIERE | doc | ARHITECT |
```

## REGULA DE RESTAURARE
Conform CLAUDE.md G4: `git show <sha>:path`, `git checkout <sha> -- cNN/`, `git revert`.
Nu există tag-uri; commit descriptiv + acest changelog = trasabilitate completă.
