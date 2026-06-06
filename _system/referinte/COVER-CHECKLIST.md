# COVER-CHECKLIST.md — checklist atomic per CONSTRUCTIE NN (V15)

Versiune V15, inghetat in chat BRAIN la 25.05.2026.

> **ACTUALIZARE · FREEZE C01 (iunie 2026) — MODEL DE HERO SCHIMBAT.** Hero principal (`hov-object`) = **numele complet al construcției** (MIZA HERO), NU cuvântul-cheie mare în centru. Modelul vechi cu Hero Word mare e ABANDONAT. CUVÂNTUL trăiește în topbar (`C{NN} · CUVÂNT`), navigare/system-map, indexare si mapările T1-T5. Sursa canonică = `_system/NOMENCLATURA-LOCKED-SCARA.md`, secțiunea „Model de afișare în construcție". Punctele de mai jos (structură cover legacy) se citesc prin acest model; la generare/regenerare NU se reface Hero Word-ul mare în centru.

## Scop

Documentatia explicita a celor ~15 puncte vulnerabile la COPY-MODIFY
pe pilot C01 V12 care TREBUIE modificate la generarea oricarei
constructii C02-C20. Lista decurge din auditul exhaustiv C03 unde s-a
descoperit ca generatorul a ratat 4 violatii in zona cover.

## Cand se foloseste

In chat CHECKIN CONSTRUCTIE NN, la `Genereaza CONSTRUCTIA NN`,
motorul:
1. Citeste IDENTITATE_TEHNICA din SPEC CNN (SISTEM_TRAINITY.md)
2. Aplica toate modificarile atomice de mai jos
3. Ruleaza post-flight gate cross-contamination (R-V03.39)
4. Bifeaza explicit fiecare punct in raport

## HTML-Studiu + HTML-Editor-Studiu (cover-header)

### Punctul 1: cover-label
**Selector:** `<div class="cover-label">`
**Pilot C01:** `PACK 02 EXCEL · TREAPTA 1 · CONSTRUCȚIA C01`
**Inlocuire CNN:** `PACK 02 EXCEL · TREAPTA {treapta_nr} · CONSTRUCȚIA C{NN}`

### Punctul 2: cover-title rand 1
**Selector:** `<h1 class="cover-title">{X}<br>`
**Pilot C01:** `STRUCTURA`
**Inlocuire CNN:** `{nume_hero_caps_rand1}` din IDENTITATE_TEHNICA

### Punctul 3: cover-title rand 2
**Selector:** `<br>{X}</h1>`
**Pilot C01:** `TABELELOR`
**Inlocuire CNN:** `{nume_hero_caps_rand2}`

### Punctul 4: cover-subtitle
**Selector:** `<p class="cover-subtitle">`
**Pilot C01:** `Arată ca tabel. Nu este tabel.`
**Inlocuire CNN:** SPEC.INTRIGA exacta

### Punctul 5: cover-miza
**Selector:** `<div class="cover-miza">`
**Pilot C01:** `O decizie corectă pe date structurate greșit rămâne...`
**Inlocuire CNN:** SPEC.MIZA exacta

### Punctul 6: cover-meta-val TREAPTA (R-V03.43 toate CAPS)
**Selector:** primul `<span class="cover-meta-val">`
**Pilot C01 (dupa fix V15):** `<b>STRUCTURA</b> · CONTROL · AUDIT · NORMALIZARE (SCAN)`
**Inlocuire per treapta curenta:**
- C01: `<b>STRUCTURA</b> · CONTROL · AUDIT · NORMALIZARE (SCAN)`
- C02: `STRUCTURA · <b>CONTROL</b> · AUDIT · NORMALIZARE (SCAN)`
- C03: `STRUCTURA · CONTROL · <b>AUDIT</b> · NORMALIZARE (SCAN)`
- C04: `STRUCTURA · CONTROL · AUDIT · <b>NORMALIZARE</b> (SCAN)`

Pentru T2-T5 lista de treapta se schimba per IDENTITATE_TEHNICA.

### Punctul 7: cover-meta-val CONSTRUCTIE
**Selector:** al doilea `<span class="cover-meta-val">`
**Pilot C01:** `01 din 20 · Pack 02 Excel`
**Inlocuire CNN:** `{NN} din 20 · Pack 02 Excel`

### Punctul 8: cover-meta-val INPUT (filename link)
**Selector:** `<a href="Date-Input-Excel-...">`
**Pilot C01:** `Date-Input-Excel-01-Structura.xlsx`
**Inlocuire CNN:** `Date-Input-Excel-{NN}-{slug}.xlsx`

