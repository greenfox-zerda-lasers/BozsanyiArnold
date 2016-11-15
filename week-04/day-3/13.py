from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300, bg="black")
canvas.pack()

def drawline(x,y):
    for y in range(20,281,20):
        for x in range(20,281,20):
            if x ==20 or x == 280 or y == 20 or y == 280:
                canvas.create_line(x, y,canvassize//2,canvassize// 2, fill="pink")

drawline(20,20)
root.mainloop()
