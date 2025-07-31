from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.fd(10)

screen.listen()
screen.onkey(fun = move_forward, key = "space")
screen.exitonclick()