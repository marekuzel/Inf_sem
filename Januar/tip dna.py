from tkinter import *
from random import *

canvas = Canvas(width=1000, height=1000)
canvas.pack()


subor = open('tip.txt', 'r')

while True:
    veta = subor.readline()
    slovo = veta.split()
    for i in slovo:
        x = randint(200,900)
        y = randint(200,900)
        canvas.create_text(x,y,text=i,tag=str(i))
    canvas.update()
    for i in slovo:
        canvas.itemconfig(str(i),fill='red')
        canvas.update()
        canvas.itemconfig(str(i),fill='black')
        canvas.after(500)
    canvas.delete('all')

subor.close()
