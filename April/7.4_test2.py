with open ("trojuholnik.txt", "r") as r:
    r = r.readlines()
rovnostranne, pravouhle, rovnostranne_aj_pravouhle = 0,0,0
for i in r:
    i = i.strip()
    i = i.split(" ")
    i.sort()

    strana3, strana2, strana1 = int(i[0]), int(i[1]), int(i[2])
    if strana1**2 == strana2**2 + strana3**2:
        pravouhle += 1
        if strana1 == strana2 or strana2 == strana3 or strana3 == strana1:
            rovnostranne_aj_pravouhle += 1
    if strana1 == strana2 or strana2 == strana3 or strana3 == strana1:
        rovnostranne += 1
        if strana1**2 == strana2**2 + strana3**2:
            rovnostranne_aj_pravouhle += 1
            
print (rovnostranne_aj_pravouhle,pravouhle, rovnostranne)