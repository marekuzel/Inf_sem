with open ("obraz.txt", "r") as r:
    r = r.readlines()
negativ = ""
for i in r:
    for j in i:
        print (j)
        if j == "0":
            negativ += "1"
        elif j == "1":
            negativ += "0"
    negativ += "\n"
negativSubor = open ("negativ_obraz.txt", "a")
negativSubor.write (negativ)
negativSubor.close()
print (r,negativ)