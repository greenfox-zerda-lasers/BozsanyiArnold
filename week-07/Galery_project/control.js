var currentPos = 0
var displaySpace = document.getElementById('currentImage')
var photoButtons = document.getElementsByClassName('photos')
var arrowButtons = document.getElementsByClassName('arrows')

var thePhotos = [
  {link: 'url("pictures/firstpic.jpg")'},
  {link: 'url("pictures/secondpic.jpg")'},
  {link: 'url("pictures/thirdpic.jpg")'},
  {link: 'url("pictures/fourthpic.jpg")'}
]

// show the default picture.

displaySpace.setAttribute('style', 'background-image:' + thePhotos[currentPos].link)

// Set each picture's background.

for (var k = 0; k < thePhotos.length; k++) {
  photoButtons[k].setAttribute('style', 'background-image:' + thePhotos[k].link)
}

// directDisplay is the one function depending on event manipulating the currentPos variable,
// and displaying the rigth indexed picture.

function directDisplay (event) {
  for (var i = 0; i < photoButtons.length; i++) {
    if (event.target === photoButtons[i]) {
      currentPos = i
    }
  }
  displaySpace.setAttribute('style', 'background-image:' + thePhotos[currentPos].link)
}

for (var i = 0; i < photoButtons.length; i++) {
  photoButtons[i].addEventListener('click', directDisplay)
}

function arrowControl (event) {
  if (event.target === arrowButtons[0]) {
    if (currentPos > 0) {
      currentPos--
    } else {
      currentPos = 3
    }
  } else {
    if (currentPos < thePhotos.length - 1) {
      currentPos++
    } else {
      currentPos = 0
    }
  }
  displaySpace.setAttribute('style', 'background-image:' + thePhotos[currentPos].link)
}

for (var n = 0; n < arrowButtons.length; n++) {
  arrowButtons[n].addEventListener('click', arrowControl)
}
