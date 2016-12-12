'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets (consuption) {
  this.consuption = consuption;
  this.fuel = 0;
}

Rockets.prototype.fill = function (amount) {
  this.amount = amount;
  this.fuel += this.amount;
}

Rockets.prototype.launch = function () {
  if (this.fuel >= this.consuption) {
    this.fuel -= this.consuption;
    console.log('The rocket has been launched.')
  } else {
    console.log('Not enough fuel')
  }
}

var falcon1 = new Rockets(10);

console.log(falcon1.fuel);
falcon1.fill(50);
console.log(falcon1.fuel);
falcon1.launch();
console.log(falcon1.fuel);
