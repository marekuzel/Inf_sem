sudoku = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
dictionaryOfRows, row = {}, []
for i, s in enumerate(sudoku, start=1):
    row.append(s)
    if i % 9 == 0:
        dictionaryOfRows["sudokuRow{0}".format(int(i/9))] = row
        row = []

def getZero ():
    positionOfZeroX, positionOfZeroY = [],[]
    for i in range (1,10):
        xPos = 0
        for j in (dictionaryOfRows["sudokuRow{0}".format(int(i))]):
            xPos += 1
            if int(j) == 0:
                positionOfZeroX.append(xPos)
                positionOfZeroY.append(i)
    print(positionOfZeroX, positionOfZeroY)
getZero()