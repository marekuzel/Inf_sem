cinx = int(input("Číslo 1: "))
ciny = int(input("Číslo 2: "))

if cinx == ciny:
    print (str(cinx) + " = " + str(ciny))
elif cinx > ciny:
    print(str(cinx) + " > " + str(ciny))
else:
    print(str(cinx) + " < " + str(ciny))