'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal() {
}

Animal.prototype.loud = function (say) {
  this.say = say;
}

var dog = new Animal();
dog.loud('woof');
console.log(dog.say);

var goose = new Animal();
goose.loud('GaGAgaga');
console.log(goose.say);
