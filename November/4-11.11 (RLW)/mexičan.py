from tkinter import *
import random

mainwin = Tk()
size = 1000
canvas = Canvas(mainwin, width=size, height=size)
canvas.pack()


def mexičan(x, y, size):
    canvas.create_oval(x - 35*size/2, y - 5*size/2, x + 35*size/2, y + 5*size/2, fill="black",tag = "mexican")
    canvas.create_oval(x - 25*size/2, y - 25*size/2, x + 25*size/2, y + 25*size/2, fill="brown",tag = "mexican")
    canvas.create_oval(x - 15*size/2, y - 15*size/2, x + 15*size/2, y + 15*size/2, fill="yellow",tag = "mexican")


for i in range(0, 50):
    canvas.after(180)
    canvas.update()
    x=random.randrange(0,1000)
    y = random.randrange(0,1000)
    size = random.randrange(1,15)
    mexičan(x,y,size)

mainwin.mainloop()