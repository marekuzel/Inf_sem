cinx = int(input("Prvé číslo: "))
ciny = int(input("Druhé číslo: "))
cinz = int(input("Tretie číslo: "))

if cinx + ciny > cinz and ciny + cinz > cinx and cinz + ciny > cinx:
    print ("čísla sú strany trojuholníka")
else:
    print("čísla niesú strany trojuholníka")