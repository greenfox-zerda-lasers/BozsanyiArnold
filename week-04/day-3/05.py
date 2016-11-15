from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def drawhorizontal(x,y):
    return canvas.create_line(x,y,x+50,y)
drawhorizontal(50,15)
drawhorizontal(50,10)
drawhorizontal(50,20)
root.mainloop()
