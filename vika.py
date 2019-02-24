import turtle

l = 400

v = turtle.Turtle()
v.screen.bgcolor("#808080")
v.speed("normal")
# v.color("#66FF66")
v.pensize(3)
v.up()
v.goto(-l/2,0)
v.down()
for x in range(37):
    v.color(x/37, x/37, x/37)
    v.forward(l)
    v.left(180-5)
v.hideturtle()