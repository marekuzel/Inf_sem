from calendar import monthrange #https://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python

ui = int(input("zadaj aktuálny rok: "))
ui2 = int(input("zadaj mesiac: "))
ui3 = input("zadaj 1. deň v mesiaci: ")

x = monthrange(ui, ui2)

x = x[1]
workday = 0
if ui3 == "monday":
    workday += 5
    x -= 7
elif ui3 == "tuesday":
    workday += 4
    x -= 6
elif ui3 == "wednesday":
    workday += 3
    x -= 5
elif ui3 == "thursday":
    workday += 2
    x -= 4
elif ui3 == "friday":
    workday += 1
    x -= 3
elif ui3 == "saturday":
    x -= 2
else:
    x-=1

workday += (x//7)*5

if x%7 >= 5:
    workday += x % 7
else:
    x += 5
print (workday)
