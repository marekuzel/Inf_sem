from tkinter import *
import random

mainwin = Tk()
size = 1000
canvas = Canvas (mainwin, width = size, height = size, bg = "khaki1")
canvas.pack()

x = 500
y = 500
def mexičanbok(x,y):
    canvas.create_oval(x-35,y-5,x+35,y+5,fill="black",tag = "mexičan")
    canvas.create_oval(x-25,y-25,x+25,y+25,fill="brown",tag = "mexičan")
    canvas.create_oval(x-15,y-15,x+15,y+15,fill="yellow",tag = "mexičan")

def mexičanhore(x,y):
    canvas.create_oval(x-5,y-35,x+5,y+35,fill="black",tag = "mexičan")
    canvas.create_oval(x-25,y-25,x+25,y+25,fill="brown",tag = "mexičan")
    canvas.create_oval(x-15,y-15,x+15,y+15,fill="yellow",tag = "mexičan")
def cactus (x1,y1):
    canvas.create_oval(x-20,y-20,x+20,y+20,fill = "green")
    canvas.create_oval(x -30 - 10, y - 10, x - 10 - 10, y + 10, fill="green")
    canvas.create_oval(x + 30 + 10, y - 10, x + 10 + 10, y + 10, fill="green")


for i in range (15):
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    cactus(x,y)
def movement(event):
    global x, y, x1,y1
    if event.char == "d":
        canvas.delete("mexičan")
        x += 10
        mexičanbok(x,y)
    elif event.char == "w":
        canvas.delete("mexičan")
        y -= 10
        mexičanhore(x,y)
    elif event.char == "a":
        canvas.delete("mexičan")
        x -= 10
        mexičanbok(x,y)
    elif event.char == "s":
        canvas.delete("mexičan")
        y += 10
        mexičanhore(x,y)

    canvas.update()
    canvas.after(25)


mainwin.bind("<Key>", movement)
mainwin.mainloop()