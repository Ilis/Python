import turtle

t = turtle.Turtle()

t.hideturtle()

t.speed("fastest")

t.screen.bgcolor("#1B1B1B")

t.up()
t.backward(256)
t.down()

for x in range(256):
    t.color(1-x/256.0, 0, x/256.0)
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.forward(2)
