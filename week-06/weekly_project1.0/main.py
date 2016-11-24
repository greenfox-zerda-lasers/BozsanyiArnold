from view import View
from map import Map
from characters import Characters
from characters import Hero
from characters import Skeleton
from characters import Boss
from tkinter import *


class GamePlay:
    def __init__(self):
        self.view = View()
        self.map = Map()
        self.characters = Characters('anyadat')
        self.hero = Hero()
        self.skeleton = Skeleton()
        self.boss = Boss()
        self.view.draw_map(self.map.gamezone1)



gameplay1 = GamePlay()
