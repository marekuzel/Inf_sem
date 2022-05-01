import random
from tkinter import *
mainwin = Tk()
canvasSize = 1000
canvas = Canvas(mainwin, height = canvasSize, width = canvasSize)
canvas.pack()

def mriezka():
    for i in range (0,3):
        for j in range (0,3):
            canvas.create_rectangle (i*(canvasSize/3),j*(canvasSize/3), i*(canvasSize/3)+(canvasSize/3),j*(canvasSize/3) + (canvasSize/3))
def klikKrizik(e):
    x = e.x
    y = e.y
    canvas.create_line(x-(canvasSize/3)/3,y-(canvasSize/3)/3, x+(canvasSize/3)/3, y+(canvasSize/3)/3)
    canvas.create_line(x-(canvasSize/3)/3,y+(canvasSize/3)/3, x+(canvasSize/3)/3, y-(canvasSize/3)/3)
def klikKruh(e):
    x = e.x
    y = e.y
    canvas.create_oval (x-(canvasSize/3)/3,y-(canvasSize/3)/3, x+(canvasSize/3)/3, y+(canvasSize/3)/3)
mriezka()
canvas.bind ("<Button-1>", klikKrizik)
canvas.bind ("<Button-3>", klikKruh)
mainwin.mainloop()