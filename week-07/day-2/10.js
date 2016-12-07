'use strict'

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {

    grades : [],
    addGrade : function (num) {
    if (num <= 5 && num > 0) {
      this.grades.push(num)
    } else {
      return 'Grades are only acceptable between numbers 1 and 5!!!!!! #YoloSwag'
    }
  },
  getAverage: function () {
     return this.grades.reduce(function (a, b) { return a + b }, 0) / this.grades.length
  }
}
student.addGrade(5)
student.addGrade(2)
student.addGrade(4)
console.log(student.getAverage())
