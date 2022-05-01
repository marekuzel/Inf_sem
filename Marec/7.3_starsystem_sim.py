from tkinter import *
import math
mainwin = Tk()
CANVAS_SIZE = 1000
AU = 149597870.7 #km in one astronomical unit
PI = 3.1415 #being generous
SCALE = 1000
canvas = Canvas (mainwin, width = CANVAS_SIZE, height = CANVAS_SIZE, bg = "Black")
canvas.pack()

class Planet:
    def __init__(self, weight, radius, distance, velocity_x, velocity_y, sun, color, tag):
        self.weight = weight
        self.radius = radius
        self.distance = distance
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.sun = sun
        self.color = color
        self.tag = tag
    def draw(self):
        if self.sun == True:
            canvas.create_oval (CANVAS_SIZE/2 - self.radius/2, CANVAS_SIZE/2 - self.radius/2, CANVAS_SIZE/2 + self.radius/2, CANVAS_SIZE/2 + self.radius/2, fill = self.color, tags = self.tag)
        else:
            canvas.create_oval(CANVAS_SIZE/2 - self.radius/2 - self.distance, )
sun = Planet (1.989*10**30, 50, 0, 0, 0,True, "Yellow", "Sun")
sun.draw()




mainwin.mainloop()