import PIL.Image
import PIL.ImageTk
from tkinter import *
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

    def drawzone(self, matrix):
        for i in range(len(matrix)):
            for n in range(len(matrix[i])):
                if matrix[i][n] == 'f':
                    self.canvas.create_image(n * 72,i * 72,image = self.floor_img, anchor=NW)
                else:
                    self.canvas.create_image(n * 72,i * 72, image = self.wall_img, anchor=NW)
