'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function isInString (string, letter) {
  for (var i = 0; i < string.length; i++) {
    if (string[i] === letter) {
      return true
    }
  }return false
}

console.log(isInString('alma','a'))
