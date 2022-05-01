import tkinter
import math

canvas=tkinter.Canvas(width=1024,height=521)
canvas.pack()

def ciara (event):
    global x_start,y_start
    x_start = event.x
    y_start = event.y
    
def hover (event):
    global x_start,y_start, xx,xy
    canvas.delete ("ciara")
    xx = event.x
    xy = event.y
    canvas.create_line (x_start,y_start, xx, xy, tags = "ciara")
    canvas.update()
    x_len = abs(x_start-xx)
    y_len = abs(y_start-xy)
    canvas.create_text (100,100, text=math.sqrt(x_len*x_len-y_len*y_len), tags = "ciara")

canvas.bind("<Button-1>", ciara)
canvas.bind("<B1-Motion>", hover)

tkinter.mainloop()