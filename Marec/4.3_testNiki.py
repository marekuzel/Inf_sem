from tkinter import *
import random
mainwin = Tk()
CANVAS_SIZE = 1000
canvas = Canvas (mainwin, height = CANVAS_SIZE, width = CANVAS_SIZE)
userInput,userInput2 = int(input ("Guess of first player: ")), int(input ("Guess of second player: "))
canvas.pack()

SIZE_OF_CUBE = 80
canvas.create_rectangle (CANVAS_SIZE-SIZE_OF_CUBE/2, CANVAS_SIZE-SIZE_OF_CUBE/2, CANVAS_SIZE+SIZE_OF_CUBE,CANVAS_SIZE+SIZE_OF_CUBE)
canvas.create_oval (CANVAS_SIZE-SIZE_OF_CUBE/5,CANVAS_SIZE-SIZE_OF_CUBE/5,CANVAS_SIZE+SIZE_OF_CUBE/5,CANVAS_SIZE+SIZE_OF_CUBE/5)

canvas.create_text (500, 100 , text = "Guess of first player is " + str(userInput) + " and guess of second player is " + str(userInput2))

class Kocka:
    def __init__(self, value):
        self.value = value
    def plain():
        for i in range (0,3):
            for j in range (0,3):
                canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+SIZE_OF_CUBE/3*i ,CANVAS_SIZE/2+SIZE_OF_CUBE/3*j )
    def hod(value):
        for i in range (0,3):
            for j in range (0,3):
                if value == 1:
                    if i == 1 and j == 1 :
                        canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+ SIZE_OF_CUBE/3*i,CANVAS_SIZE/2 + SIZE_OF_CUBE/3*j, fill = "black", tags = "kocka")
                if value == 2:
                    if i == 0 and j == 0 or i == 2 and j ==2:
                        canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+ SIZE_OF_CUBE/3*i,CANVAS_SIZE/2 + SIZE_OF_CUBE/3*j, fill = "black", tags = "kocka")
                elif value == 3:
                    if i == 0 and j == 0 or i == 2 and j ==2 or i == 1 and j == 1:
                        canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+ SIZE_OF_CUBE/3*i,CANVAS_SIZE/2 + SIZE_OF_CUBE/3*j, fill = "black", tags = "kocka")
                elif value == 4:
                    if i == 0 and j == 0 or i == 2 and j ==2 or i == 2 and j == 0 or i == 0 and j == 2 :
                        canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+ SIZE_OF_CUBE/3*i,CANVAS_SIZE/2 + SIZE_OF_CUBE/3*j, fill = "black", tags = "kocka")
                elif value == 5:
                    if i == 0 and j == 0 or i == 2 and j ==2 or i == 2 and j == 0 or i == 0 and j == 2 or i == 1 and j == 1:
                        canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+ SIZE_OF_CUBE/3*i,CANVAS_SIZE/2 + SIZE_OF_CUBE/3*j, fill = "black", tags = "kocka")    
                elif value == 6:
                    if i == 0 and j == 0 or i == 2 and j ==2 or i == 2 and j == 0 or i == 0 and j == 2 or i == 0 and j ==1 or i == 2 and j ==1:
                        canvas.create_rectangle (CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*i,CANVAS_SIZE/2-SIZE_OF_CUBE/3 + SIZE_OF_CUBE/3*j,CANVAS_SIZE/2+ SIZE_OF_CUBE/3*i,CANVAS_SIZE/2 + SIZE_OF_CUBE/3*j, fill = "black", tags = "kocka")  

Kocka.plain()

def main(throw):
    for i in range (int(throw)+1):
        global randomNumber
        randomNumber = random.randrange (0,6)
        Kocka.hod(randomNumber)
        canvas.update()
        if i < int(throw):
            canvas.after (50)
            canvas.delete ("kocka")
finalScore = 0
def hod(numberOfThrows):
    global finalScore
    for i in range (int(numberOfThrows)):
        main(10)
        canvas.create_text (500,200, text = randomNumber, tags = "text")
        finalScore += randomNumber
        canvas.after (5000)
        canvas.delete ("text")
hod(2)
if abs(userInput - finalScore) < abs(userInput2 - finalScore):
    canvas.create_text (500,700, text = "Player 1 won. Overall score is: " + str(finalScore))
else:
    canvas.create_text (500,700, text = "Player 2 won. Overall score is: : " + str(finalScore))
mainwin.mainloop()