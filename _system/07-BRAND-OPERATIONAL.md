# Brand operațional Trainity

Cum se exprimă brand-ul Trainity în fișierele sistemului. Vocabular, tone of voice, colors, segmentare.

---

## Ecosistemul Trainity

```
Bogdan Târlă (persoană/trainer)
    ├── IT Learning (training center, fondată 2007, #1 RO Microsoft Office)
    ├── Dr.Excel (e-learning brand, 1.200+ video lessons, 14.500+ studenți)
    └── Trainity (implementation/consultancy, fondată 2026)
            ├── Pack 02 Excel (B2C) ← acest sistem
            └── Sistem Trainity Excel (B2B, 5-day guided implementation)
```

**Pack 02 Excel** = produs B2C — 20 construcții educaționale, livrabile self-paced.

**Sistem Trainity Excel** = produs B2B — implementare ghidată pentru echipe corporative.

---

## Vocabular obligatoriu vs interzis

### Vocabular obligatoriu (Trainity §4)

Termenii canonici care **trebuie** folosiți peste tot în sistem:

| Termen | Folosință |
|---|---|
| **sistem** | "Sistemul Trainity Excel", "sistemul de construcții" |
| **construim** | "Construim fluxul", "construim cunoașterea" |
| **augmentat cu AI** | "Excel augmentat cu AI Copilot" |
| **echipă** | "Echipa de implementare", "echipa B2B" |
| **rutină** | "Rutina de refresh", "rutina lunară" |
| **mod de lucru** | "Modul de lucru cu Excel + AI" |

### Vocabular INTERZIS

Termenii care **NU pot apărea** în HTML, FILM, Creativ, prompturi:

| Termen | De ce interzis |
|---|---|
| **curs** | Trainity nu vinde cursuri (educație clasică). Vinde sistem. |
| **cursant** | Idem. Folosim "operator", "utilizator", "ARHITECT". |
| **lecție** | Idem. Folosim "construcție", "etapă", "scenă". |
| **modul** | Sună a educație tradițională. Folosim "construcție". |
| **tutorial** | Sună a YouTube how-to. Folosim "demonstrație". |
| **masterclass** | Termen overused. Trainity nu e curs. |
| **webinar** | Trainity nu face evenimente live broadcast. |
| **productivitate** | Termen prea generic. Trainity vinde sistem demonstrabil. |
| **AI hype terms** | "AI revoluționar", "AI transformă tot", "AI-first" etc. |
| **fost MVP** | Microsoft MVP e canonic "Microsoft MVP Excel pentru România, singurul". Nicio referință temporală. |
| **pivot / restructurare / migrație** | Trainity NU e pivot al carierei lui Bogdan — e ADIȚIE la ecosistem (Dr.Excel + IT Learning + Trainity coexistă) |
| **nu mai vând training** | Bogdan încă livrează training corporativ. Doar nu mai e centrul activității. |

**Verificare empirică:** Gate v20 R-V02.11 verifică cu context awareness (de exemplu "lecție" e ok într-o citare a tradiției pedagogice — *"în tradiția lecțiilor lui Newton"* — dar nu ca termen Trainity).

---

## Tone of voice

### În HTML-Studiu (cockpit cursant)

- **Voce**: directă, conducătoare ("Deschide fișierul", "Apasă butonul")
- **Persoana**: imperativ + "tu"
- **Ritmul**: scurt, comandă-confirmare
- **Exemple**:
  > "Caută anomaliile invizibile la prima privire."
  > "Fixează suma martor pe valoare_neta."
  > "Verifică că predarea cap-coadă conservă suma."

### În HTML-Video (cinematic broadcast)

- **Voce**: narrativă plural ("deschidem", "marcăm", "verificăm")
- **Persoana**: noi (trainer + cursant împreună)
- **Ritmul**: cinematic, fraze scurte, pauze controlate
- **Stare emoțională**: recunoaștere acută, control calm
- **Exemple**:
  > "Arată ca tabel. Anteturi, totaluri, AutoFilter. Pare gata. Verific dacă este."
  > "Cer demonstrația. Promptul e instrument de audit, nu de execuție."
  > "Nu reconstruiesc. Fac controlabil."

**Diferență canonică (R-V03.4):** Studiu = cockpit operativ → tu execuți. Video = broadcast narativ → noi observăm împreună.

### În Creativ.txt

- **Voce**: rețetă creativă pentru Bogdan
- **Conține**: HOOK, MIZA, MANTRA, WOW, MOTTO, schemă scenă, ritm cinematic
- **Funcție**: ghid pentru recordare voice-over

### În FILM.docx

