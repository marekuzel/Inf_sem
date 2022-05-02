from  tkinter import *
import math

SIZE = 300
mainwin = Tk()
canvas = Canvas (mainwin, width = SIZE, height = SIZE)
canvas.pack()

with open ("body.txt", "r") as r:
    r = r.readlines()
x_bodu, y_bodu = [],[]

for counter,  i in enumerate (r):
    i = i.split()
    canvas.create_oval (int(i[0])-2.5, int(i[1])-2.5,int(i[0]) + 2.5, int(i[1]) + 2.5)
    canvas.create_text (int(i[0]), int(i[1])-10, text = counter)
    x_bodu.append(int(i[0]))
    y_bodu.append(int(i[1].strip()))
    
kliknutiePoradie = 0
print (r)
def kliknutie(e):#pamatat si kolkate kliknutie je a porovnavat ho s takym cislom v zozname r
    global kliknutiePoradie
    x = e.x
    y = e.y
    ciara = False
    if math.sqrt(((x-x_bodu[kliknutiePoradie])**2) + ((y-y_bodu[kliknutiePoradie])**2)) < 7:
        canvas.create_line (x_bodu[kliknutiePoradie-1], y_bodu[kliknutiePoradie-1],x_bodu[kliknutiePoradie], y_bodu[kliknutiePoradie])
        kliknutiePoradie += 1
    else:
        print ("nespravny bod")
canvas.bind ("<Button-1>", kliknutie)
mainwin.mainloop()