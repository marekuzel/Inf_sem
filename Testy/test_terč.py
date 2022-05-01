import random
import math
from tkinter import *
mainwin = Tk()
size = 1000
canvas = Canvas (mainwin, width = size, height = size)
canvas.pack()
wid = 300
wdth = (wid/10)
nepl_pokus = 0
poč_bodov = 0
def terč(wid):
    for i in range (0,10):
        canvas.create_oval(500-wid/2,500-wid/2,500+wid/2,wid/2+500)
        wid -= wdth

for i in range (0,3):
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    if y < 500:
        yq = 500 - y
    else:
        yq = y - 500
    if x < 500:
        xq = 500 - x
    else:
        xq = x - 500
    c = math.sqrt(xq**2 + yq**2)
    if c<wdth:
        poč_bodov += 10
    elif c<wdth*2:
        poč_bodov += 9
    elif c< wdth*3:
        poč_bodov += 8
    elif c < wdth * 4:
        poč_bodov += 7
    elif c < wdth * 5:
        poč_bodov += 5
    elif c < wdth * 6:
        poč_bodov += 4
    elif c < wdth * 7:
        poč_bodov += 3
    elif c < wdth * 8:
        poč_bodov += 2
    elif c < wdth * 9:
        poč_bodov += 1
    elif c > wid:
        nepl_pokus += 1

    print (xq,yq)
    canvas.create_oval(x-2,y-2,x+2,y+2)
if nepl_pokus == 3:
    print ("neplatný pokus")
else:
    print (poč_bodov)
terč(wid)
mainwin.mainloop()