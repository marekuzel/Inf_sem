import random

userInput,output = input("Pre Číslo zadaj C, pre malé písmeno zadaj M, a pre veľké písmeno zadaj : "), ""
for i in userInput:
    if i == "C":
        nahodna = chr(random.randrange (48,58))
    elif i == "M":
        nahodna = chr(random.randrange(97,123))
    elif i == "V":
        nahodna = chr(random.randrange(65,91))
    output += str(nahodna)
print (output)