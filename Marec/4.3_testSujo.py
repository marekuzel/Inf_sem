from tkinter import *
import random
mainwin = Tk()
CANVAS_SIZE =1000
canvas = Canvas (mainwin, width = CANVAS_SIZE, height = CANVAS_SIZE)
canvas.pack()



class Runner:
    def __init__ (self, velocity, radius,pos_x, pos_y):
        self.velocity = velocity
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
    def motion(self):
        self.pos_x += self.velocity    
    def get_graphic (self):
        canvas.create_oval (self.pos_x - self.radius,self.pos_y - self.radius, self.pos_x + self.radius,self.pos_y + self.radius)
def start (e):
    x=e.x
    y=e.y
    beh()
    
d,listOfRunners = {},[]
numberOfRunners, speedestRunner, nOfRunner = 12, 0, 0
for i in range (0,numberOfRunners):
    speed = random.randrange (10,30)
    if speed > speedestRunner:
        speedestRunner = speed
        nOfRunner = i
    d["bezec{}".format(i)] = Runner (speed,5,0,100+i*(600/numberOfRunners)) #https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
    listOfRunners.append (d["bezec{}".format(i)])
    canvas.create_text (10,100+i*(600/numberOfRunners),text = i)

canvas.create_text (500,50, text = f"Click to start the race, number {nOfRunner} will win")

def beh():
    for i in range (500):
        for x in listOfRunners:
            x.motion()
            x.get_graphic()
        canvas.update()
        canvas.after(100)
        canvas.delete ("all")

canvas.bind("<Button-1>", start)

mainwin.mainloop()