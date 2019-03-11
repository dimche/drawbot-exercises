w = 200
h = 200
newPage(w, h)

rows = 10
steps = 25

rowHeight = h / rows
stepWidth = w / steps

curRow = 0
while curRow < h:
    y = rowHeight * curRow
    curRow += 1

    curStep = 0
    while curStep < steps:
        x = stepWidth * curStep
        if curRow % 2 == 0:
            fill(1 - 1 / steps * curStep)
        else:
            fill(1 / steps * curStep)

        rect(x, y, stepWidth, rowHeight)
        curStep += 1