/*
 * Get started page: platform picker and "Copy command" buttons.
 *
 * Without JavaScript all four platform commands stay visible and can be
 * selected by hand.
 */
(function () {
  'use strict';

  var MESSAGE_COPIED = 'Command copied. Paste it into your terminal and follow its prompts.';
  var MESSAGE_SELECTED = "Couldn't copy automatically. The command is selected: press Ctrl+C (or Cmd+C).";

  function detectPlatform() {
    var agent = (navigator.userAgent || '').toLowerCase();
    if (agent.indexOf('windows') !== -1) {
      return 'windows';
    }
    if (agent.indexOf('mac os') !== -1 || agent.indexOf('macintosh') !== -1) {
      return 'mac';
    }
    if (agent.indexOf('linux') !== -1 && agent.indexOf('android') === -1) {
      return 'linux';
    }
    return 'windows';
  }

  function choosePlatform(picker, platform) {
    var buttons = picker.querySelectorAll('.platform-buttons button');
    Array.prototype.forEach.call(buttons, function (button) {
      button.setAttribute('aria-pressed', String(button.getAttribute('data-platform') === platform));
    });
    var panels = picker.querySelectorAll('.platform-panel');
    Array.prototype.forEach.call(panels, function (panel) {
      panel.hidden = panel.getAttribute('data-platform') !== platform;
    });
  }

  function selectText(element) {
    var range = document.createRange();
    range.selectNodeContents(element);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
  }

  async function copyCommand(button, status) {
    var code = button.closest('.platform-panel').querySelector('pre code');
    try {
      await navigator.clipboard.writeText(code.textContent);
      status.textContent = MESSAGE_COPIED;
      status.classList.remove('is-warning');
    } catch (error) {
      selectText(code);
      status.textContent = MESSAGE_SELECTED;
      status.classList.add('is-warning');
    }
  }

  function setUpPicker(picker) {
    var buttonGroup = picker.querySelector('.platform-buttons');
    var status = picker.querySelector('[data-copy-status]');
    buttonGroup.hidden = false;
    buttonGroup.addEventListener('click', function (event) {
      var button = event.target.closest('button[data-platform]');
      if (button) {
        choosePlatform(picker, button.getAttribute('data-platform'));
      }
    });
    Array.prototype.forEach.call(picker.querySelectorAll('[data-copy-command]'), function (button) {
      button.hidden = false;
      button.addEventListener('click', function () {
        copyCommand(button, status);
      });
    });
    choosePlatform(picker, detectPlatform());
  }

  var picker = document.querySelector('[data-platform-picker]');
  if (picker) {
    setUpPicker(picker);
  }
})();
