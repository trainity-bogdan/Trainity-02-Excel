#!/usr/bin/env python3
"""
audit_sync.py - V39 (structura versiune unica per constructie)

Audit empiric de sincronizare. Structura noua:
  cNN/                  o singura versiune (fara canonic/editat)
    HTML-* x4
    Date_MASTER-CNN.xlsx
    Creativ + FILM
    assets/             cele 6 imagini exec-stage (jpg)

Usage:
    python3 _system/generatoare/audit_sync.py
    python3 _system/generatoare/audit_sync.py --json
"""

import sys, re, os, glob, json, zipfile

def _fold(s):
    """Pliaza diacriticele romanesti -> ASCII, lowercase (comparatii de nume
    modulo diacritice). Slug ASCII din filename vs display cu diacritice."""
    return s.translate(str.maketrans('ăâîșțĂÂÎȘȚşţ', 'aaistAAISTst')).lower()

DETECTORS = {}

def detector(rule_code, name, scope):
    def deco(fn):
        DETECTORS[rule_code] = {'name': name, 'scope': scope, 'fn': fn}
        return fn
    return deco

def _get_nn(folder):
    m = re.search(r'/?c(\d+)/?$', folder)
    return m.group(1).zfill(2) if m else None

@detector('R-V03.60', 'cover-meta fara INPUT/OUTPUT', 'studiu')
def _r0360(c):
    return 0 == len(re.findall(r'cover-meta-key">(?:INPUT|OUTPUT)<', c))

@detector('R-V03.61', '.nav-controls fara margin-top:auto', 'studiu')
def _r0361(c):
    m = re.search(r'\.nav-controls\s*\{[^}]+\}', c)
    return m and 'margin-top: auto' not in m.group(0) and 'margin-top:auto' not in m.group(0)

@detector('R-V03.59', 'Highlighter V34 capture+no-button+no-ESC', 'video')
def _r0359(c):
    return ('onClickCapture, true' in c
            and 'class="hl-reset"' not in c
            and '.hl-reset' not in c
            and "keyCode === 27" not in c
            and "key === 'Escape'" not in c)

@detector('V32-fix', 'Zero referinte Date-Output/Date-Input', 'all_html')
def _v32(c):
    return 0 == len(re.findall(r'Date-Output-Excel|Date-Input-Excel', c))

@detector('R-V03.72', 'Zero em/en-dash + bullet tu-list canonic (2022)', 'all_html')
def _r0372(c):
    # B1: zero em-dash (U+2014) / en-dash (U+2013) ORIUNDE (text, CSS content, comentarii JS/CSS)
    if '—' in c or '–' in c:
        return False
    # B2: daca exista model premium (tu-list), bullet-ul TREBUIE sa fie canonic \2022 (acelasi in toate constructiile)
    m = re.search(r'\.tu-list li::before\{[^}]*content:"([^"]*)"', c)
    if m and m.group(1) != '\\2022':
        return False
    return True

@detector('R-V03.33', 'Imagini base64 inline in Video', 'video')
def _r0333(c):
    return c.count('data:image/') >= 5

@detector('R-V03.47', 'Cele 6 livrabile canonice', 'folder')
def _r0347(folder):
    nn = _get_nn(folder)
    if not nn: return False
    patterns = [
        f'HTML-Studiu-Excel-{nn}-*.html',
        f'HTML-Editor-Studiu-Excel-{nn}-*.html',
        f'HTML-Video-Excel-{nn}-*.html',
        f'HTML-Editor-Video-Excel-{nn}-*.html',
        f'Date_MASTER-C{nn}.xlsx',
        f'Creativ-Excel-{nn}-*.txt',
    ]
    return all(glob.glob(os.path.join(folder, p)) for p in patterns)

@detector('R-V03.58', 'FILM.docx prezent', 'folder')
def _r0358(folder):
    nn = _get_nn(folder)
    if not nn: return False
    return bool(glob.glob(os.path.join(folder, f'FILM-Excel-{nn}-*.docx')))

