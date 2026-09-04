/*
 * Documentation version selector for weasis.org.
 *
 * The head partial (layouts/partials/docversion-head.html) has already resolved
 * the reader's version and stamped it on <html data-docv="…">; generated CSS
 * does the filtering. All that is left here is the dropdown: reflect the
 * resolved value, and remember a new choice in localStorage and in the URL so a
 * copied link keeps the selected version.
 */
(function () {
  var cfg = window.WeasisDocVersion;
  if (!cfg) {
    return;
  }

  /* One short line, shown only while the reader is off the current release —
     the dropdown already names the version, so this only has to say that the
     page is being filtered and offer the way back. */
  function showState(idx) {
    var box = document.querySelector('.wv-docv-state');
    if (!box) {
      return;
    }
    var filtered = idx !== cfg.def;
    box.hidden = !filtered;
    var message = box.querySelector('.wv-docv-msg');
    if (message) {
      message.textContent = filtered ? 'Filtered to ' + cfg.ids[idx] + ' \u2014 ' : '';
    }
  }

  /* The badge color says whether the feature is in the reader's version; the
     tooltip should say the same thing in words. Both wordings are emitted by the
     shortcode — `title` for present, `data-v-alt` for missing — so the sentences
     stay next to the rest of the badge text instead of being built here. */
  function retitle(idx) {
    var badges = document.querySelectorAll('.wv-badge[data-v-alt]');
    for (var i = 0; i < badges.length; i++) {
      var badge = badges[i];
      if (!badge.getAttribute('data-v-title')) {
        badge.setAttribute('data-v-title', badge.title);
      }
      var since = badge.getAttribute('data-v-since');
      var until = badge.getAttribute('data-v-until');
      var missing =
        (since !== null && idx < parseInt(since, 10)) ||
        (until !== null && idx > parseInt(until, 10));
      badge.title = missing
        ? badge.getAttribute('data-v-alt')
        : badge.getAttribute('data-v-title');
    }
  }

  function select(idx) {
    document.documentElement.setAttribute('data-docv', idx);
    cfg.idx = idx;
    showState(idx);
    retitle(idx);
    try {
      window.localStorage.setItem(cfg.key, cfg.ids[idx]);
    } catch (e) {
      /* private browsing, storage disabled — the choice just won't persist */
    }
    if (window.history && window.history.replaceState) {
      var url = new URL(window.location.href);
      url.searchParams.set('v', cfg.ids[idx]);
      window.history.replaceState(null, '', url.toString());
    }
  }

  function init() {
    /* The status line and the tooltips describe the reader's version, which the
       head script has already resolved — they must not depend on the selector
       being present. It is absent from the print output, which is still filtered
       by the same CSS, so gating these on it left those pages showing a red
       badge with a tooltip claiming the feature is available. */
    showState(cfg.idx);
    retitle(cfg.idx);

    var select_ = document.getElementById('R-select-docversion');
    if (!select_) {
      return;
    }
    select_.value = String(cfg.idx);
    select_.addEventListener('change', function () {
      var option = select_.options[select_.selectedIndex];
      var archived = option && option.getAttribute('data-url');
      if (archived) {
        window.location.href = archived;
        return;
      }
      select(parseInt(select_.value, 10));
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
