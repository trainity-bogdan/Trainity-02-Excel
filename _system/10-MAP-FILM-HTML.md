# 10 · MAPARE FILM → HTML (frazele de impact)

**Scop:** sursă de adevăr pentru ce text din FILM (.docx) se sincronizează în cele 4 machete HTML. La comanda „update html / sincronizează FILM", motorul aplică maparea de mai jos mecanic, în toate cele 4 fișiere relevante.

**Principiu:** FILM = MASTER. HTML urmează FILM. Dacă HTML are o formulare mai bună decât FILM, se BACK-PORTEAZĂ în FILM întâi (FILM rămâne master), apoi se sincronizează.

---

## Cele 4 machete

| Machetă | Conține sloturi de impact |
|---|---|
| HTML-Studiu | cover-subtitle, cover-miza, mantra-band-main, payoff-motto |
| HTML-Editor-Studiu | (idem Studiu) |
| HTML-Video | hero-hook, final-motto, exec-closing-motto, exec-emotion×6, exec-phrase×6 |
| HTML-Editor-Video | (idem Video) |

---

## Maparea câmp FILM → slot HTML

Rolul slotului e dat de eticheta proprie din HTML (`mantra-band-sub` = „MANTRA · TRAINITY", `exec-closing-prelabel` = „Motto:").

| Câmp FILM (IDENTITATE) | HTML-Studiu | HTML-Video | Observații |
|---|---|---|---|
| **INTRIGA (HOOK)** | `cover-subtitle` (text integral) | `hero-hook` (split pe cele 2 propoziții: prop.1 + `<span class="hero-hook-twist">`prop.2`</span>`) | — |
| **MIZA** | `cover-miza` | — | doar Studiu |
| **MANTRA · TRAINITY** | `mantra-band-main` (cuvânt-cheie în `<mark>`) | — | doar Studiu |
| **WOW (PAYOFF FINAL)** | linie-climax `[data-wow="1"]` (`.payoff-line.accent`) chiar înainte de `payoff-motto` | frag `[data-wow="1"]` (`.accent`) chiar înainte de `final-motto` (renumerotează motto + bump `data-frag-total`) | vârful fluxului emoţional, înainte de semnătură |
| **MOTTO (SEMNĂTURĂ)** | `payoff-motto` | `final-motto` (ultimul frag) + `exec-closing-motto` (ultima parte în `<span class="exec-closing-motto-yellow">`) | apare 3 locuri |
| **CONTRACT (DESTINAȚIE)** *(element nou)* | bloc `<section class="exec-hero" data-contract="1">` în cusătura SCENA REALĂ → primul pas | (Studiu only; în Video rolul e jucat de `hero-sub`) | promisiune privită înainte; copy DRAFT, de formalizat în FILM după ce ARHITECT fixează wording-ul |

| Câmp FILM (SLIDES EXECUTIVE) | HTML-Video | 
|---|---|
| **STARE (exec-emotion)** ×6 | `exec-emotion` din slide-urile 1-6 (1:1 pe etapă) |
| **FRAZĂ DE IMPACT (exec-phrase)** ×6 | `exec-phrase` din slide-urile 1-6 (1:1 pe etapă) |

> NB: câmpul `hook:` din array-ul JS de etape NU e frază de impact — e hook-ul de scenă al etapei. NU se sincronizează din SLIDES EXECUTIVE.

---

## WOW (rezolvat — opţiunea B)

WOW are acum slot dedicat: linie-climax verbatim chiar înainte de motto, ca vârf al fluxului emoţional. Vizual: highlight **verde** (`.payoff-wow`, `#18843e`) cu etichetă `WOW:` (`.wow-tag`). Structură: `<span class="wow-tag">WOW:</span><span data-wow="1">FRAZĂ</span>` — sync-ul atinge DOAR `[data-wow]` (fraza), eticheta + culoarea rămân. În Video e frag propriu (renumerotează motto-ul + creşte `data-frag-total` cu 1).

## CONTRACT (element nou — copy DRAFT)

Cusătura SCENA REALĂ → primul pas primeşte un „contract de destinaţie": o promisiune privită înainte de călătorie (timp prezent-viitor). Bloc `exec-hero` ancorat `[data-contract="1"]`, Studiu only. Copy-ul curent e DRAFT, scris de motor; se formalizează ca element SPEC în FILM după ce ARHITECT fixează wording-ul, apoi se masterizează ca restul.

