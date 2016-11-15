from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
diagonal = canvas.create_line(0, 0, 300, 300, fill="green")

root.mainloop()
