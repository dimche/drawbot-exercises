side = 200
newPage(side, side)

density = 20

stroke(0, .4, .8)
strokeWidth(.25)

gap = side / density
step = 0
while step < density:

    x1 = 0
    x2 = gap / 2 * (step + 1)    
    y1 = (gap * step + side) / 2
    y2 = side
    line((x1, y1), (x2, y2))
    
    # print(step, '(', x1, y1, '), (', x2, y2, ')')
    
    x1 = (gap * step + side) / 2
    x2 = side
    y1 = 0
    y2 = gap / 2 * (step + 1)
    line((x1, y1), (x2, y2))
    
    # print(step, '(', x1, y1, '), (', x2, y2, ')')
    
    x1 = side - (gap * (step + 1)) / 2
    x2 = side
    y1 = side
    y2 = (gap * step + side) / 2
    line((x1, y1), (x2, y2))
    
    # print(step, '(', x1, y1, '), (', x2, y2, ')')
    
    x1 = gap * (step + 1) / 2
    x2 = 0
    y1 = 0
    y2 = (side - (gap * step)) / 2
    line((x1, y1), (x2, y2))
    
    # print(step, '(', x1, y1, '), (', x2, y2, ')')
    
    step += 1