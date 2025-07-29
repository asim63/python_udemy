import colorgram
from turtle import Turtle, Screen, colormode
import random 

color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219)]
colormode(255)
# colors = colorgram.extract("Day 18\hirst_image_painting.jpg", 25)
# rgb_colour = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     t = (r, g, b)
#     rgb_colour.append(t)
# print(rgb_colour)

t = Turtle()
t.speed(0)
x = -200
y = -225
t.teleport(x,y)
for i in range(10):
    for j in range(10):
        t.pendown()
        my_tuple = random.choice(color_list)
        t.color(my_tuple)
        t.dot(20)
        t.penup()
        t.fd(50)
    t.penup()
    y = y + 50  
    t.setpos(x,y)
    
    
        


screen = Screen()
screen.exitonclick()
