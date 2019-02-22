import turtle

wn = turtle.Screen()
wn.bgcolor("mint cream")

vc = 0
va = 15
vl = 250
lc = 0
la = 10
ll = 200

v = turtle.Turtle()
l = turtle.Turtle()

v.color("green")
v.pensize(2)
l.color("blue")
l.pensize(2)

v.speed("fast")
l.speed("fast")

v.up()
l.up()

v.backward(vl/2)
l.backward(ll/2)

v.down()
l.down()

while vc < 720 or lc < 720:
    # print(vc, lc)
    if vc < 720:
        v.forward(vl)
        v.left(180 - va)
    if lc < 720:
        l.forward(ll)
        l.left(180 - la)
    vc += va
    lc += la

wn.exitonclick()
print(vc, lc)
