'use strict';

var students = [
  {name: 'Rezso', age: 9.5, candies: 2},
  {name: 'Gerzson', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 3},
  {name: 'Zsombor', age: 12, candies: 5},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];


// create a function that counts the students that
// has more than 4 candies

function candyRich (object) {
  var count = 0
  for (var i = 0; i < object.length; i++) {
    if (object[i].candies > 4) {
      count++
    }
  }
  return count
}

console.log(candyRich(students))
