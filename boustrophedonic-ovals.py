side = 200
newPage(side, side)

padding = 10
gap = 5

rows = 9
cols = rows

maxDiam = (side - padding * 2 - gap * (rows - 1)) / rows

light = .8
dark = .2
even = light
odd = dark

counter = 0
while counter < rows * cols:
    if (counter // rows) % 2 == 0:
        diam = (maxDiam / cols) + (counter % cols) * (maxDiam - maxDiam / cols) / (cols - 1)
    else:
        diam = (maxDiam / cols) + (cols - counter % cols - 1) * (maxDiam - maxDiam / cols) / (cols - 1)
        
    x = padding + (maxDiam - diam) / 2 + (maxDiam + gap) * (counter % cols)
    y = padding + (maxDiam - diam) / 2 + (maxDiam + gap) * (counter // rows)
    
    if counter % 2 == 0:
        fill(odd)
    else:
        fill(even)

    oval(x, y, diam, diam)
    counter += 1
    
    print(round(x, 1), round(y, 1), round(diam, 1))