function DarkMode() {
  if (document.getElementById('darkModeSwitch').checked) {
    var color = '#ffffff'
    var header = document.getElementById('header')
    var container = document.getElementById('container')
    header.style.color=color;
    container.style.backgroundColor=color;
  }
  else {
    //화이트 모드로 바꿔주는 코드
  }
}