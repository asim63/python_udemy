from turtle import Turtle
FONT = ('Arial', 16 ,'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
        super().__init__()
        self.clear()
        self.penup()
        self.teleport(10,270)
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move = False, align = ALIGNMENT, font = FONT)
        
        
    def increment(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()