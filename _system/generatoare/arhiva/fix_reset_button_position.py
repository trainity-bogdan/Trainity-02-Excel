#!/usr/bin/env python3
"""
fix_reset_button_position.py - V33 (R-V03.61)

Elimina margin-top: auto din .nav-controls in HTML-Studiu si
HTML-Editor-Studiu, ca butonul RESETEAZA PROGRES sa fie lipit
imediat dupa meniu pe orice viewport (responsive corectat).

Bug observat: pe tableta landscape (~1600x1000), side-nav are
height fix calc(100vh - 110px), continut nu umple, margin-top:
auto impingea butonul la baza, lasand gap ~315px intre meniu
si buton. Pe desktop normal nu se observa pentru ca continutul
umple inaltimea.

Fix: eliminam margin-top: auto din .nav-controls. Butonul ramane
imediat dupa nav-finals (verificarile finale 1-8). Compact pe
toate rezolutiile.

Idempotent.
"""

import sys
import os
import re


def patch(html_path):
    if not os.path.exists(html_path):
        print(f"EROARE: {html_path} nu exista", file=sys.stderr)
        return 1
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Pattern: .nav-controls { ... margin-top: auto; ... }
    # Inlocuiesc doar in regula CSS .nav-controls (nu in alte locuri)
    pattern = re.compile(
        r'(\.nav-controls\s*\{[^}]*?)(margin-top:\s*auto;\s*)([^}]*\})',
        re.DOTALL
    )
    
    new_html, n = pattern.subn(r'\1\3', html)
    
    if n == 0:
        print(f"  SKIP: {html_path} - margin-top: auto nu mai exista in .nav-controls")
        return 0
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"  OK: {html_path} - eliminat margin-top: auto ({n} ocurente)")
    return 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_reset_button_position.py <html_path>")
        sys.exit(1)
    sys.exit(patch(sys.argv[1]))


if __name__ == '__main__':
    main()
