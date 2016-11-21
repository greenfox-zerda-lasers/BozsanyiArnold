class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
        if self.yob < 0 or self.yob > 2016:
            raise ValueError



person1 = Person('Joey',1984)
print(person1.name, person1.yob)
person2 = Person('Chandler', -350)
print(person2.name, person2.yob)
