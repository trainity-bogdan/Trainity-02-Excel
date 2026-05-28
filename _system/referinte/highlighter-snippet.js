/* ============================================================
   HIGHLIGHTER PERSISTENT (R-V03.59 V34+)
   Inject in HTML-Video, langa scriptul de progres.
   
   Comportament V34:
   1. Selectezi text -> la mouseup, se inveleste in <span.trainity-highlight>
   2. Click pe marcaj -> toggle off (elimina span), DAR previne advance
      la urmatorul slide/frag (capture phase intercepteaza inainte de
      handler-ul stage)
   3. Click pe acelasi loc (acum text plain) -> merge inainte normal
   4. NU mai exista buton Reset (eliminat V34)
   5. Tasta ESC NU mai reseteaza (eliminat V34)
   6. Marcajele salvate in localStorage cu key trainity_c{NN}_video_highlights_v1
   7. La incarcare, marcajele restorate din localStorage
   ============================================================ */

(function() {
  'use strict';

  const SCRIPT_ID = 'trainity-highlighter-v1';
  if (document.getElementById(SCRIPT_ID)) return;

  function detectNN() {
    const m = (document.title + document.body.innerText).match(/C(\d{2})\b/);
    return m ? m[1] : '00';
  }
  const NN = detectNN();
  const STORAGE_KEY = `trainity_c${NN}_video_highlights_v1`;

  function loadHighlights() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return [];
      const data = JSON.parse(raw);
      return Array.isArray(data) ? data : [];
    } catch (e) { return []; }
  }

  function saveHighlights(arr) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(arr)); }
    catch (e) { console.warn('Highlighter: localStorage save failed', e); }
  }

  function wrapSelection() {
    const sel = window.getSelection();
    if (!sel || sel.rangeCount === 0) return null;
    const range = sel.getRangeAt(0);
    const text = sel.toString().trim();
    if (text.length === 0) return null;
    if (isInsideHighlight(range.startContainer) || isInsideHighlight(range.endContainer)) return null;
    if (rangeContainsBlockedElements(range)) return null;

    try {
      const span = document.createElement('span');
      span.className = 'trainity-highlight';
      span.dataset.hlId = Date.now() + '-' + Math.floor(Math.random() * 1000);
      range.surroundContents(span);
      sel.removeAllRanges();
      return span;
    } catch (e) {
      try {
        const content = range.extractContents();
        const span = document.createElement('span');
        span.className = 'trainity-highlight';
        span.dataset.hlId = Date.now() + '-' + Math.floor(Math.random() * 1000);
        span.appendChild(content);
        range.insertNode(span);
        sel.removeAllRanges();
        return span;
      } catch (e2) { return null; }
    }
  }

  function isInsideHighlight(node) {
    let cur = node;
    while (cur) {
      if (cur.nodeType === 1 && cur.classList && cur.classList.contains('trainity-highlight')) return true;
      cur = cur.parentNode;
    }
    return false;
  }

  function rangeContainsBlockedElements(range) {
    const BLOCKED = ['IMG','BUTTON','INPUT','TEXTAREA','SELECT','IFRAME','VIDEO','AUDIO','CANVAS','SVG'];
    const fragment = range.cloneContents();
    for (const tag of BLOCKED) {
      if (fragment.querySelector && fragment.querySelector(tag.toLowerCase())) return true;
    }
    return false;
  }

  function removeHighlight(span) {
    const parent = span.parentNode;
    if (!parent) return;
    while (span.firstChild) parent.insertBefore(span.firstChild, span);
    parent.removeChild(span);
    parent.normalize();
  }

  function getNodePath(node) {
    const parts = [];
    let cur = node;
    while (cur && cur !== document.body) {
      const parent = cur.parentNode;
      if (!parent) break;
      parts.unshift(Array.prototype.indexOf.call(parent.childNodes, cur));
      cur = parent;
    }
    return parts.join('/');
  }

  function getNodeByPath(path) {
    if (!path) return null;
    const parts = path.split('/').map(Number);
    let cur = document.body;
    for (const idx of parts) {
      if (!cur || !cur.childNodes || idx >= cur.childNodes.length) return null;
      cur = cur.childNodes[idx];
    }
    return cur;
  }

  function serializeHighlights() {
    const arr = [];
    document.querySelectorAll('.trainity-highlight').forEach(span => {
      arr.push({
        id: span.dataset.hlId,
        text: span.textContent,
        parentPath: getNodePath(span.parentNode),
        siblingIdx: Array.prototype.indexOf.call(span.parentNode.childNodes, span)
      });
    });
    return arr;
  }

  function restoreHighlights() {
    const arr = loadHighlights();
    if (arr.length === 0) return 0;
    let restored = 0;
    const byParent = {};
    arr.forEach(h => {
      if (!byParent[h.parentPath]) byParent[h.parentPath] = [];
      byParent[h.parentPath].push(h);
    });
    Object.keys(byParent).forEach(parentPath => {
      const items = byParent[parentPath].sort((a, b) => b.siblingIdx - a.siblingIdx);
      const parent = getNodeByPath(parentPath);
      if (!parent) return;
      items.forEach(h => {
        for (let i = 0; i < parent.childNodes.length; i++) {
          const child = parent.childNodes[i];
          if (child.nodeType === 3 && child.textContent.includes(h.text)) {
            const text = child.textContent;
            const idx = text.indexOf(h.text);
            const before = text.substring(0, idx);
            const after = text.substring(idx + h.text.length);
            const span = document.createElement('span');
            span.className = 'trainity-highlight';
            span.dataset.hlId = h.id;
            span.textContent = h.text;
            const frag = document.createDocumentFragment();
            if (before) frag.appendChild(document.createTextNode(before));
            frag.appendChild(span);
            if (after) frag.appendChild(document.createTextNode(after));
            parent.replaceChild(frag, child);
            restored++;
            break;
          }
        }
      });
    });
    return restored;
  }

  function onMouseUp(e) {
    if (e.target && e.target.classList && e.target.classList.contains('trainity-highlight')) return;
    setTimeout(() => {
      const span = wrapSelection();
      if (span) saveHighlights(serializeHighlights());
    }, 10);
  }

  // CAPTURE PHASE - intercepteaza click PE highlight INAINTE de stage handler
  function onClickCapture(e) {
    const t = e.target;
    if (!t) return;
    let hl = t;
    while (hl && hl !== document.body) {
      if (hl.nodeType === 1 && hl.classList && hl.classList.contains('trainity-highlight')) {
        e.preventDefault();
        e.stopPropagation();
        if (typeof e.stopImmediatePropagation === 'function') e.stopImmediatePropagation();
        removeHighlight(hl);
        saveHighlights(serializeHighlights());
        return;
      }
      hl = hl.parentNode;
    }
  }

  function init() {
    const marker = document.createElement('meta');
    marker.id = SCRIPT_ID;
    marker.name = 'trainity-highlighter';
    marker.content = 'v34';
    document.head.appendChild(marker);

    // V34: NU mai exista buton reset, NU mai exista ESC handler
    document.addEventListener('mouseup', onMouseUp);
    document.addEventListener('click', onClickCapture, true); // CAPTURE

    setTimeout(() => {
      const restored = restoreHighlights();
      if (restored > 0) saveHighlights(serializeHighlights());
    }, 100);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
