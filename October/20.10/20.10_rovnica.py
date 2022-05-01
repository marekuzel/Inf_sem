import math
ui = input ("Napíš koeficienty kvadratickej rovnice :")


ui = ui.replace(" ", "")
ui = ui.split(",")



a = int(ui[0])
b = int(ui[1])
c = int(ui[2])
if (b**2)-(4*a*c) == 0:
    x1 = ((b*-1) + (math.sqrt((b**2)-(4*a*c))))/(2*a)
    print(str(x1) + "," + "rovnica má jeden koreň")
elif (b**2)-(4*a*c) < 0 :
    print ("rovnica nemá korene")
else:
    x1 = ((b*-1) + (math.sqrt((b**2)-(4*a*c))))/(2*a)

    x2 = ((b*-1) - (math.sqrt((b**2)-(4*a*c))))/(2*a)
    print (str(x1) + "," + str(x2) + "," + "rovnica má dva korene")