# BRAIN → CLAUDE

## STATUS
PENDING

## MANDAT-ID
BRAIN-018-REV1

## MANDAT
C09 RELAȚII, audit complet pentru `HTML-Editor-Studiu-Excel-09-Relatii.html` înainte de orice Video, Editor-Video, FILM sau imagini.

## CONTEXT
Am citit raportul `CLAUDE-TO-BRAIN.md` pentru BRAIN-017-REV1.

Ai generat:
`c09/HTML-Editor-Studiu-Excel-09-Relatii.html`

Raportul spune:
- companion sincronizat 1:1 cu baza stabilizată.
- gate 09 PASS.
- audit_sync C01-C08 OK.
- index.html neatins.
- zero Video / Editor-Video / FILM / assets.
- baza HTML-Studiu neatinsă.

BRAIN acceptă direcția, dar NU trecem la Video până nu audităm companionul Editor-Studiu.

## OBSERVAȚIE BRAIN DUPĂ VIZUALIZARE SCREENSHOT
BRAIN a verificat vizual partea de sus din C09 și a semnalat o problemă de UX / consistență vizuală:

Hero-ul actual nu seamănă sub nicio formă cu hero-ul din Studiu de la celelalte construcții.
Partea de sus pare o imagine / poster, dar de fapt este un placeholder CSS introdus după eliminarea clonei C08.
BRAIN nu a dat încă un prompt Banana / Gemini pentru generarea creativului real de hero HTML-Studiu C09.

Prin urmare:
- Nu trata placeholderul actual ca soluție finală.
- Tratează-l ca placeholder temporar anti-clonă.
- În audit, verifică explicit dacă placeholderul rupe consistența vizuală față de celelalte construcții.
- Dacă rupe standardul de hero Studiu, raportează MAJOR UX, nu PASS curat.
- Nu genera imagine nouă în acest mandat.
- Nu modifica hero-ul în acest mandat.
- Recomandă ce trebuie făcut: prompt Banana / Gemini pentru hero C09 sau hero CSS standardizat care respectă layout-ul celorlalte construcții.

## OBIECTIV
Auditează complet:
`c09/HTML-Editor-Studiu-Excel-09-Relatii.html`

Scop:
- confirmă că este companion real, nu doar copie cu toolbar.
- confirmă că este sincronizat cu `HTML-Studiu-Excel-09-Relatii.html`.
- confirmă că zonele LOCKED sunt reale și protejate.
- confirmă că zonele editabile sunt utile și nu permit ruperea arhitecturii C09.
- confirmă că exportul scoate stratul editor și livrează HTML curat.
- confirmă că nu introduce contaminări C10/C11/C12/T4/T5.
- confirmă că nu reintroduce hero C08 / base64 / clonă vizuală.
- confirmă dacă hero-ul placeholder actual este acceptabil doar temporar sau produce datorie UX majoră.

## DOCUMENTE DE CITIT OBLIGATORIU
Citește:
- CLAUDE.md.
- STARE-CURENTA.md.
- BRAIN-TO-CLAUDE.md.
- CLAUDE-TO-BRAIN.md, raport BRAIN-017-REV1.
- c09/HTML-Studiu-Excel-09-Relatii.html.
- c09/HTML-Editor-Studiu-Excel-09-Relatii.html.
- c09/Date_MASTER-C09.xlsx.
- c09/Creativ-Excel-09-Relatii.txt.
- _system/04-ARHITECTURA-LIVRABILE.md.
- _system/12-ARHITECTURA-CONCEPTUALA-T3.md.
- _system/blueprints/BLUEPRINT-C09-RELATII.md.
- _system/generatoare/gate_v20.py.
- _system/generatoare/tier_guard_t3.py.
- _system/generatoare/audit_sync.py.

## AUDITURI CERUTE
Fă raport separat pentru fiecare zonă.

### A. Sincronizare cu baza
Compară Editor-Studiu cu HTML-Studiu după eliminarea stratului editor:
- panou editor.
- CSS edit-style.
- JS edit-script.
- toolbar editor.
- atribute contenteditable.
- clase locked-slot.
- atribute data-editor-ready.

Trebuie să rezulte HTML curat aproape identic cu baza. Raportează diferențele reale, nu whitespace.

### B. Zone LOCKED
Verifică dacă sunt marcate și ne-editabile:
- Hero-title: "Cum transform legăturile în răspunsuri?".
- AHA: "Fără relații ai date. Cu relații ai răspunsuri.".
- Mantra: "Nu mutăm datele. Le legăm.".
- Formula model: "Fișierul are mai multe foi. Modelul are un fact și patru dimensiuni.".
- Formula Join vs Union: "Join leagă tabele diferite. Union adună tabele de același fel.".
- BOMBĂ / GREȘEALA / CINE DEVII / WOW / MOTTO.

Atenție: verifică și problema de capitalizare. Dacă fraza din LOCKED_PHRASES nu prinde varianta reală din text, raportează MAJOR.

