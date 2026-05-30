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
| V45 | c9bf784 | 29 mai 2026 | Re-arhitectură T2 (după feedback extern via G-06): C05 CLASIFICARE→DICȚIONAR (rename, conținut=inventar) + C06 CUANTIFICARE→CLASIFICARE (REBUILD: reguli IFS/SWITCH/XLOOKUP/scor, coloane derivate clasa_valoare/segment_produs/scor). Cele 4 obiecte T2 distincte: dicționar/clasificare/memorie/ecosistem. Gardă T2/T3 (etichetare descriptivă ≠ prioritizare strategică=C11). Rafinări C07/C08 + rol „CONTROL UMAN" (eliminat „operatorul" din toate 8 FILM-urile). Meta-list propagată. Lecții L167-L168. Audit 80/80 ZERO DRIFT. |
| V46 | 02bc0fb | 30 mai 2026 | Sistem sincronizare FILM↔HTML: mapare canonică câmp→slot în `_system/10-MAP-FILM-HTML.md` (FILM=master, „update html" mecanic). Sloturi noi: WOW (climax verde `.payoff-wow` + etichetă „WOW:", `[data-wow]`) + CONTRACT (destinație, `exec-hero [data-contract]`, copy draft). Sincronizate complet C01-C04 (identitate + 6 exec slides + WOW + CONTRACT, 4 machete fiecare). FILM C02/C03/C04 reparate diacritic + typo „.." (docx returnate ARHITECT). C01 rezolvat (sync HTML←FILM, reparat confuzia rol mantra/motto). L169: C01 nu era special — lipsea FILM proaspăt. C01 ulterior VALIDAT (FILM trimis de ARHITECT = byte-identic cu repo, sync confirmat corect; L170). Audit 80/80 ZERO DRIFT. |
| V47 | 98e4bfb | 30 mai 2026 | Redesign experiență C01 = model premium validat. HERO COCKPIT (poster+cockpit în ecran 1: imagine-obiect schelă STRUCTURĂ + întrebare + hartă T1 simplificată; topbar păstrat). ARC transformare cursant cu DOUĂ VOCI simțite (TU închis/persoana II vs DATE deschis/tehnic, fără etichete): titlu+miză → BOMBA „Arată ca tabel. Nu este unul." (memoria 24h) → recunoaștere→greșeală→AHA(vârf)→CINE DEVII → demonstrație+pași → DUPĂ C01 POȚI + DE ACUM ÎNAINTE (gated, bookend cu CINE DEVII). Ierarhie 3-1-1. FILM C01 = Biblia SPEC v2.0 (4 secțiuni) + CINE DEVII. Randator headless Chromium/Playwright (verificare mobil+desktop înainte de livrare). Lecții L171 (verifică randat, nu orb) + L172 (design=scădere+o idee). Doar C01 (model de propagat în C02-C08). Audit 80/80 ZERO DRIFT. |

> Versiunile V01-V42 nu au fost marcate cu SHA (istoric în `_system/arhiva/`
> + STARE-CURENTA). Înregistrarea pe SHA începe de la V43.
