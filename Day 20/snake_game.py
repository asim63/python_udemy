from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#Screen setup
screen = Screen()
screen.setup(width = 600, height =600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()
        snake.extend()
       
    #detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset()
    
    #detect collision with body
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()
screen.exitonclick()

