'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(width,height) {
  this.width = width;
  this.height = height;
}

function getArea() {
  return 'The area of the rectangle is:' + this.width * this.height;
}

function getCircumference() {
  return 'The circumference of the rectangle is:' + 2 * this.width + 2 * this.height;
}

var recti = new Rectangle(5, 10);
console.log(recti.width);
console.log(recti.height);
var area = recti.getArea();
console.log(area);
