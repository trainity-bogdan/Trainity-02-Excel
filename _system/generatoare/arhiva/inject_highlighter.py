#!/usr/bin/env python3
"""
inject_highlighter.py - V34

Injecteaza feature-ul Highlighter Persistent (R-V03.59) intr-un
HTML-Video existent.

V34: detecteaza versiunea instalata anterior si re-injecteaza.
- Daca exista versiune mai veche (V31 cu buton Reset + ESC), o elimina
  si pune V34 (fara buton, fara ESC, capture phase pentru preven advance).
- Idempotent: daca V34 deja injectat, skip.
"""

import sys
import os
import re


def inject(html_path, output_path=None, snippet_dir=None):
    if not os.path.exists(html_path):
        print(f"EROARE: {html_path} nu exista", file=sys.stderr)
        return 1

    if snippet_dir is None:
        candidates = [
            'referinte',
            '../referinte',
            os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'referinte'),
        ]
        for cand in candidates:
            if os.path.exists(os.path.join(cand, 'highlighter-snippet.css')):
                snippet_dir = cand
                break

    if not snippet_dir or not os.path.exists(os.path.join(snippet_dir, 'highlighter-snippet.css')):
        print(f"EROARE: nu gasesc snippet-uri in referinte/", file=sys.stderr)
        return 2

    css_path = os.path.join(snippet_dir, 'highlighter-snippet.css')
    js_path = os.path.join(snippet_dir, 'highlighter-snippet.js')

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # V34: detect versiune existenta. Daca e V34, skip. Daca e mai veche, elimin + reinject.
    existing_marker = re.search(r"content:\s*'(v\d+)'", html) or re.search(r"content=\"(v\d+)\"", html)
    is_v34 = False
    if existing_marker:
        ver = existing_marker.group(1)
        if ver == 'v34':
            print(f"  SKIP: {html_path} are deja V34")
            return 0
        else:
            print(f"  UPGRADE: {html_path} are {ver}, eliminam si reinjectam V34")
            # Elimin CSS vechi
            html = re.sub(
                r'\n\n/\* === HIGHLIGHTER R-V03\.59[^*]*\*/\n.*?(?=\n</style>|\n\n/\*|\n<)',
                '',
                html, count=1, flags=re.DOTALL
            )
            # Elimin block JS vechi
            html = re.sub(
                r'\n<script>\n/\* HIGHLIGHTER R-V03\.59[^*]*\*/.*?</script>\n',
                '',
                html, count=1, flags=re.DOTALL
            )
    elif 'trainity-highlighter-v1' in html or 'trainity-highlight' in html:
        # Versiune foarte veche sau marker fara content - elimin via cleanup global
        # Caut CSS vechi
        html = re.sub(
            r'\n\n/\* === HIGHLIGHTER R-V03\.59[^*]*?\*/\s*\n.*?(?=\n\n/\*|\n</style>)',
            '',
            html, flags=re.DOTALL
        )
        # Caut JS vechi (V31 cu buton)
        html = re.sub(
            r'\n<script>\s*\n/\* HIGHLIGHTER R-V03\.59[^*]*?\*/.*?</script>\n',
            '',
            html, flags=re.DOTALL
        )
        # Elimin orice meta marker ramas
        html = re.sub(r'<meta id="trainity-highlighter-v1"[^>]*>\s*', '', html)
        # Sterg orice <button class="hl-reset">...</button>
        html = re.sub(r'<button class="hl-reset"[^>]*>.*?</button>', '', html, flags=re.DOTALL)
        print(f"  UPGRADE: {html_path} avea highlighter vechi (fara marker version), reinjectam V34")
    
    # Re-verific dupa cleanup ca sa nu fie deja V34
    if 'trainity-highlighter-v1' in html and 'capture' in html.lower():
        # E deja V34 sau confuz - skip
        print(f"  SKIP: {html_path} pare deja V34 dupa cleanup")
        return 0

    with open(css_path, 'r', encoding='utf-8') as f: css = f.read()
    with open(js_path, 'r', encoding='utf-8') as f: js = f.read()

    # Inject CSS
    inject_css = f'\n\n/* === HIGHLIGHTER R-V03.59 (V34+) === */\n{css}\n'
    last_style = html.rfind('</style>')
    if last_style > 0:
        html = html[:last_style] + inject_css + html[last_style:]
    else:
        head_end = html.find('</head>')
        if head_end > 0:
            html = html[:head_end] + f'<style>{inject_css}</style>\n' + html[head_end:]
        else:
            return 3

    # Inject JS
    inject_js = f'\n<script>\n/* HIGHLIGHTER R-V03.59 (V34+) */\n{js}\n</script>\n'
    last_body = html.rfind('</body>')
    if last_body > 0:
        html = html[:last_body] + inject_js + html[last_body:]
    else:
        html += inject_js

    out = output_path if output_path else html_path
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  OK: highlighter V34 injectat in {out}")
    return 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 inject_highlighter.py <html_path> [-o <output>]")
        sys.exit(1)
    html_path = sys.argv[1]
    output_path = None
    if '-o' in sys.argv:
        idx = sys.argv.index('-o')
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]
    sys.exit(inject(html_path, output_path))


if __name__ == '__main__':
    main()
