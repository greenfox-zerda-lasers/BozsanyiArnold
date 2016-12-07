
'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise
function isPrime (value) {
  for (var i = 2; i < value; i++) {
    if (value % i === 0) {
      return false
    }
  }
  return true
}

function isAllPrime (arrayOfNum) {
  return arrayOfNum.every(function (e) {
    return isPrime(e)
  })
}

console.log(isAllPrime(numbers))