---

## Procedură „update html" (mecanic)

1. Citește valorile de identitate + SLIDES EXECUTIVE din FILM (.docx).
2. Pentru fiecare câmp, suprascrie slotul HTML corespunzător în toate cele 4 machete (Studiu + Editor-Studiu pentru sloturile Studiu; Video + Editor-Video pentru sloturile Video).
3. Split-uri: INTRIGA → hero-hook pe 2 propoziţii; MOTTO → final-motto / exec-closing-motto (ultima parte highlight).
4. Rulează `audit_sync.py` (ZERO DRIFT) + verifică vizual sloturile.
5. Commit + push.

---

## Status sincronizare per construcţie

| Cod | INTRIGA | MIZA | MANTRA | MOTTO | exec slides | WOW | CONTRACT |
|---|---|---|---|---|---|---|---|
| C01 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ slot nou | ✓ draft |
| C02 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ slot nou | ✓ draft |
| C03 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ slot nou | ✓ draft |
| C04 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ slot nou | ✓ draft |

C01: rezolvat prin sync HTML←FILM (repo). A reparat şi confuzia de rol (mantra-band ţinea textul MOTTO). Liniile HTML vechi înlocuite: cover-miza „O decizie corectă…", payoff-motto „Mai întâi structura. Apoi orice." → dacă ARHITECT le vrea înapoi, se pun în FILM şi se re-sincronizează.

