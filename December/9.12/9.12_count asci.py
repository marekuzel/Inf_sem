#todo: created by szeko34, dopisať kod
s = open("subor 2", "r")

subor=s.readlines()
print(subor)

znakov=0

for i in range(26):
    znak = chr(ord("a")+i)
    b = 0
    for r in subor:
        b += r.lower().count(znak)
    znakov += b

print(znakov)

for i in range(26):
    znak = chr(ord("a")+i)
    b = 0
    for r in subor:
        #b += r.count("a") + r.count("A")
        b += r.lower().count(znak)
    print(znak, b / znakov)

s.close()
