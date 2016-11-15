from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
myrectangle = canvas.create_rectangle(145, 145, 10, 10)
leftside = canvas.create_line(25, 25, 25, 200, fill="green")
topline = canvas.create_line(25, 25, 200, 25, fill="yellow")
rightline = canvas.create_line(200, 25, 200, 200, fill="purple")
botline = canvas.create_line(25, 200, 200, 200, fill="lightblue")

root.mainloop()
