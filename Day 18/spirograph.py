from turtle import Turtle, Screen, colormode
import random

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

t = Turtle()
colormode(255)
t.speed(0)
for i in range(0,360,5):
    t.setheading(i)
    t.color(random_colour())
    t.circle(100)


screen = Screen()
screen.exitonclick()