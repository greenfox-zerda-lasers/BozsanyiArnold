class Car():
    type = ()
    km = 0
    def __init__(self, type, km):
        self.type = type
        self.km = km
    def run(self, run):
        self.run = run
        return self.km + self.run , self.type

car1 = Car('Mitsubitshi', 20000)
print(car1.run(150))
