import turtle
import math
import random

flo = turtle.Turtle()

flo.color("red" , "yellow")
flo.speed(10)
i = 1

while True:
    flo.forward(math.sqrt(i)*20)
    flo.left(180 -15)
    i = i+ 1


turtle.done()