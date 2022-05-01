from tkinter import *
mainwin = Tk()

with open ("mapa.txt", "r") as r:
    r = r.readlines()

rozmery = r[0].split()
WIDTH, HEIGHT = int(rozmery[0].strip()), int (rozmery[1].strip())

canvas = Canvas (mainwin, width = WIDTH*50, height = HEIGHT*50)
canvas.pack()

for i in range (1,WIDTH-1):
    r[i] = r[i].strip()
    for j in range (HEIGHT):
        if r[i][j] == "R":
            colorOfThePixel = "red"
        elif r[i][j] == "G":
            colorOfThePixel = "green"
        else:
            colorOfThePixel = "blue"
        canvas.create_rectangle(i*50, j*50, i*50 + 50, j* 50 + 50, fill = colorOfThePixel)

mainwin.mainloop()