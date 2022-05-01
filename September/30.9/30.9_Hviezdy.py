x = int(input("počet hviezd na prvom riadku: "))
y = x
z = []
for i in range (0,x):
    for j in range (0,y):
        z.append("*")
    print (" ".join(z)) #https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
    z = []
    y = x - i-1