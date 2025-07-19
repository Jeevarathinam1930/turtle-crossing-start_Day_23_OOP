from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
    def move(self):
        self.goto(x=0,y=self.ycor()+MOVE_DISTANCE)#to move forward
    def reset_player_position(self):
        self.goto(STARTING_POSITION)
