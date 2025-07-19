from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-270,270)
        self.level_no=1#level number
        self.level()
    def level(self):
        self.write(f"LEVEL :{self.level_no}",align="center",font=FONT)
    def increase(self):
        self.level_no+=1
        self.clear()
        self.level()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=FONT)
