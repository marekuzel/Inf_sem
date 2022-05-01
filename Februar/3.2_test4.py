from tkinter import *
mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()

def kruh (x,y, polomer, farba, oznacenie):
    canvas.create_oval(x - polomer, y - polomer, x + polomer, y + polomer, fill = farba, tags = oznacenie)
                
kruh(500, 600,50,  farba = "white", oznacenie = "prazdna")
kruh(500, 400,50,  farba = "white", oznacenie = "prazdna")
kruh(500, 200,50,  farba = "white", oznacenie = "prazdna")

def behSemaforu1():
    kruh(500, 200,50,  farba = "red", oznacenie = "cervena")
    canvas.update ()
    canvas.after (3000)
    behSemaforu2()
def behSemaforu2():
    kruh(500, 400,50,  farba = "orange", oznacenie = "oranzova")
    canvas.update()
    canvas.after (2000)
    canvas.delete ("oranzova")
    canvas.delete ("cervena")
    behSemaforu3()
def behSemaforu3():
    kruh(500, 600,50,  farba = "green", oznacenie = "zelena")
    canvas.update ()
    canvas.after (3000)
    

behSemaforu1
mainwin.mainloop()