- **Voce**: script video procedural
- **Structura**: 6 etape × 8 secțiuni canonice fiecare
- **Pentru**: OBS Studio recording cu fundal HTML-Video

---

## Brand colors (inviolabile)

Sistemul vizual T-02 → T-10 (frozen 14 aprilie 2026):

### Paletă canonică

| Element | Hex | Rol |
|---|---|---|
| **Yellow** | `#FFD400` | Brand primary — NICIODATĂ `#F2C94C` (greșit istoric) |
| **Black** | `#000` | Brand secondary, fundal HTML-Video |
| **Soft-black** | `#0A0A0A` | Container colors |
| **Pale-yellow** | `#FFFAE0` | Editorial pills background |
| **Border editorial pills** | `#FFE680` | |
| **Text grey** | `#444` | Body text |
| **Muted** | `#888–#AAAAAA` | Subtle elements |
| **Dividers black** | `#2A2A2A` | Pe fundal negru |
| **Dividers white** | `#EEE` | Pe fundal alb |
| **Red anomaly** | `#C00000` | Probleme, erori (anomaly-grid) |
| **Orange stage** | `#E8A800` | Pași intermediari (în step-action) |

### Componente vizuale signature

- **Stat-board negru `#0A0A0A`** cu `border-radius: 16px` + `box-shadow: 3px 3px 0 0 #FFD400` — semnătura Trainity
- **Yellow bar 6px** între secțiuni (în landing-uri)
- **CTA principal**: yellow `#FFD400` + border 2px black + box-shadow 5px 5px 0 0 black + black dot 7px + CAPS + weight 800
- **Card MIZA (`.cover-miza`)** în modelul premium HTML-Studiu (V52): card alb cu `border-radius:10px`, `border:1px solid #ececec`, accent galben `border-left:4px solid var(--tr-y,#FFD400)`, shadow dublu `0 6px 24px rgba(10,10,10,.10), 0 1px 3px rgba(10,10,10,.06)`, `padding:20px 24px`. Ridică MIZA de pe pagină ca element-cheie. Aplicat C01-C04 (Studiu + Editor-Studiu); de propagat la C05-C08 odată cu modelul premium.

---

## Tipografia canonică

```
H1: 70px, weight 800, letter-spacing -2.4px, line-height 0.98
H2: 50-60px, weight 800
Subhook: 26px, weight 600
Body: 17px, weight 400, max-width 540px, line-height 1.6
Editorial labels: 11px, weight 700, letter-spacing 1.8px, UPPERCASE, color yellow
Micro-text: 12-13px, color #666, italic
```

**Font stack:** `-apple-system, "SF Pro Display", Inter, Arial fallback`

**Sentence case** în text normal. **CAPS** doar pe CTA principal și pe monumental boxes.

---

## Segmentare B2C vs B2B

### Pack 02 Excel (B2C) — acesta este sistemul

**Cui se adresează:** profesioniști individuali care lucrează cu Excel zilnic (analiști, contabili, manageri proiect, antreprenori). Echipe sub 6 persoane sau persoane fizice.

**Format livrabil:** 20 construcții self-paced. Cursant intră, parcurge construcție cu construcție, în orice ordine (deși ordine recomandată e 01-20).

**Preț:** 495 lei (1 construcție test) — pricing strategy via LearnWorlds.

**Landing page:** B2C Work 10X Pack Landing (frozen 15 aprilie 2026), 6 slides W-01 → W-06, paletă violet-night `#1A1033` + yellow `#FFD400`.

### Sistem Trainity Excel (B2B) — produs separat

**Cui se adresează:** companii cu echipe 6+ persoane care fac raportare bazată pe Excel (CFO, COO, HR Director).

**Format livrabil:** 5-day guided implementation (implementare ghidată pe 5 zile).

**Preț B2B:**
- Echipe 6-7: 3.120 EUR fix minimum
- Echipe 8-9: grilă progresivă 0% discount
- Echipe 10-12: 10% discount
- Echipe 13-15: 15% discount
- Echipe 16+: 20% discount

**Landing page:** B2B Excel Landing (frozen 14 aprilie 2026), 13 secțiuni T-01 → T-10 + 3 kill slides.

**CTA standard inviolabil:** "PRIMEȘTE GRATUIT SISTEMUL PE EMAIL"

---

## Relația dintre Pack 02 Excel și landing pages

Pack 02 Excel = **produsul livrat după landing converted**.

Flux:
1. Vizitator pe landing B2B sau B2C
2. Convert prin CTA
3. Primește acces la cursanți / la echipa B2B
4. Acces în Pack 02 Excel (cele 20 construcții)
5. Parcurge construcțiile

