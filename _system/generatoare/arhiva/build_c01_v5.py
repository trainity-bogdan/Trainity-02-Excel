# -*- coding: utf-8 -*-
# C01 STRUCTURA TABELELOR v5 - CSS refactorizat zero duplicate, badge 3 stari,
# layout desktop stabil, mobil robust clamp. Feedback extern via G-06.
import json as _j
OUT = "/home/claude/brain/livrabile_C01/HTML-Excel-01-Structura.html"
HOOK   = "Arată ca tabel. Nu este tabel."
MANTRA = "Nu reconstruim tabelul. Îl facem controlabil."
MOTTO  = "Mai întâi structura. Apoi orice."
SUMA   = "1.247.893,50"
WOW6   = "Nimic șters. Nimic adăugat. Doar structura, eliberată."

# Cele 5 fenomene C01 (BLOC 14 - inghetate)
ANOMALII = [
    ("01","ANTET RAPORT","3 rânduri de titlu raport înainte de antetul real al tabelului."),
    ("02","SUBTOTALURI","4 rânduri SUBTOTAL pe categorie, inserate între tranzacții."),
    ("03","TOTAL GENERAL","1 rând TOTAL GENERAL la final, numărat de SUM ca dată."),
    ("04","BLANK FALS","53 rânduri goale false care rup continuitatea tabelului între tranzacții."),
    ("05","COLOANE ASCUNSE","2 coloane ascunse (cod_filiala, cod_user) care nu se văd, dar există în fișier."),
]

