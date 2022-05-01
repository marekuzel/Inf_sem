import random
userInput = int(input("Zadaj počet príkladov: "))
list1,list2, listOdpovedi = [],[], []

n=0
while n < userInput:
    cislo1,cislo2 = random.randint(0,9), random.randint(0,9)
    list1.append(cislo1)
    list2.append(cislo2)
    userInputOdpoved = int(input(f"{cislo1} . {cislo2} = "))
    listOdpovedi.append(userInputOdpoved)
    n += 1
counter = 0
for i in range(userInput):
    if listOdpovedi[i]== list1[i]*list2[i]:
        odpoved = list1[i]*list2[i]
        print ("spravna odpoved")
        print (f"spravne riesenie:{cislo1} . {cislo2} = {odpoved}")
        counter += 1
    elif listOdpovedi[i] != list1[i]*list2[i]:
        print ("nespravna odpoveď")
        odpoved = list1[i]*list2[i]
        print (f"spravne riesenie: {cislo1} . {cislo2} = {odpoved}")
print (f"Počet správnych odpovedí je {counter} z {userInput} príkladov")