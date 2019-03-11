side = 200
newPage(side, side)

density = 20

stroke(0)
strokeWidth(1)

gap = side / density
step = 0
while step < density:
    x1 = 0
    x2 = gap * (step + 1)    
    y1 = gap * step
    y2 = side
    line((x1, y1), (x2, y2))
    
    x1 = gap * step
    x2 = side
    y1 = 0
    y2 = gap * (step + 1)
    line((x1, y1), (x2, y2))
    
    print(step, '(', x1, y1, '), (', x2, y2, ')')
    step += 1