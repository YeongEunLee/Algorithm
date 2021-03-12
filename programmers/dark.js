const $checkbox = document.querySelector('.check');

$checkbox.addEventListener('click', e=> {
  if (e.target.checked) {             document.documentElement.setAttribute('color-theme', 'dark');
  } else {    document.documentElement.setAttribute('color-theme', 'light');
  }
});