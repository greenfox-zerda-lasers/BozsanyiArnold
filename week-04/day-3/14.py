from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300)

canvas.pack()

def drawline(x,y):
    for i in range(0,canvassize+1,20):
        canvas.create_line(0,canvassize-i,canvassize-i,canvassize, fill="green")
        canvas.create_line(0+i,0,canvassize, 0+i, fill="purple")

drawline(20,20)
root.mainloop()
