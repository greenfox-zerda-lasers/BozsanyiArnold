'use strict'

var numbers = [3, 4, 5, 6, 7]
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function evensInArray (array) {
  var evens = new Array()
  for (var e = 0; e < array.length; e++) {
    if (array[e] % 2 === 0) {
      evens.push(array[e])
    }
  }
  return evens
}
console.log(evensInArray(numbers))
