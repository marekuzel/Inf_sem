from tkinter import *
import random

mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()

with open ("typDna.txt","r") as r:
    
    xr = r.readlines()

x = 1000
y = 500
randText = random.choice(xr)

def klik(event):
    global randText
    randText = random.choice(xr)

def typ (x,y, d):
    canvas.create_text (x,y,text = d, tags = "Typ")
    canvas.update ()
    canvas.after (50)
    canvas.delete ("Typ")
    if x<-100:
        x = 1100
    x -=10
    typ (x,y, randText)
    



canvas.bind ("<Button-1>", klik)
typ (x,y,randText)
mainwin.mainloop()