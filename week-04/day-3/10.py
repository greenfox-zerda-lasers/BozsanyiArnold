from tkinter import *
root = Tk()

canvassize = 300
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def rectangling(size):
    return canvas.create_rectangle(canvassize // 2 - size // 2, canvassize // 2 - size // 2, canvassize//2 + size //2, canvassize//2 + size //2, fill="black")

rectangling(50)

root.mainloop()
