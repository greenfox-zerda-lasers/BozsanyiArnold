import PIL.Image
import PIL.ImageTk
from tkinter import *
from model import GameZones
import random


class View:

    def __init__(self):
        self.root = Tk()
        self.tile_size = 72
        self.descriptions_size = 400
        self.canvas = Canvas(self.root, width = self.descriptions_size + 10 * self.tile_size, height = 11 * self.tile_size, background = "blue")


        floor = PIL.Image.open("floor.png")
        self.floor_img = PIL.ImageTk.PhotoImage(floor)

        wall = PIL.Image.open("wall.png")
        self.wall_img = PIL.ImageTk.PhotoImage(wall)

        hfront = PIL.Image.open("hero-down.png")
        self.hero_front = PIL.ImageTk.PhotoImage(hfront)

        hback = PIL.Image.open("hero-up.png")
        self.hero_back = PIL.ImageTk.PhotoImage(hback)

        hright = PIL.Image.open("hero-right.png")
        self.hero_right = PIL.ImageTk.PhotoImage(hright)

        hleft = PIL.Image.open("hero-left.png")
        self.hero_left = PIL.ImageTk.PhotoImage(hleft)

        skel = PIL.Image.open("skeleton.png")
        self.skeleton = PIL.ImageTk.PhotoImage(skel)

        boss = PIL.Image.open("boss.png")
        self.boss = PIL.ImageTk.PhotoImage(boss)

        self.canvas.pack()
        self.gamezone = GameZones()

    def drawzone(self, matrix):
        for i in range(len(matrix)):
            for n in range(len(matrix[i])):
                if matrix[i][n] == 'f':
                    self.canvas.create_image(n * 72,i * 72,image = self.floor_img, anchor=NW)
                else:
                    self.canvas.create_image(n * 72,i * 72, image = self.wall_img, anchor=NW)

    def show_hero(self,lastkey,x,y):
        if lastkey == 'w':
            self.canvas.create_image(x*72,y*72,image = self.hero_back,anchor=NW, tag = 'hero')
        elif lastkey =='s':
            self.canvas.create_image(x*72,y*72,image = self.hero_front,anchor=NW, tag = 'hero')
        elif lastkey == 'a':
            self.canvas.create_image(x*72,y*72,image = self.hero_left,anchor=NW, tag = 'hero')
        elif lastkey == 'd':
            self.canvas.create_image(x*72,y*72,image = self.hero_right,anchor=NW, tag = 'hero')

    def show_skeleton(self,x):
        self.canvas.create_image(x[0][0]*72,x[0][1]*72,image = self.skeleton,anchor = NW, tag = 'skeleton1')
        self.canvas.create_image(x[1][0]*72,x[1][1]*72,image = self.skeleton,anchor = NW, tag = 'skeleton2')
        self.canvas.create_image(x[2][0]*72,x[2][1]*72,image = self.skeleton,anchor = NW, tag = 'skeleton3')


    def show_boss(self,x):
        self.canvas.create_image(x[0]*72,x[1]*72,image = self.boss, anchor = NW, tag = 'boss')
