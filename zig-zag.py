w = 200
h = 200
newPage(w, h)

density = 10

stroke(0)
strokeWidth(3)

waveLen = w / density
step = 0
while step < density:
    y1 = h
    y2 = 0
    if step % 2 == 0:
        x1 = waveLen * step
        x2 = waveLen * (step + 1)
    else:
        x1 = waveLen * (step + 1)
        x2 = waveLen * step
    
    line((x1, y1), (x2, y2))
    print(step, '(', x1, y1, '), (', x2, y2, ')')
    step += 1