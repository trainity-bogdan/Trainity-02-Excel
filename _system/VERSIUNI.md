# Registru versiuni · Pack 02 Excel

Marker oficial de versiune întreținut în repo (înlocuiește tag-urile git, care
nu pot fi împinse din mediul de execuție remote — proxy-ul acceptă doar branch-uri).

„Snapshot oficial V{N}" = commit-ul SHA înregistrat aici. Restore:
`git checkout <sha>` sau `git checkout <sha> -- <cale>`.

Dacă ARHITECT vrea și tag git pe GitHub, îl creează manual de pe mașina lui:
`git tag -a v{N} <sha> -m "..."` + `git push origin v{N}`.

| Versiune | Commit SHA | Data | Sumar |
|---|---|---|---|
| V43 | a2cdc3b | 29 mai 2026 | C06 CUANTIFICARE livrat (6/20, 30%) · fix layout buton continue/scroll (matriță+C01-C06) · drift exec video reparat C03/C05/C06 + detector R-V03.71 anti-clonă exec video · procedura 08 generare/validare + workflow FILM-ca-sursă · secțiune SLIDES EXECUTIVE în toate FILM-urile · set texte C06 rafinat (round-trip PASS). Audit 60/60 ZERO DRIFT. |
| V44 | a95745b | 29 mai 2026 | T2 CUNOAȘTERE COMPLET (8/20, 40%) · C07 DATARE/MEMORIA SETULUI (axă temporală) + C08 CARTOGRAFIERE/HARTA ECOSISTEMULUI (axă relațională descriptivă, recunoaștere ≠ modelare) · naming TIPIZARE→CARTOGRAFIERE + meta-list propagată C05-C08 · delimitare obsesivă C07/C08 + C08↔C09 lock în 06-MAP · G-06 codificat ca doc 09 · rafinări ARHITECT (voce impersonală, motto-uri, fenomene) · lecții L164-L166. Audit 80/80 ZERO DRIFT. |

> Versiunile V01-V42 nu au fost marcate cu SHA (istoric în `_system/arhiva/`
> + STARE-CURENTA). Înregistrarea pe SHA începe de la V43.
