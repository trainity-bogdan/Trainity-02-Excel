# PROTOCOL FILM = OBS DIN HTML-VIDEO (R-V03.19)

## Context

Per R-V03.19 (decizie Bogdan V11), **PPT a fost eliminat** din schema
canonica de livrabile + **FILM nu se mai genereaza** prin script
(gen_film_c01.js sters). FILM-ul este produs **extern**, prin OBS
Studio, ca inregistrare a HTML-Video rulat in browser la 1280x720+.

## De ce

HTML-Video V11+ contine:
- 53 slide-uri scenice (Hero + 6 etape × ~8 slide-uri + Verify + Final)
- Executive Show imbedded la final (slide tranzitie CONCLUZII + 6 slide-uri
  cinematic Ken Burns 9s pe imagini fundal Banana 2 + closing apoteotic)
- Toate transitiile, fragmentele, animatiile, prompturile, copy-buttons
  functionale interactiv

Filmarea OBS captureaza fluxul cinematic real (cu sunet narativ Bogdan
inregistrat separat), produce FILM-Excel-NN-Nume.mp4 ca artefact extern.
NU mai e nevoie de un DOCX paralel cu structura procedurala - HTML-Video
e sursa de adevar narativa.

## Workflow operational (Bogdan)

1. Deschide HTML-Video-Excel-NN-Nume.html in Chrome la 1920×1080 (sau
   monitor extern dedicat). Imaginile sunt base64 inline (R-V03.33),
   incarcare instant fara dependinte externe.

2. Porneste OBS Studio cu sursa "Window Capture" pe browser-ul Chrome
   (fereastra HTML-Video). Configurare recomandata:
   - Output: 1920×1080, 60 fps, MP4 H.264, bitrate 8000 kbps
   - Audio: microfon Bogdan + audio sistem (pentru sunete UI)

3. Foloseste keyboard shortcuts HTML-Video pentru navigare cinematic:
   - `Space` / `→` = avanseaza fragment / slide
   - `←` = retragere
   - `Enter` = Validează (pe ecranele cu actiune)
   - `C` = Copiază prompt (pe ecran Prompt)
   - `R` = Reset progres

4. La Executive Show (ultimele 7 slide-uri), animatiile Ken Burns ruleaza
   9 secunde per slide cu transitie crossfade. Bogdan poate vorbi peste
   sau lasa pauze de respiro.

5. Inchei filmarea pe closing apoteotic (motto + semnatura "Bogdan Tarla
   (Dr.Excel)" pe 2 randuri verticale centrate). OBS produce
   FILM-Excel-NN-Nume.mp4.

## Ce NU se mai face

- NU se mai genereaza FILM-Excel-NN-Nume.docx prin script.
- NU se mai genereaza PPT-Excel-NN-Nume.pptx (R-V03.19).
- gen_film_c01.js + gen_ppt_c01.js au fost ELIMINATE din `generatoare/`
  in V12.

## Livrabilele canonice ramase (schema V12 = 6 livrabile + 1 extern)

LIVRABILE GENERATE AUTOMAT (6):
1. Date-Input-Excel-NN-Nume.xlsx
2. Date-Output-Excel-NN-Nume.xlsx
3. HTML-Studiu-Excel-NN-Nume.html
4. HTML-Editor-Studiu-Excel-NN-Nume.html
5. HTML-Video-Excel-NN-Nume.html (base64 inline)
6. HTML-Editor-Video-Excel-NN-Nume.html (base64 inline)

(Creativ abandonat V68: prompturile imaginilor exec-stage le face ARHITECT
 extern, cu ChatGPT; nu se mai generează/stochează ca fișier.)

LIVRABIL EXTERN (1, produs cu OBS):
- FILM-Excel-NN-Nume.mp4

PDF este TIER 2 DERIVED OPT-IN cu comanda separata `Genereaza PDF din
STUDY` + atasament obligatoriu (R-V03.15).
