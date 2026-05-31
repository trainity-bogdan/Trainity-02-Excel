# TRAINITY_OPERATING_SYSTEM_v1.md · Modul oficial de lucru (T2-T5)

> Sistemul de operare pentru dezvoltarea treptelor Trainity. Generalizează ce a
> funcționat la T2. Aplicabil identic la T3, T4, T5.

---

## 1. PRINCIPIUL CENTRAL

**Nu lucrăm document-centric. Lucrăm rule-centric.**

Nu mai reparăm construcții una câte una. Definim regulile treptei o dată, apoi orice
construcție și orice modificare se verifică contra regulilor și se propagă transversal.
Driftul din T2 a apărut exact pentru că lucrul a fost document-centric (fix-uri
secvențiale nepropagate). Acest OS îl face imposibil.

## 2. ROLURI

| Rol | Responsabilitate | Poate |
|---|---|---|
| **ARHITECT** (Bogdan) | decide CE; aprobă reguli sacre, identitate, decizii structurale | aprobă/respinge, îngheață AHA/nume, oprește implementatorul |
| **IMPLEMENTATOR** (motor) | execută CUM; propagă transversal | modifică doar cu impact analysis + aprobare unde e cerută |
| **AUDITOR** (motor în rol advers) | caută motive de respingere | dă FAIL, ancorat în exemple |
| **QA / GOVERNANCE** (motor) | rulează gate-uri + drift score | blochează release sub prag |
| **EDITOR** | copy de impact (payoff/WOW/motto) | doar în runde dedicate (DEZAMBIGUIZARE), nu ad-hoc |

## 3. WORKFLOW STANDARD (o treaptă, cap-coadă)

1. **CONCEPT** — arhitect definește axele și întrebările treptei (1 per construcție).
2. **DNA EXTRACTION** — după ce există ≥2 construcții, extrage ADN-ul real (ca T2_DNA).
3. **ARCHITECTURE BIBLE** — normalizează ADN-ul în reguli (ca T2_ARCHITECTURE_BIBLE).
4. **POSITION MATRIX** — mapează pozițiile structurale (ca T2_POSITION_MATRIX).
5. **IMPLEMENTATION** — construcțiile, contra Bible, cu propagare transversală.
6. **DRIFT DETECTOR** — verifică abaterile + drift score.
7. **RELEASE GATE** — 10 gate-uri.
8. **VERSIONING** — changelog + commit descriptiv.
9. **AUDIT FINAL** — audit advers de treaptă (identitate + lanț + cursant + manager).

## 4. REGULI DE COLABORARE CU AI

- **AI CREEAZĂ** doar: construcție nouă din blueprint aprobat, documente de guvernanță, poze (din prompt aprobat).
- **AI MODIFICĂ** doar: cu impact analysis + propagare transversală; copy de impact doar în runde dedicate.
- **AI DOAR AUDITEAZĂ** când: arhitectul cere audit (nu implementare).
- **AI CERE DECIZIE ARHITECTURALĂ** când: regulă sacră, identitate locked, decizie
  structurală (ex C06 E4), conflict de autoritate, payoff/WOW/motto.
- **AI VERIFICĂ TRANSVERSAL** la ORICE modificare de poziție structurală — obligatoriu.

## 5. REGULI PENTRU CONSTRUCȚII NOI
- Niciun HTML fără blueprint.
- Niciun blueprint fără Bible.
- Nicio modificare fără impact analysis.
- Nicio construcție fără drift score.
- Nicio treaptă fără position matrix.
- COPY+MODIFY pornește din `c01` (referința-cobai), nu dintr-o construcție divergentă.

## 6. PROTOCOL PENTRU TREPTE VIITOARE (T3+)

- **Pornire T3:** definește axele (T3 = ANALIZĂ: interpretează ce a cunoscut T2).
- **Extrage ADN T3** după primele 2 construcții.
- **Compară cu T2:** scheletul (6/18/5/8/2) se moștenește; identitatea diferă (T3
  INTERPRETEAZĂ, T2 DESCRIE).
- **Evită contaminarea inversă:** T3 NU repetă competențe T2 (nu re-inventaria, nu
  re-clasifica); T2 NU face T3 (garda din Bible S2).
- **Coerență între trepte:** semnăturile retorice (mantra „Nu X. Y", motto „Un X. Apoi
  orice Y") se păstrează ca limbaj Trainity; conținutul se schimbă pe treaptă.

## 7. CHECKLIST FINAL PENTRU ARHITECT
**Ce trebuie să ceară:** blueprint înainte de HTML; position matrix; drift score; audit
advers; propagare transversală dovedită.
**Ce trebuie să verifice:** identitate distinctă (test 10s); AHA locked; garda T2/T3;
handoff; uniformitate transversală.
**Ce nu trebuie să accepte:** fix local nepropagat; payoff/WOW modificat ad-hoc; termeni
T3 în T2; „AUDIT" în T2; construcție fără hero dedicat; cosmetizarea unui reziduu structural.
**Când oprește implementatorul:** când modifică o regulă sacră fără aprobare; când
optimizează local în loc de transversal; când rescrie în loc de uniformizează; când
inventează reguli nesusținute de construcțiile existente.
