from pathlib import Path

REGISTRY = Path('_system/arhiva/SISTEM_TRAINITY-versiuni.md')
BRAIN_SPEC = Path('_brain/c10/BRAIN-TO-CLAUDE.md')

OLD_LINE = '## SPEC C10 - ANALIZA PIVOT   [Status: NEGENERAT]'
NEW_HEADER = '## SPEC C10 - MĂSURI   [Status: FROZEN]'
NEXT_LINE = '## SPEC C11 - DATA MODEL   [Status: NEGENERAT]'


def main() -> None:
    if not REGISTRY.exists():
        raise SystemExit(f'ERROR: missing registry: {REGISTRY}')
    if not BRAIN_SPEC.exists():
        raise SystemExit(f'ERROR: missing brain spec: {BRAIN_SPEC}')

    registry_text = REGISTRY.read_text(encoding='utf-8')
    brain_text = BRAIN_SPEC.read_text(encoding='utf-8')

    line_count_before = registry_text.count('\n') + 1
    if line_count_before < 5000:
        raise SystemExit(f'ERROR: registry too short before patch: {line_count_before} lines')

    required_markers = [
        'PARTEA VI - SPEC INGHETAT CONSTRUCTII',
        '## SPEC C01',
        '## SPEC C08',
        OLD_LINE,
        NEXT_LINE,
    ]
    for marker in required_markers:
        if marker not in registry_text:
            raise SystemExit(f'ERROR: required marker missing before patch: {marker}')

    if NEW_HEADER in registry_text:
        print('OK: C10 already frozen. No change needed.')
        return

    start_marker = '# SPEC C10 FINAL ÎNGHEȚAT'
    if start_marker not in brain_text:
        raise SystemExit('ERROR: final C10 brain spec marker missing')

    spec = brain_text.split(start_marker, 1)[1].strip()
    spec = spec.replace('## 1. SLUG', '### 1. SLUG')
    spec = spec.replace('## 2. INTRIGA', '### 2. INTRIGA')
    spec = spec.replace('## 3. PROBLEMELE', '### 3. PROBLEMELE')
    spec = spec.replace('## 4. MIZA', '### 4. MIZA')
    spec = spec.replace('## 5. MANTRA', '### 5. MANTRA')
    spec = spec.replace('## 6. WOW', '### 6. WOW')
    spec = spec.replace('## 7. MOTTO', '### 7. MOTTO')
    spec = spec.replace('## 8. FENOMENE C10', '### 8. FENOMENE C10')
    spec = spec.replace('## 9. STEP-TITLES FINALE', '### 9. STEP-TITLES FINALE')
    spec = spec.replace('## AHA C10', '### AHA C10')
    spec = spec.replace('## Schimbare mentală urmărită', '### Schimbare mentală urmărită')
    spec = spec.replace('## Formula finală C10', '### Formula finală C10')
    spec = spec.strip().strip('-').strip()

    replacement = NEW_HEADER + '\n\n' + spec
    new_text = registry_text.replace(OLD_LINE, replacement, 1)

    if new_text == registry_text:
        raise SystemExit('ERROR: patch produced no change')
    if new_text.count(NEW_HEADER) != 1:
        raise SystemExit('ERROR: C10 frozen header count invalid')
    if OLD_LINE in new_text:
        raise SystemExit('ERROR: old C10 placeholder still present')
    if NEXT_LINE not in new_text:
        raise SystemExit('ERROR: C11 marker missing after patch')

    line_count_after = new_text.count('\n') + 1
    if line_count_after < 5000:
        raise SystemExit(f'ERROR: registry too short after patch: {line_count_after} lines')

    REGISTRY.write_text(new_text, encoding='utf-8')
    print(f'OK: C10 frozen safely. Lines before={line_count_before}, after={line_count_after}')


if __name__ == '__main__':
    main()
