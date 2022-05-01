x = int(input("počet štvorcov na jednej strane: "))
m = int(input("m: "))
if x%2 == 0:
    s = int(x / 2)
    for i in range(0, s):
        print ((("#"*m)+("."*m))*s)
        print((("." * m)+("#" * m)) * s)
else:
    s = int(x / 2)
    sz = int(x%2)
    for i in range(0, s):
        print((("#" * m) + ("." * m)) * s + ("#" * m))
        print((("." * m) + ("#" * m)) * s + ("." * m))
    print((("#" * m) + ("." * m)) * s + ("#" * m))
    #todo: nefunguje m dobre, asi staci dat print 2* ale neviem