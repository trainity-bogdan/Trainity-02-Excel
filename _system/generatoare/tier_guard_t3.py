#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tier_guard_t3.py - garda tehnica TIER-AWARE pentru TREAPTA 3 (C09-C12).

Implementeaza mecanic garda T3 inghetata in Bible §T3 + 12-ARHITECTURA-CONCEPTUALA-T3
(BRAIN-006). Detector SEPARAT, ca sa NU atinga audit_sync / gate_v20 (care pazesc
ZERO DRIFT si gardele T1/T2). Stdlib only (re/glob/os).

Ce verifica, tier-aware:
  1. INVERSIUNE T2->T3: Data Model / join / comparatie / trend / KPI sunt INTERZISE
     in T2 (C05-C08) dar PERMISE in T3 (C09-C12). Acelasi termen, verdict opus dupa
     treapta. (R-TIER-PARAM)
  2. INTRA-T3 (verb-semnatura): fiecare constructie isi ancoreaza verbul propriu;
     verbul altei constructii T3 ca ancora in sloturile de identitate = contaminare.
       C09 a lega · C10 a defini (motto: masoara) · C11 a compara · C12 a explica
  3. T3 -> T4/T5: dashboard / grafic publicabil / raport vizual / cockpit-scorecard
     vizual / alerta / actiune automata / recomandare executata = INTERZIS in T3.
  4. C09 GUARD special (granita C09|C10): C09 poate Data Model/relatii/chei/
     cardinalitate/1:M + prima citire cross-tabel; NU poate defini masuri numite
     (C10), ranking (C11), explica cauze (C12), dashboard (T4).

R-TEASER-1: un termen al treptei/constructiei urmatoare, intr-un context de teaser
sau handoff explicit (ex. "C09 deschide Data Model", "Preda catre C10"), NU e
contaminare. Whitelist automat.

Buckets de raportare:
  - T2_RELAX   : termen T3-permis aparut intr-o constructie T2 (= contaminare T2)
  - INTRA_T3   : verb-semnatura al unei constructii ancorat in alta (slot identitate)
  - T3_TO_T4T5 : termen T4/T5 intr-o constructie T3
  - WARN       : semnal non-blocant (ancora in afara sloturilor de identitate)

Uz:
  python3 tier_guard_t3.py            # ruleaza pe c09..c12 existente (N/A daca lipsesc)
  python3 tier_guard_t3.py c09        # o singura constructie
  python3 tier_guard_t3.py --self-test  # demonstreaza regulile pe fixturi inline
  exit code: 0 = curat / N/A, 1 = erori blocante.
