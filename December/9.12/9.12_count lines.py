with open ("subor 2", "r") as r:
    x = r.readlines()
num = {}
for i in range (len(x)):
    for j in x[i].replace("\n",""):
        j = j.lower()
        if j in num:
            num[j] += 1
        else:
            num[j] = 1
print (num)