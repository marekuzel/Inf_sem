import random
from tkinter import *
mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()
score = 0
def klik(e):
    global velkost,x,y, score
    xe = e.x
    ye = e.y
    if xe < x+velkost/2 and xe > x-velkost/2:
        if ye < y+velkost and ye > y-velkost/2:
            score+=1
    """canvas.delete("all")
            canvas.update()
            stvorec()"""

def stvorec ():
    global velkost,x,y
    velkost = 50
    x,y = random.randrange (950-velkost),random.randrange (950-velkost)
    canvas.create_rectangle (x-velkost/2, y-velkost/2, x+velkost/2, y+velkost/2,fill = "yellow")
    canvas.create_text (100,100,text = score)
    canvas.update()
    
    stvorec2()
def stvorec2 ():
    canvas.after(1000)
    canvas.delete ("all")
    stvorec()
stvorec ()

canvas.bind ("<Button-1>", klik)
mainwin.mainloop()