### C. Zone editabile
Verifică dacă sunt editabile doar zonele potrivite:
- microcopy de pași.
- explicații learner.
- exemple fără cifre finale.
- prompturi AI, păstrând scopul de verificare.
- payoff non-locked.

Dacă editorul permite editarea unor zone care ar trebui LOCKED, raportează MAJOR.
Dacă blochează prea mult și devine inutil, raportează MINOR / MAJOR după caz.

### D. Export curat
Verifică logica `editorExport()`:
- elimină toolbar.
- elimină style editor.
- elimină script editor.
- elimină panoul companion.
- elimină contenteditable.
- elimină spellcheck.
- elimină data-editor-ready.
- elimină locked-slot.
- descarcă HTML curat.

Raportează dacă exportul păstrează accidental urme de editor.

### E. Reset
Verifică dacă `editorReset()` curăță doar progresul Trainity și reload, fără efecte periculoase.

### F. Gate conceptual C09
Verifică dacă panoul editor sau textul editabil nu introduce predare despre:
- măsuri.
- filter context.
- KPI.
- rank.
- top / bottom.
- cauze / interpretare.
- dashboard.
- acțiuni automate.

Aparițiile ca negații în panou sunt acceptabile doar dacă nu devin predare sau funcționalitate.

### G. Model DATE
Verifică dacă Editor-Studiu păstrează:
- un fact: Vanzari.
- patru dimensiuni: PRODUSE, CLIENTI, Regiuni, Calendar.
- formula fișier vs model.
- zero formulări incorecte de tip "patru tabele" în sensul greșit.

### H. Hero / anti-clonă C08 / UX vizual
Verifică:
- zero base64 C08.
- placeholder RELAȚII prezent.
- nu există imagine externă.
- nu există asset nou.
- nu există contaminare vizuală C08.
- dacă placeholderul actual rupe consistența cu hero-ul din Studiu de la celelalte construcții.
- dacă lipsa unui prompt Banana / Gemini pentru hero C09 blochează livrarea finală vizuală.

### I. UX editor
Verifică dacă panoul sus este util, clar și nu ocupă excesiv experiența.
Verifică dacă toolbarul jos nu rupe experiența pe mobil.
Verifică dacă locked badges sunt vizibile, dar nu distrug layout-ul.
Verifică separat UX-ul hero placeholder, pentru că BRAIN l-a semnalat vizual ca fiind în afara standardului celorlalte construcții.

### J. Tehnic HTML / JS
Verifică:
- tag-uri închise.
- script fără erori evidente.
- CSS editor izolat.
- nu există id duplicat problematic.
- nu există evenimente care se bat cu scriptul de progres.
- contenteditable nu strică butoanele de navigație.
- localStorage rămâne C09.

### K. Validare prin gate-uri
Rulează validările cerute mai jos și interpretează rezultatele, nu doar le listezi.

## FIȘIERE PERMISE
Ai voie să modifici doar:
- `CLAUDE-TO-BRAIN.md`.
- `STARE-CURENTA.md`, doar dacă fluxul standard cere actualizare.

Nu modifica Editor-Studiu în acest mandat.
Nu modifica HTML-Studiu în acest mandat.
Nu crea Video.
Nu crea Editor-Video.
Nu crea FILM.
Nu crea imagini.
Nu modifica index.html.

Dacă găsești bug critic, raportează-l, nu-l repara în acest mandat.

## VALIDĂRI CERUTE
Rulează:
1. `gate_v20 09 c09 c01`.
2. `tier_guard_t3` pentru C09.
3. `audit_sync`.
4. comparație Editor curățat vs HTML-Studiu.
5. verificare 18 pași, 8 verificări, 5 fenomene, 2 prompturi.
6. verificare zone LOCKED.
7. verificare zone editabile.
8. verificare export curat, prin analiză cod.
9. verificare că nu există base64 C08.
10. verificare că nu ai modificat fișiere interzise.
11. verificare hero placeholder vs standard hero Studiu C05-C08, raportată ca UX.

## RAPORT CERUT ÎN CLAUDE-TO-BRAIN.md
Scrie raport complet:
1. Status.
2. Rezumat executiv.
3. Fișiere citite.
4. Validări rulate.
5. Audit sincronizare cu baza.
6. Audit zone LOCKED.
7. Audit zone editabile.
8. Audit export curat.
9. Audit reset.
10. Audit granițe C09/C10/C11/C12/T4/T5.
11. Audit model DATE.
12. Audit hero / anti-clonă C08 / UX vizual.
13. Audit UX editor.
14. Audit tehnic HTML / JS.
15. Probleme găsite, cu severitate: BLOCKER / MAJOR / MINOR / WARN.
16. Fixuri recomandate, dar NU aplicate.
17. Decizie: PASS / PASS CU FIXURI / REPARAȚIE MAJORĂ.
18. Ce NU ai modificat.
19. Ce rămâne pentru pasul următor.
20. Commit / status Git.

## MANDAT CURENT
Execută BRAIN-018-REV1.
Audit complet Editor-Studiu C09.
Nu modifica fișierul auditat.
Nu trece la Video încă.
