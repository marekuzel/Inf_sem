import random
from tkinter import *

mainwin = Tk()
canvas = Canvas(mainwin, width = 300, height = 300)
canvas.pack()

sučet = []
for i in range (1000):
    x,y = random.randrange(1,7),random.randrange(1,7)
    sučet.append(x+y)
    textFile = open ("hodKockou.txt", "a")
    textFile.write(f"{x} {y} {x+y} \n")
    textFile.close()

for i in range (6):
    canvas.create_line (0,50*i,400,50*i) 
for i in range (2,13):
    numberOfNumber = int(sučet.count(i))
    print (numberOfNumber)
    canvas.create_rectangle (0+i*20,300-numberOfNumber-2,i*20+5,300-numberOfNumber+2)
    canvas.create_text (0+i*20,10, text = i)
mainwin.mainloop()