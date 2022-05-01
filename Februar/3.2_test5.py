from tkinter import *
mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()


def suradnice ():
    canvas.create_line (500, 0, 500, 1000)
    canvas.create_line (0, 500, 1000, 500)
suradnice ()

userInput = input ("Zadajte čísla:")
userInput = userInput.split(";")
if len(userInput) == 3:
    a = int(userInput[0])
    b = int(userInput[1])
    c = int(userInput[2])
    for i in range (20):
        canvas.create_line (i*5, (a*(i*i)+b*i + c)*5, i*5+1, (a*(i*i)+b*i + c)*5+1)
    canvas.update()
elif len(userInput) == 2:
    a = int(userInput[0])
    b = int(userInput[1])
elif len(userInput) == 1:
    a = int(userInput[0])
print (userInput, a)


mainwin.mainloop ()