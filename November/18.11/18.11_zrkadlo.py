from tkinter import *

csize = 1000
mainwin = Tk()
canvas = Canvas (mainwin, width = csize, height = csize)
canvas.pack()

def freehand (event):
    global xs,ys
    xs = event.x
    ys = event.y
    canvas.create_line(xs,ys,xs+1,ys+1,)
    if xs < 500:
        canvas.create_line(500 + (500-xs), ys, 501 + (500-xs), ys + 1)
    elif xs > 500:
        canvas.create_line(500 - (xs-500), ys, 501 - (xs-500), ys + 1)
canvas.bind ("<Motion>", freehand) #problem
mainwin.mainloop()