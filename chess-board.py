newPage(200, 200)
w = width()
h = height()

dark = .2
light = .8

even = light
odd = dark

mySide = 20

rows = h // mySide
cols = rows
paddingV = (h % mySide) / 2
paddingH = (w % mySide) / 2

print("rows:", rows, "\rpadding:", paddingH, "\r ")

def isEven(counter):
    if counter % 2 != 0:
        return 1
    else:
        return 0

rowCounter = rows

while rowCounter > 0:
    if isEven(rowCounter):
        fill(odd)
    else:
        fill(even)
    print(rowCounter)
    rect(paddingH, paddingV + mySide * (rowCounter - 1), mySide, mySide)
    rowCounter -= 1
    
    colCounter = cols
    while colCounter > 1:
        if isEven(rowCounter):
            if isEven(colCounter):
                fill(even)
            else:
                fill(odd)
        else:
            if isEven(colCounter):
                fill(odd)
            else:
                fill(even)

        print('  ', colCounter)
        rect(paddingH + mySide * (colCounter - 1), paddingV + mySide * (rowCounter), mySide, mySide)
        colCounter -= 1