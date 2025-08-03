from turtle import Turtle
FONT = ('Courier', 16 ,'normal')
GF = ('Courier', 20 ,'normal')
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
        self.write(f"Score = {self.score}", align = ALIGNMENT, font = FONT)
        
        
    def increment(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
        
    def gameover(self):
        self.teleport(0,0)
        self.write("GAME OVER!!!", align = ALIGNMENT, font = GF)