'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function getItTexted (number) {
  if (number === 0) {
    return 'Zero'
  } else if (number === 1) {
    return 'One'
  } else if (number === 2) {
    return 'Two'
  } else if (number === 3) {
    return 'Three'
  } else if (number === 4) {
    return 'Four'
  } else if (number === 5) {
    return 'Five'
  } else if (number > 5) {
    return 'Many'
  } else {
    throw new Error('Please don\'t insert negative number.')
  }
}
console.log(getItTexted(-5))
