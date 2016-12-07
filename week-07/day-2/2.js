'use strict';

// create a function called apply that takes a function and calls it with one argument
// that is the string 'apple'
function apply (fun) {
  if (fun === console.log) {
    console.log('Apple')
  }
}

apply(console.log) // should log apple
