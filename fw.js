const zeroButton = document.getElementById('0-btn');
const oneButton = document.getElementById('1-btn');
const twoButton = document.getElementById('2-btn')
const threeButton = document.getElementById('3-btn');
const fourButton = document.getElementById('4-btn')
const fwContainer = document.getElementById('fw-container');
const fw = document.getElementById('fw');
const exitScreen = document.getElementById('exitscreen');
zeroButton.addEventListener('click', f);
oneButton.addEventListener('click', f);
twoButton.addEventListener('click', f);
threeButton.addEventListener('click', f);
fourButton.addEventListener('click', f);
const mediaDoubleF = new Image(200,200);
mediaDoubleF.src = 'img/mediadbl.png';	
let x;
let y;
let num = 0;

function f() {
  zeroButton.classList.add('hide');
  oneButton.classList.add('hide');
  twoButton.classList.add('hide');
  threeButton.classList.add('hide');
  fourButton.classList.add('hide');  
  x = 0; //[[[*array*]]].sort(() => Math.random() - .5);
  y = 0;
  fwContainer.classList.remove('hide');
}

//function showFramework(fw) {
  //fw.innerHTML = "<img src=" + bgimage.src + " />";
//}

function exitPage() {
  fwContainer.classList.add('hide');
  exitScreen.classList.remove('hide');
  exitScreen.innerHTML = `
      <h2><font color="ffffff"><center><button onclick="home()">Home</button>
      <form><button type="submit" formaction="https://www.github.com/sixie6e">GitHub</button></form></center></h2>`;
}

function home() {
  exitScreen.classList.add('hide');
  num = 0;
  x = 0; //[[[*array*]]].sort(() => Math.random() - .5);
  y = 0;
  f();
}
