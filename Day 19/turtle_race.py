from turtle import Turtle, Screen
color = ['red','orange','yellow','green','blue','purple']
x = -240
y = -120
screen = Screen()
screen.setup(width=500, height = 400)
for i in color:
    j = 1
    t = Turtle()
    t.shape('turtle')
    t.color(i)
    t.penup()
    t.setpos(x,y)
    y += 50
    


# user_bet = screen.textinput(title = "Make your bet", prompt = "which turtle will win the race? Enter a colour: ")
# print(user_bet)
screen.exitonclick()