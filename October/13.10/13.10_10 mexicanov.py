from tkinter import *

mainwin = Tk()

csize = 1000

canvas = Canvas(mainwin, width = csize, height = csize)
canvas.pack()

size = 50

def Mexican(x,y):
    canvas.create_oval (x - size / 2 - size/15, y  - size/15, x - size / 2 + size/15, y + size/15)
    canvas.create_oval (x+size/2 - size/15,y - size/15,x+size/2 + size/15, y + size/15)
    canvas.create_oval (x - size/15,y - size*1.5,x + size/15,y + size*1.5)
    canvas.create_oval (x-size/2,y-size/2, x + size/2, y + size/2, fill = "white")
    canvas.create_oval (x-size/8,y-size/8, x + size/8, y + size/8)
for i in range (1,11):
    Mexican(i * csize/12, 500)

mainwin.mainloop()