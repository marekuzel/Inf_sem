while True:
    userInput = input ("Zadaj požadovanú akciu (bez diakritiky): \nPridať ŠPZ   (Pridat)\nHľadať ŠPZ    (Hladat)\nSpočítať ŠPZ v okrese    (SpocitatOK)\nVypísať registrované ŠPZ v okrese     (Vypísat)\nSpočítať všetky ŠPZ     (SpocitatVS)\nVypnúť program      (zavriet)\n:")
    userInput = userInput.lower()
    if userInput == "pridat":
        userInputPridanie = input("Zadaj SPZ (napr. BL 000 XX): ")
        pridanie = open ("SPZ.txt", "a")
        pridanie.write(userInputPridanie + "\n")
        pridanie.close()
        userInput = ""
    elif userInput == "hladat":
        userInputHladanie = input("Zadaj hľadanú ŠPZ: ")
        with open ("SPZ.txt", "r") as r:
            r = r.readlines()
            r = (i.strip() for i in r)
        if userInputHladanie in r:
            print ("ŠPZ je v systéme")
        else:
            print ("ŠPZ nie je registorvaná v systéme")
    elif userInput == "spocitatok":
        userInputSpocitanie = input("Zadaj názov okresu: ")
        celkovyPocetOK = 0
        with open ("SPZ.txt", "r") as r:
            r = r.readlines()
        for i in r:
            if i[:2] == userInputSpocitanie:
                celkovyPocetOK += 1
        print (celkovyPocetOK)
    elif userInput == "vypisat":
        userInputVypisanie = input("Zadaj názov okresu: ")
        with open ("SPZ.txt", "r") as r:
            r = r.readlines()
        for i in r:
            if i[:2] == userInputVypisanie:
                print (i.strip())
    elif userInput == "spocitatvs":
        with open ("SPZ.txt", "r") as r:
            r = r.readlines()
        print (len(r))
    elif userInput == "zavriet":
        break