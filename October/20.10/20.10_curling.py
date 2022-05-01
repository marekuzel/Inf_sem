import random
import math
from tkinter import *
mainwin = Tk()
size = 1000
canvas = Canvas (mainwin, width = size, height = size)
canvas.pack()

def draha(wid):
    colors = ["blue", "white", "red", "white"]
    osize = (wid/3)
    sosize = osize/2
    msize = 0
    canvas.create_rectangle(2,(size/2)-(wid/2),size,(size/2)+(wid/2))

    for i in range (0,4):
        canvas.create_oval((size*0.8)-osize+msize/2,500-osize+msize/2, (size*0.8) + osize-msize/2, 500 + osize-msize/2, fill = colors[i])
        msize += sosize
def kameň1(x,y, ksize):
    canvas.create_oval(x - ksize,y - ksize,x+ ksize,y+ ksize, fill = "green")
def kameň2(x,y, ksize):
    canvas.create_oval(x - ksize,y - ksize,x+ ksize,y+ ksize, fill = "pink")


ksize = 10 #veľkosť kameňov
wid = 300 #širka drahy
draha(wid)
k1dist = 1000

for i in range (0,8):
    x = random.randint(500+ksize, size - ksize)
    y = random.randint(wid + ksize, size - (wid + ksize))
    if y < 500:
        yq = 500 - y
    else:
        yq = y - 500
    if x < (0.8*size):
        xq = 0.8*size - x
    else:
        xq = x - (0.8*size)

    f1 = xq * xq + yq * yq
    dist1 = math.sqrt(f1)
    if dist1 < k1dist:
        k1dist = dist1
    kameň1(x,y, ksize)

k2dist = 1000
for i in range (0,8):
    x = random.randint(500 + ksize, size - ksize)
    y = random.randint(wid + ksize, size - (wid + ksize))
    if y < 500:
        yq = 500-y
    else:
        yq = y - 500
    if x < (0.8 * size):
        xq = 0.8 * size - x
    else:
        xq = x - (0.8*size)
    print (xq, yq)
    f2 = xq ** 2 + yq ** 2
    dist2 = math.sqrt(f2)
    if dist2 < k2dist:
        k2dist = dist2
    kameň2 (x,y, ksize)
if k2dist > k1dist:
    canvas.create_rectangle(2,(size/2)-(wid/2),size,(size/2)+(wid/2), outline="green")
else:
    canvas.create_rectangle(2, (size / 2) - (wid / 2), size, (size / 2) + (wid / 2), outline="pink")
print (k1dist, k2dist)
mainwin.mainloop()