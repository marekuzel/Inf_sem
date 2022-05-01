from tkinter import *
osize = 500
mainwin = Tk()
canvas = Canvas (mainwin, width= osize, height = osize )
canvas.pack()

with open ("subor 1", "r") as r:
    x = r.readlines()
for i in range(len(x)):
        x[i] = x[i].replace("\n", "")
for i in range (len(x)):
    if x[i] == "K":
        canvas.create_oval(x[i+1],x[i+2],x[i+3],x[i+4],fill = "green")
    elif x[i] == "O":
        canvas.create_rectangle(x[i + 1], x[i + 2], x[i + 3], x[i + 4], fill = "green")
        print ((int(x[i+3])-int(x[i+1])) * (int(x[i+4])-int(x[i+2])))

mainwin.mainloop()