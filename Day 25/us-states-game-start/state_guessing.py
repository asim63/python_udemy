import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"Day 25\us-states-game-start\blank_states_img.gif"

data = pd.read_csv(r"Day 25\us-states-game-start\50_states.csv")

screen.addshape(image)
turtle.shape(image)

game = True
correct_guess = []
while (len(correct_guess) < 50 and game):
    answer_state = screen.textinput(title = f"{len(correct_guess)}/50 States Correct", prompt = "Input state's name").title()
    if answer_state in data.state.values and not answer_state in correct_guess :
        new_data = data[data.state == answer_state]
        print(new_data)
        x = int(new_data.x.iloc[0])
        y = int(new_data.y.iloc[0])
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.teleport(x,y)
        t.write(f"{answer_state}")
        correct_guess.append(answer_state)  
    elif answer_state == "Exit":
        game = False
turtle.mainloop()

