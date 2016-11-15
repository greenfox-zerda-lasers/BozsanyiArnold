from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def drawline(x,y):
    size = canvassize
    for size in canvas:
        canvas.create_line(x,size-y,size-x,size)
        size -=20
drawline(20,20)
drawline(20,40)


root.mainloop()
