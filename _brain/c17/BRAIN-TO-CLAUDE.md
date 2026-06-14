# BRAIN -> CLAUDE C17

## STATUS
MANDAT_REVIZUIRE_BLUEPRINT_C17

## CONTEXT
C17 Blueprint a fost propus si este in review BRAIN.
Status curent in _brain/c17/CLAUDE-TO-BRAIN.md:
C17_BLUEPRINT_READY_FOR_REVIEW.

Observatii BRAIN:
- Slug-ul propus `Sistematizare` este compatibil cu identitatea C17.
- Blueprint-ul are 6 etape si 18 pasi.
- Structura `_SISTEM` este suficient de concreta pentru review: blocuri A-F, named ranges, hyperlink-uri, formule vii, START AICI, punct de reluare, test anti-SOP.
- Testele sunt prezente: anti-SOP, substitut, anti-C18, anti-C19, anti-C20, filmabilitate.

Riscuri de corectat punctual:
1. In etapa 2 apare formularea "cartografiezi componentele reale". Risc ecou C08. Inlocuieste cu "inventariezi functional componentele reale".
2. Unde "harta reluabila" risca ecou C08, foloseste "structura reluabila" sau "harta functionala" doar daca e clar legata de workbook.
3. In etapa 5 apare "praguri de proces". Risc C19. Inlocuieste cu "conventii de proces".
4. Unde apare "rol", clarifica: "profil de competenta, nu ownership".
5. `FORMULATEXT`, `ROWS`, `COUNTA` si referintele live trebuie confirmate explicit ca oglinzi de stare, nu reguli, nu validari, nu control C19.

## MANDAT
Revizuieste punctual blueprint-ul C17 in:
_brain/c17/CLAUDE-TO-BRAIN.md

Nu modifica sistemul.
Nu genera artefacte.
Nu crea folder `c17/`.
Nu intra in HTML, Date_MASTER, build scripts sau FILM.
Nu intra in C18.

Aplică urmatoarele corectii:

1. Inlocuieste formularea:
"cartografiezi componentele reale"
cu:
"inventariezi functional componentele reale"

2. Inlocuieste:
"harta reluabila"
unde risca ecou C08,
cu:
"structura reluabila" sau "harta functionala", doar daca e clar legata de workbook.

3. In etapa 5, inlocuieste:
"praguri de proces"
cu:
"conventii de proces"

4. In toate locurile unde apare "rol", clarifica:
"profil de competenta, nu ownership".

5. Confirma explicit ca `FORMULATEXT`, `ROWS`, `COUNTA` si referintele live sunt:
oglinzi de stare, nu reguli, nu validari, nu control C19.

Dupa corectii:
- re-ruleaza audit intern pe C08/C18/C19/C20;
- verifica anti-SOP;
- verifica filmabilitatea;
- verifica zero em-dash;
- pastreaza verdictul doar daca este justificat.

## OUTPUT CERUT
CLAUDE -> BRAIN

Include:
- ce ai schimbat;
- ce riscuri ai inchis;
- audit intern C08/C18/C19/C20;
- verdict final:

C17_BLUEPRINT_CONFIRMED

sau

C17_BLUEPRINT_NEEDS_REVISION
