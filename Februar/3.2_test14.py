#V súbore rozhodcovia.txt sú uvedené hodnotenia športového výkonu jednotlivými rozhodcami. 
# Podľa pravidiel sa najvyššie a najnižšie hodnotenie neberú do úvahy.
# Aké je priemerné hodnotenie zvyšných rozhodcov? Napíšte program tak, aby to vedel vyhodnotiť. 
# Zároveň bude vedieť po zadaní mena vypísať bodové hodnotenie od daného rozhodcu, alebo, že sa rozhodca s týmto menom v súbore nenachádza.

with open ("rozhodcovia.txt", "r") as r:
    x = r.readlines()
lowestScore = 1000
highestScore = 0
mena = []
for i in x:
    i = i.split(" ")
    mena.append(i[1].strip())
    if float(i[0]) < lowestScore:
        lowestScore = float(i[0])
    elif float(i[0]) > highestScore:
        highestScore = float(i[0])
sum = 0
for i in range (len(x)):
    print (x[i])
    if x[i] != highestScore:
        if x[i] != lowestScore:
            sum += float(i)
print (sum)
print (sum/len(x)-2)
while True:
    inp = input("meno: ")
    for i in x:
        i = i.split(" ")
        if i[1].strip() == inp:
            print (i[0])
    if inp != i[1].strip():
        print ("nemame hraca s takymto menom")