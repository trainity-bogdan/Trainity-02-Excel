#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
detect_c06_purity.py - detector de puritate CLASIFICARE pentru C06 (T2).

Acopera gaurile gasite la MEGA AUDIT C06 pe care audit_sync/gate nu le prind:
  D1. refresh / flux permanent in corpul C06 (contaminare C04/T5)
  D2. scor min-max (rescalare numerica = cuantificare C07, nu clasificare)
  D3. em/en-dash in xlsx (audit_sync scaneaza doar HTML)
  D4. XLOOKUP prezent (cele 3 functii-semnatura 06-MAP: IFS/SWITCH/XLOOKUP)
  D5. (RETRAS V68 - Creativ abandonat: prompturile nu se mai stocheaza)
  D6. cuvinte INTERZIS T3 in C06 (prioritar/strategic/critic/valoros)
  D7. imagini exec-stage clone byte-identice C01 (R-V59)

Uz:  python3 detect_c06_purity.py [dir_constructie] [dir_pilot_c01]
     default: c06 c01
Stdlib only (zipfile/hashlib/re). openpyxl NU e necesar (citeste XML brut).
"""
import sys, os, re, zipfile, hashlib, glob

NN_DIR = sys.argv[1] if len(sys.argv) > 1 else 'c06'
PILOT = sys.argv[2] if len(sys.argv) > 2 else 'c01'

results = []  # (check, status, detail)


def add(check, ok, detail=''):
    results.append((check, 'PASS' if ok else 'FAIL', detail))


def strip_noise(t):
    t = re.sub(r'data:image[^"\')]+', '', t)
    t = re.sub(r'<style[^>]*>.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.S)
    return t


html_files = sorted(glob.glob(f'{NN_DIR}/HTML-*.html'))
xlsx = glob.glob(f'{NN_DIR}/Date_MASTER-*.xlsx')


def read(f):
    return open(f, encoding='utf-8', errors='ignore').read()


# --- D1. refresh / flux permanent in corpul HTML (body text + steps JS) ---
# whitelist: refreshActionBtn (functie JS), 'hard refresh' (comentariu cache-bust editor)
d1bad = []
for f in html_files:
    t = read(f)
    t = re.sub(r'data:image[^"\')]+', '', t)
    for m in re.finditer(r'(?i)\brefresh\b', t):
        ctx = t[max(0, m.start() - 25):m.end() + 18]
        if 'refreshActionBtn' in ctx or 'hard refresh' in ctx.lower() or 'cache-bust' in ctx.lower():
            continue
        d1bad.append((os.path.basename(f), re.sub(r'\s+', ' ', ctx).strip()))
add('D1 refresh/flux in corp HTML', not d1bad, '; '.join(f"{a}:{b}" for a, b in d1bad[:4]))

# --- D2. scor min-max (rescalare numerica) ---
# whitelist: .normalize() = DOM JS, nu normalizare de date
d2bad = []
pat = re.compile(r'MAX\([^)]*\)\s*[-=].*?MIN\(|/\s*\(\s*MAX\(|\bnormaliz(?!e\(\))', re.I)
for f in html_files:
    t = read(f)
    t = re.sub(r'\.normalize\(\)', '', t)
    if pat.search(t):
        d2bad.append(os.path.basename(f))
add('D2 scor min-max / normalizare', not d2bad, ', '.join(d2bad))

# --- D3. em/en-dash in xlsx ---
d3 = 0
for xl in xlsx:
    z = zipfile.ZipFile(xl)
    for n in z.namelist():
        if n.endswith('.xml'):
            d = z.read(n).decode('utf-8', errors='ignore')
            d3 += d.count('—') + d.count('–') + d.count('&#8212;') + d.count('&#8211;')
add('D3 em/en-dash in xlsx', d3 == 0, f"{d3} aparitii")

# --- D4. XLOOKUP + IFS + SWITCH prezente in Studiu ---
studiu = [f for f in html_files if 'Studiu' in f and 'Editor' not in f]
d4 = {}
if studiu:
    t = strip_noise(read(studiu[0]))
    for fn in ('IFS', 'SWITCH', 'XLOOKUP'):
        d4[fn] = len(re.findall(fn, t))
missing = [k for k, v in d4.items() if v == 0]
add('D4 functii-semnatura IFS/SWITCH/XLOOKUP', not missing,
    f"prezente={d4}" if not missing else f"LIPSA={missing} ({d4})")

# --- D5. RETRAS V68 (Creativ abandonat: prompturile nu se mai stocheaza) ---

# --- D6. cuvinte INTERZIS T3 (06-MAP anti-redrift) ---
t3words = ['prioritar', 'prioritate', 'strategic', 'critic', 'valoros', 'irelevant']
d6bad = []
for f in html_files + xlsx:
    if f.endswith('.xlsx'):
        z = zipfile.ZipFile(f)
        t = ' '.join(z.read(n).decode('utf-8', errors='ignore')
                     for n in z.namelist() if n.endswith('.xml'))
    else:
        t = strip_noise(read(f))
    for w in t3words:
        if re.search(r'(?i)\b' + re.escape(w), t):
            d6bad.append(f"{os.path.basename(f)}:{w}")
add('D6 fara limbaj T3 (prioritar/strategic/critic)', not d6bad, '; '.join(d6bad[:5]))

# --- D7. imagini exec-stage clone C01 (R-V59) ---
def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()
clones = []
for n in range(1, 7):
    a = f'{NN_DIR}/assets/exec-stage-{n}.jpg'
    b = f'{PILOT}/assets/exec-stage-{n}.jpg'
    if os.path.exists(a) and os.path.exists(b) and md5(a) == md5(b):
        clones.append(n)
add('D7 exec-stage NU sunt clone C01 (R-V59)', not clones,
    f"CLONE stage {clones} (PENDING BANANA)" if clones else 'toate unice')

# --- raport ---
print('=' * 70)
print(f'DETECT C06 PURITY - {NN_DIR} (pilot {PILOT})')
print('=' * 70)
fails = 0
for check, status, detail in results:
    mark = 'OK ' if status == 'PASS' else 'XX '
    print(f'  {mark} {check:48} {status}' + (f'  [{detail}]' if detail else ''))
    if status == 'FAIL':
        fails += 1
print('-' * 70)
print(f'{"PASS" if fails == 0 else "FAIL"}: {len(results)-fails}/{len(results)} checks OK, {fails} FAIL')
sys.exit(1 if fails else 0)
