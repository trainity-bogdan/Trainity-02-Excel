#!/usr/bin/env python3
"""
patch_runner.py - V38 (R-V03.64)

Motor unificat pentru aplicare patch-uri sistem din rețete YAML.

Substitue scripturile individuale:
- inject_highlighter.py
- fix_reset_button_position.py
- remove_input_output_meta.py
- etc.

Pattern: o singură rețetă YAML definește patch-ul.
Rețetele trăiesc în _system/patch_recipes/.

Usage:
    python3 patch_runner.py reteta.yaml
    python3 patch_runner.py reteta.yaml --dry-run        # arată ce ar face fără să aplice
    python3 patch_runner.py reteta.yaml --target-canonic  # aplică și pe canonic
    python3 patch_runner.py --list-recipes               # listă rețete disponibile
"""

import sys
import os
import re
import glob
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("EROARE: lipsește PyYAML. Instalează: pip install pyyaml")
    sys.exit(1)


# ─── OPERATII DISPONIBILE ──────────────────────────────────


def op_regex_replace(content, pattern, replacement, count=0, **kwargs):
    """Substituție regex. count=0 = toate aparițiile."""
    new_content, n = re.subn(pattern, replacement, content, count=count, flags=re.MULTILINE | re.DOTALL)
    return new_content, n > 0


def op_insert_dupa_marker(content, marker, continut, daca_lipseste=True, **kwargs):
    """Inserează conținut după un marker, dacă nu există deja."""
    if daca_lipseste and continut.strip() in content:
        return content, False
    idx = content.find(marker)
    if idx < 0:
        return content, False
    insert_at = idx + len(marker)
    new_content = content[:insert_at] + '\n' + continut + content[insert_at:]
    return new_content, True


def op_insert_inainte_marker(content, marker, continut, daca_lipseste=True, **kwargs):
    """Inserează conținut înainte de un marker."""
    if daca_lipseste and continut.strip() in content:
        return content, False
    idx = content.find(marker)
    if idx < 0:
        return content, False
    new_content = content[:idx] + continut + '\n' + content[idx:]
    return new_content, True


def op_inlocuieste_bloc(content, start_marker, end_marker, continut_nou, **kwargs):
    """Înlocuiește tot conținutul între două markere."""
    start_idx = content.find(start_marker)
    if start_idx < 0:
        return content, False
    end_idx = content.find(end_marker, start_idx + len(start_marker))
    if end_idx < 0:
        return content, False
    new_content = content[:start_idx + len(start_marker)] + '\n' + continut_nou + '\n' + content[end_idx:]
    return new_content, True


def op_sterge_linii(content, pattern, **kwargs):
    """Șterge linii care match pattern."""
    lines = content.split('\n')
    new_lines = [l for l in lines if not re.search(pattern, l)]
    if len(new_lines) == len(lines):
        return content, False
    return '\n'.join(new_lines), True


def op_adauga_meta_marker(content, marker_name, marker_value, **kwargs):
    """Adaugă <meta name="X" content="Y"> în head HTML."""
    pattern = rf'<meta\s+name=["\']?{re.escape(marker_name)}["\']?\s+content=["\']?{re.escape(marker_value)}'
    if re.search(pattern, content):
        return content, False
    head_close = content.find('</head>')
    if head_close < 0:
        return content, False
    marker_html = f'  <meta name="{marker_name}" content="{marker_value}">\n'
    new_content = content[:head_close] + marker_html + content[head_close:]
    return new_content, True


OPERATII = {
    'regex_replace': op_regex_replace,
    'insert_dupa_marker': op_insert_dupa_marker,
    'insert_inainte_marker': op_insert_inainte_marker,
    'inlocuieste_bloc': op_inlocuieste_bloc,
    'sterge_linii': op_sterge_linii,
    'adauga_meta_marker': op_adauga_meta_marker,
}


# ─── EXECUTIE PATCH ────────────────────────────────────────


