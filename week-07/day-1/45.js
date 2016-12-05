'use strict'

var names = ['Zakarias', 'Hans', 'Otto', 'Ole']
// create a function that returns the shortest string
// from an array

function shortestString (array) {
  array.sort (function (a, b) {
    return a.length - b.length
  })
  return array[0]
}
console.log(shortestString(names))
