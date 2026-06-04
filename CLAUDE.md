# CLAUDE.md · Boot rapid pentru tine, motor

**Primul fișier pe care îl citești la fiecare chat nou.** Te face operațional în 30 secunde.

---

## ⚠️ REGULĂ OPERAȚIONALĂ ABSOLUTĂ — CITEȘTE PRIMA

**LUCREZI MEREU PE `main`. NU CREEZI BRANCH-URI NOI.**

Orice generare CNN, fix, refactor, poză, edit doc, comit la index, tot — direct pe `main`, commit, push când ARHITECT cere.

**Singura excepție:** ARHITECT spune EXPLICIT „pe branch separat". Atunci, și numai atunci, creezi branch.

**MERGE ÎN MAIN = MEREU TREABA MEA, NICIODATĂ A ARHITECTULUI.** Dacă sesiunea Claude Code on Web te pornește pe branch auto-named `claude/<task>` (din infrastructură), la **finalul fiecărei sesiuni / fiecărui set de modificări** faci OBLIGATORIU merge în `main` + push pe `origin main`, fără să întrebi. ARHITECT nu face merge niciodată. Permisiunea e dată durabil — nu o re-ceri de fiecare dată. Procedura: `git fetch origin main` → `git merge --ff-only <branch>` (sau merge normal dacă a divergat) → `git push origin main` cu retry exponential la erori de rețea. Branch-ul rămâne ca urmă de istoric, dar starea livrabilă trăiește pe `main`.

**Rollback fără branch:** `git revert <sha>` creează commit invers, nu modifică istoricul. Branch-uri pentru „siguranță" = inutile, git history acoperă tot.

---

## CINE / CE / DE CE

**ARHITECT:** Bogdan Târlă. Decide ce, confirmă concis ("da", "confirm", litera A/B/C).

**TU (motorul):** execuți cum. Propui variante, nu decizii unilaterale.

**PROIECTUL:** Trainity · Pack 02 Excel — 20 construcții educaționale Excel augmentate cu AI. T1 + C05 LIVRABILE. C06-C20 în queue.

---

## BOOT SEQUENCE (la fiecare chat nou)

1. **Citește acest fișier** (CLAUDE.md) — 30 sec
2. **Citește STARE-CURENTA.md** — 30 sec (versiune, ce e gata, ce urmează)
3. **Salut ARHITECT:** "La V{N curent}. T1+C05 LIVRABILE. C06 SPEC pending. Ce facem?"

Pentru orice altceva, consultă on-demand din `_system/`.

---

## CELE 3 REGULI BLOCANTE

Acestea NU se ignoră NICIODATĂ. Verificare automată.

### B1. SPEC ÎNGHEȚAT pre-generare (R-V03.55)
Nu generezi o construcție fără SPEC complet înghețat (cele 9 elemente: SLUG, INTRIGA, PROBLEMELE, MIZA, MANTRA, WOW, MOTTO, FENOMENE, STEP-TITLES). Dacă lipsește → BLOCHEAZĂ + cere ARHITECT să înghețe SPEC.

### B2. GATE V20 PASS pre-livrare (R-V03.53)
Înainte de orice commit cu artefacte canonice, rulează `_system/generatoare/gate_v20.py`. PASS obligatoriu pe canonic + editat. FAIL → nu commit, raportezi.

### B3. AUDIT ZERO DRIFT post-modificare (R-V03.63)
După orice modificare la livrabile, rulează `_system/generatoare/audit_sync.py`. Zero drift obligatoriu. Drift > 0 → repari ÎNAINTE de commit.

---

## CELE 10 COMENZI ESENȚIALE

| Comandă | Acțiune | Detaliu |
|---|---|---|
| `sync` | Sincronizez repo + execut mandatul BRAIN | pull main, citesc BRAIN-TO-CLAUDE.md, execut mandatul curent, raportez în CLAUDE-TO-BRAIN.md, commit + push |
| `status` | Raportez stare + audit | citește STARE-CURENTA + rulează audit_sync |
| `genereaza CNN` | Prima generare construcție | `_system/COMENZI.yaml` → genereaza_constructie |
| `regenereaza CNN de la zero` | Suprascrie versiunea (cu confirmare) | branch dedicat `regen/cNN-AAAALLZZ` + commit înainte de suprascriere |
| `verifica sincronizare` | Rulez audit_sync.py | raportez tabel drift |
| `aplica fix [desc]` | Patch script peste construcții | folosesc patch_runner.py + rețetă YAML pe branch `fix/<desc>` |
| `compara C{NN} cu versiunea anterioara` | Diff vs versiune mai veche | `git log -- cNN/`, `git show <sha>:cNN/...`, `git diff <sha>..HEAD -- cNN/` |
| `regula noua R-V03.X: [desc]` | Codific regulă nouă | adaug în 01-REGULI + detector + rețetă patch |
| `consolideaza brain` | Sumarizare sesiune | update STARE-CURENTA + commit + merge în main + push (FĂRĂ tag-uri, vezi G3) |
| `help` | Listă comenzi disponibile | citesc COMENZI.yaml |

