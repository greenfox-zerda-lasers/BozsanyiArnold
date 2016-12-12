var photoButtons = document.querySelectorAll('.photos')
var displaySpace = document.querySelector('#currentImage')
var currentPos = 0
var arrowButtons = document.querySelectorAll('.arrows')

// Direct Display Functions

function firstDisplay () { currentPos = 0 }
function secondDisplay () { currentPos = 1 }
function thirdDisplay () { currentPos = 2 }
function fourthDisplay () { currentPos = 3 }

//  Event connection to the display functions

photoButtons[0].addEventListener('click', firstDisplay)
photoButtons[1].addEventListener('click', secondDisplay)
photoButtons[2].addEventListener('click', thirdDisplay)
photoButtons[3].addEventListener('click', fourthDisplay)

// Arrow functions

function theNext () {
  if (currentPos < 3) {
    currentPos++
  } else if (currentPos === 3) {
    currentPos = 0
  }
}
function thePrev () {
  if (currentPos > 0) {
    currentPos--
  } else if (currentPos === 0) {
    currentPos = 3
  }
}

// Arrow function calls

arrowButtons[0].addEventListener('click', thePrev)
arrowButtons[1].addEventListener('click', theNext)

if (currentPos === 3) {
  displaySpace.setAttribute('class', photoButtons[3].getAttribute('class').split(/\s+/).slice(1, 2))
} else if (currentPos === 2) {
  displaySpace.setAttribute('class', photoButtons[2].getAttribute('class').split(/\s+/).slice(1, 2))
} else if (currentPos === 1) {
  displaySpace.setAttribute('class', photoButtons[1].getAttribute('class').split(/\s+/).slice(1, 2))
} else if (currentPos === 0) {
  displaySpace.setAttribute('class', photoButtons[0].getAttribute('class').split(/\s+/).slice(1, 2))
}
