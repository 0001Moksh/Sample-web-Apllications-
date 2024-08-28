let index = 0;
displayImages();
function displayImages() {
  let i;
  const images = document.getElementsByClassName("image");
  for (i = 0; i < images.length; i++) {
    images[i].style.display = "none";
  }
  index++;
  if (index > images.length) {
    index = 1;
  }
  images[index - 1].style.display = "block";
  setTimeout(displayImages, 3000);
}

function aki() {
  const a = document.getElementById('form');
  const change = `
      display : block;
      animation: form 2s;
  `
  a.style.cssText = change;
}

function close() {
  const a = document.getElementById('form');
  const change = `
      display : none;
  `
  a.style.cssText = change;
}
function closePopup() {
  const a = document.getElementById('popup');
  const change = `
      display : none;
  `
  a.style.cssText = change;
}

function popup() {
  const a = document.getElementById('popup');
  const change = `
      display : block;
      animation: popup 1s linear;
  `
  a.style.cssText = change;
}

function closeform() {
  const a = document.getElementById('form');
  const change = `
      display : none;
  `
  a.style.cssText = change;
}

