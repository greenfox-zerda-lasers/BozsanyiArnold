from tkinter import *
import time
import random
import webcolors
root = Tk()
size = 600
canvas = Canvas(root, width = size, height = size, bg = "black")
canvas.pack()

def rgb():
   return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])

def trinerv(x,y,size):
    time.sleep(0.0001)
    canvas.create_polygon(x, y,x+size,y,x+size/2,y+size * (3**0.5/2),outline=rgb(),fill="")
    canvas.update()
    if size > 20:
        trinerv(x,y,size/2)
        trinerv(x+size/2,y,size/2)
        trinerv(x+size/4,y+size/2 * (3**0.5/2),size/2)

trinerv(0,0,size)
canvas.mainloop()