### Punctul 9: cover-meta-val OUTPUT (filename link)
**Selector:** `<a href="Date-Output-Excel-...">`
**Pilot C01:** `Date-Output-Excel-01-Structura.xlsx`
**Inlocuire CNN:** `Date-Output-Excel-{NN}-{slug}.xlsx`

### Punctul 10: cover-meta-val AI INTEGRAT (description)
**Selector:** ultimul `<span class="cover-meta-val">`
**Pilot C01:** `2 prompturi Copilot · investigație + transformare controlată`
**Inlocuire CNN:** SPEC-specific (descriere precisa per natura
constructiei)

## HTML-Studiu + HTML-Editor-Studiu (next-section, final block)

### Punctul 11: next-label
**Selector:** `<div class="next-label">`
**Pilot C01:** `TREAPTA 1 · CONSTRUCȚIA URMĂTOARE`
**Inlocuire CNN:** ramane TREAPTA actuala daca CNN nu inchide treapta;
schimba la "TREAPTA NEXT" daca CNN=C04 sau C08 sau C12 sau C16

### Punctul 12: next-title
**Selector:** `<h3 class="next-title">`
**Pilot C01:** `C02 · Controlul datelor`
**Inlocuire CNN:** `C{NN+1} · {nume_next_title_case}`

### Punctul 13: next-desc
**Selector:** `<p class="next-desc">`
**Inlocuire CNN:** SPEC.PUNTE_NEXT exacta

## HTML-Studiu + HTML-Editor-Studiu (footer, nav)

### Punctul 14: footer
**Selector:** `<footer class="footer">`
**Pilot C01:** `TRAINITY · C01 STRUCTURA TABELELOR · Cockpit operațional`
**Inlocuire CNN:** `TRAINITY · C{NN} {nume_hero_caps} · Cockpit operațional`

### Punctul 15: nav-brand-label + nav-brand-title
**Selector:** `<div class="nav-brand-label">` + `<div class="nav-brand-title">`
**Pilot C01:** `PACK 02 EXCEL · C01` + `STRUCTURA TABELELOR`
**Inlocuire CNN:** `PACK 02 EXCEL · C{NN}` + `{nume_hero_caps}`

### Punctul 16: mobile-topbar-title
**Selector:** `<div class="mobile-topbar-title">`
**Pilot C01:** `C01 · Structura tabelelor`
**Inlocuire CNN:** `C{NN} · {nume_title_case}`

## HTML-Video + HTML-Editor-Video (analoge)

### Punctul 17: <title>
**Selector:** `<title>`
**Pilot C01:** `C01 · STRUCTURA TABELELOR · BROADCAST`
**Inlocuire CNN:** `C{NN} · {nume_hero_caps} · BROADCAST`

### Punctul 18: topbar-brand
**Selector:** `<div class="topbar-brand">`
**Pilot C01:** `Sistemul 02 - Excel · C01 · Structura tabelelor`
**Inlocuire CNN:** `Sistemul 02 - Excel · C{NN} · {nume_title_case}`

## Toate HTML-urile (storage keys)

### Punctul 19: localStorage STORAGE_KEY in Studiu
**Pilot C01:** `trainity_c01_study_v1`
**Inlocuire CNN:** `trainity_c{NN}_study_v1`

### Punctul 20: localStorage STORAGE_KEY in Video
**Pilot C01:** `trainity_c01_video_v1`
**Inlocuire CNN:** `trainity_c{NN}_video_v1`

## Verificare automata (R-V03.39 post-flight gate)

Dupa generare, motorul ruleaza scan automat:
1. Niciun "C01" / "C02" / ... / "C20" vizibil in text-uri HTML, cu
   exceptia C{NN} curent
2. cover-label contine EXACT "CONSTRUCȚIA C{NN}"
3. nume_hero_caps apare in: cover-title, footer, nav-brand-title
4. nume_title_case apare in: mobile-topbar, topbar-brand,
   next-title (al constructiei anterioare)
5. localStorage keys = trainity_c{NN}_*
6. Niciun "Normalize" in engleza (sau alta engleza din lista neagra)
7. cover-meta-val TREAPTA respecta capitalizarea toate CAPS R-V03.43
8. similarity check cu pilot C01 V12 < 30% pe step-titles (R-V03.41)

Daca **oricare** verificare picătură → present_files BLOCAT.
