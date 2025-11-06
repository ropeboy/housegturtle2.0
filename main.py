from gturtle import* 
t = makeTurtle

p = 8
w = 240
h = 240
x = -w//2
y = h//2
c = 0
d = 0

t = setPenWidth(p)
t.setPenColor("red")
t.setPos(x, y)
t.right(90)
repeat h//p:
    repeat w//p:
        forward(p)
        x = x + p
        if abs(x) < (c*p):
            t.setPenColor("black")
        else:
            t.setPenColor("red")
    if d < 15:
        d = d + 1
        c = c + 1
    if c >= 15:
        c = c - 2

    y = y - p
    x = -w//2
    setPos(-w//2, y)




