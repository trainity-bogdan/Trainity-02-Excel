#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R-V65.form-drift  ·  Detector de contaminare de FORMA (content-blind)
=====================================================================

Scop: prinde MATRITELE RETORICE reciclate intre constructii, nu continutul.
Auditurile de pana acum (audit_sync, gate_v20) verifica structura, identitatea,
anti-clona narativa, dash, nume FILM, clone de imagine. NICIUNUL nu vede FORMA:
doua sloturi pot avea continut complet diferit dar aceeasi schela sintactica
("Oamenii X. Profesionistii Y." x8, "Nu mai vezi X. Vezi Y." x6 etc.).

Metoda (content-blind, semantic-blind):
  1. Extrage sloturile-semnatura din HTML-Studiu + cele 6 campuri de corp FILM.
  2. Pliaza diacriticele, lowercase.
  3. MASCARE: pastreaza doar markerii structurali/functionali (lista alba);
     orice substantiv / verb-axa / concept devine '•'. Colapseaza '•' repetate.
     Rezulta SEMNATURA DE FORMA a slotului, independenta de continut.
  4. Grupeaza constructiile pe semnatura identica + similaritate difflib.
  5. Verdict PASS / WARNING / FAIL per slot, pe praguri.

Plus: detectie de BOILERPLATE INTRA-FILM (cele 6 etape ale unui camp identice).

Doar stdlib (re, html, glob, zipfile, difflib, unicodedata). Fara dependente.

Rulare:
    python3 _system/generatoare/detect_form_drift.py
    python3 _system/generatoare/detect_form_drift.py --verbose
