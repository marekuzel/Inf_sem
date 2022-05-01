from tkinter import *
from random import randrange
mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()
pouziteCisla = []
def stvorec (x,y):
    for i in range (5):
        for j in range (5):
            cisloAktualne = randrange (1,26)
            if cisloAktualne in pouziteCisla:
                while cisloAktualne in pouziteCisla:
                    cisloAktualne = randrange (1,26)    
            canvas.create_rectangle (x + i*100, y+j*100, x + 100+i*100, y + 100 + j*100)
            canvas.create_text (x +50 + i*100, y + 50 +j*100,text =  cisloAktualne)
            pouziteCisla.append(cisloAktualne)
stvorec(50,50)
mainwin.mainloop()