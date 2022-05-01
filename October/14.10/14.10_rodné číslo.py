cin = int(input("Rodné číslo bez /: "))

if cin%11 == 0:
    print ("rodné číslo sedí")
else:
    print ("nerodné číslo")
scin = str(cin)
s = 0
for i in range (0,len(scin)):
    s += int(scin[i])
if s%11 == 0:
    print ("ciferný súčet je delitelný 11")
else:
    print("neciferný súčet je delitelný 11")