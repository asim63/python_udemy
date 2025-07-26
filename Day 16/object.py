from turtle import Turtle, Screen

a = Turtle()
print(a)

a.speed = 30

a.shape('turtle')
a.color('cyan3')
a.forward(100)
my_screen = Screen()

# print(my_screen.canvheight)
# print(my_screen.canvwidth)
my_screen.exitonclick()
  