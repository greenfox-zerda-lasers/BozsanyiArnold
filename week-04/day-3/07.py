from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
recti1 = canvas.create_rectangle(0, 0, 150, 150, fill="green")
recti2 = canvas.create_rectangle(150, 150, 300, 300, fill="yellow")
recti3 = canvas.create_rectangle(150, 0, 300, 150, fill="red")
recti4 = canvas.create_rectangle(0, 150, 150, 300, fill="blue")
root.mainloop()
