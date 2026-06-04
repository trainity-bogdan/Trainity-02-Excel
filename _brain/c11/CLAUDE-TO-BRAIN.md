# CLAUDE → BRAIN · C11 COMPARAȚII / RANK

## STATUS
BLOCAT_PRECONDITII_SISTEM (MANDAT C11-03 nu poate rula fără CERERE SYSTEM)

## RAPORT SYNC (2026-06-04) · MANDAT C11-03 GENERARE

Sync executat în chat dedicat C11. Am preluat mandatul de generare și am rulat
verificările pre-generare permise. Generarea NU a pornit: există 3 precondiții
de sistem neîndeplinite care impun modificări în fișiere sistem interzise mie.

### STATUS GENERARE
NEÎNCEPUTĂ — blocată la pre-flight (B1) + lipsă IDENTITATE_TEHNICA C11.

### LISTA FIȘIERE C11 CREATE / MODIFICATE
- Niciun fișier `c11/` creat (R-V01.2 interzice livrarea parțială; nu pornesc o generare care nu poate trece gate-urile).
- Modificat doar acest raport: `_brain/c11/CLAUDE-TO-BRAIN.md`.

### REZULTAT SCAN VOCABULAR INTERZIS
N/A — nu există încă artefacte C11 de scanat. Regula de adresare directă `tu` +
lista interzisă (`cursant`, `participant`, `elev`, `student`) rămâne pregătită
ca post-pass obligatoriu la generare (matrița `c01/` e T1 veche, va trebui
curățată de persoana a III-a).

### REZULTAT DELIMITĂRI C10 / C12 / T4
Confirmate ca direcție (clasament/contribuție/concentrare = C11; cauza „de ce" =
C12; dashboard = T4; actori agregați, nu rânduri). Nu pot fi validate empiric
fără artefacte.

### REZULTAT VALIDĂRI
- `python3 _system/generatoare/pre_generation_check.py 11` → **BLOCAJ B1**: „SPEC C11 ESTE NEGENERAT". Checker-ul citește registrul `_system/arhiva/SISTEM_TRAINITY-versiuni.md`, unde C11 figurează ca `SPEC C11 - DATA MODEL [Status: NEGENERAT]`.
- `gate_v20.py` și `audit_sync.py` NU au fost rulate (nu există artefacte C11). Ele nu depind de registrul SPEC, vor putea rula după generare.

---

## CAUZA BLOCAJULUI (3 impedimente de sistem)

### 1. SPEC C11 neînghețat în REGISTRUL SISTEM (B1 hard)
SPEC-ul C11 e înghețat în `_brain/c11/BRAIN-TO-CLAUDE.md` (workflow per-construcție),
dar `pre_generation_check.py` citește `_system/arhiva/SISTEM_TRAINITY-versiuni.md`
(linia ~2463), unde apare: `## SPEC C11 - DATA MODEL [Status: NEGENERAT]`.
Cât timp registrul sistem zice NEGENERAT, B1 blochează generarea. R-V01.2 +
regula B1 din CLAUDE.md sunt absolute, nu le pot ocoli.

### 2. CONFLICT DE IDENTITATE: legacy „DATA MODEL" vs BRAIN „COMPARAȚII"
Registrul legacy descrie C11 = **DATA MODEL** (relationships, measures,
dimensions, DAX) — vezi `SISTEM_TRAINITY-versiuni.md:568, 997, 1003, 2463`.
Aceasta e identitatea VECHE. Re-arhitectura T3 (BRAIN-006) a mutat:
C09 = RELAȚII/model, C10 = MĂSURI, **C11 = COMPARAȚII/RANK**, C12 = INTERPRETARE.
„DATA MODEL" e acum teritoriu C09. Dacă nu se reconciliază registrul, pre-check
și gate operează pe identitatea greșită → drift garantat.

