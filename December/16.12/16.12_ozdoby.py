with open ("ozdoby", "r") as r:
    x = r.readlines()
dictionary = {}
for i in x:
    i = i.replace("\n", "")
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print (dictionary)
print ("Najviac je :", max(dictionary), "(", max(dictionary.values()), "kusov )")