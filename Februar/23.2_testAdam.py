import random
listOfWeapons = ["kameň", "papier", "nožnice"]
while True:
    userInput = input ("Napíš kameň, Papier, Nožnice [môžeš skúsiť bombu]: ")
    userInput = userInput.lower()
    randomWeapon = random.choice (listOfWeapons)
    if userInput == "bomba":
        print ("Vyhral si... although this seems like cheating")
        
    elif userInput == randomWeapon:
        print ("Vyzerá to na remízu, skús znovu")
        continue
    elif randomWeapon == "kameň":
        if userInput == "papier":
            print ("Vyhral si... tento krát")
        elif userInput == "nožnice":
            print ("Prehral si")
    elif randomWeapon == "papier":
        if userInput == "kameň":
            print ("Prehral si")
        else:
            print ("Výhra!")
    elif randomWeapon == "nožnice":
        if userInput == "kameň":
            print ("Výhra")
        else:
            print ("prečo by si si vybral papier?. Jasná prehra... proti nožniciam papier?")