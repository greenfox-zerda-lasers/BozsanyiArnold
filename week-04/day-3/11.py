from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def rectangling(size, color):
    return canvas.create_rectangle(canvassize // 2 - size // 2, canvassize // 2 - size // 2, canvassize//2 + size //2, canvassize//2 + size //2, fill= color)
size = 300
colors = ("red", "blue", "green", "lightblue", "pink", "purple")
for color in colors:
    rectangling(size, color)
    size -= 50

root.mainloop()
