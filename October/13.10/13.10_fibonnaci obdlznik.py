from tkinter import *
mainwin = Tk()
size = 1000
canvas = Canvas (mainwin,width = size, height = size)
canvas.pack()

cin = int(input("Počet postupnosti: "))

x = size/2
y = size/2
unit = 5
prevunit = 0
prev1unit = 0

for i in range (0,cin):
    unit = prev1unit + unit
    prev1unit = prevunit #prev1unit is needed to store preunit value since we are going to need it after changing it value, im sure that this could be done more elegantly
    canvas.create_rectangle(x,y,x + unit, y + unit)
    x = x + unit
    y = y + unit
    prevunit = unit





    unit = prev1unit + unit
    prev1unit = prevunit
    canvas.create_rectangle(x, y, x + unit, y - unit)

    x = x + unit
    y = y - unit
    prevunit = unit

    unit = prev1unit + unit
    prev1unit = prevunit
    canvas.create_rectangle(x, y, x - unit, y - unit)
    x = x - unit
    y = y - unit
    prevunit = unit

    unit = prev1unit + unit
    prev1unit = prevunit
    canvas.create_rectangle(x, y, x - unit, y + unit)
    x = x - unit
    y = y + unit
    prevunit = unit
mainwin.mainloop()