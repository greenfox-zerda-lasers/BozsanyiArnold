'use strict'

// create a function that returns it's input factorial

function factorial (number) {
  var result = 1
  for (var count = number; count > 1; count--) {
    result *= count
  }
  return result
}
console.log(factorial(4))
