with open ("mena.txt", "r", encoding="utf-8") as r:
    r = r.readlines()
for i in range (1,len(r)):
    meno = r[i].split()
    lowMeno1, lowMeno2 = meno[0][:3].lower(),meno[1][:2].lower()
    print (lowMeno1+lowMeno2)