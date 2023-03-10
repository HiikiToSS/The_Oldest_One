import turtle
turtle.speed(20)
def trungles():
    for i in range(2):
        turtle.forward(140)
        turtle.left(120)
    turtle.forward(140)
for i in range(3):
    trungles()
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
turtle.exitonclick()