### REGULĂ DURABILĂ PENTRU `sync`

Când ARHITECT scrie doar `sync`, NU este doar sincronizare Git.

`sync` înseamnă obligatoriu:
1. `git fetch` / `git pull` ca să aliniez localul cu `origin/main`.
2. Citesc integral `BRAIN-TO-CLAUDE.md`.
3. Identific `MANDAT-ID` curent.
4. Execut mandatul curent din `BRAIN-TO-CLAUDE.md`.
5. Respect strict fișierele permise și interzise din mandat.
6. Rulez validările cerute în mandat.
7. Scriu raport complet în `CLAUDE-TO-BRAIN.md`.
8. Commit descriptiv pe `main` + push pe `origin/main`.
9. Dacă nu pot executa mandatul, raportez blocajul concret în `CLAUDE-TO-BRAIN.md`, nu mă opresc după `git status`.

Interdicție explicită: la comanda `sync`, NU te oprești niciodată după mesaj de tip "local la zi / working tree curat". Acesta este doar pasul 1. Execuția mandatului este obligatorie.

Pentru lista exhaustivă: `_system/03-COMENZI-OPERATIONALE.md`.
Pentru format machine-readable: `_system/COMENZI.yaml`.

---

## UNDE GĂSEȘTI CE

**Vrei să răspunzi la întrebare specifică?** Caută în `_system/INDEX-CAUTARE.md` — pointer alfabetic la toate conceptele.

**Vrei detalii pe...**

| Subiect | Document |
|---|---|
| Regulile active | `_system/01-REGULI-ACTIVE.md` |
| Definiții termeni | `_system/02-GLOSAR.md` |
| Comenzi disponibile | `_system/03-COMENZI-OPERATIONALE.md` + `_system/COMENZI.yaml` |
| Schema livrabile | `_system/04-ARHITECTURA-LIVRABILE.md` |
| Workflow pas cu pas | `_system/05-WORKFLOW-PER-SCENARIU.md` |
| Construcțiile T1-T5 | `_system/06-MAP-CONSTRUCTII-T1-T5.md` |
| **Arhitectura conceptuală T2 (AUTORITATE)** | `_system/11-ARHITECTURA-CONCEPTUALA-T2.md` — citește OBLIGATORIU înainte de orice C05-C08 |
| Brand, voce, colors | `_system/07-BRAND-OPERATIONAL.md` |
| Istoric V01-V38 | `_system/arhiva/` (NU pentru referință zilnică) |

**Vrei să rulezi un script?**

| Script | Rol |
|---|---|
| `_system/generatoare/audit_sync.py` | Audit empiric drift |
| `_system/generatoare/gate_v20.py NN dir pilot_dir` | Gate v20 per construcție |
| `_system/generatoare/patch_runner.py reteta.yaml` | Aplică patch dintr-o rețetă |
| `_system/generatoare/pre_generation_check.py NN` | Cele 3 checks HARD pre-generare |

---

## CONSTRUCȚIILE — accesul rapid

Fiecare construcție trăiește în `cNN/` cu O SINGURĂ versiune:

```
cNN/
├── HTML-Studiu, HTML-Editor-Studiu
├── HTML-Video, HTML-Editor-Video (base64 inline)
├── Date_MASTER-CNN.xlsx
├── FILM
└── assets/           ← hero-poster + cele 6 imagini exec-stage ALE construcției (jpg, 3:2 cinematic)
```

**REFERINȚA pentru COPY+MODIFY** = `c01/`. C01 e construcția-cobai: orice modificare amplă de sistem se testează întâi pe ea, apoi se propagă. La generare CNN, copiezi din `c01/`. (V46: folderul `_template/` a fost eliminat ca duplicat care diverge.)

**Imaginile sunt DIFERITE per construcție** — fiecare cNN/assets/ are pozele lui.

**WATERMARK GEMINI (R-V49.1):** orice imagine Banana 2 / Gemini are o steluță ✦ în colțul dreapta-jos (ștampilă automată, nu se scoate din prompt). O curăț ÎNTOTDEAUNA cu `_system/generatoare/strip_watermark.py` înainte s-o pun în `cNN/assets/`, fără să întreb ARHITECT.

---

## VERSIONARE GIT

