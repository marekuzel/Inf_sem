userInput = input ("Zadaj akciu:\nEvidovanie žiaka(Evidencia)\nVyhladanie žiaka(Vyhladanie)\nSpočítanie roku(spocitanie)\nVýpis roku (vypis)\nSpočítanie všetkých(spocitajVsetko)")
userInput = userInput.lower()

with open ("evidencia.txt", "r") as r:
        r = r.readlines()

if userInput == "evidencia":
    userInputEvid = input ("Zadaj ID žiaka (napr. 22 001) :")
    with open ("evidencia.txt", "a") as a:
        a.write (userInputEvid)
elif userInput == "vyhladanie":
    userInputVyhl = input ("Zadaj ID hľadaného žiaka: ")
    if userInputVyhl in r:
        print ("Žiak je v systéme")
elif userInput == "spocitanie":
    count= 0
    userInputSpoc = input ("Zadaj rok: ")
    for i in r:
        if i[:2] == userInputSpoc:
            count += 1
    print (count)
elif userInput == "vypis":
    userInputVyp = input ("Zadaj rok: ")
    for i in r:
        if i[:2] == userInputVyp:
            print (i)
elif userInput == "spocitajvsetko":
    count= 0
    for i in r:
        count += 1
    print (count)