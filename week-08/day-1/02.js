'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(width,height) {
  this.width = width;
  this.height = height;
}

Rectangle.prototype.getArea = function () {
  return 'The area of the rectangle is:' + this.width * this.height;
}

Rectangle.prototype.getCircumference = function () {
  return 'The circumference of the rectangle is:' + 2 * (this.width + this.height);
}

var recti = new Rectangle(10, 50);
console.log(recti.getArea());
console.log(recti.getCircumference());
