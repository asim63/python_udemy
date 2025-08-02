from turtle import Turtle, Screen



#Screen setup
screen = Screen()
screen.setup(width = 600, height =600)
screen.bgcolor('black')
screen.title('Snake Game')

x = 0 
y = 0
for i in range(3):
    t = Turtle()
    t.shape('square')
    t.color('white')
    t.setpos(x,y)
    x += -20

screen.listen()
screen.exitonclick()

