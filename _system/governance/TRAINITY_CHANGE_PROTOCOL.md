# TRAINITY_CHANGE_PROTOCOL.md · Modificare fără drift + changelog

> **REGULA DE AUR:** nicio modificare locală fără întrebarea:
> *„Ce poziții structurale echivalente sunt afectate în celelalte construcții?"*
> Acesta e mecanismul care previne driftul T2 (fix-uri secvențiale nepropagate).
> *(Absoarbe fostul T2_VERSIONING_PROTOCOL — vezi §Changelog.)*

---

## CELE 7 ETAPE ALE ORICĂREI MODIFICĂRI

1. **CHANGE REQUEST** — ce, în ce construcție observat, de ce. Tip: terminologic /
   structural / pedagogic / metodologic / handoff / retoric / hero.
2. **IMPACT ANALYSIS** — întrebări: e poziție structurală (Position Matrix)? regulă SACRĂ
   (Bible §SHARED)? identitate locked (S5)? atinge garda treptei (§TIER)?
3. **POSITION MAPPING** — localizează poziția în Position Matrix; găsește echivalentul în
   toate construcțiile treptei. Dacă NU e în matrice → element local → modificare punctuală OK.
4. **TRANSVERSAL PROPAGATION** — aplici pe TOATE construcțiile cu acea poziție, în aceeași
   pasă, NU secvențial. *(Lecția T2: AUDIT→VERIFICARE aplicat doar la C07/C08 a creat split.)*
5. **DRIFT CHECK** — rulează Detector (checklist relevant). Confirmă uniformitate transversală.
6. **RELEASE GATE** — treci gate-urile afectate.
7. **APPROVAL + CHANGELOG** — ARHITECT aprobă unde e cerut; înregistrezi în changelog.

**Anti-pattern interzis:** „Am observat X în C0N, repar doar C0N." → INTERZIS dacă X e
poziție structurală. Orice fix de poziție = pasă transversală.

## EXEMPLE (din istoric T2)
- Nume etapă (AUDIT→VERIFICARE): poziție E4 → toate 4. *Greșeala: aplicat doar C07/C08.*
- phase-tag (RECALC→RECALCUL): poziție E5 → verifică toate 4.
- handoff („Setul vine"→„Setul predat de"): poziție PAS 01 → toate 4.
- completion (scoate „auditabil"): poziție completion-title → toate 4.
- verificare E4 (C06 construiește): NU propagare mecanică → decizie arhitecturală.

---

## §CHANGELOG (înlocuiește versionarea semantică — fără MAJOR/MINOR/PATCH)

> Trasabilitate prin commit descriptiv pe `main` + acest tabel (aliniat CLAUDE.md G3:
> FĂRĂ tag-uri git, FĂRĂ numere de versiune). Restore = `git show/checkout/revert`.

```
| Data | Fișier(e) | Poziție structurală | Regulă (ID) | Propagat în | Aprobat de |
```

**Tip modificare** (descriptiv, nu numeric):
- **locală** — o singură construcție, element non-structural.
- **transversală** — poziție structurală propagată pe toate construcțiile treptei.
- **regulă** — schimbare în Bible (necesită aprobare arhitect + actualizare Detector dacă e detectabilă).
- **seed** — pornire treaptă nouă (secțiune §TIER nouă, prin TIER SEED).

**Istoric retroactiv T2:**
```
| 2026-05-31 | c05,c06 | E4 nume etapă | R-TERM-1 | C05,C06 | ARHITECT | transversală |
| 2026-05-31 | c05 | E5 phase-tag | R-TERM-2 | C05 | motor | transversală |
| 2026-05-31 | c05,c06,c07 | confirmare E6 | R-TERM-5/garda | C05,C06,C07 | ARHITECT | transversală |
| 2026-05-31 | c06 | fenomen 03 | garda §T2 (XLOOKUP) | C06 | ARHITECT | regulă+local |
| 2026-05-31 | 06-MAP | C08 secțiune | R-NAME-1 | doc | ARHITECT | regulă |
| 2026-05-31 | Bible §T3 | inițiere treaptă T3 | R-SEED-1/2/3, R-TIER-PARAM | §T3 (identitate+gardă+AHA C09) | ARHITECT | seed |
```
