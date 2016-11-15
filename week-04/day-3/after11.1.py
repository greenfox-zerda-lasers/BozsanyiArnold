from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def rectangling(x,y):
    counterpcs = 18
    while counterpcs > 1:
        canvas.create_rectangle(x, y, x+10, y+10, fill="purple")
        y +=10
        x +=10
        counterpcs -= 1
rectangling(5,5)
root.mainloop()
