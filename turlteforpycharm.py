import turtle as t

t.width(4)
t.color("red")

w = 120
h = 120
x = -w // 2
y = h // 2

c = 0
p = 4
d = 0

t.penup()
t.setpos(x, y)
t.pendown()
t.right(90)

for _ in range(h // p):
    for _ in range(w // p):
        t.forward(p)
        x += p
        if abs(x) < (c * 4):
            t.color("black")
        else:
            t.color("red")
    if d < 15:
        c += 1
        d += 1
    if c >= 15:
        c -= 2
    y -= p
    x = -w // 2
    t.penup()
    t.setpos(-w // 2, y)
    t.pendown()

t.hideturtle()
t.done()
