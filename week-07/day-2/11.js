'use strict'

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack () {
  this.storage = []
  this.size = function () {
    return this.storage.length
  }
  this.push = function (something) {
    this.storage[this.storage.length] = something
  }
  this.pop = function () {
    var deleted = this.storage[this.storage.length - 1]
    this.storage.length -= 1
    return deleted
  }
}
var stack = new Stack()
stack.push('Kutule')
stack.push('NemAdom')
stack.push(2)
stack.push(678)
console.log(stack.size())
console.log(stack.pop())
console.log(stack.size())
