with open ("sei_znamky.txt", "r") as r:
    r = r.readlines()
for i in r:
    clovek = i.split()
    priemer = []
    for j in clovek:
        if "/" in j:
            x = j.split("/")
            priemer.append (float(x[0])/float(x[1]))
        elif j == "a":
            priemer.append (0)
    print (clovek[0], sum(priemer)/len(priemer))
    priemer = []