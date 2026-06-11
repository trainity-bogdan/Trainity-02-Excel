# CLAUDE -> BRAIN C15

## 1. STATUS
**C15_IMAGE_PROMPTS_PREPARED** · pachet de prompturi/brief-uri pentru imaginile C15 (1 hero-poster + 6 exec-stage), pe axa SINTEZĂ. NU am generat imagini, NU am integrat, NU am atins `c15/**` / artefactele text / SYSTEM / C14 / C16. SPEC 11-slot LOCKED neatins. Singura scriere: acest raport. Prompturile vizuale sunt în engleză (convenția generatorului); meta-câmpurile în română, pentru ARHITECT.

## 2. CONTEXT GENERARE TEXT
C15 SINTETIZARE = generat la nivel text (6 artefacte canonice): `gate_v20 15 c15 c01` = PASS, `audit_sync` = C15 OK cu `V39.assets = XX`. Singurul rest pentru release-ul R-V01.2 complet = pachetul de imagini (hero + 6 exec-stage jpg în `c15/assets/`). Acest pas pregătește prompturile; generarea + integrarea rămân la ARHITECT (apoi le procesez: watermark scos + base64 inline).

## 3. PRINCIPIU VIZUAL C15
Fiecare imagine spune povestea SINTEZEI, nu a altei trepte:
- pagina e DEJA compusă (focar, ierarhie) — corectă, dar **mută**;
- problema: pagina **arată**, nu **spune**;
- cursantul **extrage și formulează** mesajul esențial;
- rezultatul = **o singură frază** care contează (headline galben);
- pagina devine **dovada** mesajului.

Limbaj vizual recurent (ancoră de coerență): o **pagină de raport business curată** (substrat, gri/alb) + o **bară de headline** care trece din goală (mută) în **o singură propoziție galbenă** (mesajul). Galbenul = mereu mesajul/fraza, niciodată decorul.

## 4. HERO-POSTER PROMPT

