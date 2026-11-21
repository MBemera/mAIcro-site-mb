/*
 * "Ask your agent" prompt for the mAIcro page.
 *
 * - Any element with [data-copy-prompt] copies the text of <pre id="agent-prompt">.
 *   The hero link also moves to the #ask-agent section.
 * - Visiting with ?prompt=1 or #ask-agent shows the section and tries to copy.
 *   Browsers often refuse to copy without a click, so if that fails the prompt
 *   text is selected instead, ready for Ctrl+C / Cmd+C.
 * - Without JavaScript the prompt stays visible in the <pre> and prompt.txt
 *   can be downloaded, so nothing depends on this file.
 */
(function () {
  'use strict';

  var MSG_COPIED = 'Prompt copied — paste it into your agent.';
  var MSG_SELECTED = "Couldn't copy automatically. The prompt is selected below: press Ctrl+C (or Cmd+C) to copy it.";
  var MSG_DEEP_LINK = 'The prompt is selected below. Press Ctrl+C (or Cmd+C) to copy it, or use the Copy prompt button.';

  var promptEl;
  var statusEl;
  var sectionEl;
  var headingEl;
  var clearTimer;

  function setStatus(message, isWarning) {
    window.clearTimeout(clearTimer);
    statusEl.textContent = message;
    statusEl.classList.toggle('is-warning', Boolean(isWarning));
    if (!isWarning) {
      clearTimer = window.setTimeout(function () {
        statusEl.textContent = '';
      }, 8000);
    }
  }

  function selectPrompt() {
    var selection = window.getSelection();
    var range = document.createRange();
    range.selectNodeContents(promptEl);
    selection.removeAllRanges();
    selection.addRange(range);
  }

  // Fallback for browsers or contexts without the async Clipboard API.
  function legacyCopy(text) {
    var area = document.createElement('textarea');
    var ok = false;
    area.value = text;
    area.setAttribute('readonly', '');
    area.style.position = 'fixed';
    area.style.top = '0';
    area.style.left = '-9999px';
    document.body.appendChild(area);
    area.select();
    try {
      ok = document.execCommand('copy');
    } catch (err) {
      ok = false;
    }
    document.body.removeChild(area);
    return ok;
  }

  // Resolves to true if the prompt reached the clipboard.
  function copyPrompt() {
    var text = promptEl.textContent;
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).then(
        function () { return true; },
        function () { return legacyCopy(text); }
      );
    }
    return Promise.resolve(legacyCopy(text));
  }

  function prefersReducedMotion() {
    return Boolean(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  }

  function showSection(smooth) {
    sectionEl.scrollIntoView({ behavior: smooth && !prefersReducedMotion() ? 'smooth' : 'auto', block: 'start' });
    headingEl.focus({ preventScroll: true });
  }

  function onCopyClick(event) {
    var isLink = event.currentTarget.tagName === 'A';

    // Start the copy while the click still counts as a user gesture.
    copyPrompt().then(function (ok) {
      if (ok) {
        setStatus(MSG_COPIED, false);
      } else {
        selectPrompt();
        setStatus(MSG_SELECTED, true);
      }
    });

    if (isLink) {
      event.preventDefault();
      showSection(true);
      if (window.location.hash !== '#ask-agent' && window.history.pushState) {
        window.history.pushState(null, '', '#ask-agent');
      }
    }
  }

  function arrivedForPrompt() {
    var params = new URLSearchParams(window.location.search);
    return params.get('prompt') === '1' || window.location.hash === '#ask-agent';
  }

  function onDeepLink() {
    showSection(false);
    copyPrompt().then(function (ok) {
      if (ok) {
        setStatus(MSG_COPIED, false);
      } else {
        selectPrompt();
        setStatus(MSG_DEEP_LINK, true);
      }
    });
  }

  function init() {
    promptEl = document.getElementById('agent-prompt');
    statusEl = document.getElementById('prompt-status');
    sectionEl = document.getElementById('ask-agent');
    headingEl = document.getElementById('ask-agent-title');
    if (!promptEl || !statusEl || !sectionEl || !headingEl) {
      return;
    }

    var triggers = document.querySelectorAll('[data-copy-prompt]');
    for (var i = 0; i < triggers.length; i++) {
      triggers[i].hidden = false;
      triggers[i].addEventListener('click', onCopyClick);
    }

    if (arrivedForPrompt()) {
      onDeepLink();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
