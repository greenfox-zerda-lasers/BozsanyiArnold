from tkinter import *
import time
import random
import webcolors

root = Tk()
size = 600
canvas = Canvas(root,width=size, height=size)
canvas.pack()
def rgb():
   return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])
def hexnerv(x,y,size):
    time.sleep(0.03)
    canvas.update()
    canvas.create_polygon(
    x+size/4,y,
    x+size*0.75,y,
    x+size,(y + size/2 * (3**0.5/2)),
    x +size*1.5/2,(y +size * (3**0.5/2)),
    x + size/2/2,(y + size * (3**0.5/2)),
    x,y+size/2 * (3**0.5/2),fill="", outline="black")
    if size >20:
        hexnerv(x+size/8,y,size/2)
        hexnerv(x+size/8,y+size/2*(3**0.5/2),size/2)
        hexnerv(x+size/2,y+size/4*(3**0.5/2),size/2)

hexnerv(0,20,600)

root.mainloop()
