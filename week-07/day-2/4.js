'use strict'

var af = [4, 5, 6, 7]
// print all the elements of af, dont use for or while :)

function logEach (arr) {
  if (arr.length >= 1) {
    console.log(arr.shift())
    logEach(arr)
  }
}
logEach(af)
