from tkinter import *

size = 1000
mainwin = Tk()
canvas = Canvas (mainwin, height = size, width = size)
canvas.pack()

def rect_start(event):
    global xs, ys
    xs = event.x
    ys = event.y

def drag (event):
    global xs,ys
    canvas.delete("rect")
    canvas.create_rectangle(xs,ys,event.x, event.y, tag = "rect")
    canvas.update()


def drop (event):
    global xs,ys
    canvas.create_rectangle(xs,ys,event.x, event.y, tag = "rect")

canvas.bind("<Button-1>", rect_start)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", drop)
mainwin.mainloop()