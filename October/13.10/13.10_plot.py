from tkinter import *

mainwin = Tk()

size = 1000

canvas = Canvas (mainwin, width = size,height = size)
canvas.pack()

cin = int(input("počet čiar: "))
x = size/cin
y = (size*0.5)*-1
for i in range (int(y), 2*cin):
    canvas.create_line(i*x, 0 , i*x + 0.5*size, size)
for i in range(int(y), 2 * cin):
    canvas.create_line(i * x + 0.5 * size, 0, i * x, size)
mainwin.mainloop()