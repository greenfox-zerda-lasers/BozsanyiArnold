import PIL.Image
import PIL.ImageTk
from tkinter import *


class View:

    def __init__(self):
        self.root = Tk()
        self.tile_size = 72
        self.canvas = Canvas(self.root, width = self.tile_size *10, height = self.tile_size * 11)

        #IMPORTING THE PICTURES!!!!#YOLO

        floor = PIL.Image("floor.png")
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
        self.canvas.mainloop()

    def draw_map(self,matrix):
        for i in range(len(matrix)):
            for n in range(len(matrix[i])):
                if matrix[i][n] == 'f':
                    self.canvas_create_image (n * 72 ,i * 72, image = self.floor_img, anchor = NW )
                else:
                    self.canvas.create_image (n * 72, i * 72, image = self.wall_img, anchor = NW )

    def draw_hero_front(self, x, y):
        self.canvas.create_image(x, y, image = self.hero_front)

    def draw_hero_back(self, x, y):
        self.canvas.create_image(x, y, image = self.hero_back)

    def draw_hero_right(self, x, y):
        self.canvas.create_image(x, y, image = self.hero_right)

    def draw_hero_left(self, x, y):
        self.canvas.create_image(x, y, image = self.hero_left)

    def draw_skeleton(self, x, y):
        self.canvas.create_image(x, y, image = self.skeleton)

    def draw_boss(self, x, y):
        self.canvas.create_image(x, y, image = self.boss)
