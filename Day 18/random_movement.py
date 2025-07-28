from turtle import Turtle, Screen
import random

t = Turtle()
direction = [0, 90, 180, 270]

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    t.color(R,G,B)

def move_random_path():
    t.setheading(random.choice(direction))
    t.fd(20)
    
t.speed(10)
t.pensize(8)

for i in range(200):
    change_color()
    move_random_path()

screen = Screen()
screen.exitonclick()