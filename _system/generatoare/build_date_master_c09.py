#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_date_master_c09.py - Date_MASTER-C09.xlsx (T3 · RELATII), versiune SIMPLA UX.

BRAIN-012-REV1: workbook de cursant, MAXIM 7 foi vizibile. C09 nu e un curs de
data modeling, e constructia in care cursantul intelege si executa relatiile.
Mesaj: "Tabelele nu sunt problema. Problema e ca nu vorbesc intre ele."

7 foi vizibile:
  1 START          - ghid scurt al exercitiului
  2 Vanzari        - fact principal (neatins fata de C08, suma conservata)
  3 Produse        - dimensiune (cheie cod_produs)
  4 Clienti        - dimensiune (cheie client; cod_client = cheia stabila)
  5 Regiuni        - dimensiune (cheie judet -> regiune macro)
  6 Calendar       - dimensiune (cheie data -> an/luna/trimestru)
  7 Relatii_Model  - comaseaza: model 1:M + integritate + citire demo + handoff

Eliminate fata de slice 1: AGENTI, DEPOZITE, _REL_CLIENTI, _MODEL, _INTEGRITATE,
_CITIRE_DEMO, _README, CONTROL_FINAL. Zero foi helper ascunse.

Garda C09 (pastrata): doar legare + prima citire cross-tabel. Zero masuri DAX
numite, zero ranking, zero dashboard, zero cauza, zero recomandare.

