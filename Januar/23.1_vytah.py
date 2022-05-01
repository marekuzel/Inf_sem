from tkinter import *

mainwin = Tk()
canvas = Canvas (mainwin, height = 1000, width = 1000)
canvas.pack()
kdeSom = 0
def kruh (x, r):
    canvas.create_oval (x - r + 150, 500-r, x + r + 150, 500 + r)

def svetlo (x, r,  tag):
    canvas.create_oval (x - r + 150, 500-r, x + r + 150, 500 + r, tags = tag, fill = "yellow")
def zeleneSvetlo(x, r,  tag):
    canvas.create_oval (x - r + 150, 500-r, x + r + 150, 500 + r, tags = tag, fill = "green")
for i in range (0,5):
    kruh (i*150 , 50)
while True:
    kamIdem = int(input("Podlažie:"))
    if kamIdem > kdeSom:
        for i in range (kdeSom + 1, kamIdem + 1):
            svetlo (i*150 , 50 , "vysvietene")
            canvas.after (1000)
            canvas.update()
            canvas.delete ("vysvietene")
            if i == kamIdem:
                canvas.delete("vysvieteneZelene")
                canvas.update()
                zeleneSvetlo (i*150 , 50 , "vysvieteneZelene")
        kdeSom = kamIdem
    elif kdeSom > kamIdem:
        for i in range (kdeSom - 1, kamIdem - 1, -1):
            svetlo (i*150 , 50 , "vysvietene")
            canvas.after (1000)
            canvas.update()
            canvas.delete ("vysvietene")
            if i == kamIdem:
                canvas.delete("vysvieteneZelene")
                canvas.update()
                zeleneSvetlo (i*150 , 50 , "vysvieteneZelene")
        kdeSom = kamIdem
            
        
mainwin.mainloop()