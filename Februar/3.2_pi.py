with open ("pi.txt","r") as r:
    r = r.readline()
listDvojcislie = []
for i in range (len(str(r))):
    dvojcislie = str(r[i]) + str(r[i+1])
    if dvojcislie in listDvojcislie:
        print (listDvojcislie[i-1])
    else:
        listDvojcislie.append(dvojcislie)