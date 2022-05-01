from tkinter import *

mainwin = Tk ()

x = int(input("počet štvorcov: "))
y = 1000

canvas = Canvas(mainwin,width = y, height = y)
canvas.pack()

s = y/x

for j in range (0,x):
    canvas.create_rectangle(j*s,j*s,j*s+s,j*s+s)

mainwin.mainloop ()