from turtle import Turtle, Screen

bob = Turtle()

for i in range(0,4):
    bob.forward(100)
    bob.right(90)

screen = Screen()
screen.exitonclick()
