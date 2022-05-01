from tkinter import *
mainwin = Tk()
canvas = Canvas(mainwin, width = 1000, height = 1000)
canvas.pack()

with open ("kalkulackoveCisla.txt","r") as r:
    x = r.readlines()

def prazdnyStvorec(x,y,r):
    canvas.create_rectangle(x-r,y-r,x+r,y+r)
def plnyStvorec(x,y,r):
    canvas.create_rectangle(x-r,y-r,x+r,y+r, fill = "black", tags = "Plny")

for i in range (0,5):
    for j in range (0,5):
        prazdnyStvorec(i*200, j*200, 200)
def funkcia():
    for i in range (0,9):
        jWatch = 5
        x[i] = x[i][1:]
        jCoord = 0
        iCoord = 0
        for j in range (0,len(x[i])):
            jCoord += 1
            if j > jWatch:
                jCoord = 0
                iCoord += 1
            if x[i][j] == "x":
                plnyStvorec(iCoord*200, jCoord*200, 200)
            elif x[i][j] == "0":
                prazdnyStvorec(iCoord*200, jCoord*200, 200)
        
    canvas.update()
    canvas.after (100)
    canvas.delete("Plny")
    funkcia()
funkcia()

mainwin.mainloop()