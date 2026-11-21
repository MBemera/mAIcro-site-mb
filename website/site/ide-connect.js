/*
 * "Connect your IDE" panel and "Open course in mAIcro" buttons.
 *
 * Mirrors the live maicro.app behaviour: the IDE address is stored only in
 * this browser; the page checks <origin>/health and that the address serves
 * the mAIcro IDE, then opens courses in a named tab via #course=<id>.
 * Credentials are never asked for or sent; sign-in happens inside the IDE.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'maicro-website-ide-address';
  var HEALTH_TEXT = 'mAIcro host is healthy';
  var CHECK_TIMEOUT_MS = 8000;
  var IDE_WINDOW_NAME = 'maicro-ide';

  var panels = [];
  var connectedAddress = null;

  function readAddress() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (error) {
      return null;
    }
  }

  function storeAddress(address) {
    try {
      if (address) {
        window.localStorage.setItem(STORAGE_KEY, address);
      } else {
        window.localStorage.removeItem(STORAGE_KEY);
      }
    } catch (error) {
      throw new Error('The address could not be saved in this browser.');
    }
  }

  function normaliseAddress(input) {
    var url;
    try {
      url = new URL(input.trim());
    } catch (error) {
      throw new Error('Enter a complete address, such as http://localhost:4321.');
    }
    if (url.protocol !== 'http:' && url.protocol !== 'https:') {
      throw new Error('The address must start with http:// or https://.');
    }
    url.hash = '';
    return url.toString();
  }

  function timeoutSignal() {
    return window.AbortSignal && AbortSignal.timeout ? AbortSignal.timeout(CHECK_TIMEOUT_MS) : undefined;
  }

  async function checkIde(address) {
    var url = new URL(address);
    var options = { credentials: 'omit', cache: 'no-store', signal: timeoutSignal() };
    var health = await fetch(new URL('/health', url), options);
    if (!health.ok || (await health.text()).trim() !== HEALTH_TEXT) {
      throw new Error('The address did not respond as a mAIcro host.');
    }
    var page = await fetch(url, options);
    var isIde = page.ok && /<title>\s*mAIcro IDE\s*<\/title>/i.test(await page.text());
    if (!isIde) {
      throw new Error('The mAIcro IDE could not be found at this address.');
    }
  }

  function describeError(error) {
    if (error instanceof TypeError || (error && error.name === 'TimeoutError')) {
      return 'Could not reach the IDE. Check its address and network access. An HTTPS website may require an HTTPS IDE address.';
    }
    return error && error.message ? error.message : 'Could not check the IDE address.';
  }

  function render(message, isWarning) {
    panels.forEach(function (panel) {
      panel.status.textContent = message;
      panel.status.classList.toggle('is-warning', Boolean(isWarning));
      panel.disconnect.hidden = !readAddress();
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-open-course]'), function (button) {
      button.disabled = !connectedAddress;
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-open-course-hint]'), function (hint) {
      hint.hidden = Boolean(connectedAddress);
    });
  }

  async function connect(address) {
    connectedAddress = null;
    render('Checking ' + address + ' …', false);
    try {
      await checkIde(address);
      connectedAddress = address;
      render('Connected to ' + new URL(address).host + '. Course buttons now open in your IDE.', false);
    } catch (error) {
      render(describeError(error), true);
    }
  }

  function openCourse(courseId) {
    if (!connectedAddress) {
      render('Connect to your IDE first.', true);
      return;
    }
    var url = new URL(connectedAddress);
    url.hash = new URLSearchParams({ course: courseId }).toString();
    var ideWindow = window.open('', IDE_WINDOW_NAME);
    if (!ideWindow) {
      render('The browser blocked the IDE tab. Allow pop-ups and try again.', true);
      return;
    }
    ideWindow.opener = null;
    ideWindow.location.href = url.toString();
    ideWindow.focus();
  }

  function setUpPanel(element) {
    var form = element.querySelector('[data-connect-form]');
    var panel = {
      input: form.querySelector('input'),
      status: element.querySelector('[data-connect-status]'),
      disconnect: form.querySelector('[data-disconnect]')
    };
    form.hidden = false;
    panel.input.value = readAddress() || '';
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      try {
        var address = normaliseAddress(panel.input.value);
        storeAddress(address);
        connect(address);
      } catch (error) {
        render(error.message, true);
      }
    });
    panel.disconnect.addEventListener('click', function () {
      storeAddress(null);
      connectedAddress = null;
      panel.input.value = '';
      render('Address forgotten on this device.', false);
    });
    panels.push(panel);
  }

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-ide-connect]'), setUpPanel);
    Array.prototype.forEach.call(document.querySelectorAll('[data-open-course]'), function (button) {
      button.addEventListener('click', function () {
        openCourse(button.getAttribute('data-open-course'));
      });
    });
    var saved = readAddress();
    if (saved) {
      connect(saved);
    } else {
      render('', false);
    }
  }

  init();
})();