C03/C04: FILM-ul din repo = docx-ul reparat (voce „noi", fără conflict V45), sincronizat complet.

C05-C08: încă NEsincronizate (FILM↔HTML drift vechi posibil); de procesat la primirea FILM-urilor rafinate sau la cerere.

### ARC TRANSFORMARE · BOMBĂ (model premium V47+) — sync V56

Modelul premium a adăugat în HTML-Studiu stratul pedagogic „arcul TU" (`tu-section`): **BOMBA** (`cover-subtitle`, idee dominantă) · **SUNĂ CUNOSCUT** (`tu-recunoastere` = lead + bullets) · **GREȘEALA CLASICĂ** (`tu-greseala`) · **AHA** (`tu-aha`) · **CINE DEVII** (`tu-promise`). Acesta se back-portează în FILM ca secțiune `ARC TRANSFORMARE · CINE DEVINE CURSANTUL` (după IDENTITATE, înainte de SLIDES EXECUTIVE). FILM rămâne master.

**Atenție la mapare:** la construcțiile premium `cover-subtitle` ține **BOMBA**, NU INTRIGA. INTRIGA (hook de scenă) rămâne element FILM separat și alimentează `hero-hook` din Video.

**V56:** back-portat arcul complet din Studiu în FILM la **C02 + C03** (lipsea integral) și completat fraza a 2-a din MIZA C04 („Orice raport construit deasupra pornește de pe o bază care se reface singură."). C04 avea deja arcul; C01 îl are în format Biblia v2.0. **C01-C04 acum sincrone FILM↔Studiu** pe INTRIGA/BOMBĂ · MIZA · MANTRA · WOW · MOTTO · ARC. Singura diferență rămasă, intenționată: C03 MIZA în FILM e la persoana „noi" („Demonstrăm/dovedim"), Studiu la „C03 demonstrează/dovedește" — aceeași informație, voce diferită.

---

## SPEC v2.0 — FILM = „Biblia construcției" (4 secțiuni)

Decizie ARHITECT: FILM-ul nu mai e doar script video, ci **sursa unică** pentru video + narație + Shorts + Study + PPT + LP. Structurat în 4 secțiuni distincte (ordine: înțeleg → aplic → devin):

| # | Secțiune | Elemente | Rutare (consumator) |
|---|---|---|---|
| 1 | **IDENTITATE CINEMATICĂ** | Intriga · Miza · Mantra · Wow · Motto | Video (rendat) + Study |
| 2 | **ARSENAL NARATIV** | Simptom în business · Greșeala clasică · Aha moment · Fraza de trailer | Narația lui Bogdan + Shorts + trailer + LP. **NU** slide-uri video noi (Video rămâne curat). În Study: callout-uri (`.arsenal-band` = AHA + greșeală + simptom). |
| 3 | **BRIEF PEDAGOGIC** | Întrebarea · Micro-brief · De ce contează · Înainte · După · Ce vei obține | Study (hero + corp). |
| 4 | **TRANSFORMAREA CURSANTULUI** | Competența dobândită · De acum înainte | Study (închidere `.transformare-section`) + LP + Shorts. |

Apoi: SLIDES EXECUTIVE (→ exec slides Video) + cele 6 etape (script video).

### Sloturi HTML-Studiu noi (v2.0)
- `.arsenal-band` (`.aha-callout` + `.arsenal-card.greseala` + `.arsenal-card.simptom`) — după hero.
- **COMPETENȚA** → hero (`.hero-competency`, label „CE VEI PUTEA FACE"): obiectiv ÎNAINTE de pași (advance organizer).
- **DE ACUM ÎNAINTE** → `.transformare-section` (`.ts-identity`): închidere **gated** (apare la final, când toți pașii sunt bifați, ca payoff-ul). Split pe timp: abilitate=obiectiv sus, identitate=răsplată jos.
- Hero (deja): question, micro-brief, before→after, outcomes (vezi sus).

### Gărzi
- **FRAZA DE TRAILER = linia-campioană PROMOVATĂ** (poate FI aha/motto/wow/mantra — cea mai virală pentru Shorts/copertă/LP), NU obligatoriu o frază nouă → evită ecoul + taie cost copy.
- **Registru de voci** per construcție: toate frazele scurte (intriga/greșeala/aha/mantra/wow/motto/trailer) verificate una lângă alta, anti-ecou.
- **R-V02.15** pe Simptom: calitativ generic, ZERO cifre business.
- **3 unghiuri de „de ce" distincte:** Miza (dorință, cinematic) ≠ Simptom (durere business) ≠ De ce contează (consecință pedagogică).

### Status propagare v2.0
| Cod | FILM v2.0 (4 secțiuni) | Study arsenal+transformare |
|---|---|---|
| C01 | ✓ prototip | ✓ prototip |
| C02-C08 | — (de propagat după validare C01) | — |

---

## C01 — model experiență VALIDAT (V47)

Layout HTML-Studiu (de propagat în C02-C08), cu **două voci simțite, fără etichete**:

**HERO COCKPIT** (poster+cockpit): imagine-obiect (schelă) cu cuvântul-obiect uriaș overlay (`.hov-object`) + `hero-question` (întrebarea) + bandă cockpit (`.system-map` simplificată pe cele 4 din treaptă, fără buton).

**Apoi, în ordine:**
1. `study-intro-top`: titlu (`cover-title`) + micro-brief (`hero-microbrief`) + miză (`cover-miza`) — context.
2. **BOMBA** `intriga-bomb` (`cover-subtitle` gigantic, „Nu este unul." pe highlight galben) — memoria de 24h. **INTRIGA s-a mutat din Hero aici.**
3. **VOCEA TA** (secțiuni `.tu-section`, fundal închis, persoana a II-a): `tu-recunoastere` (simptom) → `tu-greseala` → `tu-aha` (VÂRF, cel mai mare) → `tu-promise` (CINE DEVII).
4. **VOCEA DATELOR** (deschis/tehnic): `hero-beforeafter` (ÎNAINTE❌→DUPĂ✅) + DE CE + mantra + scena + `hero-outcomes` + pașii.
5. **RĂSPLATA** (gated, `.transformare-section`, voce TU): COMPETENȚA „DUPĂ C01 POȚI" + DE ACUM ÎNAINTE (ecou la CINE DEVII).

**Bookend identitate:** CINE DEVII (promisiune, vizibilă, după AHA) + DE ACUM ÎNAINTE (confirmare, gated la final) — împart prima frază.

**Rutare element nou:** INTRIGA → `intriga-bomb` (Studiu, gigantic) + hero-hook (Video). CINE DEVII → `tu-promise` (Studiu). Restul, ca în tabelul de sus.

**Metodă:** orice modificare vizuală se verifică randată headless (chromium, 393px mobil + 1280px desktop) ÎNAINTE de livrare.

**Status:** C01 = model validat. C02-C08 = de propagat (necesită copy per beat + imagine-obiect per construcție).
