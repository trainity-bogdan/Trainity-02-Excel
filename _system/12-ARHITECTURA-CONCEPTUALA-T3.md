# 12 · ARHITECTURA CONCEPTUALĂ T3 (AUTORITATE)

> **STATUT: AUTORITATE CONCEPTUALĂ T3.** Citește OBLIGATORIU înainte de orice C09-C12.
> Sursa de reguli mecanice = `governance/TRAINITY_ARCHITECTURE_BIBLE.md §T3` (SPEC-uri locked).
> Acest document explică treapta pentru chat-uri viitoare. Înghețat prin BRAIN-006.
> Oglinda lui `11-ARHITECTURA-CONCEPTUALA-T2.md` (autoritatea T2).

---

## CE ESTE T3
T3 = ANALIZĂ / INTERPRETARE. Setul CUNOSCUT (T2) devine INTERPRETAT.
**Regula de aur moștenită din T2:** „T2 pune etichete; T3 interpretează etichetele."
Întrebarea treptei: **„Pot obține răspunsuri?"**

## CE REZOLVĂ T3 (problema mare)
La sfârșitul T2 ai un set complet cunoscut (vocabular C05, sens C06, calendar C07, hartă C08), dar MUT: știi totul DESPRE date, dar datele nu îți RĂSPUND la o întrebare de business. Ai patru tabele corecte, înțelese, datate, cartografiate, și niciun răspuns care să le traverseze. T3 umple golul dintre „înțeleg datele" și „obțin răspunsuri".

## TRANSFORMAREA T3 CAP-COADĂ
```
legături recunoscute (C08)
   -> model interogabil (C09)
   -> măsură vie (C10)
   -> clasament (C11)
   -> cauză / înțeles (C12)
   -> predare către T4
```
Fiecare construcție CONSUMĂ output-ul precedentei. Cursantul intră cu un set descriptiv și iese cu un model care răspunde la întrebări de business, fără să fi desenat un raport (T4) sau automatizat ceva (T5).

---

## LANȚUL C09-C12 (identități LOCKED)

| | C09 RELAȚII | C10 MĂSURI | C11 COMPARAȚII | C12 INTERPRETARE |
|---|---|---|---|---|
| Întrebare-mamă | Ce pot întreba? | Cât? | Care? | De ce? |
| Verb-semnătură | a lega | a defini (motto: măsoară) | a compara | a explica |
| Substantiv | relația / modelul | măsura vie | clasamentul | cauza / înțelesul |
| Output | model interogabil (1:M) | măsură stabilă | clasament / diferență | insight verbal |
| Predă | C10 | C11 | C12 | T4 |