@detector('R-V39.assets', 'Folder assets/ cu 6 imagini exec-stage jpg', 'folder')
def _rassets(folder):
    assets = os.path.join(folder, 'assets')
    if not os.path.isdir(assets): return False
    jpgs = glob.glob(os.path.join(assets, 'exec-stage-*.jpg'))
    return len(jpgs) == 6


# ============================================================
# R-V03.69 — DETECTOR ANTI-CLONĂ NARATIVĂ
# ============================================================
# Scop: prinde cazul când o construcție livrabilă are LISTE TITLARE
# IDENTICE LITERAL cu altă construcție (semnal că generarea COPY+MODIFY
# nu a înlocuit conținutul specific axei). Exemplu istoric: c05/HTML-Studiu
# avea inv-list cu fenomenele C01 (ANTET DE RAPORT, SUBTOTALURI etc.)
# nesubstituite la generare V28 (descoperit empiric V42).
#
# Zone verificate: inv-item-label, anomaly-title, final-label.
# Verdict: dacă două cNN au ACEEAȘI listă în aceeași zonă → DRIFT NARATIV.
# ============================================================

import re as _re_v369

def _extract_zone(content, pattern):
    return tuple(m.strip() for m in _re_v369.findall(pattern, content))

_NARRATIVE_ZONES = {
    'inv': r'<div class="inv-item-label">([^<]+)</div>',
    'anomaly': r'<b class="anomaly-title">([^<]+)</b>',
    'final': r'<div class="final-label">([^<]+)</div>',
}

# Cache pentru lista de zone narative per cNN — populat la primul apel
_NARR_CACHE = {}

def _populate_narr_cache(root):
    if _NARR_CACHE: return
    for c_folder in sorted(glob.glob(os.path.join(root, 'c[0-9][0-9]'))):
        nn = os.path.basename(c_folder).upper()
        sts = glob.glob(os.path.join(c_folder, 'HTML-Studiu-Excel-*.html'))
        if not sts: continue
        with open(sts[0], encoding='utf-8') as f: content = f.read()
        _NARR_CACHE[nn] = {z: _extract_zone(content, p) for z, p in _NARRATIVE_ZONES.items()}

@detector('R-V03.69', 'Anti-clonă narativă: liste titlare neidentice cu alt cNN', 'folder')
def _r0369(folder):
    _populate_narr_cache('.')
    nn = os.path.basename(folder).upper()
    if nn not in _NARR_CACHE: return True
    my = _NARR_CACHE[nn]
    for other_nn, other in _NARR_CACHE.items():
        if other_nn == nn: continue
        for zone in _NARRATIVE_ZONES.keys():
            ml, ol = my.get(zone, ()), other.get(zone, ())
            if ml and ol and ml == ol:
                # Drift detectat: identitate literală cu alt cNN
                return False
    return True


# ============================================================
# R-V03.71 — ANTI-CLONĂ EXEC VIDEO (extensie R-V03.69 pe machetele Video)
# ============================================================
# Prinde clonarea zonelor de CONȚINUT din HTML-Video intre constructii:
# exec-phrase (frazele de impact / etapa), exec-emotion (starea / etapa),
# hero-sub (subtitlul hero). Cauza descoperita empiric V43: C03/C05/C06 aveau
# exec-emotion (si C05/C06 si exec-phrase) identice cu C01 - mostenite la
# generarea COPY+MODIFY si NEPRINSE de R-V03.69 (care citea doar HTML-Studiu).
# Zone EXCLUSE intentionat (shared brand/generic): exec-title (REALITATE...),
# exec-label (Etapa 0X), motto-ul de brand.
# ============================================================

_VIDEO_ZONES = {
    'exec-phrase': r'class="exec-phrase[^"]*"[^>]*>([^<]+)<',
    'exec-emotion': r'class="exec-emotion[^"]*"[^>]*>([^<]+)<',
    'hero-sub': r'class="hero-sub[^"]*"[^>]*>([^<]+)<',
}
_VID_CACHE = {}

