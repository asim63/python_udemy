from turtle import Turtle, Screen
from paddle import Paddle
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 900, height = 700)
screen.title("Pong Game")
screen.tracer(0)



paddle1 = Paddle( x= -438, y = 0)
paddle2 = Paddle( x = 430, y = 0)
game_is_on = True


while(game_is_on):
    screen.update()
    time.sleep(0.1)    



screen.exitonclick()