**Gramatica de treaptă (din Bible §T3):** MOTTO = slot de treaptă, poartă verbul generic („Întrebi [WH]. Modelul [verb]."). HERO/GREȘEALA/MANTRA/WOW/CINE DEVII = sloturi de construcție, poartă verbul-semnătură propriu. Verbul-semnătură al unei construcții e INTERZIS ca ancoră în slotturile alteia (regula anti-contaminare).

---

## ARHITECTURA FIECĂREI CONSTRUCȚII

### C09 RELAȚII (LOCKED, TIER SEED al T3)
- **Problema:** date cunoscute dar izolate; un răspuns trăiește în mai multe tabele care nu se caută.
- **Produce:** modelul relațional (relații 1:M active, Data Model coerent, prima citire cross-tabel).
- **Instrumente:** Data Model, relații 1:M, cardinalitate, chei, tabele conectate, merge/join.
- **Livrabil:** Date_MASTER-C09 (_MODEL/relații active) + 4 HTML + FILM + hero + 6 exec-stage + Creativ.
- **NU are voie:** măsuri (C10), comparații (C11), explicații (C12), raportare (T4), acțiune (T5).
- **AHA:** „Fără relații ai date. Cu relații ai răspunsuri."

### C10 MĂSURI (LOCKED, varianta revizuită)
- **Problema:** fiecare calculează altă cifră pentru aceeași întrebare; o cifră bună pentru o felie e greșită pentru alta.
- **Produce:** o măsură vie (definită o dată, context-aware, single source of truth).
- **Instrumente:** măsuri, agregări, DAX de bază, context de filtrare, Power Pivot, single source of truth.
- **Livrabil:** Date_MASTER-C10 (măsuri definite peste model) + machetele.
- **NU are voie:** ranking/comparații (C11), explicații (C12), dashboard (T4), acțiune (T5).
- **AHA:** „Un număr stă în tabel. O măsură trăiește în întrebare."

### C11 COMPARAȚII (LOCKED)
- **Problema:** măsuri corecte, dar nu știi care contează.
- **Produce:** clasament / diferență / contribuție.
- **Instrumente:** ranking, top/bottom, diferențe, contribuții (% din total), sortare analitică, ABC/Pareto ca instrumente.
- **Livrabil:** Date_MASTER-C11 (clasamente/contribuții) + machetele.
- **NU are voie:** explicații cauzale (C12), grafic publicabil (T4), decizie automată (T5).
- **AHA:** „Un număr nu e mare sau mic. E mare sau mic față de altul."

### C12 INTERPRETARE (LOCKED, închide T3)
- **Problema:** știi care a crescut, nu de ce; un clasament fără cauză nu e decizie.
- **Produce:** insight verbal / cauză / înțeles citit din model. Închide treapta.
- **Instrumente:** citire din model, drill-down ANALITIC (citire, nu widget T4), explicație, cauză, insight verbal.
- **Livrabil:** Date_MASTER-C12 + machetele cu insight explicativ.
- **NU are voie:** dashboard/grafic/raport vizual (T4); decizie/alertă/acțiune (T5); What-if ca identitate.
- **AHA:** „Cifrele spun ce. Numai interpretarea spune de ce."

---

## GRANIȚE ÎNTRE CONSTRUCȚII
- **C09|C10:** C09 se oprește la MODEL; C10 începe la prima MĂSURĂ definită. (a lega vs a defini)
- **C10|C11:** C10 = cifra fiecăruia (absolut); C11 = ordinea/diferența (relativ). (a defini vs a compara)
- **C11|C12:** C11 = CARE (mărime); C12 = DE CE (cauză). (a compara vs a explica)

## GRANIȚE T2 / T3 / T4 / T5 (formula LOCKED)
**T3 produce răspunsul · T4 îl face vizibil · T5 îl pune în acțiune.**

| Treaptă | Întrebare | Output | Interzis |
|---|---|---|---|
| T2 CUNOAȘTERE | Ce există/înseamnă/când/cu cine? | set cunoscut | interpretare, comparație, join, Data Model, KPI (= T3+) |
| T3 ANALIZĂ | Pot obține răspunsuri? | model/măsură/clasament/cauză | dashboard/grafic publicabil (T4); alertă/acțiune (T5) |
| T4 RAPORTARE | Cum vede altcineva, dintr-o privire? | dashboard/cockpit/scorecard | a inventa răspunsuri noi (T3); acțiune automată (T5) |
| T5 AUTOMATIZARE | Cum se întâmplă fără mine? | refresh/alertă/flux/sistem | a re-analiza (T3) sau re-designa raportul (T4) ca lecție nouă |

**Nuanță:** decizia UMANĂ stă între T4 și T5 (consumatorul pachetului). Decizia AUTOMATĂ = T5.
**Inversiunea T2->T3:** termenii interziși în T2 (join, Data Model, comparație, trend, KPI) devin COMPETENȚĂ în T3 (R-TIER-PARAM, tier-aware).

---

## RISCURI (de ținut sub control la implementare)
- **C09 intră în C10:** garda permite C09 „măsuri de bază peste model" doar ca primă citire cross-tabel demonstrativă; definirea măsurilor numite = C10. Graniță de ținut strict.
- **C10 confundat cu C11:** mitigat de ancorarea C10 pe „define once / context", nu pe „cifre".
- **C12 fuge în T4/T5:** C12 = insight verbal; orice vizual = T4, orice acțiune = T5.
- **Saturația „Oamenii/Profesioniștii":** permisă în T3 ca semnătură (BRAIN-006), dar marcată ca risc de saturație pentru treptele următoare (diversificare la T4/T5).

## DECIZII LOCKED (BRAIN-006)
1. C10 = MĂSURI (nume). 2. Motto C10 = „Întrebi cât. Modelul măsoară." 3. Verb construcție C10 = „a defini". 4. Identitate C10 = măsura vie / define once / context-aware / single source of truth. 5. AHA C10 = „Un număr stă în tabel. O măsură trăiește în întrebare." 6. C12 = INTERPRETARE / „de ce". 7. „What-if/scenarii" retras din identitatea C12. 8. Formula granițelor: T3 produce / T4 vizibil / T5 acțiune. 9. „Oamenii/Profesioniștii" permisă în T3, risc de saturație notat.

## STARE DE IMPLEMENTARE
- Arhitectură T3 = ÎNGHEȚATĂ cap-coadă (Bible §T3 + acest document + 06-MAP realiniat).
- C09 = singura cu blueprint dedicat (`blueprints/BLUEPRINT-C09-RELATII.md`), gata de implementare.
- C10/C11/C12 = SPEC 11-slot locked în Bible; blueprint-urile dedicate se creează la SEED-ul fiecăreia.
