class Circle():
    radius = 0
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return self.radius * 2 *self.pi
    def get_area(self):
        return self.radius**2 * self.pi

circle1 = Circle(9)
print (circle1.get_circumference(), circle1.get_area())