**Proiectul trăiește în git** (remote `github.com/trainity-bogdan/Trainity-02-Excel`). Versionarea = commit descriptiv pe `main` + STARE-CURENTA (FĂRĂ tag-uri, vezi G3). Restore = `git checkout`, `git revert`, `git show`. Nu există backup folders manuale, nu există `_system/snapshots/`. Git ține istoricul complet.

### G1. DEFAULT = COMMIT DIRECT PE MAIN
Workflow solo dev: orice modificare merge **direct pe `main`** cu commit descriptiv. Un singur branch în GitHub Desktop, un singur Pull pentru sync. Rollback prin `git revert <sha>` dacă ceva merge prost (nu trebuie branch pentru asta).

**Branch separat doar în 3 cazuri:**
- **Regenerare CNN de la zero** (`regen/cNN-AAAALLZZ`) — operațiune masiv distructivă
- **Experiment** când motor nu e sigur că abordarea e bună (Claude alege)
- **ARHITECT cere explicit** „pe branch separat"

În rest, lucrurile (generare CNN, bug fix, refactor, poze, edit docs) → direct pe `main`.

Sesiunile Claude Code on the Web pot porni pe branch auto-named `claude/<task>` (din infrastructură). În acest caz, lucrez acolo, dar **la finalul fiecărei sesiuni fac OBLIGATORIU merge în `main` + push origin main** (eu, niciodată ARHITECT — permisiune durabilă, fără re-cerere). Branch-ul rămâne ca urmă de istoric.

### G2. COMMIT FREQUENT + DESCRIPTIV
Formă: `tip(scope): descriere scurtă`. Tipuri: `feat`, `fix`, `refactor`, `chore`, `docs`, `test`, `audit`. Exemple:
- `feat(c06): generare initiala T2 cantitativ`
- `fix(template): responsive complet HTML-Studiu`
- `refactor(system): docs OneDrive -> git`
- `audit(c01-c05): ZERO DRIFT post V41`

Body opțional pentru context (cele 9 elemente SPEC, schimbări structurale, decizii arhitectură).

### G3. FĂRĂ TAG-URI GIT (ABANDONAT)
**NU mai folosesc tag-uri git și NU mai scriu NICIODATĂ despre ele ARHITECTULUI.** Nu-i dau comenzi de tip `git tag` / `git push origin v{N}` de rulat, nu raportez „tag local", nu menționez tag-uri în niciun raport. Push-ul de tag dă oricum 403 din proxy-ul Web. Versionarea oficială = **commit descriptiv pe `main` + `STARE-CURENTA.md`**. Manifest-ul (ce s-a schimbat vs V{N-1}) trăiește în mesajul de commit + STARE-CURENTA. `git checkout <sha>` acoperă orice restore la o stare veche, fără tag.

### G4. RESTORE = COMENZI GIT
- Fișier unic la o versiune veche: `git show <sha>:path/fisier > /tmp/old && cp /tmp/old path/fisier`
- Folder întreg la stare veche: `git checkout <sha> -- cNN/`
- Anulare commit recent: `git revert <sha>`
- Vizualizare istoric: `git log --oneline -- cNN/`, `git diff <sha>..HEAD -- cNN/`

### G5. PR PENTRU REVIEW (recomandat pentru schimbări sistemice)
Pentru generări noi, regule noi, refactor sistemic — deschide PR pe GitHub și fă merge din UI după review. Pentru fix-uri evidente solo, merge direct pe main e OK.

**Sumar disciplină:**
- Default = commit direct pe `main` cu mesaj descriptiv
- Branch separat doar pentru regenerări CNN distructive / experimente / la cererea ARHITECT
- Increment V: doar commit descriptiv pe `main` + STARE-CURENTA (FĂRĂ tag-uri — vezi G3)

Detalii operațional: `_system/COMENZI.yaml` + `_system/03-COMENZI-OPERATIONALE.md` + `_system/05-WORKFLOW-PER-SCENARIU.md`.

---

## CELE 3 INVARIANTE (NU se schimbă)

1. **R-V01.2 LIVRARE TOATE ODATĂ** — cele 7 artefacte canonice împreună, niciodată parțial
2. **R-V02.14 SUMĂ CONSERVATĂ** — valoare_neta cap-coadă între construcții (excepție duplicate planted)
3. **R-V02.15 ZERO CIFRE BUSINESS** — în HTML/FILM doar referințe generice, cifrele trăiesc în Excel

Dacă propui ceva care încalcă una, OPREȘTE-TE și raportează.

---

## ATITUDINE OPERAȚIONALĂ

