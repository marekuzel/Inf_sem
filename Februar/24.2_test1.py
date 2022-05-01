from tkinter import *
import random
mainwin = Tk()
rozmer = 1000
canvas = Canvas (mainwin, width = rozmer, height = rozmer)
canvas.pack()

userInput = input ("Zadaj rozsah a počet ťahov, napr. (1-100,5): ")
if "-" not in userInput or "," not in userInput:
    print ("incorrect format")
userInput = userInput.split(",")
userInput[0] = userInput[0].split ("-")
spodRozsah, horRozsah, randList = userInput[0][0], userInput[0][1], []

def tah(spodRozsah, horRozsah, počTahov):
    while len(randList) != počTahov:
        nahodneCislo = random.randrange(spodRozsah, horRozsah)
        if nahodneCislo not in randList:
             randList.append (nahodneCislo)
             
    for i in range (počTahov):
        strana = rozmer/(počTahov*2)
        canvas.create_oval (2*i*strana,500 - strana/2,strana+2*i*strana, 500 + strana/2)
        canvas.create_text (2*i*strana + strana/2, 500, text = randList[i])
        canvas.after (800)
        canvas.update()

tah (int(spodRozsah), int(horRozsah), int(userInput[1]))

mainwin.mainloop()