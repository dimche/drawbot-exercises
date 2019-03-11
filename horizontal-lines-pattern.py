w = 200
h = 200
newPage(w, h)

padding = 13
rows = 9
cols = 9
horGap = 9
maxThickness = 12
minThickness = 3

stroke(0)

verGap = (h - padding * 2 - rows * maxThickness) / (rows - 1)
colWidth = (w - padding * 2 - horGap * (cols - 1)) / cols

rowCounter = 0
while rowCounter < rows:
    y1 = padding + maxThickness / 2 + (maxThickness + verGap) * rowCounter
    y2 = y1
    rowCounter += 1

    colCounter = 0
    while colCounter < cols:
        x1 = padding + (colWidth + horGap) * colCounter
        x2 = x1 + colWidth
        
        if colCounter <= (cols - 1) / 2:
            thickness = minThickness + (colCounter) * (maxThickness - minThickness) / floor((cols - 1) / 2)
            strokeWidth(thickness)
        else:
            thickness = minThickness + (cols - colCounter - 1) * (maxThickness - minThickness) / floor((cols - 1) / 2)
            strokeWidth(thickness)

        line((x1, y1), (x2, y2))
        print((colCounter + 1), round(thickness, 2))
        colCounter += 1