CSS = r"""
/* ============ 1. BASE ============ */
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
html, body { background: #fff; color: #000; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif; line-height: 1.5; -webkit-font-smoothing: antialiased; }
body { font-size: 15px; overflow-x: hidden; }
::selection { background: #FFD400; color: #000; }
::-moz-selection { background: #FFD400; color: #000; }
mark.persist { background: #000; color: #FFD400; padding: 1px 2px; cursor: pointer; border-radius: 2px; transition: background .15s; }
mark.persist:hover { background: #1F7A1F; }
mark.persist::selection { background: #FFD400; color: #000; }

/* ============ 2. LAYOUT ============ */
.book-app { max-width: 1180px; margin: 0 auto; position: relative; }
.app-grid { display: block; padding-right: 240px; }
.main-content { min-width: 0; }
.side-nav { position: fixed; top: 0; right: calc((100% - 1180px) / 2); width: 226px; height: calc(100vh - 54px); overflow-y: auto; background: #000; color: #FFD400; padding: 8px 0; border-left: 1px solid #333; display: flex; flex-direction: column; }
.side-nav::-webkit-scrollbar { width: 6px; }
.side-nav::-webkit-scrollbar-track { background: transparent; }
.side-nav::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
.side-nav::-webkit-scrollbar-thumb:hover { background: #555; }
.side-nav { scrollbar-width: thin; scrollbar-color: #333 transparent; }
@media (min-width: 1181px) { .side-nav { right: calc(50vw - 590px); } }
@media (max-width: 1180px) { .book-app { max-width: 100%; } .app-grid { padding-right: 240px; } .side-nav { right: 0; } }
.mobile-nav-toggle { display: none; position: fixed; top: 12px; right: 12px; z-index: 200; background: #000; color: #FFD400; border: none; width: 44px; height: 44px; font-size: 18px; cursor: pointer; }
.mobile-nav-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,.5); z-index: 150; }
.mobile-nav-overlay.show { display: block; }

/* ============ 3. COMPONENTS ============ */
/* sidebar */
.side-nav-brand { padding: 0 14px 4px; border-bottom: 1px solid #333; margin-bottom: 3px; }
.side-nav-label { font-size: 10px; letter-spacing: 1.6px; color: #888; margin-bottom: 4px; font-weight: 500; }
.side-nav-title { font-size: 14px; font-weight: 500; color: #FFD400; line-height: 1.1; }
.nav-progress-mini { padding: 0 14px 4px; border-bottom: 1px solid #333; margin-bottom: 3px; }
.nav-progress-track { background: #333; height: 3px; margin-bottom: 4px; }
.nav-progress-fill { background: #FFD400; height: 100%; width: 0; transition: width .3s ease; }
.nav-progress-stat { font-size: 10px; color: #FFD400; letter-spacing: .3px; display: flex; justify-content: space-between; line-height: 1.2; }
.nav-progress-stat span:last-child { color: #888; }
.nav-summary { padding: 3px 14px; border-bottom: 1px solid #333; margin-bottom: 3px; }
.nav-summary-row { display: flex; justify-content: space-between; align-items: baseline; padding: 2px 0; gap: 10px; line-height: 1.3; }
.nav-summary-k { font-size: 9px; letter-spacing: .6px; color: #888; flex-shrink: 0; }
.nav-summary-v { font-size: 10px; font-weight: 700; color: #FFD400; text-align: right; }
.nav-section-label { padding: 4px 14px 2px; font-size: 9px; letter-spacing: 1.3px; color: #888; font-weight: 500; }
.nav-controls { padding: 0 14px 4px; border-bottom: 1px solid #333; margin-bottom: 3px; display: flex; flex-direction: column; gap: 3px; }
.nav-ctrl-btn { background: #FFD400; color: #000; border: none; padding: 4px 10px; font-size: 10px; font-weight: 800; letter-spacing: .8px; cursor: pointer; font-family: inherit; transition: all .15s; line-height: 1.4; }
.nav-ctrl-btn:hover { background: #fff; }
.nav-ctrl-btn:active { transform: translateY(1px); }
.nav-ctrl-btn.alt { background: transparent; color: #888; border: 1px solid #444; }
.nav-ctrl-btn.alt:hover { background: transparent; color: #FFD400; border-color: #FFD400; }
.nav-item { display: block; padding: 3px 14px; color: #FFD400; cursor: pointer; font-size: 11.5px; border-left: 3px solid transparent; transition: all .15s; line-height: 1.2; }
.nav-item:hover { background: #1a1a1a; border-left-color: #444; }
.nav-item.active { background: #1a1a1a; border-left-color: #FFD400; }
.nav-item.done { color: #888; }
.nav-item.done .nav-item-num { background: #1F7A1F; color: #fff; }
.nav-item-row { display: flex; align-items: center; gap: 10px; }
.nav-item-num { width: 17px; height: 17px; background: #FFD400; color: #000; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 500; flex-shrink: 0; }
.nav-item-text { line-height: 1.3; flex: 1; }
.nav-item-meta { font-size: 9px; color: #888; letter-spacing: .3px; margin-top: 0; line-height: 1.15; }
.nav-final-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 4px; padding: 0 14px 4px; }
.nav-final-dot { aspect-ratio: 1; background: #1a1a1a; border: 1px solid #333; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #FFD400; font-weight: 500; cursor: pointer; transition: all .15s; }
.nav-final-dot:hover { background: #222; }
.nav-final-dot.done { background: #1F7A1F; border-color: #1F7A1F; color: #fff; }
.nav-reset { padding: 10px 16px 14px; border-top: 1px solid #333; margin-top: 10px; }
.nav-reset-btn { background: transparent; color: #888; border: 1px solid #333; padding: 7px 12px; font-size: 10px; letter-spacing: .6px; cursor: pointer; font-family: inherit; width: 100%; }
.nav-reset-btn:hover { color: #FFD400; border-color: #FFD400; }
.nav-reset-btn + .nav-reset-btn { margin-top: 5px; }

/* cover */
.cover { background: #FFD400; padding: 56px 40px 40px; border-bottom: 4px solid #000; text-align: right; position: relative; }
.cover-label { font-size: 12px; font-weight: 500; letter-spacing: 1.8px; color: #000; margin-bottom: 12px; }
.cover-label-pill { background: #000; color: #FFD400; padding: 4px 12px; font-weight: 700; letter-spacing: 1.6px; margin-left: 4px; }
.cover-title { font-size: clamp(38px, 7vw, 64px); font-weight: 500; line-height: 1; color: #000; margin-bottom: 16px; letter-spacing: -1px; word-break: break-word; }
.cover-subtitle-main { display: inline-block; background: #C00000; color: #fff; border: 2px solid #000; box-shadow: 4px 4px 0 #000; font-size: clamp(15px, 2.4vw, 18px); font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; line-height: 1.3; padding: 10px 18px; margin: 8px 0 16px; }
.cover-subtitle-main::before { content: "INTRIGA · "; font-weight: 800; letter-spacing: 1.4px; color: #fff; opacity: .8; font-size: 11px; vertical-align: middle; margin-right: 6px; }
.cover-miza { background: #000; color: #FFD400; display: block; padding: 16px 24px; font-size: clamp(15px, 2.2vw, 17px); font-weight: 800; line-height: 1.35; letter-spacing: -.2px; margin: 16px 0 24px; text-align: left; }
.cover-miza::before { content: "MIZA "; font-weight: 800; letter-spacing: 1.4px; color: #FFD400; opacity: .55; font-size: 11px; margin-right: 8px; display: inline-block; }
.cover-meta { display: grid; grid-template-columns: 1fr; background: #000; padding: 16px 24px; margin-top: 24px; text-align: left; }
.cover-meta-row { display: grid; grid-template-columns: 200px 1fr; padding: 10px 0; border-bottom: 1px solid #333; color: #FFD400; font-size: 13px; letter-spacing: .4px; align-items: baseline; }
.cover-meta-row:last-child { border-bottom: none; }
.cover-meta-row span:first-child { font-weight: 500; letter-spacing: 1.4px; font-size: 12px; }
.cover-meta-row .meta-value b { color: #fff; font-weight: 700; }
.meta-link { color: #FFD400; text-decoration: underline; text-decoration-color: rgba(255,212,0,.35); text-underline-offset: 3px; transition: all .15s; }
.meta-link:hover { color: #fff; text-decoration-color: #fff; }
.mantra-band { background: #FFD400; color: #000; padding: 34px 40px; text-align: center; border-top: 4px solid #000; border-bottom: 4px solid #000; }
.mantra-band-main { font-size: clamp(20px, 3.8vw, 30px); font-weight: 900; letter-spacing: -.3px; line-height: 1.2; text-transform: uppercase; }
.mantra-band-sub { font-size: clamp(12px, 2vw, 15px); font-weight: 800; letter-spacing: 2px; margin-top: 12px; color: #000; opacity: .72; }

/* exec hero */
.exec-hero-panel { background: #000; color: #fff; padding: 52px 44px; border-bottom: 4px solid #FFD400; }
.exec-kicker { color: #FFD400; font-size: 12px; letter-spacing: 1.8px; font-weight: 700; margin-bottom: 14px; }
.exec-hero-panel h2 { color: #FFD400; font-size: clamp(28px, 5vw, 44px); line-height: 1.05; letter-spacing: -1px; margin-bottom: 18px; text-transform: uppercase; font-weight: 900; }
.exec-hero-panel p { color: #fff; font-size: clamp(15px, 2.2vw, 18px); line-height: 1.55; max-width: 850px; }
.exec-hero-panel p + p { margin-top: 14px; }
.exec-sharp + p { margin-top: 18px; }
.exec-sharp { color: #FFD400; font-weight: 800; line-height: 1.4; max-width: 760px; margin-top: 16px; border-left: 4px solid #FFD400; padding-left: 18px; }

/* wow strip */
.wow-strip { background: #FFD400; color: #000; display: flex; align-items: center; gap: 28px; padding: 34px 44px; border-bottom: 4px solid #000; }
.wow-strip.secondary { background: #000; color: #FFD400; border-top: 4px solid #FFD400; border-bottom: 4px solid #FFD400; }
.wow-number { font-size: clamp(40px, 8vw, 76px); font-weight: 900; line-height: .9; letter-spacing: -2px; min-width: 190px; text-align: center; word-break: break-word; }
.wow-title { font-size: clamp(20px, 3.4vw, 26px); font-weight: 900; line-height: 1; letter-spacing: 1px; }
.wow-sub { font-size: clamp(14px, 2vw, 16px); margin-top: 8px; opacity: .85; }

/* section */
.section { padding: 48px 40px 32px; border-bottom: 1px solid #F0F0F0; scroll-margin-top: 20px; }
.compact-section { padding-top: 38px; }
.section-marker { font-size: 12px; font-weight: 500; letter-spacing: 1.6px; color: #888; margin-top: 36px; margin-bottom: 10px; }
.section-title { font-size: clamp(22px, 4vw, 28px); font-weight: 500; color: #000; line-height: 1.15; margin-bottom: 12px; }
.section-intro { font-size: 16px; color: #444; line-height: 1.6; margin-bottom: 24px; max-width: 720px; }

/* anomaly */
.anomaly-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 24px 0; }
.anomaly-card { border: 2px solid #000; padding: 16px 14px; min-height: 140px; background: #fff; }
.anomaly-card span { display: inline-flex; background: #000; color: #FFD400; width: 28px; height: 28px; align-items: center; justify-content: center; font-size: 11px; font-weight: 800; margin-bottom: 12px; }
.anomaly-card b { display: block; font-size: 12px; line-height: 1.2; margin-bottom: 8px; }
.anomaly-card p { font-size: 13px; line-height: 1.4; color: #333; }

/* decision / slogan / inline */
.decision-block { background: #000; color: #fff; border-left: 8px solid #FFD400; padding: 24px 26px; margin: 24px 0; }
.decision-block.mini { background: #FFF4E5; color: #000; border: 1px solid #E8A800; border-left: 8px solid #E8A800; }
.decision-label { color: #FFD400; font-size: 11px; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 8px; }
.decision-block.mini .decision-label { color: #B36A00; }
.decision-title { font-size: clamp(20px, 3.4vw, 24px); font-weight: 900; line-height: 1.15; }
.slogan-box { background: #FFD400; padding: 32px 28px; margin: 32px 0; text-align: center; }
.slogan-text { font-size: clamp(22px, 4vw, 28px); font-weight: 500; color: #000; line-height: 1.2; }

/* data table */
.data-table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 20px 0; border: 1px solid #eee; border-radius: 4px; max-width: 100%; }
.data-table { width: 100%; border-collapse: collapse; font-size: 14px; background: #fff; }
.data-table thead { background: #000; color: #FFD400; }
.data-table thead th { padding: 14px 16px; text-align: left; font-weight: 700; font-size: 11px; letter-spacing: 1.2px; text-transform: uppercase; white-space: nowrap; }
.data-table tbody tr { border-bottom: 1px solid #eee; }
.data-table tbody tr:nth-child(even) { background: #fafafa; }
.data-table tbody tr:hover { background: #FFFDF0; }
.data-table tbody td { padding: 12px 16px; vertical-align: middle; line-height: 1.4; color: #000; }
.data-table tbody td:first-child { font-weight: 700; width: 44px; text-align: center; color: #FFD400; background: #000; }
.data-table tbody td.good { color: #1F7A1F; font-weight: 700; }
.data-table tbody td.bad { color: #C00000; font-weight: 700; }

/* stage */
.stage { margin-bottom: 14px; scroll-margin-top: 20px; }
.stage-header { background: #000; color: #FFD400; padding: 24px 32px; cursor: pointer; position: relative; user-select: none; transition: background .2s; }
.stage-header:hover { background: #1a1a1a; }
.stage-header-quote { font-style: italic; font-size: 14px; color: #FFD400; opacity: .85; margin-bottom: 12px; line-height: 1.4; }
.stage-header-grid { display: flex; align-items: flex-start; gap: 18px; }
.stage-number { font-size: 56px; font-weight: 500; line-height: 1; color: #FFD400; flex-shrink: 0; }
.stage-info { flex: 1; min-width: 0; }
.stage-info-label { font-size: 11px; letter-spacing: 1.6px; margin-bottom: 6px; opacity: .7; }
.stage-info-name { font-size: clamp(17px, 3vw, 22px); font-weight: 500; margin-bottom: 8px; }
.stage-info-meta { font-size: 12px; letter-spacing: .5px; opacity: .85; display: flex; align-items: center; flex-wrap: wrap; gap: 6px; }
.stage-info-badges { margin-top: 10px; }
.phase-tag { display: inline-block; background: #FFD400; color: #000; font-size: 10px; font-weight: 800; letter-spacing: 1px; padding: 2px 8px; }
.stage-badge { display: inline-block; font-size: 10px; font-weight: 800; letter-spacing: 1.2px; color: #888; border: 1px solid #444; padding: 5px 12px; }
.stage-toggle { width: 36px; height: 36px; background: #FFD400; color: #000; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 500; flex-shrink: 0; transition: transform .2s; }
.stage-progress { position: absolute; bottom: 0; left: 0; height: 3px; background: #FFD400; width: 0; transition: width .3s ease; }
.stage-body { background: #fff; padding: 28px 32px 32px; border: 1px solid #F0F0F0; border-top: none; display: none; }
.stage-exec-summary { background: #FFFAE0; border-left: 6px solid #FFD400; padding: 16px 18px; margin-bottom: 18px; font-size: 15px; line-height: 1.45; font-weight: 600; }
.hook-local { display: flex; flex-wrap: wrap; gap: 0; margin: 4px 0 18px; }
.hook-local b { background: #000; color: #FFD400; font-size: 12px; font-weight: 800; letter-spacing: 1.4px; text-transform: uppercase; padding: 8px 14px; line-height: 1.35; }
.hook-local i { background: #FFFAE0; color: #B36A00; font-size: 12px; font-weight: 700; letter-spacing: .8px; text-transform: uppercase; padding: 8px 14px; font-style: normal; line-height: 1.35; border: 1px solid #FFE680; border-left: none; }
.stage-transition { background: #0A0A0A; color: #FFD400; border-left: 6px solid #FFD400; padding: 18px 22px; margin: 22px 0 4px; font-size: 17px; font-weight: 800; line-height: 1.4; }

/* step */
.step { background: #fff; border: 1px solid #CCC; border-left: 4px solid #000; padding: 18px 22px; margin-bottom: 12px; transition: all .2s; scroll-margin-top: 20px; }
.step-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; }
.step-head-content { flex: 1; min-width: 0; }
.step-num { font-size: 11px; color: #888; letter-spacing: 1.4px; margin-bottom: 6px; font-weight: 500; }
.step-title { font-size: 17px; font-weight: 500; color: #000; line-height: 1.3; }
.step-check { width: 26px; height: 26px; border: 2px solid #000; background: #fff; cursor: pointer; flex-shrink: 0; position: relative; transition: all .15s; }
.step-check:hover { background: #FFFAE0; }
.step-body { margin-top: 12px; padding-top: 12px; border-top: 1px solid #F0F0F0; }
.step-action { font-size: 14px; color: #000; line-height: 1.6; }

/* prompt box */
.prompt-box { background: #000; border: 1px solid #000; padding: 22px 24px; margin: 18px 0; }
.prompt-label { font-size: 11px; font-weight: 500; letter-spacing: 1.4px; color: #FFD400; margin-bottom: 14px; }
.prompt-text { background: #1a1a1a; border: 1px solid #333; padding: 16px 18px; font-family: "SF Mono", Consolas, "Courier New", monospace; font-size: 13px; line-height: 1.65; color: #fff; margin-bottom: 14px; white-space: pre-wrap; user-select: text; cursor: text; }
.prompt-text::selection { background: #FFD400; color: #000; }
.copy-btn { background: #FFD400; color: #000; border: none; padding: 11px 20px; font-size: 12px; font-weight: 500; letter-spacing: 1px; cursor: pointer; font-family: inherit; transition: all .15s; }
.copy-btn:hover { background: #fff; }
.copy-btn.copied { background: #1F7A1F; color: #fff; }

/* capcana */
.capcana { background: #FFF4E5; border: 1px solid #E8A800; padding: 18px 22px; margin: 18px 0; }
.capcana-label { font-size: 12px; font-weight: 700; letter-spacing: 1.2px; color: #B36A00; margin-bottom: 8px; }
.capcana-text { font-size: 14px; color: #000; line-height: 1.55; }

/* before/after */
.ba-grid { display: grid; grid-template-columns: 1fr 1fr; border: 2px solid #000; margin: 24px 0; }
.ba-col { padding: 26px; }
.ba-before { background: #1a1a1a; color: #fff; border-right: 2px solid #000; }
.ba-after { background: #FFD400; color: #000; }
.ba-label { font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px; }
.ba-before .ba-label { color: #E8A800; }
.ba-list { list-style: none; padding: 0; margin: 0; }
.ba-list li { font-size: 15px; line-height: 1.5; padding: 9px 0 9px 22px; position: relative; border-bottom: 1px solid rgba(255,255,255,.12); }
.ba-after .ba-list li { border-bottom: 1px solid rgba(0,0,0,.12); }
.ba-list li:last-child { border-bottom: none; }
.ba-before .ba-list li::before { content: "X"; position: absolute; left: 0; color: #C00000; font-weight: 900; }
.ba-after .ba-list li::before { content: "OK"; position: absolute; left: 0; color: #1F7A1F; font-weight: 900; font-size: 11px; }

/* verification */
.verification { background: #E8F5E8; border: 1px solid #1F7A1F; padding: 22px 24px; margin: 22px 0 0; }
.verif-label { font-size: 11px; font-weight: 500; letter-spacing: 1.4px; color: #1F7A1F; margin-bottom: 12px; }
.verif-list { list-style: none; padding: 0; margin-bottom: 16px; }
.verif-list li { font-size: 14px; color: #000; line-height: 1.7; }
.verif-list li::before { content: ">  "; font-weight: 700; color: #1F7A1F; }
.verification-btn { background: #fff; color: #000; border: 1px solid #000; padding: 10px 20px; font-size: 12px; font-weight: 500; letter-spacing: .8px; cursor: pointer; font-family: inherit; transition: all .2s; }
.verification-btn:hover { background: #FFD400; }

/* final exec */
.final-exec-section { background: #FAFAFA; padding: 48px 40px 32px; }
.final-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 24px; }
.final-card { background: #fff; border: 1px solid #CCC; padding: 16px 18px; display: flex; gap: 14px; align-items: flex-start; scroll-margin-top: 20px; }
.final-num { background: #000; color: #FFD400; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 500; flex-shrink: 0; }
.final-content { flex: 1; }
.final-label { font-size: 11px; letter-spacing: 1px; color: #888; margin-bottom: 4px; }
.final-text { font-size: 14px; color: #000; line-height: 1.5; margin-bottom: 10px; }
.final-check-btn { background: transparent; color: #000; border: 1px solid #000; padding: 6px 14px; font-size: 11px; font-weight: 500; letter-spacing: .6px; cursor: pointer; font-family: inherit; }
.final-check-btn:hover { background: #FFD400; }
.completion-badge { background: #1F7A1F; color: #fff; padding: 36px 40px; text-align: center; display: none; }
.completion-badge.show { display: block; }
.completion-title { font-size: 28px; font-weight: 500; margin-bottom: 8px; }
.completion-subtitle { font-size: 15px; opacity: .9; line-height: 1.5; }

/* next + payoff + footer */
.next-section { background: #F8F8F8; padding: 36px 40px; }
.next-c02-box { background: #fff; border: 1px solid #CCC; border-left: 4px solid #FFD400; padding: 20px 24px; margin-top: 16px; }
.next-c02-label { font-size: 11px; letter-spacing: 1.4px; color: #888; margin-bottom: 6px; }
.next-c02-name { font-size: 18px; font-weight: 500; color: #000; margin-bottom: 6px; }
.next-c02-desc { font-size: 14px; color: #444; line-height: 1.5; }
.payoff-section { background: #000; color: #fff; padding: 64px 40px; }
.payoff-line { font-size: clamp(18px, 3vw, 22px); font-weight: 500; line-height: 1.5; color: #fff; max-width: 720px; }
.payoff-line.dim { color: #888; }
.payoff-break { height: 28px; }
.payoff-key { font-size: clamp(22px, 4.5vw, 28px); font-weight: 900; color: #FFD400; line-height: 1.25; max-width: 720px; }
.payoff-key::before { content: "WOW "; font-weight: 800; letter-spacing: 1.4px; color: #FFD400; opacity: .55; font-size: 11px; margin-right: 8px; display: inline-block; vertical-align: middle; }
.payoff-num { display: flex; flex-wrap: wrap; gap: 0 24px; margin: 32px 0; border-top: 2px solid #FFD400; border-bottom: 2px solid #FFD400; }
.payoff-num .pn { padding: 18px 0; }
.payoff-num .pn-v { display: block; font-size: clamp(22px, 4vw, 30px); font-weight: 900; color: #FFD400; line-height: 1; word-break: break-word; }
.payoff-num .pn-k { display: block; font-size: 12px; color: #888; letter-spacing: 1px; text-transform: uppercase; margin-top: 6px; }
.payoff-close { font-size: clamp(24px, 5vw, 32px); font-weight: 900; color: #FFD400; margin-top: 28px; line-height: 1.2; }
.payoff-motto { margin-top: 44px; padding-top: 22px; border-top: 1px solid #333; font-size: clamp(14px, 2vw, 16px); font-style: italic; color: #888; letter-spacing: .3px; max-width: 720px; }
.payoff-motto::before { content: "MOTTO "; font-style: normal; font-weight: 800; letter-spacing: 1.4px; color: #FFD400; opacity: .55; font-size: 11px; margin-right: 8px; display: inline-block; vertical-align: middle; }
.footer { background: #000; color: #888; padding: 28px 40px; text-align: center; font-size: 12px; letter-spacing: .5px; line-height: 1.7; }
.footer-brand { color: #FFD400; font-weight: 500; }
/* Buton CONTINUA CU PASUL - FIXED sticky jos, in coloana sidebar, separat de sidebar */
.nav-next-btn { display: none; position: fixed; bottom: 0; right: calc((100% - 1180px) / 2); width: 226px; background: #FFD400; color: #000; border: none; border-top: 3px solid #000; padding: 14px 14px; font-size: 12px; font-weight: 700; letter-spacing: .6px; cursor: pointer; font-family: inherit; z-index: 70; transition: all .15s; text-align: center; line-height: 1.3; box-shadow: 0 -3px 12px rgba(0,0,0,.25); }
.nav-next-btn:hover { background: #000; color: #FFD400; }
.nav-next-btn.show { display: block; }
@media (max-width: 1180px) { .nav-next-btn { right: 0; } }
@media (min-width: 1181px) { .nav-next-btn { right: calc(50vw - 590px); } }
/* Sidebar lasa loc jos pentru buton (padding-bottom) ca sa nu acopere ultimele etape la scroll */
/* sidebar acum are height calc, nu mai depaseste butonul; gap vizual de 6px alb */
/* Scroll-to-top - mai mic, sticky bottom-right in zona continut (nu peste sidebar) */
.scroll-top-btn { position: fixed; bottom: 18px; right: max(calc((100vw - 1180px)/2 + 242px), 242px); width: 36px; height: 36px; background: #000; color: #FFD400; border: 2px solid #FFD400; box-shadow: 2px 2px 0 #FFD400; font-size: 16px; font-weight: 700; line-height: 1; cursor: pointer; z-index: 65; display: flex; align-items: center; justify-content: center; transition: all .15s; }
.scroll-top-btn:hover { background: #FFD400; color: #000; border-color: #000; box-shadow: 2px 2px 0 #000; }
.scroll-top-btn:active { transform: translate(1px, 1px); box-shadow: 1px 1px 0 #FFD400; }
/* Buton PDF stanga sus */
.pdf-download-btn { position: absolute; top: 24px; left: 24px; background: #C00000; color: #fff; border: 2px solid #000; padding: 7px 12px; font-size: 10.5px; font-weight: 700; letter-spacing: .6px; cursor: pointer; font-family: inherit; box-shadow: 3px 3px 0 #000; transition: all .15s; z-index: 5; display: inline-flex; align-items: center; gap: 6px; }
.pdf-download-btn:hover { background: #fff; color: #C00000; }
.pdf-download-btn:active { transform: translate(2px, 2px); box-shadow: 1px 1px 0 #000; }
.pdf-arrow { font-size: 12px; line-height: 1; }
@media print { .pdf-download-btn { display: none; } }
.pdf-arrow { font-size: 14px; font-weight: 900; }

/* ============ 4. STATES ============ */
.stage.open .stage-toggle { transform: rotate(180deg); }
.stage.open .stage-body { display: block; }
.stage.done .stage-header { background: #155515; }
.stage.done .stage-header:hover { background: #1F7A1F; }
.stage.done .stage-header-quote { color: #fff; }
.stage.done .stage-number { color: #fff; }
.stage.done .stage-toggle { background: #fff; color: #1F7A1F; }
.stage.done .stage-progress { background: #fff; }
.stage-badge.working { color: #000; background: #E8A800; border-color: #E8A800; }
.stage-badge.done { color: #fff; background: #1F7A1F; border-color: #1F7A1F; }
.step.done { background: #000; border-color: #000; border-left-color: #FFD400; }
.step.done .step-title, .step.done .step-action { color: #FFD400; }
.step.done .step-num { color: #888; }
.step.done .step-title { text-decoration: line-through; opacity: .7; }
.step.done .step-body { border-top-color: #333; }
.step.done .step-check { background: #FFD400; border-color: #FFD400; }
.step.done .step-check::after { content: ""; position: absolute; left: 7px; top: 2px; width: 7px; height: 13px; border: solid #000; border-width: 0 3px 3px 0; transform: rotate(45deg); }
.verification.done { background: #F0FAF0; border-color: #155515; }
.verification.done .verification-btn { background: #1F7A1F; color: #fff; border-color: #1F7A1F; }
.verification.done .verification-btn:hover { background: #155515; }
.verification.done .verification-btn::before { content: "OK  "; font-size: 10px; }
.final-card.done { background: #F0FAF0; border-color: #1F7A1F; }
.final-card.done .final-num { background: #1F7A1F; color: #fff; }
.final-card.done .final-check-btn { background: #1F7A1F; color: #fff; border-color: #1F7A1F; }

/* ============ 5. RESPONSIVE ============ */
@media (max-width: 980px) {
  .pdf-download-btn { top: 12px; left: 12px; padding: 9px 14px; font-size: 11px; box-shadow: 3px 3px 0 #000; }
  /* Pe mobil, buton "continua pas" e bandă fixed jos full-width */
  .nav-next-btn.show { left: 0; right: 0; width: auto; padding: 14px 18px; }
  .app-grid { display: block; padding-right: 0; }
  .side-nav { right: 0; transform: translateX(100%); transition: transform .3s ease; z-index: 180; width: 280px; }
  .side-nav.open { transform: translateX(0); }
  .mobile-nav-toggle { display: flex; align-items: center; justify-content: center; }
  .cover { text-align: left; padding-top: 72px; }
  .anomaly-grid { grid-template-columns: 1fr; }
  .wow-strip { flex-direction: column; align-items: flex-start; gap: 12px; }
  .wow-number { text-align: left; min-width: 0; }
  .scroll-top-btn { right: 16px; bottom: 70px; width: 34px; height: 34px; font-size: 15px; }
}
@media (max-width: 700px) {
  .cover { padding: 64px 20px 24px; }
  .pdf-download-btn { top: 18px; left: 18px; padding: 5px 9px; font-size: 9.5px; box-shadow: 2px 2px 0 #000; }
  .pdf-arrow { font-size: 10px; }
  .cover-meta { padding: 14px 18px; }
  .cover-meta-row { grid-template-columns: 1fr; gap: 4px; padding: 10px 0; }
  .mantra-band { padding: 26px 20px; }
  .mobile-nav-toggle { top: 14px; right: 14px; width: 40px; height: 40px; }
  .exec-hero-panel { padding: 36px 20px; }
  .wow-strip { padding: 26px 20px; }
  .section, .final-exec-section, .next-section { padding: 32px 20px 22px; }
  .stage-header { padding: 18px 16px; }
  .stage-header-grid { gap: 12px; }
  .stage-number { font-size: 36px; }
  .stage-info-badges { margin-top: 8px; }
  .hook-local { flex-direction: column; }
  .hook-local b, .hook-local i { font-size: 11px; padding: 7px 12px; }
  .hook-local i { border-left: 1px solid #FFE680; border-top: none; }
  .stage-badge { font-size: 9px; padding: 4px 9px; }
  .stage-toggle { width: 30px; height: 30px; font-size: 15px; }
  .stage-body { padding: 22px 16px 24px; }
  .step { padding: 18px 16px; }
  .prompt-box { padding: 18px 16px; }
  .prompt-text { padding: 14px; font-size: 14px; }
  .copy-btn { font-size: 12px; padding: 12px 18px; }
  .anomaly-grid { grid-template-columns: 1fr; }
  .data-table thead th, .data-table tbody td { padding: 10px; font-size: 13px; }
  .ba-grid { grid-template-columns: 1fr; }
  .ba-before { border-right: none; border-bottom: 2px solid #000; }
  .ba-col { padding: 22px 18px; }
  .final-grid { grid-template-columns: 1fr; gap: 10px; }
  .payoff-section { padding: 44px 20px; }
  .payoff-num .pn { padding: 14px 0; margin-right: 20px; }
  .footer { padding: 24px 20px 90px; }
  .next-section { padding-bottom: 90px; }
  .completion-badge { padding: 28px 20px; }
  .scroll-top-btn { bottom: 64px; right: 14px; width: 42px; height: 42px; font-size: 19px; }
}
@media (max-width: 380px) {
  .cover { padding: 64px 16px 22px; }
  .section, .final-exec-section, .next-section { padding: 28px 16px 18px; }
  .stage-header { padding: 16px 14px; }
  .stage-number { font-size: 32px; }
  .stage-body { padding: 18px 14px 20px; }
  .step { padding: 16px 14px; }
  .prompt-box { padding: 16px 12px; }
}
@media (min-width: 701px) and (pointer: coarse) {
  .app-grid { padding-right: 0; }
  .side-nav { right: 0; transform: translateX(100%); transition: transform .3s ease; z-index: 180; width: 320px; }
  .side-nav.open { transform: translateX(0); }
  .mobile-nav-toggle { display: flex; align-items: center; justify-content: center; top: 30px; right: 30px; width: 49px; height: 49px; font-size: 22px; }
  .cover { text-align: left; }
}
"""

