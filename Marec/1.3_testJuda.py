userInput = input ("Číslo, akcia, číslo (oddeliť čiarkami): ")
userInput = userInput.split(",")
cislo1, cislo2, akcia = int(userInput[0]), int(userInput[2]), userInput[1]
if akcia == "*":
    print (cislo1*cislo2)
elif akcia == "+":
    print (cislo1 + cislo2)
elif akcia == "-":
    print (cislo1 - cislo2)
elif akcia == "**":
    print (cislo1**cislo2)
elif akcia == "/":
    print (cislo1/cislo2)