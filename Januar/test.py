import random
from tkinter import *

mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()

with open ("textinput.txt", "r") as r:
    x = r.readlines()
def slovo_1 (x,y, textItself):
    canvas.create_text(x,y,text = textItself)
def slovo():
    for i in x:
        i = i.replace ("\n", "")
        listValuesx1 = []
        listValuesy1 = []
        slovaList = i.split ()
        for j in range (0,len(slovaList)):
            x1 = random.randrange (100,850)
            y1 = random.randrange (100,850)
            slovo_1 (x1, y1, slovaList [j])
            listValuesx1.append(x1)
            listValuesy1.append(y1)
        for j in range (0,len(listValuesx1)):
            canvas.create_text(listValuesx1[j],listValuesy1[j],text = slovaList [j], fill = "red", tags = "cerven")
            canvas.update()
            canvas.after(1000)
            canvas.delete("cerven")
        canvas.delete("all")
        slovo()
slovo()
mainwin.mainloop ()