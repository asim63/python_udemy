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
screen.onkeypress(paddle1.paddle_up, "w")
screen.onkeypress(paddle1.paddle_down, "s")
screen.onkeypress(paddle2.paddle_up, "Up")
screen.onkeypress(paddle2.paddle_down, "Down")


while(game_is_on):
    screen.update()   
    time.sleep(ball.move_speed)
    ball.move()
    
    #detect collision with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()        

    elif paddle1.xcor() - 15 < ball.xcor() < paddle1.xcor() + 15 and ball.distance(paddle1) < 50:
        
        #more deviation up on edges
        if paddle1.ycor() -35 > ball.ycor() < paddle1.ycor() + 35:
            ball.y_move += random.randint(3,6)
        else:
            ball.y_move -= random.randint(0,3)
        ball.bounce_with_paddle()
        
    elif paddle2.xcor() - 15 < ball.xcor() < paddle2.xcor() + 15 and ball.distance(paddle2) < 50:
        #more deviation on edges
        if paddle2.ycor() -35 > ball.ycor() < paddle2.ycor() + 35:
            if ball.y_move < 0:
                ball.y_move -= random.randint(3,6)
            else:
                ball.y_move += random.randint(3,6)
        else:
            if ball.y_move < 0:
                ball.y_move += random.randint(0,3)
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

