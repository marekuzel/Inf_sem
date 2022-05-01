from tkinter import *
mainwin = Tk()
canvas = Canvas (mainwin, height = 1000, width = 1000)
canvas.pack()

def initClick(e):
    global ystart,xstart
    ystart = e.y
    xstart = e.x
    canvas.delete ("obdlznik", "obsah")
def dragAnim (e):
    canvas.delete ("obdlznik", "obsah")
    global ystart,xstart
    ynow = e.y
    xnow = e.x
    canvas.create_rectangle(xstart,ystart,xnow, ynow, tags = "obdlznik")
    canvas.update()
    canvas.create_text (100 , 100, text = abs(xnow-xstart)*abs(ynow-ystart), tags = "obsah")
canvas.bind("<Button-1>", initClick)
canvas.bind("<B1-Motion>", dragAnim)
mainwin.mainloop()