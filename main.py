from gturtle import *
t = makeTurtle()
t.setPenWidth(4)
t.setPenColor("red")
#t.hideTurtle()

w = 120
h = 120
x = -w//2
y = h//2

c = 0
p = 4
d = 0

setPos(x, y)
t.right(90)
repeat h//p:
    repeat w//p:
        t.forward(p)
        x = x + p
        if abs(x) < (c*4):
            setPenColor("black")
        else:
            setPenColor("red")
    if d < 15:
        c = c + 1
        d = d + 1
    if c >= 15:
        c = c - 2
    y = y - p
    x = -w//2
    t.setPos(-w//2, y)