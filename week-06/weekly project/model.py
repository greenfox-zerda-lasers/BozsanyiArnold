import random

class GameZones:

    def __init__(self):
        self.gamezone1 = [['f', 'f', 'f', 'w', 'f', 'w', 'f', 'f', 'f', 'f'],
                          ['f', 'f', 'f', 'w', 'f', 'w', 'f', 'w', 'w', 'f'],
                          ['f', 'w', 'w', 'w', 'f', 'w', 'f', 'w', 'w', 'f'],
                          ['f', 'f', 'f', 'f', 'f', 'w', 'f', 'f', 'f', 'f'],
                          ['w', 'w', 'w', 'w', 'f', 'w', 'w', 'w', 'w', 'f'],
                          ['f', 'w', 'f', 'w', 'f', 'f', 'f', 'f', 'w', 'f'],
                          ['f', 'w', 'f', 'w', 'f', 'w', 'w', 'f', 'w', 'f'],
                          ['f', 'f', 'f', 'f', 'f', 'w', 'w', 'f', 'w', 'f'],
                          ['f', 'w', 'w', 'w', 'f', 'f', 'f', 'f', 'w', 'f'],
                          ['f', 'f', 'f', 'w', 'f', 'w', 'w', 'f', 'w', 'f'],
                          ['f', 'w', 'f', 'w', 'f', 'w', 'f', 'f', 'f', 'f']]

        self.gamezone2 = [['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
                          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'f'],
                          ['w', 'f', 'f', 'f', 'f', 'w', 'f', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'w', 'w', 'w', 'w', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'f', 'f', 'f', 'w', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'f', 'f', 'f', 'w', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'f', 'f', 'f', 'w', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'f', 'w', 'w', 'w', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'f', 'f', 'f', 'f', 'f', 'w', 'f'],
                          ['w', 'f', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'f'],
                          ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']]


def dice():
    return random.randint(1,6)

def dice3():
    return random.randint(3,6)

class Characters:
    def __init__(self):
        self.lv = 1

class Hero(Characters):
    def __init__(self):
        self.position = [0,0]
        self.movement_counter = 0
        self.max_hp = 20 + 3 * dice()
        self.hp = self.max_hp
        self.dp = 2 * dice()
        self.sp = 5 + dice()
        self.lv = 1

class Skeleton(Characters):
    def __init__(self):
        self.lv = 1
        self.positions = [[4,4],[7,8],[6,3]]
        self.hp = 2 * self.lv * dice()
        self.dp = self.lv/2 * dice()
        self.sp = self.lv * dice()

class Boss(Characters):
    def __init__(self):
        self.lv = 1
        self.position = [6,0]
        self.hp = 2 * self.lv * dice() + dice()
        self.dp = self.lv/2 * dice() + (dice()/2)
        self.sp = self.lv * dice() +self.lv
