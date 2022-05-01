from tkinter import *
import random
mainwin = Tk()
size = 1000
canvas = Canvas(mainwin, width = size, height = size)
canvas.pack()

def štvorec(x,y,ssize):
    canvas.create_rectangle(x-ssize/2,y-ssize/2,x+ssize/2,y+ssize/2)
def kružok(x,y, ssize):
    canvas.create_oval(x - ssize / 2, y - ssize / 2, x + ssize / 2, y + ssize / 2)

for i in range (0,50):
    ssize = random.randrange (0,100)
    x = random.randrange (0,size-ssize)
    y = random.randrange (0,size-ssize)
    if y >= size/2:
        kružok (x,y,ssize)
    else:
        štvorec(x,y,ssize)

mainwin.mainloop()