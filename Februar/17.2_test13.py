import math
userInput = input ("napíš neznáme a, b, c: ")
userInput = userInput.split(",")
a,b,c = int(userInput[0]), int(userInput[1]), int(userInput[2])
diskriminant = (b*b) - (4*a*c)
if diskriminant < 0:
    print ("korene rovnice nemajú riešenie")
elif diskriminant == 0:
    x1 = (-1*b + math.sqrt(diskriminant))/(2*a)
    print (f"Rovnica má jedno riešenie, a tým je {x1}")
else:
    x1 = (-1*b + math.sqrt(diskriminant))/(2*a)
    x2 = (-1*b - math.sqrt(diskriminant))/(2*a)
    print (f"Rovnica má dve riešenia, a tým sú {x1} a {x2}")