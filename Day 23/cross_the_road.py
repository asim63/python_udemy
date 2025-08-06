import time
from turtle import Screen
from player import Player
# from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_up,"w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if player.ycor() > 280:
        player.touch_the_line()
        scoreboard.increment()