"""
import sys, os, re, glob

# ---------------------------------------------------------------- helpers
def _fold(s):
    # pliaza diacriticele RO -> ASCII, lowercase. Translate 1:1 => pastreaza
    # lungimea => indicii din textul foldat se aliniaza cu originalul.
    return s.translate(str.maketrans('ăâîșțĂÂÎȘȚşţ', 'aaistAAISTst')).lower()

def _strip_noise(t):
    t = re.sub(r'data:image[^"\')]+', '', t)
    t = re.sub(r'<style[^>]*>.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.S)
    return t

def tier_of(nn):
    n = int(nn)
    return ('T1' if n <= 4 else 'T2' if n <= 8 else
            'T3' if n <= 12 else 'T4' if n <= 16 else 'T5')

# Marker de teaser / handoff (R-TEASER-1). Cautat in fereastra din jurul gasirii.
_TEASER_RX = re.compile(r'c0[5-9]|c1[0-6]|deschide|preda|treapta urm|handoff|next')

def _is_teaser(window_folded):
    return bool(_TEASER_RX.search(window_folded))

# ---------------------------------------------------------------- term banks
# Conventie de potrivire:
#   "term"  -> potrivire PREFIX (stem), cu granita la stanga (ex. "masur"
#              prinde masura/masuri/masoara-NU; "explic" prinde explica/explicam).
#   "=term" -> potrivire CUVANT INTREG (ambele granite), pentru tokeni scurti
#              ambigui in romana (merge, top, abc, join, trend, ranking...).
def _matches(term, folded):
    if term.startswith('='):
        rx = re.compile(r'(?<![a-z0-9])' + re.escape(term[1:]) + r'(?![a-z0-9])')
    else:
        rx = re.compile(r'(?<![a-z0-9])' + re.escape(term))
    return [m.start() for m in rx.finditer(folded)]

def _find(terms, folded, original, teaser_ok=True):
    """[(term, ctx)] pentru fiecare termen; sare gasirile in context de teaser."""
    out = []
    for term in terms:
        for i in _matches(term, folded):
            win = folded[max(0, i-80):i+len(term)+80]
            if teaser_ok and _is_teaser(win):
                continue
            ctx = re.sub(r'\s+', ' ', original[max(0, i-30):i+len(term)+30]).strip()
            out.append((term.lstrip('='), ctx))
    return out

# Ce ramane INTERZIS in T2 (garda T2/T3 din Bible §T2). 'merge' scos: verb RO comun
# si nu e in lista Bible §T2; 'join' = cuvant intreg (unambiguu, doar englez).
T2_FORBIDDEN = ['data model', '=join', '=kpi', 'comparat', 'comparati', '=trend',
                'cel mai mare', 'cel mai mic', '=ranking', 'dashboard']
# Interzis in T3 fiindca apartine T4 (vizual) sau T5 (actiune).
T4T5_FORBIDDEN = ['dashboard', 'grafic publicabil', 'raport vizual', 'cockpit',
                  'scorecard', 'slicer', 'alert', 'actiune automata',
                  'recomandare execut', 'flux decizional', 'refresh automat',
                  'buton de actiune']
# Verb-semnatura per constructie T3: ancore PROPRII vs INTERZISE (ale altora).
SIGNATURE = {
    '09': {'verb': 'a lega',
           'own': ['a lega', 'legatur', 'relati', 'model', 'tabele conectate',
                   'cardinalitate', 'chei', '=1:m', '=join', '=merge', 'cross-tabel'],
           'forbidden': ['a defini', 'definim', 'masura vie', 'clasament', '=ranking',
                         '=top', 'bottom', 'de ce', 'explic', 'cauz', 'dashboard']},
    '10': {'verb': 'a defini', 'motto_verb': 'masoara',
           'own': ['a defini', 'definim', 'defineste', 'masur', 'context',
                   'single source', 'sursa unic'],
           'forbidden': ['=ranking', '=top', 'bottom', 'clasament', 'a compara',
                         'comparam', 'explic', 'de ce', 'cauz', 'dashboard']},
    '11': {'verb': 'a compara',
           'own': ['a compara', 'comparam', 'comparat', 'clasament', 'diferent',
                   'contributi', '=ranking', '=top', 'bottom', 'pareto', '=abc'],
           'forbidden': ['cauz', 'de ce', 'explic', 'insight final', 'dashboard',
                         'grafic publicabil']},
    '12': {'verb': 'a explica',
           'own': ['a explica', 'explicam', 'explic', 'de ce', 'cauz', 'insight',
                   'interpret'],
           'forbidden': ['dashboard', 'grafic publicabil', 'raport vizual', 'alert',
                         'actiune', 'recomandare execut', 'what-if', 'what if',
                         'scenari']},
}
# Sloturile de identitate unde ancorarea conteaza (FAIL); in afara lor = WARN.
IDENTITY_SLOT_CLASSES = ['hero-question-text', 'greseala', 'mantra-band-main',
                         'payoff-wow', 'payoff-motto', 'cine-devii', 'data-bomba',
                         'data-aha', 'data-wow', 'data-motto', 'data-greseala']

def _slot_text(html):
    chunks = []
    for cls in IDENTITY_SLOT_CLASSES:
        for m in re.finditer(r'(?:class|data-[a-z]+)="[^"]*' + re.escape(cls) +
                             r'[^"]*"[^>]*>(.*?)<', html, re.S):
            chunks.append(re.sub('<[^>]+>', ' ', m.group(1)))
    return ' '.join(chunks)

# ---------------------------------------------------------------- core scan
def scan(nn, text):
    """Returneaza (findings, has_blocking). finding = (bucket, sev, term, ctx)."""
    t = tier_of(nn)
    stripped = _strip_noise(text)
    folded = _fold(stripped)
    slot = _slot_text(stripped)
    slot_folded = _fold(slot)
    findings = []

    if t == 'T2':
        # garda T2 NU se relaxeaza: termenii T3 raman contaminare in T2,
        # MINUS teaserele/handoff-urile legitime (R-TEASER-1).
        for term, ctx in _find(T2_FORBIDDEN, folded, stripped):
            findings.append(('T2_RELAX', 'ERROR', term, ctx))
        return findings, any(s == 'ERROR' for _, s, _, _ in findings)

    if t != 'T3':
        return findings, False  # garda asta e doar pentru T3

    # --- T3 -> T4/T5 (interzis vizual / actiune), minus teaser catre T4/T5
    for term, ctx in _find(T4T5_FORBIDDEN, folded, stripped):
        findings.append(('T3_TO_T4T5', 'ERROR', term, ctx))

    # --- intra-T3 verb-semnatura
    sig = SIGNATURE.get(nn)
    if sig:
        # ancore INTERZISE (ale altor constructii) in sloturile de identitate = FAIL.
        # In sloturi NU aplicam whitelist de teaser (sloturile sunt identitate pura).
        for term, ctx in _find(sig['forbidden'], slot_folded, slot, teaser_ok=False):
            if term in ('dashboard', 'grafic publicabil', 'raport vizual'):
                continue  # deja prins de T3_TO_T4T5
            findings.append(('INTRA_T3', 'ERROR', term, ctx))
        # aceleasi ancore in corp (in afara sloturilor) = WARN, minus teaser/handoff
        body_folded = folded.replace(slot_folded, ' ') if slot_folded else folded
        for term, ctx in _find(sig['forbidden'], body_folded, stripped):
            if term in ('dashboard', 'grafic publicabil', 'raport vizual'):
                continue
            if any(f[2] == term and f[0] == 'INTRA_T3' for f in findings):
                continue
            findings.append(('WARN', 'WARNING', term, ctx))

    has_block = any(s == 'ERROR' for _, s, _, _ in findings)
    return findings, has_block

# ---------------------------------------------------------------- per-constructie
def run_construction(nn_dir):
    nn = re.sub(r'\D', '', os.path.basename(nn_dir.rstrip('/')))[-2:].zfill(2)
    htmls = sorted(glob.glob(os.path.join(nn_dir, 'HTML-*.html')))
    if not htmls:
        print(f"[{nn_dir}] N/A - nu exista HTML (constructie negenerata)")
        return 0, 0
    total_block = total_warn = 0
    for f in htmls:
        text = open(f, encoding='utf-8', errors='ignore').read()
        findings, _ = scan(nn, text)
        for bucket, sev, term, ctx in findings:
            tag = 'FAIL' if sev == 'ERROR' else 'WARN'
            print(f"  [{tag}] {bucket:11s} {os.path.basename(f)}: '{term}' :: {ctx}")
            if sev == 'ERROR':
                total_block += 1
            else:
                total_warn += 1
    verdict = 'FAIL' if total_block else ('WARNING' if total_warn else 'PASS')
    print(f"[{nn_dir}] tier={tier_of(nn)} -> {verdict} "
          f"({total_block} blocante, {total_warn} avertismente)")
    return total_block, total_warn

# ---------------------------------------------------------------- self-test
def self_test():
    """Demonstreaza regulile pe fixturi inline (C09-C12 inca negenerate)."""
    def slot(cls, txt):
        return f'<p class="{cls}">{txt}</p>'
    cases = [
        ("Data Model PERMIS in T3 (C09)", '09',
         slot('hero-question-text', 'Cum leg tabelele in Data Model?'),
         [], ['T2_RELAX', 'T3_TO_T4T5', 'INTRA_T3']),
        ("Data Model INTERZIS in T2 (C08, non-teaser)", '08',
         '<p>Construim un Data Model peste set, ca livrabil.</p>',
         ['T2_RELAX'], []),
        ("Data Model in TEASER T2 = PERMIS (R-TEASER-1)", '08',
         '<p class="step-action">Preda catre C09. C09 deschide Data Model.</p>',
         [], ['T2_RELAX']),
        ("'merge' (verb RO) NU e flag in T2", '08',
         '<p>Mergem la pas sarit prin tabel.</p>',
         [], ['T2_RELAX']),
        ("dashboard INTERZIS in T3 (C12)", '12',
         '<p>Livram un dashboard executiv.</p>',
         ['T3_TO_T4T5'], []),
        ("'a defini' PERMIS ca verb C10", '10',
         slot('mantra-band-main', 'Nu scriem cifra. O definim.'),
         [], ['INTRA_T3', 'T3_TO_T4T5']),
        ("ranking PERMIS in C11", '11',
         slot('hero-question-text', 'Cum transform masurile intr-un ranking?'),
         [], ['INTRA_T3', 'T3_TO_T4T5']),
        ("ranking INTERZIS in C10 (e verbul C11)", '10',
         slot('greseala', 'Profesionistii fac ranking pe masuri.'),
         ['INTRA_T3'], []),
        ("What-if NU e identitate C12", '12',
         slot('hero-question-text', 'Construim un model what-if de scenarii.'),
         ['INTRA_T3'], []),
        ("cauza/de ce INTERZIS ca ancora in C11", '11',
         slot('greseala', 'Explicam de ce a crescut clientul.'),
         ['INTRA_T3'], []),
    ]
    ok = True
    for name, nn, html, must, mustnot in cases:
        findings, _ = scan(nn, html)
        buckets = {b for b, _, _, _ in findings}
        miss = [b for b in must if b not in buckets]
        extra = [b for b in mustnot if b in buckets]
        passed = not miss and not extra
        ok = ok and passed
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        if not passed:
            print(f"        buckets={sorted(buckets)} lipsa={miss} nedorit={extra}")
    print(f"\nSELF-TEST: {'PASS' if ok else 'FAIL'} ({len(cases)} cazuri)")
    return 0 if ok else 1

# ---------------------------------------------------------------- main
def main():
    args = sys.argv[1:]
    if '--self-test' in args:
        sys.exit(self_test())
    targets = [a for a in args if not a.startswith('-')]
    if not targets:
        targets = [d for d in ('c09', 'c10', 'c11', 'c12') if os.path.isdir(d)]
        if not targets:
            print("Nicio constructie T3 generata inca (c09-c12 absente). "
                  "Garda e gata; ruleaza --self-test pentru demonstratie.")
            sys.exit(0)
    total_block = 0
    for d in targets:
        b, _ = run_construction(d)
        total_block += b
    sys.exit(1 if total_block else 0)

if __name__ == '__main__':
    main()
