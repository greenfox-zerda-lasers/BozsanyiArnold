'use strict'

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function sumArray (array) {
  var result = 0
  for (var element = 0; element < array.length; element++) {
    result += array[element]
  }
  return result
}
console.log(sumArray(numbers))
