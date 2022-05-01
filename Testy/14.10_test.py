from tkinter import *
mainwin = Tk()
size = 1000
canvas = Canvas (mainwin, width = size, height = size)
canvas.pack()

cin = int(input("Počet kruhov: "))
osize = 100

def Kruh(x,y , osize):
    canvas.create_oval (x-osize/2,y - osize/2,x+osize/2,y + osize/2)

for i in range (1,cin+1):
    Kruh ((i*(size/cin)), size/2, 150)

mainwin.mainloop()