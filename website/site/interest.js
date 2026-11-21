/*
 * "What brings you here?" picker (home) and story filter with the same
 * choices (stories index).
 *
 * The choice is kept in localStorage on this device only. Without JavaScript,
 * every interest panel and every story stays visible. On a first visit the home
 * picker opens on the first interest and the story list shows everything;
 * "No preference" shows every panel and every story.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'maicro-interest';
  var PICKER_DEFAULT = 'learn';
  var STORIES_DEFAULT = 'all';
  var INTEREST_LABELS = {
    learn: 'AI & agentic software',
    personal: 'Personal software',
    prototype: 'Prototyping faster',
    agent: 'AI agents'
  };

  function isKnownInterest(value) {
    return value === 'all' || Boolean(INTEREST_LABELS[value]);
  }

  function readInterest(fallback) {
    try {
      var value = window.localStorage.getItem(STORAGE_KEY);
      return isKnownInterest(value) ? value : fallback;
    } catch (error) {
      return fallback;
    }
  }

  function saveInterest(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (error) {
      console.warn('Could not save the interest choice:', error);
    }
  }

  function showPanelFor(picker, interest) {
    var panels = picker.querySelectorAll('.interest-panel');
    Array.prototype.forEach.call(panels, function (panel) {
      panel.hidden = interest !== 'all' && panel.getAttribute('data-interest') !== interest;
    });
  }

  function setUpPicker(picker, note) {
    var options = picker.querySelector('.interest-options');
    var current = readInterest(PICKER_DEFAULT);
    options.hidden = false;
    var selected = options.querySelector('input[value="' + current + '"]');
    if (selected) {
      selected.checked = true;
    }
    showPanelFor(picker, current);
    options.addEventListener('change', function (event) {
      saveInterest(event.target.value);
      showPanelFor(picker, event.target.value);
      if (note) {
        filterStories(note, event.target.value);
      }
    });
  }

  function describeCount(shown) {
    return shown + (shown === 1 ? ' story.' : ' stories.');
  }

  function showAllStories(note) {
    saveInterest('all');
    var noPreference = document.querySelector('.interest-options input[value="all"]');
    if (noPreference) {
      noPreference.checked = true;
    }
    filterStories(note, 'all');
  }

  function filterStories(note, interest) {
    var items = document.querySelectorAll('.story-list > li');
    var shown = 0;
    Array.prototype.forEach.call(items, function (item) {
      var interests = item.getAttribute('data-interests').split(' ');
      var visible = interest === 'all' || interests.indexOf(interest) !== -1;
      item.hidden = !visible;
      shown += visible ? 1 : 0;
    });
    renderFilterNote(note, interest, shown);
  }

  function renderFilterNote(note, interest, shown) {
    note.textContent = '';
    if (interest === 'all') {
      note.textContent = 'All stories · ' + describeCount(shown);
      return;
    }
    note.appendChild(document.createTextNode(INTEREST_LABELS[interest] + ' · ' + describeCount(shown) + ' '));
    var showAll = document.createElement('button');
    showAll.type = 'button';
    showAll.className = 'link-button';
    showAll.textContent = 'Show all stories';
    showAll.addEventListener('click', function () {
      showAllStories(note);
    });
    note.appendChild(showAll);
  }

  function init() {
    var picker = document.querySelector('[data-interest-picker]');
    var note = document.querySelector('[data-story-filter-note]');
    if (picker) {
      setUpPicker(picker, note);
    }
    if (note) {
      filterStories(note, readInterest(STORIES_DEFAULT));
    }
  }

  init();
})();
