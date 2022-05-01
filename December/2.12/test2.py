#Napapípíštepe propograpam, ktoporypy ropobipi topotopo.

x = ["N","a"]
y = ["a","e","i","o","u","y"]
x_f = []

for i in range (len(x)):
    x_f.append(x[i])
    for j in y:
        if x[i] == j:
            x_f.append("p")
            x_f.append(x[i])
print (x_f)