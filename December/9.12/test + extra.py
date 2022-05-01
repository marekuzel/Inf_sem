with open ("subor 1", "r") as r:
    x = r.readlines()
print ("Výška stromu :" , len (x))
for s in x:
    s = s .replace ("\n","")
pocet_0 = 0
zle = 0
first_half = True
for i in range (len(x)):
    for j in x[i]:
        if j == "O":
            pocet_0 += 1
print ("Počet gúl:", pocet_0)
for i in range (len(x)):
    for a in range (len(x[i])):
        if a == "|":
            first_half = False
        if first_half is True:
            if a == "\\":
                zle += 1
        elif first_half is False:
            if a == "/":
                zle += 1
print (zle)