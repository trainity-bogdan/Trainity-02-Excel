# BRAIN -> CLAUDE C17

## STATUS
MANDAT_SYSTEM_FREEZE_SPEC_C17

## CONTEXT
C17 SPEC 11-slot este confirmat in _brain/c17/CLAUDE-TO-BRAIN.md.
Status verificat: C17_SPEC_CONFIRMED.

C17:
- SISTEMATIZAREA
- CUVANT LOCKED = SISTEM
- VERB LOCKED = SISTEMATIZEZ
- T5 = AUTONOMIE
- iese din OCAZIE
- axa: RELUABILITATEA / forma reluabila
- artefact obligatoriu: _SISTEM
- _SISTEM = harta functionala nativ-Excel, legata de workbook, nu SOP, nu documentatie
- garda OGLINDA: oglindeste, leaga si navigheaza, nu executa, nu judeca, nu deleaga

SPEC 11-slot confirmat:

1. HERO:
"Cum transform munca pe care doar eu o stiu intr-un sistem pe care altcineva il porneste?"

MIZA HERO:
"SISTEMATIZAREA MUNCII RELUABILE"

2. BOMBA:
"Munca ta merge perfect. Pana pleci tu."

3. GRESEALA:
"Nu ai un proces. Ai o memorie personala care tine un Excel in viata."

4. AHA:
"O munca facuta de doua ori nu mai e o livrare. E un sistem ascuns in workbook."

5. MANTRA:
"Nu o fac din nou. O fac sistem."

6. WOW:
"Un proces care traia doar in capul tau. Acum o harta vie in workbook, pe care altcineva o porneste fara tine."

7. MOTTO C17:
"Pleci, si munca o reia altcineva."

Nota:
Template-ul T5 "Pleci, si munca [...]" ramane TEMPLATE CANDIDAT T5, NU LOCKED pentru toata treapta. Se retesteaza la C18-C20.

8. CINE DEVII:
"Nu mai esti omul care tine munca. Esti omul care o face sistem."

9. PAYOFF:
"Acum poti lipsi o saptamana, si munca are cine s-o reia."

10. MIZA:
"Cata vreme munca depinde de o singura persoana, e un risc ascuns: in concediu, la demisie, la suprasolicitare, se opreste. Sistematizarea o face sa continue cu oricine instruit, nu doar cu autorul ei."

11. VERB-SEMNATURA:
a sistematiza / SISTEMATIZEZ

## MANDAT
CERERE SYSTEM · FREEZE SPEC C17

Ai voie sa modifici doar fisiere SYSTEM permise.

Nu modifica:
- c17/**
- HTML-uri
- Date_MASTER
- build scripts
- FILM
- C18/C19/C20
- nomenclatura LOCKED

Obiectiv:
Consemneaza in sistem inghetarea SPEC C17 si marcheaza C17 pregatit pentru etapa urmatoare: SLUG + Blueprint.

Actualizeaza, dupa caz:
- STARE-CURENTA.md
- _system/14-ARHITECTURA-CONCEPTUALA-T5.md
- _system/00-INDEX.md, doar daca indexul trebuie sa reflecte noua stare

Ruleaza:
- audit_sync
- verificare nomenclatura LOCKED neatinsa
- verificare zero em-dash
- verificare ca nu ai atins c17/**
- verificare ca nu ai generat artefacte

## OUTPUT CERUT
SYSTEM REPORT · C17 SPEC FREEZE

Include:
- fisiere modificate
- commit
- verificari rulate
- status final

Raspunde la final:
C17_SPEC_FROZEN_READY_FOR_BLUEPRINT
sau
C17_SPEC_FREEZE_FAILED
