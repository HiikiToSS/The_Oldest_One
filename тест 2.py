import random
import turtle

turtle.speed(100)

def mnogoug():
  leng = random.randint(20,60)
  for i in range(6):
    turtle.forward(leng)
    turtle.left(60)
  
def randPlace():
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

for i in range(10):
  mnogoug()
  randPlace()
turtle.exitonclick()