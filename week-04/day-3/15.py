from tkinter import *
root = Tk()
canvassize = 300

canvas = Canvas(root, width = 300, height = 300, bg="black")
canvas.pack()

def drawline():
    for i in range(0,canvassize,20):
        canvas.create_line(canvassize//2,canvassize//2-i,canvassize//2-i,canvassize//2, fill="green")
        canvas.create_line(canvassize//2+i,canvassize//2,canvassize//2, canvassize//2+i, fill="purple")
        canvas.create_line(canvassize//2,canvassize//2-i,canvassize//2-i,canvassize//2, fill="blue")
        canvas.create_line(canvassize//2+i,canvassize//2,canvassize//2, canvassize//2+i, fill="yellow")

drawline()
root.mainloop()
