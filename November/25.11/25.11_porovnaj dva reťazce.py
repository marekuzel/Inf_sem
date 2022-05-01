#Porovnajte dva reťazce a vypíšte len tie znaky, ktoré sú rovnaké na rovnakých pozíciách.
list_a = ["a","b","c", "d"]
list_b = ["v","b","i", "d", "e"]
ind = 0
for i in list_a:
    if ind <= len(list_b) and i == list_b[ind]:
        print (i)
    ind += 1