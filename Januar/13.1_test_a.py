import math
with open("Test_a_input", "r") as r:
    x = r.readlines()
listInput = []
Area = 0
biggestArea = 0
biggestType = ""
finalType = ""
for line in range(len(x)):
    x[line] = x[line].replace("\n", "")
    listInput.append(x[line].split())
    x1 = int(listInput[line][1])
    y1 = int(listInput[line][2])
    x2 = int(listInput[line][3])
    y2 = int(listInput[line][4])
    if listInput[line][0] == "K":
        Area = abs(x2 - x1) * abs(y2 - y1)
        biggestType = "kvader"
    elif listInput[line][0] == "O":
        Area = (abs(x2 - x1) / 2) * (abs(y2 - y1) / 2) * math.pi
        biggestType = "oval"
    if Area > biggestArea:
        biggestArea = Area
        finalType = biggestType
print(biggestArea, finalType)