**Implicații pentru documentație sistem:**
- Construcțiile NU repetă mesajele landing (nu sunt fix sales material)
- Construcțiile asumă că cursantul a înțeles propunerea (decide pe baza landing-ului)
- Construcțiile sunt **livrare educațională**, NU re-sell

---

## Microsoft MVP — comunicare canonică

**Formula canonică (inviolabilă):**
> "Microsoft MVP Excel pentru România, singurul"

**De ce această formulare:**
- Subliniază unicitatea (singurul în România)
- Fără durată ("din 2018", "10 ani consecutiv")
- Fără timpuri verbale negative ("fost MVP")
- Fără anul nominalizării

**De ce NU referință temporală:**
Microsoft MVP se reînnoiește anual. Comunicarea cu durată creează vulnerabilitate la întrebări gen "ești încă MVP?". Formula canonică evită complet acest subiect.

**Aplicabilitate:**
- Landing pages
- Bio Bogdan
- HTML-Studiu cover-meta (la C20 sau introducere pack)
- HTML-Video opening sequence
- Materiale marketing

---

## Aplicare în HTML-Studiu

### Cover-header (3 rânduri canonice)

```html
<div class="cover-meta">
  <div><span class="cover-meta-key">TREAPTA:</span> <span class="cover-meta-val">TREAPTA 1 · STRUCTURA</span></div>
  <div><span class="cover-meta-key">CONSTRUCȚIE:</span> <span class="cover-meta-val">01 · STRUCTURA TABELELOR</span></div>
  <div><span class="cover-meta-key">AI INTEGRAT:</span> <span class="cover-meta-val">COPILOT</span></div>
</div>
```

**NU adăuga** rânduri INPUT, OUTPUT, NIVEL, DURATĂ — schema veche, abandonată (R-V03.60).

### Step-action (max 18 per construcție)

Format: verb la imperativ + obiect specific construcției.

✓ Bun:
- "Deschide fișierul predat de construcția precedentă"
- "Caută anomaliile invizibile la prima privire"
- "Fixează suma martor pe valoare_neta"

✗ Rău (generic, clonare):
- "Deschide fișierul"
- "Lucrează cu datele"
- "Continuă mai departe"

### Prompt-label (specific construcției)

✓ Bun:
- "PROMPT 1 · INSTRUMENT DE AUDIT STRUCTURAL"
- "PROMPT 2 · INSTRUMENT DE TRANSFORMARE CONTROLATĂ"

✗ Rău (generic):
- "PROMPT 1"
- "PROMPT 2"

**Lecția L144 — toleranță zero pe clone**: prompt-label și prompt-text NU pot fi identice cu cele din C01 pilot.

---

## Aplicare în HTML-Video

### Voce trainer plural

Toate verbele la persoana 1 plural în sesiunile narrative:

✓ "Deschidem fișierul, recunoaștem aparența, fixăm martorul"
✗ "Deschide fișierul, recunoaște aparența, fixează martorul" (e voce Studiu)

### Imagini cinematic

6 fișiere `exec-stage-1.jpg` până la `exec-stage-6.jpg` per construcție, în `cNN/assets/` (3:2 cinematic, V41 eliminat PNG duplicate).

**Important (V39):** imaginile sunt **diferite per construcție** — fiecare cNN/ are propriul `assets/` cu pozele specifice axei sale. NU mai există `_system/referinte/assets_canonice/` partajat (eliminat la V39). Pentru o poză nouă brand care merge peste toate construcțiile, se aplică patch pe fiecare `cNN/assets/` separat.

Format: 3:2 cinematic, generate cu Banana 2 conform asset perpetuu prompturi (R-V03.38).

**Stilistic:** Ken Burns slow pan effect în HTML-Video.

**Inline base64** în HTML — niciodată referință externă (R-V03.33).

---

## Sumar reguli brand operațional

| Aspect | Sursa de adevăr |
|---|---|
| Vocabular obligatoriu | Trainity §4 → acest document secțiune "Vocabular" |
| Vocabular interzis | R-V02.11 → acest document secțiune "Vocabular" |
| Voce Studiu vs Video | R-V03.4 → acest document secțiune "Tone of voice" |
| Cover-meta canonic | R-V03.60 → acest document secțiune "Aplicare HTML-Studiu" |
| MVP formula | Acest document secțiune "Microsoft MVP" |
| Brand colors | Acest document secțiune "Brand colors" |
| Step-action specific | R-V03.41 + L144 → acest document secțiune "Step-action" |
| Voce plural Video | R-V03.4 → acest document secțiune "Voce trainer" |

Toate aceste reguli sunt verificate empiric de **Gate v20** (`_system/generatoare/gate_v20.py`).
