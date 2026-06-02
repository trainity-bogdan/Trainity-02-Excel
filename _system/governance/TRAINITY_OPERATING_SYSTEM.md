# TRAINITY_OPERATING_SYSTEM.md · Modul oficial de lucru (T2-T5)

> Sistemul de operare pentru dezvoltarea treptelor Trainity. Generalizat din T2.

---

## 1. PRINCIPIUL CENTRAL
**Nu lucrăm document-centric. Lucrăm rule-centric.** Regulile treptei se definesc o dată
(Bible = sursă unică), orice modificare se verifică contra lor și se propagă transversal.
Driftul T2 a apărut pentru că lucrul a fost document-centric (fix-uri secvențiale
nepropagate). Acest OS îl face imposibil.

## 2. DOI ACTORI (nu roluri inventate)
| Actor | Decide | Poate |
|---|---|---|
| **ARHITECT** (Bogdan) | CE | aprobă reguli sacre / identitate / decizii structurale; îngheață AHA/nume; oprește motorul |
| **MOTOR** (AI) | CUM | execută cu impact analysis + propagare transversală; auditează (rol advers la cerere); rulează gate-uri |

> Motorul poartă „pălării" (implementator / auditor / QA) după sarcină — NU sunt roluri
> separate. Copy-ul de impact (payoff/WOW/motto) se atinge doar în runde dedicate.

## 3. WORKFLOW STANDARD (o treaptă)
CONCEPT → *(TIER SEED dacă e prima construcție a treptei)* → IMPLEMENTATION → DRIFT
DETECTOR → RELEASE GATE → CHANGELOG → AUDIT FINAL.
DNA EXTRACTION + POSITION MATRIX = **după minimum 2 construcții** ale treptei (R-SEED-2),
retroactiv. Apoi treci în EXISTING TIER.

## 4. TIER SEED — pornirea unei trepte noi
**Trigger:** construcția N e prima dintr-o treaptă nouă (ex. C09 = prima T3).
1. **MOȘTENEȘTE §SHARED** din Bible (schelet 6/18/5/8/2, handoff, AI, disciplină
   terminologică). Nu-l atingi.
2. **DEFINEȘTE identitatea** treptei: axă · întrebare-mamă · ce produce / ce NU produce.
3. **DEFINEȘTE garda** (permis = competența proprie; interzis = treapta următoare) →
   o scrii ca secțiune §TIER nouă în Bible (ex. §T3). Aprobare ARHITECT (regulă).
4. **CONSTRUIEȘTE** prima construcție pe §SHARED + garda nouă.
5. **NU rula:** DNA extraction · Position Matrix · cross-construction (Gate G5-cross). N/A.
6. **DUPĂ a 2-a construcție:** extragi DNA-ul treptei + creezi Position Matrix → EXISTING TIER.

**Output TIER SEED:** o secțiune §TIER în Bible + prima construcție. **ZERO documente noi.**
Reguli care guvernează SEED: R-SEED-1/2/3, R-TIER-PARAM (Bible §SHARED).

## 5. CELE DOUĂ MODURI (Detector + Gate)
- **EXISTING TIER** (≥2 construcții): rulează tot, inclusiv cross-construction.
- **TIER SEED** (prima): doar §SHARED + garda nouă; cross-construction N/A.
- Parametru `tier` obligatoriu: lista de interziși = a treptei curente (R-TIER-PARAM).

## 6. REGULI DE COLABORARE CU AI (motorul)
- **CREEAZĂ** doar: construcție din blueprint aprobat, documente de guvernanță, poze (prompt aprobat).
- **MODIFICĂ** doar: cu impact analysis + propagare transversală; copy de impact doar în runde dedicate.
- **DOAR AUDITEAZĂ** când: arhitectul cere audit (nu implementare).
- **CERE DECIZIE** când: regulă sacră / identitate locked / decizie structurală / conflict de autoritate.
- **VERIFICĂ TRANSVERSAL** la ORICE modificare de poziție structurală — obligatoriu.

## 7. REGULI PENTRU CONSTRUCȚII NOI
Niciun HTML fără blueprint · niciun blueprint fără Bible · nicio modificare fără impact
analysis · nicio construcție fără verdict de Detector · nicio treaptă (≥2 constr.) fără
Position Matrix. COPY+MODIFY pornește din `c01`.

## 8. PROTOCOL TREPTE VIITOARE (T3+)
- Pornire = **TIER SEED** (§4). T3 = ANALIZĂ (interpretează ce a cunoscut T2).
- Scheletul se moștenește (S4); identitatea DIFERĂ (R-SEED-3).
- Evită contaminarea inversă: T3 nu reia T2; T2 nu face T3 (garda §TIER).
- Semnăturile retorice (mantra „Nu X. Y", motto „Un X. Apoi orice Y") = limbaj Trainity,
  păstrate; conținutul se schimbă pe treaptă.

## 9. CHECKLIST FINAL PENTRU ARHITECT
**Cere:** blueprint înainte de HTML; (în EXISTING TIER) Position Matrix; verdict Detector;
audit advers; propagare transversală dovedită.
**Verifică:** identitate distinctă (test 10s); AHA locked; garda treptei; handoff; uniformitate.
**Nu accepta:** fix local nepropagat; copy de impact ad-hoc; termeni de treaptă superioară
fără teaser; „AUDIT" în nume etapă; construcție fără hero dedicat; cosmetizarea unui reziduu structural.
**Oprește motorul când:** modifică regulă sacră fără aprobare; optimizează local în loc de
transversal; rescrie în loc de uniformizează; inventează reguli nesusținute de construcțiile existente.
