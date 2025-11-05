from gturtle import *
t = makeTurtle()
t.hideTurtle()

p = 8
w = 240
h = 240
x = -w//2
y = h//2
c = 0
d = 0
e = 0

t.setPenWidth(p)
t.setPenColor("red")
t.setPos(x, y)
t.right(90)
repeat h//p:
    repeat w//p:
        t.forward(p)
        x = x + p
        if abs(x) < (c*p):
            setPenColor("black")
        else:
            setPenColor("red")

    if d < 15:
        d = d + 1
        c = c + 1

    if d >= 15:
        c = c - 1

    y = y - p
    x = -w//2
    t.setPos(-w//2, y)