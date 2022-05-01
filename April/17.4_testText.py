with open ("text.txt", "r", encoding="utf8") as r:
    r=r.readlines()
print (f"Počet znakov v súbore je {len(r[0])}")
r[0].lower()
newList = (word[0].upper() + word[1:] for word in r[0].split("."))
for i in newList:
    i = i + ". "
print (newList)