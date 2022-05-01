from tkinter import *
import random

size = 1000
mainwin = Tk()
canvas = Canvas (mainwin, height = size, width = size)
canvas.pack()

def mexican(x, y, size):
    canvas.create_oval(x - 35*size/2, y - 5*size/2, x + 35*size/2, y + 5*size/2, fill="black",tag = "mexican")
    canvas.create_oval(x - 25*size/2, y - 25*size/2, x + 25*size/2, y + 25*size/2, fill="brown",tag = "mexican")
    canvas.create_oval(x - 15*size/2, y - 15*size/2, x + 15*size/2, y + 15*size/2, fill="yellow",tag = "mexican")

def drag (event):
    msize = random.randrange(1,7)
    x = event.x
    y = event.y
    mexican(x,y, msize)

canvas.bind("<B1-Motion>", drag)
mainwin.mainloop()