STAGES = [
 dict(n=1, name="REALITATE", label="ETAPA 1 · CONFRUNTAREA CU HAOSUL", energy="Manual", phase="INPUT", transition='Acum vedem haosul. Dar încă nu știm exact ce e ambalaj.',
   emotion="Disconfort. Suspiciune. Ceva nu e în regulă.",
   hook="Ochiul vede tabel. Sistemul vede haos.",
   quote="Deschizi exportul ERP. Pare un tabel ordonat. Fixezi referința înainte să atingi orice.",
   summary="Scop: expui haosul structural fără cosmetizare și fixezi punctul de referință care nu trebuie să se schimbe.",
   steps=[
     ("Deschide exportul ERP brut", "Dublu-click pe INPUT-Excel-01-Structura.xlsx, foaia Date. 2.062 rânduri care arată ca un tabel curat. Citește foaia _REALITATE."),
     ("Privește structura, nu conținutul", "Antet de raport pe primele 3 rânduri. Subtotaluri inserate între categorii. Blank-uri false. Un TOTAL GENERAL la final. Ochiul vede tabel. Structura nu e tabel."),
     ("Fixează suma de referință", "Selectează coloana valoare_neta. Citește SUM din status bar: %s lei. Acest număr este martorul. Dacă se schimbă după transformare, ceva s-a pierdut." % SUMA),
   ],
   decision=("dark","HAOS, NU EROARE","Datele sunt corecte. Ambalajul nu este. Înainte de orice calcul, structura trebuie să fie reală. C01 nu repară cifre. Reconstruiește continuitatea."),
   verif=("VERIFICAREA ETAPEI 1 · REFERINȚĂ FIXATĂ",
     ["Fișier INPUT deschis pe foaia Date, 2.062 rânduri vizibile",
      "Ambalajul identificat vizual: antet, subtotaluri, blank-uri, total",
      "Suma de control %s lei notată din SUM clasic" % SUMA,
      "Referința fixată: orice transformare se măsoară față de ea"],
     "VERIFICĂ ETAPA 1"),
   wow=("61","din 2.062 de rânduri nu sunt tranzacții.","Sunt ambalaj care arată exact ca date.","main"),
 ),
 dict(n=2, name="INVESTIGATIE", label="ETAPA 2 · ÎNȚELEGERE ASISTATĂ DE AI", energy="Promptul 1", phase="AI", transition='Acum știm ce este ambalaj. Putem transforma.',
   emotion="Claritate care se ridică. Începi să înțelegi ce vezi.",
   hook="Înainte să calculezi, dovedește că ai date.",
   quote="Nu reparăm încă. Întâi înțelegem. Promptul natural este instrument de investigație, nu comandă.",
   summary="Scop: operatorul investighează exportul asistat de AI și înțelege exact ce e ambalaj, înainte de orice transformare.",
   steps=[
     ("Activează Copilot pe foaia Date", "Deschide Copilot în panoul lateral Excel, pe foaia Date. Nu ceri nicio modificare. Doar investighezi."),
     ("Rulează Promptul 1 de investigație", "Lipești promptul de mai jos. AI analizează structura și raportează numeric, fără să atingă o singură celulă."),
     ("Citește raportul de structură", "AI întoarce harta exactă: ce e antet, ce e subtotal, ce e gol fals, unde începe tabelul real. Acum știi, nu bănuiești."),
   ],
   prompt=("PROMPT 1 · INSTRUMENT DE INVESTIGAȚIE",
     "Mă uit la acest fișier și pare un tabel normal, dar bănuiesc că nu este. Verifică structura și spune-mi: ce nu ar trebui să fie aici dacă ar fi un tabel curat? Numără pe categorii. Nu modifica nimic, doar raportează."),
   table=("RAPORT AI · STRUCTURĂ INVESTIGATĂ (NIMIC MODIFICAT)",
     ["#","Categorie structurală","Rânduri","Status"],
     [["1","Antet de raport","3","ambalaj"],
      ["2","Antet real tabel","1 (rândul 4)","reper"],
      ["3","Subtotaluri pe categorie","4","ambalaj"],
      ["4","Total general","1","ambalaj"],
      ["5","Blank-uri false","53","ambalaj"],
      ["6","Tranzacții reale","2.000","date"]]),
   capcana="Investigația nu repară. Investigația înțelege. Cine sare direct la transformare repară lucruri pe care nu le-a înțeles și le strică altfel.",
   verif=("VERIFICAREA ETAPEI 2 · STRUCTURĂ ÎNȚELEASĂ",
     ["Promptul 1 rulat, datele complet neatinse",
      "Total ambalaj cuantificat = 61 rânduri",
      "2.000 tranzacții reale confirmate de AI",
      "Antetul real localizat exact: rândul 4"],
     "VERIFICĂ ETAPA 2"),
   wow=("2.000","tranzacții reale, confirmate.","Fără să fi atins fișierul. Întâi înțelegi, apoi transformi.","secondary"),
 ),
 dict(n=3, name="TRANSFORMARE", label="ETAPA 3 · RECONSTRUCȚIE STRUCTURALĂ", energy="Power Query", phase="PQ", transition='Acum fluxul există. Dar nu avem încă voie să avem încredere.',
   emotion="Putere. Haosul începe să se organizeze sub control.",
   hook="Nu reparăm cifre. Reparăm structura.",
   quote="Cu realitatea înțeleasă, reconstruim continuitatea. Power Query ca motor de maturizare, nu ca buton.",
   summary="Scop: ambalajul dispare, cele 14 coloane reale rămân stabile, nicio tranzacție reală nu e atinsă.",
   steps=[
     ("Încarcă exportul în Power Query", "Date > Obține date > Din tabel/interval. Exportul intră ca sursă în editorul Power Query. Sursa brută rămâne intactă pentru trasabilitate."),
     ("Rulează Promptul 2 de reconstrucție", "Lipești promptul pentru pașii M: skip 3 rânduri, promovează antet, filtrează SUBTOTAL/TOTAL, elimină rânduri goale, păstrează cele 14 coloane."),
     ("Aplică și încarcă tabelul curat", "Power Query execută pașii. 2.062 devine 2.000. Cele 14 coloane rămân. Închide și încarcă ca tabel Excel curat pe foaie nouă."),
   ],
   prompt=("PROMPT 2 · INSTRUMENT DE TRANSFORMARE CONTROLATĂ",
     "Acum că știi exact ce e în plus, ajută-mă să curăț fișierul. Construiește un flux repetabil care păstrează doar tranzacțiile reale și antetul corect. Vreau să pot reaplica același flux luna viitoare, când iau alt export. Folosește Power Query."),
   table=("BEFORE / AFTER · TRANSFORMAREA STRUCTURALĂ",
     ["#","Indicator","Înainte","După"],
     [["1","Total rânduri","2.062","2.000"],
      ["2","Rânduri ambalaj","61","0"],
      ["3","Coloane reale","14","14"],
      ["4","Continuitate tabel","ruptă","stabilă"],
      ["5","SUM valoare_neta","%s" % SUMA,"%s" % SUMA]]),
   capcana="Cine șterge manual subtotaluri rând cu rând reface aceeași muncă la fiecare export nou. Un flux o face o dată și apoi se repetă singur.",
   verif=("VERIFICAREA ETAPEI 3 · STRUCTURĂ RECONSTRUITĂ",
     ["Flux Power Query construit cu pașii M corecți",
      "2.062 rânduri brute → 2.000 tranzacții reale",
      "14 coloane reale păstrate, niciuna pierdută",
      "Tabel curat încărcat pe foaie nouă, sursă intactă"],
     "VERIFICĂ ETAPA 3"),
   wow=("2.062 → 2.000","Același fișier. Aceeași sumă.","Dar acum Excel îl înțelege.","main"),
 ),
 dict(n=4, name="VERIFICARE", label="ETAPA 4 · ÎNCREDERE CÂȘTIGATĂ", energy="AGGREGATE", phase="CONTROL", transition='Acum suma este conservată. Urmează testul real: repetabilitatea.',
   emotion="Suspiciune controlată care devine încredere dovedită.",
   hook="Un flux care a rulat nu e un flux corect.",
   quote="Nu avem încredere oarbă în flux. Verificăm efectul, nu doar că a rulat.",
   summary="Scop: dovedim numeric că suma s-a conservat și nicio tranzacție reală nu s-a pierdut pe drum.",
   steps=[
     ("Recalculează suma pe tabelul curat", "SUM pe valoare_neta în tabelul curat: %s lei. Compară cu martorul fixat în Etapa 1." % SUMA),
     ("Confruntă SUM cu AGGREGATE", "AGGREGATE(9;...) pe aceeași coloană. Pe datele murdare SUM prindea și subtotalurile. Acum SUM = AGGREGATE. Aceeași poveste numerică."),
     ("Verifică integritatea referențială", "Fiecare cod client din tabel există în nomenclatorul CLIENTI. 0 referințe lipsă. 2.000 rânduri, 14 coloane confirmate."),
   ],
   table=("CONTROL NUMERIC · DOVADA INTEGRITĂȚII",
     ["#","Verificare","Așteptat","Rezultat"],
     [["1","SUM valoare_neta","%s" % SUMA,"%s ✓" % SUMA],
      ["2","SUM = AGGREGATE","egale","egale ✓"],
      ["3","Număr rânduri","2.000","2.000 ✓"],
      ["4","Număr coloane","14","14 ✓"],
      ["5","Referințe clienți lipsă","0","0 ✓"]]),
   capcana="Un flux care a rulat nu înseamnă un flux corect. Fără verificarea sumei, ai putea pierde rânduri reale fără să observi niciodată.",
   verif=("VERIFICAREA ETAPEI 4 · INTEGRITATE CONFIRMATĂ",
     ["SUM pe tabel curat = %s lei" % SUMA,
      "SUM = AGGREGATE (subtotaluri eliminate)",
      "2.000 rânduri, 14 coloane confirmate",
      "Integritate referință clienți = 0 lipsă"],
     "VERIFICĂ ETAPA 4"),
   wow=("%s" % SUMA,"Suma nu s-a clintit.","Structura s-a eliberat. Valoarea a rămas exactă.","secondary"),
 ),
 dict(n=5, name="STABILIZARE", label="ETAPA 5 · CALM OPERAȚIONAL", energy="Refresh", phase="REFRESH", transition='Acum nu mai reparăm fișierul. Avem sistem.',
   emotion="Calm. Sistemul rezistă fără tine.",
   hook="Un tabel fals produce decizii false. La fiecare lună.",
   quote="Transformarea nu e o intervenție unică. O facem repetabilă, ca să nu se mai întoarcă haosul.",
   summary="Scop: același flux rezistă la următorul export, fără intervenție manuală, fără panică la final de lună.",
   steps=[
     ("Leagă fluxul la sursă ca mecanism", "Fluxul Power Query rămâne conectat la sursă. La un export nou cu aceeași structură, un singur Refresh reconstruiește totul."),
     ("Testează un refresh simulat", "Înlocuiește sursa cu un export nou de structură identică. Date > Reîmprospătează tot. Rezultatul se reconstruiește identic, zero clic manual."),
     ("Documentează regula anti-recurență", "Notează în fișier structura ERP cunoscută și pașii fixați. O abatere de structură oprește fluxul vizibil, nu silențios."),
   ],
   slogan=MANTRA,
   capcana="Improvizația pe fiecare fișier nu scalează. Un mecanism stabil rezistă la export după export, lună după lună.",
   verif=("VERIFICAREA ETAPEI 5 · MECANISM STABIL",
     ["Flux Power Query legat la sursă, refreshabil",
      "Refresh simulat reconstruiește rezultatul identic",
      "Regula anti-recurență documentată în fișier",
      "Zero intervenție manuală la export nou"],
     "VERIFICĂ ETAPA 5"),
   wow=("1 Refresh","Export nou luna viitoare?","Un singur Refresh. Și haosul nu se mai întoarce.","main"),
 ),
 dict(n=6, name="CONFIRMARE", label="ETAPA 6 · PAYOFF", energy="Cap-coadă", phase="BI-READY", transition='Structura este eliberată. C02 poate începe.',
   emotion="Payoff. Sistemul funcționează. Ești în control.",
   hook="Arată ca tabel. Acum chiar este.",
   quote="Construcția e validată operațional. Verificăm sistemul cap-coadă și predăm baza mai departe.",
   summary="Scop: certifici că baza e BI-ready, refreshabilă, pregătită pentru C02 Controlul datelor.",
   steps=[
     ("Verifică sistemul cap-coadă", "2.062 rânduri brute → 2.000 tranzacții reale. 14 coloane stabile. %s lei conservați. Tabel curat, refreshabil." % SUMA),
     ("Confirmă baza BI-ready", "Tabelul curat poate intra direct în calcul, analiză, dashboard, fără să amplifice haos. Structura nu mai minte."),
     ("Predă către C02", "Baza stabilă e pregătită pentru C02 Controlul datelor: separarea valid tehnic de corect operațional."),
   ],
   decision=("dark","SISTEM VALIDAT","Structura a fost eliberată fără să pierzi o tranzacție. Baza nu mai induce în eroare calculul, analiza sau dashboard-ul. Aici se termină haosul structural."),
   verif=("VERIFICAREA ETAPEI 6 · BAZĂ BI-READY",
     ["Sistem verificat cap-coadă: 2.062 → 2.000",
      "14 coloane stabile, %s lei conservați" % SUMA,
      "Bază BI-ready: poate intra în calcul/analiză/dashboard",
      "Pregătit pentru C02 Controlul datelor"],
     "VERIFICĂ ETAPA 6"),
   wow=("2.000 / 2.000", WOW6, "Toate tranzacțiile reale, păstrate. Zero atinse.","main"),
 ),
]

