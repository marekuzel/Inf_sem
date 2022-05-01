import random, math
from tkinter import *
mainwin = Tk()
canvasSize = 1000
canvas = Canvas (mainwin, width = canvasSize, height = canvasSize)
canvas.pack()
def dvaKruhy():
    x1,x2,y1,y2 = random.randrange (50,950),random.randrange (50,950),random.randrange (50,950),random.randrange (50,950)
    canvas.create_oval (x1-50,y1-50,x1+50,y1+50)
    canvas.create_oval (x2-50,y2-50,x2+50,y2+50)
    canvas.create_line (x1,y1,x2,y2)
    vzdialenost = math.sqrt((abs(x1-x2)+abs(y1-y2))**2)
    canvas.create_text (100,100,text=vzdialenost)
dvaKruhy()

mainwin.mainloop()