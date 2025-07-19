import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard=Scoreboard()
car_manager = CarManager()
screen = Screen()
player=Player()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_the_car()
    if player.ycor() > 280:
        scoreboard.increase()
        player.reset_player_position()
        car_manager.increase_speed()
    for car in car_manager.cars:
        if car.distance(player) < 20 :
            scoreboard.game_over()
            game_is_on=False
screen.exitonclick()

