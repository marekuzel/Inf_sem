from tkinter import *

sizef = 1000
mainwin = Tk()
canvas = Canvas(mainwin, width = sizef, height = sizef)
canvas.pack()

x = 11
x1 = 1000
y = 50
size = 20
lopta = canvas.create_oval(x - size,y - size,x + size,y + size,tag = "lopta", fill = "red")

while True:
    canvas.move(lopta,10,0)
    x += 10
    canvas.update()
    canvas.after (20)
    if x > 1000:
        for i in range (150):
            canvas.move(lopta, -10, 0)
            x1 -= 10
            canvas.update()
            canvas.after(20)

mainwin.mainloop()