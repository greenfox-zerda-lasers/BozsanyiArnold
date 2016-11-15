from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
rectie = canvas.create_rectangle(145, 145, 155, 155, fill="green")

root.mainloop()
