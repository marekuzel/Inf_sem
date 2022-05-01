with open ("pecenie", "r") as r:
    x = r.readlines()
dictionary = {}
for i in x:
    i = i.replace ("\n", "")
    x_list = i.split()
    if x_list[0] not in dictionary:
        dictionary [x_list[0]] = int(x_list[1])
    else:
        dictionary[x_list[0]] += int(x_list[1])
rovnako = max(dictionary.values())
print (dictionary)
for i in dictionary:
    if dictionary[i] < rovnako:
        print ("treba dopiecť :", i,rovnako - dictionary[i])
