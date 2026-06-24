(function () {
  function applyTheme(theme) {
    var isDark = theme === 'dark';
    document.body.setAttribute('theme', isDark ? 'dark' : 'light');
    document.body.setAttribute('cfg-theme', isDark ? 'dark' : 'light');
    if (window.localStorage) {
      window.localStorage.setItem('theme', isDark ? 'dark' : 'light');
    }
  }

  var storedTheme = window.localStorage && window.localStorage.getItem('theme');
  if (storedTheme === 'auto') {
    applyTheme('light');
  }

  document.addEventListener('click', function (event) {
    var switcher = event.target.closest && event.target.closest('.theme-switch');
    if (!switcher) return;

    event.preventDefault();
    event.stopImmediatePropagation();
    applyTheme(document.body.getAttribute('theme') === 'dark' ? 'light' : 'dark');
  }, true);
})();
