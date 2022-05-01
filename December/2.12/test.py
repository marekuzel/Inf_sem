x = ["a","h","o","j"]
y = ["x","x","x"]
x_f = []
for i in range (len(x)-1):
    x_f.append(x[i])
    for i in range(len(y)):
        x_f.append(y[i])
x_f.append(x[len(x)-1])

print (x_f)