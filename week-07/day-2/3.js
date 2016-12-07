'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

function each (arr, fun) {
  var result = []
  fun = arr.length
  result.push(arr * fun)
  return result
}

console.log(each([1,2,3], 3))
