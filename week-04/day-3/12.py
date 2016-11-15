from tkinter import *
root = Tk()
canvassize = 500

canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

def rectangling(x,y):
    ycor = y
    counterx = 0
    countery = 0
    while x < canvassize *7 // 8:
        y = ycor
        while y < canvassize *7 //8:
            if counterx % 2 ==0 and countery % 2 != 0 or counterx % 2!=0 and countery % 2 == 0:
                canvas.create_rectangle(x, y,x+canvassize// 8,y + canvassize // 8, fill="black")
            else:
                canvas.create_rectangle(x, y,x+canvassize// 8,y + canvassize // 8 )
            y += canvassize //8
            counterx += 1
        x += canvassize //8
        countery +=1

rectangling(0,0)
root.mainloop()
