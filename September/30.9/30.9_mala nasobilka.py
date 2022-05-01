x = int(input("počet násobkov čísela: "))
l = []
for i in range (1,x+1):
    for j in range (1,11):
        h = j*i
        l.append(h)
    print (l)
    l=[]