def aplica_patch(reteta_path, target_canonic=False, dry_run=False, verbose=True):
    """Aplică un patch dintr-o rețetă YAML."""
    with open(reteta_path, encoding='utf-8') as f:
        reteta = yaml.safe_load(f)
    
    regula = reteta.get('regula', 'UNKNOWN')
    nume = reteta.get('nume', 'Patch fără nume')
    target_files_globs = reteta.get('target_files', [])
    target_canonic_default = reteta.get('target_canonic', False)
    operatii = reteta.get('operatii', [])
    
    apply_to_canonic = target_canonic or target_canonic_default
    
    if verbose:
        print(f"\n{'='*70}")
        print(f"PATCH: {regula} - {nume}")
        print(f"{'='*70}")
        print(f"Mode: {'DRY-RUN' if dry_run else 'APLICARE'}")
        print(f"Target canonic: {apply_to_canonic}")
        print()
    
    # Expandez glob-urile
    all_files = set()
    for pattern in target_files_globs:
        # Dacă target_canonic e False, exclud canonic/ din glob
        if not apply_to_canonic and 'canonic' in pattern:
            continue
        for f in glob.glob(pattern, recursive=True):
            # Verifică din nou: dacă fișierul e în canonic/ și target_canonic e False, skip
            if not apply_to_canonic and '/canonic/' in f:
                continue
            all_files.add(f)
    
    if not all_files:
        print(f"  AVERTISMENT: niciun fișier match pe pattern-uri")
        return 0, 0
    
    if verbose:
        print(f"Fișiere target ({len(all_files)}):")
        for f in sorted(all_files):
            print(f"  - {f}")
        print()
    
    # Aplic operațiile per fișier
    modificate = 0
    neschimbate = 0
    
    for fpath in sorted(all_files):
        with open(fpath, encoding='utf-8') as f:
            content_original = f.read()
        
        content = content_original
        modificat_in_acest_fisier = False
        
        for op in operatii:
            op_tip = op.get('tip')
            if op_tip not in OPERATII:
                print(f"  EROARE: operație necunoscută '{op_tip}'")
                continue
            
            op_fn = OPERATII[op_tip]
            op_params = {k: v for k, v in op.items() if k != 'tip'}
            
            try:
                content, did_change = op_fn(content, **op_params)
                if did_change:
                    modificat_in_acest_fisier = True
                    if verbose:
                        print(f"    {fpath}: aplicat '{op_tip}'")
            except Exception as e:
                print(f"    {fpath}: EROARE la '{op_tip}': {e}")
        
        if modificat_in_acest_fisier:
            if not dry_run:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
            modificate += 1
        else:
            neschimbate += 1
    
    if verbose:
        print()
        print(f"REZULTAT: {modificate} fișiere modificate, {neschimbate} neschimbate (idempotent)")
        if dry_run:
            print("(DRY-RUN: nimic scris pe disc)")
        print()
    
    return modificate, neschimbate


def listeaza_retete():
    """Listă rețete disponibile."""
    base = Path(__file__).parent.parent / 'patch_recipes'
    if not base.exists():
        print(f"Folder rețete nu există: {base}")
        return
    
    print(f"\n{'='*70}")
    print(f"REȚETE DISPONIBILE în {base}")
    print(f"{'='*70}")
    
    retete = sorted(base.glob('*.yaml'))
    if not retete:
        print("  (niciuna)")
        return
    
    for r in retete:
        try:
            with open(r, encoding='utf-8') as f:
                data = yaml.safe_load(f)
            print(f"  {r.name}")
            print(f"    Regula: {data.get('regula', '?')}")
            print(f"    Nume: {data.get('nume', '?')}")
            print(f"    Status: {data.get('status', 'ACTIVĂ')}")
            print()
        except Exception as e:
            print(f"  {r.name} - EROARE citire: {e}")


def main():
    parser = argparse.ArgumentParser(description='Patch runner Trainity V38')
    parser.add_argument('reteta', nargs='?', help='Cale către rețetă YAML')
    parser.add_argument('--dry-run', action='store_true', help='Arată ce ar face fără să aplice')
    parser.add_argument('--target-canonic', action='store_true', help='Aplică și pe canonic/')
    parser.add_argument('--list-recipes', action='store_true', help='Listă rețete disponibile')
    parser.add_argument('--quiet', action='store_true', help='Output minim')
    
    args = parser.parse_args()
    
    if args.list_recipes:
        listeaza_retete()
        return
    
    if not args.reteta:
        parser.print_help()
        return
    
    reteta_path = args.reteta
    # Acceptă și numele scurt (caută în patch_recipes/)
    if not os.path.exists(reteta_path):
        candidat = Path(__file__).parent.parent / 'patch_recipes' / reteta_path
        if candidat.exists():
            reteta_path = str(candidat)
        elif not reteta_path.endswith('.yaml'):
            candidat = Path(__file__).parent.parent / 'patch_recipes' / f'{reteta_path}.yaml'
            if candidat.exists():
                reteta_path = str(candidat)
    
    if not os.path.exists(reteta_path):
        print(f"EROARE: rețetă nu există: {reteta_path}")
        sys.exit(1)
    
    aplica_patch(
        reteta_path,
        target_canonic=args.target_canonic,
        dry_run=args.dry_run,
        verbose=not args.quiet,
    )


if __name__ == '__main__':
    main()