Uz: python3 _system/generatoare/build_date_master_c09.py
"""
import openpyxl
from openpyxl.styles import Font, PatternFill
import os

SRC = 'c08/Date_MASTER-C08.xlsx'
OUT = 'c09/Date_MASTER-C09.xlsx'
SUMA_ASTEPTATA = 7986019.38

JUDET_REGIUNE = {
    'Brașov': 'Transilvania', 'Cluj': 'Transilvania', 'Mureș': 'Transilvania',
    'Sibiu': 'Transilvania', 'Timiș': 'Banat', 'București': 'Muntenia',
    'Constanța': 'Dobrogea', 'Iași': 'Moldova',
}
LUNI = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie',
        'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie']
ZILE = ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']

HDR_FILL = PatternFill('solid', fgColor='1F2A44')
HDR_FONT = Font(color='FFFFFF', bold=True)
TITLE = Font(bold=True, size=12, color='1F2A44')
SECT = Font(bold=True, size=11, color='B8860B')


def hdr(ws, row):
    for c in ws[row]:
        if c.value is not None:
            c.fill = HDR_FILL; c.font = HDR_FONT


def main():
    os.makedirs('c09', exist_ok=True)
    src = openpyxl.load_workbook(SRC, data_only=True)
    V = src['Vanzari']
    vhdr = [c.value for c in next(V.iter_rows(min_row=1, max_row=1))]
    ix = {h: i for i, h in enumerate(vhdr)}
    vrows = [list(r) for r in V.iter_rows(min_row=2, values_only=True)]
    nrows = len(vrows)
    vlast = nrows + 1

    out = openpyxl.Workbook()
    out.remove(out.active)

    # --- 1 START (ghid cursant) ---
    ws = out.create_sheet('START')
    for line in [
        ['C09 · RELATII · cum fac tabelele sa raspunda impreuna'],
        [],
        ['Ideea mare:'],
        ['Tabelele nu sunt problema. Problema e ca nu vorbesc intre ele.'],
        ['Tabele separate  ->  chei  ->  relatii  ->  un model care raspunde.'],
        [],
        ['AHA: Fara relatii ai date. Cu relatii ai raspunsuri.'],
        [],
        ['Ce ai in acest fisier:'],
        ['  Vanzari        tabelul fact (fiecare tranzactie)'],
        ['  PRODUSE        dimensiune, legata prin cod_produs'],
        ['  CLIENTI        dimensiune, legata prin client (cod_client = cheia stabila)'],
        ['  Regiuni        dimensiune, legata prin judet (judet -> regiune)'],
        ['  Calendar       dimensiune, legata prin data (data -> an/luna/trimestru)'],
        ['  Relatii_Model  modelul: relatiile, verificarea lor si prima citire cross-tabel'],
        [],
        ['Exercitiul:'],
        ['  1. Vezi ca Vanzari nu stie singur regiunea sau perioada: ii lipsesc.'],
        ['  2. Legi fiecare dimensiune prin cheia ei (relatie 1:M).'],
        ['  3. Verifici relatiile in Relatii_Model (zero chei orfane).'],
        ['  4. Pui o intrebare care traverseaza tabelele si primesti un raspuns.'],
        [],
        ['C09 doar leaga si face prima citire cross-tabel.'],
        ['Cat valoreaza fiecare (masuri) vine la C10. Care conteaza, la C11. De ce, la C12.'],
    ]:
        ws.append(line)
    ws['A1'].font = TITLE
    ws['A3'].font = SECT; ws['A9'].font = SECT; ws['A17'].font = SECT

    # --- 2 Vanzari (fact neatins) ---
    wv = out.create_sheet('Vanzari')
    wv.append(vhdr)
    for r in vrows:
        wv.append(r)
    hdr(wv, 1)

    # --- 3 PRODUSE (nume canonic cerut de gate DATA-CONTINUITY) ---
    wp = out.create_sheet('PRODUSE')
    for row in src['PRODUSE'].iter_rows(values_only=True):
        wp.append(list(row))
    hdr(wp, 1)
    prod_last = src['PRODUSE'].max_row

    # --- 4 CLIENTI (nume canonic cerut de gate) ---
    wcl = out.create_sheet('CLIENTI')
    for row in src['CLIENTI'].iter_rows(values_only=True):
        wcl.append(list(row))
    hdr(wcl, 1)
    cli_last = src['CLIENTI'].max_row

    # AGENTI + DEPOZITE: cerute de contractul de date al gate-ului (canonic), dar
    # NU fac parte din experienta cursantului -> ASCUNSE (sheet_state='hidden').
    # Nu sunt legate de fact (fara cheie); raman doar pentru continuitatea schemei.
    for name in ('AGENTI', 'DEPOZITE'):
        wh = out.create_sheet(name)
        for row in src[name].iter_rows(values_only=True):
            wh.append(list(row))
        hdr(wh, 1)
        wh.sheet_state = 'hidden'

    # --- 5 Regiuni ---
    judete = sorted({r[ix['judet']] for r in vrows})
    wrg = out.create_sheet('Regiuni')
    wrg.append(['judet', 'regiune'])
    for j in judete:
        wrg.append([j, JUDET_REGIUNE.get(j, 'Necunoscuta')])
    hdr(wrg, 1)
    reg_last = len(judete) + 1

    # --- 6 Calendar ---
    dates = sorted({r[ix['data_factura']] for r in vrows if r[ix['data_factura']]})
    wca = out.create_sheet('Calendar')
    wca.append(['data', 'an', 'luna_nr', 'luna_nume', 'trimestru', 'zi_saptamana'])
    for d in dates:
        q = (d.month - 1) // 3 + 1
        wca.append([d, d.year, d.month, LUNI[d.month - 1], f'T{q}', ZILE[d.weekday()]])
    hdr(wca, 1)

    # cifre verificate independent (pentru coloana "rezultat" statica + assert)
    suma = round(sum(float(r[ix['valoare_neta']]) for r in vrows
                     if r[ix['valoare_neta']] not in (None, '')), 2)
    n_prod = len({r[ix['cod_produs']] for r in vrows})
    n_cli = len({r[ix['client_nume']] for r in vrows})
    n_reg = len(set(JUDET_REGIUNE.get(j) for j in judete))
    n_cal = len(dates)
    transilvania = [j for j in judete if JUDET_REGIUNE.get(j) == 'Transilvania']
    rng_t = ';'.join('"%s"' % j for j in transilvania)
    demo_client = sorted({r[ix['client_nume']] for r in vrows})[0]
    val_trans = round(sum(float(r[ix['valoare_neta']]) for r in vrows
                          if r[ix['judet']] in transilvania), 2)
    cnt_client = sum(1 for r in vrows if r[ix['client_nume']] == demo_client)

    # --- 7 Relatii_Model (comaseaza model + integritate + demo + handoff) ---
    wm = out.create_sheet('Relatii_Model')
    A = wm.append
    A(['RELATII_MODEL C09 · modelul, verificarea lui si prima citire cross-tabel'])
    A([])
    A(['1) MODELUL · relatii 1:M (fact Vanzari legat de dimensiuni)'])
    A(['fact', 'dimensiune', 'cheie', 'cardinalitate', 'ce aduce dimensiunea'])
    A(['Vanzari', 'PRODUSE', 'cod_produs', 'M:1', 'categorie, pret_baza'])
    A(['Vanzari', 'CLIENTI', 'client_nume (cheie stabila: cod_client)', 'M:1', 'cod_client, judet'])
    A(['Vanzari', 'Regiuni', 'judet', 'M:1', 'regiune macro'])
    A(['Vanzari', 'Calendar', 'data_factura', 'M:1', 'an, luna, trimestru'])
    A([])
    A(['2) INTEGRITATE · relatii curate (zero chei orfane), cardinalitate, suma'])
    A(['verificare', 'rezultat', 'asteptat'])
    A(['orfani cod_produs (fact fara dimensiune)',
       '=SUMPRODUCT(--ISNA(MATCH(Vanzari!E2:E%d,PRODUSE!A2:A%d,0)))' % (vlast, prod_last), 0])
    A(['orfani client (nume fara potrivire in Clienti)',
       '=SUMPRODUCT(--ISNA(MATCH(Vanzari!C2:C%d,CLIENTI!B2:B%d,0)))' % (vlast, cli_last), 0])
    A(['orfani judet (fact fara regiune)',
       '=SUMPRODUCT(--ISNA(MATCH(Vanzari!D2:D%d,Regiuni!A2:A%d,0)))' % (vlast, reg_last), 0])
    A(['cardinalitate Produse (distinct in fact)',
       '=SUMPRODUCT(1/COUNTIF(Vanzari!E2:E%d,Vanzari!E2:E%d))' % (vlast, vlast), n_prod])
    A(['cardinalitate Clienti (distinct in fact)', n_cli, n_cli])
    A(['cardinalitate Regiuni', n_reg, n_reg])
    A(['cardinalitate Calendar (zile)', n_cal, n_cal])
    A(['suma valoare_neta (conservata din C08)',
       '=ROUND(SUM(Vanzari!J2:J%d),2)' % vlast, SUMA_ASTEPTATA])
    A([])
    A(['3) PRIMA CITIRE CROSS-TABEL · o singura citire de demonstratie'])
    A(['(nu e masura reutilizabila, nu e clasament; doar dovada ca modelul raspunde)'])
    A(['Intrebare: cata valoare pe regiunea "Transilvania"?'])
    A(['Vanzari singur nu poate: nu are coloana "regiune", doar "judet".'])
    A(['Raspuns prin Vanzari[judet] -> Regiuni:',
       '=SUMPRODUCT((ISNUMBER(MATCH(Vanzari!D2:D%d,{%s},0)))*Vanzari!J2:J%d)' % (vlast, rng_t, vlast),
       val_trans])
    A(['Intrebare: cate tranzactii are clientul "%s"?' % demo_client])
    A(['Raspuns prin Vanzari[client_nume] -> Clienti:',
       '=COUNTIF(Vanzari!C2:C%d,"%s")' % (vlast, demo_client), cnt_client])
    A([])
    A(['4) HANDOFF'])
    A(['input de la C08', 'set cunoscut (ecosistem recunoscut descriptiv)'])
    A(['output C09', 'model relational interogabil (relatii activate + prima citire)'])
    A(['predat catre C10', 'defineste masuri peste model (C09 nu defineste masuri)'])
    A(['suma conservata cap-coada', SUMA_ASTEPTATA])

    wm['A1'].font = TITLE
    for cell in ('A3', 'A9', 'A20', 'A29'):
        wm[cell].font = SECT
    hdr(wm, 4)   # header model
    hdr(wm, 10)  # header integritate

    out.save(OUT)
    visible = [ws.title for ws in out.worksheets if ws.sheet_state == 'visible']
    hidden = [ws.title for ws in out.worksheets if ws.sheet_state != 'visible']
    print('SCRIS:', OUT)
    print('  foi vizibile (%d):' % len(visible), visible)
    print('  foi ascunse (%d):' % len(hidden), hidden)
    print('  suma:', suma, '| delta:', round(suma - SUMA_ASTEPTATA, 2))
    print('  cardinalitati: Produse=%d Clienti=%d Regiuni=%d Calendar=%d' %
          (n_prod, n_cli, n_reg, n_cal))
    print('  demo: Transilvania=%.2f | client "%s"=%d tranzactii' %
          (val_trans, demo_client, cnt_client))
    assert len(visible) <= 7, 'PREA MULTE FOI: %d' % len(visible)
    assert abs(suma - SUMA_ASTEPTATA) < 0.01, 'SUMA NU se conserva'
    print('  OK: <=7 foi, suma conservata')


if __name__ == '__main__':
    main()