FINALS = [
 ("CONTROL", "OUTPUT-Excel-01-Structura.xlsx există și se deschide"),
 ("VOLUM", "2.062 rânduri brute la intrare"),
 ("VOLUM", "2.000 tranzacții reale la ieșire"),
 ("STRUCTURĂ", "14 coloane reale păstrate"),
 ("AMBALAJ", "61 rânduri ambalaj eliminate"),
 ("SUMĂ", "SUM valoare_neta = %s lei" % SUMA),
 ("SUMĂ", "SUM = AGGREGATE (subtotaluri excluse)"),
 ("REFERINȚĂ", "Integritate clienți = 0 referințe lipsă"),
]

ALL_STEPS, STAGE_STEPS = [], {}
sid = 0
for st in STAGES:
    ids = []
    for _ in st["steps"]:
        sid += 1; ids.append(sid); ALL_STEPS.append(sid)
    STAGE_STEPS[st["n"]] = ids



def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wow_html(w):
    num, title, sub, kind = w
    cls = " secondary" if kind == "secondary" else ""
    return ('<div class="wow-strip%s"><div class="wow-number">%s</div>'
            '<div><div class="wow-title">%s</div>'
            '<div class="wow-sub">%s</div></div></div>'
            % (cls, esc(num), esc(title), esc(sub)))


