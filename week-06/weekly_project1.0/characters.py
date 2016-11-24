import random

def dice():
    random.randint(1,6)
class Characters:
    def __init__(self, maxHP, DP, SP):
        self.lv = 1
        self.maxHP = maxHP
        self.HP = self.maxHP
        self.DP = DP
        self.SP = SP

class Hero(Characters):
    def __init__(self):
        super().__init__(20 + 3 * dice(), 2 * dice(),5 + dice())

class Skeleton(Characters):
    def __init__(self):
        super().__init__(2 * self.lv * dice(),self.lv/2 * dice(),self.lv * dice())

class Boss(Characters):
    def __init__(self):
        super().__init__(2 * self.lv * dice() + dice(), self.lv/2 * dice() + +dice()/2, self.lv * dice() + self.lv)
