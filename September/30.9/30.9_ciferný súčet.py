import math
x = int(input("číslo: "))
c = []
y = 10
j = 0
while True:
    j += 1
    f = math.pow(10,j)
    c.append(((x % y)/f)*10)
    x = x - (x % y)
    if y>x:
        break
    y *= 10
sum = 0
for i in range (0,len(c)):
    sum += c[i]
print (c)
print (sum)