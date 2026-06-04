# SYSTEM WRITE HANDOFF · Protocol ChatGPT BRAIN -> Claude Code EXECUTOR

## Decizie operațională

ChatGPT nu mai este executor Git pentru fișiere SYSTEM comune. ChatGPT formulează mandatul, Claude Code execută local în repo.

## De ce

Claude Code lucrează pe clone complet al repo-ului, vede fișierele integral, poate edita chirurgical, poate rula scripturi, poate verifica `git diff` și poate rezolva conflicte local.

ChatGPT prin GitHub connector poate scrie fișiere, dar pentru fișiere mari existente riscul de overwrite distructiv este prea mare dacă sursa este trunchiată.

## Roluri

### ChatGPT BRAIN al construcției

- primește cererea SYSTEM de la chatul construcției,
- analizează dacă modificarea este permisă,
- formulează mandatul pentru Claude Code,
- poate crea scripturi de patch mici, idempotente și verificabile,
- nu execută overwrite pe fișiere SYSTEM mari,
- nu face commit direct pe registrul mare.

### Claude Code EXECUTOR al construcției

- rulează local în repo,
- aplică patch-ul sau scriptul primit,
- rezolvă conflicte mecanice,
- rulează verificări,
- face commit/push doar după diff verificat,
- raportează exact ce a modificat.

### Bogdan / Arhitect

- se asigură că nu rulează simultan două sesiuni Claude Code care scriu în fișiere SYSTEM comune,
- decide conflictele conceptuale,
- secvențializează modificările SYSTEM.

## Regula hard pentru toate chat-urile

Dacă o construcție cere modificarea unui fișier comun SYSTEM, executorul se oprește și cere mandat.

Fișiere SYSTEM comune:

- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `index.html`
- `COMENZI.yaml`
- `gate_v20.py`
- `audit_sync.py`
- `_system/**`
- `_brain/system/**`

## Flux obligatoriu

1. Claude Code construcție întâlnește nevoia de scriere SYSTEM.
2. Claude Code se oprește și formulează `CERERE SYSTEM`.
3. Bogdan aduce cererea în ChatGPT BRAIN al construcției.
4. ChatGPT BRAIN produce `PROMPT PENTRU CLAUDE CODE EXECUTOR`.
5. Bogdan dă promptul în Claude Code.
6. Claude Code execută local, cu `git status`, patch, verificări, `git diff`, commit, push.
7. Claude Code raportează rezultatul.
8. ChatGPT BRAIN poate audita raportul.

## Reguli conflict

Claude Code poate rezolva conflicte mecanice:

- două blocuri aditive diferite,
- două înregistrări pentru construcții diferite,
- actualizări independente în secțiuni diferite.

Claude Code NU decide singur conflicte conceptuale:

- două reguli incompatibile,
- schimbări diferite pe aceeași arhitectură,
- redenumiri de sistem cu impact transversal,
- modificări de gate cu efect pe mai multe construcții.

În conflict conceptual, Claude Code se oprește și cere decizie BRAIN / Arhitect.

## Interdicții

- Nu se face `git push --force`.
- Nu se face `git reset --hard` fără mandat explicit.
- Nu se rezolvă conflict prin `accept current` sau `accept incoming` orb.
- Nu se șterg blocuri ale altor construcții pentru a trece conflictul.
- Nu se execută overwrite complet pe fișiere SYSTEM mari prin connector.

## Verificări minime Claude Code

Înainte:

```bash
git status
git pull
```

După patch:

```bash
git status
git diff --stat
git diff --check
```

Pentru registrul mare:

```bash
wc -l _system/arhiva/SISTEM_TRAINITY-versiuni.md
grep -n "PARTEA VI - SPEC INGHETAT CONSTRUCTII" _system/arhiva/SISTEM_TRAINITY-versiuni.md
grep -n "## SPEC C" _system/arhiva/SISTEM_TRAINITY-versiuni.md
```

## Format raport Claude Code

Raportul trebuie să conțină:

- fișiere modificate,
- output verificări,
- diff stat,
- conflicte rezolvate, dacă există,
- ce s-a păstrat,
- ce s-a eliminat,
- commit SHA,
- confirmare dacă construcția poate continua.
