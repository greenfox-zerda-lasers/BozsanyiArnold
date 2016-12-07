'use strict'

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function lettersOccurence (string) {
  return string.split('').reduce(function (acc, item) {
    if (acc[item] === undefined) {
      acc[item] = 0
    }
    acc[item]++
    return acc
  }, {})
}

console.log(lettersOccurence('apple'))