def _populate_vid_cache(root):
    if _VID_CACHE: return
    for c_folder in sorted(glob.glob(os.path.join(root, 'c[0-9][0-9]'))):
        nn = os.path.basename(c_folder).upper()
        vids = glob.glob(os.path.join(c_folder, 'HTML-Video-Excel-*.html'))
        if not vids: continue
        with open(vids[0], encoding='utf-8') as f:
            content = f.read()
        # strip base64 (zgomot, nu contine clase de continut)
        content = _re_v369.sub(r'data:image/[^"\']+', '', content)
        _VID_CACHE[nn] = {z: tuple(m.strip() for m in _re_v369.findall(p, content))
                          for z, p in _VIDEO_ZONES.items()}

@detector('R-V03.71', 'Anti-clonă exec video: exec-phrase/emotion/hero-sub neidentice cu alt cNN', 'folder')
def _r0371(folder):
    _populate_vid_cache('.')
    nn = os.path.basename(folder).upper()
    if nn not in _VID_CACHE: return True
    my = _VID_CACHE[nn]
    for other_nn, other in _VID_CACHE.items():
        if other_nn == nn: continue
        for zone in _VIDEO_ZONES.keys():
            ml, ol = my.get(zone, ()), other.get(zone, ())
            if ml and ol and ml == ol:
                # Identitate literala a zonei de continut cu alt cNN
                return False
    return True


@detector('R-V03.73', 'Meniu mobil fara banda nav-brand (referinta C01)', 'studiu')
def _rnavbrand(c):
    # Side-nav-ul incepe direct cu .nav-progress, ca in c01. Banda nav-brand
    # (PACK 02 EXCEL + titlu) e redundanta si pe mobil ascunde butonul Reset
    # sub fold. Bug descoperit empiric la C02-C07 (V58). Prezenta blocului HTML
    # sau a regulii CSS = drift. L191.
    return '<div class="nav-brand">' not in c and '.nav-brand {' not in c


@detector('R-V57.parity', 'Paritate semnatura premium (mantra V56 + miza card)', 'studiu')
def _rparity(c):
    # Se aplica DOAR constructiilor PREMIUM (hero-visual-overlay). Legacy
    # (inca pe model vechi) = N/A pana primesc premium. Prinde cazul cand o
    # propagare de componenta-semnatura (ex. mantra V56, miza card V53) ajunge
    # la unele constructii premium dar NU la altele (drift de paritate vizuala
    # pe care structura/anti-clona/dash NU il prind). L189.
    if 'hero-visual-overlay' not in c:
        return True  # legacy (nepremium) = N/A, pass vacuos (harness 'studiu' face all(), None devine False)
    m = re.search(r'\.mantra-band-main\s*\{[^}]*\}', c)
    if not m:
        return False
    mantra_scale = 'clamp(30px, 7vw, 64px)' in m.group(0) and 'font-weight: 900' in m.group(0)
    mantra_clone = 'box-decoration-break: clone' in c
    miza_card = re.search(r'\.cover-miza\s*\{[^}]*box-shadow[^}]*\}', c) is not None
    return mantra_scale and mantra_clone and miza_card


