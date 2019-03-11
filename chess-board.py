w = 200
h = 200
newPage(w, h)

light = .8
dark = .2

even = light
odd = dark

mySide = 24

rows = h // mySide
cols = w // mySide
paddingV = (h % mySide) / 2
paddingH = (w % mySide) / 2

rowCounter = 0
while rowCounter < rows:
    y = paddingV + mySide * rowCounter
    rowCounter += 1

    colCounter = 0
    while colCounter < cols:
        x = paddingH + mySide * colCounter
        if (rowCounter + colCounter) % 2 == 0:
            fill(odd)
        else:
            fill(even)

        rect(x, y, mySide, mySide)
        colCounter += 1

print(rows, "×", cols, "\rpadding:", paddingH)
