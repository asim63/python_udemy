from turtle import Turtle
FONT = ('Courier', 16 ,'normal')
GF = ('Courier', 20 ,'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
        with open("Day 20/data.txt", mode= 'r') as file:
            self.high_score = file.read()
        super().__init__()
        self.clear()
        self.penup()
        self.teleport(10,270)
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align = ALIGNMENT, font = FONT)
        
        
    def increment(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset_scoreboard(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("Day 20/data.txt", mode= 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()