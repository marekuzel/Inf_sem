import random
from tkinter import *
mainwin = Tk() 
sirka=400
vyska=400
 
p=Canvas(mainwin, height=vyska,width=sirka)
p.pack()
 
def italy():
    for i in range(1000):
        x=random.randint(0,sirka)
        y=random.randint(0,vyska)
        if x<=vyska/3:
            farba="green"
        elif x<=2*vyska/3:
            farba="white"
        else:
            farba="red"
        p.create_oval(x,y,x+3,y+3,fill=farba)
 
def japan():
    for i in range(1000):
        x=random.randint(0,sirka)
        y=random.randint(0,vyska)
        if abs(x-200) < 50:
            if abs(y-200) < 50:
                farba = "red"
        else:
            farba = "white"
        p.create_oval(x,y,x+3,y+3,fill=farba)
            
 
 
if random.randint(0,1)==0:
    italy()
    p.update()
    p.after(200)
else:
    japan()
    p.update()
    p.after(200)
mainwin.mainloop()