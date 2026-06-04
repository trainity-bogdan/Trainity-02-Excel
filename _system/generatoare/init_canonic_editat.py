#!/usr/bin/env python3
"""
init_canonic_editat.py - V36 (R-V03.62)

Promoveaza structura plata `livrabile_C{NN}/` la structura V36+ cu
doua stari distincte:

ÎNAINTE:
livrabile_C02/
├── HTML-Studiu-...
├── HTML-Editor-Studiu-...
├── HTML-Video-...
├── HTML-Editor-Video-...
├── Date_MASTER-C02.xlsx
├── FILM-... (optional)
└── assets/ (optional)

DUPĂ:
livrabile_C02/
├── canonic/              # snapshot inghetat (V01 = prima generare)
│   └── [toate fisierele de mai sus + meta marker snapshot=canonic-V01]
└── editat/               # versiunea evolutiva (start identic cu canonic)
    └── [aceleasi fisiere + meta marker snapshot=editat]

Idempotent: skip silentios daca structura deja exista (detecteaza
prin prezenta folder canonic/).

Usage:
    python3 init_canonic_editat.py livrabile_C02
"""

import os
import sys
import shutil
import re


def has_meta_marker(content, name, value):
    """Verifica daca HTML-ul are deja meta marker-ul respectiv."""
    pattern = re.compile(
        rf'<meta\s+name=["\']?{re.escape(name)}["\']?\s+content=["\']?{re.escape(value)}["\']?',
        re.IGNORECASE
    )
    return bool(pattern.search(content))


def add_meta_marker(html_path, marker_value):
    """Adauga <meta name="trainity-snapshot" content="..."> in head."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if has_meta_marker(html, 'trainity-snapshot', marker_value):
        return False  # deja exista
    
    # Cauta </head> si insereaza inainte
    head_close = html.find('</head>')
    if head_close < 0:
        return False
    
    marker = f'  <meta name="trainity-snapshot" content="{marker_value}">\n'
    new_html = html[:head_close] + marker + html[head_close:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    return True


def migrate(livrabile_dir):
    """Migreaza un folder livrabile_C{NN}/ la structura canonic/+editat/."""
    if not os.path.isdir(livrabile_dir):
        print(f"EROARE: {livrabile_dir} nu exista", file=sys.stderr)
        return 1
    
    canonic_dir = os.path.join(livrabile_dir, 'canonic')
    editat_dir = os.path.join(livrabile_dir, 'editat')
    
    # Idempotent check
    if os.path.isdir(canonic_dir) and os.path.isdir(editat_dir):
        print(f"  SKIP: {livrabile_dir} are deja structura canonic/editat")
        return 0
    
    # Identific fisierele de migrat (la nivelul radacina al livrabile_C{NN}/)
    items_to_move = []
    for item in os.listdir(livrabile_dir):
        item_path = os.path.join(livrabile_dir, item)
        # Skip foldere existente canonic/editat
        if item in ('canonic', 'editat'):
            continue
        items_to_move.append(item)
    
    if not items_to_move:
        print(f"  EROARE: {livrabile_dir} este gol")
        return 2
    
    # Creez canonic/ si editat/
    os.makedirs(canonic_dir, exist_ok=True)
    os.makedirs(editat_dir, exist_ok=True)
    
    # MUT fisierele in canonic/ + COPIEZ in editat/
    for item in items_to_move:
        src = os.path.join(livrabile_dir, item)
        canonic_dst = os.path.join(canonic_dir, item)
        editat_dst = os.path.join(editat_dir, item)
        
        # Mut in canonic
        shutil.move(src, canonic_dst)
        
        # Copiez in editat (deep pentru foldere)
        if os.path.isdir(canonic_dst):
            shutil.copytree(canonic_dst, editat_dst)
        else:
            shutil.copy2(canonic_dst, editat_dst)
    
    # Adaug meta marker in HTML-uri
    n_canonic = 0
    n_editat = 0
    for fname in os.listdir(canonic_dir):
        if fname.endswith('.html'):
            if add_meta_marker(os.path.join(canonic_dir, fname), 'canonic-V01'):
                n_canonic += 1
    for fname in os.listdir(editat_dir):
        if fname.endswith('.html'):
            if add_meta_marker(os.path.join(editat_dir, fname), 'editat'):
                n_editat += 1
    
    print(f"  OK: {livrabile_dir} migrat -> canonic/ ({n_canonic} HTML markat) + editat/ ({n_editat} HTML markat)")
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    for livrabile_dir in sys.argv[1:]:
        migrate(livrabile_dir)


if __name__ == '__main__':
    main()
