# NO_DESTRUCTIVE_WRITES · Regulă SYSTEM

## De ce există

În 4 iunie 2026, fișierul `_system/arhiva/SISTEM_TRAINITY-versiuni.md` a fost trunchiat accidental prin folosirea unui overwrite complet pe un fișier SYSTEM mare, fără conținut complet disponibil și fără gardă de linie.

Această regulă previne repetarea incidentului.

## Regulă hard

Pentru orice fișier SYSTEM critic sau orice fișier peste 300 de linii:

1. Este interzis overwrite-ul complet prin connector sau tool care cere `content` complet, dacă răspunsul sursă este trunchiat.
2. Este interzis write direct pe `main` pentru fișiere SYSTEM mari.
3. Orice modificare trebuie făcută ca patch minimal, pe branch separat, cu diff verificat.
4. Dacă tool-ul afișează `truncated`, operația de write se oprește imediat.
5. Pentru fișierele de registru/arhivă SYSTEM, trebuie verificat numărul de linii înainte și după modificare.

## Comenzi minime de preflight

```bash
git status
wc -l _system/arhiva/SISTEM_TRAINITY-versiuni.md
grep -n "PARTEA VI - SPEC INGHETAT CONSTRUCTII" _system/arhiva/SISTEM_TRAINITY-versiuni.md
grep -n "## SPEC C01" _system/arhiva/SISTEM_TRAINITY-versiuni.md
grep -n "## SPEC C08" _system/arhiva/SISTEM_TRAINITY-versiuni.md
```

## Comenzi minime postflight

```bash
git diff --stat
git diff -- _system/arhiva/SISTEM_TRAINITY-versiuni.md
wc -l _system/arhiva/SISTEM_TRAINITY-versiuni.md
```

## Condiții de oprire

Oprește imediat operația dacă:

- fișierul are sub 5.000 de linii după modificare,
- lipsesc markerii `## SPEC C01`, `## SPEC C08` sau `PARTEA VI - SPEC INGHETAT CONSTRUCTII`,
- diff-ul arată ștergere masivă neintenționată,
- operația propusă este overwrite complet pe fișier SYSTEM mare.

## Regulă pentru Andrei SYSTEM

Andrei SYSTEM nu mai execută overwrite complet pe fișiere SYSTEM mari prin GitHub connector.

Permis:
- citire,
- audit,
- creare fișier mic de gardă,
- propunere patch,
- branch/PR controlat dacă tool-ul permite diff complet.

Interzis:
- update_file direct pe registru SYSTEM mare,
- rescriere completă când conținutul este trunchiat,
- modificare directă pe main fără verificări.
