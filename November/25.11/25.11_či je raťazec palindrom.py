#Zistite, či je zadaný reťazec palindróm, nemyslite na veľké a malé písmená, medzery nezohľadňujte.
list_ = ["a","a","b"]
palindrom = ""
for i in range (int(len(list_)//2)):
    if list_[i] == list_[len(list_)-i-1]:
        palindrom = True
    else:
        palindrom = False
        break
if palindrom is True:
    print ("palindróm")
else:
    print ("nie palindróm")