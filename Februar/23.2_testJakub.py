userInput = input ("Napíš číslo: ")
for i in range (1,len(userInput)+1):
    if i%3 == 0:
        print (" " + userInput[i-1],end = "")
    else:
        print (userInput[i-1],end = "")