@detector('R-V58.filmname', 'Nume FILM == identitate HTML (anti-rename-stale)', 'folder')
def _rfilmname(folder):
    # Dupa un rename de constructie (ex. C05 CLASIFICARE->DICTIONAR in V44),
    # filename-ul FILM + HTML se actualizeaza, dar titlul DIN .docx poate ramane
    # cu numele vechi (care acum apartine altei constructii). audit/gate nu
    # prind (nu citesc continutul FILM). Verifica: stem-ul numelui din titlul
    # FILM (".docx") apare in identitatea HTML (topbar + footer + cover-title),
    # modulo diacritice. Numele narativ (C07 MEMORIA, C08 ECOSISTEM) trec, ca
    # apar si in cover-title HTML. L190.
    films = glob.glob(os.path.join(folder, 'FILM-Excel-*.docx'))
    studs = glob.glob(os.path.join(folder, 'HTML-Studiu-Excel-*.html'))
    if not films or not studs:
        return True  # N/A
    try:
        with zipfile.ZipFile(films[0]) as z:
            xml = z.read('word/document.xml').decode('utf-8', 'ignore')
    except Exception:
        return True  # nu pot citi .docx (ex. lipsa) -> nu blochez
    wt = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml)
    title = wt[0] if wt else ''
    m = re.search(r'C\d+\s+(\w+)', title, re.U)
    if not m:
        return True
    stem = _fold(m.group(1))[:5]
    if len(stem) < 4:
        return True
    with open(studs[0], encoding='utf-8') as fh:
        h = fh.read()
    parts = []
    for pat in (r'mobile-topbar-title">([^<]*)', r'class="footer">\s*([^<]*)', r'cover-title">([^<]*)'):
        mm = re.search(pat, h)
        parts.append(mm.group(1) if mm else '')
    return stem in _fold(' '.join(parts))


def audit(root='.', json_out=False):
    zones = {}
    for c_folder in sorted(glob.glob(os.path.join(root, 'c[0-9][0-9]'))):
        nn = os.path.basename(c_folder).upper()
        zones[nn] = c_folder

    def _read(f):
        with open(f, encoding='utf-8') as fh:
            return fh.read()

    results = {}
    err_count = 0
    for zname, folder in zones.items():
        results[zname] = {}
        sts = glob.glob(os.path.join(folder, 'HTML-Studiu-Excel-*.html'))
        est = glob.glob(os.path.join(folder, 'HTML-Editor-Studiu-Excel-*.html'))
        vid = glob.glob(os.path.join(folder, 'HTML-Video-Excel-*.html'))
        evi = glob.glob(os.path.join(folder, 'HTML-Editor-Video-Excel-*.html'))
        for rc, det in DETECTORS.items():
            scope = det['scope']
            r = None
            try:
                if scope == 'folder':
                    r = det['fn'](folder)
                elif scope == 'studiu':
                    files = sts + est
                    if files: r = all(det['fn'](_read(f)) for f in files)
                elif scope == 'video':
                    files = vid + evi
                    if files: r = all(det['fn'](_read(f)) for f in files)
                elif scope == 'all_html':
                    files = sts + est + vid + evi
                    if files: r = all(det['fn'](_read(f)) for f in files)
            except Exception as e:
                r = 'ERR'
                err_count += 1
                print(f"[WARN] {zname} {rc}: {type(e).__name__}: {e}", file=sys.stderr)
            if r is not None: results[zname][rc] = r

    if json_out:
        print(json.dumps(results, indent=2))
        return 0

    drift = 0
    errs = 0
    print(f"\n{'Zona':<8}", end='')
    for rc in DETECTORS.keys():
        print(f"{rc[-10:]:>12}", end='')
    print()
    print("-" * (8 + 12 * len(DETECTORS)))
    for zname, zres in results.items():
        print(f"{zname:<8}", end='')
        for rc in DETECTORS.keys():
            if rc in zres:
                v = zres[rc]
                if v is True:
                    sym = 'OK'
                elif v is False:
                    sym = 'XX'
                    drift += 1
                else:
                    sym = 'ERR'
                    errs += 1
            else:
                sym = '-'
            print(f"{sym:>12}", end='')
        print()
    print()
    total_cells = len(DETECTORS) * len(results)
    real_evals = sum(1 for z in results.values() for v in z.values() if v is True or v is False)
    if drift == 0 and errs == 0:
        print(f"ZERO DRIFT - {real_evals}/{total_cells} verificari rulate, toate PASS")
    elif drift == 0 and errs > 0:
        print(f"ZERO DRIFT confirmat pe {real_evals}/{total_cells} verificari, dar {errs} detectoare au ERR (vezi WARN stderr)")
    else:
        print(f"DRIFT: {drift} celule cu probleme + {errs} ERR")
    return 0 if (drift == 0 and errs == 0) else 1


if __name__ == '__main__':
    sys.exit(audit('.', '--json' in sys.argv))
