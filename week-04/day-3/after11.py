from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def rectangling(x,y,n):
    counterpcs = 6
    while counterpcs >= 1:
        canvas.create_rectangle(x, y, x+n, y+n, fill="purple")
        y +=n
        x +=n
        n *= 2
        counterpcs -= 1
rectangling(5,5,10)
root.mainloop()
