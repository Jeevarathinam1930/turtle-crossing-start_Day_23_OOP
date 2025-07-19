import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.hideturtle()
        self.speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.new_y=random.randint(-50, 50)*5
            car.goto(x=300, y=car.new_y)
            self.cars.append(car)
    def move_the_car(self):
        for i in self.cars:
            i.backward(self.speed)#i is the one car in the list cars
    def increase_speed(self):
        self.speed+=MOVE_INCREMENT



