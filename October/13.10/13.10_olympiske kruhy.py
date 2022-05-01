from tkinter import *
mainwin = Tk()
size = 1000
canvas = Canvas(mainwin, width = size, height = size)
canvas.pack()
osize = 50

def Circle(x,y):
    canvas.create_oval(x - osize,y-osize,x+osize,y+osize)
for i in range (0,3):
    Circle(110*i + 150, i + 200)
for j in range(0,2):
    Circle(110*j + 200, j + 250)
mainwin.mainloop()