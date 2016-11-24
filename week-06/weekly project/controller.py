from view import View
from model import GameZones
from model import Hero
from model import Skeleton
from model import Boss
from model import Characters
import random

def dice():
    return random.randint(1,4)

class GamePlay:
    def __init__(self):
        self.view = View()
        self.gamezones = GameZones()
        self.hero = Hero()
        self.skeleton = Skeleton()
        self.boss = Boss()
        self.characters = Characters()
        self.view.drawzone(self.gamezones.gamezone1)
        self.view.show_boss(self.boss.position)
        self.view.show_skeleton(self.skeleton.positions)
        self.view.show_hero('s',0,0)
        self.view.root.bind('<w>',self.move)
        self.view.root.bind('s',self.move)
        self.view.root.bind('a',self.move)
        self.view.root.bind('d',self.move)
        self.view.root.bind('<space>',self.fight_with_skeleton1)
        self.view.canvas.mainloop()

    def move(self,event):
        self.view.canvas.delete('hero')
        if event.keysym == 'd' and self.validator(self.hero.position[0],self.hero.position[1] + 1):
            self.hero.position[1] += 1
        elif event.keysym == 'a' and self.validator(self.hero.position[0],self.hero.position[1] - 1):
            self.hero.position[1] -= 1
        elif event.keysym == 's' and self.validator(self.hero.position[0] + 1,self.hero.position[1]):
            self.hero.position[0] += 1
        elif event.keysym == 'w' and self.validator(self.hero.position[0] - 1,self.hero.position[1]):
            self.hero.position[0] -= 1
        self.view.show_hero(event.keysym, self.hero.position[1],self.hero.position[0])
        self.hero.movement_counter += 1

    def validator(self,x,y):
        if y <= 9 and y >= 0 and x <= 10 and x >= 0:
            if self.gamezones.gamezone1[x][y] == 'f':
                return True
        return False

    def fight_with_skeleton1(self,event):
        if event.keysym == '<space>':
            self.skeleton.hp -= (self.hero.sp - self.skeleton.dp)
            self.hero.hp -= (self.skeleton.sp - self.hero.dp)
            if self.skeleton.hp <= 0:
                self.view.canvas.delete('skeleton1')
            elif self.hero.hp <= 0:
                self.view.canvas.delete('hero')
                self.hero.position = [0,0]
                self.view.show_hero('s',0,0)

gameplay1 = GamePlay()
