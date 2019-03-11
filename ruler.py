w = 1000
h = 1000
newPage(w, h)

mainTick = 5
halfTick = mainTick * 0.75
smallTick = mainTick * 0.5
myStroke = .25

x = 0
y1 = h / 2

millimetres = True

if millimetres == True:
    unit = 2.835
    bigUnit = 10
else:
    unit = 1
    bigUnit = 12

while x <= w:
    curVal = round((x / unit), 3)
    if x == 0 or curVal % bigUnit == 0:
        y2 = y1 - mainTick
    elif curVal % (bigUnit / 2) == 0:
        y2 = y1 - halfTick
    else: 
        y2 = y1 - smallTick
    strokeWidth(myStroke)
    stroke(0)
    line((x, y1), (x, y2))
    if x != 0 and curVal % bigUnit == 0:
        fontSize = 6
        font("IBM Plex Mono Thin", fontSize)
        textY = y2 - fontSize * 1.2
        text(str(round(curVal/bigUnit)), (x, textY), align="center")
    x += unit    

