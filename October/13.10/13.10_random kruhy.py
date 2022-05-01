from tkinter import *
import random
mainwin = Tk()
size = 1000

canvas = Canvas(mainwin, width = size,height = size)
canvas.pack()

def kružok(x,y,osize):
    canvas.create_oval(x,y,x+osize,y+osize)

for i in range (0,10):
    ovsize = random.randint(0,int(size/3))
    kružok(random.randint(0,size-int(ovsize)),random.randint(0,size-int(ovsize)), ovsize)

mainwin.mainloop()