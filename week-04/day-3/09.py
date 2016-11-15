from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def rectangling(x):
    return canvas.create_rectangle(x,x,x+50,x+50)

rectangling(0)
rectangling(50)

root.mainloop()