**Titlu intern:** `hero-poster-excel-15-sintetizarea`
**Scop vizual:** coperta construcției — „o pagină devine o singură frază care contează" (MIZĂ HERO: MESAJUL ESENȚIAL).
**Prompt (EN):** "Premium cinematic business still. A clean, well-composed report page (charts and a ranking, neatly arranged with clear hierarchy) lies on a dark navy desk, dimmed and secondary. Above it, floating and in sharp focus, a single bold yellow headline sentence on a clean bar, as if distilled from the page. Thin connecting line from the page up to the sentence, signalling the page proves the sentence. Editorial, minimal, high-end consulting aesthetic. Palette strictly white, near-black/navy, one accent yellow. Soft directional light, shallow depth of field. No people."
**Elemente obligatorii:** pagină de raport compusă (substrat, estompată) · o singură frază-headline galbenă, dominantă · relația frază-deasupra / pagină-dedesubt (dovadă).
**Elemente interzise:** simboluri de calcul (=, Σ, calculator), săgeți cauză-efect, blocuri rearanjate/mutate, butoane de decizie/acțiune, listă-rezumat lungă, dashboard generic fără headline, personaje, sci-fi, iconuri random.
**Text vizibil recomandat:** o singură frază scurtă în română pe bara galbenă (ex. „O categorie duce rezultatul.") — sau placeholder neutru dacă ARHITECT preferă fără text; titlu opțional mic „C15 · SINTEZĂ".
**Format recomandat:** 3:2 cinematic (ex. 1200×800), jpg.
**Notă de coerență C15:** o pagină (arată) -> o frază (spune). Fără calcul, fără decizie.

## 5. CELE 6 EXEC-STAGE PROMPTS

### exec-stage-1 · E1 INPUT — Pagina mută
**Scop vizual:** pagina compusă, corectă, dar fără mesaj (bară de headline goală).
**Prompt (EN):** "Premium business still: a complete, correctly composed report page (clear focal chart, hierarchy, reading order) on a navy surface, but the title/headline bar at the top is conspicuously empty, a blank highlighted strip where a sentence should be. The page looks finished yet says nothing. A faint question mark hovers, conveying 'so what?'. Minimal, editorial, white/near-black/one yellow accent (only on the empty bar outline). No people, no clutter."
**Elemente obligatorii:** pagină compusă corectă · bară de headline GOALĂ (mută) · senzație de „arată, nu spune".
**Elemente interzise:** mesaj deja scris, calcul, rearanjare, decizie.
**Text vizibil recomandat:** bară goală + mic „?" / „și ce-i cu asta?" discret.
**Format:** 16:9 (1600×900), jpg.
**Notă C15:** starea de intrare — pagina mută primită de la compunere.

### exec-stage-2 · E2 AI — Rezumatul automat
**Scop vizual:** AI scurtează pagina (rezumat proporțional) vs. mesajul care încă lipsește.
**Prompt (EN):** "Premium business still: the same report page beside an AI-generated summary panel, a long proportional list of equal-weight bullet points (a faithful but flat shrink of everything). A subtle AI/Copilot glyph marks the panel as machine-made. Side by side, the contrast reads: a shortened-everything list, not yet one message. White/near-black, one yellow accent reserved for a still-empty headline slot. Clean, editorial, no people."
**Elemente obligatorii:** panou rezumat = listă proporțională, multe puncte egale · marcaj AI discret · headline-ul încă negol/neformulat.
**Elemente interzise:** o singură frază-mesaj (aceea vine la E3), calcul de cifre noi, cauze.
**Text vizibil recomandat:** etichetă „REZUMAT (AI)" pe panou; opțional „rezumat ≠ sinteză".
**Format:** 16:9, jpg.
**Notă C15:** partea automatizabilă (rezumat draft); încă nu e mesajul.

### exec-stage-3 · E3 SINTEZĂ — Mesajul esențial
**Scop vizual:** momentul formulării — o singură frază galbenă cristalizează din pagină.
**Prompt (EN):** "Premium cinematic still: the decisive moment, a single bold yellow sentence crystallizes on the headline bar above the report page, while the page itself recedes into supporting proof. A human hand (no full figure) places/underlines the one sentence. Sense of distillation: many elements below, one statement above. White/near-black, dominant single yellow line. Editorial, high-end, focused light on the sentence."
**Elemente obligatorii:** o SINGURĂ frază galbenă, dominantă · pagina ca dovadă, secundară · gestul de formulare (mână, fără personaj).
**Elemente interzise:** mai multe mesaje, listă, calcul, săgeți cauzale, rearanjarea paginii.
**Text vizibil recomandat:** o frază scurtă RO pe headline (ex. „O categorie duce rezultatul.").
**Format:** 16:9, jpg.
**Notă C15:** inima construcției — formularea mesajului (nu descoperirea).

### exec-stage-4 · E4 CONTROL — Testul „și ce-i cu asta?"
**Scop vizual:** mesajul trecut prin filtrul so-what; indicativ, nimic nou peste pagină.
**Prompt (EN):** "Premium business still: the single yellow headline sentence under a clean test/filter overlay, a checkmark beside it and a rejected, greyed-out 'noise' sentence struck through below. A small label conveys the filter 'without this, would the decision change?'. The kept sentence is indicative (a statement), not an instruction. White/near-black, yellow only on the validated sentence and the check. Minimal, editorial, no people."
**Elemente obligatorii:** mesaj validat (bifă) · o frază-zgomot respinsă (tăiată) · filtrul so-what.
**Elemente interzise:** limbaj de decizie/acțiune („de făcut", buton), cifră/cauză nouă, calcul.
**Text vizibil recomandat:** „fără asta, decidentul hotărăște la fel?" + bifă pe mesaj.
**Format:** 16:9, jpg.
**Notă C15:** indicativ, nu decizional; formulat, nu descoperit.

### exec-stage-5 · E5 REFORMULARE — Mesajul se adaptează la schimbare
**Scop vizual:** datele s-au schimbat în amonte; headline-ul se rescrie (verbal), cifrele rămân.
**Prompt (EN):** "Premium business still: the report page shows subtly updated data (a small change in the chart), while the headline sentence is being rewritten, an old yellow sentence lightly struck through, a fresh yellow sentence written above it. The figures live in the page/model and are untouched; only the words change. Sense of re-phrasing, not re-calculating. White/near-black, two yellow sentence states (old faded, new sharp). Editorial, no people."
**Elemente obligatorii:** headline vechi (estompat) + headline nou (clar) · date actualizate în pagină · cifrele neatinse (rămân ale modelului).
**Elemente interzise:** simboluri de recalcul/calculator, formule, rearanjarea layout-ului, decizie.
**Text vizibil recomandat:** frază veche tăiată + frază nouă; opțional „reformulez, nu recalculez".
**Format:** 16:9, jpg.
**Notă C15:** reformulare = act verbal; recalculul e în amonte (T3), nu în C15.

### exec-stage-6 · E6 PAYOFF — O pagină a devenit un mesaj
**Scop vizual:** starea finală — headline sus, pagina-dovadă dedesubt, predată spre livrare.
**Prompt (EN):** "Premium cinematic still: the finished report, a single confident yellow headline sentence at the top, the well-composed page below as its proof, the two clearly belonging together. The report is being handed forward (a subtle motion/arrow toward the right edge, toward the next step), calm and resolved. High-end consulting aesthetic, white/near-black, one yellow accent on the headline. No people, no decision buttons."
**Elemente obligatorii:** headline + pagină-dovadă, împreună · sentiment de finalizare · predare înainte (spre livrare), subtilă.
**Elemente interzise:** încadrare de decizie / „de hotărât" / pachet de decizie (aceea e C16), calcul, rearanjare.
**Text vizibil recomandat:** headline-ul final RO; opțional mic „către livrare".
**Format:** 16:9, jpg.
**Notă C15:** o pagină a devenit un mesaj care contează; predarea spre C16 e doar handoff, nu decizie.

## 6. ELEMENTE INTERZISE GLOBAL (pe toate cele 7)
- calcul (calculator, formule, =, Σ), analiză cauzală (săgeți cauză-efect, „de ce");
- rearanjare/mutare de blocuri ca subiect (aceea e C14);
- decizie / livrare (butoane, „de hotărât", pachet de decizie — aceea e C16);
- rezumat generic prezentat ca rezultat final (rezumatul e doar contrast la E2);
- dashboard generic FĂRĂ headline/mesaj;
- kitsch, science-fiction, personaje exagerate, iconografie random;
- orice abatere de la paleta alb / negru-navy / un singur galben-accent.

## 7. CE RĂMÂNE PENDING DUPĂ ACEST PAS
- ARHITECT generează cele 7 imagini (extern) pe baza acestui pachet;
- eu le procesez: scot watermark-ul (steluța Gemini, R-V49.1), salvez `c15/assets/hero-poster-excel-15-sintetizarea.jpg` + `c15/assets/exec-stage-1..6.jpg` (hash ≠ C01), integrez base64 inline (resize) în HTML-Video + HTML-Editor-Video;
- după integrare: `R-V59.imgclone` / `V39.assets` trece de la XX la OK → `audit_sync` ZERO DRIFT → release R-V01.2 complet C15 (cele 7 artefacte împreună), ca la C07/C08.

## 8. CE NU AM MODIFICAT
- NU am generat imagini, NU am integrat, NU am atins `c15/**` (artefacte + build scripts) sau `c15/assets/`.
- NU am modificat artefactele text, Excel, FILM, SYSTEM, C14, C16, alt `_brain/cYY`.
- NU am redeschis SPEC C15. Singura scriere: acest raport.

## 9. COMMIT
Commit descriptiv pe main asociat acestui raport (`docs(c15): pachet prompturi imagini C15 - hero + 6 exec-stage`), push pe origin/main. Hash raportat în chat.

Pachetul de prompturi C15 e gata pentru ARHITECT. La sosirea imaginilor, le procesez și le integrez, apoi închidem release-ul complet.
