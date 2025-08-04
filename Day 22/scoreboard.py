from turtle import Turtle
FONT = ('Roboto', 40,'normal')
class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.teleport(x,y)
        self.hideturtle()
        self.color('white')
        self.write(self.score, font = FONT )