def table_html(t):
    title, head, rows = t
    h = '<div class="data-table-wrap"><table class="data-table"><thead><tr>'
    for c in head:
        h += '<th>%s</th>' % esc(c)
    h += '</tr></thead><tbody>'
    for r in rows:
        h += '<tr>'
        for i, c in enumerate(r):
            cls = ""
            cv = c
            if "✓" in c:
                cls = ' class="good"'
            elif i >= 2 and any(k in c for k in ["ambalaj", "ruptă"]):
                cls = ' class="bad"'
            h += '<td%s>%s</td>' % (cls, esc(cv))
        h += '</tr>'
    h += '</tbody></table></div>'
    return ('<div class="section-marker">%s</div>%s' % (esc(title), h))


parts = []
parts.append('<!DOCTYPE html>\n<html lang="ro">\n<head>\n<meta charset="UTF-8">\n')
parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
parts.append('<title>C01 · Structura Tabelelor · Trainity</title>\n<style>%s</style>\n</head>\n<body>\n' % CSS)
parts.append('<button class="mobile-nav-toggle" onclick="toggleMobileNav()" aria-label="Meniu">&#9776;</button>\n')
parts.append('<div class="mobile-nav-overlay" id="navOverlay" onclick="toggleMobileNav()"></div>\n')
parts.append('<div class="book-app"><div class="app-grid">\n')

