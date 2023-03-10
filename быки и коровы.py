import turtle
import random
def g():
  f=["black"]
  for i in range(50):
    g=random.choice(f)
    turtle.color(g)
    turtle.begin_fill('red')
    turtle.end_fill()
    turtle.circle(i-0.1,280)
    turtle.right(25)
g()