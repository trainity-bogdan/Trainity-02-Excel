# BRAIN -> CLAUDE C17

## STATUS
MANDAT_FIX_GATE_CROSS_CONTAMINATION_C17

## CONTEXT
C17 este generat complet, identitatea tehnica C17 a fost adaugata, iar gate_v20 ruleaza.
Status curent verificat in _brain/c17/CLAUDE-TO-BRAIN.md:
C17_GATE_FAIL_CROSS_CONTAMINATION.

Problema raportata:
- gate_v20 pica pe 6 referinte legitime C18 in zone ne-whitelisted.
- Problema nu este conceptuala, ci de formulare tehnica in artefactele C17.
- Fixul cerut este punctual in c17/**.

Referinte raportate de Claude:
1. ba-val: "eticheta candidat C18"
2. stage-tags: "Predare C18"
3. Video JSON title: "Granita spre C18..."

## MANDAT
Aplica fixul punctual pentru gate_v20 cross-contamination.

Ai voie sa lucrezi doar in:
- c17/**

Nu modifica:
- _system/**
- STARE-CURENTA.md
- CLAUDE.md
- README.md
- index.html
- gate_v20.py
- audit_sync.py
- COMENZI.yaml
- c18/**
- c19/**
- c20/**
- nomenclatura LOCKED

Fix obligatoriu:

1. In c17/build_html_studiu_c17.py:
- "candidat C18" -> "candidat de automatizare"
- "Predare C18" -> "Predare T5" sau "Handoff"

2. In c17/build_html_video_c17.py:
- titlul pasului 18 fara "C18"
- recomandat: "Granita spre automatizare"

3. Pastreaza referintele C18 doar in zone whitelisted, unde sunt necesare pentru handoff.

Dupa fix:
- regenereaza cele 4 HTML-uri;
- ruleaza gate_v20 17 c17 c01;
- ruleaza audit_sync;
- verifica zero em-dash;
- verifica nomenclatura LOCKED neatinsa;
- verifica fara drift de continut;
- verifica granite C18/C19/C20;
- verifica ca Date_MASTER si FILM nu au fost modificate decat daca este strict necesar.

## OUTPUT CERUT
CLAUDE -> BRAIN

Include:
- fisiere modificate;
- commit;
- rezultat gate_v20;
- rezultat audit_sync;
- riscuri ramase;
- status final.

Raspunde la final:
C17_GATE_PASS_READY_FOR_RELEASE
sau
C17_GATE_FIX_FAILED
