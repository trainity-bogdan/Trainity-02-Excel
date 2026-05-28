#!/usr/bin/env python3
"""
gen_imagini_base64.py - R-V03.33

Utility care converteste folderul assets/ (6 imagini exec-stage-*.jpg
generate Banana 2) in bloc CSS cu url("data:image/jpeg;base64,...")
inline pentru injectare in HTML-Video + HTML-Editor-Video.

Folosire in pipeline build_cNN.py (COPY-MODIFY pe build_c01_v5.py):
    from gen_imagini_base64 import build_exec_show_css
    css_block = build_exec_show_css("/path/to/assets/")
    # Apoi inject css_block in template HTML_VIDEO la sectiunea
    # ".exec-image[data-exec-img=..." (inlocuieste path-urile relative)

R-V03.33 INTERZICE path-uri relative (assets/exec-stage-N.jpg).
TOATE imaginile Executive Show traiesc embedded base64 in HTML.
Folderul assets/ nu se livreaza ca artefact separat - sursa pentru
generator doar.
"""

import base64
import os
import sys
from pathlib import Path


def build_exec_show_css(assets_dir: str, num_stages: int = 6) -> str:
    """
    Citeste imaginile exec-stage-1.jpg ... exec-stage-N.jpg din assets_dir,
    le encodeaza base64 si returneaza bloc CSS gata de inserat in <style>.

    Args:
        assets_dir: path catre folderul cu imaginile sursa
        num_stages: numar de slide-uri Executive Show (default 6)

    Returns:
        string CSS cu N reguli .exec-image[data-exec-img="exec-stage-K"]
        cu url("data:image/jpeg;base64,...") inline.
    """
    assets_path = Path(assets_dir)
    if not assets_path.is_dir():
        raise FileNotFoundError(f"Folder assets nu exista: {assets_dir}")

    lines = ["/* V12: imagini Banana 2 inline base64 (R-V03.33) */"]
    for i in range(1, num_stages + 1):
        img_path = assets_path / f"exec-stage-{i}.jpg"
        if not img_path.is_file():
            raise FileNotFoundError(f"Imagine lipsa: {img_path}")
        with open(img_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        lines.append(f'.exec-image[data-exec-img="exec-stage-{i}"] {{')
        lines.append(f'  background-image: url("data:image/jpeg;base64,{b64}");')
        lines.append("}")
    return "\n".join(lines)


def replace_in_html(html_path: str, assets_dir: str, num_stages: int = 6) -> None:
    """
    Inlocuieste in HTML existent blocul CSS cu path relativ
    `assets/exec-stage-N.jpg` cu echivalent base64 inline.

    Pattern cautat:
        /* V11.6: imagini reale generate Banana 2 - TOATE 6 GENERATE */
        .exec-image[data-exec-img="exec-stage-1"] { background-image: url("assets/exec-stage-1.jpg"); }
        ...

    Pattern inserat:
        /* V12: imagini Banana 2 inline base64 (R-V03.33) */
        .exec-image[data-exec-img="exec-stage-1"] { background-image: url("data:image/jpeg;base64,..."); }
        ...
    """
    import re

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    new_css = build_exec_show_css(assets_dir, num_stages)

    # Pattern flexibil: detecteaza varianta V11 cu path relativ
    pattern = re.compile(
        r"/\* V11\.6: imagini reale generate Banana 2[^*]*\*/\s*\n"
        + r"(?:\.exec-image\[data-exec-img=\"exec-stage-\d+\"\][^}]*\}\s*\n?)+",
        re.MULTILINE,
    )
    new_html, n = pattern.subn(new_css + "\n", html)
    if n != 1:
        raise ValueError(f"Pattern V11 nu a fost gasit (n={n}) in {html_path}")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"OK: {html_path} actualizat cu {num_stages} imagini base64 inline")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Folosire: python3 gen_imagini_base64.py <html_path> <assets_dir>")
        sys.exit(1)
    replace_in_html(sys.argv[1], sys.argv[2])
