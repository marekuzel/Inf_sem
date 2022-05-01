"""14. Naprogramujte aplikáciu pre plánovanie leteckého výletu nad grafickou plochou.
    Let začína v ľavom hornom bode. Po kliknutí na plochu sa na danom mieste objaví očíslovaný bod trasy. 
    Po kliknutí pravým tlačidlom sa všetky body trasy prepoja najkratšou možnou cestou v zamýšľanom poradí navštívenia.
"""
"""14. Naprogramujte aplikáciu pre plánovanie leteckého výletu nad grafickou plochou.
    Let začína v ľavom hornom bode. Po kliknutí na plochu sa na danom mieste objaví očíslovaný bod trasy. 
    Po kliknutí pravým tlačidlom sa všetky body trasy prepoja najkratšou možnou cestou v zamýšľanom poradí navštívenia.
"""
import math
from tkinter import *
mainwin = Tk()
canvas = Canvas (mainwin, width = 1000, height = 1000)
canvas.pack()

začiatokLetuY, začiatokLetuX,bodyLetuListX, bodyLetuListY = 0,0, ["0"], ["0"]
početKliknuti = 0
palivo = 1500
def kliknutie (e):
    global početKliknuti
    početKliknuti += 1
    x = e.x
    y = e.y
    bodyLetuListX.append (x)
    bodyLetuListY.append (y)
    canvas.create_text (x, y,text = početKliknuti)
    canvas.update()
    
def spojenie (e):
    for i in range (početKliknuti):
        bodyLetuListX[i] = int (bodyLetuListX[i])
        if palivo < math.sqrt((bodyLetuListX[i] - bodyLetuListX[i+1])**2 + (bodyLetuListY[i] -bodyLetuListY[i+1])**2):
            print ("ehh")
        else:
            print (bodyLetuListX), int(bodyLetuListY[i]), int(bodyLetuListX[i+1]), int(bodyLetuListY[i+1]))
            canvas.create_line (bodyLetuListX, int(bodyLetuListY[i]), int(bodyLetuListX[i+1]), int(bodyLetuListY[i+1]))
            canvas.update()
            
canvas.bind ("<Button-1>", kliknutie)
canvas.bind("<Button-3>", spojenie)
mainwin.mainloop()