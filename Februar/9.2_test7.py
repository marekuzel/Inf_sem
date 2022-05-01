"""
7.  In A Hole In The Ground There Lived A Hobbit
Vzdajme hold tomuto dielu tým, že každé jedno začiatočné písmeno slova bude veľké. Upravte tak vstupný súbor hobit.txt.
Navyše niekto zabudol, že za čiarkou sa má písať medzera, preto sa pozrite aj na to a pokúste sa za každú čiarku do textu vložiť medzeru.
Nech program tiež zistí počet slov v texte (pozor na pomlčky).
"""
with open ("hobit.txt", "r") as r:
    x = r.readlines()
x_final = []
x = x[0].split()
for i in range (len(x)):
    if "," in x[i]:
        position = int(x[i].find(","))+1
        x_final.append (x[i][:position] + " " + x[i][position:])
        print (x[i][:position] + " " + x[i][position:])
    elif "-" in x[i]:
        position = int(x[i].find("-"))
        x_final.append (x[i][:position] + " " + x[i][position:])
    else:
        x_final.append(x[i])
for i in range (len(x_final)):
    x_final[i] = x_final[i].capitalize()

print (x_final, len(x))
