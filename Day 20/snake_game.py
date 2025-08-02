from turtle import Turtle, Screen
import time
from snake import Snake

#Screen setup
screen = Screen()
screen.setup(width = 600, height =600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()
x = 0 
y = 0
game_is_on = True
segment = []


snake = Snake()


while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

