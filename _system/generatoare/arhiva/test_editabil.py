from playwright.sync_api import sync_playwright
import pathlib

URL = "file://" + str(pathlib.Path("/home/claude/brain/livrabile_C01/HTML-EDITABIL-Excel-01-Structura.html").resolve())
P=0; F=0; LOG=[]
def ok(name, cond):
    global P,F
    if cond: P+=1; LOG.append(("PASS",name))
    else: F+=1; LOG.append(("FAIL",name))

def run(pw, label, vw, vh, is_mobile):
    global P,F
    br = pw.chromium.launch()
    ctx = br.new_context(viewport={"width":vw,"height":vh}, is_mobile=is_mobile, has_touch=is_mobile)
    pg = ctx.new_page()
    pg.on("dialog", lambda d: d.accept())
    pg.goto(URL, wait_until="networkidle")
    pg.wait_for_timeout(400)

    pre = f"[{label} {vw}x{vh}] "

    # ---- COCKPIT ----
    # 1. bifare pas + persistenta
    pg.eval_on_selector('.step[data-step="1"] .step-check', "e=>e.click()")
    pg.wait_for_timeout(150)
    done1 = pg.eval_on_selector('.step[data-step="1"]', "e=>e.classList.contains('done')")
    ok(pre+"bifare pas 1", done1)
    # persistenta reload
    pg.reload(wait_until="networkidle"); pg.wait_for_timeout(300)
    persist = pg.eval_on_selector('.step[data-step="1"]', "e=>e.classList.contains('done')")
    ok(pre+"persistenta localStorage dupa reload", persist)
    # 2. contor progres update
    stat = pg.eval_on_selector('#navStepStat', "e=>e.textContent")
    ok(pre+"contor pas actualizat ("+stat+")", "1" in stat)
    # 3. verificare etapa -> badge VALIDAT
    pg.eval_on_selector('.verification[data-verif="1"] .verification-btn', "e=>e.click()")
    pg.wait_for_timeout(150)
    badge = pg.eval_on_selector('.stage-badge[data-badge="1"]', "e=>e.textContent.trim()")
    ok(pre+"badge -> VALIDAT", badge=="VALIDAT")
    # 4. badge IN LUCRU (etapa 2: bifez 1 pas, fara verificare)
    pg.eval_on_selector('.step[data-step="4"] .step-check', "e=>e.click()")
    pg.wait_for_timeout(150)
    b2 = pg.eval_on_selector('.stage-badge[data-badge="2"]', "e=>e.textContent.trim()")
    ok(pre+"badge -> IN LUCRU", b2=="ÎN LUCRU")
    # 5. copy prompt
    cp = pg.query_selector('.copy-btn')
    if cp:
        pg.eval_on_selector('.copy-btn', "e=>e.click()"); pg.wait_for_timeout(200)
        cls = pg.eval_on_selector('.copy-btn', "e=>e.className")
        ok(pre+"copy prompt (clasa copied)", "copied" in cls)
    else:
        ok(pre+"copy prompt prezent", False)
    # 6. scroll-top button
    st = pg.query_selector('#scrollTopBtn')
    ok(pre+"buton scroll-top exista", st is not None)
    if st:
        pg.evaluate("window.scrollTo(0,2000)"); pg.wait_for_timeout(200)
        pg.eval_on_selector('#scrollTopBtn', "e=>e.click()"); pg.wait_for_timeout(1400)
        y = pg.evaluate("window.scrollY")
        ok(pre+"scroll-top duce sus (y="+str(int(y))+")", y < 50)
    # 7. reset progres (buton sus)
    rp = pg.query_selector('button.nav-ctrl-btn')
    ok(pre+"buton reset progres prezent", rp is not None)
    # 8. highlight persistent (selectie text -> mark) - simulez prin functia
    hl = pg.evaluate("typeof clearHighlights==='function' && typeof processSelection==='function'")
    ok(pre+"functii highlight prezente", hl)

    # ---- RESPONSIVE / NAV MOBIL ----
    mt = pg.query_selector('.mobile-nav-toggle')
    mt_visible = pg.eval_on_selector('.mobile-nav-toggle', "e=>getComputedStyle(e).display!=='none'") if mt else False
    if is_mobile or vw<=980:
        ok(pre+"hamburger vizibil pe mobil", mt_visible)
        if mt_visible:
            pg.eval_on_selector('.mobile-nav-toggle', "e=>e.click()"); pg.wait_for_timeout(300)
            navopen = pg.eval_on_selector('#sideNav', "e=>e.classList.contains('open')")
            ok(pre+"nav mobil se deschide", navopen)
            ov = pg.query_selector('.mobile-nav-overlay.show') or pg.query_selector('#navOverlay')
            ok(pre+"overlay nav prezent", ov is not None)
            # inchide nav
            pg.eval_on_selector('#sideNav', "e=>e.classList.remove('open')")
    else:
        ok(pre+"hamburger ASCUNS pe desktop", not mt_visible)
        sn = pg.eval_on_selector('#sideNav', "e=>getComputedStyle(e).position")
        ok(pre+"sidebar fixed pe desktop", sn=="fixed")

    # overflow orizontal (nu trebuie sa existe pe mobil)
    sw = pg.evaluate("document.documentElement.scrollWidth")
    cw = pg.evaluate("document.documentElement.clientWidth")
    ok(pre+f"fara overflow orizontal (sw={sw} cw={cw})", sw <= cw+2)

    # ---- EDITOR WYSIWYG ----
    bar = pg.query_selector('#tr-bar')
    ok(pre+"bara editor #tr-bar", bar is not None)
    fab = pg.query_selector('#tr-fab')
    ok(pre+"FAB editor #tr-fab", fab is not None)
    for bid in ["tr-toggle","tr-undo","tr-redo","tr-restore","tr-save","tr-export","tr-pdf","tr-clear","tr-hidebar"]:
        ok(pre+f"buton #{bid}", pg.query_selector('#'+bid) is not None)
    # toggle editare ON
    ntr_before = pg.evaluate("document.querySelectorAll('[data-tr]').length")
    ok(pre+"0 data-tr inainte de editare", ntr_before==0)
    pg.eval_on_selector('#tr-toggle', "e=>e.click()")
    pg.wait_for_timeout(300)
    ntr = pg.evaluate("document.querySelectorAll('[data-tr]').length")
    ok(pre+f"data-tr aplicat la toggle ({ntr})", ntr>30)
    tron = pg.eval_on_selector('body', "e=>e.classList.contains('tr-on')")
    ok(pre+"body.tr-on activ", tron)
    ce = pg.eval_on_selector('.stage-info-name[data-tr]', "e=>e.isContentEditable")
    ok(pre+"element editabil (isContentEditable real)", ce==True)
    # editez efectiv un text
    pg.eval_on_selector('.stage-info-name[data-tr]', "e=>e.focus()")
    pg.wait_for_timeout(100)
    pg.eval_on_selector('.stage-info-name[data-tr]', "e=>{e.textContent='TEST EDIT';e.dispatchEvent(new Event('input',{bubbles:true}));}")
    pg.wait_for_timeout(120)
    pg.eval_on_selector('.stage-info-name[data-tr]', "e=>e.blur()")
    pg.wait_for_timeout(200)
    val = pg.eval_on_selector('.stage-info-name[data-tr]', "e=>e.textContent")
    ok(pre+"editare text efectiva", val=="TEST EDIT")
    # buton sterge element
    delx = pg.query_selector('.tr-x')
    ok(pre+"buton sterge ✕ prezent", delx is not None)
    # tr-block pe wrapper
    trb = pg.query_selector('.step.tr-block')
    ok(pre+"bloc .step.tr-block", trb is not None)
    # selectori NOI C01 prinsi
    for cls in [".mantra-band-main",".stage-transition",".payoff-key",".hook-local b",".slogan-text"]:
        n = pg.evaluate(f"document.querySelectorAll('{cls}[data-tr]').length")
        ok(pre+f"selector nou {cls} taggat", n>0)
    # SAVE
    pg.eval_on_selector('#tr-save', "e=>e.click()")
    pg.wait_for_timeout(200)
    saved = pg.evaluate("localStorage.getItem('trainity_c01_edits_v3')!==null")
    ok(pre+"salvare localStorage (cheie izolata v3)", saved)
    # UNDO
    undo_enabled = pg.eval_on_selector('#tr-undo', "e=>!e.disabled")
    ok(pre+"undo activabil dupa editare", undo_enabled)
    if undo_enabled:
        pg.eval_on_selector('#tr-undo', "e=>e.click()")
        pg.wait_for_timeout(200)
        rv = pg.eval_on_selector('.stage-info-name[data-tr]', "e=>e.textContent")
        ok(pre+"undo revine la textul original", rv!="TEST EDIT")
    # EXPORT HTML (verific ca produce blob/descarcare)
    exported = pg.evaluate("""()=>{
        let captured=null;
        const _c=URL.createObjectURL; URL.createObjectURL=function(b){captured=b;return 'blob:test';};
        try{ document.getElementById('tr-export').click(); }catch(e){return 'ERR:'+e.message;}
        URL.createObjectURL=_c;
        return captured? 'BLOB_OK('+(captured.size||0)+')':'NO_BLOB';
    }""")
    ok(pre+"export HTML produce blob ("+str(exported)+")", str(exported).startswith("BLOB_OK"))
    # toggle editare OFF (testat INAINTE de export PDF - exportPDF reactiveaza editing la afterprint, by design)
    pg.eval_on_selector('#tr-toggle', "e=>e.click()")
    pg.wait_for_timeout(400)
    troff = pg.eval_on_selector('body', "e=>!e.classList.contains('tr-on')")
    ok(pre+"editare OFF (tr-on scos)", troff)
    # EXPORT PDF (window.print apelat) - stub print
    printed = pg.evaluate("""()=>{
        let called=false; const _p=window.print; window.print=function(){called=true;};
        try{ document.getElementById('tr-pdf').click(); }catch(e){return 'ERR';}
        return new Promise(r=>setTimeout(()=>{window.print=_p; r(called);},600));
    }""")
    ok(pre+"export PDF apeleaza window.print", printed==True)
    pg.wait_for_timeout(700)
    # @media print exista
    hasprint = pg.evaluate("[...document.styleSheets].some(s=>{try{return [...s.cssRules].some(r=>r.media&&String(r.media).includes('print'))}catch(e){return false}})")
    ok(pre+"@media print activ in stylesheet", hasprint)
    # hide bar -> FAB
    pg.eval_on_selector('#tr-hidebar', "e=>e.click()")
    pg.wait_for_timeout(150)
    barhidden = pg.eval_on_selector('#tr-bar', "e=>e.classList.contains('tr-hide')")
    ok(pre+"ascunde bara -> tr-hide", barhidden)

    ctx.close(); br.close()

with sync_playwright() as pw:
    run(pw, "DESKTOP", 1440, 900, False)
    run(pw, "DESKTOP-FHD", 1920, 1080, False)
    run(pw, "MOBIL", 390, 844, True)
    run(pw, "MOBIL-MIC", 360, 740, True)
    run(pw, "TABLETA", 768, 1024, True)

print("\n".join(f"  {s} {n}" for s,n in LOG if s=="FAIL") or "  (niciun FAIL)")
print(f"\n===== {P} PASS / {F} FAIL =====")
