# V súbore farby.txt sú vypísané farby v RGB kóde po riadkoch s tým, že počet znakov predstavuje sýtosť farby.
# Zobrazte kódy týchto farieb v klasickom zápise a vykreslite aspoň jeden obdĺžnik danej farby. ( f'#{r:02x}{g:02x}{b:02x}')

from tkinter import*
mainwin = Tk()
canvas = Canvas (mainwin , height = 1000, width = 1000)
canvas.pack()

with open ("rgb.txt", "r") as r:
    x = r.readlines()

for i in range (len(x)):
    r = x[i].count("R")
    g = x[i].count("G")
    b = x[i].count("B")
    canvas.create_rectangle (250,250, 750,750 , fill = f'#{r:02x}{g:02x}{b:02x}')
    canvas.update()
    canvas.after (500)
    canvas.delete ("all")

mainwin.mainloop()