from turtle import Turtle, Screen
import random
color = ['red','orange','yellow','green','blue','purple']
x = -240
y = -120
screen = Screen()
screen.setup(width=500, height = 400)
turtles = []

for i in color:
    j = 1
    t = Turtle()
    t.shape('turtle')
    t.color(i)
    t.penup()
    t.setpos(x,y)
    turtles.append(t)
    y += 50
    

user_bet = screen.textinput(title = "Make your bet", prompt = "which turtle will win the race? Enter a colour: ").lower()
race_is_on  = False
for i in color:
    if user_bet == i:
        race_is_on = True
        
if race_is_on == False:
    print("Invalid colour choose one from Rainbow colour")
while(race_is_on):
    for turtle in turtles:    
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("Your lose")
                
screen.exitonclick()