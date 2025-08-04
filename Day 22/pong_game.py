from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 900, height = 700)
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True
paddle1 = Paddle( x= -438, y = 0)
paddle2 = Paddle( x = 430, y = 0)

ball = Ball()
screen.listen()
screen.onkey(paddle1.paddle_up, "w")
screen.onkey(paddle1.paddle_down, "s")
screen.onkey(paddle2.paddle_up, "Up")
screen.onkey(paddle2.paddle_down, "Down")


while(game_is_on):
    screen.update()   
    time.sleep(0.1)
    ball.move()

screen.exitonclick()