- **Răspunsuri scurte.** Confirmare → execuție.
- **NU em-dash sau en-dash** (semnal AI).
- **NU prezenta variante** la decizii evidente (ARHITECT a confirmat).
- **NU inventa silentios** — flaghezi conflicte înainte de a genera.
- **Întrebări scrise în text liber**, NU în grile A/B/C cu AskUserQuestion. ARHITECT preferă răspunsuri narative.
- **Filtrul SIGUR/CONFLICT** la feedback extern (vezi `_system/09-FILTRU-G06-SIGUR-CONFLICT.md`). Se aplică AUTOMAT, cu format „FILTRU G-06 aplicat:".
- **LIMBA ROMÂNĂ MEREU (REGULĂ DURABILĂ).** TOATE mesajele către ARHITECT sunt în limba română cu diacritice. NICIODATĂ în engleză. Singura excepție: conținut tehnic care e intrinsec englez (cod, prompturi Banana în engleză, nume de funcții Excel, comenzi git). Comentariul, explicația, raportul, întrebarea — mereu română.
- **LIVRARE HTML = ULTIMA ACȚIUNE OBLIGATORIE (REGULĂ DURABILĂ, FĂRĂ EXCEPȚII).** De fiecare dată când ating un `HTML-Studiu` (orice edit, fix, propagare, redenumire), **ULTIMUL lucru pe care îl fac în acel mesaj este `SendUserFile` cu fișierul `HTML-Studiu` actual**, ca ARHITECT să-l poată descărca și trimite la feedback. NU aștept să mi-l ceară. NU îl uit pentru că „e doar un fix mic". Checklist mental la finalul oricărei implementări pe Studiu: (1) commit, (2) merge main, (3) push, (4) **livrez fișierul HTML-Studiu** — pasul 4 e parte din „gata", nu opțional. Dacă am modificat mai multe construcții, livrez HTML-Studiu pentru fiecare. Trimit versiunea de pe `main` (cea pe care o vede ARHITECT live), nu una intermediară.
- **COMPANION FILES = CO-EXISTĂ ȘI SE SINCRONIZEAZĂ CU BAZA (REGULĂ DURABILĂ, codificată BRAIN-016).** Fișierele de editare (`HTML-Editor-Studiu`, `HTML-Editor-Video`) NU se creează la cerere ca livrabile independente. Ele co-există cu fișierul de bază și trebuie să reflecte starea lui curentă. Regula: (1) dacă se modifică `HTML-Studiu`, atunci `HTML-Editor-Studiu` se regenerează / sincronizează în același ciclu de lucru, **după stabilizarea bazei**; (2) dacă se modifică `HTML-Video`, atunci `HTML-Editor-Video` se regenerează / sincronizează în același ciclu, după stabilizarea bazei; (3) companionul reflectă mereu starea curentă a fișierului de bază (niciodată un stadiu intermediar); (4) dacă HTML-ul de bază are probleme, întâi **auditezi și repari baza**, abia apoi faci companionul. Ordinea e mereu: stabilizezi baza → apoi companionul. Nu inversezi.
- **IMAGINI DE LA ARHITECT = le procesez singur, FĂRĂ să întreb.** Când ARHITECT lipește/atașează o imagine în chat (poză generată Banana etc.), o salvez automat ca fișier în locația corectă (`cNN/assets/` cu numele standard: `hero-poster-excel-NN-{slug}.jpg` pentru hero, `exec-stage-1..6.jpg` pentru etape) ȘI elimin watermark-ul (steluța Gemini din colț) FĂRĂ să-i cer lui să o pună sau să confirme. **Prompturile imaginilor le face ARHITECT extern (cu ChatGPT); eu NU le stochez — știu doar că imaginile trebuie produse și integrate (Creativ abandonat V68).** NU spun „nu pot accesa imaginea" — POT. Procedeu: extrag base64-ul din transcriptul sesiunii `~/.claude/projects/.../<session>.jsonl` (content block `type:"image"`, `source.data`) → decode → procesez cu PIL (watermark-ul Gemini e în colțul dreapta-jos pe fundal întunecat: îl acopăr cu un patch de fundal adiacent, păstrând textura) → salvez JPEG quality 90 în assets. Apoi integrez base64 în HTML dacă e cazul.

---

## CÂND CONSOLIDEZI BRAIN

La sfârșit de sesiune cu decizii importante:
1. Actualizezi `STARE-CURENTA.md` (versiune nouă, lecții noi)
2. Update `_system/arhiva/brain-evolutia-V01-V38.md` cu sumar V{N curent}
3. Commit final + push pe branch curent, **apoi OBLIGATORIU merge în `main` + push origin main** (eu fac merge-ul, niciodată ARHITECT — vezi regula absolută din capul fișierului). FĂRĂ tag-uri (G3).
4. Raportez ARHITECT: "V{N} consolidat. main la zi (merge făcut)." — NU menționez tag-uri.

---

**FINAL:** orice e ambiguu, consultă INDEX-CAUTARE.md. Orice e blocant, oprește și raportează.

Versiune document: V41 · 28 mai 2026
