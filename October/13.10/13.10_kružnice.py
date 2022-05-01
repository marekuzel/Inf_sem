from tkinter import *
mainwin = Tk()

size = 1000
canvas = Canvas(mainwin,width = size, height = size)
canvas.pack()

cin = int(input("Počet kruhov: "))


def Kružok(x,osize):
    canvas.create_oval(x-osize/2,x-osize/2,x+osize/2,x+osize/2)

for i in range (0,cin):
    Kružok(size/2, i*(size/cin))
mainwin.mainloop()