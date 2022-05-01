from tkinter import *
size = 1000
mainwin = Tk()
canvas = Canvas (mainwin, height = size, width = size)
canvas.pack()

def Kruh (event):
    ksize = 20
    x = event.x
    y = event.y
    canvas.create_oval(x - ksize, y - ksize, x + ksize, y + ksize)

canvas.bind("<Button-1>", Kruh)
mainwin.mainloop()