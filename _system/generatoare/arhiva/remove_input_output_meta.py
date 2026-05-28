#!/usr/bin/env python3
"""
remove_input_output_meta.py - V32 (R-V03.60)

Elimina cele doua randuri INPUT + OUTPUT din `<div class="cover-meta">`
in HTML-Studiu si HTML-Editor-Studiu.

Motivatie: schema livrabile R-V03.47/R-V03.49 foloseste un singur fisier
Date_MASTER-CNN.xlsx (NU Date-Input + Date-Output separate). Cele doua
randuri INPUT/OUTPUT din cover-meta erau reziduuri din schema veche si
nu mai sunt de actualitate.

Idempotent: re-run pe acelasi fisier nu face nimic (anti-duble-patch).

Usage:
    python3 remove_input_output_meta.py path/to/HTML-Studiu-Excel-NN.html
    python3 remove_input_output_meta.py path/to/HTML-Studiu-Excel-NN.html -o out.html
"""

import sys
import os
import re


def patch(html_path, output_path=None):
    if not os.path.exists(html_path):
        print(f"EROARE: {html_path} nu exista", file=sys.stderr)
        return 1
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original_len = len(html)
    
    # Pattern: <div class="cover-meta-row">\s*<span class="cover-meta-key">INPUT</span>...</div>
    # Elimina rand INPUT
    pattern_input = re.compile(
        r'\s*<div class="cover-meta-row">\s*'
        r'<span class="cover-meta-key">INPUT</span>\s*'
        r'<span class="cover-meta-val">.*?</span>\s*'
        r'</div>',
        re.DOTALL
    )
    new_html, n_input = pattern_input.subn('', html)
    
    # Elimina rand OUTPUT
    pattern_output = re.compile(
        r'\s*<div class="cover-meta-row">\s*'
        r'<span class="cover-meta-key">OUTPUT</span>\s*'
        r'<span class="cover-meta-val">.*?</span>\s*'
        r'</div>',
        re.DOTALL
    )
    new_html, n_output = pattern_output.subn('', new_html)
    
    if n_input == 0 and n_output == 0:
        print(f"  SKIP: {html_path} nu are randuri INPUT/OUTPUT in cover-meta")
        return 0
    
    out = output_path if output_path else html_path
    with open(out, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    delta = len(new_html) - original_len
    print(f"  OK: {out} - eliminat INPUT={n_input} OUTPUT={n_output} (delta {delta} bytes)")
    return 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 remove_input_output_meta.py <html_path> [-o <output>]")
        sys.exit(1)
    
    html_path = sys.argv[1]
    output_path = None
    if '-o' in sys.argv:
        idx = sys.argv.index('-o')
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]
    
    sys.exit(patch(html_path, output_path))


if __name__ == '__main__':
    main()
