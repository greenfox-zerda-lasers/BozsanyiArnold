from tkinter import *
import time
import random
import webcolors

def rgb():
    return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])


root = Tk()
size = 600
canvas = Canvas(root, width = size, height = size, bg = rgb())
canvas.pack()



def hexanerv(x,y,size):
    time.sleep(0.00000000001)
    canvas.create_polygon(
    x+size/4,y,
    x+size*0.75,y,
    x+size,(y + size/2 * (3**0.5/2)),
    x +size*1.5/2,(y +size * (3**0.5/2)),
    x + size/2/2,(y + size * (3**0.5/2)),
    x,y+size/2 * (3**0.5/2), fill=rgb(), outline=rgb())
    canvas.update()
    if size > 20:
        hexanerv(x+size/4/1.5,y,size/3)
        hexanerv(x+size/2,y,size/3)
        hexanerv(x+size*(3**0.5/2)-size/5,y+size/2*(3**0.5/2)/1.5,size/3)
        hexanerv(x,y+size/2*(3**0.5/2)/1.5,size/3)
        hexanerv(x+size/4/1.5,y+size*(2/3)*(3**0.5/2),size/3)
        hexanerv(x+size/2,y+size*(2/3)*(3**0.5/2),size/3)

while True:
    hexanerv(0,40,size)


canvas.mainloop()