### 3. LIPSEȘTE IDENTITATE_TEHNICA pentru C11
`_system/referinte/IDENTITATE-TEHNICA.md` conține acum blocul tehnic pentru
**C10** (hero „MĂSURA POTRIVITĂ", `nume_slug: Masuri`, input `Date_MASTER-C09`,
output `Date_MASTER-C10`), cu doar `next_cod: C11` ca pointer. NU există bloc
IDENTITATE_TEHNICA C11 (nume hero, slug `comparatii`, input/output, titluri,
localStorage keys, prompt-label specific). Procedura de generare (aceeași
referință) spune explicit: „Daca un camp lipseste → motorul OPRESTE generarea
si cere completarea in BRAIN." Plus R-V03.40/L142: prompt-label specific, NU clonă.

---

## DEPENDENȚĂ DE SECVENȚĂ (decizie BRAIN, nu strict SYSTEM)

### C10 nu este construit
Construcțiile livrate fizic: `c01/`-`c09/`. **`c10/` NU există** (chat-ul C10 e
la SPEC). Pipeline-ul de identitate tehnică e single-slot și e setat acum pe C10
(`next_cod: C11`). Două consecințe:
- Lanțul T3 LOCKED este model→măsură→**clasament**→explicație: C11 (clasament) vine DUPĂ C10 (măsură). Generarea C11 înaintea C10 inversează secvența.
- R-V02.14 (sumă conservată cap-coadă) cere input C11 = output C10 (`Date_MASTER-C10.xlsx`), care nu există. Cea mai recentă verigă reală e `Date_MASTER-C09.xlsx`.

**Întrebare BRAIN:** generez C11 cu baseline de date `Date_MASTER-C09` (ultima
verigă reală) și notez lacuna C10, SAU se construiește întâi C10 și abia apoi C11
(recomandat, respectă lanțul LOCKED și pipeline-ul de identitate single-slot)?

---

## CERERE SYSTEM
Construcție: C11
Fișiere comune cerute (NU le-am atins):
1. `_system/arhiva/SISTEM_TRAINITY-versiuni.md`
2. `_system/referinte/IDENTITATE-TEHNICA.md`

Motiv: generarea C11 nu poate porni B1/B2/B3-compliant fără aceste actualizări.

Impact: fără ele, `pre_generation_check.py 11` dă BLOCAJ și generatorul se
oprește la lipsa IDENTITATE_TEHNICA C11.

Propunere (pentru Chat SYSTEM):
1. În `SISTEM_TRAINITY-versiuni.md`: reconciliază identitatea C11 (DATA MODEL →
   COMPARAȚII/RANK, conform BRAIN-006), inserează cele 9 elemente SPEC înghețate
   din `_brain/c11/BRAIN-TO-CLAUDE.md` și treci `[Status: NEGENERAT]` →
   `[Status: INGHETAT]`.
2. În `IDENTITATE-TEHNICA.md`: definește blocul IDENTITATE_TEHNICA C11 (hero
   caps, `nume_slug: comparatii`, title_studiu/video, footer/topbar, localStorage
   `trainity_c11_*`, input/output Date_MASTER, prompt-label specific C11 — nu clonă).
3. Confirmă decizia de secvență C10↔C11 (vezi întrebarea de mai sus).
4. Confirmă că la prima generare imaginile C11 (hero + 6 exec-stage) sunt
   placeholdere `c01/` până le produce ARHITECT extern (Creativ abandonat V68).

Execuția C11 se oprește până la decizia SYSTEM + BRAIN pe punctele de mai sus.

---

## CE E PREGĂTIT DE PARTEA MEA (pot porni imediat ce se deblochează)
- SPEC C11 înghețat și internalizat (9 elemente, 6 fenomene, 8 step narrative).
- Matrița `c01/` analizată: 18 step-titles + 18 step-actions + 2 prompturi +
  8 final-labels + 7 payoff + 6 stage-quotes (Studiu); perechea Video/BROADCAST
  separată. Plan COPY+MODIFY clar.
- Post-pass de vocabular (`tu`, fără termeni școlari) pregătit ca pas obligatoriu.
- Strategie de propagare uniformă a textului în Studiu + Editor-Studiu (string-uri
  comune) și tratare separată a perechii Video.
