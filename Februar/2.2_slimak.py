from tkinter import *
import random
mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()

def rebrík(maxNStvorcov):
    global nStvorcov, stranaStvorca
    nStvorcov = random.randrange (3,maxNStvorcov)
    print (nStvorcov)
    stranaStvorca = 1000/nStvorcov
    for i in range (0,nStvorcov):
        canvas.create_rectangle (500-(stranaStvorca/2),i*stranaStvorca, 500+(stranaStvorca/2), (i+1)*stranaStvorca)
rebrík(30)
def kruh (poz):
    canvas.create_oval (500-(stranaStvorca/4),poz*stranaStvorca/2, 500+(stranaStvorca/4), (poz+1)*stranaStvorca/2)
kruh (nStvorcov)

canvas.mainloop()