"""

import re, html, glob, zipfile, unicodedata, sys, os
from collections import defaultdict
from difflib import SequenceMatcher

# ----------------------------------------------------------------------------
# Lista alba de markeri structurali / functionali (forme pliate de diacritice).
# Tot ce NU e aici devine '•'. Aici traieste scheletul sintactic; substantivele
# si verbele-axa (continutul) sunt mascate.
# ----------------------------------------------------------------------------
WHITELIST = set("""
nu nici fara
un o niste unei unui unor acest aceasta acestui acestei fiecare orice tot toata
toate toti alt alta altul alta acelasi aceeasi aceleasi
de la in pe cu din pentru prin pana peste sub spre catre despre dintr dintre
dintru asupra langa fata
si sau dar insa iar ci ca daca desi fiindca deci totusi apoi atunci asadar
el ea ei ele tu noi voi eu le il ii o se isi ma te ne va care ce cine cui
ale carui carei caror lui ei
este e sunt era fi fie am ai a au vei va vom veti vor poate pot
mai deja inca acum abia doar numai chiar niciodata mereu maine azi astazi
intai inainte dupa cat decat mult putin necesar
vezi incepe inseamna construim facem cunosti enumera
oamenii profesionistii
""".split())

# Markeri de frame care, desi lexicali, SUNT semnatura (anchore de matrita).
# Inclusi explicit in WHITELIST mai sus: vezi, incepe, inseamna, oamenii,
# profesionistii, construim, facem, cunosti, enumera.

# Semnaturi intentionate, exceptate (ca EXEC_CLONE_EXCEPTIONS din audit_sync):
# handoff de serie + etichete structurale. Nu dau FAIL.
ALLOWED_FORM_CLONES = {
    "handoff": re.compile(r"^c0\d poate incepe", re.I),
}

SLOT_LABELS = ["BOMBA", "GRESEALA", "AHA", "MANTRA", "WOW", "MOTTO", "CINE-DEVII", "PAYOFF"]
FILM_FIELDS = ["STARE", "VOCEA", "DEMONSTRATIA", "INTERVENTIA", "MOMENT", "REVEAL"]


def fold(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower()


def text_of(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def strip_noise(c):
    # L191: scoate base64/style/script inainte de orice scan lexical
    c = re.sub(r"data:image[^\"')]+", " ", c)
    c = re.sub(r"<style.*?</style>", " ", c, flags=re.S)
    c = re.sub(r"<script.*?</script>", " ", c, flags=re.S)
    return c


def skeleton(text):
    """Reduce textul la semnatura de forma: markeri structurali + punctuatie,
    restul mascat '•'. Content-blind."""
    text = fold(text)
    toks = re.findall(r"[a-z]+|[.,:?!;]", text)
    out = []
    for t in toks:
        if t in ".,:?!;":
            out.append(t)
        elif t in WHITELIST:
            out.append(t)
        else:
            out.append("•")
    # colapseaza '•' consecutive
    r = []
    for x in out:
        if x == "•" and r and r[-1] == "•":
            continue
        r.append(x)
    return " ".join(r).strip()


def is_allowed(text):
    f = fold(text).strip()
    return any(p.search(f) for p in ALLOWED_FORM_CLONES.values())


# ----------------------------------------------------------------------------
# Extractie sloturi din HTML-Studiu
# ----------------------------------------------------------------------------
def extract_studiu(path):
    c = strip_noise(open(path, encoding="utf-8").read())
    g = {}

    def grab(pat):
        m = re.search(pat, c, re.S)
        return text_of(m.group(1)) if m else ""

    g["BOMBA"] = re.sub(r"^SUN[ÄÂA]? ?CUNOSCUT\??\s*", "",
                        grab(r'tu-section tu-recunoastere">(.*?)</section>'),
                        flags=re.I)
    g["GRESEALA"] = re.sub(r"^GRE[SȘ]EALA[^A-Za-z]*CLASIC[AĂ]?\s*", "",
                           grab(r'tu-section tu-greseala">(.*?)</section>'), flags=re.I)
    g["AHA"] = re.sub(r"^AHA\s*", "", grab(r'tu-section tu-aha">(.*?)</section>'))
    g["CINE-DEVII"] = re.sub(r"^CINE DEVII\s*", "",
                             grab(r'tu-section tu-promise">(.*?)</section>'))
    g["MANTRA"] = grab(r'class="mantra-band-main"[^>]*>(.*?)</')
    g["MOTTO"] = grab(r'class="payoff-motto"[^>]*>(.*?)</')
    wow = re.search(r'data-wow="1"[^>]*>(.*?)</', c, re.S)
    g["WOW"] = text_of(wow.group(1)) if wow else ""
    dims = re.findall(r'class="payoff-line dim"[^>]*>(.*?)</', c, re.S)
    g["PAYOFF"] = " ".join(text_of(d) for d in dims[:3])
    return g


# ----------------------------------------------------------------------------
# Extractie corp FILM (6 campuri x 6 etape) din docx
# ----------------------------------------------------------------------------
def film_paragraphs(docx):
    z = zipfile.ZipFile(docx)
    xml = z.read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        t = html.unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S))).strip()
        if t:
            out.append(t)
    return out


def field_of(label):
    u = fold(label)
    if u.startswith("stare") and "exec" not in u:
        return "STARE"
    if u.startswith("vocea"):
        return "VOCEA"
    if u.startswith("demonstra"):
        return "DEMONSTRATIA"
    if u.startswith("interventia"):
        return "INTERVENTIA"
    if u.startswith("moment de control"):
        return "MOMENT"
    if u == "reveal":
        return "REVEAL"
    return None


def extract_film(docx):
    """Returneaza {camp: [continut_etapa_1..6]} - continutul = paragraful de dupa eticheta."""
    ps = film_paragraphs(docx)
    fields = defaultdict(list)
    for i, p in enumerate(ps):
        f = field_of(p)
        if f and i + 1 < len(ps):
            nxt = ps[i + 1]
            if field_of(nxt) is None:  # nu e alta eticheta
                fields[f].append(nxt)
    return fields


# ----------------------------------------------------------------------------
# Analiza de grupare + verdict
# ----------------------------------------------------------------------------
def verdict_for_slot(sig_by_cc):
    """sig_by_cc: {CC: skeleton}. Returneaza (verdict, groups, max_ratio)."""
    items = [(cc, s) for cc, s in sig_by_cc.items() if s]
    N = len(items)
    groups = defaultdict(list)
    for cc, s in items:
        groups[s].append(cc)
    g = max((len(v) for v in groups.values()), default=0)
    # similaritate maxima intre perechi de skeleton distincte
    sigs = [s for _, s in items]
    max_ratio = 0.0
    for i in range(len(sigs)):
        for j in range(i + 1, len(sigs)):
            r = SequenceMatcher(None, sigs[i], sigs[j]).ratio()
            max_ratio = max(max_ratio, r)
    if N == 0:
        return "N/A", groups, 0.0, 0
    third = -(-N // 3)   # ceil(N/3)
    half = N // 2
    triple_sim = sum(1 for i in range(len(sigs)) for j in range(i + 1, len(sigs))
                     if SequenceMatcher(None, sigs[i], sigs[j]).ratio() >= 0.85)
    if g > half or triple_sim >= 3:
        v = "FAIL"
    elif g > third or max_ratio >= 0.60:
        v = "WARNING"
    else:
        v = "PASS"
    return v, groups, max_ratio, g


def main():
    verbose = "--verbose" in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.chdir(root)

    constr = sorted([d for d in glob.glob("c0*") if os.path.isdir(d)])
    studiu = {}
    film = {}
    for d in constr:
        cc = d.upper()
        sp = glob.glob(f"{d}/HTML-Studiu-*.html")
        if sp:
            studiu[cc] = extract_studiu(sp[0])
        fp = glob.glob(f"{d}/FILM-*.docx")
        if fp:
            film[cc] = extract_film(fp[0])

    print("=" * 78)
    print("R-V65.form-drift  ·  BASELINE C01-C08  ·  audit de FORMA (content-blind)")
    print("=" * 78)

    # ---- PART A: sloturi de identitate (inter-constructie) ----
    print("\n### PARTEA A · SLOTURI-SEMNATURA (Studiu) · grupare pe forma\n")
    slot_verdicts = {}
    for slot in SLOT_LABELS:
        sig = {cc: skeleton(studiu[cc].get(slot, "")) for cc in studiu}
        v, groups, mr, g = verdict_for_slot(sig)
        slot_verdicts[slot] = v
        big = sorted(groups.items(), key=lambda x: -len(x[1]))
        flag = {"FAIL": "❌", "WARNING": "⚠️ ", "PASS": "✅", "N/A": "··"}[v]
        print(f"{flag} {slot:<11} grup-max={g}/{len(sig)}  sim-max={mr:.2f}  -> {v}")
        for sk, ccs in big[:3]:
            print(f"      [{len(ccs)}x {','.join(ccs)}]  {sk[:74]}")

    # ---- PART B: boilerplate intra-FILM (cele 6 etape identice?) ----
    print("\n### PARTEA B · CORP FILM · variatie intre cele 6 etape (boilerplate?)\n")
    print(f"{'':6}" + "".join(f"{f[:6]:>8}" for f in FILM_FIELDS) + "   MEDIE")
    film_scores = {}
    for cc in sorted(film):
        row = []
        for f in FILM_FIELDS:
            stages = film[cc].get(f, [])
            if not stages:
                row.append(None)
                continue
            sk = [skeleton(s) for s in stages]
            distinct = len(set(sk))
            row.append(distinct / len(sk))   # 1.0 = toate distincte, ~.17 = toate identice
        vals = [x for x in row if x is not None]
        avg = sum(vals) / len(vals) if vals else 0
        film_scores[cc] = avg
        cells = "".join((f"{x*100:7.0f}%" if x is not None else f"{'--':>8}") for x in row)
        tag = "❌ BOILERPLATE" if avg < 0.30 else ("⚠️ partial" if avg < 0.70 else "✅")
        print(f"{cc:6}{cells}   {avg*100:4.0f}%  {tag}")

    # ---- SCORURI DE DIFERENTIERE ----
    # IMPORTANT: gruparea pe potrivire EXACTA de skeleton e pacalita de
    # conjunctii minore (cu/fiindca/ce se) => supraestimeaza unicitatea si
    # contrazice verdictele FAIL (care vin din similaritate). De aceea scorul
    # foloseste CLUSTERING pe similaritate (>=SIM_CLUSTER), nu potrivire exacta.
    SIM_CLUSTER = 0.80
    print("\n### SCOR DE DIFERENTIERE DE FORMA  (cluster sim>=%.2f)\n" % SIM_CLUSTER)

    def cluster_size_of(cc, slot_sig):
        """Marimea clusterului de forma din care face parte cc pe acest slot."""
        s = slot_sig.get(cc, "")
        if not s:
            return None
        size = 0
        for cc2, s2 in slot_sig.items():
            if s2 and SequenceMatcher(None, s, s2).ratio() >= SIM_CLUSTER:
                size += 1
        return size

    slot_sigs = {slot: {cc: skeleton(studiu[cc].get(slot, "")) for cc in studiu}
                 for slot in SLOT_LABELS}
    per_constr = {}
    for cc in sorted(studiu):
        us = []
        for slot in SLOT_LABELS:
            cs = cluster_size_of(cc, slot_sigs[slot])
            if cs:
                us.append(1.0 / cs)
        per_constr[cc] = sum(us) / len(us) if us else 0
    for cc in sorted(per_constr):
        print(f"   {cc}: forma-unica {per_constr[cc]*100:4.0f}%")

    def tier_avg(ccs):
        v = [per_constr[c] for c in ccs if c in per_constr]
        return sum(v) / len(v) * 100 if v else 0
    t1 = tier_avg(["C01", "C02", "C03", "C04"])
    t2 = tier_avg(["C05", "C06", "C07", "C08"])
    sys_avg = sum(per_constr.values()) / len(per_constr) * 100
    print(f"\n   T1 (C01-C04): {t1:4.0f}%   T2 (C05-C08): {t2:4.0f}%   SISTEM: {sys_avg:4.0f}%")

    # ---- SUMAR ----
    fails = [s for s, v in slot_verdicts.items() if v == "FAIL"]
    warns = [s for s, v in slot_verdicts.items() if v == "WARNING"]
    passes = [s for s, v in slot_verdicts.items() if v == "PASS"]
    film_bp = [cc for cc, a in film_scores.items() if a < 0.30]
    print("\n" + "=" * 78)
    print(f"SLOTURI  FAIL: {fails}")
    print(f"SLOTURI  WARN: {warns}")
    print(f"SLOTURI  PASS: {passes}")
    print(f"FILM boilerplate: {film_bp}")
    overall = "FAIL" if (len(fails) >= 3 or film_bp) else ("WARNING" if (fails or warns) else "PASS")
    print(f"VERDICT SISTEM R-V65: {overall}")
    print("=" * 78)
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
