class Person():
    firstname = ''
    lastname = ''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def greeting(self):
        return ('Ayyo %s %s' % (self.firstname, self.lastname))



class Student(Person):
    list1 = []
    def add_grades(self, element):
        if element <= 5 and element >= 1 and element % 1 == 0:
            self.list1 += [element]
            return self.list1
        else:
            print('Wrong grade dude. Must be 0 or negative or to much.')
    def salute(self):
        return (self.firstname, self.lastname, (sum(self.list1) / len(self.list1)) )

person1 = Student('Carlos', 'Santiago')
person1.add_grades(4)
person1.add_grades(6)
person1.add_grades(5)
person1.add_grades(2)
print(person1.salute())