# SIDEBAR (dreapta, negru)
parts.append('<nav class="side-nav" id="sideNav">\n')
parts.append('<div class="side-nav-brand"><div class="side-nav-label">PACK 02 EXCEL · C01</div>'
             '<div class="side-nav-title">STRUCTURA TABELELOR</div></div>\n')
parts.append('<div class="nav-controls">'
             '<button class="nav-ctrl-btn" onclick="resetProgress()">RESETEAZĂ PROGRES</button>'
             '<button class="nav-ctrl-btn" onclick="clearHighlights()">ȘTERGE EVIDENȚIERILE</button></div>\n')
parts.append('<div class="nav-progress-mini"><div class="nav-progress-track">'
             '<div class="nav-progress-fill" id="navProgressFill"></div></div>'
             '<div class="nav-progress-stat"><span id="navStepStat">0 / %d pași</span>'
             '<span id="navFinalStat">0 / 8 final</span></div></div>\n' % len(ALL_STEPS))
parts.append('<div class="nav-summary"><div class="nav-summary-row">'
             '<span class="nav-summary-k">ETAPĂ ACTIVĂ</span>'
             '<span class="nav-summary-v" id="navActiveStage">1 · REALITATE</span></div>'
             '<div class="nav-summary-row"><span class="nav-summary-k">PAȘI VALIDAȚI</span>'
             '<span class="nav-summary-v" id="navStepsValidated">0 / %d</span></div></div>\n' % len(ALL_STEPS))
parts.append('<div class="nav-section-label">6 ETAPE</div>\n')
for st in STAGES:
    parts.append('<div class="nav-item" data-stage-link="%d" onclick="navigateStage(%d)">'
                 '<div class="nav-item-row"><div class="nav-item-num">%d</div>'
                 '<div class="nav-item-text">%s<div class="nav-item-meta">%d pași · %s</div></div>'
                 '</div></div>\n' % (st["n"], st["n"], st["n"], st["name"], len(st["steps"]), st["energy"]))
parts.append('<div class="nav-section-label">8 VERIFICĂRI FINALE</div>\n')
parts.append('<div class="nav-final-grid">\n')
for i in range(1, 9):
    parts.append('<div class="nav-final-dot" data-final-link="%d" onclick="navigateFinal(%d)">%d</div>\n' % (i, i, i))
parts.append('</div>\n')
parts.append('</nav>\n')
parts.append('<button class="nav-next-btn" id="floatingNext" onclick="goToNextStep()">'
             '<span id="floatingNextLabel">CONTINUĂ CU PASUL 01</span></button>\n')

parts.append('<main class="main-content">\n')

# COVER
parts.append('<div class="cover">\n')
parts.append('<button class="pdf-download-btn" onclick="window.print()" '
             'aria-label="Descarcă PDF" title="Descarcă PDF (Salvează ca PDF în dialogul de print)">'
             '<span class="pdf-arrow">&#8595;</span> DESCARCĂ PDF</button>\n')
parts.append('<div class="cover-label">PACK 02 EXCEL · TREAPTA 1 STRUCTURA · '
             '<span class="cover-label-pill">CONSTRUCȚIA C01</span></div>\n')
parts.append('<div class="cover-title">STRUCTURA TABELELOR</div>\n')
parts.append('<div class="cover-subtitle-main">%s</div>\n' % esc(HOOK))
parts.append('<div class="cover-miza">O decizie corectă pe date structurate greșit '
             'rămâne o decizie greșită.</div>\n')
parts.append('<div class="cover-meta">')
for k, v in [
    ("TREAPTA 1", '<b>STRUCTURA</b>, CONTROL, AUDIT, NORMALIZE (SCAN)'),
    ("CONSTRUCȚIE", "01 din 20 · PACK 02 - EXCEL"),
    ("INPUT", '<a class="meta-link" href="INPUT-Excel-01-Structura.xlsx" download>INPUT-Excel-01-Structura.xlsx</a>'),
    ("OUTPUT", '<a class="meta-link" href="OUTPUT-Excel-01-Structura.xlsx" download>OUTPUT-Excel-01-Structura.xlsx</a>'),
    ("PPT EXEC", '<a class="meta-link" href="PPT-Excel-01-Structura.pptx" download>PPT-Excel-01-Structura.pptx</a>'),
    ("AI INTEGRAT", "2 prompturi Copilot · 61 rânduri ambalaj eliminate"),
    ("SUMĂ DE CONTROL", "<b>%s lei</b>" % SUMA),
]:
    parts.append('<div class="cover-meta-row"><span>%s</span>'
                 '<span class="meta-value">%s</span></div>' % (k, v))
parts.append('</div>\n</div>\n')

# EXEC HERO - deschiderea tensiunii (REALITATE macro)
parts.append('<div class="exec-hero-panel">\n')
parts.append('<div class="exec-kicker">DE CE C01 · ÎNAINTE DE ORICE CALCUL</div>\n')
parts.append('<h2>Exportul ERP pare tabel. Nu este.</h2>\n')
parts.append('<p class="exec-sharp">Problema nu este că datele sunt greșite. Problema este că Excel nu știe unde încep datele.</p>\n')
parts.append('<p>Are subtotaluri, anteturi de raport, blank-uri false, un total general numărat ca dată. '
             'Orice calcul, analiză sau dashboard construit peste această structură moștenește haosul și îl amplifică. '
             'C01 nu reconstruiește fișierul. Îl face controlabil.</p>\n')
parts.append('</div>\n')

# MANTRA BAND - galben cu text negru, imediat inainte de Etapa 1
parts.append('<div class="mantra-band"><div class="mantra-band-sub">MANTRA · TRAINITY</div>'
             '<div class="mantra-band-main">%s</div></div>\n' % esc(MANTRA.upper()))

# SCENA REALA - cele 5 fenomene, plasate INAINTE de Etapa 1 (revelatie post-deschidere)
parts.append('<div class="section-marker">SCENA REALĂ · CE PARE DATĂ DAR ESTE AMBALAJ</div>\n')
parts.append('<div class="anomaly-grid">')
for a in ANOMALII:
    parts.append('<div class="anomaly-card"><span>%s</span><b>%s</b><p>%s</p></div>'
                 % (esc(a[0]), esc(a[1]), esc(a[2])))
parts.append('</div>\n')

# STAGES
for idx, st in enumerate(STAGES):
    step_ids = STAGE_STEPS[st["n"]]
    open_cls = " open" if idx == 0 else ""
    parts.append('<div class="stage%s" id="stage-%d" data-stage="%d">\n' % (open_cls, st["n"], st["n"]))
    parts.append('<div class="stage-header" onclick="toggleStage(%d)">\n' % st["n"])
    parts.append('<div class="stage-header-quote">%s</div>\n' % esc(st["quote"]))
    parts.append('<div class="stage-header-grid">'
                 '<div class="stage-number">%d</div>'
                 '<div class="stage-info"><div class="stage-info-label">%s</div>'
                 '<div class="stage-info-name">%s</div>'
                 '<div class="stage-info-meta"><span class="phase-tag">%s</span> %s · %d pași</div>'
                 '<div class="stage-info-badges">'
                 '<span class="stage-badge" data-badge="%d">NEÎNCEPUT</span></div></div>'
                 '<div class="stage-toggle">&#9662;</div></div>\n'
                 % (st["n"], esc(st["label"]), st["name"], esc(st["phase"]), st["energy"], len(st["steps"]), st["n"]))
    parts.append('<div class="stage-progress" data-stage-progress="%d"></div>\n' % st["n"])
    parts.append('</div>\n')
    parts.append('<div class="stage-body">\n')
    # HOOK local + emotie
    parts.append('<div class="hook-local"><b>%s</b><i>%s</i></div>\n' % (esc(st["hook"] if "hook" in st else HOOK), esc(st["emotion"])))
    parts.append('<div class="stage-exec-summary">%s</div>\n' % esc(st["summary"]))
    # DEMO: pasi
    for j, (title, action) in enumerate(st["steps"]):
        step_id = step_ids[j]
        parts.append('<div class="step" data-step="%d">'
                     '<div class="step-head"><div class="step-head-content">'
                     '<div class="step-num">Pasul %02d</div>'
                     '<div class="step-title">%s</div></div>'
                     '<div class="step-check" onclick="toggleStep(%d)" title="Marchează pasul ca verificat"></div>'
                     '</div><div class="step-body"><p class="step-action">%s</p></div></div>\n'
                     % (step_id, step_id, esc(title), step_id, esc(action)))
    # INVESTIGATIE: prompt-box (unde exista)
    if "prompt" in st:
        pl, pt = st["prompt"]
        parts.append('<div class="prompt-box"><div class="prompt-label">%s</div>'
                     '<div class="prompt-text">%s</div>'
                     '<button class="copy-btn" onclick="copyPrompt(this)">COPIAZĂ PROMPTUL</button></div>\n'
                     % (esc(pl), esc(pt)))
    # SCENA: data-table (anomaly-grid e plasat autonom inainte de stages)
    if "table" in st:
        parts.append(table_html(st["table"]) + "\n")
    # CONTROL: capcana
    if "capcana" in st:
        parts.append('<div class="capcana"><div class="capcana-label">CAPCANA</div>'
                     '<div class="capcana-text">%s</div></div>\n' % esc(st["capcana"]))
    # REVEAL: decision-block sau slogan
    if "decision" in st:
        kind, lab, txt = st["decision"]
        mc = " mini" if kind == "mini" else ""
        parts.append('<div class="decision-block%s"><div class="decision-label">%s</div>'
                     '<div class="decision-title">%s</div></div>\n' % (mc, esc(lab), esc(txt)))
    if "slogan" in st:
        parts.append('<div class="slogan-box"><div class="slogan-text">%s</div></div>\n' % esc(st["slogan"]))
    # WOW (payoff cinematic al etapei)
    parts.append(wow_html(st["wow"]) + "\n")
    # VERIFICARE
    vl, items, btn = st["verif"]
    parts.append('<div class="verification" data-verif="%d">'
                 '<div class="verif-label">%s</div><ul class="verif-list">'
                 % (st["n"], esc(vl)))
    for it in items:
        parts.append('<li>%s</li>' % esc(it))
    parts.append('</ul><button class="verification-btn" onclick="confirmVerification(%d)">%s</button></div>\n'
                 % (st["n"], esc(btn)))
    if st.get("transition"):
        parts.append('<div class="stage-transition">%s</div>\n' % esc(st["transition"]))
    parts.append('</div>\n</div>\n')

