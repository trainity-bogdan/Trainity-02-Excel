# BRAIN → CLAUDE · C11 COMPARAȚII / RANK

## STATUS
MANDAT_SYSTEM_GATE_ACTIV

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C11.

La comanda `sync`, citește:
- `_brain/c11/CHAT-CONTEXT.md`
- `_brain/c11/BRAIN-TO-CLAUDE.md`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C11
C11 este generată complet.
Raport Claude: `GENERAT · GATE PASS (logic) · ZERO DRIFT · CLEAN`.
A rămas o singură cerere SYSTEM: adăugarea identității C11 în `gate_v20.py`, ca invocarea canonică a gate-ului să funcționeze fără wrapper.

## MANDAT C11-06 · SYSTEM FIX GATE V20 IDENTITATE C11

### STATUS
MANDAT_SYSTEM_GATE_ACTIV

### OBIECTIV
Adaugă identitatea C11 în dicționarul hardcodat `IDENTITATI` din `_system/generatoare/gate_v20.py`, fără să modifici altceva.

### FIȘIER AUTORIZAT
Ai voie să modifici strict:
- `_system/generatoare/gate_v20.py`

Nu modifica:
- `CLAUDE.md`
- `README.md`
- `STARE-CURENTA.md`
- `index.html`
- alte fișiere `_system/**`
- alte construcții
- fișiere din `c11/**`, cu excepția cazului în care rulezi validări care nu modifică fișiere

### MODIFICARE CERUTĂ
În `load_identitate()`, în dicționarul `IDENTITATI`, adaugă intrarea pentru C11 între `'10'` și `'12'`:

```python
'11': {
    'cod': 'C11', 'nume_hero_caps_rand1': 'CINE',
    'nume_slug': 'Comparatii',
    'meta_val_treapta': 'RELAȚII · MĂSURI · <b>COMPARAȚII</b> · INTERPRETARE (ANALIZĂ)'
},
```

### VALIDARE CERUTĂ
După modificare:
1. Rulează invocarea canonică:
   `python3 _system/generatoare/gate_v20.py 11 c11/ c01/`
2. Confirmă PASS.
3. Rulează `audit_sync.py` dacă este permis.
4. Confirmă că C11 rămâne ZERO DRIFT.

### LIVRARE CERUTĂ
Actualizează `_brain/c11/CLAUDE-TO-BRAIN.md` cu:
- fișierul modificat
- confirmarea că intrarea C11 a fost adăugată în `gate_v20.py`
- rezultat gate canonic C11
- rezultat audit C11 / audit global, cu mențiune explicită dacă există drift pe alte construcții
- confirmarea că nu ai modificat artefactele C11

### RESTRICȚII
Nu regenera C11.
Nu modifica HTML, xlsx, docx sau assets C11.
Nu modifica alte construcții.
