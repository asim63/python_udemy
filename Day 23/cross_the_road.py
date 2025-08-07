import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard= Scoreboard()

screen.listen()
screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_up,"w")
screen.onkeypress(player.move_down,"Down")
screen.onkeypress(player.move_down,"s")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.06)
    screen.update()

    car_manager.create_a_car() 
    car_manager.move_cars()
    
    if player.ycor() > 280:
        player.touch_the_line()
        scoreboard.increment()
        car_manager.level_increase()
    
    #collide with cars
    for car in car_manager.cars:
        if abs(player.ycor() - car.ycor()) < 20 and player.distance(car) < 20:
            screen.clear()
            scoreboard.gameover()
            game_is_on = False
            
screen.exitonclick()
        
    
         