# BEFORE / AFTER (doua panouri dramatice, dupa parcurgerea etapelor)
parts.append('<section class="section compact-section">\n')
parts.append('<div class="section-marker">DOVADA TRANSFORMĂRII</div>\n')
parts.append('<div class="section-title">Înainte era ambalaj. După este sistem.</div>\n')
parts.append('<div class="ba-grid">'
             '<div class="ba-col ba-before"><div class="ba-label">ÎNAINTE</div><ul class="ba-list">'
             '<li>Pare tabel, dar nu este</li>'
             '<li>Conține 61 rânduri ambalaj</li>'
             '<li>Rupe continuitatea datelor</li>'
             '<li>SUM prinde subtotalurile, induce calcule greșite</li>'
             '<li>Nu rezistă la un export nou</li></ul></div>'
             '<div class="ba-col ba-after"><div class="ba-label">DUPĂ</div><ul class="ba-list">'
             '<li>Tabel real, controlabil</li>'
             '<li>2.000 tranzacții reale</li>'
             '<li>14 coloane stabile</li>'
             '<li>SUM = AGGREGATE, sumă conservată</li>'
             '<li>Refreshabil, un singur Refresh</li></ul></div>'
             '</div>\n')
parts.append('</section>\n')
parts.append('<section class="final-exec-section">\n')
parts.append('<div class="section-marker">RITUAL TRAINITY · CONTROL FINAL</div>\n')
parts.append('<div class="section-title">8 verificări finale canonice</div>\n')
parts.append('<div class="section-intro">Înainte de a preda baza către C02, sistemul confirmă fiecare '
             'invariant. Aceleași verificări, aceeași zonă, la fiecare construcție.</div>\n')
parts.append('<div class="final-grid">\n')
for i, (lab, txt) in enumerate(FINALS, 1):
    parts.append('<div class="final-card" data-final="%d"><div class="final-num">%d</div>'
                 '<div class="final-content"><div class="final-label">%s</div>'
                 '<div class="final-text">%s</div>'
                 '<button class="final-check-btn" onclick="confirmFinal(%d)">VERIFICĂ</button>'
                 '</div></div>\n' % (i, i, esc(lab), esc(txt), i))
parts.append('</div>\n')
parts.append('<div class="completion-badge" id="completion"><div class="completion-title">'
             'Bază BI-ready validată.</div><div class="completion-subtitle">'
             'Toate cele 8 verificări finale confirmate. C01 e pregătit pentru C02 Controlul datelor.</div></div>\n')
parts.append('</section>\n')

# NEXT C02 (puntea)
parts.append('<section class="next-section">\n')
parts.append('<div class="section-marker">CE URMEAZĂ</div>\n')
parts.append('<div class="section-title">Structura e stabilă. Acum o controlăm.</div>\n')
parts.append('<div class="next-c02-box"><div class="next-c02-label">TREAPTA 1 · CONSTRUCȚIA URMĂTOARE</div>'
             '<div class="next-c02-name">C02 · CONTROLUL DATELOR</div>'
             '<div class="next-c02-desc">Structura e curată, dar nu tot ce e valid tehnic e și corect '
             'operațional. C02 separă cele două și marchează anomaliile, fără să repare orbește.</div></div>\n')
parts.append('</section>\n')

# PAYOFF CINEMATIC FINAL (inlocuieste identitatea seaca)
parts.append('<section class="payoff-section">\n')
parts.append('<div class="payoff-line dim">Nu am șters date.</div>\n')
parts.append('<div class="payoff-line dim">Nu am adăugat date.</div>\n')
parts.append('<div class="payoff-line dim">Nu am cosmetizat fișierul.</div>\n')
parts.append('<div class="payoff-break"></div>\n')
parts.append('<div class="payoff-key">Am separat realitatea de ambalaj.</div>\n')
parts.append('<div class="payoff-num">'
             '<div class="pn"><span class="pn-v">2.062</span><span class="pn-k">rânduri brute</span></div>'
             '<div class="pn"><span class="pn-v">2.000</span><span class="pn-k">tranzacții reale</span></div>'
             '<div class="pn"><span class="pn-v">61</span><span class="pn-k">ambalaj eliminat</span></div>'
             '<div class="pn"><span class="pn-v">14</span><span class="pn-k">coloane stabile</span></div>'
             '<div class="pn"><span class="pn-v">%s</span><span class="pn-k">lei conservați</span></div>'
             '</div>\n' % SUMA)
parts.append('<div class="payoff-close">Structura este eliberată.<br>C02 poate începe.</div>\n')
parts.append('<div class="payoff-motto">%s</div>\n' % esc(MOTTO))
parts.append('</section>\n')

parts.append('<div class="footer">Sumă de control %s lei · '
             '<span class="footer-brand">TRAINITY</span> · C01 STRUCTURA TABELELOR · '
             'cockpit operațional live</div>\n' % SUMA)
parts.append('</main>\n')
parts.append('</div></div>\n')
parts.append('<button class="scroll-top-btn" id="scrollTopBtn" onclick="scrollToTopTrainity()" '
             'aria-label="Înapoi la început" title="Înapoi la început">&#8593;</button>\n')

# ================= JS: cele 22 functii portate fidel =================

