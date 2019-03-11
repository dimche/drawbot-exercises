w = 490
h = 432
newPage(w, h)

density = 10
vertical = False

if vertical == True:
    side = w
else:
    side = h
myStroke = side / density

step = 1
while step <= density:
    if step % 2 == 0:
        stroke(1)
    else:
        stroke(0)
    if vertical == True:
        x1 = (step - .5) * myStroke
        x2 = x1
        y1 = 0
        y2 = h
    else:
        x1 = 0
        x2 = w
        y1 = (step - .5) * myStroke
        y2 = y1

    strokeWidth(myStroke)
    line((x1, y1), (x2, y2))
    print(step)
    step += 1
