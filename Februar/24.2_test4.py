"""Napíšte hru "hádaj na aké číslo myslím". 
Program si vymyslí číslo zo zadaného rozsahu a hovorí vám, či máte pridať a ubrať až do okamihu, kedy dané číslo uhádnete"""

userInputRozsah = int(input("Zadaj rozsah v ktorom bude hľadané číslo: "))
import random
randomCislo = random.randrange (0,userInputRozsah)
while userInputRozsah != randomCislo:
    userInput = int(input("Hľadané číslo"))
    if userInput < randomCislo:
        print (f"Číslo je väčšie ako {userInput}")
    elif userInput > randomCislo:
        print (f"Číslo je menšie ako {userInput}")
    else:
        break
print (f"uhádol si. číslo bolo {randomCislo}")