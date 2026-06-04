# BRAIN → CLAUDE · C10 MĂSURI

## STATUS
AUTHORIZE_SYSTEM_FIX_FOR_C10

## CONTEXT CHAT
Acest fișier este folosit exclusiv de Chat Claude C10.

La comanda `sync`, citește:
- `_brain/c10/CHAT-CONTEXT.md`
- `_brain/c10/BRAIN-TO-CLAUDE.md`

Lucrează exclusiv pe `main`.
Nu crea branch-uri.

## STARE CURENTĂ C10
SPEC C10 este final și înghețat. Generarea C10 este începută, dar blocată la B2 deoarece `gate_v20.py` nu are încă intrarea hardcodată pentru C10.

---

# AUTORIZARE BRAIN PENTRU DEBLOCARE C10

BRAIN autorizează Claude C10 să aplice modificarea minimă necesară în fișierul de sistem cerut de propriul raport:

`_system/generatoare/gate_v20.py`

Scop unic: deblocarea B2 pentru C10.

Modificare permisă:
Adaugă intrarea `10` în dict-ul `IDENTITATI` din `load_identitate`, după intrarea `09`.

Bloc de adăugat:

```python
        '10': {
            'cod': 'C10', 'nume_hero_caps_rand1': 'MĂSURA',
            'nume_slug': 'Masuri',
            'meta_val_treapta': 'RELAȚII · <b>MĂSURI</b> · COMPARAȚII · INTERPRETARE (ANALIZĂ)'
        },
```

Această modificare este aprobată explicit de BRAIN pentru C10.

---

# CONFIRMĂRI BRAIN

1. Confirm decizia Claude C10 de a copia HTML din C09, nu din C01, pentru continuitate T3.
2. Confirm că B2 trebuie satisfăcut, nu ocolit.
3. Confirm că după patch-ul minim în `gate_v20.py`, Claude C10 trebuie să ruleze din nou gate_v20 pentru C10.
4. Dacă gate_v20 trece, Claude C10 continuă generarea setului complet C10:
   - HTML-Editor-Studiu
   - HTML-Video
   - HTML-Editor-Video
   - FILM
   - audit_sync ZERO DRIFT
   - gate_v20 PASS
   - tier_guard_t3 PASS
   - commit unic al setului canonic

---

# LIMITE

Nu modifica alte reguli sistem.
Nu rescrie `gate_v20.py` complet.
Nu modifica arhitectura generală a gate-ului.
Nu muta încă scripturile build C10 în `_system/generatoare/`; cererea #2 este neblocantă și rămâne pentru mai târziu.
Nu modifica alte construcții.

---

# SPEC C10 FINAL RĂMÂNE NESCHIMBAT

C10 = MĂSURI.
Verb: `a defini`.
Întrebare-mamă: `Cât?`.
Hero: `MĂSURA POTRIVITĂ`.
Fenomene C10:
1. Măsura ca definiție unică, single source of truth.
2. Baza de raportare.
3. Reperul / pragul.
4. Context-awareness.
5. Cifra utilă vs cifra decorativă.
6. Semnalul controlabil.

Nu include ranking, contribuție, comparație contextuală, ABC sau Pareto.
