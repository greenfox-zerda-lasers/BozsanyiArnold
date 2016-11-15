class Pirate():
    drink = 0

    def drink_rum(self):
        self.drink  += 1
    def hows_goin_mate(self):
        if self.drink >= 5:
            return 'Arrrrr!'
        else:
            return "Nothin'"
pirate1 = Pirate()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
print(pirate1.hows_goin_mate())
