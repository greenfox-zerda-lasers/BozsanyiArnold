from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def rectangling(x,y):
    return canvas.create_rectangle(x,y,x+50,y+50)

rectangling(0,0,)
rectangling(50,50)

root.mainloop()
