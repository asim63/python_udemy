from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
import random
def middle_bar():
    t = Turtle()
    t.teleport(0,-340)
    t.color('white')
    t.shape('square')
    t.shapesize(3,0.6)
    t.setheading(90)
    while(t.ycor() < 350):
        t.fd(40)
        t.penup()
        t.fd(40)
        t.pendown()
        
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 900, height = 700)
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True
middle_bar()
paddle1 = Paddle( x= -438, y = 0)
paddle2 = Paddle( x = 430, y = 0)

ball = Ball()
scoreboard_l = Scoreboard(-75, 290)
scoreboard_r = Scoreboard( 50, 290)

screen.listen()
screen.onkey(paddle1.paddle_up, "w")
screen.onkey(paddle1.paddle_down, "s")
screen.onkey(paddle2.paddle_up, "Up")
screen.onkey(paddle2.paddle_down, "Down")


while(game_is_on):
    screen.update()   
    time.sleep(0.08)
    ball.move()
    
    #detect collision with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()        

    elif paddle1.xcor() - 20 < ball.xcor() < paddle1.xcor() + 20 and paddle1.ycor() -50 < ball.ycor() < paddle1.ycor() + 50:
        if paddle1.ycor() -30 > ball.ycor() < paddle1.ycor() + 30:
            ball.y_move += random.randint(3,6)
        else:
            ball.y_move -= random.randint(0,3)
        ball.bounce_with_paddle()
        
    elif paddle2.xcor() - 20 < ball.xcor() < paddle2.xcor() + 20 and paddle2.ycor() -50 < ball.ycor() < paddle2.ycor() + 50:
        if paddle2.ycor() -30 > ball.ycor() < paddle2.ycor() + 30:
            ball.y_move += random.randint(3,6)
        else:
            ball.y_move -= random.randint(0,3)
        ball.bounce_with_paddle()
     
    elif ball.xcor() > 450:
        ball.reball()
        scoreboard_l.increment()
        
    elif ball.xcor() < -450:
        ball.reball()
        scoreboard_r.increment()
        
        
screen.exitonclick()

