with open ("subor 2", "r") as r:
    x = r.readlines()
o = open("subor 3", "w")
for line in x:
    for char in range (len(line)):
        o.write (chr(ord(line[char])+3))

o.close()