JS = r"""
const STORAGE_KEY = "trainity_c01_structura_state";
const STAGE_STEPS = __STAGE_STEPS__;
const ALL_STEPS = __ALL_STEPS__;
const STAGE_VERIFS = {1:1,2:2,3:3,4:4,5:5,6:6};
function loadState(){try{const r=localStorage.getItem(STORAGE_KEY);if(r)return JSON.parse(r);}catch(e){}return{steps:{},verif:{},final:{},activeStage:1};}
let state=loadState();let activeStage=state.activeStage||1;
function saveState(){try{localStorage.setItem(STORAGE_KEY,JSON.stringify(state));}catch(e){}}
function toggleStage(id){activeStage=(activeStage===id)?0:id;state.activeStage=activeStage;saveState();renderStages();if(activeStage===id){setTimeout(function(){const el=document.getElementById('stage-'+id);if(el)el.scrollIntoView({behavior:'smooth',block:'start'});},50);}}
function toggleStep(id){var wasUnchecked=!state.steps[id];state.steps[id]=!state.steps[id];saveState();render();if(wasUnchecked&&state.steps[id]){setTimeout(function(){for(var k=0;k<ALL_STEPS.length;k++){var sid=ALL_STEPS[k];if(!state.steps[sid]){var el=document.querySelector('[data-step="'+sid+'"]');if(el){el.scrollIntoView({behavior:'smooth',block:'center'});el.style.transition='box-shadow .3s';el.style.boxShadow='0 0 0 3px #FFD400';setTimeout(function(){el.style.boxShadow='';},1500);}return;}}},220);}}
function confirmVerification(id){if(state.verif[id]){state.verif[id]=false;saveState();render();return;}state.verif[id]=true;saveState();render();const nx=parseInt(id)+1;if(nx<=6){setTimeout(function(){activeStage=nx;state.activeStage=activeStage;saveState();renderStages();const el=document.getElementById('stage-'+nx);if(el)el.scrollIntoView({behavior:'smooth',block:'start'});},600);}}
function confirmFinal(id){state.final[id]=!state.final[id];saveState();render();}
function copyPrompt(btn){const box=btn.closest('.prompt-box');const t=box.querySelector('.prompt-text').innerText;const ok=function(){btn.classList.add('copied');btn.textContent='COPIAT  \u2713';setTimeout(function(){btn.classList.remove('copied');btn.textContent='COPIAZĂ PROMPTUL';},2000);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok).catch(function(){fallbackCopy(t,ok);});}else{fallbackCopy(t,ok);}}
function fallbackCopy(text,cb){const ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}document.body.removeChild(ta);cb();}
function navigateStage(id){activeStage=id;state.activeStage=activeStage;saveState();renderStages();const el=document.getElementById('stage-'+id);if(el)el.scrollIntoView({behavior:'smooth',block:'start'});document.getElementById('sideNav').classList.remove('open');document.getElementById('navOverlay').classList.remove('show');}
function navigateFinal(id){const el=document.querySelector('[data-final="'+id+'"]');if(el)el.scrollIntoView({behavior:'smooth',block:'center'});document.getElementById('sideNav').classList.remove('open');document.getElementById('navOverlay').classList.remove('show');}
function goToNextStep(){for(const sid of ALL_STEPS){if(!state.steps[sid]){let tg=1;for(const s in STAGE_STEPS){if(STAGE_STEPS[s].indexOf(sid)>=0){tg=parseInt(s);break;}}if(activeStage!==tg){activeStage=tg;state.activeStage=activeStage;saveState();renderStages();}setTimeout(function(){const el=document.querySelector('[data-step="'+sid+'"]');if(el){el.scrollIntoView({behavior:'smooth',block:'center'});el.style.transition='box-shadow 0.3s';el.style.boxShadow='0 0 0 3px #FFD400';setTimeout(function(){el.style.boxShadow='';},1500);}},100);return;}}for(let i=1;i<=8;i++){if(!state.final[i]){navigateFinal(i);return;}}}
function resetProgress(){if(!confirm('Resetează progresul construcției C01?'))return;state={steps:{},verif:{},final:{},activeStage:1};activeStage=1;saveState();render();}
function toggleMobileNav(){document.getElementById('sideNav').classList.toggle('open');document.getElementById('navOverlay').classList.toggle('show');}
function renderStages(){document.querySelectorAll('.stage').forEach(function(el){const id=parseInt(el.dataset.stage);el.classList.toggle('open',activeStage===id);el.classList.toggle('done',!!state.verif[STAGE_VERIFS[id]]);});document.querySelectorAll('.nav-item').forEach(function(el){const id=parseInt(el.dataset.stageLink);el.classList.toggle('active',activeStage===id);});}
function render(){
 document.querySelectorAll('.step').forEach(function(el){el.classList.toggle('done',!!state.steps[el.dataset.step]);});
 document.querySelectorAll('.verification').forEach(function(el){el.classList.toggle('done',!!state.verif[el.dataset.verif]);});
 document.querySelectorAll('.final-card').forEach(function(el){const d=!!state.final[el.dataset.final];el.classList.toggle('done',d);const b=el.querySelector('.final-check-btn');if(b)b.textContent=d?'VERIFICAT':'VERIFICĂ';});
 for(let s=1;s<=6;s++){const ids=STAGE_STEPS[s]||[];const dn=ids.filter(function(i){return state.steps[i];}).length;const p=ids.length?(dn/ids.length)*100:0;const b=document.querySelector('[data-stage-progress="'+s+'"]');if(b)b.style.width=p+'%';}
 document.querySelectorAll('.nav-item').forEach(function(el){const id=parseInt(el.dataset.stageLink);el.classList.toggle('done',!!state.verif[STAGE_VERIFS[id]]);});
 document.querySelectorAll('.nav-final-dot').forEach(function(el){el.classList.toggle('done',!!state.final[el.dataset.finalLink]);});
 const sd=ALL_STEPS.filter(function(i){return state.steps[i];}).length;
 const fd=Object.keys(state.final).filter(function(k){return state.final[k];}).length;
 const td=sd+fd,ti=ALL_STEPS.length+8;
 document.getElementById('navProgressFill').style.width=Math.round((td/ti)*100)+'%';
 document.getElementById('navStepStat').textContent=sd+' / '+ALL_STEPS.length+' pași';
 document.getElementById('navFinalStat').textContent=fd+' / 8 final';
 document.getElementById('navStepsValidated').textContent=sd+' / '+ALL_STEPS.length;
 var SNAMES={1:'REALITATE',2:'INVESTIGAȚIE',3:'TRANSFORMARE',4:'VERIFICARE',5:'STABILIZARE',6:'CONFIRMARE'};
 var as=activeStage>=1&&activeStage<=6?activeStage:1;
 document.getElementById('navActiveStage').textContent=as+' · '+SNAMES[as];
 document.querySelectorAll('.stage-badge').forEach(function(el){var id=parseInt(el.dataset.badge);var ids=STAGE_STEPS[id]||[];var anyStep=ids.some(function(i){return state.steps[i];});el.classList.remove('working','done');if(state.verif[id]){el.textContent='VALIDAT';el.classList.add('done');}else if(anyStep){el.textContent='ÎN LUCRU';el.classList.add('working');}else{el.textContent='NEÎNCEPUT';}});
 document.getElementById('completion').classList.toggle('show',fd===8);
 const fb=document.getElementById('floatingNext');
 if(td===ti){fb.classList.remove('show');}else{let l='';for(const sid of ALL_STEPS){if(!state.steps[sid]){l='CONTINUĂ CU PASUL '+String(sid).padStart(2,'0');break;}}if(!l){for(let i=1;i<=8;i++){if(!state.final[i]){l='VALIDEAZĂ CONTROLUL '+String(i).padStart(2,'0');break;}}}document.getElementById('floatingNextLabel').textContent=l;fb.classList.add('show');}
 renderStages();
}
function expandAll(){document.querySelectorAll('.stage').forEach(function(el){el.classList.add('open');});}
function collapseAll(){document.querySelectorAll('.stage').forEach(function(el){el.classList.remove('open');});activeStage=0;state.activeStage=0;saveState();}
function resetCurrentStage(){var a=activeStage;if(a<1||a>6){alert('Nicio etapă activă de resetat.');return;}if(!confirm('Resetează doar progresul etapei '+a+'?'))return;(STAGE_STEPS[a]||[]).forEach(function(i){delete state.steps[i];});delete state.verif[a];saveState();render();}
render();
document.addEventListener('mouseup',function(){setTimeout(processSelection,0);});
function processSelection(){const sel=window.getSelection();if(!sel||sel.rangeCount===0||sel.isCollapsed)return;const range=sel.getRangeAt(0);if(range.collapsed)return;const c=range.commonAncestorContainer;const ce=c.nodeType===3?c.parentElement:c;if(!ce.closest('.main-content'))return;if(ce.closest('button, .copy-btn, .verification-btn, .final-check-btn, .step-check, .stage-toggle, .nav-reset-btn, .floating-next, .mobile-nav-toggle, .stage-header'))return;const tn=collectTextNodesInRange(range);if(tn.length===0){sel.removeAllRanges();return;}const wm=[];for(const it of tn){const n=it.node;if(it.startOffset===it.endOffset)continue;if(!n.parentElement)continue;if(n.parentElement.closest('mark.persist'))continue;if(n.parentElement.closest('button, .copy-btn, .verification-btn, .final-check-btn, .step-check, .stage-toggle, .nav-reset-btn, .floating-next, .mobile-nav-toggle, .stage-header'))continue;try{const m=wrapTextNodeRange(n,it.startOffset,it.endOffset);if(m)wm.push(m);}catch(e){}}if(wm.length>0){const nr=document.createRange();nr.setStartBefore(wm[0]);nr.setEndAfter(wm[wm.length-1]);sel.removeAllRanges();sel.addRange(nr);}else{sel.removeAllRanges();}document.body.offsetHeight;}
function collectTextNodesInRange(range){const res=[];const sc=range.startContainer,ec=range.endContainer,so=range.startOffset,eo=range.endOffset;if(sc===ec&&sc.nodeType===3){res.push({node:sc,startOffset:so,endOffset:eo});return res;}const root=range.commonAncestorContainer.nodeType===3?range.commonAncestorContainer.parentNode:range.commonAncestorContainer;const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;while((n=w.nextNode())){if(!nodeIntersectsRange(n,range))continue;let s=0,e=n.nodeValue.length;if(n===sc)s=so;if(n===ec)e=eo;if(s<e)res.push({node:n,startOffset:s,endOffset:e});}return res;}
function nodeIntersectsRange(node,range){const nr=document.createRange();try{nr.selectNodeContents(node);}catch(e){return false;}return range.compareBoundaryPoints(Range.END_TO_START,nr)<=0&&range.compareBoundaryPoints(Range.START_TO_END,nr)>=0;}
function wrapTextNodeRange(tn,so,eo){let t=tn;if(eo<t.nodeValue.length){t.splitText(eo);}if(so>0){t=t.splitText(so);}const m=document.createElement('mark');m.className='persist';m.addEventListener('click',removeMark);t.parentNode.insertBefore(m,t);m.appendChild(t);return m;}
function removeMark(e){e.stopPropagation();const m=this;const p=m.parentNode;while(m.firstChild)p.insertBefore(m.firstChild,m);p.removeChild(m);p.normalize();}
function clearHighlights(){const ms=document.querySelectorAll('mark.persist');if(ms.length===0)return;if(!confirm('Șterge cele '+ms.length+' evidențieri?'))return;ms.forEach(function(m){const p=m.parentNode;while(m.firstChild)p.insertBefore(m.firstChild,m);p.removeChild(m);p.normalize();});}
function scrollToTopTrainity(){window.scrollTo({top:0,behavior:'smooth'});}
"""
JS = JS.replace("__STAGE_STEPS__", _j.dumps({str(k): v for k, v in STAGE_STEPS.items()}))
JS = JS.replace("__ALL_STEPS__", _j.dumps(ALL_STEPS))
parts.append('<script>\n%s\n</script>\n</body>\n</html>\n' % JS)

html = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

import re
print("size:", len(html.encode("utf-8")), "bytes")
print("functii JS:", len(re.findall(r'\bfunction [a-zA-Z]', html)))
print("steps:", len(ALL_STEPS), STAGE_STEPS)
print("copy-btn:", html.count('class="copy-btn"'))
print("anomaly-card:", html.count('anomaly-card'), "data-table:", html.count('class="data-table"'),
      "wow-strip:", html.count('wow-strip'), "decision-block:", html.count('decision-block'),
      "slogan-box:", html.count('slogan-box'), "next-c02:", html.count('next-c02-box'))
print("em-dash:", html.count("\u2014"), "en-dash:", html.count("\u2013"))
import re as _re
bad = [w for w in ["cursant","lec\u021bie","masterclass","webinar","productivitate"] if _re.search(r'\b'+w, html.lower())]
print("cuvinte interzise:", bad if bad else "0")
print("OK")
