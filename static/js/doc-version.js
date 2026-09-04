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

  function select(idx) {
    document.documentElement.setAttribute('data-docv', idx);
    cfg.idx = idx;
    showState(idx);
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
    var select_ = document.getElementById('R-select-docversion');
    if (!select_) {
      return;
    }
    select_.value = String(cfg.idx);
    showState(cfg.idx);
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
