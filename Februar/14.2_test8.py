with open ("trojuholniky.txt","r") as r:
    r = r.readlines()
pravouhle, rovnostranne, rovnoramenne = 0, 0, 0

for i in r:
    i = i.split()
    i[0], i[1], i[2] = int(i[0]), int(i[1]), int(i[2])
    if i[0] > i[1] and i[0] > i[2]:
        najdlhsiaStrana = i[0]
        zvysneStrany = i[1]*i[1] + i[2]*i[2]
    elif i[1] > i[0] and i[1] > i[2]:
        najdlhsiaStrana = i[1]
        zvysneStrany = i[2]*i[2] + i[0]*i[0]
    else:
        najdlhsiaStrana = i[2]
        zvysneStrany = i[0]*i[0] + i[1]*i[1]
        
        
    if i[0] == i[1] and i[2] == i[0]:
        rovnostranne += 1
    elif i[0] == i[1] or i[1] == i[2]:
        rovnoramenne += 1
    elif (najdlhsiaStrana*najdlhsiaStrana) == zvysneStrany:
        pravouhle += 1
print (rovnostranne, rovnoramenne, pravouhle)