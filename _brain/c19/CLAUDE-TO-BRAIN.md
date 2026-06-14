# CLAUDE -> BRAIN C19

## STATUS
C19_GENERARE_SLICE_3_HTML_VIDEO (HTML-Video + HTML-Editor-Video C19 generate si verificate; imagini DRAFT placeholder; NU release complet)

SURSA: mandat `MANDAT_SLICE_3_HTML_VIDEO` (origin/main ec5f86d). Build-scripturi in `c19/` (pattern c17 broadcast). Verificat independent (eu) peste self-verify-ul generatorului.

---

## SLICE 3 ARTEFACTE GENERATE
- **`c19/HTML-Video-Excel-19-Guvernare.html`** (~101 KB) - GENERAT + verificat.
- **`c19/HTML-Editor-Video-Excel-19-Guvernare.html`** (~112 KB) - GENERAT + verificat (companion, body+STAGES identice cu Video + strat editor).
- Build-scripturi: `c19/build_html_video_c19.py`, `c19/build_html_editor_video_c19.py`.
- Ramase (Slice 4): FILM + assets finale.

## SURSA VIDEO
Pattern build-script `c17` broadcast (head+CSS+JS din sibling Video, inlocuiesc BODY scaffolding + `const STAGES[]` + `const PROMPTS{}` + STORAGE_KEY + title + exec placeholders). Sibling = `c18/HTML-Video` (head/CSS/JS). **BODY scris CURAT pentru C19** (NU mostenit body-ul c18 care avea leftover clona c01 "Constructia 01"/AUTOMATIZARE). Editor = body+STAGES identice cu Video + head/tail editor din c18 Editor-Video.

## IDENTITATE C19 IN VIDEO
8/8 sloturi locked VERBATIM (verificat NFC): hov-object, HERO, BOMBA, MANTRA, WOW, MOTTO, **GRESEALA** (reparata: mutata in span data-locked verbatim `Confunzi «merge» cu «merge corect».`), AHA. Cele 6 etape verbatim + 18 step-titles in STAGES + 2 prompturi Copilot. title `C19 · GUVERNARE · BROADCAST`, topbar `C19 · Guvernare`, localStorage `trainity_c19_video_v1`, NEXT `Delegarea` (C20). Arc: input gresit -> regula -> prag/stare -> exceptie -> oprire controlata -> testul ochilor inchisi.

## DATE_MASTER FOLOSIT
`c19/Date_MASTER-C19.xlsx` (`_GUVERNARE`) ca sursa de adevar. Explicat in video: `STATUS=OPRIT` INTENTIONAT; `_GUVERNARE` prinde anomaliile pe care motorul C18 le-ar fi lasat tacit; C19 NU repara motorul, il tine corect prin reguli; fail-safe BLOCHEAZA rezultatul corupt. Zero cifre business in pagina (R-V02.15).

## STATUS IMAGINI
**DRAFT_IMAGINI_FALLBACK.** Cele 6 exec-stage + hero = SVG placeholder inline (axa CONTROL: REALITATE/DEVIATII/REGULA/PRAG-SEMNAL/OPRIRE/TEST). **ZERO base64 JPEG clona** (verificat: 0; dimensiuni ~101/112 KB, nu ~800 KB ca c18 cu clone). NU declar hash imagini PASS.

## VALIDARI SLICE 3 (rulate)
- Existenta HTML-Video + HTML-Editor-Video C19: **PASS** (ambele HTML valide, inchidere `</html>`).
- Identitate C19 locked in Video: **PASS** (8/8 sloturi verbatim dupa fix GRESEALA).
- Cele 6 etape: **PASS** (6/6 verbatim). 18 step-titles + 2 prompturi: **PASS**.
- Arcul video: **PASS** (6/6).
- Etapa 4 = semnal care schimba starea (nu dashboard): **PASS**.
- Etapa 5 = oprire automata (nu interventie umana): **PASS** (fail-safe, fara responsabil; "responsabil" apare doar in granita C20 verbatim).
- Zero em-dash / en-dash: **PASS** (0/0).
- Anti-contaminare: **PASS** (`_AUTOMATIZARE`/`AUTOMATIZEZ`/`_SISTEM`/`trainity_c18`/`trainity_c17`/`Construcția 01`/`Structurare`/`18-Automatizare`/`01-Structurare` = 0; "motor" = 2 callback-uri C18 legitime).
- Fallback imagini: **PASS** (0 base64 JPEG; placeholder DRAFT).
- Editor video fara leftover C17/C18: **PASS** (0 tokens straine; tokens C19 corecte: localStorage, export `HTML-Video-Excel-19-Guvernare-Editat`, editorExport).

## VALIDARI NERULATE / PROBLEME
- `gate_v20.py 19`: **NU_RULAT** (necesita toate 7 artefactele; lipsesc FILM + assets finale). La finalul Slice 4.
- `audit_sync.py` pe C19 complet: **NU_RULAT** (la final).
- imgclone (hash != c01): **N/A** - imaginile sunt placeholder DRAFT, nu finale; nu declar PASS.
- Fix aplicat: GRESEALA nu era verbatim in span-ul locked (avea prefix + "confunzi" mic); reparata in build script + regenerat. Restul = zero abateri.

## STATUS RELEASE
**NU release complet.** Slice 3 din generare. Lipsesc FILM + imagini finale. `DRAFT`.

## RISCURI RAMASE
1. Imagini DRAFT placeholder -> release blocat pana la cele 7 imagini GUVERNARE (ARHITECT).
2. STATUS=OPRIT in demonstratie = intentionat (explicat in pagina).
3. Branch de sesiune divergent; commit pe main aliniat.

## CERERI CATRE BRAIN / SYSTEM
- **Catre ARHITECT:** cele 7 imagini GUVERNARE (hero + 6 exec-stage).
- La urmatorul `sync`: Slice 4 (FILM + assets), apoi gate_v20 + audit_sync finale.
- **CERERE SYSTEM:** niciuna.

## COMMIT
Commit pe `main`: `feat(c19): Slice 3 - HTML-Video + HTML-Editor-Video Guvernare (placeholdere DRAFT, fix GRESEALA verbatim)`. SHA in git log.

**C19_GENERARE_SLICE_3_HTML_VIDEO**
